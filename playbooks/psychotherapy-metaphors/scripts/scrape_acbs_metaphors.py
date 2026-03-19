#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""
Scrape the ACBS (Association for Contextual Behavioral Science) metaphors page
to extract named ACT metaphors.

Source: https://contextualscience.org/metaphors
Backup: https://contextualconsulting.co.uk/therapy-approaches/a-z-of-act-metaphors

Outputs JSON array of metaphor names to stdout.
"""
import json
import sys

import requests
from bs4 import BeautifulSoup


URLS = [
    "https://contextualscience.org/metaphors",
    "https://contextualconsulting.co.uk/therapy-approaches/a-z-of-act-metaphors",
]


def scrape_acbs(url: str) -> list[str]:
    """Scrape metaphor names from the ACBS metaphors page."""
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    names = []
    # ACBS page lists metaphors as links in a content area
    for link in soup.select("a"):
        text = link.get_text(strip=True)
        # Filter to likely metaphor titles (skip navigation, etc.)
        if len(text) > 3 and "metaphor" in text.lower() or "ACT" in text:
            names.append(text)

    return names


def scrape_contextual_consulting(url: str) -> list[dict]:
    """Scrape the A-Z ACT metaphors from Contextual Consulting."""
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    metaphors = []
    # Look for headings or list items containing metaphor names
    for heading in soup.find_all(["h2", "h3", "h4", "li"]):
        text = heading.get_text(strip=True)
        if any(keyword in text.lower() for keyword in [
            "metaphor", "bus", "quicksand", "tug", "leaves",
            "monster", "compass", "anchor", "radio", "sky",
            "weather", "party", "guest", "garden", "ship",
        ]):
            metaphors.append({"name": text, "source_url": url})

    return metaphors


def main():
    results = {"acbs_metaphors": [], "contextual_consulting": []}

    for url in URLS:
        try:
            if "contextualscience" in url:
                names = scrape_acbs(url)
                results["acbs_metaphors"] = names
            else:
                metaphors = scrape_contextual_consulting(url)
                results["contextual_consulting"] = metaphors
        except Exception as e:
            print(f"Warning: Failed to scrape {url}: {e}", file=sys.stderr)

    json.dump(results, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
