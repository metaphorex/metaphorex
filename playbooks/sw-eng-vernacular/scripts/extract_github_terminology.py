#!/usr/bin/env python3
"""Extract metaphorical programming terms from the saqemlas/software-engineering-terminology
GitHub repository.

Source: https://github.com/saqemlas/software-engineering-terminology

This repo curates software engineering terminology, idioms, and concepts.
We filter for entries with genuine metaphorical structure, excluding those
already captured by other archive scripts.

Output: JSON array of candidate objects to stdout.
"""

import json
import sys

# Raw data from the GitHub repository.
# (term, source_domain, include, rationale)
RAW_ENTRIES = [
    ("Technical Debt", "economics", True, "Financial debt maps onto accumulated shortcuts"),
    ("Code Smell", "embodied-experience", True, "Olfactory detection maps onto code quality intuition"),
    ("Bikeshedding", "architecture-and-building", True, "Trivial construction project maps onto trivial debates"),
    ("Dogfooding", "animal-husbandry", True, "Eating your own pet food maps onto using your own product"),
    ("Rubber Ducking", "social-behavior", False, "Already in codinghorror list"),
    ("Yak Shaving", "animal-husbandry", True, "Grooming a yak maps onto prerequisite task chains"),
    ("Skunkworks", "military-command", True, "Secret military R&D maps onto autonomous innovation teams"),
    ("Bus Factor", "risk-assessment", True, "Getting hit by a bus maps onto team knowledge concentration"),
    ("Boil the Ocean", "natural-phenomena", True, "Impossible physical task maps onto overambitious projects"),
    ("Drinking the Kool-Aid", "history", True, "Jonestown maps onto uncritical adoption"),
    ("Red Herring", "detective-fiction", True, "False trail maps onto misleading debugging clues"),
    ("Reinvent the Wheel", "engineering", True, "Redundant invention maps onto unnecessary reimplementation"),
    ("Angry Fruit Salad", "food-and-cooking", True, "Garish food presentation maps onto bad UI color choices"),
    ("Bread Crumbs", "fairy-tales", True, "Hansel and Gretel trail maps onto debug logging"),
    ("Software Decay", "biology", False, "Duplicate of Software Rot"),
    ("Kitchen Table Software", "domestic-life", False, "Thin metaphor"),
    ("Broken Arrow", "military-command", False, "Thin metaphor, obscure usage"),
    ("Conway's Law", "general", False, "Named law, not vernacular metaphor"),
    ("Brooks' Law", "general", False, "Named law, not vernacular metaphor"),
    ("Ninety-Ninety Rule", "general", False, "Observation, not metaphor"),
]


def main():
    candidates = []
    for term, domain, include, rationale in RAW_ENTRIES:
        if include:
            candidates.append({
                "term": term,
                "source_domain": domain,
                "rationale": rationale,
                "archive": "github-saqemlas",
            })
    json.dump(candidates, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
