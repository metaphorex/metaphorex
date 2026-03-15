#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""
Fetch metaphorical connections from the Glasgow Mapping Metaphor database.

This script queries the AJAX API at mappingmetaphor.arts.gla.ac.uk to retrieve
all strong metaphorical connections for a given list of subcategories.
It outputs structured JSON to stdout.

Usage:
    uv run scripts/fetch_connections.py > connections.json
    uv run scripts/fetch_connections.py --categories 3C01,1N01 > subset.json
"""

import argparse
import json
import re
import sys
import time

import requests

BASE_URL = "https://mappingmetaphor.arts.gla.ac.uk/ajax/getJSON-table-drilldown.php"

# All 37 top-level categories in the Glasgow Mapping Metaphor database
ALL_CATEGORIES = [
    # External World (1A-1Q)
    "1A", "1B", "1C", "1D", "1E", "1F", "1G", "1H", "1I", "1J",
    "1K", "1L", "1M", "1N", "1O", "1P", "1Q",
    # Mental World (2A-2G)
    "2A", "2B", "2C", "2D", "2E", "2F", "2G",
    # Social World (3A-3M)
    "3A", "3B", "3C", "3D", "3E", "3F", "3G", "3H", "3I", "3J",
    "3K", "3L", "3M",
]

# Subcategories to query for trial slice -- chosen for cross-domain richness
TRIAL_SUBCATEGORIES = [
    "1B01",  # Life
    "1C01",  # Health
    "1C02",  # Ill-health
    "1E01",  # Animals (general)
    "1F01",  # Plants
    "1G01",  # Food and eating
    "1H01",  # Textiles (general)
    "1I01",  # Physical sensation (general)
    "1J08",  # Strength
    "1J09",  # Weakness
    "1N01",  # Movement (general)
    "1N02",  # Walking and running
    "1O11",  # Difficulty
    "3C01",  # War and armed hostility
    "3L01",  # Trade and commerce
    "3L02",  # Money
    "2B03",  # Answer and argument
    "2D01",  # Emotion (general)
    "2D06",  # Emotional suffering
    "2D08",  # Love and friendship
    "1A28",  # Atmosphere and weather
    "3J01",  # Travel and travelling
]


def strip_html(text: str) -> str:
    """Remove HTML tags from a string."""
    return re.sub(r"<[^>]+>", "", text)


def fetch_connections(subcat: str, strength: str = "strong") -> list[dict]:
    """Fetch connections for a subcategory from the Glasgow API."""
    params = {"subCat": subcat, "strength": strength}
    try:
        resp = requests.get(BASE_URL, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except (requests.RequestException, ValueError) as e:
        print(f"Warning: failed to fetch {subcat}: {e}", file=sys.stderr)
        return []

    results = []
    for entry in data:
        words = [strip_html(w) for w in entry.get("words", [])]
        results.append({
            "cat1": entry["cat1"],
            "cat1_name": entry["m1name"],
            "cat2": entry["cat2"],
            "cat2_name": entry["m2name"],
            "direction": entry["direction"],
            "strength": entry["strength"],
            "first_date": entry["firstdate"],
            "sample_words": words,
        })
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Glasgow Mapping Metaphor connections"
    )
    parser.add_argument(
        "--categories",
        help="Comma-separated list of subcategory codes (default: trial slice)",
    )
    parser.add_argument(
        "--strength",
        default="strong",
        choices=["strong", "weak", "both"],
        help="Filter by connection strength (default: strong)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Delay between requests in seconds (default: 1.0)",
    )
    args = parser.parse_args()

    categories = (
        args.categories.split(",") if args.categories else TRIAL_SUBCATEGORIES
    )

    all_connections = []
    seen = set()

    for i, cat in enumerate(categories):
        print(f"Fetching {cat} ({i+1}/{len(categories)})...", file=sys.stderr)
        connections = fetch_connections(cat, args.strength)
        for conn in connections:
            # Deduplicate by category pair (order-independent)
            pair_key = tuple(sorted([conn["cat1"], conn["cat2"]]))
            if pair_key not in seen:
                seen.add(pair_key)
                all_connections.append(conn)
        if i < len(categories) - 1:
            time.sleep(args.delay)

    output = {
        "source": "Glasgow Mapping Metaphor database",
        "url": "https://mappingmetaphor.arts.gla.ac.uk/",
        "fetch_params": {
            "categories": categories,
            "strength": args.strength,
        },
        "total_connections": len(all_connections),
        "connections": all_connections,
    }

    json.dump(output, sys.stdout, indent=2)
    print(file=sys.stderr)
    print(f"Total unique connections: {len(all_connections)}", file=sys.stderr)


if __name__ == "__main__":
    main()
