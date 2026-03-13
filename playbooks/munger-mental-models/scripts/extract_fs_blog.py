#!/usr/bin/env python3
"""
Extract mental model names and categories from the Farnam Street
mental models page (fs.blog/mental-models/).

This script fetches the FS Blog mental models index page, parses out
model names and their category headings, and writes structured JSON
to stdout. Used as one of two archive sources for the Munger mental
models prospecting project.

Usage:
    python extract_fs_blog.py > fs_blog_models.json

Requires: requests, beautifulsoup4
"""

import json
import re
import sys

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print(
        "Install dependencies: pip install requests beautifulsoup4",
        file=sys.stderr,
    )
    sys.exit(1)

URL = "https://fs.blog/mental-models/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def fetch_and_parse():
    """Fetch the FS Blog mental models page and extract model entries."""
    resp = requests.get(URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # The page organizes models under h2 category headings with
    # individual model names in h3 tags or bold text within the
    # entry-content div.
    content = soup.find("div", class_="entry-content")
    if not content:
        # Fallback: try article body
        content = soup.find("article") or soup

    models = []
    current_category = "Uncategorized"

    for tag in content.find_all(["h2", "h3", "strong"]):
        text = tag.get_text(strip=True)
        if not text:
            continue

        if tag.name == "h2":
            current_category = text
        elif tag.name == "h3":
            models.append({
                "name": text,
                "category": current_category,
                "source_url": URL,
            })
        elif tag.name == "strong" and tag.parent and tag.parent.name in ("p", "li"):
            # Some models appear as bold text in paragraphs
            # Filter out short labels or non-model text
            if len(text) > 3 and not text.endswith(":"):
                models.append({
                    "name": text,
                    "category": current_category,
                    "source_url": URL,
                })

    return {
        "source": "fs.blog/mental-models/",
        "fetched_url": URL,
        "model_count": len(models),
        "models": models,
    }


if __name__ == "__main__":
    result = fetch_and_parse()
    json.dump(result, sys.stdout, indent=2)
    print(file=sys.stdout)  # trailing newline
