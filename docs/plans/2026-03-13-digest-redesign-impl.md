# Digest Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the single digest script with two subcommands (`ops` and
`changelog`) that produce separate operator reports and public changelogs,
fix cost tracking and pipeline status bugs, and add trend data.

**Architecture:** One script (`scripts/digest.py`) with shared helpers and two
formatters. Ops reports go to `docs/ops/`, changelogs to `docs/changelog/`.
Astro renders both via separate content collections. GitHub Actions run each
on independent schedules.

**Tech Stack:** Python 3.11+ (PEP 723 inline deps), GitHub Actions, Astro 5,
`gh` CLI, `python-frontmatter`.

**Design doc:** `docs/plans/2026-03-13-digest-redesign-design.md`

---

## Task 1: Rewrite digest script with `ops` and `changelog` subcommands

Rewrites `scripts/digest.py` from scratch. Fixes all data bugs (cost tracking,
duplicates, pipeline noise) and adds trend data.

**Files:**
- Rewrite: `scripts/digest.py`
- Create: `docs/ops/.gitkeep`
- Create: `docs/changelog/.gitkeep`
- Delete contents: `docs/digests/` (remove old files)

**Step 1: Create new output directories**

```bash
mkdir -p docs/ops docs/changelog
touch docs/ops/.gitkeep docs/changelog/.gitkeep
```

**Step 2: Rewrite the digest script**

Rewrite `scripts/digest.py` with this structure:

```python
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


def stats_from_issues(since: str) -> list[dict]:
    """Parse ## stats: lines from issue comments since a date.

    Queries all import-project issues and parses structured stats
    comments posted by agents.
    """
    issues_raw = gh(
        "issue", "list", "-R", REPO,
        "--label", "import-project",
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

    # 7-day activity table
    week_start = target_date - timedelta(days=6)
    daily_stats = []
    for i in range(7):
        d = week_start + timedelta(days=i)
        day_slugs = entries_added_on(d)
        day_stats = stats_from_issues(d.isoformat())
        day_cost = sum(s["cost"] for s in day_stats)
        daily_stats.append({"date": d, "added": len(day_slugs), "cost": day_cost})

    total_added = sum(ds["added"] for ds in daily_stats)
    total_cost = sum(ds["cost"] for ds in daily_stats)

    # Today's stats for cost
    today_stats = stats_from_issues(target_date.isoformat())
    today_cost = sum(s["cost"] for s in today_stats)

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
    lines.append(f"- **${today_cost:.2f} spent** today (${total_cost:.2f} this week)")
    lines.append("")

    # 7-Day Activity
    lines.append("## 7-Day Activity")
    lines.append("| Date | Added | Cost |")
    lines.append("|------|-------|------|")
    for ds in daily_stats:
        lines.append(f"| {ds['date'].strftime('%m-%d')} | {ds['added']} | ${ds['cost']:.2f} |")
    lines.append(f"| **Total** | **{total_added}** | **${total_cost:.2f}** |")
    lines.append("")

    # Costs by Agent (all week)
    all_week_stats = []
    for ds in daily_stats:
        all_week_stats.extend(stats_from_issues(ds["date"].isoformat()))
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
```

**Important changes from the old script:**
- `entries_added_on()` uses frontmatter `created` field, not PR merge dates — eliminates duplicates
- `stats_from_issues()` parses JSON in Python instead of jq — fixes the date filter bug
- `pipeline_status()` skips projects with 0 sub-issues — eliminates noise
- `kaizen_backlog()` empty state includes a "File one" link
- Ops report has "At a Glance" with deltas and "7-Day Activity" table

**Step 3: Delete old digest files and directory**

```bash
rm -rf docs/digests
```

**Step 4: Test the ops report**

```bash
uv run scripts/digest.py ops --date 2026-03-13
```

Expected: Creates `docs/ops/2026-03-13.md` with At a Glance section showing
entry count, deltas, and cost data. Pipeline Status shows only projects with
sub-issues.

**Step 5: Test the changelog**

```bash
uv run scripts/digest.py changelog --date 2026-03-13
```

Expected: Creates `docs/changelog/2026-W11.md` with entry count and flat list
of new entries. No costs, no pipeline status, no operator internals.

**Step 6: Generate retroactive reports**

