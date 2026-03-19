# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""Scrape publicly accessible structured sources for theatrical directing concepts.

Primary source (Hauser & Reich, Notes on Directing) is a copyrighted book
with no open-access digital archive. The archive.org copies are borrow-only.
This script scrapes the SUPPLEMENTARY structured sources that are publicly
accessible, producing a partial candidate list. LLM gap-fill is required
for the primary source candidates.

Scraped sources:
  1. Goodreads quotes page for Notes on Directing (public quotes)
  2. Fluidself.org Impro summary (Johnstone concepts)
  3. Dramatics.org Viewpoints article (Bogart/Overlie concepts)

Output: JSON to stdout with extracted concepts keyed by source.
"""

import json
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Metaphorex research bot; +https://github.com/metaphorex/metaphorex)"
}


def scrape_goodreads_quotes() -> list[dict]:
    """Scrape publicly visible quotes from Notes on Directing on Goodreads."""
    url = "https://www.goodreads.com/work/quotes/246935-notes-on-directing"
    quotes = []
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        # Goodreads quote text is in <div class="quoteText">
        for qt in soup.select(".quoteText"):
            text = qt.get_text(strip=True)
            # Clean up attribution
            text = re.sub(r"\s*---?\s*Frank Hauser.*$", "", text)
            text = re.sub(r"\s*---?\s*Russell Reich.*$", "", text)
            if text and len(text) > 20:
                quotes.append({"text": text.strip(), "source_url": url})
    except Exception as e:
        print(f"Warning: Goodreads scrape failed: {e}", file=sys.stderr)
    return quotes


def scrape_fluidself_impro() -> list[dict]:
    """Scrape structured Impro concepts from fluidself.org book notes."""
    url = "https://fluidself.org/books/art/impro"
    concepts = []
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        # Extract section headings and bullet points
        article = soup.select_one("article") or soup.select_one(".post-content") or soup
        current_section = "general"
        for el in article.find_all(["h2", "h3", "li", "p", "strong"]):
            if el.name in ("h2", "h3"):
                current_section = el.get_text(strip=True).lower()
            elif el.name == "li":
                text = el.get_text(strip=True)
                if len(text) > 15:
                    concepts.append({
                        "section": current_section,
                        "text": text,
                        "source_url": url,
                    })
    except Exception as e:
        print(f"Warning: Fluidself scrape failed: {e}", file=sys.stderr)
    return concepts


def scrape_dramatics_viewpoints() -> list[dict]:
    """Scrape Viewpoints definitions from Dramatics Magazine."""
    url = "https://dramatics.org/understanding-viewpoints/"
    viewpoints = []
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        # Look for viewpoint definitions in the article body
        article = soup.select_one("article") or soup.select_one(".entry-content") or soup
        for el in article.find_all(["p", "li", "h2", "h3", "strong"]):
            text = el.get_text(strip=True)
            # Look for viewpoint names (typically bold or in headers)
            if any(vp in text.lower() for vp in [
                "spatial relationship", "kinesthetic response", "shape",
                "gesture", "repetition", "architecture", "tempo",
                "duration", "topography", "pitch", "dynamic", "timbre",
                "silence", "acceleration",
            ]):
                viewpoints.append({
                    "text": text,
                    "source_url": url,
                })
    except Exception as e:
        print(f"Warning: Dramatics scrape failed: {e}", file=sys.stderr)
    return viewpoints


def main():
    results = {
        "scraped_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "sources": {
            "goodreads_quotes": {
                "url": "https://www.goodreads.com/work/quotes/246935-notes-on-directing",
                "description": "Publicly visible quotes from Notes on Directing",
                "data": scrape_goodreads_quotes(),
            },
            "fluidself_impro": {
                "url": "https://fluidself.org/books/art/impro",
                "description": "Structured Impro concepts from fluidself.org",
                "data": scrape_fluidself_impro(),
            },
            "dramatics_viewpoints": {
                "url": "https://dramatics.org/understanding-viewpoints/",
                "description": "Viewpoints definitions from Dramatics Magazine",
                "data": scrape_dramatics_viewpoints(),
            },
        },
        "notes": [
            "Primary source (Hauser & Reich Notes on Directing) is copyrighted.",
            "Archive.org copies are borrow-only, not freely scrapable.",
            "This script covers supplementary structured sources only.",
            "Primary source candidates require LLM gap-fill.",
        ],
    }
    json.dump(results, sys.stdout, indent=2)
    print(file=sys.stdout)  # trailing newline


if __name__ == "__main__":
    main()
