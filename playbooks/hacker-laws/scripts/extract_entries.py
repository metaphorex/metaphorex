#!/usr/bin/env python3
"""Extract law/principle entries from dwmkerr/hacker-laws README.md.

Fetches the README from GitHub, parses Markdown headings to identify
each entry, and writes structured JSON to stdout.

Usage:
    python3 extract_entries.py
    python3 extract_entries.py --local /path/to/README.md
"""

import json
import re
import sys
import urllib.request


GITHUB_RAW_URL = (
    "https://raw.githubusercontent.com/dwmkerr/hacker-laws/master/README.md"
)

# Sections that are NOT individual law/principle entries
SKIP_HEADINGS = {
    "introduction",
    "laws",
    "principles",
    "reading list",
    "online resources",
    "pdf ebook",
    "podcast",
    "contributors",
    "solid",  # umbrella heading for SOLID sub-principles
}

# Sub-principles under SOLID that are design guidelines, not metaphors
SOLID_SUBPRINCIPLES = {
    "the single responsibility principle",
    "the open/closed principle",
    "the liskov substitution principle",
    "the interface segregation principle",
    "the dependency inversion principle",
}


def fetch_readme(local_path=None):
    if local_path:
        with open(local_path, "r", encoding="utf-8") as f:
            return f.read()
    req = urllib.request.Request(GITHUB_RAW_URL)
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8")


def parse_entries(text):
    """Parse H3 headings and their body text from the README."""
    entries = []
    # Split on ### headings (H3)
    parts = re.split(r"^### (.+)$", text, flags=re.MULTILINE)
    # parts[0] is everything before first H3
    # then alternating: heading, body, heading, body...
    for i in range(1, len(parts), 2):
        raw_heading = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""

        # Clean heading: remove markdown links, extra whitespace
        heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", raw_heading)
        heading = heading.strip()

        heading_lower = heading.lower()
        if heading_lower in SKIP_HEADINGS or heading_lower in SOLID_SUBPRINCIPLES:
            continue

        # Extract the first blockquote as the key quote
        quote_match = re.search(r"^>\s*(.+?)(?:\n(?!>)|\Z)", body, re.MULTILINE | re.DOTALL)
        quote = ""
        if quote_match:
            raw_quote = quote_match.group(0).strip()
            # Clean up blockquote markers
            quote = re.sub(r"^>\s*", "", raw_quote, flags=re.MULTILINE).strip()
            # Remove attribution lines (starting with _)
            quote_lines = [l for l in quote.split("\n") if not l.strip().startswith("_")]
            quote = " ".join(l.strip() for l in quote_lines if l.strip())

        # Extract Wikipedia or other reference link
        link_match = re.search(r"\[.+?\]\((https?://[^)]+)\)", body)
        ref_url = link_match.group(1) if link_match else ""

        entries.append({
            "heading": heading,
            "quote": quote,
            "ref_url": ref_url,
            "body_preview": body[:500].strip(),
        })

    return entries


def main():
    local_path = None
    if len(sys.argv) > 2 and sys.argv[1] == "--local":
        local_path = sys.argv[2]

    text = fetch_readme(local_path)
    entries = parse_entries(text)

    output = {
        "source_url": GITHUB_RAW_URL,
        "entry_count": len(entries),
        "entries": entries,
    }

    json.dump(output, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
