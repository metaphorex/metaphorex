#!/usr/bin/env python3
"""
Extract the full 129 mental models list from Sources of Insight's
Charlie Munger Mental Models page.

This script fetches the structured article at
sourcesofinsight.com/charlie-munger-mental-models/ and parses out
model names, categories, and descriptions. It writes structured JSON
to stdout.

Usage:
    python extract_sourcesofinsight.py > sourcesofinsight_models.json

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

URL = "https://sourcesofinsight.com/charlie-munger-mental-models/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def fetch_and_parse():
    """Fetch the Sources of Insight page and extract model entries."""
    try:
        resp = requests.get(URL, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(
            f"HTTP error fetching {URL}: {e} "
            f"(status {resp.status_code}). "
            "The site may block automated requests. "
            "Try fetching manually and saving the HTML locally.",
            file=sys.stderr,
        )
        return {
            "source": "sourcesofinsight.com/charlie-munger-mental-models/",
            "fetched_url": URL,
            "error": f"HTTP {resp.status_code}: {e}",
            "model_count": 0,
            "models": [],
        }
    except requests.exceptions.RequestException as e:
        print(
            f"Network error fetching {URL}: {e}",
            file=sys.stderr,
        )
        return {
            "source": "sourcesofinsight.com/charlie-munger-mental-models/",
            "fetched_url": URL,
            "error": str(e),
            "model_count": 0,
            "models": [],
        }
    soup = BeautifulSoup(resp.text, "html.parser")

    content = soup.find("div", class_="entry-content")
    if not content:
        content = soup.find("article") or soup

    models = []
    current_category = "Uncategorized"

    for tag in content.find_all(["h2", "h3", "li", "ol", "strong"]):
        text = tag.get_text(strip=True)
        if not text:
            continue

        if tag.name == "h2":
            # Category headers like "Psychology: Tendencies & Biases"
            current_category = text
        elif tag.name == "h3":
            # Some models may appear as h3
            models.append({
                "name": text,
                "category": current_category,
            })
        elif tag.name == "li":
            # Numbered list items with model names
            # Format: "Model Name -- description" or "Model Name"
            li_text = text
            # Try to split on common separators
            for sep in [" -- ", " – ", " — ", ": "]:
                if sep in li_text:
                    name_part, desc_part = li_text.split(sep, 1)
                    models.append({
                        "name": name_part.strip().lstrip("0123456789. "),
                        "category": current_category,
                        "description": desc_part.strip(),
                    })
                    break
            else:
                # No separator found; use the whole text as name
                cleaned = li_text.lstrip("0123456789. ").strip()
                if cleaned and len(cleaned) > 3:
                    models.append({
                        "name": cleaned,
                        "category": current_category,
                    })

    # Deduplicate by name
    seen = set()
    unique = []
    for m in models:
        key = m["name"].lower()
        if key not in seen:
            seen.add(key)
            unique.append(m)

    return {
        "source": "sourcesofinsight.com/charlie-munger-mental-models/",
        "fetched_url": URL,
        "model_count": len(unique),
        "models": unique,
    }


if __name__ == "__main__":
    result = fetch_and_parse()
    json.dump(result, sys.stdout, indent=2)
    print(file=sys.stdout)
