#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""
Extract dangling references from the Metaphorex catalog.

Scans all entries in catalog/entries/ for `related:` fields that reference
slugs with no corresponding entry file. Outputs structured JSON to stdout.

Usage:
    uv run playbooks/dangling-references/scripts/extract_dangling.py
"""

import json
import sys
from pathlib import Path

import yaml

CATALOG = Path(__file__).resolve().parents[3] / "catalog"
ENTRIES_DIR = CATALOG / "entries"

# Consolidation map: when two slugs refer to the same concept, map both
# to the canonical slug
CONSOLIDATIONS = {
    "antifragility": "antifragile",
    "canary-in-the-coal-mine": "canary-in-a-coal-mine",
    "free-rider": "free-rider-problem",
}

# Slugs that exist in pending PRs and should be excluded from the manifest
PENDING_PR_SLUGS = {
    "dichotomy-of-control",   # PR #2444 (Stoic batch 1)
    "life-is-a-play",         # PR #2444
    "memento-mori",           # PR #2444
    "negative-visualization", # PR #2444
    "the-mind-is-a-citadel",  # PR #2444
    "cognitive-defusion",     # PR #2291
    "tug-of-war-with-a-monster",  # PR #2291
    "the-line",               # PR #2241
    "pendulation",            # PR #2297
    "jig",                    # PR #2368
}


def load_entry(path: Path) -> dict | None:
    """Load YAML frontmatter from a catalog entry."""
    text = path.read_text()
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        return yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None


def find_dangling() -> dict[str, int]:
    """Return {slug: reference_count} for all dangling references."""
    existing = {p.stem for p in ENTRIES_DIR.glob("*.md")}
    refs: dict[str, int] = {}

    for entry_path in sorted(ENTRIES_DIR.glob("*.md")):
        meta = load_entry(entry_path)
        if not meta:
            continue
        related = meta.get("related", []) or []
        for slug in related:
            if slug not in existing:
                canonical = CONSOLIDATIONS.get(slug, slug)
                refs[canonical] = refs.get(canonical, 0) + 1

    return refs


def main():
    dangling = find_dangling()

    # Remove pending PR slugs
    for slug in PENDING_PR_SLUGS:
        canonical = CONSOLIDATIONS.get(slug, slug)
        dangling.pop(canonical, None)

    # Sort by reference count descending, then alphabetically
    sorted_slugs = sorted(dangling.keys(), key=lambda s: (-dangling[s], s))

    output = {
        "source": "catalog/entries/ related: field scan",
        "total": len(sorted_slugs),
        "candidates": [
            {"slug": slug, "ref_count": dangling[slug]}
            for slug in sorted_slugs
        ],
    }

    json.dump(output, sys.stdout, indent=2)
    print()  # trailing newline


if __name__ == "__main__":
    main()
