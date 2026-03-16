# /// script
# requires-python = ">=3.11"
# dependencies = ["python-frontmatter>=1.1.0"]
# ///
"""Migrate catalog/mappings/ frontmatter and body sections to schema v2.

Frontmatter transforms:
  kind: conceptual-metaphor  →  kind: metaphor
  kind: dead-metaphor        →  kind: metaphor  +  dead: true
  kind: cross-field-mapping   →  kind: metaphor
  target_frame: x            →  (removed)  +  applies_to: [x]

Body section renames:
  ## What It Brings  →  ## Transfers
  ## Where It Breaks →  ## Limits

Idempotent: safe to re-run. Use --dry-run to preview changes.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import frontmatter

CATALOG_DIR = Path(__file__).resolve().parent.parent / "catalog" / "mappings"

KIND_MAP = {
    "conceptual-metaphor": "metaphor",
    "dead-metaphor": "metaphor",
    "cross-field-mapping": "metaphor",
}

SECTION_RENAMES = {
    "## What It Brings": "## Transfers",
    "## Where It Breaks": "## Limits",
}


def migrate_post(post: frontmatter.Post) -> list[str]:
    """Apply v2 transforms to a post in-place. Return list of changes made."""
    changes: list[str] = []

    # --- kind transform ---
    kind = post.get("kind")
    if kind in KIND_MAP:
        new_kind = KIND_MAP[kind]
        if kind == "dead-metaphor":
            if not post.get("dead"):
                post["dead"] = True
                changes.append(f"kind: {kind} → {new_kind} + dead: true")
            else:
                changes.append(f"kind: {kind} → {new_kind}")
        else:
            changes.append(f"kind: {kind} → {new_kind}")
        post["kind"] = new_kind

    # --- target_frame → applies_to ---
    if "target_frame" in post.metadata:
        tf = post["target_frame"]
        if "applies_to" not in post.metadata:
            post["applies_to"] = [tf]
            changes.append(f"target_frame: {tf} → applies_to: [{tf}]")
        del post["target_frame"]
        if "target_frame" not in changes[-1] if changes else True:
            changes.append(f"removed stale target_frame: {tf}")

    # --- body section renames ---
    content = post.content
    for old_heading, new_heading in SECTION_RENAMES.items():
        if old_heading in content:
            content = content.replace(old_heading, new_heading)
            changes.append(f"section: {old_heading} → {new_heading}")
    post.content = content

    return changes


def main() -> None:
    parser = argparse.ArgumentParser(description="Migrate mappings to schema v2")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would change without writing files",
    )
    args = parser.parse_args()

    if not CATALOG_DIR.is_dir():
        print(f"ERROR: catalog dir not found: {CATALOG_DIR}", file=sys.stderr)
        sys.exit(1)

    files = sorted(CATALOG_DIR.glob("*.md"))
    migrated = 0
    skipped = 0

    for path in files:
        post = frontmatter.load(path)
        changes = migrate_post(post)

        if changes:
            migrated += 1
            label = "[dry-run] " if args.dry_run else ""
            print(f"{label}{path.name}:")
            for c in changes:
                print(f"  - {c}")
            if not args.dry_run:
                path.write_text(frontmatter.dumps(post) + "\n", encoding="utf-8")
        else:
            skipped += 1

    print(f"\nSummary: {migrated} migrated, {skipped} already current")


if __name__ == "__main__":
    main()
