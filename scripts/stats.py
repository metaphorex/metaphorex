#!/usr/bin/env python3
"""Parse and summarize ## stats: lines from GitHub issue comments.

Usage:
    # Summarize costs for an issue
    gh api repos/metaphorex/metaphorex/issues/3/comments --paginate \
        --jq '.[].body' | python3 scripts/stats.py summary

    # Include project timeline (start-to-finish elapsed time)
    gh api repos/metaphorex/metaphorex/issues/3/comments --paginate \
        --jq '.[].body' | python3 scripts/stats.py summary \
        --repo metaphorex/metaphorex --issue 3

    # Emit a stats line (for agents to call)
    python3 scripts/stats.py emit --agent smelter --model haiku \
        --tokens-in 20000 --tokens-out 3022 --ms 111000 \
        --prs 52,53 --issues 21,22

    # Validate stats lines
    echo '## stats:smelter:haiku tokens_in=20000 ...' | python3 scripts/stats.py validate
"""

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime

# Current Anthropic API prices per million tokens (as of 2026-03-10)
# https://docs.anthropic.com/en/docs/about-claude/pricing
PRICES: dict[str, tuple[float, float]] = {
    # model_key: (input_usd_per_mtok, output_usd_per_mtok)
    "opus": (15.00, 75.00),
    "sonnet": (3.00, 15.00),
    "haiku": (0.80, 4.00),
}

STATS_PATTERN = re.compile(
    r"^## stats:(?P<agent>[a-z-]+):(?P<model>[a-z0-9.-]+)\s+(?P<kv>.+)$"
)

KV_PATTERN = re.compile(r"(?P<key>[a-z_]+)=(?P<value>[^\s]+)")


@dataclass
class StatsLine:
    agent: str
    model: str
    tokens_in: int = 0
    tokens_out: int = 0
    ms: int = 0
    usd_in_per_mtok: float = 0.0
    usd_out_per_mtok: float = 0.0
    prs: list[int] = field(default_factory=list)
    issues: list[int] = field(default_factory=list)

    @property
    def cost_usd(self) -> float:
        return (
            self.tokens_in * self.usd_in_per_mtok / 1_000_000
            + self.tokens_out * self.usd_out_per_mtok / 1_000_000
        )

    @property
    def total_tokens(self) -> int:
        return self.tokens_in + self.tokens_out


def parse_line(line: str) -> StatsLine | None:
    """Parse a single ## stats: line into a StatsLine."""
    m = STATS_PATTERN.match(line.strip())
    if not m:
        return None

    agent = m.group("agent")
    model = m.group("model")
    kv_str = m.group("kv")

    kvs = {km.group("key"): km.group("value") for km in KV_PATTERN.finditer(kv_str)}

    def int_list(val: str) -> list[int]:
        return [int(x) for x in val.split(",") if x]

    return StatsLine(
        agent=agent,
        model=model,
        tokens_in=int(kvs.get("tokens_in", 0)),
        tokens_out=int(kvs.get("tokens_out", 0)),
        ms=int(kvs.get("ms", 0)),
        usd_in_per_mtok=float(kvs.get("usd_in_per_mtok", 0)),
        usd_out_per_mtok=float(kvs.get("usd_out_per_mtok", 0)),
        prs=int_list(kvs.get("prs", "")),
        issues=int_list(kvs.get("issues", "")),
    )


def parse_comments(text: str) -> list[StatsLine]:
    """Extract all stats lines from comment text (may contain non-stats lines)."""
    results = []
    for line in text.splitlines():
        parsed = parse_line(line)
        if parsed:
            results.append(parsed)
    return results


