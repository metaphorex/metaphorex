#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Build the enrichment manifest.json from the survey output.

Reads catalog/entries/ directly and produces manifest.json in the format
expected by the Prospector playbook system.

Usage:
    uv run playbooks/catalog-enrichment/scripts/build_manifest.py > \
        playbooks/catalog-enrichment/manifest.json
"""

import json
import sys
from pathlib import Path

import yaml


def parse_frontmatter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.index("---", 3)
    return yaml.safe_load(text[3:end])


def main():
    catalog_dir = Path("catalog/entries")
    candidates = []

    for path in sorted(catalog_dir.glob("*.md")):
        fm = parse_frontmatter(path)
        if fm is None:
            continue

        has_transfers = "transfers" in fm and fm["transfers"]
        has_limits = "limits" in fm and fm["limits"]

        if has_transfers and has_limits:
            continue

        missing = []
        if not has_transfers:
            missing.append("transfers")
        if not has_limits:
            missing.append("limits")

        candidates.append({
            "slug": fm.get("slug", path.stem),
            "name": fm.get("name", path.stem),
            "kind": fm.get("kind", "unknown"),
            "source_frame": fm.get("source_frame", ""),
            "target_frame": "",
            "categories": fm.get("categories", []),
            "source": "archive",
            "missing_fields": missing,
            "description": f"Add {' and '.join(missing)} propositions to existing entry",
        })

    manifest = {
        "project": "catalog-enrichment",
        "project_issue": 1460,
        "source_type": "archive",
        "archive_urls": [],
        "total_catalog_entries": 694,
        "already_enriched": 694 - len(candidates),
        "candidates": candidates,
    }

    json.dump(manifest, sys.stdout, indent=2)
    print(file=sys.stdout)


if __name__ == "__main__":
    main()
