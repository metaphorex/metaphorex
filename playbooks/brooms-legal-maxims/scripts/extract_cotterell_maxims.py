#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "beautifulsoup4"]
# ///
"""
Extract legal maxims from Cotterell's Collection of Latin Maxims (Gutenberg #68465)
and Halkerston's Collection of Latin Maxims & Rules (Gutenberg #72240).

Outputs structured JSON to stdout with Latin text, English translation, and source.
These are the primary Gutenberg archives cited in import issue #1227.
"""

import json
import re
import sys

import httpx
from bs4 import BeautifulSoup

SOURCES = {
    "cotterell": {
        "url": "https://www.gutenberg.org/files/68465/68465-h/68465-h.htm",
        "title": "A Collection of Latin Maxims and Phrases (Cotterell, 1858)",
    },
    "halkerston": {
        "url": "https://www.gutenberg.org/cache/epub/72240/pg72240-images.html",
        "title": "A Collection of Latin Maxims & Rules (Halkerston, 1823)",
    },
}


def fetch_html(url: str) -> str:
    """Fetch HTML content from a URL."""
    resp = httpx.get(url, follow_redirects=True, timeout=30)
    resp.raise_for_status()
    return resp.text


def extract_cotterell(html: str) -> list[dict]:
    """Extract maxims from Cotterell's collection.

    Cotterell's HTML uses this structure for each maxim entry:
      <p class='c008'>
        <strong><span lang="la">Latin maxim text.</span></strong>
        <em>English translation.</em>
      </p>
    Explanatory paragraphs follow with class='c005'.
    """
    soup = BeautifulSoup(html, "html.parser")
    maxims = []

    for p in soup.find_all("p", class_="c008"):
        strong = p.find("strong")
        em = p.find("em")
        if not strong or not em:
            continue

        latin = strong.get_text(strip=True)
        english = em.get_text(separator=" ", strip=True)

        # Strip leading number and asterisk: "* 1. Latin text" -> "Latin text"
        latin = re.sub(r"^\*?\s*\d+\.\s*", "", latin)

        # Skip entries that are too short to be real maxims
        if len(latin) < 5 or len(english) < 5:
            continue

        maxims.append(
            {
                "latin": latin,
                "english": english,
                "source_text": "cotterell",
            }
        )

    return maxims


def extract_halkerston(html: str) -> list[dict]:
    """Extract maxims from Halkerston's collection.

    Halkerston's HTML uses this structure:
      <p>Latin maxim text.</p>
      <div class="blockquot"><p>English translation.</p></div>
    Maxims are organized alphabetically with letter headings.
    """
    soup = BeautifulSoup(html, "html.parser")
    maxims = []

    for blockquot in soup.find_all("div", class_="blockquot"):
        # The Latin text is in the <p> immediately preceding the blockquot div
        prev = blockquot.find_previous_sibling()
        if not prev or prev.name != "p":
            continue

        latin = prev.get_text(separator=" ", strip=True)
        english = blockquot.get_text(separator=" ", strip=True)

        if len(latin) < 5 or len(english) < 5:
            continue

        maxims.append(
            {
                "latin": latin,
                "english": english,
                "source_text": "halkerston",
            }
        )

    return maxims


def main():
    all_maxims = []

    for source_key, source_info in SOURCES.items():
        print(f"Fetching {source_info['title']}...", file=sys.stderr)
        try:
            html = fetch_html(source_info["url"])
        except Exception as e:
            print(f"  Error fetching {source_key}: {e}", file=sys.stderr)
            continue

        if source_key == "cotterell":
            maxims = extract_cotterell(html)
        else:
            maxims = extract_halkerston(html)

        print(f"  Extracted {len(maxims)} maxims from {source_key}", file=sys.stderr)
        all_maxims.extend(maxims)

    output = {
        "sources": SOURCES,
        "total_extracted": len(all_maxims),
        "maxims": all_maxims,
    }
    json.dump(output, sys.stdout, indent=2, ensure_ascii=False)
    print(file=sys.stdout)  # trailing newline


if __name__ == "__main__":
    main()
