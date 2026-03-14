# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
"""Backfill created/updated dates into catalog frontmatter from git history.

Usage:
    uv run scripts/backfill_dates.py              # dry-run (print changes)
    uv run scripts/backfill_dates.py --write      # write changes to files
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT / "catalog"


def git_created(path: Path) -> str:
    """Get the date this file was first added to git."""
    result = subprocess.run(
        ["git", "log", "--follow", "--diff-filter=A", "--format=%aI", "--", str(path)],
        capture_output=True, text=True, cwd=ROOT,
    )
    dates = result.stdout.strip().splitlines()
    if not dates:
        # File not yet committed — use today
        from datetime import date
        return date.today().isoformat()
    # --follow returns oldest last
    return dates[-1][:10]


def git_updated(path: Path) -> str:
    """Get the date of the most recent commit touching this file."""
    result = subprocess.run(
        ["git", "log", "-1", "--format=%aI", "--", str(path)],
        capture_output=True, text=True, cwd=ROOT,
    )
    date_str = result.stdout.strip()
    if not date_str:
        from datetime import date
        return date.today().isoformat()
    return date_str[:10]


def backfill(write: bool = False) -> None:
    changed = 0
    skipped = 0

    for subdir in ["mappings", "frames", "categories"]:
        dir_path = CATALOG_DIR / subdir
        for md_file in sorted(dir_path.glob("*.md")):
            post = frontmatter.load(md_file)
            modified = False

            if "created" not in post.metadata:
                post.metadata["created"] = git_created(md_file)
                modified = True

            if "updated" not in post.metadata:
                post.metadata["updated"] = git_updated(md_file)
                modified = True

            if modified:
                changed += 1
                print(f"  {subdir}/{md_file.name}: created={post.metadata['created']} updated={post.metadata['updated']}")
                if write:
                    frontmatter.dump(post, md_file)
            else:
                skipped += 1

    print(f"\n{changed} files {'updated' if write else 'would be updated'}, {skipped} already had dates.")
    if not write and changed > 0:
        print("Run with --write to apply changes.")


def main() -> None:
    write = "--write" in sys.argv
    backfill(write=write)


if __name__ == "__main__":
    main()
