#!/usr/bin/env python3
"""Survey GitHub for actionable Metaphorex pipeline work.

Usage:
    uv run scripts/survey.py --repo metaphorex/metaphorex

Outputs JSON to stdout with categorized work items.
"""

import argparse
import json
import subprocess
import sys


def gh_query(args: list[str]) -> subprocess.Popen:
    """Start a gh CLI query as a background process."""
    return subprocess.Popen(
        ["gh", *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )


def gh_graphql(query: str) -> dict:
    """Run a GraphQL query via gh api and return parsed JSON."""
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={query}"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"GraphQL query failed: {result.stderr.strip()}", file=sys.stderr)
        return {}
    return json.loads(result.stdout)


def collect(proc: subprocess.Popen) -> list[dict]:
    """Wait for a gh process and parse its JSON output."""
    stdout, stderr = proc.communicate()
    if proc.returncode != 0:
        print(f"gh query failed: {stderr.strip()}", file=sys.stderr)
        return []
    try:
        return json.loads(stdout) if stdout.strip() else []
    except json.JSONDecodeError:
        return []


def survey(repo: str) -> dict:
    """Run all GitHub queries in parallel and return structured results."""
    owner, name = repo.split("/")

    # Launch PR queries concurrently (REST is fine for these)
    pr_smelting = gh_query([
        "pr", "list", "-R", repo,
        "--label", "needs-smelting",
        "--json", "number,title",
    ])
    pr_assay = gh_query([
        "pr", "list", "-R", repo,
        "--label", "needs-assay",
        "--json", "number,title",
    ])
    pr_miner_fix = gh_query([
        "pr", "list", "-R", repo,
        "--label", "needs-miner-fix",
        "--json", "number,title",
    ])
    pr_in_progress = gh_query([
        "pr", "list", "-R", repo,
        "--label", "in-progress",
        "--json", "number,title",
    ])

    # Use GraphQL for issues — native sub-issue parent field tells us
    # which issues are top-level projects vs sub-issues, no label needed.
    gql = gh_graphql(f"""{{
      repository(owner: "{owner}", name: "{name}") {{
        issues(first: 100, labels: ["import-project"], states: OPEN) {{
          nodes {{
            number
            title
            labels(first: 10) {{ nodes {{ name }} }}
            parent {{ number }}
          }}
        }}
      }}
    }}""")

    # Collect PR results
    smelting = [{"number": p["number"], "title": p["title"]} for p in collect(pr_smelting)]
    assay = [{"number": p["number"], "title": p["title"]} for p in collect(pr_assay)]
    miner_fix = [{"number": p["number"], "title": p["title"]} for p in collect(pr_miner_fix)]
    in_progress = [{"number": p["number"], "title": p["title"]} for p in collect(pr_in_progress)]

    # Categorize issues using native sub-issue relationships:
    # - No parent → top-level project issue
    # - Has parent → sub-issue (mining candidate)
    all_issues = (
        gql.get("data", {}).get("repository", {}).get("issues", {}).get("nodes", [])
    )
    parents = []
    sub_issues = []

    for issue in all_issues:
        if issue.get("parent") is None:
            parents.append(issue)
        else:
            sub_issues.append(issue)

    # Parents without in-progress = not yet prospected
    needs_prospecting = []

    for p in parents:
        label_names = [l["name"] for l in p.get("labels", {}).get("nodes", [])]
        if "in-progress" not in label_names:
            needs_prospecting.append({
                "number": p["number"],
                "title": p["title"],
            })

    # Sub-issues without in-progress = unclaimed mining work
    unclaimed = []

    for issue in sub_issues:
        label_names = [l["name"] for l in issue.get("labels", {}).get("nodes", [])]
        if "in-progress" not in label_names:
            unclaimed.append({
                "number": issue["number"],
                "title": issue["title"],
            })

    result = {
        "needs_smelting": smelting,
        "needs_assay": assay,
        "needs_miner_fix": miner_fix,
        "in_progress": in_progress,
        "unclaimed": unclaimed,
        "needs_prospecting": needs_prospecting,
        "total_actionable": (
            len(smelting) + len(assay) + len(miner_fix)
            + len(unclaimed) + len(needs_prospecting)
        ),
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Survey GitHub for actionable Metaphorex pipeline work"
    )
    parser.add_argument(
        "--repo", required=True,
        help="GitHub repo (e.g. metaphorex/metaphorex)",
    )
    args = parser.parse_args()

    result = survey(args.repo)
    json.dump(result, sys.stdout, indent=2)
    print()  # trailing newline


if __name__ == "__main__":
    main()
