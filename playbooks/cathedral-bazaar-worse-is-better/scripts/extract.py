#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Extract mapping candidates from Cathedral & Bazaar + Worse Is Better essays.

Sources:
1. Raymond, E.S. "The Cathedral and the Bazaar" (1997)
   https://www.catb.org/esr/writings/homesteading/cathedral-bazaar/
2. Gabriel, R.P. "The Rise of 'Worse Is Better'" (1991)
   https://www.dreamsongs.com/RiseOfWorseIsBetter.html

This is a nugget-type project with 3 candidates drawn from close reading
of two short essays. The candidates are encoded as static data because
the sources are prose essays, not structured databases.

Outputs JSON to stdout. Idempotent: same output on each run.
"""

import json
import sys

PROJECT = "cathedral-bazaar-worse-is-better"
PROJECT_ISSUE = 897

ARCHIVE_URLS = [
    "https://www.catb.org/esr/writings/homesteading/cathedral-bazaar/",
    "https://www.dreamsongs.com/RiseOfWorseIsBetter.html",
    "https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar",
    "https://www.dreamsongs.com/WorseIsBetter.html",
]

# --- Candidates extracted from close reading of both essays ---

RAYMOND_CANDIDATES = [
    {
        "slug": "software-development-is-cathedral-building",
        "name": "Software Development Is Cathedral Building",
        "kind": "conceptual-metaphor",
        "source_frame": "architecture-and-building",
        "target_frame": "software-engineering",
        "categories": ["software-engineering", "philosophy", "systems-thinking"],
        "source": "archive",
        "essay": "The Cathedral and the Bazaar",
        "author": "raymond",
        "description": (
            "Raymond's cathedral model: centralized, top-down software "
            "development mapped through the metaphor of building a cathedral. "
            "The architect controls the vision, construction follows a master "
            "plan, and the finished product is revealed only when complete. "
            "Imports assumptions about singular authorship, sequential phases, "
            "and the primacy of design over emergence."
        ),
        "key_quotes": [
            "I believed that the most important software needed to be built "
            "like cathedrals, carefully crafted by individual wizards or "
            "small bands of mages working in splendid isolation.",
        ],
        "structural_mappings": {
            "architect": "lead developer / project manager",
            "blueprint": "specification / design document",
            "construction phases": "development milestones / release cycles",
            "consecration": "ship date / release",
            "stone": "code modules",
            "flying buttress": "supporting infrastructure",
        },
    },
    {
        "slug": "software-development-is-a-bazaar",
        "name": "Software Development Is a Bazaar",
        "kind": "conceptual-metaphor",
        "source_frame": "marketplace",
        "target_frame": "software-engineering",
        "categories": ["software-engineering", "philosophy", "systems-thinking"],
        "source": "archive",
        "essay": "The Cathedral and the Bazaar",
        "author": "raymond",
        "description": (
            "Raymond's bazaar model: decentralized, many-voiced open-source "
            "development mapped through the metaphor of a Middle Eastern "
            "bazaar. Many vendors hawk their wares, the crowd self-organizes, "
            "quality emerges from competition and choice rather than central "
            "planning. Imports Linus's Law ('given enough eyeballs, all bugs "
            "are shallow') as the mechanism by which apparent chaos produces "
            "reliable software."
        ),
        "key_quotes": [
            "The Linux community seemed to resemble a great babbling bazaar "
            "of differing agendas and approaches out of which a coherent and "
            "stable system could seemingly emerge only by a succession of "
            "miracles.",
        ],
        "structural_mappings": {
            "vendor / stallholder": "contributor / maintainer",
            "goods / wares": "patches / features / packages",
            "haggling": "code review / discussion",
            "crowd": "user-developer community",
            "noise / babble": "mailing list chatter / competing proposals",
            "variety of goods": "many competing implementations",
            "market forces": "Linus's Law (many eyeballs find bugs)",
        },
    },
]

GABRIEL_CANDIDATES = [
    {
        "slug": "worse-is-better",
        "name": "Worse Is Better",
        "kind": "paradigm",
        "source_frame": "natural-selection",
        "target_frame": "software-engineering",
        "categories": ["software-engineering", "philosophy", "systems-thinking"],
        "source": "archive",
        "essay": "The Rise of 'Worse Is Better'",
        "author": "gabriel",
        "description": (
            "Gabriel's paradigm contrasting two design philosophies: the MIT "
            "approach (correctness and completeness over simplicity) vs. the "
            "New Jersey approach (implementation simplicity over everything "
            "else). Gabriel uses explicitly viral/evolutionary language: "
            "simpler software spreads like a virus because it runs on limited "
            "hardware, becomes portable, conditions users to accept it, then "
            "improves incrementally. The 'worse' software wins because it is "
            "fitter in the Darwinian sense."
        ),
        "key_quotes": [
            "It is slightly better to be simple than correct.",
            "The worse-is-better software first will gain acceptance, second "
            "will condition its users to expect less, and third will be "
            "improved to a point that is almost the right thing.",
        ],
        "design_philosophy_contrast": {
            "mit_approach": {
                "simplicity": "Interface must be simple; implementation complexity acceptable",
                "correctness": "Design must be correct in all observable aspects",
                "consistency": "Must not be inconsistent, even at cost of simplicity",
                "completeness": "Must cover all reasonably expected cases",
            },
            "new_jersey_approach": {
                "simplicity": "Implementation must be simple; interface simplicity secondary",
                "correctness": "Slightly better to be simple than correct",
                "consistency": "Can be sacrificed for simplicity",
                "completeness": "Can be sacrificed for simplicity",
            },
        },
    },
]


def build_manifest():
    """Build the manifest from all candidate sources."""
    all_candidates = RAYMOND_CANDIDATES + GABRIEL_CANDIDATES

    # Strip extra fields not in manifest schema
    manifest_candidates = []
    for c in all_candidates:
        manifest_candidates.append({
            "slug": c["slug"],
            "name": c["name"],
            "kind": c["kind"],
            "source_frame": c["source_frame"],
            "target_frame": c["target_frame"],
            "categories": c["categories"],
            "source": c["source"],
            "description": c["description"],
        })

    return {
        "project": PROJECT,
        "project_issue": PROJECT_ISSUE,
        "source_type": "archive",
        "archive_urls": ARCHIVE_URLS,
        "candidates": manifest_candidates,
    }


def main():
    manifest = build_manifest()
    json.dump(manifest, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
