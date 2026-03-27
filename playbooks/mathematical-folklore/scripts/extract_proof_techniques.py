#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""
Extract humorous/informal proof techniques from the Illinois CS archive.

Source: https://mfleck.cs.illinois.edu/proof.html
Also cross-references: https://jcdverha.home.xs4all.nl/scijokes/9_7.html

Outputs JSON to stdout with each named technique, its description,
and whether it has metaphorical potential for the Metaphorex catalog.
"""
import json
import re
import sys

import requests
from bs4 import BeautifulSoup

URLS = [
    "https://mfleck.cs.illinois.edu/proof.html",
    "https://users.cs.northwestern.edu/~riesbeck/proofs.html",
]


def fetch_and_parse(url: str) -> list[dict]:
    """Fetch a proof techniques page and extract named techniques."""
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    techniques = []
    # Most of these pages use <b> or <strong> for technique names
    # followed by descriptive text
    text = soup.get_text(separator="\n")

    # Pattern: "Proof by <name>" followed by description
    pattern = re.compile(
        r"(?:Proof|Disproof)\s+by\s+([A-Za-z][A-Za-z\s]+?)(?:\.|:|\n)",
        re.IGNORECASE,
    )
    for match in pattern.finditer(text):
        name = match.group(1).strip().rstrip(".")
        if len(name) > 3 and len(name) < 50:
            techniques.append(
                {
                    "raw_name": f"Proof by {name}",
                    "slug": "proof-by-" + re.sub(r"\s+", "-", name.lower()),
                    "source_url": url,
                }
            )

    return techniques


def deduplicate(techniques: list[dict]) -> list[dict]:
    """Remove duplicates by slug."""
    seen = set()
    result = []
    for t in techniques:
        if t["slug"] not in seen:
            seen.add(t["slug"])
            result.append(t)
    return result


def main():
    all_techniques = []
    for url in URLS:
        try:
            all_techniques.extend(fetch_and_parse(url))
        except Exception as e:
            print(f"Warning: failed to fetch {url}: {e}", file=sys.stderr)

    all_techniques = deduplicate(all_techniques)
    json.dump(all_techniques, sys.stdout, indent=2)
    print(f"\n\nTotal techniques extracted: {len(all_techniques)}", file=sys.stderr)


if __name__ == "__main__":
    main()