```bash
for d in 2026-03-07 2026-03-08 2026-03-09 2026-03-10 2026-03-11 2026-03-12 2026-03-13; do
  uv run scripts/digest.py ops --date "$d" 2>&1 | head -1
done
uv run scripts/digest.py changelog --date 2026-03-07
uv run scripts/digest.py changelog --date 2026-03-13
```

Expected: 7 ops reports in `docs/ops/`, 2 changelogs in `docs/changelog/`.

**Step 7: Commit**

```bash
git add scripts/digest.py docs/ops/ docs/changelog/
git rm -rf docs/digests/ 2>/dev/null || true
git add -u docs/digests/
git commit -m "feat: rewrite digest as ops + changelog subcommands

Ops report: daily, with at-a-glance deltas, 7-day activity table,
cost breakdown by agent, pipeline status (project-level only).
Changelog: weekly, public-friendly, entries grouped by created date.

Fixes: cost tracking date filter, duplicate entries across days,
noisy pipeline table, PR-centric language."
```

**Human verification:** Open `docs/ops/2026-03-13.md` and confirm: At a Glance
shows entry count with delta, 7-Day Activity has 7 rows, Costs by Agent shows
real data from issue comments, Pipeline Status shows only projects with
sub-issues.

---

## Task 2: Update site collections and pages

Replace the `digests` Astro collection with `changelog` and `ops` collections.
Rewrite the changelog page, create the ops page, update nav.

**Files:**
- Modify: `site/src/content.config.ts`
- Rewrite: `site/src/pages/changelog.astro`
- Create: `site/src/pages/ops.astro`
- Modify: `site/src/layouts/Base.astro:323-327` (add ops link to footer)

**Step 1: Update content config**

In `site/src/content.config.ts`, replace the `digests` collection with two
new collections:

```typescript
const changelog = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "../docs/changelog" }),
  schema: z.object({
    date: z.coerce.date(),
    type: z.literal("changelog"),
    week: z.string(),
  }),
});

const ops = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "../docs/ops" }),
  schema: z.object({
    date: z.coerce.date(),
    type: z.literal("ops"),
  }),
});

export const collections = { mappings, frames, categories, changelog, ops };
```

Remove the `digests` collection entirely.

**Step 2: Rewrite the changelog page**

Replace `site/src/pages/changelog.astro` with:

```astro
---
import Base from "@/layouts/Base.astro";
import { getCollection, render } from "astro:content";

const entries = await getCollection("changelog");
const sorted = entries
  .sort((a, b) => b.data.date.getTime() - a.data.date.getTime())
  .slice(0, 20);
---

<Base title="Changelog" description="Weekly updates from the Metaphorex catalog">
  <article>
    <h1>Changelog</h1>
    <p>Weekly updates showing new entries added to the catalog.</p>

    {sorted.map(async (entry) => {
      const { Content } = await render(entry);
      return (
        <details>
          <summary>
            <strong>{entry.data.week}</strong>
          </summary>
          <Content />
        </details>
      );
    })}
  </article>
</Base>
```

**Step 3: Create the ops page**

Create `site/src/pages/ops.astro`:

```astro
---
import Base from "@/layouts/Base.astro";
import { getCollection, render } from "astro:content";

const entries = await getCollection("ops");
const sorted = entries
  .sort((a, b) => b.data.date.getTime() - a.data.date.getTime())
  .slice(0, 14);
---

<Base title="Ops Reports" description="Daily operator reports from the Metaphorex pipeline">
  <article>
    <h1>Ops Reports</h1>
    <p>Daily pipeline reports: costs, growth trends, and project status.</p>

    {sorted.map(async (entry) => {
      const { Content } = await render(entry);
      const label = entry.data.date.toISOString().split("T")[0];
      return (
        <details>
          <summary>
            <strong>{label}</strong>
          </summary>
          <Content />
        </details>
      );
    })}
  </article>
</Base>
```

**Step 4: Update nav — add ops link to footer**

In `site/src/layouts/Base.astro`, replace the footer (line 323-326):

```html
    <footer>
      Metaphorex {corpusVersion} &middot;
      <a href="https://github.com/metaphorex/metaphorex">GitHub</a> &middot;
      <a href="/ops/">Ops</a> &middot;
      CC BY-SA 4.0
    </footer>
```

The main nav already has Changelog — leave it there. Ops is less prominent
in the footer.

**Step 5: Build and verify**

```bash
cd site && bunx astro build
```

Expected: Build succeeds. Check that `dist/changelog/index.html` and
`dist/ops/index.html` exist.

