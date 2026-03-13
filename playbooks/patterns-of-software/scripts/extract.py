#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Extract mapping candidates from Gabriel's "Patterns of Software" (1996).

Sources:
1. Gabriel, R.P. "Patterns of Software: Tales from the Software Community" (1996)
   https://dreamsongs.com/Files/PatternsOfSoftware.pdf
2. Akkartik's notes on Habitability:
   https://akkartik.name/post/habitability
3. Norswap's highlights:
   https://norswap.com/patterns-of-software/

This is a nugget-type project with 4 candidates drawn from close reading
of the Alexander-inspired essays in Part I of the book. The candidates are
encoded as static data because the source is a prose book, not a structured
database.

Outputs JSON to stdout. Idempotent: same output on each run.
"""

import json
import sys

PROJECT = "patterns-of-software"
PROJECT_ISSUE = 898

ARCHIVE_URLS = [
    "https://dreamsongs.com/Files/PatternsOfSoftware.pdf",
    "https://akkartik.name/post/habitability",
    "https://norswap.com/patterns-of-software/",
]

# --- Candidates extracted from close reading of Part I essays ---

CANDIDATES = [
    {
        "slug": "software-habitability",
        "name": "Software Habitability",
        "kind": "cross-field-mapping",
        "source_frame": "architecture-and-building",
        "target_frame": "software-engineering",
        "categories": ["software-engineering", "cognitive-linguistics"],
        "source": "archive",
        "essay": "Habitability and Piecemeal Growth",
        "author": "gabriel",
        "description": (
            "Gabriel maps Alexander's concept of architectural habitability "
            "onto source code. A habitable building is one its inhabitants can "
            "understand, modify, and feel at home in; habitable code is code "
            "that programmers can navigate, understand, and change comfortably. "
            "The New England farmhouse -- rambling but livable -- is the model, "
            "contrasted with the Superdome and modern skyscrapers (monuments to "
            "design ingenuity that cannot be modified or grown). Gabriel argues "
            "that most programming languages optimize for the wrong thing: "
            "clarity, efficiency, or mathematical precision, when they should "
            "optimize for habitability."
        ),
        "key_quotes": [
            "Habitability is the characteristic of source code that enables "
            "programmers, coders, bug-fixers, and people coming to the code "
            "later in its life to understand its construction and intentions "
            "and to change it comfortably and confidently.",
            "Programs live and grow, and their inhabitants -- the programmers "
            "-- need to work with that program the way the farmer works with "
            "the homestead.",
        ],
        "structural_mappings": {
            "building inhabitant": "programmer / maintainer",
            "architectural habitability": "code navigability and modifiability",
            "New England farmhouse": "well-structured, growable codebase",
            "Superdome / skyscraper": "overdesigned, monument-like code",
            "feeling at home": "developer comfort and ownership",
            "tailoring one's own space": "modifying code confidently",
        },
    },
    {
        "slug": "piecemeal-growth",
        "name": "Piecemeal Growth",
        "kind": "cross-field-mapping",
        "source_frame": "architecture-and-building",
        "target_frame": "software-engineering",
        "categories": ["software-engineering", "systems-thinking"],
        "source": "archive",
        "essay": "Habitability and Piecemeal Growth",
        "author": "gabriel",
        "description": (
            "Gabriel imports Alexander's concept of piecemeal growth: systems "
            "grow incrementally through repair rather than replacement, like "
            "buildings that are 'embellished, modified, reduced, enlarged, "
            "improved' over time. The opposite is 'large lump development' -- "
            "building a complete, perfect artifact and abandoning it. Gabriel "
            "contrasts the dynamic, continuous view (piecemeal) with the "
            "static, discontinuous view (large lump) and argues that master "
            "plans alienate the inhabitants of software just as they alienate "
            "the inhabitants of buildings."
        ),
        "key_quotes": [
            "Piecemeal growth is based on the idea of repair.",
            "It is simply not possible to fix today what the environment "
            "should be like [in the future], and then to steer the piecemeal "
            "process of development toward that fixed, imaginary world.",
            "The existence of a master plan alienates the users.",
        ],
        "structural_mappings": {
            "building repair / embellishment": "code maintenance / feature addition",
            "large lump development": "waterfall / big-bang rewrite",
            "piecemeal growth": "iterative development / continuous refactoring",
            "master plan": "detailed upfront design / specification",
            "organic order": "emergent architecture",
            "inhabitant alienation": "developer disengagement from over-specified code",
        },
    },
    {
        "slug": "code-is-compressed-thought",
        "name": "Code Is Compressed Thought",
        "kind": "conceptual-metaphor",
        "source_frame": "writing",
        "target_frame": "software-engineering",
        "categories": ["software-engineering", "cognitive-linguistics"],
        "source": "archive",
        "essay": "Reuse Versus Compression",
        "author": "gabriel",
        "description": (
            "Gabriel reframes object-oriented inheritance not as 'reuse' but "
            "as 'compression' -- a concept borrowed from language and "
            "literature. Compressed text draws meaning from context, like "
            "poetry whose 'heavily layered meanings can seem dense because of "
            "the multiple images it generates.' A subclass definition is "
            "compressed writing: it says little explicitly but means much "
            "because of its superclass context. Gabriel warns that compression "
            "is dangerous -- it requires the reader to hold the full context "
            "in mind, and changing the base code can silently break the "
            "compressed code that depends on it."
        ),
        "key_quotes": [
            "Compression is the characteristic of a piece of text that the "
            "meaning of any part of it is 'larger' than that piece has by "
            "itself.",
            "Compression in poetry is fine because the ultimate definitions "
            "of the words and phrases are outside the poet's mind. Not so "
            "for compression in programs.",
        ],
        "structural_mappings": {
            "poetic compression": "inheritance-based code compression",
            "context-dependent meaning": "subclass depending on superclass definitions",
            "dense prose": "deep class hierarchy",
            "reader needing full context": "programmer needing superclass knowledge",
            "fragile meaning": "fragile base class problem",
        },
    },
    {
        "slug": "the-quality-without-a-name",
        "name": "The Quality Without a Name",
        "kind": "cross-field-mapping",
        "source_frame": "architecture-and-building",
        "target_frame": "software-engineering",
        "categories": ["software-engineering", "philosophy"],
        "source": "archive",
        "essay": "The Quality Without a Name / The Bead Game, Rugs, and Beauty",
        "author": "gabriel",
        "description": (
            "Gabriel explores Alexander's central concept -- an objective "
            "quality of 'wholeness' or 'aliveness' that good buildings "
            "possess and that cannot be reduced to any single named property. "
            "Gabriel asks whether software can possess this quality, and "
            "whether the software patterns movement has missed Alexander's "
            "deeper point by adopting the mechanical form of pattern languages "
            "while ignoring the quality they were meant to generate. The "
            "essay traces Alexander's journey from Notes on the Synthesis of "
            "Form through A Pattern Language to the failed Mexicali project, "
            "and Alexander's subsequent search for a universal formative "
            "principle connecting art, nature, and geometry."
        ),
        "key_quotes": [
            "Computer scientists who try to write patterns without "
            "understanding this quality are quite likely not following "
            "Alexander's program, and perhaps they are not helping themselves "
            "and others as much as they believe. Or perhaps they are doing "
            "harm.",
            "I am not yet sure how, because I am not clear on what the "
            "quality without a name is in the realm of software.",
        ],
        "structural_mappings": {
            "aliveness in buildings": "aliveness in software (undefined)",
            "quality without a name": "emergent quality of good code (unformalized)",
            "pattern language generating quality": "design patterns generating good software",
            "failure of Mexicali project": "failure of GoF patterns to produce quality",
            "geometric beauty": "structural beauty of code",
            "bead game conjecture": "unifying principle across domains",
        },
    },
]


def build_manifest():
    """Build the manifest from all candidate sources."""
    manifest_candidates = []
    for c in CANDIDATES:
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
