# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
"""Backfill contributors[] from GitHub activity.

For each mapping, finds:
  - The PR that introduced the file
  - Any issue linked in the PR
  - The issue filer's GitHub username
  - All PR authors who subsequently touched the file

Deduplicates against the author field and writes to contributors[].

Usage:
    uv run scripts/backfill_contributors.py             # dry run (print changes)
    uv run scripts/backfill_contributors.py --write      # write changes to files
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
MAPPINGS_DIR = ROOT / "catalog" / "mappings"


def gh(args: list[str]) -> str:
    """Run a gh CLI command and return stdout."""
    result = subprocess.run(
        ["gh"] + args,
        capture_output=True, text=True, check=True,
    )
    return result.stdout.strip()


def get_prs_for_file(filepath: str) -> list[dict]:
    """Find all merged PRs that touched a file."""
    # Use gh to search for PRs that modified this file
    output = gh([
        "pr", "list",
        "--state", "merged",
        "--search", f"'{filepath}'",
        "--json", "number,author,body",
        "--limit", "50",
    ])
    if not output:
        return []
    return json.loads(output)


def get_pr_for_commit(sha: str) -> dict | None:
    """Find the PR associated with a commit."""
    try:
        output = gh([
            "pr", "list",
            "--state", "merged",
            "--search", sha,
            "--json", "number,author,body",
            "--limit", "1",
        ])
        prs = json.loads(output) if output else []
        return prs[0] if prs else None
    except subprocess.CalledProcessError:
        return None


def get_introducing_commit(filepath: str) -> str | None:
    """Find the commit that first added a file."""
    result = subprocess.run(
        ["git", "log", "--diff-filter=A", "--format=%H", "--", filepath],
        capture_output=True, text=True, check=True,
        cwd=ROOT,
    )
    lines = result.stdout.strip().split("\n")
    return lines[-1] if lines and lines[-1] else None


def get_all_commit_authors(filepath: str) -> set[str]:
    """Get all GitHub usernames who committed changes to a file.

    Uses git log Co-Authored-By trailers and author emails.
    Returns GitHub usernames where identifiable.
    """
    result = subprocess.run(
        ["git", "log", "--format=%an%n%(trailers:key=Co-Authored-By)", "--", filepath],
        capture_output=True, text=True, check=True,
        cwd=ROOT,
    )
    # This gets commit authors but not necessarily GitHub usernames
    # For a more robust approach, we cross-reference with PR data
    return set()


def extract_issue_number(pr_body: str) -> int | None:
    """Extract linked issue number from PR body."""
    import re
    # Match patterns like "Closes #123", "Fixes #123", "Resolves #123"
    # Also match bare "#123" references
    patterns = [
        r"(?:closes|fixes|resolves)\s+#(\d+)",
        r"(?:close|fix|resolve)\s+#(\d+)",
        r"issue\s+#(\d+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, pr_body, re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None


def get_issue_author(issue_number: int) -> str | None:
    """Get the GitHub username of an issue's author."""
    try:
        output = gh([
            "issue", "view", str(issue_number),
            "--json", "author",
        ])
        data = json.loads(output)
        return data.get("author", {}).get("login")
    except subprocess.CalledProcessError:
        return None


def get_pr_authors_for_file(filepath: str) -> set[str]:
    """Get all PR authors who touched a file via git log + gh."""
    # Get all commit SHAs that touched this file
    result = subprocess.run(
        ["git", "log", "--format=%H", "--", filepath],
        capture_output=True, text=True, check=True,
        cwd=ROOT,
    )
    shas = [s for s in result.stdout.strip().split("\n") if s]

    authors = set()
    seen_prs = set()
    for sha in shas:
        pr = get_pr_for_commit(sha)
        if pr and pr["number"] not in seen_prs:
            seen_prs.add(pr["number"])
            login = pr.get("author", {}).get("login")
            if login:
                authors.add(login)
    return authors


def process_mapping(path: Path, write: bool) -> dict | None:
    """Process a single mapping file. Returns change info or None."""
    post = frontmatter.load(path)
    meta = post.metadata
    author = meta.get("author", "")
    existing = set(meta.get("contributors", []))

    filepath = f"catalog/mappings/{path.name}"
    new_contributors = set()

    # Find the introducing commit and its PR
    intro_sha = get_introducing_commit(filepath)
    if intro_sha:
        pr = get_pr_for_commit(intro_sha)
        if pr:
            # Check for linked issue
            body = pr.get("body", "") or ""
            issue_num = extract_issue_number(body)
            if issue_num:
                issue_author = get_issue_author(issue_num)
                if issue_author:
                    new_contributors.add(issue_author)

    # Find all PR authors who touched the file
    pr_authors = get_pr_authors_for_file(filepath)
    new_contributors.update(pr_authors)

    # Remove the author (don't list them as contributor too)
    # For agent authors, strip the agent: prefix for comparison
    if author.startswith("agent:"):
        # Agent authors don't have GitHub usernames to filter
        pass
    else:
        new_contributors.discard(author)

    # Remove bot accounts
    new_contributors -= {"metaphorex-miner", "metaphorex-prospector",
                         "metaphorex-assayer", "metaphorex-smelter"}

    # Merge with existing
    combined = sorted(existing | new_contributors)

    if set(combined) == existing:
        return None  # No change

    if write:
        post.metadata["contributors"] = combined
        path.write_text(frontmatter.dumps(post) + "\n")

    return {
        "file": path.name,
        "added": sorted(new_contributors - existing),
        "total": combined,
    }


def main() -> None:
    write = "--write" in sys.argv

    changes = []
    mapping_files = sorted(MAPPINGS_DIR.glob("*.md"))
    total = len(mapping_files)

    for i, path in enumerate(mapping_files, 1):
        print(f"\r[{i}/{total}] {path.name}", end="", flush=True, file=sys.stderr)
        change = process_mapping(path, write=write)
        if change:
            changes.append(change)

    print(file=sys.stderr)

    if changes:
        print(f"\n{len(changes)} mapping(s) updated:\n")
        for c in changes:
            added = ", ".join(c["added"]) if c["added"] else "(no new)"
            print(f"  {c['file']}: +{added}")
    else:
        print("\nNo changes needed.")

    if not write and changes:
        print(f"\nDry run. Use --write to apply {len(changes)} change(s).")


if __name__ == "__main__":
    main()
