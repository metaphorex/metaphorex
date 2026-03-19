# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests>=2.31",
#   "beautifulsoup4>=4.12",
# ]
# ///
"""
Extract kitchen terminology from online culinary glossaries.

Sources:
  - Escoffier School: slang/lingo page + kitchen jargon page
  - WebstaurantStore: kitchen slang glossary + culinary terms glossary

Writes structured JSON to stdout. Idempotent per source content.
"""

import json
import re
import sys

import requests
from bs4 import BeautifulSoup

SOURCES = [
    {
        "url": "https://www.escoffier.edu/blog/culinary-arts/slang-and-lingo-every-chef-should-learn/",
        "label": "escoffier-slang",
    },
    {
        "url": "https://www.escoffier.edu/blog/culinary-arts/more-useful-examples-of-chef-jargon/",
        "label": "escoffier-jargon",
    },
    {
        "url": "https://www.webstaurantstore.com/article/511/kitchen-slang-phrases.html",
        "label": "webstaurantstore-slang",
    },
    {
        "url": "https://www.webstaurantstore.com/article/939/culinary-terms-glossary.html",
        "label": "webstaurantstore-glossary",
    },
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Metaphorex research bot; educational use)"
}


def fetch_page(url: str) -> BeautifulSoup:
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def extract_bold_terms(soup: BeautifulSoup) -> list[dict]:
    """Extract terms defined via <strong> or <b> tags in article body."""
    terms = []
    article = soup.find("article") or soup.find("div", class_=re.compile(r"article|content|entry"))
    if not article:
        article = soup

    for bold in article.find_all(["strong", "b"]):
        term_text = bold.get_text(strip=True)
        # Skip navigation, headers, meta
        if len(term_text) < 2 or len(term_text) > 80:
            continue
        # Get surrounding paragraph for definition
        parent = bold.find_parent("p") or bold.find_parent("li")
        if parent:
            full_text = parent.get_text(strip=True)
            # Remove the term itself from the definition
            definition = full_text.replace(term_text, "", 1).strip()
            definition = re.sub(r"^[\s:.\-]+", "", definition)
            if definition and len(definition) > 10:
                terms.append({"term": term_text, "definition": definition[:300]})

    return terms


def extract_h2_terms(soup: BeautifulSoup) -> list[dict]:
    """Extract terms defined under H2/H3 headings."""
    terms = []
    for heading in soup.find_all(["h2", "h3"]):
        term_text = heading.get_text(strip=True)
        if len(term_text) < 2 or len(term_text) > 80:
            continue
        # Get next sibling paragraph
        definition = ""
        for sibling in heading.find_next_siblings():
            if sibling.name in ["h2", "h3", "h1"]:
                break
            if sibling.name == "p":
                definition += " " + sibling.get_text(strip=True)
        definition = definition.strip()[:300]
        if definition and len(definition) > 10:
            terms.append({"term": term_text, "definition": definition})
    return terms


def main():
    all_terms = {}

    for source in SOURCES:
        try:
            soup = fetch_page(source["url"])
            terms = extract_bold_terms(soup)
            if len(terms) < 5:
                # Fall back to heading-based extraction
                terms = extract_h2_terms(soup)
            for t in terms:
                key = t["term"].lower().strip().rstrip(":")
                if key not in all_terms:
                    all_terms[key] = {
                        "term": t["term"].strip().rstrip(":"),
                        "definition": t["definition"],
                        "source_url": source["url"],
                        "source_label": source["label"],
                    }
        except Exception as e:
            print(f"WARNING: Failed to fetch {source['url']}: {e}", file=sys.stderr)

    output = {
        "source": "culinary-glossaries",
        "terms_count": len(all_terms),
        "terms": list(all_terms.values()),
    }
    json.dump(output, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
