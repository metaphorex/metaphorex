#!/usr/bin/env python3
"""Scrape Walter Darby Bannard quotes from AZ Quotes.

Fetches all pages of Bannard quotes from azquotes.com and outputs
structured JSON to stdout. Idempotent: same output on each run.

Usage:
    python scrape_azquotes_bannard.py > bannard_quotes.json
"""

import json
import re
import sys
import urllib.request
from html.parser import HTMLParser


class AZQuoteParser(HTMLParser):
    """Extract quote text from AZ Quotes HTML."""

    def __init__(self):
        super().__init__()
        self.quotes = []
        self._in_quote = False
        self._current_quote = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "a" and "title" in attrs_dict:
            title = attrs_dict["title"]
            if title.startswith("Quote by Walter Darby Bannard"):
                self._in_quote = True
                self._current_quote = ""
        # Also catch <p> with class "quote"
        if tag == "p" and attrs_dict.get("class", "") == "quote":
            self._in_quote = True
            self._current_quote = ""

    def handle_endtag(self, tag):
        if self._in_quote and tag in ("a", "p"):
            text = self._current_quote.strip()
            if text and text not in self.quotes:
                self.quotes.append(text)
            self._in_quote = False
            self._current_quote = ""

    def handle_data(self, data):
        if self._in_quote:
            self._current_quote += data


def fetch_page(page_num):
    """Fetch a single page of quotes."""
    if page_num == 1:
        url = "https://www.azquotes.com/author/21913-Walter_Darby_Bannard"
    else:
        url = f"https://www.azquotes.com/author/21913-Walter_Darby_Bannard/{page_num}"

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Metaphorex research bot; academic use)"
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"Warning: failed to fetch page {page_num}: {e}", file=sys.stderr)
        return ""


def main():
    all_quotes = []
    # AZ Quotes typically has 25 quotes per page; Bannard has ~98
    for page in range(1, 5):
        html = fetch_page(page)
        if not html:
            continue
        parser = AZQuoteParser()
        parser.feed(html)
        for q in parser.quotes:
            if q not in all_quotes:
                all_quotes.append(q)

    output = {
        "source": "azquotes.com/author/21913-Walter_Darby_Bannard",
        "author": "Walter Darby Bannard",
        "quote_count": len(all_quotes),
        "quotes": [{"index": i + 1, "text": q} for i, q in enumerate(all_quotes)],
    }
    json.dump(output, sys.stdout, indent=2, ensure_ascii=False)
    print(file=sys.stdout)


if __name__ == "__main__":
    main()
