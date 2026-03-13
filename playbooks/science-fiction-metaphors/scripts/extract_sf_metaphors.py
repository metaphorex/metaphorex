#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "beautifulsoup4"]
# ///
"""
Extract science fiction terms and concepts that function as real-world
metaphors from structured web archives.

Sources:
1. SF Encyclopedia (sf-encyclopedia.com) - Theme entries index
   https://sf-encyclopedia.com/category/theme
2. OUP Blog - "Nine words from science fiction" (2009)
   https://blog.oup.com/2009/03/science-fiction/
3. SFRA Review - neologisms study (2021)
   https://sfrareview.org/2021/07/20/is-that-from-science-or-fiction/
4. Gizmodo - "31 Essential Science Fiction Terms" (2014)
   https://gizmodo.com/31-essential-science-fiction-terms-and-where-they-came-1594794250

Outputs JSON to stdout with extracted candidates.
"""

import json
import sys

import httpx
from bs4 import BeautifulSoup


def fetch_sfe_themes() -> list[dict]:
    """Scrape the SF Encyclopedia theme index page.

    The SFE organizes themes as an alphabetical list of links. Each theme
    represents an SF concept that the encyclopedia considers significant
    enough to warrant its own entry. We extract theme names that correspond
    to concepts which have crossed into real-world discourse.
    """
    url = "https://sf-encyclopedia.com/category/theme"
    try:
        resp = httpx.get(url, follow_redirects=True, timeout=30)
        resp.raise_for_status()
    except httpx.HTTPError as e:
        print(f"Warning: Could not fetch SFE themes: {e}", file=sys.stderr)
        return []

    soup = BeautifulSoup(resp.text, "html.parser")

    # The SFE theme page lists themes as links in an alphabetical directory.
    # We look for <a> tags within the main content area.
    themes = []
    # Try finding the main content area
    content = (
        soup.find("div", class_="content")
        or soup.find("main")
        or soup.find("article")
        or soup
    )

    for link in content.find_all("a"):
        href = link.get("href", "")
        text = link.get_text(strip=True)
        if not text or len(text) < 2:
            continue
        # SFE entry links follow the pattern /entry/<slug>
        if "/entry/" in href:
            themes.append({
                "name": text,
                "url": f"https://sf-encyclopedia.com{href}" if href.startswith("/") else href,
                "source": "sfe",
            })

    return themes


def fetch_oup_blog() -> list[dict]:
    """Scrape the OUP Blog post on SF words entering mainstream usage.

    The blog post by Jeff Prucher (editor of Brave New Words) lists 9 words
    that entered general English from science fiction, with etymological data.
    """
    url = "https://blog.oup.com/2009/03/science-fiction/"
    try:
        resp = httpx.get(url, follow_redirects=True, timeout=30)
        resp.raise_for_status()
    except httpx.HTTPError as e:
        print(f"Warning: Could not fetch OUP blog: {e}", file=sys.stderr)
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    content = (
        soup.find("div", class_="entry-content")
        or soup.find("article")
        or soup
    )

    terms = []
    # The post uses bold or strong tags for term names, or numbered lists
    for strong in content.find_all(["strong", "b"]):
        name = strong.get_text(strip=True)
        if not name or len(name) < 3:
            continue
        # Get surrounding paragraph text as description
        parent = strong.find_parent("p") or strong.find_parent("li")
        desc = parent.get_text(strip=True) if parent else ""
        terms.append({
            "name": name,
            "description": desc[:500],
            "source_url": url,
        })

    # Fallback: try list items if no bold items found
    if not terms:
        for li in content.find_all("li"):
            text = li.get_text(strip=True)
            if len(text) > 10:
                terms.append({
                    "name": text.split("–")[0].strip() if "–" in text else text[:50],
                    "description": text[:500],
                    "source_url": url,
                })

    return terms


def main():
    sfe = fetch_sfe_themes()
    oup = fetch_oup_blog()

    # Filter SFE themes to those most relevant to real-world metaphorical usage.
    # These are the SFE theme entries that correspond to SF concepts which have
    # achieved "cultural escape velocity" -- used by people who may not know
    # the SF origin. This filtering is based on the issue's inclusion test.
    metaphor_relevant_themes = {
        "Androids", "Artificial Intelligence", "Automation", "Avatars",
        "Big Dumb Objects", "Clones", "Colonization of Other Worlds",
        "Communications", "Computers", "Cryogenics", "Cryonics",
        "Cybernetics", "Cyberpunk", "Cyberspace", "Cyborgs",
        "Dystopias", "Ecology", "Frankenstein Monster", "Generation Starships",
        "Genetic Engineering", "Hive Minds", "Immortality",
        "Nanotechnology", "Parallel Worlds", "Posthuman",
        "Robots", "Robotics", "Singularity", "Simulation",
        "Terraforming", "Time Travel", "Utopias", "Virtual Reality",
        "Weapons", "Dyson Sphere",
    }

    filtered_sfe = [
        t for t in sfe
        if t["name"] in metaphor_relevant_themes
    ]

    output = {
        "sources": [
            {
                "name": "SF Encyclopedia - Theme Entries",
                "url": "https://sf-encyclopedia.com/category/theme",
                "total_themes": len(sfe),
                "metaphor_relevant": len(filtered_sfe),
            },
            {
                "name": "OUP Blog - Nine Words from Science Fiction",
                "url": "https://blog.oup.com/2009/03/science-fiction/",
                "terms_found": len(oup),
            },
        ],
        "sfe_themes": filtered_sfe,
        "oup_terms": oup,
    }

    json.dump(output, sys.stdout, indent=2)
    print(file=sys.stderr)
    print(
        f"Extracted {len(filtered_sfe)} relevant themes from SFE "
        f"(of {len(sfe)} total), {len(oup)} from OUP blog",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
