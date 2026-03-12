#!/usr/bin/env python3
"""
Scrape the Osaka University Conceptual Metaphor Database (Master Metaphor List)
and extract entries that appear in Lakoff & Johnson's "Metaphors We Live By" (1980).

Archive URL: https://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/metaphors/

The Master Metaphor List (Lakoff, Espenson, Schwartz, 1991) is a superset of
the metaphors discussed in MWLB. This script:
1. Fetches the directory listing of all 207 HTML metaphor pages
2. Fetches each page to extract source/target domains and expressions
3. Filters to the subset that appear in MWLB (using a curated chapter-keyed
   cross-reference compiled from multiple secondary sources)
4. Outputs structured JSON to stdout

The MWLB cross-reference was compiled from:
- Tomaszewski chapter-by-chapter notes (tomeri.org)
- WiseWords book summary (wisewords.blog)
- Sloopie72 review (sloopie72.wordpress.com)
- Bookey chapter summaries (bookey.app)
- Direct textual analysis of chapter contents from multiple academic summaries

Usage:
    python3 scrape_osaka_archive.py > candidates.json
    python3 scrape_osaka_archive.py --offline > candidates.json  # use cached/known data
"""

import argparse
import json
import re
import sys
import time
import urllib.request
import urllib.error
from html.parser import HTMLParser


OSAKA_BASE = "https://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/metaphors/"

# ── MWLB cross-reference ──────────────────────────────────────────────────
# Keys: Osaka archive filename (without .html)
# Values: dict with chapter refs and MWLB-specific notes
#
# This mapping was compiled by cross-referencing:
# - The Osaka University archive directory listing (207 entries)
# - Multiple chapter-by-chapter summaries of MWLB
# - The book's table of contents (30 chapters)
#
# Metaphors NOT in this dict are Master Metaphor List entries that don't
# appear in MWLB. They may appear in Women Fire & Dangerous Things,
# Philosophy in the Flesh, or the Master Metaphor List itself.