def format_line(s: StatsLine) -> str:
    """Format a StatsLine back into the canonical ## stats: format."""
    parts = [
        f"## stats:{s.agent}:{s.model}",
        f"tokens_in={s.tokens_in}",
        f"tokens_out={s.tokens_out}",
        f"ms={s.ms}",
        f"usd_in_per_mtok={s.usd_in_per_mtok:.2f}",
        f"usd_out_per_mtok={s.usd_out_per_mtok:.2f}",
    ]
    if s.prs:
        parts.append(f"prs={','.join(str(p) for p in s.prs)}")
    if s.issues:
        parts.append(f"issues={','.join(str(i) for i in s.issues)}")
    return " ".join(parts)


def summarize(lines: list[StatsLine]) -> str:
    """Produce a summary report from a list of StatsLines."""
    if not lines:
        return "No stats lines found."

    by_agent: dict[str, list[StatsLine]] = {}
    for line in lines:
        by_agent.setdefault(line.agent, []).append(line)

    total_cost = sum(l.cost_usd for l in lines)
    total_tokens = sum(l.total_tokens for l in lines)
    total_ms = sum(l.ms for l in lines)

    out = []
    out.append("## stats:summary")
    out.append("")
    out.append(f"Total runs: {len(lines)}")
    out.append(f"Total tokens: {total_tokens:,}")
    out.append(f"Total cost: ${total_cost:.2f}")
    out.append(f"Total time: {total_ms / 1000:.0f}s ({total_ms / 60000:.1f}m)")
    out.append("")

    out.append("| Agent | Model | Runs | Tokens In | Tokens Out | Cost | Time |")
    out.append("|-------|-------|------|-----------|------------|------|------|")

    for agent, agent_lines in sorted(by_agent.items()):
        by_model: dict[str, list[StatsLine]] = {}
        for l in agent_lines:
            by_model.setdefault(l.model, []).append(l)

        for model, model_lines in sorted(by_model.items()):
            runs = len(model_lines)
            t_in = sum(l.tokens_in for l in model_lines)
            t_out = sum(l.tokens_out for l in model_lines)
            cost = sum(l.cost_usd for l in model_lines)
            ms = sum(l.ms for l in model_lines)
            out.append(
                f"| {agent} | {model} | {runs} | {t_in:,} | {t_out:,} "
                f"| ${cost:.2f} | {ms / 1000:.0f}s |"
            )

    out.append("")
    out.append(f"Prices captured at time of each run (baked into stats lines).")

    return "\n".join(out)


def cmd_emit(args: argparse.Namespace) -> None:
    """Emit a stats line to stdout."""
    model_key = args.model
    if model_key not in PRICES:
        print(f"Unknown model: {model_key}. Known: {', '.join(PRICES)}", file=sys.stderr)
        sys.exit(1)

    price_in, price_out = PRICES[model_key]

    s = StatsLine(
        agent=args.agent,
        model=model_key,
        tokens_in=args.tokens_in,
        tokens_out=args.tokens_out,
        ms=args.ms,
        usd_in_per_mtok=price_in,
        usd_out_per_mtok=price_out,
        prs=[int(x) for x in args.prs.split(",") if x] if args.prs else [],
        issues=[int(x) for x in args.issues.split(",") if x] if args.issues else [],
    )
    print(format_line(s))


def query_project_timeline(repo: str, issue: int) -> dict | None:
    """Query GitHub for project start/end timestamps."""
    try:
        # Get parent issue created_at
        result = subprocess.run(
            ["gh", "api", f"repos/{repo}/issues/{issue}",
             "--jq", ".created_at"],
            capture_output=True, text=True, check=True,
        )
        created_at = result.stdout.strip()

        # Get all sub-issues (issues that reference this parent)
        # We use the comments to find stats lines with issue numbers,
        # then check those issues for closed_at
        result = subprocess.run(
            ["gh", "issue", "list", "-R", repo,
             "--label", "import-project", "--state", "all",
             "--json", "number,title,state,closedAt,createdAt",
             "--limit", "200"],
            capture_output=True, text=True, check=True,
        )
        sub_issues = json.loads(result.stdout)

        # Filter to sub-issues (exclude parent itself)
        subs = [s for s in sub_issues if s["number"] != issue]

        total = len(subs)
        closed = [s for s in subs if s["state"] == "CLOSED"]
        open_issues = [s for s in subs if s["state"] == "OPEN"]

        # Find latest closed_at among closed sub-issues
        latest_close = None
        for s in closed:
            if s.get("closedAt"):
                dt = datetime.fromisoformat(s["closedAt"].replace("Z", "+00:00"))
                if latest_close is None or dt > latest_close:
                    latest_close = dt

        start = datetime.fromisoformat(created_at.replace("Z", "+00:00"))

        return {
            "created_at": start,
            "latest_close": latest_close,
            "total_sub_issues": total,
            "closed": len(closed),
            "open": len(open_issues),
        }
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        return None


