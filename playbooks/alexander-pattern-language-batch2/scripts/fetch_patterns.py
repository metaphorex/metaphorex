#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["httpx", "selectolax"]
# ///
"""
Fetch pattern summaries from patternlanguage.cc for Alexander Pattern Language
batch 2 candidates.

Outputs structured JSON to stdout. Idempotent: same input produces same output.
"""
import json
import sys
import httpx
from selectolax.parser import HTMLParser

BASE_URL = "https://patternlanguage.cc/Patterns"

# Batch 2 candidates: slug -> (pattern_number, pattern_name)
BATCH2_PATTERNS = {
    "connection-to-the-earth": (168, "Connection to the Earth"),
    "garden-growing-wild": (172, "Garden Growing Wild"),
    "alcoves": (179, "Alcoves"),
    "window-place": (180, "Window Place"),
    "workspace-enclosure": (183, "Workspace Enclosure"),
    "sitting-circle": (185, "Sitting Circle"),
    "ceiling-height-variety": (190, "Ceiling Height Variety"),
    "windows-overlooking-life": (192, "Windows Overlooking Life"),
    "thick-walls": (197, "Thick Walls"),
    "secret-place": (204, "Secret Place"),
    "structure-follows-social-spaces": (205, "Structure Follows Social Spaces"),
    "good-materials": (207, "Good Materials"),
    "gradual-stiffening": (208, "Gradual Stiffening"),
    "natural-doors-and-windows": (221, "Natural Doors and Windows"),
    "deep-reveals": (223, "Deep Reveals"),
    "filtered-light": (238, "Filtered Light"),
    "small-panes": (239, "Small Panes"),
    "ornament": (249, "Ornament"),
    "pools-of-light": (252, "Pools of Light"),
    "different-chairs": (251, "Different Chairs"),
    "things-from-your-life": (253, "Things From Your Life"),
}


def url_name(name: str, number: int) -> str:
    """Build the patternlanguage.cc URL path component."""
    return f"{name.replace(' ', '-')}-({number})"


def fetch_pattern(slug: str, number: int, name: str, client: httpx.Client) -> dict:
    """Fetch a single pattern page and extract the summary text."""
    url = f"{BASE_URL}/{url_name(name, number)}"
    summary = ""
    try:
        resp = client.get(url, follow_redirects=True, timeout=15)
        if resp.status_code == 200:
            tree = HTMLParser(resp.text)
            # Try to extract blockquote or first paragraph content
            for bq in tree.css("blockquote"):
                text = bq.text(strip=True)
                if len(text) > 30:
                    summary = text[:500]
                    break
            if not summary:
                for p in tree.css("p"):
                    text = p.text(strip=True)
                    if len(text) > 30:
                        summary = text[:500]
                        break
    except Exception as e:
        summary = f"[fetch error: {e}]"

    return {
        "slug": slug,
        "name": name.upper(),
        "pattern_number": number,
        "archive_url": url,
        "summary": summary,
    }


def main():
    results = []
    with httpx.Client() as client:
        for slug, (number, name) in sorted(
            BATCH2_PATTERNS.items(), key=lambda x: x[1][0]
        ):
            info = fetch_pattern(slug, number, name, client)
            results.append(info)
            print(f"  fetched #{number}: {name}", file=sys.stderr)

    json.dump(results, sys.stdout, indent=2)
    print(file=sys.stderr)
    print(f"Fetched {len(results)} patterns.", file=sys.stderr)


if __name__ == "__main__":
    main()