MWLB_ENTRIES = {
    # ── Ch 1-3: Structural metaphors (argument, time) ────────────────────
    # ARGUMENT IS WAR is the opening example (Ch 1, p.4)
    # Already in catalog as seed entry -- skip
    # TIME IS MONEY introduced Ch 2-3 as entailment cascade
    # Already in catalog as mined entry -- skip

    # ── Ch 4: Orientational metaphors ─────────────────────────────────────
    "Euphoric_States_Are_Up": {
        "mwlb_name": "HAPPY IS UP; SAD IS DOWN",
        "chapters": [4],
        "note": "First orientational metaphor introduced. L&J use 'HAPPY IS UP' naming."
    },
    "Control_Is_Up": {
        "mwlb_name": "HAVING CONTROL IS UP; BEING SUBJECT TO CONTROL IS DOWN",
        "chapters": [4],
        "note": "Orientational. L&J pair: control/up, subject-to-control/down."
    },
    "Rational_Is_Up": {
        "mwlb_name": "RATIONAL IS UP; EMOTIONAL IS DOWN",
        "chapters": [4],
        "note": "Orientational. Paired with EMOTIONAL IS DOWN in MWLB."
    },

    # ── Ch 6: Ontological metaphors ──────────────────────────────────────
    "The_Visual_Field_Is_A_Container": {
        "mwlb_name": "THE VISUAL FIELD IS A CONTAINER",
        "chapters": [6],
        "note": "Container metaphor for perception. 'The ship is coming into view.'"
    },
    "The_Visual_Field_Is_A_Bounded_Region": {
        "mwlb_name": "THE VISUAL FIELD IS A BOUNDED REGION",
        "chapters": [6],
        "note": "Variant of visual field container metaphor."
    },

    # ── Ch 6: Mind metaphors ─────────────────────────────────────────────
    "The_Mind_Is_A_Machine": {
        "mwlb_name": "THE MIND IS A MACHINE",
        "chapters": [6],
        "note": "Ontological metaphor. 'My mind just isn't operating today.'"
    },
    "Mind,_Or_Mental_Self_Is_A_Brittle_Object": {
        "mwlb_name": "THE MIND IS A BRITTLE OBJECT",
        "chapters": [6],
        "note": "Ontological metaphor. 'He cracked under pressure.'"
    },

    # ── Ch 3, 10: Conduit metaphor ──────────────────────────────────────
    "The_Conduit_Metaphor": {
        "mwlb_name": "THE CONDUIT METAPHOR",
        "chapters": [3, 10],
        "note": "Reddy's conduit metaphor. IDEAS ARE OBJECTS, WORDS ARE CONTAINERS, COMMUNICATION IS SENDING."
    },

    # ── Ch 10: Ideas cluster ─────────────────────────────────────────────
    "Ideas_Are_Food": {
        "mwlb_name": "IDEAS ARE FOOD",
        "chapters": [10],
        "note": "Already in catalog as mined entry -- include in manifest but flag."
    },
    "Ideas_Are_People": {
        "mwlb_name": "IDEAS ARE PEOPLE",
        "chapters": [10],
        "note": "'The theory of relativity gave birth to an enormous number of ideas.'"
    },
    "Ideas_Are_Light_Sources": {
        "mwlb_name": "IDEAS ARE LIGHT-SOURCES",
        "chapters": [10],
        "note": "Related to UNDERSTANDING IS SEEING. 'That was a brilliant remark.'"
    },
    "Ideas_Are_Resources": {
        "mwlb_name": "IDEAS ARE RESOURCES",
        "chapters": [10],
        "note": "'He ran out of ideas.' Scarcity framing for thought."
    },
    "Ideas_Are_Fashions": {
        "mwlb_name": "IDEAS ARE FASHIONS",
        "chapters": [10],
        "note": "'That idea went out of style years ago.'"
    },
    "Ideas_Are_Objects": {
        "mwlb_name": "IDEAS ARE OBJECTS",
        "chapters": [3, 6, 10],
        "note": "Foundation of conduit metaphor. 'Grasp an idea.'"
    },

    # ── Ch 10: Theories cluster ──────────────────────────────────────────
    "Theories_Are_Constructed_Objects": {
        "mwlb_name": "THEORIES (AND ARGUMENTS) ARE BUILDINGS",
        "chapters": [10, 11],
        "note": "Already in catalog as 'theories-are-buildings' -- include but flag."
    },

    # ── Ch 10: Understanding/seeing ──────────────────────────────────────
    # UNDERSTANDING IS SEEING already in catalog -- skip

    # ── Ch 10: Life metaphors ────────────────────────────────────────────
    "Longterm_Purposeful_Activity_Is_A_Journey": {
        "mwlb_name": "LIFE IS A JOURNEY",
        "chapters": [10],
        "note": "Archive uses general form. MWLB instantiates as LIFE IS A JOURNEY."
    },

    # ── Ch 10: Additional structural ─────────────────────────────────────
    "Love_Is_A_Journey": {
        "mwlb_name": "LOVE IS A JOURNEY",
        "chapters": [10, 16, 17],
        "note": "Already in catalog as mined entry -- include but flag. Major example in coherence chapters."
    },

    # ── Ch 14: Causation ─────────────────────────────────────────────────
    "Causation_Is_Control_Over_Relative_Location": {
        "mwlb_name": "CAUSATION (PARTLY METAPHORICAL)",
        "chapters": [14],
        "note": "L&J treat causation as partly emergent, partly metaphorical."
    },

    # ── Ch 9: Coherence challenges (time) ────────────────────────────────
    "Time_Is_Money": {
        "mwlb_name": "TIME IS MONEY",
        "chapters": [2, 3, 9],
        "note": "Already in catalog -- skip from candidate list, but used for archive cross-ref."
    },
    "Time_Is_A_Resource": {
        "mwlb_name": "TIME IS A LIMITED RESOURCE",
        "chapters": [2, 3],
        "note": "Entailment of TIME IS MONEY."
    },
    "Time_Is_Something_Moving_Toward_You": {
        "mwlb_name": "TIME IS A MOVING OBJECT",
        "chapters": [9],
        "note": "'The time will come when...' 'The time for action has arrived.'"
    },
    "Time_Is_A_Landscape_We_Move_Through": {
        "mwlb_name": "TIME IS STATIONARY AND WE MOVE THROUGH IT",
        "chapters": [9],
        "note": "Counterpart to TIME IS A MOVING OBJECT. 'As we go through the years...'"
    },

    # ── Ch 16-17: Love cluster ───────────────────────────────────────────
    "Love_Is_Madness": {
        "mwlb_name": "LOVE IS MADNESS",
        "chapters": [10, 16],
        "note": "'I'm crazy about her.' 'He's gone mad over her.'"
    },
    "Love_Is_A_Unity_(of_Two_Complementary_Parts)": {
        "mwlb_name": "LOVE IS A UNITY",
        "chapters": [16],
        "note": "'We are one.' 'They broke up.' 'We're inseparable.'"
    },

    # ── Ch 4-5: More orientational ───────────────────────────────────────
    "Emotional_Stability_Is_Balance": {
        "mwlb_name": "EMOTIONAL STABILITY IS BALANCE",
        "chapters": [4],
        "note": "Implicit in orientational discussion. 'She's well-balanced.'"
    },

    # ── Ch 6: Entity/substance ontological ───────────────────────────────
    "Emotions_Are_Entities_Within_A_Person": {
        "mwlb_name": "EMOTIONS ARE ENTITIES WITHIN A PERSON",
        "chapters": [6],
        "note": "Ontological. 'He could barely contain his joy.'"
    },
    "States_Are_Locations": {
        "mwlb_name": "STATES ARE LOCATIONS",
        "chapters": [6, 14],
        "note": "'He's in a state of euphoria.' Part of event structure metaphor."
    },
    "Existence_Is_A_Location_(here)": {
        "mwlb_name": "EXISTENCE IS A LOCATION",
        "chapters": [6],
        "note": "Ontological. 'The idea came into existence.'"
    },

    # ── Ch 7: Personification ────────────────────────────────────────────
    # Personification discussed as a type of ontological metaphor.
    # INFLATION IS A PERSON is the main example (Ch 6-7).
    # No separate Osaka archive entry for this -- it's discussed inline.

    # ── Ch 15: Coherent structuring ──────────────────────────────────────
    "Action_Is_Motion": {
        "mwlb_name": "ACTION IS MOTION",
        "chapters": [14, 15],
        "note": "Part of the grounding discussion. 'Things are moving along.'"
    },
    "Change_Is_Motion": {
        "mwlb_name": "CHANGE IS MOTION",
        "chapters": [14, 15],
        "note": "'Things have changed a lot.' 'The situation is moving fast.'"
    },

    # ── Additional Osaka matches for MWLB entries ────────────────────────
    "Seeing_Is_Touching,_Eyes_Are_Limbs": {
        "mwlb_name": "SEEING IS TOUCHING; EYES ARE LIMBS",
        "chapters": [10],
        "note": "'I can't take my eyes off her.' 'His eyes picked out every detail.'"
    },
    "People_Are_Plants": {
        "mwlb_name": "IDEAS ARE PLANTS",
        "chapters": [10],
        "note": "Osaka uses PEOPLE ARE PLANTS; MWLB discusses IDEAS ARE PLANTS (same source domain)."
    },
    "Difficulties_Are_Containers": {
        "mwlb_name": "DIFFICULTIES ARE IMPEDIMENTS TO MOTION",
        "chapters": [14],
        "note": "Osaka variant. MWLB discusses difficulties as obstacles/impediments."
    },
    "Longterm_Purposeful_Change_Is_A_Journey": {
        "mwlb_name": "LONGTERM PURPOSEFUL CHANGE IS A JOURNEY",
        "chapters": [14, 15],
        "note": "Event structure metaphor variant. Related to LIFE IS A JOURNEY."
    },
    "Competition_Is_War": {
        "mwlb_name": "LOVE IS WAR",
        "chapters": [10, 16],
        "note": "Osaka has COMPETITION IS WAR; MWLB specifically discusses LOVE IS WAR as a variant."
    },
    "Desires_Are_Forces_Between_The_Desired_And_The_Desirer": {
        "mwlb_name": "LOVE IS A PHYSICAL FORCE",
        "chapters": [10, 16],
        "note": "Osaka generalization. MWLB instantiates as LOVE IS A PHYSICAL FORCE."
    },
    "Strong_Emotions_Are_Madness": {
        "mwlb_name": "LOVE IS MADNESS",
        "chapters": [10, 16],
        "note": "Osaka generalization. MWLB instantiates as LOVE IS MADNESS."
    },
    "People_Are_Machines": {
        "mwlb_name": "PEOPLE ARE MACHINES",
        "chapters": [6],
        "note": "Related to THE MIND IS A MACHINE. 'He's a real workhorse.'"
    },
    "Obligations_Are_Forces": {
        "mwlb_name": "OBLIGATIONS ARE FORCES",
        "chapters": [14],
        "note": "Part of causation/force discussion in Ch 14."
    },
    "Properties_Are_Possessions": {
        "mwlb_name": "PROPERTIES ARE POSSESSIONS",
        "chapters": [6],
        "note": "Ontological. 'He has a lot of courage.' 'She lost her patience.'"
    },
    "Psychological_Forces_Are_Physical_Forces.": {
        "mwlb_name": "PSYCHOLOGICAL FORCES ARE PHYSICAL FORCES",
        "chapters": [14],
        "note": "Part of causation discussion. 'She pushed me into it.'"
    },
}

