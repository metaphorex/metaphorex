#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""
Extract nautical terms from curated web archives that have migrated
into everyday English as metaphors.

Primary sources:
  - NOAA: https://oceanservice.noaa.gov/navigation/nautical-terms.html
  - Royal Museums Greenwich: https://www.rmg.co.uk/stories/maritime-history/nautical-origins-everyday-phrases
  - Rubicon3: https://www.rubicon3adventure.com/50-sailor-sayings-you-wont-believe-are-part-of-your-daily-speech/

The script fetches these pages, parses the nautical terms mentioned,
and outputs a JSON list of terms with their nautical origin and modern
metaphorical meaning. This is used as an input to build the manifest.

Usage:
    python3 extract_nautical_metaphors.py
    python3 extract_nautical_metaphors.py --cached   # use cached HTML files
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Install deps: pip install requests beautifulsoup4", file=sys.stderr)
    sys.exit(1)

SOURCES = [
    {
        "name": "NOAA Nautical Terms",
        "url": "https://oceanservice.noaa.gov/navigation/nautical-terms.html",
    },
    {
        "name": "Royal Museums Greenwich",
        "url": "https://www.rmg.co.uk/stories/maritime-history/nautical-origins-everyday-phrases",
    },
]

CACHE_DIR = Path(__file__).parent / ".cache"


def fetch_or_cache(url: str, name: str, use_cache: bool) -> str:
    """Fetch URL content, optionally caching to disk."""
    CACHE_DIR.mkdir(exist_ok=True)
    cache_file = CACHE_DIR / f"{name.replace(' ', '_').lower()}.html"

    if use_cache and cache_file.exists():
        return cache_file.read_text()

    resp = requests.get(url, timeout=30, headers={"User-Agent": "Metaphorex-Prospector/1.0"})
    resp.raise_for_status()
    html = resp.text
    cache_file.write_text(html)
    return html


def extract_noaa(html: str) -> list[dict]:
    """Extract terms from NOAA nautical terms page."""
    soup = BeautifulSoup(html, "html.parser")
    terms = []

    # NOAA uses h2/h3 headings or bold terms followed by descriptions
    for heading in soup.find_all(["h2", "h3"]):
        text = heading.get_text(strip=True)
        # Skip navigation/structural headings
        if text.lower() in ("", "navigation", "search", "menu"):
            continue
        desc_parts = []
        for sib in heading.find_next_siblings():
            if sib.name in ("h2", "h3"):
                break
            desc_parts.append(sib.get_text(strip=True))
        desc = " ".join(desc_parts).strip()
        if desc and len(text) < 100:
            terms.append({"term": text, "description": desc, "source": "NOAA"})

    return terms


def extract_rmg(html: str) -> list[dict]:
    """Extract terms from Royal Museums Greenwich page."""
    soup = BeautifulSoup(html, "html.parser")
    terms = []

    for heading in soup.find_all(["h2", "h3"]):
        text = heading.get_text(strip=True)
        if len(text) > 100 or text.lower() in ("", "related stories", "share"):
            continue
        desc_parts = []
        for sib in heading.find_next_siblings():
            if sib.name in ("h2", "h3"):
                break
            desc_parts.append(sib.get_text(strip=True))
        desc = " ".join(desc_parts).strip()
        if desc:
            terms.append({"term": text, "description": desc, "source": "Royal Museums Greenwich"})

    return terms


def main():
    parser = argparse.ArgumentParser(description="Extract nautical metaphors from web archives")
    parser.add_argument("--cached", action="store_true", help="Use cached HTML files")
    args = parser.parse_args()

    all_terms = []

    for source in SOURCES:
        try:
            html = fetch_or_cache(source["url"], source["name"], args.cached)
            if "noaa" in source["url"]:
                terms = extract_noaa(html)
            elif "rmg" in source["url"]:
                terms = extract_rmg(html)
            else:
                terms = []
            all_terms.extend(terms)
            print(f"Extracted {len(terms)} terms from {source['name']}", file=sys.stderr)
        except Exception as e:
            print(f"Warning: Failed to fetch {source['name']}: {e}", file=sys.stderr)

    # Deduplicate by normalized term name
    seen = set()
    unique = []
    for t in all_terms:
        key = re.sub(r"[^a-z]", "", t["term"].lower())
        if key not in seen:
            seen.add(key)
            unique.append(t)

    json.dump(unique, sys.stdout, indent=2)
    print(f"\nTotal unique terms: {len(unique)}", file=sys.stderr)


if __name__ == "__main__":
    main()
