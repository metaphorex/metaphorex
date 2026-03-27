#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""Scrape the 13 Laws of the House of God from wanderings.net.

Outputs JSON to stdout with the laws that have cross-domain metaphorical
transfer potential. Each law includes the original text, the law number,
and whether it qualifies for the manifest.

Idempotent: produces identical output on each run given the same source.
"""
import json
import sys

import requests
from bs4 import BeautifulSoup

URL = "https://www.wanderings.net/notebook/Main/HouseOfGodLaws"

# The 13 Laws with cross-domain assessment.
# We hardcode these because the page structure is simple and stable,
# and we need to annotate which ones have cross-domain transfer.
LAWS = [
    {
        "number": 1,
        "text": "Gomers don't die.",
        "qualifies": False,
        "reason": "Domain-specific medical slang, no cross-domain transfer",
    },
    {
        "number": 2,
        "text": "Gomers go to ground.",
        "qualifies": False,
        "reason": "Domain-specific medical slang",
    },
    {
        "number": 3,
        "text": "At a cardiac arrest, the first procedure is to take your own pulse.",
        "qualifies": True,
        "reason": "Encodes composure-under-pressure: assess yourself before acting in crisis",
    },
    {
        "number": 4,
        "text": "The patient is the one with the disease.",
        "qualifies": True,
        "reason": "Encodes professional detachment: the helper is not the one needing help",
    },
    {
        "number": 5,
        "text": "Placement comes first.",
        "qualifies": False,
        "reason": "Domain-specific hospital logistics",
    },
    {
        "number": 6,
        "text": "There is no body cavity that cannot be reached with a #14 needle and a good strong arm.",
        "qualifies": False,
        "reason": "Domain-specific surgical technique",
    },
    {
        "number": 7,
        "text": "Age + BUN = Lasix dose.",
        "qualifies": False,
        "reason": "Domain-specific clinical formula",
    },
    {
        "number": 8,
        "text": "They can always hurt you more.",
        "qualifies": False,
        "reason": "Too context-dependent on hospital hierarchy",
    },
    {
        "number": 9,
        "text": "The only good admission is a dead admission.",
        "qualifies": False,
        "reason": "Domain-specific dark humor",
    },
    {
        "number": 10,
        "text": "If you don't take a temperature, you can't find a fever.",
        "qualifies": True,
        "reason": "Encodes measurement-creates-knowledge: unobserved problems don't exist in the record",
    },
    {
        "number": 11,
        "text": "Show me a medical student who only triples my work and I will kiss his feet.",
        "qualifies": False,
        "reason": "Domain-specific training complaint",
    },
    {
        "number": 12,
        "text": "If the radiology resident and the medical student both see a lesion on the chest x-ray, there can be no lesion there.",
        "qualifies": False,
        "reason": "Domain-specific diagnostic humor",
    },
    {
        "number": 13,
        "text": "The delivery of good medical care is to do as much nothing as possible.",
        "qualifies": True,
        "reason": "Encodes minimal-intervention wisdom: restraint as the highest form of action",
    },
]


def verify_source():
    """Fetch the source page and verify the laws are still there."""
    try:
        resp = requests.get(URL, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        text = soup.get_text().lower()
        # Spot-check a few laws
        checks = [
            "take your own pulse",
            "patient is the one with the disease",
            "do as much nothing as possible",
        ]
        found = sum(1 for c in checks if c in text)
        return found >= 2  # At least 2 of 3 found
    except Exception as e:
        print(f"Warning: could not verify source: {e}", file=sys.stderr)
        return False


def main():
    verified = verify_source()
    qualifying = [law for law in LAWS if law["qualifies"]]
    output = {
        "source": "House of God (Samuel Shem, 1978)",
        "archive_url": URL,
        "verified": verified,
        "total_laws": len(LAWS),
        "qualifying_laws": len(qualifying),
        "laws": qualifying,
    }
    json.dump(output, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