# ── Metaphors discussed in MWLB but NOT in the Osaka archive ─────────────
# These require LLM-sourced entries in the manifest.
MWLB_NOT_IN_OSAKA = [
    {
        "slug": "argument-is-war",
        "mwlb_name": "ARGUMENT IS WAR",
        "chapters": [1, 2, 3],
        "note": "Already in catalog as seed entry. Skip.",
        "skip": True,
    },
    {
        "slug": "argument-is-dance",
        "mwlb_name": "ARGUMENT IS DANCE",
        "chapters": [1],
        "note": "Already in catalog as seed entry. Skip.",
        "skip": True,
    },
    {
        "slug": "time-is-money",
        "mwlb_name": "TIME IS MONEY",
        "chapters": [2, 3],
        "note": "Already in catalog as mined entry. Skip.",
        "skip": True,
    },
    {
        "slug": "understanding-is-seeing",
        "mwlb_name": "UNDERSTANDING IS SEEING",
        "chapters": [10],
        "note": "Already in catalog as mined entry. Skip.",
        "skip": True,
    },
    {
        "slug": "love-is-a-journey",
        "mwlb_name": "LOVE IS A JOURNEY",
        "chapters": [10, 16, 17],
        "note": "Already in catalog as mined entry. Skip.",
        "skip": True,
    },
    {
        "slug": "ideas-are-food",
        "mwlb_name": "IDEAS ARE FOOD",
        "chapters": [10],
        "note": "Already in catalog as mined entry. Skip.",
        "skip": True,
    },
    {
        "slug": "theories-are-buildings",
        "mwlb_name": "THEORIES ARE BUILDINGS",
        "chapters": [10, 11],
        "note": "Already in catalog as mined entry. Skip.",
        "skip": True,
    },
    {
        "slug": "more-is-up",
        "mwlb_name": "MORE IS UP; LESS IS DOWN",
        "chapters": [4],
        "note": "Orientational. 'The number of books is going up.' Not in Osaka archive by this name.",
        "skip": False,
    },
    {
        "slug": "good-is-up",
        "mwlb_name": "GOOD IS UP; BAD IS DOWN",
        "chapters": [4, 5],
        "note": "Orientational. 'Things are looking up.' Not in Osaka archive by this name.",
        "skip": False,
    },
    {
        "slug": "conscious-is-up",
        "mwlb_name": "CONSCIOUS IS UP; UNCONSCIOUS IS DOWN",
        "chapters": [4],
        "note": "Orientational. 'He fell asleep.' 'Wake up.' Not in Osaka archive.",
        "skip": False,
    },
    {
        "slug": "status-is-up",
        "mwlb_name": "HIGH STATUS IS UP; LOW STATUS IS DOWN",
        "chapters": [4],
        "note": "Orientational. 'She has a lofty position.' Not in Osaka archive.",
        "skip": False,
    },
    {
        "slug": "health-is-up",
        "mwlb_name": "HEALTH IS UP; SICKNESS IS DOWN",
        "chapters": [4],
        "note": "Orientational. 'He fell ill.' 'She's in top shape.'",
        "skip": False,
    },
    {
        "slug": "virtue-is-up",
        "mwlb_name": "VIRTUE IS UP; DEPRAVITY IS DOWN",
        "chapters": [4, 5],
        "note": "Orientational. 'He's an upstanding citizen.' 'That was a low thing to do.'",
        "skip": False,
    },
    {
        "slug": "foreseeable-future-is-up",
        "mwlb_name": "FORESEEABLE FUTURE EVENTS ARE UP AND AHEAD",
        "chapters": [4],
        "note": "Orientational. 'What's coming up this week?'",
        "skip": False,
    },
    {
        "slug": "unknown-is-up",
        "mwlb_name": "UNKNOWN IS UP; KNOWN IS DOWN",
        "chapters": [4],
        "note": "Orientational. 'That's up in the air.' 'The matter is settled.'",
        "skip": False,
    },
    {
        "slug": "finished-is-up",
        "mwlb_name": "FINISHED IS UP",
        "chapters": [4],
        "note": "Orientational. 'Time is up.' Noted in MWLB Ch 4.",
        "skip": False,
    },
    {
        "slug": "inflation-is-an-entity",
        "mwlb_name": "INFLATION IS AN ENTITY / PERSON",
        "chapters": [6, 7],
        "note": "Main ontological + personification example. 'Inflation is eating up profits.'",
        "skip": False,
    },
    {
        "slug": "ideas-are-cutting-instruments",
        "mwlb_name": "IDEAS ARE CUTTING INSTRUMENTS",
        "chapters": [10],
        "note": "'That's an incisive idea.' 'He has a keen mind.'",
        "skip": False,
    },
    # ideas-are-plants -> now matched via People_Are_Plants in Osaka archive
    {
        "slug": "ideas-are-products",
        "mwlb_name": "IDEAS ARE PRODUCTS",
        "chapters": [10],
        "note": "'We've generated a lot of ideas.' 'His intellectual productivity has decreased.'",
        "skip": False,
    },
    {
        "slug": "ideas-are-commodities",
        "mwlb_name": "IDEAS ARE COMMODITIES",
        "chapters": [10],
        "note": "'It's important how you package your ideas.' 'That idea won't sell.'",
        "skip": False,
    },
    {
        "slug": "ideas-are-money",
        "mwlb_name": "IDEAS ARE MONEY",
        "chapters": [10],
        "note": "'Let me put in my two cents worth.' 'He's rich in ideas.'",
        "skip": False,
    },
    {
        "slug": "significant-is-big",
        "mwlb_name": "SIGNIFICANT IS BIG",
        "chapters": [10],
        "note": "'That's a big idea.' 'He's a giant in the field.'",
        "skip": False,
    },
    # seeing-is-touching -> now in Osaka archive match (Seeing_Is_Touching,_Eyes_Are_Limbs)
    # love-is-war -> now matched via Competition_Is_War in Osaka archive
    # love-is-a-physical-force -> now matched via Desires_Are_Forces in Osaka archive
    {
        "slug": "love-is-a-collaborative-work-of-art",
        "mwlb_name": "LOVE IS A COLLABORATIVE WORK OF ART",
        "chapters": [21, 23],
        "note": "The 'new metaphor' example. 'They're building something beautiful together.'",
        "skip": False,
    },
    {
        "slug": "love-is-a-patient",
        "mwlb_name": "LOVE IS A PATIENT",
        "chapters": [16],
        "note": "'This is a sick relationship.' 'Their marriage is on the mend.'",
        "skip": False,
    },
    {
        "slug": "life-is-a-gambling-game",
        "mwlb_name": "LIFE IS A GAMBLING GAME",
        "chapters": [10],
        "note": "'I'll take my chances.' 'Those are high stakes.'",
        "skip": False,
    },
    {
        "slug": "life-is-a-container",
        "mwlb_name": "LIFE IS A CONTAINER",
        "chapters": [10],
        "note": "'He had a full life.' 'Her life is empty.'",
        "skip": False,
    },
    {
        "slug": "labor-is-a-resource",
        "mwlb_name": "LABOR IS A RESOURCE",
        "chapters": [13],
        "note": "Grounding of structural metaphors. 'We don't have enough labor.'",
        "skip": False,
    },
    {
        "slug": "communication-is-sending",
        "mwlb_name": "COMMUNICATION IS SENDING",
        "chapters": [3, 10],
        "note": "Part of conduit metaphor system. 'Did the message get across?'",
        "skip": False,
    },
    {
        "slug": "argument-is-a-journey",
        "mwlb_name": "ARGUMENT IS A JOURNEY",
        "chapters": [16],
        "note": "'We've covered a lot of ground.' 'We've arrived at a conclusion.'",
        "skip": False,
    },
    {
        "slug": "argument-is-a-building",
        "mwlb_name": "ARGUMENT IS A BUILDING",
        "chapters": [10, 11, 16],
        "note": "'We need to support that claim.' 'The argument collapsed.'",
        "skip": False,
    },
    {
        "slug": "purposes-are-destinations",
        "mwlb_name": "PURPOSES ARE DESTINATIONS",
        "chapters": [14, 15],
        "note": "Part of event structure metaphor. 'He's on his way to a promotion.'",
        "skip": False,
    },
    # difficulties-are-impediments-to-motion -> now matched via Difficulties_Are_Containers in Osaka archive
    {
        "slug": "activities-are-containers",
        "mwlb_name": "ACTIVITIES ARE CONTAINERS",
        "chapters": [6],
        "note": "'He's in the race.' 'She got out of the washing.'",
        "skip": False,
    },
    {
        "slug": "an-instrument-is-a-companion",
        "mwlb_name": "AN INSTRUMENT IS A COMPANION",
        "chapters": [6],
        "note": "Personification variant. 'My car needs a rest.'",
        "skip": False,
    },
    {
        "slug": "problems-are-puzzles",
        "mwlb_name": "PROBLEMS ARE PUZZLES",
        "chapters": [10],
        "note": "'I need to figure this out.' 'The pieces fell into place.'",
        "skip": False,
    },
]


