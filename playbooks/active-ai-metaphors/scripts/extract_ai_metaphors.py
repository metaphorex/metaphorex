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
    """Scrape Leon Furze's 'AI Metaphors We Live By' blog post.

    The blog structures metaphors as H3 headings within H2 category sections.
    Each H3 contains a quoted metaphor name (e.g., "The Black Box"), followed
    by explanatory paragraphs. We extract each H3 heading as a metaphor name
    and gather the following paragraph(s) as the description.
    """
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

    metaphors = []
    # Furze organizes metaphors under H3 headings within H2 category sections.
    # Each H3 text is the metaphor name (e.g., "The Black Box", "The Copilot").
    for h3 in content.find_all("h3"):
        name = h3.get_text(strip=True)
        # Skip empty, very short, or WordPress widget headings
        if not name or len(name) < 3:
            continue
        # Filter out WordPress social sharing widgets and non-metaphor headings
        skip_patterns = ["like this", "share this", "related", "comments"]
        if any(p in name.lower() for p in skip_patterns):
            continue
        # Gather description from sibling paragraphs after this heading
        desc_parts = []
        for sibling in h3.find_next_siblings():
            if sibling.name in ("h2", "h3"):
                break  # stop at next heading
            if sibling.name == "p":
                desc_parts.append(sibling.get_text(strip=True))
        description = " ".join(desc_parts)[:500] if desc_parts else ""
        metaphors.append({
            "name": name,
            "description": description,
            "source_url": url,
        })

    # Fallback: if no H3 headings found, try H2 headings as categories
    if not metaphors:
        for h2 in content.find_all("h2"):
            name = h2.get_text(strip=True)
            if not name or len(name) < 3:
                continue
            desc_parts = []
            for sibling in h2.find_next_siblings():
                if sibling.name == "h2":
                    break
                if sibling.name == "p":
                    desc_parts.append(sibling.get_text(strip=True))
            description = " ".join(desc_parts)[:500] if desc_parts else ""
            metaphors.append({
                "name": name,
                "description": description,
                "source_url": url,
            })

    return metaphors


def fetch_maas_categories() -> list[dict]:
    """Extract the analogies table from Maas's paper summary on law-ai.org.

    The page contains "Table 1: Overview of AI Analogies" structured as an
    HTML table with columns: Theme, Frame (varieties), Brief description.
    We target this specific table and ignore navigation/TOC list items.
    """
    url = "https://law-ai.org/ai-policy-metaphors/"
    try:
        resp = httpx.get(url, follow_redirects=True, timeout=30)
        resp.raise_for_status()
    except httpx.HTTPError as e:
        print(f"Warning: Could not fetch Maas summary: {e}", file=sys.stderr)
        return []

    soup = BeautifulSoup(resp.text, "html.parser")

    # Find the analogies table -- look for tables in the main content area.
    # The table has columns: Theme, Frame (varieties), Brief description.
    metaphors = []
    tables = soup.find_all("table")
    for table in tables:
        # Check if this looks like the analogies table by inspecting headers
        header_row = table.find("tr")
        if not header_row:
            continue
        headers = [
            th.get_text(strip=True).lower()
            for th in header_row.find_all(["th", "td"])
        ]
        # Look for the table with theme/frame/description columns
        is_analogies_table = (
            any("theme" in h for h in headers)
            or any("frame" in h for h in headers)
            or any("analogy" in h or "metaphor" in h for h in headers)
        )
        if not is_analogies_table and len(headers) < 2:
            continue

        rows = table.find_all("tr")
        current_theme = ""
        for row in rows[1:]:  # skip header row
            cells = row.find_all(["td", "th"])
            if len(cells) >= 2:
                # Theme column may use rowspan, so track the current theme
                theme_text = cells[0].get_text(strip=True)
                if theme_text:
                    current_theme = theme_text
                # Frame/name is typically the second column
                frame_col = 1 if len(cells) >= 3 else 0
                name = cells[frame_col].get_text(strip=True)
                desc = cells[-1].get_text(strip=True) if len(cells) >= 3 else ""
                if name and len(name) > 2:
                    # Skip category header rows where name matches theme text
                    # (these are merged-cell headers, not actual analogies)
                    if name == current_theme:
                        continue
                    metaphors.append({
                        "name": name,
                        "theme": current_theme,
                        "description": desc,
                        "source_url": url,
                    })

    # Fallback: if no table found, try to find structured content sections
    # with headings that name the 5 categories (Essence, Operation, etc.)
    if not metaphors:
        content = soup.find("article") or soup.find("main") or soup
        category_keywords = [
            "essence", "operation", "relation", "function", "impact",
        ]
        for h in content.find_all(["h2", "h3", "h4"]):
            heading_text = h.get_text(strip=True).lower()
            if any(kw in heading_text for kw in category_keywords):
                # Gather items from the list following this heading
                for sibling in h.find_next_siblings():
                    if sibling.name in ("h2", "h3", "h4"):
                        break
                    if sibling.name in ("ul", "ol"):
                        for li in sibling.find_all("li", recursive=False):
                            item_text = li.get_text(strip=True)
                            if len(item_text) > 5:
                                metaphors.append({
                                    "name": item_text[:100],
                                    "theme": heading_text,
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
