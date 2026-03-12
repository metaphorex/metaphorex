#!/usr/bin/env python3
"""Extract metaphorical programming terms from the dev.to article
'I plowed through coding slang Wikipedia articles so you don't have to'.

Source: https://dev.to/thormeier/i-plowed-through-coding-slang-wikipedia-articles-so-you-dont-have-to-25-terms-you-probably-didnt-know-3lkf

This article systematically went through Wikipedia's computing jargon
articles and curated 25 terms. We filter for those with genuine
metaphorical structure.

Output: JSON array of candidate objects to stdout.
"""

import json
import sys

# Raw data from the dev.to article.
# (term, source_domain, include, rationale)
RAW_ENTRIES = [
    ("Cargo Cult Programming", "anthropology", True, "Melanesian cargo cults map onto ritual code copying"),
    ("Shotgun Debugging", "weaponry", True, "Scattershot approach maps onto random code changes"),
    ("Shotgun Surgery", "medicine", True, "Traumatic surgery maps onto cascading code changes"),
    ("Voodoo Programming", "religion", True, "Magical ritual maps onto trial-and-error coding"),
    ("Deep Magic", "mysticism", True, "Arcane knowledge maps onto obscure technical expertise"),
    ("Big Ball of Mud", "material-metaphor", True, "Shapeless mass maps onto structureless software"),
    ("Spaghetti Code", "food-and-cooking", True, "Tangled pasta maps onto tangled control flow"),
    ("Yo-yo Problem", "toys", True, "Up-down toy maps onto navigating class hierarchies"),
    ("Boat Anchor", "maritime", True, "Dead weight maps onto obsolete retained technology"),
    ("Action at a Distance", "physics", True, "Quantum spooky action maps onto unexpected side effects"),
    ("Software Rot", "biology", True, "Organic decay maps onto code degradation over time"),
    ("Copy-and-Paste Programming", "general", False, "Literal description, not metaphorical"),
    ("Magic Pushbutton", "general", False, "Thin metaphor, mostly descriptive"),
    ("Data Clump", "general", False, "Descriptive label, not cross-domain"),
    ("Fat Comma", "general", False, "Syntax nickname, not metaphorical"),
    ("Comment Programming", "general", False, "Descriptive, not metaphorical"),
    ("Conference Room Pilot", "general", False, "Process term, not metaphorical"),
    ("Fill Character", "general", False, "Technical, not metaphorical"),
    ("Worse is Better", "philosophy", False, "Design philosophy, not a vernacular metaphor"),
    ("Deutsch Limit", "general", False, "Named rule, not metaphorical"),
    ("Greenspun's Tenth Rule", "general", False, "Observation, not metaphor"),
    ("Software Peter Principle", "organizational-behavior", True, "Peter Principle maps onto software complexity growth"),
    ("Heisenbug", "physics", False, "Already in codinghorror list"),
    ("Bogosort", "general", False, "Algorithm name, thin metaphor"),
    ("Yoda Conditions", "pop-culture", False, "Already in codinghorror list"),
]


def main():
    candidates = []
    for term, domain, include, rationale in RAW_ENTRIES:
        if include:
            candidates.append({
                "term": term,
                "source_domain": domain,
                "rationale": rationale,
                "archive": "devto-wikipedia",
            })
    json.dump(candidates, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
