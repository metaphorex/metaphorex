#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""
Extract agricultural proverb and farming idiom candidates from structured web archives.

Sources:
  - https://glossophilia.org/2021/01/on-and-off-the-farm-some-phrases-straight-out-of-the-barnyard/
  - https://permacultureprinciples.com/permaculture-principles/
  - https://www.enchantedlearning.com/english/adages/farm.shtml

Produces structured JSON to stdout. Idempotent: same output on each run
(modulo source page changes).

Usage:
  uv run playbooks/agricultural-proverbs/scripts/extract_agricultural_candidates.py
"""

import json
import re
import sys

import requests
from bs4 import BeautifulSoup

GLOSSOPHILIA_URL = "https://glossophilia.org/2021/01/on-and-off-the-farm-some-phrases-straight-out-of-the-barnyard/"
ENCHANTED_URL = "https://www.enchantedlearning.com/english/adages/farm.shtml"

HEADERS = {
    "User-Agent": "Metaphorex-Prospector/1.0 (research; https://github.com/metaphorex/metaphorex)"
}


def fetch_glossophilia():
    """Extract farm phrases from Glossophilia's barnyard article."""
    candidates = []
    try:
        resp = requests.get(GLOSSOPHILIA_URL, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # The article uses bold text for phrase names within paragraphs
        content = soup.find("div", class_="entry-content") or soup.find("article")
        if not content:
            print("Warning: Could not find content div on Glossophilia", file=sys.stderr)
            return candidates

        # Extract bold phrases which are the idiom names
        for bold in content.find_all(["strong", "b"]):
            text = bold.get_text(strip=True)
            # Filter out navigation/header text, keep idiom phrases
            if len(text) > 5 and len(text) < 100:
                candidates.append({
                    "phrase": text,
                    "source_url": GLOSSOPHILIA_URL,
                })
    except Exception as e:
        print(f"Warning: Failed to fetch Glossophilia: {e}", file=sys.stderr)

    return candidates


def fetch_enchanted_learning():
    """Extract farm adages from EnchantedLearning."""
    candidates = []
    try:
        resp = requests.get(ENCHANTED_URL, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Look for bold/strong phrases which contain the adages
        for bold in soup.find_all(["strong", "b"]):
            text = bold.get_text(strip=True)
            if len(text) > 10 and any(c.isalpha() for c in text):
                candidates.append({
                    "phrase": text,
                    "source_url": ENCHANTED_URL,
                })
    except Exception as e:
        print(f"Warning: Failed to fetch EnchantedLearning: {e}", file=sys.stderr)

    return candidates


# Holmgren's 12 principles (canonical, from permacultureprinciples.com)
HOLMGREN_PRINCIPLES = [
    {"number": 1, "name": "Observe and Interact", "proverb": "Beauty is in the eye of the beholder"},
    {"number": 2, "name": "Catch and Store Energy", "proverb": "Make hay while the sun shines"},
    {"number": 3, "name": "Obtain a Yield", "proverb": "You can't work on an empty stomach"},
    {"number": 4, "name": "Apply Self-Regulation and Accept Feedback", "proverb": "The sins of the fathers are visited on the children unto the seventh generation"},
    {"number": 5, "name": "Use and Value Renewable Resources and Services", "proverb": "Let nature take its course"},
    {"number": 6, "name": "Produce No Waste", "proverb": "A stitch in time saves nine; Waste not, want not"},
    {"number": 7, "name": "Design from Patterns to Details", "proverb": "Can't see the wood for the trees"},
    {"number": 8, "name": "Integrate Rather Than Segregate", "proverb": "Many hands make light work"},
    {"number": 9, "name": "Use Small and Slow Solutions", "proverb": "The bigger they are, the harder they fall; Slow and steady wins the race"},
    {"number": 10, "name": "Use and Value Diversity", "proverb": "Don't put all your eggs in one basket"},
    {"number": 11, "name": "Use Edges and Value the Marginal", "proverb": "Don't think you are on the right track just because it's a well-beaten path"},
    {"number": 12, "name": "Creatively Use and Respond to Change", "proverb": "Vision is not seeing things as they are but as they will be"},
]


def main():
    """Collect candidates from all sources and output as JSON."""
    glossophilia_raw = fetch_glossophilia()
    enchanted_raw = fetch_enchanted_learning()

    output = {
        "sources": {
            "glossophilia": {
                "url": GLOSSOPHILIA_URL,
                "raw_count": len(glossophilia_raw),
                "phrases": [c["phrase"] for c in glossophilia_raw],
            },
            "enchanted_learning": {
                "url": ENCHANTED_URL,
                "raw_count": len(enchanted_raw),
                "phrases": [c["phrase"] for c in enchanted_raw],
            },
            "holmgren_principles": {
                "url": "https://permacultureprinciples.com/permaculture-principles/",
                "count": len(HOLMGREN_PRINCIPLES),
                "principles": HOLMGREN_PRINCIPLES,
            },
        },
        "total_raw": len(glossophilia_raw) + len(enchanted_raw) + len(HOLMGREN_PRINCIPLES),
    }

    json.dump(output, sys.stdout, indent=2)
    print(file=sys.stdout)  # trailing newline


if __name__ == "__main__":
    main()