def cmd_summary(args: argparse.Namespace) -> None:
    """Read stdin, parse stats lines, print summary."""
    text = sys.stdin.read()
    lines = parse_comments(text)
    print(summarize(lines))

    # If --repo and --issue provided, add project timeline
    if hasattr(args, "repo") and args.repo and args.issue:
        timeline = query_project_timeline(args.repo, args.issue)
        if timeline:
            print()
            print("## stats:timeline")
            print()
            start = timeline["created_at"]
            print(f"Project started: {start.strftime('%Y-%m-%d %H:%M UTC')}")

            total = timeline["total_sub_issues"]
            closed = timeline["closed"]
            open_n = timeline["open"]
            print(f"Sub-issues: {closed}/{total} closed, {open_n} open")

            if timeline["latest_close"]:
                end = timeline["latest_close"]
                elapsed = end - start
                days = elapsed.days
                hours = elapsed.seconds // 3600
                print(f"Latest close: {end.strftime('%Y-%m-%d %H:%M UTC')}")
                print(f"Elapsed: {days}d {hours}h")

                if closed == total:
                    print(f"Status: COMPLETE ({days}d {hours}h start to finish)")
                else:
                    pct = closed / total * 100 if total else 0
                    print(f"Status: {pct:.0f}% complete")


def cmd_validate(args: argparse.Namespace) -> None:
    """Read stdin, validate each line is parseable."""
    text = sys.stdin.read()
    errors = 0
    for i, line in enumerate(text.splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        parsed = parse_line(line)
        if parsed is None:
            print(f"FAIL line {i}: could not parse: {line}", file=sys.stderr)
            errors += 1
        else:
            print(f"OK line {i}: agent={parsed.agent} model={parsed.model} "
                  f"tokens={parsed.total_tokens:,} cost=${parsed.cost_usd:.4f}")
    sys.exit(1 if errors else 0)


def main() -> None:
    parser = argparse.ArgumentParser(description="Metaphorex stats accounting")
    sub = parser.add_subparsers(dest="command", required=True)

    emit = sub.add_parser("emit", help="Emit a stats line")
    emit.add_argument("--agent", required=True)
    emit.add_argument("--model", required=True, choices=list(PRICES))
    emit.add_argument("--tokens-in", type=int, required=True)
    emit.add_argument("--tokens-out", type=int, required=True)
    emit.add_argument("--ms", type=int, required=True)
    emit.add_argument("--prs", default="")
    emit.add_argument("--issues", default="")

    summary_parser = sub.add_parser("summary", help="Summarize stats from stdin")
    summary_parser.add_argument("--repo", help="GitHub repo (e.g. metaphorex/metaphorex)")
    summary_parser.add_argument("--issue", type=int, help="Parent issue number")
    sub.add_parser("validate", help="Validate stats lines from stdin")

    args = parser.parse_args()

    if args.command == "emit":
        cmd_emit(args)
    elif args.command == "summary":
        cmd_summary(args)
    elif args.command == "validate":
        cmd_validate(args)


if __name__ == "__main__":
    main()
