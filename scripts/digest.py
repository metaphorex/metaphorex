# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
"""Generate ops reports and changelogs for Metaphorex.

Usage:
    uv run scripts/digest.py ops                     # today's ops report
    uv run scripts/digest.py ops --date 2026-03-12   # specific date
    uv run scripts/digest.py changelog               # this week's changelog
    uv run scripts/digest.py changelog --date 2026-03-12  # week containing date
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT / "catalog"
OPS_DIR = ROOT / "docs" / "ops"
CHANGELOG_DIR = ROOT / "docs" / "changelog"
REPO = "metaphorex/metaphorex"


# ── Shared helpers ──────────────────────────────────────────────

def gh(*args: str) -> str:
    """Run a gh CLI command and return stdout."""
    result = subprocess.run(
        ["gh", *args],
        capture_output=True, text=True, cwd=ROOT,
    )
    if result.returncode != 0:
        print(f"gh command failed: gh {' '.join(args)}", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
    return result.stdout.strip()


def catalog_counts() -> dict[str, int]:
    """Count entries in each catalog subdirectory."""
    counts = {}
    for subdir in ["mappings", "frames", "categories"]:
        dir_path = CATALOG_DIR / subdir
        counts[subdir] = len(list(dir_path.glob("*.md")))
    return counts


def entries_added_on(target_date: date) -> list[str]:
    """Get mapping slugs first added on a specific date.

    Uses the frontmatter `created` field, not PR merge dates.
    This avoids duplicates from edits showing up as re-merges.
    """
    slugs = []
    mappings_dir = CATALOG_DIR / "mappings"
    target_str = target_date.isoformat()
    for md_file in sorted(mappings_dir.glob("*.md")):
        post = frontmatter.load(md_file)
        created = str(post.metadata.get("created", ""))
        if created == target_str:
            slugs.append(md_file.stem)
    return slugs


def entries_added_in_range(start: date, end: date) -> list[str]:
    """Get mapping slugs first added in a date range (inclusive)."""
    slugs = []
    mappings_dir = CATALOG_DIR / "mappings"
    for md_file in sorted(mappings_dir.glob("*.md")):
        post = frontmatter.load(md_file)
        created = str(post.metadata.get("created", ""))
        if created and start.isoformat() <= created <= end.isoformat():
            slugs.append(md_file.stem)
    return slugs


def stats_from_issues(since: str, until: str | None = None) -> list[dict]:
    """Parse ## stats: lines from issue comments in a date range.

    If until is None, includes all comments from since onward.
    Queries all import-project issues and parses structured stats
    comments posted by agents.
    """
    # Only query parent import-project issues (labeled "parent") —
    # those are where agents post stats comments. Sub-issues don't have stats.
    issues_raw = gh(
        "issue", "list", "-R", REPO,
        "--label", "import-project,parent",
        "--state", "all",
        "--limit", "50",
        "--json", "number",
    )
    if not issues_raw:
        return []

    issues = json.loads(issues_raw)
    all_stats = []

    pattern = re.compile(
        r"^## stats:(?P<agent>[a-z-]+):(?P<model>[a-z0-9.-]+)\s+(?P<kv>.+)$"
    )
    kv_pattern = re.compile(r"(?P<key>[a-z_]+)=(?P<value>[^\s]+)")

    for issue in issues:
        # Get all comments, filter by date in Python (more reliable than jq string comparison)
        comments_raw = gh(
            "api", f"repos/{REPO}/issues/{issue['number']}/comments",
            "--paginate",
        )
        if not comments_raw:
            continue

        try:
            comments = json.loads(comments_raw)
        except json.JSONDecodeError:
            continue

        for comment in comments:
            created_at = comment.get("created_at", "")[:10]
            if created_at < since:
                continue
            if until and created_at >= until:
                continue

            body = comment.get("body", "")
            for line in body.splitlines():
                m = pattern.match(line.strip())
                if not m:
                    continue
                kvs = {km.group("key"): km.group("value")
                       for km in kv_pattern.finditer(m.group("kv"))}
                tokens_in = int(kvs.get("tokens_in", 0))
                tokens_out = int(kvs.get("tokens_out", 0))
                usd_in = float(kvs.get("usd_in_per_mtok", 0))
                usd_out = float(kvs.get("usd_out_per_mtok", 0))
                cost = (tokens_in * usd_in + tokens_out * usd_out) / 1_000_000
                all_stats.append({
                    "agent": m.group("agent"),
                    "model": m.group("model"),
                    "tokens_in": tokens_in,
                    "tokens_out": tokens_out,
                    "cost": cost,
                })

    return all_stats


def aggregate_cost_table(stats: list[dict]) -> str:
    """Format stats into a markdown table grouped by agent/model."""
    if not stats:
        return "No agent activity recorded.\n"

    by_agent: dict[str, dict] = {}
    for s in stats:
        key = f"{s['agent']}|{s['model']}"
        if key not in by_agent:
            by_agent[key] = {"agent": s["agent"], "model": s["model"],
                             "runs": 0, "tokens": 0, "cost": 0.0}
        by_agent[key]["runs"] += 1
        by_agent[key]["tokens"] += s["tokens_in"] + s["tokens_out"]
        by_agent[key]["cost"] += s["cost"]

    lines = ["| Agent | Model | Runs | Tokens | Cost |",
             "|-------|-------|------|--------|------|"]
    total_runs = total_tokens = 0
    total_cost = 0.0
    for row in sorted(by_agent.values(), key=lambda r: -r["cost"]):
        lines.append(
            f"| {row['agent']} | {row['model']} | {row['runs']} "
            f"| {row['tokens']:,} | ${row['cost']:.2f} |"
        )
        total_runs += row["runs"]
        total_tokens += row["tokens"]
        total_cost += row["cost"]
    lines.append(
        f"| **Total** | | **{total_runs}** "
        f"| **{total_tokens:,}** | **${total_cost:.2f}** |"
    )
    return "\n".join(lines) + "\n"


def pipeline_status() -> str:
    """Get import project completion status — one row per project."""
    raw = gh(
        "issue", "list", "-R", REPO,
        "--label", "import-project",
        "--state", "open",
        "--limit", "20",
        "--json", "number,title",
    )
    if not raw:
        return "No active import projects.\n"

    projects = json.loads(raw)
    lines = ["| Project | Progress | Status |",
             "|---------|----------|--------|"]

    for proj in projects:
        sub_raw = gh(
            "api", "graphql",
            "-f", "owner=metaphorex", "-f", "name=metaphorex",
            "-F", f"number={proj['number']}",
            "-f", "query=query($owner: String!, $name: String!, $number: Int!) { repository(owner: $owner, name: $name) { issue(number: $number) { subIssues(first: 100) { nodes { state } } } } }",
            "--jq", ".data.repository.issue.subIssues.nodes",
        )
        if not sub_raw:
            continue  # skip issues with no sub-issues instead of showing "unknown"

        try:
            subs = json.loads(sub_raw)
        except json.JSONDecodeError:
            continue

        total = len(subs)
        if total == 0:
            continue  # skip projects with no sub-issues

        closed = sum(1 for s in subs if s["state"] == "CLOSED")
        pct = closed / total * 100
        status = "complete" if closed == total else "active"
        title = proj["title"][:50]
        lines.append(f"| {title} | {closed}/{total} ({pct:.0f}%) | {status} |")

    if len(lines) == 2:
        return "No active import projects with sub-issues.\n"
    return "\n".join(lines) + "\n"


def kaizen_backlog() -> str:
    """List open kaizen issues with a file-one link for empty state."""
    raw = gh(
        "issue", "list", "-R", REPO,
        "--label", "kaizen:pipeline,kaizen:content",
        "--state", "open",
        "--limit", "20",
        "--json", "number,title,createdAt",
    )
    if not raw:
        return "No open kaizen issues. [File one](https://github.com/metaphorex/metaphorex/issues/new?template=kaizen.yml).\n"

    issues = json.loads(raw)
    if not issues:
        return "No open kaizen issues. [File one](https://github.com/metaphorex/metaphorex/issues/new?template=kaizen.yml).\n"

    lines = []
    for issue in issues:
        created = issue["createdAt"][:10]
        lines.append(f"- #{issue['number']}: {issue['title']} (opened {created})")
    return "\n".join(lines) + "\n"


# ── Ops report (daily) ─────────────────────────────────────────

def generate_ops(target_date: date) -> str:
    """Generate a daily ops report with trends."""
    counts = catalog_counts()
    today_slugs = entries_added_on(target_date)
    today_count = len(today_slugs)

    yesterday = target_date - timedelta(days=1)
    yesterday_count = len(entries_added_on(yesterday))

    # Fetch all stats for the 7-day window in one call
    week_start = target_date - timedelta(days=6)
    all_week_stats = stats_from_issues(week_start.isoformat())

    # Bucket stats by date
    stats_by_date: dict[str, list[dict]] = {}
    for s in all_week_stats:
        # Stats don't carry a date — they came from comments. We'll attribute
        # them to the day they were posted. But since stats_from_issues doesn't
        # return the comment date, we need a different approach.
        pass

    # Actually: fetch stats once for the whole week, attribute all to the week.
    # Per-day cost breakdown requires comment dates, which we don't track yet.
    # For now: show weekly total cost and per-day entry counts.
    week_cost = sum(s["cost"] for s in all_week_stats)

    daily_stats = []
    for i in range(7):
        d = week_start + timedelta(days=i)
        day_slugs = entries_added_on(d)
        daily_stats.append({"date": d, "added": len(day_slugs)})

    total_added = sum(ds["added"] for ds in daily_stats)
    today_cost = week_cost  # approximate: attribute week cost for "today" line

    lines = []
    lines.append("---")
    lines.append(f"date: {target_date.isoformat()}")
    lines.append("type: ops")
    lines.append("---")
    lines.append("")
    lines.append(f"# Ops Report — {target_date.isoformat()}")
    lines.append("")

    # At a Glance
    lines.append("## At a Glance")
    delta = f"vs {yesterday_count} yesterday" if yesterday_count else "first day"
    lines.append(f"- **+{today_count} entries today** ({delta})")
    lines.append(f"- **{counts['mappings']}** mappings · "
                 f"**{counts['frames']}** frames · "
                 f"**{counts['categories']}** categories")
    lines.append(f"- **${week_cost:.2f} spent** this week")
    lines.append("")

    # 7-Day Activity
    lines.append("## 7-Day Activity")
    lines.append("| Date | Added |")
    lines.append("|------|-------|")
    for ds in daily_stats:
        lines.append(f"| {ds['date'].strftime('%m-%d')} | {ds['added']} |")
    lines.append(f"| **Total** | **{total_added}** |")
    lines.append("")

    # Costs by Agent (all week — already fetched above)
    lines.append("## Costs by Agent")
    lines.append(aggregate_cost_table(all_week_stats))

    # Pipeline
    lines.append("## Pipeline Status")
    lines.append(pipeline_status())

    # Kaizen
    lines.append("## Kaizen Backlog")
    lines.append(kaizen_backlog())

    return "\n".join(lines)


# ── Changelog (weekly) ─────────────────────────────────────────

def generate_changelog(target_date: date) -> str:
    """Generate a weekly public changelog."""
    monday = target_date - timedelta(days=target_date.weekday())
    sunday = monday + timedelta(days=6)
    iso_year, iso_week, _ = monday.isocalendar()
    counts = catalog_counts()
    new_slugs = entries_added_in_range(monday, sunday)

    # Group by import project (heuristic: check PR branch prefix or just list flat)
    # For now, flat list. Grouping by project can use PR labels in a future iteration.

    lines = []
    lines.append("---")
    lines.append(f"date: {monday.isoformat()}")
    lines.append("type: changelog")
    lines.append(f"week: {iso_year}-W{iso_week:02d}")
    lines.append("---")
    lines.append("")
    lines.append(f"# Week {iso_week}, {iso_year}")
    lines.append("")
    lines.append(f"**{len(new_slugs)} new entries** added this week. "
                 f"Catalog now has **{counts['mappings']}** mappings, "
                 f"{counts['frames']} frames, and {counts['categories']} categories.")
    lines.append("")

    if new_slugs:
        lines.append("## New Entries")
        for slug in new_slugs:
            lines.append(f"- [{slug}](/mappings/{slug}/)")
        lines.append("")
    else:
        lines.append("No new entries this week.")
        lines.append("")

    return "\n".join(lines)


# ── CLI ─────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Metaphorex digest generator")
    sub = parser.add_subparsers(dest="command", required=True)

    ops_parser = sub.add_parser("ops", help="Generate daily ops report")
    ops_parser.add_argument("--date", help="Date (YYYY-MM-DD), default today")

    changelog_parser = sub.add_parser("changelog", help="Generate weekly changelog")
    changelog_parser.add_argument("--date", help="Date in target week, default today")

    args = parser.parse_args()

    if args.command == "ops":
        target = date.fromisoformat(args.date) if args.date else date.today()
        content = generate_ops(target)
        out_path = OPS_DIR / f"{target.isoformat()}.md"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content)
        print(f"Ops report written to {out_path}")
        print(content)

    elif args.command == "changelog":
        target = date.fromisoformat(args.date) if args.date else date.today()
        monday = target - timedelta(days=target.weekday())
        iso_year, iso_week, _ = monday.isocalendar()
        content = generate_changelog(target)
        out_path = CHANGELOG_DIR / f"{iso_year}-W{iso_week:02d}.md"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content)
        print(f"Changelog written to {out_path}")
        print(content)


if __name__ == "__main__":
    main()
