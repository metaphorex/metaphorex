#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""
Extract woodworking metaphor candidates from web sources.

Primary sources:
- The Quote Garden: woodworking quotes page (HTML list)
- ESL Vault: wood idioms (HTML list)

Wikipedia Glossary of Woodworking returns 403 and is not scrapable.
LumberJocks forum threads are JavaScript-rendered and not scrapable.

This script fetches what it can and outputs structured JSON to stdout.
The manifest.json was assembled from these outputs plus manual research.

Usage:
    uv run playbooks/carpentry-woodworking/scripts/extract_candidates.py
"""

import json
import sys

import requests
from bs4 import BeautifulSoup

SOURCES = {
    "quotegarden": {
        "url": "https://www.quotegarden.com/woodworking.html",
        "description": "Woodworking quotes and proverbs with attribution",
    },
    "eslvault": {
        "url": "https://eslvault.com/wood-idioms/",
        "description": "31 wood-related idioms and figurative expressions",
    },
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def fetch_quotegarden() -> list[dict]:
    """Extract woodworking quotes from The Quote Garden."""
    resp = requests.get(SOURCES["quotegarden"]["url"], headers=HEADERS, timeout=15)
    if resp.status_code != 200:
        print(f"WARN: Quote Garden returned {resp.status_code}", file=sys.stderr)
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    quotes = []

    for tag in soup.find_all(["p", "div"]):
        text = tag.get_text(strip=True)
        if text and len(text) > 20 and "~" in text:
            parts = text.rsplit("~", 1)
            if len(parts) == 2:
                quotes.append({
                    "text": parts[0].strip().strip("\u201c\u201d\""),
                    "attribution": parts[1].strip(),
                    "source_url": SOURCES["quotegarden"]["url"],
                })

    return quotes


def fetch_eslvault() -> list[dict]:
    """Extract wood idioms from ESL Vault."""
    resp = requests.get(SOURCES["eslvault"]["url"], headers=HEADERS, timeout=15)
    if resp.status_code != 200:
        print(f"WARN: ESL Vault returned {resp.status_code}", file=sys.stderr)
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    idioms = []

    for heading in soup.find_all(["h2", "h3", "strong"]):
        text = heading.get_text(strip=True)
        if text and len(text) > 3 and not text.startswith("Related"):
            explanation = ""
            next_el = heading.find_next(["p", "li"])
            if next_el:
                explanation = next_el.get_text(strip=True)

            idioms.append({
                "idiom": text,
                "explanation": explanation[:200] if explanation else "",
                "source_url": SOURCES["eslvault"]["url"],
            })

    return idioms


def main():
    results = {
        "sources_fetched": [],
        "quotes": [],
        "idioms": [],
    }

    print("Fetching Quote Garden...", file=sys.stderr)
    quotes = fetch_quotegarden()
    if quotes:
        results["sources_fetched"].append(SOURCES["quotegarden"]["url"])
        results["quotes"] = quotes
        print(f"  Found {len(quotes)} quotes", file=sys.stderr)

    print("Fetching ESL Vault...", file=sys.stderr)
    idioms = fetch_eslvault()
    if idioms:
        results["sources_fetched"].append(SOURCES["eslvault"]["url"])
        results["idioms"] = idioms
        print(f"  Found {len(idioms)} idioms", file=sys.stderr)

    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
