#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""
Scrape the Wikipedia Glossary of Ecology to verify that candidate ecological
concepts are real, defined terms. Outputs JSON with term names and definitions.

This script is a verification tool: it confirms that manifest candidates
correspond to genuine ecological terminology, not invented concepts.

Usage:
    uv run playbooks/ecological-metaphors/scripts/scrape_wiki_ecology.py
"""

import json
import re
import sys

import requests
from bs4 import BeautifulSoup

GLOSSARY_URL = "https://en.wikipedia.org/wiki/Glossary_of_ecology"

# Manifest candidates mapped to their expected Wikipedia glossary terms.
# Some candidates use metaphorical names; this maps them to ecological terms.
CANDIDATE_TERMS = {
    "keystone-species": ["keystone species"],
    "tipping-point": ["tipping point", "regime shift"],
    "ecosystem-as-metaphor": ["ecosystem"],
    "invasive-species-as-metaphor": ["invasive species", "introduced species"],
    "carrying-capacity": ["carrying capacity"],
    "food-chain": ["food chain", "food web", "trophic level"],
    "ecological-succession": ["ecological succession", "succession"],
    "pioneer-species": ["pioneer species"],
    "apex-predator": ["apex predator"],
    "trophic-cascade": ["trophic cascade"],
    "symbiosis-as-metaphor": ["symbiosis"],
    "parasitism-as-metaphor": ["parasitism", "parasite"],
    "mutualism-as-metaphor": ["mutualism"],
    "balance-of-nature": ["balance of nature"],
    "adaptive-cycle": ["adaptive cycle", "resilience"],
    "panarchy": ["panarchy"],
    "ecological-resilience": ["resilience", "ecological resilience"],
    "ecological-niche": ["ecological niche", "niche"],
    "monoculture": ["monoculture"],
    "dead-zone": ["dead zone"],
    "indicator-species": ["indicator species", "bioindicator"],
    "edge-effect": ["edge effect", "ecotone"],
    "ecological-footprint": ["ecological footprint"],
    "natural-capital": ["natural capital", "ecosystem services"],
    "seed-and-soil": [],  # medical metaphor, not in ecology glossary
    "pollinator-as-metaphor": ["pollination", "pollinator"],
    "old-growth-vs-clear-cut": ["old-growth forest", "old growth"],
    "regime-shift": ["regime shift"],
    "ecological-arms-race": ["coevolution", "arms race"],
}


def fetch_glossary() -> BeautifulSoup:
    """Fetch and parse the Wikipedia Glossary of Ecology."""
    headers = {
        "User-Agent": "MetaphorexBot/1.0 (metaphor research project; "
        "https://github.com/metaphorex/metaphorex)"
    }
    resp = requests.get(GLOSSARY_URL, headers=headers, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def extract_terms(soup: BeautifulSoup) -> dict[str, str]:
    """Extract term-definition pairs from the glossary.

    The Wikipedia glossary uses <dt> / <dd> (definition list) markup, or
    bolded terms at the start of list items.
    """
    terms: dict[str, str] = {}

    # Try <dt>/<dd> pairs first
    for dt in soup.find_all("dt"):
        term_text = dt.get_text(strip=True).lower()
        dd = dt.find_next_sibling("dd")
        if dd:
            definition = dd.get_text(strip=True)[:300]
            terms[term_text] = definition

    # Also try <li> items with bold opening (common Wikipedia glossary format)
    for li in soup.find_all("li"):
        b = li.find("b")
        if b:
            term_text = b.get_text(strip=True).lower()
            full_text = li.get_text(strip=True)
            # Remove the bold term from the start to get the definition
            definition = full_text[len(b.get_text(strip=True)):].strip()
            definition = re.sub(r"^[\s\-\u2013\u2014:]+", "", definition)[:300]
            if definition:
                terms[term_text] = definition

    return terms


def verify_candidates(
    glossary_terms: dict[str, str],
) -> list[dict]:
    """Check each candidate against the glossary."""
    results = []
    for slug, search_terms in CANDIDATE_TERMS.items():
        found = False
        matched_term = None
        definition = None

        for search in search_terms:
            search_lower = search.lower()
            # Exact match
            if search_lower in glossary_terms:
                found = True
                matched_term = search
                definition = glossary_terms[search_lower]
                break
            # Substring match
            for gt, gd in glossary_terms.items():
                if search_lower in gt or gt in search_lower:
                    found = True
                    matched_term = gt
                    definition = gd
                    break
            if found:
                break

        results.append(
            {
                "slug": slug,
                "search_terms": search_terms,
                "found_in_glossary": found,
                "matched_term": matched_term,
                "definition": definition,
            }
        )

    return results


def main() -> None:
    print("Fetching Wikipedia Glossary of Ecology...", file=sys.stderr)
    soup = fetch_glossary()

    print("Extracting terms...", file=sys.stderr)
    glossary_terms = extract_terms(soup)
    print(f"Found {len(glossary_terms)} terms in glossary.", file=sys.stderr)

    print("Verifying candidates...", file=sys.stderr)
    results = verify_candidates(glossary_terms)

    found_count = sum(1 for r in results if r["found_in_glossary"])
    total = len(results)
    print(
        f"Verified {found_count}/{total} candidates in glossary.",
        file=sys.stderr,
    )

    # Output JSON to stdout
    output = {
        "glossary_url": GLOSSARY_URL,
        "glossary_term_count": len(glossary_terms),
        "candidates_verified": found_count,
        "candidates_total": total,
        "results": results,
    }
    json.dump(output, sys.stdout, indent=2)
    print(file=sys.stdout)


if __name__ == "__main__":
    main()
