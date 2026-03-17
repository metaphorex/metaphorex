#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""
Extract TPS glossary terms from Toyota UK Magazine and Lean Production glossary.

Produces structured JSON to stdout. Idempotent: same output on each run
(modulo source page changes).

Archives:
  - https://mag.toyota.co.uk/toyota-production-system-glossary/
  - https://www.leanproduction.com/lean-glossary/

Usage:
  uv run scripts/extract_tps_glossary.py
"""

import json
import re
import sys

import requests
from bs4 import BeautifulSoup

TOYOTA_UK_URL = "https://mag.toyota.co.uk/toyota-production-system-glossary/"
LEAN_PROD_URL = "https://www.leanproduction.com/lean-glossary/"
LEI_LEXICON_URL = "https://www.lean.org/explore-lean/lexicon-terms/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Metaphorex research bot; +https://github.com/metaphorex/metaphorex)"
}


def fetch_toyota_uk() -> list[dict]:
    """Extract glossary terms from Toyota UK Magazine TPS glossary."""
    resp = requests.get(TOYOTA_UK_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    terms = []
    for strong in soup.find_all(["strong", "b"]):
        text = strong.get_text(strip=True)
        if text and len(text) > 2 and not text.startswith("http"):
            parent = strong.parent
            if parent:
                full_text = parent.get_text(strip=True)
                definition = full_text.replace(text, "", 1).strip(" -:\u2013")
                if definition and len(definition) > 10:
                    terms.append({
                        "term": text,
                        "definition": definition,
                        "source_url": TOYOTA_UK_URL,
                    })
    return terms


def fetch_lean_production() -> list[dict]:
    """Extract glossary terms from LeanProduction.com."""
    resp = requests.get(LEAN_PROD_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    terms = []
    for heading in soup.find_all(["h2", "h3"]):
        term_name = heading.get_text(strip=True)
        if not term_name or len(term_name) < 2:
            continue
        if term_name.lower() in ("lean glossary", "glossary", "menu", "search"):
            continue
        definition = ""
        for sibling in heading.find_next_siblings():
            if sibling.name in ("h2", "h3"):
                break
            if sibling.name == "p":
                definition = sibling.get_text(strip=True)
                break
        if definition:
            terms.append({
                "term": term_name,
                "definition": definition,
                "source_url": LEAN_PROD_URL,
            })
    return terms


def fetch_lei_lexicon() -> list[dict]:
    """Extract term list from Lean Enterprise Institute lexicon."""
    resp = requests.get(LEI_LEXICON_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    terms = []
    for link in soup.find_all("a"):
        href = link.get("href", "")
        if "/lexicon-terms/" in href and href != "/explore-lean/lexicon-terms/":
            term_name = link.get_text(strip=True)
            if term_name and len(term_name) > 1:
                terms.append({
                    "term": term_name,
                    "definition": "",
                    "source_url": f"https://www.lean.org{href}" if href.startswith("/") else href,
                })
    return terms


def main():
    all_sources = {}
    errors = []

    for name, fetcher in [
        ("toyota_uk", fetch_toyota_uk),
        ("lean_production", fetch_lean_production),
        ("lei_lexicon", fetch_lei_lexicon),
    ]:
        try:
            results = fetcher()
            all_sources[name] = results
            print(f"  [{name}] Extracted {len(results)} terms", file=sys.stderr)
        except Exception as e:
            errors.append(f"{name}: {e}")
            all_sources[name] = []
            print(f"  [{name}] ERROR: {e}", file=sys.stderr)

    # Merge: deduplicate by normalized term name
    merged = {}
    for source_name, terms in all_sources.items():
        for t in terms:
            key = re.sub(r"[^a-z0-9]", "", t["term"].lower())
            if key not in merged:
                merged[key] = {
                    "term": t["term"],
                    "definitions": {},
                    "source_urls": [],
                }
            if t["definition"]:
                merged[key]["definitions"][source_name] = t["definition"]
            if t["source_url"] not in merged[key]["source_urls"]:
                merged[key]["source_urls"].append(t["source_url"])

    output = {
        "extracted_from": [TOYOTA_UK_URL, LEAN_PROD_URL, LEI_LEXICON_URL],
        "term_count": len(merged),
        "errors": errors,
        "terms": list(merged.values()),
    }

    json.dump(output, sys.stdout, indent=2, ensure_ascii=False)
    print(file=sys.stdout)


if __name__ == "__main__":
    main()
