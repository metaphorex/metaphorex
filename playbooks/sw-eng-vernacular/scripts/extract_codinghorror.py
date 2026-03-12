#!/usr/bin/env python3
"""Extract metaphorical programming jargon from Coding Horror's
'New Programming Jargon' post.

This script encodes the structured list from:
https://blog.codinghorror.com/new-programming-jargon/

The blog post aggregates the top 30+ entries from a Stack Overflow
community wiki question on new programming jargon. We filter for
entries with genuine metaphorical structure (cross-domain mapping),
excluding puns, acronyms, and purely descriptive labels.

Output: JSON array of candidate objects to stdout.
"""

import json
import sys

# Raw data extracted from the Coding Horror blog post.
# Each entry: (term, source_domain_note, include_as_candidate, rationale)
RAW_ENTRIES = [
    ("Yoda Conditions", "pop-culture", False, "Syntactic trick, not a deep metaphor"),
    ("Pokemon Exception Handling", "pop-culture", True, "Gotta catch em all maps collecting onto error handling"),
    ("Egyptian Brackets", "visual-culture", False, "Visual resemblance only, no structural mapping"),
    ("Smug Report", "social-behavior", False, "Pun, not a metaphor"),
    ("A Duck", "social-behavior", True, "Decoy/sacrifice maps onto feature negotiation"),
    ("Refuctoring", "wordplay", False, "Portmanteau, not a cross-domain mapping"),
    ("Stringly Typed", "wordplay", False, "Pun on strongly typed"),
    ("Heisenbug", "physics", True, "Quantum uncertainty maps onto debugging observation effects"),
    ("Hindenbug", "history", True, "Catastrophic disaster maps onto data-destroying bugs"),
    ("Hydra Code", "mythology", True, "Multi-headed regenerating monster maps onto cascading bugs"),
    ("Loch Ness Monster Bug", "mythology", True, "Cryptid sighting maps onto unreproducible bug reports"),
    ("Rubber Ducking", "social-behavior", True, "Conversation partner maps onto debugging technique"),
    ("Baklava Code", "food-and-cooking", True, "Layered pastry maps onto excessive abstraction layers"),
    ("Smurf Naming Convention", "pop-culture", False, "Visual joke about prefix repetition"),
    ("Protoduction", "portmanteau", False, "Portmanteau, not metaphor"),
    ("Fear Driven Development", "psychology", True, "Fear/coercion maps onto management methodology"),
    ("Chunky Salsa", "food-and-cooking", True, "Food that cant be reassembled maps onto irrecoverable failure"),
    ("Jenga Code", "games", True, "Precarious block tower maps onto fragile interdependent code"),
    ("Mad Girlfriend Bug", "social-behavior", False, "Gendered stereotype, skip"),
]


def main():
    candidates = []
    for term, domain, include, rationale in RAW_ENTRIES:
        if include:
            candidates.append({
                "term": term,
                "source_domain": domain,
                "rationale": rationale,
                "archive": "codinghorror",
            })
    json.dump(candidates, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
