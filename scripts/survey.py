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
    pr_enrichment = gh_query([
        "issue", "list", "-R", repo,
        "--label", "needs-enrichment",
        "--state", "open",
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
    kaizen_pipeline = gh_query([
        "issue", "list", "-R", repo,
        "--label", "kaizen:pipeline",
        "--state", "open",
        "--json", "number,title,labels",
        "--limit", "20",
    ])
    kaizen_content = gh_query([
        "issue", "list", "-R", repo,
        "--label", "kaizen:content",
        "--state", "open",
        "--json", "number,title,labels",
        "--limit", "20",
    ])

    # Use GraphQL for issues — native sub-issue parent field tells us
    # which issues are top-level projects vs sub-issues, no label needed.
    # Also fetch body for fallback parent detection (GitHub 100 sub-issue cap
    # means some sub-issues lack native parent linkage).
    # Paginate to handle repos with >100 import-project issues.

    # Collect PR results
    smelting = [{"number": p["number"], "title": p["title"]} for p in collect(pr_smelting)]
    assay = [{"number": p["number"], "title": p["title"]} for p in collect(pr_assay)]
    enrichment = [{"number": p["number"], "title": p["title"]} for p in collect(pr_enrichment)]
    miner_fix = [{"number": p["number"], "title": p["title"]} for p in collect(pr_miner_fix)]
    in_progress = [{"number": p["number"], "title": p["title"]} for p in collect(pr_in_progress)]
    # Merge kaizen from both labels (gh --label uses AND, so we query separately)
    # Classify by triage status based on labels
    seen_kaizen: set[int] = set()
    kaizen_open = []
    kaizen_ready = []
    kaizen_needs_human = []
    kaizen_untriaged = []
    triage_labels = {"kaizen:ready", "kaizen:needs-human", "kaizen:wont-fix"}
    for i in collect(kaizen_pipeline) + collect(kaizen_content):
        if i["number"] not in seen_kaizen:
            seen_kaizen.add(i["number"])
            item = {"number": i["number"], "title": i["title"]}
            kaizen_open.append(item)
            label_names = {l["name"] for l in i.get("labels", [])}
            if "kaizen:ready" in label_names:
                kaizen_ready.append(item)
            elif "kaizen:needs-human" in label_names:
                kaizen_needs_human.append(item)
            elif not (label_names & triage_labels):
                kaizen_untriaged.append(item)

    # Classify issues into parents (top-level projects) vs sub-issues.
    # Uses GraphQL `parent` field for native sub-issue linkage, with
    # body-text and title-prefix fallback for orphaned sub-issues
    # (GitHub caps native sub-issues at 100 per parent).
    all_issues = fetch_all_issues(owner, name)
    parents = []

    # First pass: issues with no native parent are candidate parents.
    for issue in all_issues:
        if issue.get("parent") is None:
            parents.append(issue)

    # Build title-prefix lookup from known parents: "[Project Name]" → parent#
    _sub_issue_of_re = re.compile(r"[Ss]ub-?issue of #(\d+)", re.IGNORECASE)
    _title_prefix_re = re.compile(r"^\[(.+?)\]")
    parent_title_prefixes: dict[str, int] = {}
    parent_numbers: set[int] = {p["number"] for p in parents}
    for p in parents:
        m = _title_prefix_re.match(p["title"])
        if m:
            parent_title_prefixes[m.group(1).lower()] = p["number"]

    # Second pass: re-classify orphans that are actually sub-issues
    # (body says "Sub-issue of #N" or title prefix matches a parent).
    # Track the inferred parent for each orphan so we can route them to
    # the correct unclaimed/stale bucket later.
    reclassified: list[dict] = []
    orphan_parent_map: dict[int, int] = {}  # orphan issue# → parent issue#
    for issue in list(parents):
        body = issue.get("body") or ""
        inferred_parent = None

        m = _sub_issue_of_re.search(body)
        if m:
            inferred_parent = int(m.group(1))

        if inferred_parent is None:
            tm = _title_prefix_re.match(issue["title"])
            if tm:
                prefix = tm.group(1).lower()
                if prefix in parent_title_prefixes:
                    matched_parent = parent_title_prefixes[prefix]
                    if matched_parent != issue["number"]:
                        inferred_parent = matched_parent

        if inferred_parent is not None:
            reclassified.append(issue)
            orphan_parent_map[issue["number"]] = inferred_parent

    for issue in reclassified:
        parents.remove(issue)
        parent_numbers.discard(issue["number"])

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
        elif "surveyed" in label_names:
            prospected_projects.append(entry)
        elif "needs-survey" in label_names or "in-progress" in label_names:
            needs_survey.append(entry)
        else:
            needs_prospecting.append(entry)

    # Sort each bucket so priority:high items come first
    for bucket in (needs_rework, needs_prospecting, prospected_projects, needs_survey):
        bucket.sort(key=lambda x: (0 if x["priority"] == "high" else 1, x["number"]))

    # Fetch sub-issues via REST for each surveyed project.
    # The GraphQL `parent` field is capped at 100 sub-issues per parent,
    # so we use the REST sub_issues endpoint which has no such limit.
    surveyed_parent_numbers = {p["number"] for p in prospected_projects}
    parent_priority = {
        p["number"]: p.get("priority", "normal") for p in prospected_projects
    }

    # Also gather open PR numbers that reference issues (for stale detection)
    pr_refs_proc = gh_query([
        "pr", "list", "-R", repo, "--state", "open",
        "--json", "number,body,title",
        "--limit", "200",
    ])
    pr_data = collect(pr_refs_proc)
    # Extract issue numbers referenced by open PRs (Closes #N, Fixes #N, etc.)
    _closes_re = re.compile(r"(?:closes?|fixes?|resolves?)\s+#(\d+)", re.IGNORECASE)
    referenced_by_pr: set[int] = set()
    for pr in pr_data:
        for field in (pr.get("body", ""), pr.get("title", "")):
            referenced_by_pr.update(int(m) for m in _closes_re.findall(field or ""))

    unclaimed = []
    stale_in_progress = []

    for parent_num in surveyed_parent_numbers:
        result_rest = subprocess.run(
            ["gh", "api", f"repos/{repo}/issues/{parent_num}/sub_issues?per_page=100",
             "--paginate", "--jq", ".[]"],
            capture_output=True, text=True,
        )
        if result_rest.returncode != 0:
            continue
        # Parse JSONL output (--jq .[] emits one object per line)
        for line in result_rest.stdout.strip().split("\n"):
            if not line.strip():
                continue
            try:
                si = json.loads(line)
            except json.JSONDecodeError:
                continue
            if si.get("state") != "open":
                continue
            si_labels = [l["name"] for l in si.get("labels", [])]
            si_num = si["number"]
            priority = parent_priority.get(parent_num, "normal")
            if "in-progress" not in si_labels:
                unclaimed.append({
                    "number": si_num,
                    "title": si["title"],
                    "priority": priority,
                })
            elif si_num not in referenced_by_pr:
                # Stale claim: labeled in-progress but no open PR references it
                stale_in_progress.append({
                    "number": si_num,
                    "title": si["title"],
                    "priority": priority,
                })

    # Supplement with title-pattern and body-text detection for orphaned
    # sub-issues. GitHub caps native sub-issue linkage at 100 per parent,
    # so issues beyond that limit lose their parent link and are invisible
    # to the REST sub_issues endpoint. We detect them two ways:
    #   1. orphan_parent_map: body text "Sub-issue of #N" or title prefix
    #      matching a parent (populated during reclassification above)
    #   2. Sibling inference: title prefix "[foo]" matches siblings that
    #      DO have native parent links to a surveyed parent
    seen_sub_nums = {s["number"] for s in unclaimed + stale_in_progress}

    # Build prefix→parent_num map from natively-linked sub-issues.
    # If issue #X has parent #Y and title "[foo] bar", then prefix "foo"
    # maps to parent #Y. We only care about surveyed parents.
    prefix_to_parent: dict[str, int] = {}
    for issue in all_issues:
        parent_info = issue.get("parent")
        if parent_info is None:
            continue
        pnum = parent_info["number"]
        if pnum not in surveyed_parent_numbers:
            continue
        tm = _title_prefix_re.match(issue["title"])
        if tm:
            prefix_to_parent[tm.group(1).lower()] = pnum

    for issue in all_issues:
        inum = issue["number"]
        if inum in seen_sub_nums or inum in parent_numbers:
            continue

        # Determine parent via orphan_parent_map or sibling prefix inference
        matched_parent = orphan_parent_map.get(inum)
        if matched_parent is None:
            tm = _title_prefix_re.match(issue["title"])
            if tm:
                matched_parent = prefix_to_parent.get(tm.group(1).lower())
        if matched_parent is None or matched_parent not in surveyed_parent_numbers:
            continue

        si_labels = [l["name"] for l in issue.get("labels", {}).get("nodes", [])]
        priority = parent_priority.get(matched_parent, "normal")
        if "in-progress" not in si_labels:
            unclaimed.append({
                "number": inum,
                "title": issue["title"],
                "priority": priority,
            })
        elif inum not in referenced_by_pr:
            stale_in_progress.append({
                "number": inum,
                "title": issue["title"],
                "priority": priority,
            })
        seen_sub_nums.add(inum)

    # Sort unclaimed so children of priority:high parents come first
    unclaimed.sort(key=lambda x: (0 if x["priority"] == "high" else 1, x["number"]))
    stale_in_progress.sort(key=lambda x: (0 if x["priority"] == "high" else 1, x["number"]))

    result = {
        "needs_smelting": smelting,
        "needs_assay": assay,
        "needs_enrichment": enrichment,
        "needs_miner_fix": miner_fix,
        "needs_survey": needs_survey,
        "needs_rework": needs_rework,
        "in_progress": in_progress,
        "unclaimed": unclaimed,
        "stale_in_progress": stale_in_progress,
        "kaizen_open": kaizen_open,
        "kaizen_ready": kaizen_ready,
        "kaizen_needs_human": kaizen_needs_human,
        "kaizen_untriaged": kaizen_untriaged,
        "needs_prospecting": needs_prospecting,
        "prospected_projects": prospected_projects,
        "total_actionable": (
            len(smelting) + len(assay) + len(enrichment) + len(miner_fix)
            + len(needs_survey) + len(needs_rework)
            + len(unclaimed) + len(stale_in_progress)
            + len(needs_prospecting)
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
