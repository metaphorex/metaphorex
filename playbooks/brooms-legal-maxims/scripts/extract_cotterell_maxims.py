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

    Cotterell's text uses bold/italic for Latin maxims followed by
    English translations in regular text. Structure:
    <p><b>Latin maxim</b> -- "English translation"</p>
    """
    soup = BeautifulSoup(html, "html.parser")
    maxims = []

    for p in soup.find_all("p"):
        text = p.get_text(strip=True)
        # Look for patterns: Latin text followed by dash and English
        # Cotterell uses em-dashes and quotes
        match = re.match(
            r'^([A-Z][a-z].*?(?:est|lex|non|jus|qui|nemo|res|ubi|omni|cum|pro|quod|sine|ex|in|de|ad|per|sub|super|contra|inter|ante|post|ultra|infra|supra|intra|extra|circa|prope|versus|erga|apud|coram|palam|clam|procul|secundum)\b.*?)\s*[-—]\s*["\u201c](.+?)["\u201d]',
            text,
            re.IGNORECASE,
        )
        if match:
            latin = match.group(1).strip()
            english = match.group(2).strip()
            if len(latin) > 5 and len(english) > 5:
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

    Halkerston organizes alphabetically with Latin maxims as entries
    followed by English translations.
    """
    soup = BeautifulSoup(html, "html.parser")
    maxims = []

    for p in soup.find_all("p"):
        text = p.get_text(separator=" ", strip=True)
        # Halkerston: Latin phrase, then translation
        # Many entries have the form: "Latin text. English translation."
        # or use dash/colon separators
        match = re.match(
            r'^([A-Z][a-z].*?[.;])\s*[-—:]\s*(.+?)\.?\s*$',
            text,
        )
        if match:
            latin = match.group(1).strip().rstrip(".;")
            english = match.group(2).strip()
            if (
                len(latin) > 10
                and len(english) > 10
                and any(
                    w in latin.lower()
                    for w in [
                        "est", "non", "lex", "jus", "qui", "nemo",
                        "res", "ubi", "quod", "sine", "nulla",
                    ]
                )
            ):
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
