#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "beautifulsoup4"]
# ///
"""
Extract AI metaphors from structured web archives.

Sources:
1. Leon Furze, "AI Metaphors We Live By" (2024)
   https://leonfurze.com/2024/07/19/ai-metaphors-we-live-by-the-language-of-artificial-intelligence/
2. Matthijs Maas, "AI is Like..." (2023) - categories used for cross-reference
   https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4612468
3. Making Science Public, "AI Metaphor Observatory" (2025)
   https://makingsciencepublic.com/2025/11/14/making-the-case-for-an-ai-metaphor-observatory/

Outputs JSON to stdout with extracted candidates.
"""

import json
import sys

import httpx
from bs4 import BeautifulSoup


def fetch_furze_metaphors() -> list[dict]:
    """Scrape Leon Furze's 'AI Metaphors We Live By' blog post."""
    url = "https://leonfurze.com/2024/07/19/ai-metaphors-we-live-by-the-language-of-artificial-intelligence/"
    try:
        resp = httpx.get(url, follow_redirects=True, timeout=30)
        resp.raise_for_status()
    except httpx.HTTPError as e:
        print(f"Warning: Could not fetch Furze blog: {e}", file=sys.stderr)
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    content = soup.find("div", class_="entry-content") or soup.find("article")
    if not content:
        print("Warning: Could not find content div in Furze blog", file=sys.stderr)
        return []

    # Extract metaphors from tables and headings
    metaphors = []
    tables = content.find_all("table")
    for table in tables:
        rows = table.find_all("tr")
        for row in rows[1:]:  # skip header
            cells = row.find_all(["td", "th"])
            if len(cells) >= 2:
                name = cells[0].get_text(strip=True)
                desc = cells[1].get_text(strip=True) if len(cells) > 1 else ""
                if name and name.lower() not in ("metaphor", "category", "framing"):
                    metaphors.append({
                        "name": name,
                        "description": desc,
                        "source_url": url,
                    })

    # Also extract bold terms from paragraphs as potential metaphors
    for strong in content.find_all(["strong", "b"]):
        text = strong.get_text(strip=True)
        if len(text) > 3 and len(text) < 80 and text not in [m["name"] for m in metaphors]:
            parent = strong.parent
            if parent:
                context = parent.get_text(strip=True)[:200]
                metaphors.append({
                    "name": text,
                    "description": context,
                    "source_url": url,
                })

    return metaphors


def fetch_maas_categories() -> list[dict]:
    """
    Extract the 5-category framework from Maas's paper abstract/summary pages.
    The full PDF is behind SSRN; we use the structured summary from law-ai.org.
    """
    url = "https://law-ai.org/ai-policy-metaphors/"
    try:
        resp = httpx.get(url, follow_redirects=True, timeout=30)
        resp.raise_for_status()
    except httpx.HTTPError as e:
        print(f"Warning: Could not fetch Maas summary: {e}", file=sys.stderr)
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    content = soup.find("div", class_="entry-content") or soup.find("article") or soup
    text = content.get_text()

    # Extract listed metaphors/analogies
    metaphors = []
    lists = content.find_all(["ul", "ol"])
    for lst in lists:
        for li in lst.find_all("li"):
            item_text = li.get_text(strip=True)
            if len(item_text) > 5:
                metaphors.append({
                    "name": item_text[:100],
                    "description": item_text,
                    "source_url": url,
                })

    return metaphors


def main():
    furze = fetch_furze_metaphors()
    maas = fetch_maas_categories()

    output = {
        "sources": [
            {
                "name": "Leon Furze - AI Metaphors We Live By",
                "url": "https://leonfurze.com/2024/07/19/ai-metaphors-we-live-by-the-language-of-artificial-intelligence/",
                "candidates_found": len(furze),
            },
            {
                "name": "Matthijs Maas - AI is Like...",
                "url": "https://law-ai.org/ai-policy-metaphors/",
                "candidates_found": len(maas),
            },
        ],
        "furze_metaphors": furze,
        "maas_metaphors": maas,
    }

    json.dump(output, sys.stdout, indent=2)
    print(file=sys.stderr)
    print(f"Extracted {len(furze)} from Furze, {len(maas)} from Maas", file=sys.stderr)


if __name__ == "__main__":
    main()