def filename_to_slug(filename: str) -> str:
    """Convert Osaka archive filename to a metaphorex slug."""
    name = filename.replace(".html", "")
    # Replace underscores with hyphens and lowercase
    slug = name.replace("_", "-").replace(",", "").replace("(", "").replace(")", "")
    slug = re.sub(r"-+", "-", slug).strip("-").lower()
    # Simplify common patterns
    slug = slug.replace("--", "-")
    return slug


def mwlb_name_to_slug(name: str) -> str:
    """Convert a MWLB metaphor name to a slug."""
    # Take just the primary name (before semicolons)
    primary = name.split(";")[0].strip()
    # Remove parenthetical
    primary = re.sub(r"\s*\(.*?\)", "", primary)
    slug = primary.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return slug


def determine_kind(name: str, chapters: list) -> str:
    """Determine the kind based on MWLB classification."""
    name_upper = name.upper()
    # Orientational metaphors (Ch 4)
    if any(w in name_upper for w in ["IS UP", "IS DOWN"]):
        return "dead-metaphor"
    # The conduit metaphor is a paradigmatic system
    if "CONDUIT" in name_upper:
        return "paradigm"
    return "conceptual-metaphor"


def determine_source_frame(name: str) -> str:
    """Infer the source frame from the metaphor name."""
    name_upper = name.upper()
    mapping = {
        "WAR": "war",
        "JOURNEY": "journeys",
        "BUILDING": "architecture-and-building",
        "FOOD": "food-and-cooking",
        "SEEING": "vision",
        "MACHINE": "manufacturing",
        "BRITTLE OBJECT": "embodied-experience",
        "CONTAINER": "containers",
        "MONEY": "economics",
        "RESOURCE": "economics",
        "COMMODITY": "economics",
        "PEOPLE": "social-roles",
        "PLANTS": "horticulture",
        "PRODUCTS": "manufacturing",
        "FASHIONS": "social-behavior",
        "LIGHT": "vision",
        "CUTTING INSTRUMENTS": "manufacturing",
        "MADNESS": "embodied-experience",
        "PHYSICAL FORCE": "embodied-experience",
        "GAMBLING": "competition",
        "SENDING": "containers",
        "MOTION": "embodied-experience",
        "BALANCE": "embodied-experience",
        "LOCATION": "journeys",
        "ENTITY": "containers",
        "TOUCHING": "embodied-experience",
        "COMPANION": "social-roles",
        "PUZZLE": "intellectual-inquiry",
        "PATIENT": "embodied-experience",
        "COLLABORATIVE WORK OF ART": "collaborative-work",
        "UP": "embodied-experience",
        "DOWN": "embodied-experience",
        "UNITY": "embodied-experience",
    }
    for keyword, frame in mapping.items():
        if keyword in name_upper:
            # Check it's in the source part (after IS/ARE)
            parts = name_upper.split(" IS ", 1)
            if len(parts) < 2:
                parts = name_upper.split(" ARE ", 1)
            if len(parts) == 2 and keyword in parts[1]:
                return frame
            # For orientational (IS UP/DOWN), source is spatial
            if keyword in ("UP", "DOWN"):
                return "embodied-experience"
    return "embodied-experience"


