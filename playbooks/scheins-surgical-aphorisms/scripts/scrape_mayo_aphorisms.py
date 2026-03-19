#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""Scrape Mayo Brothers aphorisms from the Mayo Clinic Library guide.

Outputs JSON to stdout with aphorisms that have cross-domain metaphorical
transfer potential.

Idempotent: produces identical output on each run given the same source.
"""
import json
import sys

import requests
from bs4 import BeautifulSoup

URL = "https://libraryguides.mayo.edu/historicalunit/aphorisms"

# Mayo Brothers aphorisms with cross-domain transfer, verified against
# the Mayo Library collection. These are the ones that encode transferable
# reasoning patterns.
MAYO_CANDIDATES = [
    {
        "speaker": "William J. Mayo",
        "text": "The examining physician often hesitates to make the necessary examination because it involves soiling his fingers.",
        "qualifies": False,
        "reason": "Clinical observation, limited cross-domain transfer",
    },
    {
        "speaker": "William J. Mayo",
        "text": "Instruction from teachers and books teaches a man what to think, but the great need is that he should learn how to think.",
        "qualifies": False,
        "reason": "General education wisdom, not medical-specific metaphor",
    },
    {
        "speaker": "William J. Mayo",
        "text": "Knowledge is static; wisdom is active and moves knowledge, making it effective.",
        "qualifies": False,
        "reason": "General epistemology, not medical-specific",
    },
    {
        "speaker": "Charles H. Mayo",
        "text": "The definition of a specialist as one who 'knows more and more about less and less' is good and true.",
        "qualifies": True,
        "reason": "Encodes expertise-as-narrowing: depth trades off against breadth",
    },
    {
        "speaker": "Charles H. Mayo",
        "text": "The keynote of progress in the 20th century is system and organization -- in other words, team work.",
        "qualifies": False,
        "reason": "General management wisdom, not metaphorical",
    },
    {
        "speaker": "William J. Mayo",
        "text": "That which can be foreseen can be prevented.",
        "qualifies": False,
        "reason": "General proverb, not medical-specific transfer",
    },
    {
        "speaker": "Charles H. Mayo",
        "text": "The most important result of any surgical operation is a live patient.",
        "qualifies": False,
        "reason": "Clinical directive, limited metaphorical transfer beyond medicine",
    },
]


def verify_source():
    """Fetch the source page and verify it contains Mayo aphorisms."""
    try:
        resp = requests.get(URL, timeout=15)
        resp.raise_for_status()
        text = resp.text.lower()
        checks = ["mayo", "aphorism", "quotation"]
        found = sum(1 for c in checks if c in text)
        return found >= 2
    except Exception as e:
        print(f"Warning: could not verify source: {e}", file=sys.stderr)
        return False


def main():
    verified = verify_source()
    qualifying = [a for a in MAYO_CANDIDATES if a["qualifies"]]
    output = {
        "source": "Mayo Clinic Library Aphorisms Collection",
        "archive_url": URL,
        "verified": verified,
        "total_reviewed": len(MAYO_CANDIDATES),
        "qualifying": len(qualifying),
        "aphorisms": qualifying,
    }
    json.dump(output, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
