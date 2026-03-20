#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""
Scrape ACT metaphor archives to extract named metaphor-interventions.

Sources:
  1. ACBS (Association for Contextual Behavioral Science) metaphors page
     https://contextualscience.org/metaphors
  2. Contextual Consulting A-Z of ACT Metaphors
     https://contextualconsulting.co.uk/therapy-approaches/a-z-of-act-metaphors

Outputs JSON to stdout with structured metaphor data.
Idempotent: same input pages produce same output.
"""
import json
import re
import sys

import requests
from bs4 import BeautifulSoup


ACBS_URL = "https://contextualscience.org/metaphors"
CC_URL = "https://contextualconsulting.co.uk/therapy-approaches/a-z-of-act-metaphors"


def scrape_acbs(url: str) -> list[dict]:
    """Scrape metaphor names from the ACBS metaphors page.

    The ACBS page lists metaphors as linked items in a community-contributed
    collection. We extract text from links and headings that reference
    specific named metaphors.
    """
    resp = requests.get(url, timeout=30, headers={"User-Agent": "metaphorex-prospector/1.0"})
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    names = []
    seen = set()

    # Look for metaphor entries in the main content area
    for el in soup.select("a, h2, h3, h4, li"):
        text = el.get_text(strip=True)
        # Filter to plausible metaphor names (3-80 chars, not navigation)
        if 3 < len(text) < 80 and text.lower() not in seen:
            lower = text.lower()
            # Skip navigation, footer, and generic links
            if any(skip in lower for skip in [
                "home", "login", "register", "search", "contact",
                "about", "privacy", "cookie", "menu", "navigation",
                "copyright", "site map", "forum", "blog",
            ]):
                continue
            seen.add(lower)
            names.append({
                "name": text,
                "source_url": url,
            })

    return names


def scrape_contextual_consulting(url: str) -> list[dict]:
    """Scrape the A-Z ACT metaphors from Contextual Consulting.

    This page lists metaphors alphabetically with brief descriptions.
    We extract headings and list items that contain known ACT metaphor
    keywords.
    """
    resp = requests.get(url, timeout=30, headers={"User-Agent": "metaphorex-prospector/1.0"})
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    metaphors = []
    seen = set()

    # Known ACT metaphor keywords for matching
    keywords = [
        "bus", "passenger", "quicksand", "tug", "war", "monster",
        "leaves", "stream", "chessboard", "chess", "sky", "weather",
        "party", "guest", "struggle", "switch", "clean", "dirty",
        "radio", "compass", "anchor", "choice", "finger", "trap",
        "ball", "pool", "demon", "boat", "hands", "thoughts",
        "hopelessness", "defusion", "flexibility", "ship",
        "garden", "swamp", "quicksand", "rope",
    ]

    for el in soup.find_all(["h2", "h3", "h4", "li", "strong", "b"]):
        text = el.get_text(strip=True)
        lower = text.lower()
        if lower in seen or len(text) < 3 or len(text) > 120:
            continue
        if any(kw in lower for kw in keywords):
            seen.add(lower)
            metaphors.append({
                "name": text,
                "source_url": url,
            })

    return metaphors


def main():
    results = {
        "sources": [ACBS_URL, CC_URL],
        "acbs_metaphors": [],
        "contextual_consulting": [],
        "errors": [],
    }

    try:
        results["acbs_metaphors"] = scrape_acbs(ACBS_URL)
    except Exception as e:
        results["errors"].append(f"ACBS scrape failed: {e}")
        print(f"Warning: Failed to scrape ACBS: {e}", file=sys.stderr)

    try:
        results["contextual_consulting"] = scrape_contextual_consulting(CC_URL)
    except Exception as e:
        results["errors"].append(f"Contextual Consulting scrape failed: {e}")
        print(f"Warning: Failed to scrape Contextual Consulting: {e}", file=sys.stderr)

    json.dump(results, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