**Step 6: Commit**

```bash
git add site/src/content.config.ts site/src/pages/changelog.astro \
  site/src/pages/ops.astro site/src/layouts/Base.astro
git commit -m "feat: split site into changelog (public) and ops (operator) pages

Changelog shows weekly roll-ups of new entries.
Ops shows daily reports with costs, trends, and pipeline status.
Ops linked from footer, changelog stays in main nav."
```

**Human verification:** Run `cd site && bunx astro dev` and visit:
- `localhost:4321/changelog/` — should show weekly entries only, clean language
- `localhost:4321/ops/` — should show daily reports with At a Glance, 7-Day
  Activity, Costs by Agent tables

---

## Task 3: Update GitHub Actions workflows

Rename workflows to match new subcommands.

**Files:**
- Rename: `.github/workflows/daily-digest.yml` → `.github/workflows/daily-ops.yml`
- Rename: `.github/workflows/weekly-digest.yml` → `.github/workflows/weekly-changelog.yml`
- Modify: `.github/workflows/deploy-site.yml:3-9` (update path triggers)

**Step 1: Rename and update daily workflow**

Delete `.github/workflows/daily-digest.yml` and create
`.github/workflows/daily-ops.yml`:

```yaml
name: Daily ops report

on:
  schedule:
    - cron: "0 9 * * *"
  workflow_dispatch: {}

permissions:
  contents: write
  issues: read
  pull-requests: read

jobs:
  ops:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: astral-sh/setup-uv@v5

      - name: Generate daily ops report
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: uv run scripts/digest.py ops

      - name: Commit and push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add docs/ops/
          git diff --cached --quiet && echo "No changes to commit" && exit 0
          git commit -m "chore: daily ops report $(date -u +%Y-%m-%d)"
          git push
```

**Step 2: Rename and update weekly workflow**

Delete `.github/workflows/weekly-digest.yml` and create
`.github/workflows/weekly-changelog.yml`:

```yaml
name: Weekly changelog

on:
  schedule:
    - cron: "0 6 * * 3"
  workflow_dispatch: {}

permissions:
  contents: write
  issues: read
  pull-requests: read

jobs:
  changelog:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: astral-sh/setup-uv@v5

      - name: Generate weekly changelog
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: uv run scripts/digest.py changelog

      - name: Commit and push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add docs/changelog/
          git diff --cached --quiet && echo "No changes to commit" && exit 0
          git commit -m "chore: weekly changelog $(date -u +%Y-W%V)"
          git push
```

**Step 3: Update deploy trigger paths**

In `.github/workflows/deploy-site.yml`, update the `paths:` section:

```yaml
  push:
    branches: [main]
    paths:
      - "docs/ops/**"
      - "docs/changelog/**"
      - "catalog/**"
```

(Replace `docs/digests/**` with the two new paths.)

**Step 4: Commit**

```bash
git rm .github/workflows/daily-digest.yml .github/workflows/weekly-digest.yml
git add .github/workflows/daily-ops.yml .github/workflows/weekly-changelog.yml \
  .github/workflows/deploy-site.yml
git commit -m "feat: rename digest workflows to daily-ops and weekly-changelog

Daily ops report at 09:00 UTC, weekly changelog Wednesday 06:00 UTC.
Deploy site triggers on docs/ops/ and docs/changelog/ changes."
```

**Human verification:** After pushing, go to the repo's Actions tab and
confirm the three workflows appear: "Daily ops report", "Weekly changelog",
"Deploy site". Manually trigger "Daily ops report" via workflow_dispatch and
confirm it generates and commits a report.

---

## Dependencies and Execution Order

```
Task 1 — standalone (script rewrite + data)
Task 2 — depends on Task 1 (needs new output dirs with content)
Task 3 — depends on Task 1 (references new subcommand names)
```

**Recommended:** Execute Task 1 first (it's the big one), then Tasks 2 + 3
in parallel.

**Note on ops report performance:** The 7-Day Activity section calls
`stats_from_issues()` once per day in the lookback window. Each call hits the
GitHub API for all import-project issue comments. For 7 days × ~10 issues =
~70 API calls. This is fine for a daily cron job but slow for local testing.
For retroactive generation of all 7 days, expect ~5 minutes. If this becomes
a problem, the stats parsing can be optimized to fetch all comments once and
filter in Python — but don't optimize prematurely.
