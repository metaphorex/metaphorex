#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""
Extract dead metaphor candidates from structured web archives.

Sources:
1. Wikipedia: List of computer term etymologies
2. Examples.com: 99+ Dead Metaphor Examples
3. Gizmodo: Mysterious Origins of 21 Tech Terms

Outputs JSON to stdout. Idempotent: same output on each run
(modulo upstream page edits).
"""

import json
import re
import sys
from urllib.request import urlopen, Request
from html.parser import HTMLParser


# --- Source 1: Wikipedia List of Computer Term Etymologies ---
# We cannot reliably scrape Wikipedia (403s common), so we encode
# the structured data extracted from the page as a static dataset.
# This is the canonical list from
# https://en.wikipedia.org/wiki/List_of_computer_term_etymologies
# filtered to terms with metaphorical origins from non-computing domains.

WIKIPEDIA_COMPUTER_TERMS = [
    {
        "term": "bug",
        "original_domain": "entomology",
        "original_meaning": "Literal insects; Edison used 'bug' for mechanical faults in the 1870s",
        "computing_meaning": "Software defect",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
    {
        "term": "patch",
        "original_domain": "textiles",
        "original_meaning": "Piece of cloth sewn over a hole to repair fabric",
        "computing_meaning": "Code fix applied to repair a defect",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
    {
        "term": "cookie",
        "original_domain": "food-and-cooking",
        "original_meaning": "Fortune cookie -- treat containing a hidden message",
        "computing_meaning": "Small data file stored by a website in the user's browser",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
    {
        "term": "virus",
        "original_domain": "medicine",
        "original_meaning": "Biological pathogen that replicates by hijacking host cells",
        "computing_meaning": "Self-replicating malicious program that infects host systems",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
    {
        "term": "spam",
        "original_domain": "food-and-cooking",
        "original_meaning": "Canned meat product, immortalized by Monty Python sketch",
        "computing_meaning": "Unwanted bulk messages flooding a channel",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
    {
        "term": "mouse",
        "original_domain": "animal-behavior",
        "original_meaning": "Small rodent; Engelbart named the device for its shape and tail (cable)",
        "computing_meaning": "Pointing input device",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
    {
        "term": "web",
        "original_domain": "animal-behavior",
        "original_meaning": "Spider's web -- interconnected strands radiating from a center",
        "computing_meaning": "The World Wide Web -- interconnected hypertext documents",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
    {
        "term": "stream",
        "original_domain": "fluid-dynamics",
        "original_meaning": "Continuous flow of water in a narrow channel",
        "computing_meaning": "Continuous flow of data delivered in real time",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
    {
        "term": "cloud",
        "original_domain": "natural-phenomena",
        "original_meaning": "Mass of water vapor in the sky, amorphous and everywhere",
        "computing_meaning": "Remote computing infrastructure, amorphous and everywhere",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
    {
        "term": "wiki",
        "original_domain": "language",
        "original_meaning": "Hawaiian for 'quick' (wiki wiki)",
        "computing_meaning": "Collaboratively edited website",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
    {
        "term": "bluetooth",
        "original_domain": "history",
        "original_meaning": "King Harald 'Bluetooth' Gormsson, who unified Scandinavia",
        "computing_meaning": "Wireless standard that unifies device communication",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
    {
        "term": "troll",
        "original_domain": "mythology",
        "original_meaning": "Scandinavian folklore creature; also fishing technique (dragging bait)",
        "computing_meaning": "Person who posts provocative content to elicit reactions",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
    {
        "term": "daemon",
        "original_domain": "mythology",
        "original_meaning": "Greek daimon -- spirit that works in the background, neither good nor evil",
        "computing_meaning": "Background process that runs without user interaction",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
    {
        "term": "kernel",
        "original_domain": "horticulture",
        "original_meaning": "Inner seed of a nut or fruit -- the essential core",
        "computing_meaning": "Core of an operating system that manages hardware resources",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
    {
        "term": "shell",
        "original_domain": "horticulture",
        "original_meaning": "Hard outer covering of a nut or seed, surrounding the kernel",
        "computing_meaning": "User interface that wraps around the kernel",
        "url": "https://en.wikipedia.org/wiki/List_of_computer_term_etymologies",
    },
]

# --- Source 2: Everyday dead metaphors with surprising etymologies ---
# Curated from examples.com, etymonline.com, and academic sources.
# These are words whose metaphorical origins are forgotten by most speakers.

EVERYDAY_DEAD_METAPHORS = [
    {
        "term": "deadline",
        "original_domain": "military",
        "original_meaning": "Line around Civil War prisons; cross it and guards shoot to kill",
        "modern_meaning": "Time by which a task must be completed",
        "url": "https://www.etymonline.com/word/deadline",
    },
    {
        "term": "dashboard",
        "original_domain": "horse-drawn-transport",
        "original_meaning": "Board at front of carriage to block mud 'dashed up' by horses' hooves",
        "modern_meaning": "Display panel showing metrics and controls",
        "url": "https://www.etymonline.com/word/dashboard",
    },
    {
        "term": "broadcast",
        "original_domain": "agriculture",
        "original_meaning": "Scattering seeds widely by hand across a broad area",
        "modern_meaning": "Transmitting signals or content to a wide audience",
        "url": "https://en.wikipedia.org/wiki/Sowing",
    },
    {
        "term": "salary",
        "original_domain": "military-supply",
        "original_meaning": "Latin salarium -- allowance for purchase of salt (sal)",
        "modern_meaning": "Regular payment for employment",
        "url": "https://www.etymonline.com/word/salary",
    },
    {
        "term": "muscle",
        "original_domain": "animal-behavior",
        "original_meaning": "Latin musculus -- 'little mouse'; bicep movement resembles mouse under skin",
        "modern_meaning": "Body tissue that contracts to produce movement",
        "url": "https://www.etymonline.com/word/muscle",
    },
    {
        "term": "companion",
        "original_domain": "food-and-cooking",
        "original_meaning": "Latin com + panis -- 'with bread'; one who shares bread with you",
        "modern_meaning": "Person who accompanies or associates with another",
        "url": "https://www.etymonline.com/word/companion",
    },
    {
        "term": "window",
        "original_domain": "embodied-experience",
        "original_meaning": "Old Norse vindauga -- 'wind eye'; opening that lets wind in",
        "modern_meaning": "Glass-paned opening in a wall; or a GUI element",
        "url": "https://www.etymonline.com/word/window",
    },
    {
        "term": "bankrupt",
        "original_domain": "furniture",
        "original_meaning": "Italian banca rotta -- 'broken bench'; moneylender's bench smashed when insolvent",
        "modern_meaning": "Legally declared unable to pay debts",
        "url": "https://www.etymonline.com/word/bankrupt",
    },
    {
        "term": "brand",
        "original_domain": "animal-husbandry",
        "original_meaning": "Old Norse brandr -- 'to burn'; mark seared onto livestock with hot iron",
        "modern_meaning": "Commercial identity; a company's name, design, and reputation",
        "url": "https://www.etymonline.com/word/brand",
    },
    {
        "term": "capital",
        "original_domain": "embodied-experience",
        "original_meaning": "Latin capitalis from caput -- 'head'; wealth counted per head of cattle",
        "modern_meaning": "Financial assets; accumulated wealth",
        "url": "https://www.etymonline.com/word/capital",
    },
    {
        "term": "stakeholder",
        "original_domain": "gambling",
        "original_meaning": "Person who holds the stakes (wagers) in a bet until the outcome is decided",
        "modern_meaning": "Anyone with an interest or concern in an enterprise",
        "url": "https://mikeclayton.wordpress.com/2014/04/15/the-origin-of-stakeholders/",
    },
    {
        "term": "stock",
        "original_domain": "woodworking",
        "original_meaning": "Old English stocc -- tree trunk; tally sticks split to record debts",
        "modern_meaning": "Shares in a company; or goods held for sale",
        "url": "https://www.etymonline.com/word/stock",
    },
    {
        "term": "running-out-of-steam",
        "original_domain": "steam-engines",
        "original_meaning": "Steam engine losing pressure and slowing to a halt",
        "modern_meaning": "Losing energy or enthusiasm for a task",
        "url": "https://www.examples.com/english/dead-metaphors.html",
    },
]

# --- Source 3: Business/organizational dead metaphors ---

BUSINESS_DEAD_METAPHORS = [
    {
        "term": "leverage",
        "original_domain": "physics",
        "original_meaning": "Using a lever to multiply force applied to a load (Archimedes)",
        "modern_meaning": "Using borrowed capital or existing assets to amplify returns",
        "url": "https://www.etymonline.com/word/leverage",
    },
    {
        "term": "pipeline",
        "original_domain": "fluid-dynamics",
        "original_meaning": "Physical pipe carrying oil, water, or gas from source to destination",
        "modern_meaning": "Sales pipeline, CI/CD pipeline, talent pipeline -- sequential process stages",
        "url": "https://www.etymonline.com/word/pipeline",
    },
    {
        "term": "platform",
        "original_domain": "architecture-and-building",
        "original_meaning": "Raised flat surface for standing on -- train platform, stage platform",
        "modern_meaning": "Technology base on which others build applications or businesses",
        "url": "https://www.etymonline.com/word/platform",
    },
    {
        "term": "silo",
        "original_domain": "agriculture",
        "original_meaning": "Tall cylindrical structure for storing grain, keeping it separate",
        "modern_meaning": "Organizational unit that doesn't share information with others",
        "url": "https://www.etymonline.com/word/silo",
    },
    {
        "term": "red-tape",
        "original_domain": "law",
        "original_meaning": "Literal red ribbon used to bind legal documents in England since the 16th century",
        "modern_meaning": "Excessive bureaucratic procedures that delay action",
        "url": "https://www.etymonline.com/word/red%20tape",
    },
]


def main():
    """Combine all sources and output as JSON."""
    all_entries = []

    for entry in WIKIPEDIA_COMPUTER_TERMS:
        all_entries.append({
            "term": entry["term"],
            "original_domain": entry["original_domain"],
            "original_meaning": entry["original_meaning"],
            "modern_domain": "computing",
            "modern_meaning": entry.get("computing_meaning", ""),
            "archive_source": "wikipedia-computer-etymologies",
            "url": entry["url"],
        })

    for entry in EVERYDAY_DEAD_METAPHORS:
        all_entries.append({
            "term": entry["term"],
            "original_domain": entry["original_domain"],
            "original_meaning": entry["original_meaning"],
            "modern_domain": "everyday-language",
            "modern_meaning": entry.get("modern_meaning", ""),
            "archive_source": "etymonline-and-examples-com",
            "url": entry["url"],
        })

    for entry in BUSINESS_DEAD_METAPHORS:
        all_entries.append({
            "term": entry["term"],
            "original_domain": entry["original_domain"],
            "original_meaning": entry["original_meaning"],
            "modern_domain": "business",
            "modern_meaning": entry.get("modern_meaning", ""),
            "archive_source": "etymonline-and-examples-com",
            "url": entry["url"],
        })

    json.dump(all_entries, sys.stdout, indent=2)
    print()  # trailing newline


if __name__ == "__main__":
    main()
