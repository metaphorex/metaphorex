#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""
Scrape Andy Riley's 'How to Talk Comedy Writer' glossary.

Fetches the most recent version of the glossary from misterandyriley.com
and outputs structured JSON to stdout. Idempotent -- same page yields
same output (modulo page edits by Riley).
"""

import json
import re
import sys

import requests
from bs4 import BeautifulSoup

URLS = [
    "https://misterandyriley.com/2019/10/25/how-to-talk-comedy-writer-updated-25th-october-2019/",
    "https://misterandyriley.com/2018/10/12/how-to-talk-comedy-writer-updated-3/",
    "https://misterandyriley.com/2017/03/31/how-to-talk-comedy-writer-updated-2/",
    "https://misterandyriley.com/2014/12/16/how-to-talk-comedy-writer/",
]


def fetch_glossary(url: str) -> list[dict]:
    """Fetch a single glossary page and extract term/definition pairs."""
    resp = requests.get(url, timeout=30, headers={"User-Agent": "Metaphorex-Prospector/1.0"})
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # Riley's WordPress theme uses class="box" for the post content area;
    # fall back to "entry-content" if the theme changes.
    entry_content = soup.find("div", class_="box") or soup.find("div", class_="entry-content")
    if not entry_content:
        print(f"WARNING: No content div found at {url}", file=sys.stderr)
        return []

    terms = []
    # Riley uses <strong> or <b> for term names, followed by definition text
    for p in entry_content.find_all("p"):
        text = p.get_text(strip=True)
        if not text:
            continue
        # Look for bold terms -- Riley formats as "TERM -- definition" or "TERM: definition"
        bold = p.find(["strong", "b"])
        if bold:
            term_name = bold.get_text(strip=True).rstrip(".:- ")
            # Get the full paragraph text and extract the definition after the term
            full_text = p.get_text(strip=True)
            # Remove the term name prefix to get definition
            definition = full_text[len(term_name):].lstrip(".:- –—\u2013\u2014 ")
            if term_name and definition:
                terms.append({
                    "term": term_name,
                    "definition": definition,
                    "source_url": url,
                })

    return terms


def main():
    all_terms = {}
    # Fetch most recent first; earlier versions may have terms dropped later
    for url in URLS:
        try:
            terms = fetch_glossary(url)
            for t in terms:
                # Deduplicate by normalized term name
                key = re.sub(r"[^a-z0-9]", "", t["term"].lower())
                if key not in all_terms:
                    all_terms[key] = t
            print(f"Fetched {len(terms)} terms from {url}", file=sys.stderr)
        except Exception as e:
            print(f"ERROR fetching {url}: {e}", file=sys.stderr)

    result = {
        "source": "Andy Riley - How to Talk Comedy Writer",
        "urls": URLS,
        "terms": sorted(all_terms.values(), key=lambda t: t["term"].lower()),
        "total": len(all_terms),
    }
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    print(file=sys.stdout)  # trailing newline


if __name__ == "__main__":
    main()
