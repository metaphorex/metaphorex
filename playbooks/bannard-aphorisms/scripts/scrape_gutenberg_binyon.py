#!/usr/bin/env python3
"""Scrape aphorisms from Binyon's 'The Mind of the Artist' on Project Gutenberg.

Fetches the plain-text version and extracts numbered aphorisms/quotes
organized by section. Outputs structured JSON to stdout.

Usage:
    python scrape_gutenberg_binyon.py > binyon_quotes.json
"""

import json
import re
import sys
import urllib.request


GUTENBERG_URL = "https://www.gutenberg.org/files/18653/18653.txt"


def fetch_text():
    """Fetch the full text from Project Gutenberg."""
    req = urllib.request.Request(
        GUTENBERG_URL,
        headers={"User-Agent": "Mozilla/5.0 (Metaphorex research bot; academic use)"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def extract_sections_and_quotes(text):
    """Extract section headings and attributed quotes from the text."""
    # Strip Gutenberg header/footer
    start = text.find("*** START OF")
    end = text.find("*** END OF")
    if start > 0:
        text = text[text.index("\n", start) + 1 :]
    if end > 0:
        text = text[:end]

    sections = []
    current_section = "Preamble"
    current_quotes = []

    # Section headings are in ALL CAPS
    section_pattern = re.compile(r"^([A-Z][A-Z &]{5,})$", re.MULTILINE)

    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Detect section headings
        m = section_pattern.match(line)
        if m and len(line) > 5:
            if current_quotes:
                sections.append(
                    {"section": current_section, "quotes": current_quotes}
                )
            current_section = m.group(1).strip().title()
            current_quotes = []
            i += 1
            continue

        # Detect attributed quotes: lines ending with --Author or —Author
        # or paragraphs followed by attribution
        if line.startswith('"') or line.startswith("\u201c"):
            # Collect multi-line quote
            quote_lines = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith('"'):
                quote_lines.append(lines[i].strip())
                i += 1
            full = " ".join(quote_lines)
            # Try to split attribution
            attr_match = re.search(r"[.\u201d\"]\s*[-\u2014]+\s*(.+)$", full)
            if attr_match:
                author = attr_match.group(1).strip().rstrip(".")
                quote_text = full[: attr_match.start() + 1].strip()
            else:
                author = "Unknown"
                quote_text = full.strip()
            if len(quote_text) > 20:
                current_quotes.append({"text": quote_text, "author": author})
            continue

        i += 1

    if current_quotes:
        sections.append({"section": current_section, "quotes": current_quotes})

    return sections


def main():
    text = fetch_text()
    sections = extract_sections_and_quotes(text)
    total = sum(len(s["quotes"]) for s in sections)

    output = {
        "source": "gutenberg.org/ebooks/18653",
        "title": "The Mind of the Artist",
        "compiler": "Mrs. Laurence Binyon",
        "section_count": len(sections),
        "total_quotes": total,
        "sections": sections,
    }
    json.dump(output, sys.stdout, indent=2, ensure_ascii=False)
    print(file=sys.stdout)


if __name__ == "__main__":
    main()
