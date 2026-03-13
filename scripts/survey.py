#!/usr/bin/env python3
"""Survey GitHub for actionable Metaphorex pipeline work.

Usage:
    uv run scripts/survey.py --repo metaphorex/metaphorex

Outputs JSON to stdout with categorized work items.
"""

import argparse
import json
import re
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


def fetch_all_issues(owner: str, name: str) -> list[dict]:
    """Fetch all open import-project issues with pagination."""
    all_nodes: list[dict] = []
    cursor = None
    while True:
        after = f', after: "{cursor}"' if cursor else ""
        data = gh_graphql(f"""{{
          repository(owner: "{owner}", name: "{name}") {{
            issues(first: 100, labels: ["import-project"], states: OPEN{after}) {{
              pageInfo {{ hasNextPage endCursor }}
              nodes {{
                number
                title
                body
                labels(first: 10) {{ nodes {{ name }} }}
                parent {{ number }}
              }}
            }}
          }}
        }}""")
        issues = (
            data.get("data", {}).get("repository", {})
            .get("issues", {})
        )
        all_nodes.extend(issues.get("nodes", []))
        page_info = issues.get("pageInfo", {})
        if not page_info.get("hasNextPage"):
            break
        cursor = page_info["endCursor"]
    return all_nodes


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
    # Also fetch body for fallback parent detection (GitHub 100 sub-issue cap
    # means some sub-issues lack native parent linkage).
    # Paginate to handle repos with >100 import-project issues.

    # Collect PR results
    smelting = [{"number": p["number"], "title": p["title"]} for p in collect(pr_smelting)]
    assay = [{"number": p["number"], "title": p["title"]} for p in collect(pr_assay)]
    miner_fix = [{"number": p["number"], "title": p["title"]} for p in collect(pr_miner_fix)]
    in_progress = [{"number": p["number"], "title": p["title"]} for p in collect(pr_in_progress)]

    # Categorize issues using native sub-issue relationships:
    # - No parent → top-level project issue
    # - Has parent → sub-issue (mining candidate)
    #
    # Fallback: GitHub caps native sub-issues at 100. Orphaned sub-issues
    # beyond that cap lack a `parent` field, so we also check the issue body
    # for "Sub-issue of #N" and the title for "[project-name]" prefixes.
    all_issues = fetch_all_issues(owner, name)
    parents = []
    sub_issues = []

    # First pass: identify parent issues (those with no native parent and
    # no body-text evidence of being a sub-issue).
    parent_numbers: set[int] = set()
    for issue in all_issues:
        if issue.get("parent") is None:
            parents.append(issue)
            parent_numbers.add(issue["number"])
        else:
            sub_issues.append(issue)

    # Build title-prefix lookup from known parents: "[Project Name]" → parent#
    _sub_issue_of_re = re.compile(r"[Ss]ub-?issue of #(\d+)", re.IGNORECASE)
    _title_prefix_re = re.compile(r"^\[(.+?)\]")
    parent_title_prefixes: dict[str, int] = {}
    for p in parents:
        m = _title_prefix_re.match(p["title"])
        if m:
            parent_title_prefixes[m.group(1).lower()] = p["number"]

    # Second pass: re-classify orphans in the parents list that are actually
    # sub-issues (body says "Sub-issue of #N" or title prefix matches a parent).
    reclassified: list[dict] = []
    for issue in list(parents):
        body = issue.get("body") or ""
        inferred_parent = None

        # Check body for "Sub-issue of #N"
        m = _sub_issue_of_re.search(body)
        if m:
            inferred_parent = int(m.group(1))

        # Check title prefix "[project-name]" against known parent titles
        if inferred_parent is None:
            tm = _title_prefix_re.match(issue["title"])
            if tm:
                prefix = tm.group(1).lower()
                if prefix in parent_title_prefixes:
                    matched_parent = parent_title_prefixes[prefix]
                    if matched_parent != issue["number"]:
                        inferred_parent = matched_parent

        if inferred_parent is not None:
            # Reclassify: move from parents to sub_issues with synthetic parent
            issue["parent"] = {"number": inferred_parent}
            reclassified.append(issue)

    for issue in reclassified:
        parents.remove(issue)
        parent_numbers.discard(issue["number"])
        sub_issues.append(issue)

    # Categorize parent issues by pipeline stage:
    #   no labels         → needs_prospecting
    #   in-progress only  → needs_survey (prospected, not yet verified)
    #   in-progress + surveyed → prospected_projects (ready for mining)
    #   needs-rework      → needs_rework (prospecting rejected)
    needs_prospecting = []
    needs_survey = []
    prospected_projects = []
    needs_rework = []

    for p in parents:
        label_names = [l["name"] for l in p.get("labels", {}).get("nodes", [])]
        priority = "high" if "priority:high" in label_names else "normal"
        entry = {
            "number": p["number"],
            "title": p["title"],
            "priority": priority,
        }
        if "needs-rework" in label_names:
            needs_rework.append(entry)
        elif "in-progress" not in label_names:
            needs_prospecting.append(entry)
        elif "surveyed" in label_names:
            prospected_projects.append(entry)
        else:
            needs_survey.append(entry)

    # Sort each bucket so priority:high items come first
    for bucket in (needs_rework, needs_prospecting, prospected_projects, needs_survey):
        bucket.sort(key=lambda x: (0 if x["priority"] == "high" else 1, x["number"]))

    # Sub-issues without in-progress = unclaimed mining work
    # Only include sub-issues whose parent project is surveyed (verified).
    surveyed_parent_numbers = {p["number"] for p in prospected_projects}
    unclaimed = []

    # Build priority lookup from parent issues
    parent_priority = {
        p["number"]: p.get("priority", "normal") for p in prospected_projects
    }

    for issue in sub_issues:
        label_names = [l["name"] for l in issue.get("labels", {}).get("nodes", [])]
        parent_num = issue.get("parent", {}).get("number") if issue.get("parent") else None
        if "in-progress" not in label_names and parent_num in surveyed_parent_numbers:
            unclaimed.append({
                "number": issue["number"],
                "title": issue["title"],
                "priority": parent_priority.get(parent_num, "normal"),
            })

    # Sort unclaimed so children of priority:high parents come first
    unclaimed.sort(key=lambda x: (0 if x["priority"] == "high" else 1, x["number"]))

    result = {
        "needs_smelting": smelting,
        "needs_assay": assay,
        "needs_miner_fix": miner_fix,
        "needs_survey": needs_survey,
        "needs_rework": needs_rework,
        "in_progress": in_progress,
        "unclaimed": unclaimed,
        "needs_prospecting": needs_prospecting,
        "prospected_projects": prospected_projects,
        "total_actionable": (
            len(smelting) + len(assay) + len(miner_fix)
            + len(needs_survey) + len(needs_rework)
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