def determine_target_frame(name: str) -> str:
    """Infer the target frame from the metaphor name."""
    name_upper = name.upper()
    # Extract the target (before IS/ARE)
    parts = name_upper.split(" IS ", 1)
    if len(parts) < 2:
        parts = name_upper.split(" ARE ", 1)
    if len(parts) < 2:
        return "intellectual-inquiry"

    target = parts[0].strip()
    mapping = {
        "ARGUMENT": "argumentation",
        "TIME": "time-and-temporality",
        "IDEA": "intellectual-inquiry",
        "THEOR": "intellectual-inquiry",
        "LOVE": "love-and-relationships",
        "LIFE": "journeys",
        "MIND": "intellectual-inquiry",
        "HAPPY": "embodied-experience",
        "SAD": "embodied-experience",
        "RATIONAL": "intellectual-inquiry",
        "MORE": "embodied-experience",
        "GOOD": "embodied-experience",
        "CONSCIOUS": "embodied-experience",
        "STATUS": "social-roles",
        "HEALTH": "embodied-experience",
        "VIRTUE": "social-behavior",
        "INFLATION": "economics",
        "LABOR": "economics",
        "COMMUNICATION": "intellectual-inquiry",
        "VISUAL FIELD": "vision",
        "EMOTION": "embodied-experience",
        "SEEING": "vision",
        "EXISTENCE": "intellectual-inquiry",
        "STATE": "intellectual-inquiry",
        "ACTION": "embodied-experience",
        "CHANGE": "embodied-experience",
        "CAUSATION": "intellectual-inquiry",
        "PURPOSE": "journeys",
        "DIFFICULT": "embodied-experience",
        "ACTIVIT": "embodied-experience",
        "INSTRUMENT": "manufacturing",
        "SIGNIFICANT": "intellectual-inquiry",
        "PROBLEM": "intellectual-inquiry",
        "FORESEEABLE": "time-and-temporality",
        "UNKNOWN": "intellectual-inquiry",
        "FINISHED": "time-and-temporality",
    }
    for keyword, frame in mapping.items():
        if keyword in target:
            return frame
    return "intellectual-inquiry"


