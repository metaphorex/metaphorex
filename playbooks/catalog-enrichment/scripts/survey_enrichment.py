#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Survey catalog entries for missing transfers/limits frontmatter.

Reads all entries in catalog/entries/, checks for transfers: and limits:
fields, and outputs a JSON manifest of entries needing enrichment grouped
into batches.

Usage:
    uv run playbooks/catalog-enrichment/scripts/survey_enrichment.py

Output: writes manifest to stdout as JSON.
"""

import json
import sys
from pathlib import Path

import yaml


def parse_frontmatter(path: Path) -> dict | None:
    """Extract YAML frontmatter from a markdown file."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.index("---", 3)
    return yaml.safe_load(text[3:end])


def needs_enrichment(fm: dict) -> dict:
    """Return dict of what's missing. Empty dict means fully enriched."""
    missing = {}
    if "transfers" not in fm or not fm["transfers"]:
        missing["transfers"] = True
    if "limits" not in fm or not fm["limits"]:
        missing["limits"] = True
    return missing


def main():
    catalog_dir = Path("catalog/entries")
    if not catalog_dir.exists():
        print(f"Error: {catalog_dir} not found", file=sys.stderr)
        sys.exit(1)

    entries = []
    enriched_count = 0
    error_count = 0

    for path in sorted(catalog_dir.glob("*.md")):
        fm = parse_frontmatter(path)
        if fm is None:
            print(f"Warning: no frontmatter in {path.name}", file=sys.stderr)
            error_count += 1
            continue

        missing = needs_enrichment(fm)
        if missing:
            entries.append({
                "slug": fm.get("slug", path.stem),
                "name": fm.get("name", path.stem),
                "kind": fm.get("kind", "unknown"),
                "source_frame": fm.get("source_frame", ""),
                "missing": list(missing.keys()),
            })
        else:
            enriched_count += 1

    # Sort by kind then slug for clean batching
    entries.sort(key=lambda e: (e["kind"], e["slug"]))

    # Group into batches of 50
    batch_size = 50
    batches = []
    for i in range(0, len(entries), batch_size):
        batch = entries[i : i + batch_size]
        kinds = {}
        for e in batch:
            kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
        batches.append({
            "batch_number": len(batches) + 1,
            "entry_count": len(batch),
            "kind_breakdown": kinds,
            "slugs": [e["slug"] for e in batch],
        })

    result = {
        "total_entries": enriched_count + len(entries),
        "already_enriched": enriched_count,
        "needs_enrichment": len(entries),
        "batch_count": len(batches),
        "entries": entries,
        "batches": batches,
    }

    json.dump(result, sys.stdout, indent=2)
    print(file=sys.stdout)  # trailing newline

    print(
        f"\nSummary: {len(entries)} of {enriched_count + len(entries)} entries need enrichment "
        f"({enriched_count} already done, {len(batches)} batches of ~{batch_size})",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