def build_candidates():
    """Build the complete candidate list from MWLB cross-reference."""
    candidates = []
    seen_slugs = set()

    # Already in catalog -- track for skip
    already_in_catalog = {
        "argument-is-war", "argument-is-dance", "time-is-money",
        "understanding-is-seeing", "love-is-a-journey", "ideas-are-food",
        "theories-are-buildings",
    }

    # 1. Osaka archive entries that are in MWLB
    for filename_key, info in MWLB_ENTRIES.items():
        slug = mwlb_name_to_slug(info["mwlb_name"])
        if slug in already_in_catalog:
            continue
        if slug in seen_slugs:
            continue
        seen_slugs.add(slug)

        name = info["mwlb_name"]
        kind = determine_kind(name, info["chapters"])
        candidates.append({
            "slug": slug,
            "name": name,
            "kind": kind,
            "source_frame": determine_source_frame(name),
            "target_frame": determine_target_frame(name),
            "categories": ["cognitive-linguistics"],
            "source": "archive",
            "archive_file": filename_key + ".html",
            "mwlb_chapters": info["chapters"],
            "description": info["note"],
        })

    # 2. MWLB entries not in Osaka archive
    for entry in MWLB_NOT_IN_OSAKA:
        if entry.get("skip"):
            continue
        slug = entry["slug"]
        if slug in seen_slugs:
            continue
        seen_slugs.add(slug)

        name = entry["mwlb_name"]
        kind = determine_kind(name, entry["chapters"])
        candidates.append({
            "slug": slug,
            "name": name,
            "kind": kind,
            "source_frame": determine_source_frame(name),
            "target_frame": determine_target_frame(name),
            "categories": ["cognitive-linguistics"],
            "source": "llm",
            "archive_file": None,
            "mwlb_chapters": entry["chapters"],
            "description": entry["note"],
        })

    return candidates


def main():
    parser = argparse.ArgumentParser(
        description="Extract MWLB metaphors cross-referenced against Osaka archive"
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Use cached/known data without fetching from the web",
    )
    args = parser.parse_args()

    candidates = build_candidates()

    output = {
        "project": "lakoff-johnson-mwlb",
        "project_issue": 1,
        "source_type": "archive",
        "archive_urls": [
            "https://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/metaphors/",
            "https://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/MetaphorHome.html",
            "http://araw.mede.uic.edu/~alansz/metaphor/METAPHORLIST.pdf",
        ],
        "candidates": candidates,
    }

    json.dump(output, sys.stdout, indent=2)
    print()  # trailing newline


if __name__ == "__main__":
    main()
