#!/usr/bin/env python3
"""
Extract Jungian archetype candidates for the Metaphorex catalog.

Sources cross-referenced:
1. Jung, C.G. Collected Works Vol. 9 Part 1: The Archetypes and the
   Collective Unconscious (1959) -- table of contents and chapter structure
2. Wikipedia Category:Jungian_archetypes -- enumerated list of archetype
   articles (accessed 2025)
3. Scott Jeffrey, "15+ Classic Jungian Archetypes" (scottjeffrey.com) --
   secondary compilation from Jungian primary sources
4. Carol Pearson, "Awakening the Heroes Within" (1991) -- the 12-archetype
   system that popularized Jung's archetypes in branding/narrative contexts

The issue (#8) scopes to Jung's CORE archetypes as figures/structures that
function as cross-domain mappings in modern discourse. This is NOT the
exhaustive list of all archetypes ever discussed (which Jung said was
infinite) but the canonical set that appears consistently across:
- Jung's own writings (CW9.1, CW9.2 Aion, Man and His Symbols)
- Secondary Jungian literature (von Franz, Hillman, Pearson)
- Cross-domain usage (branding, storytelling, organizational behavior)

Usage:
    python3 extract_archetypes.py > candidates.json
"""

import json
import sys

# ── Primary source: CW9.1 table of contents ──────────────────────────────
# Each essay in CW9.1 addresses specific archetypes. These are the
# archetypes that Jung devoted full chapters to.
CW9_1_ARCHETYPES = {
    "mother": {
        "essay": "Psychological Aspects of the Mother Archetype",
        "sections": [
            "On the Concept of the Archetype",
            "The Mother-Complex of the Son",
            "The Mother-Complex of the Daughter",
            "Positive Aspects of the Mother-Complex",
        ],
    },
    "child": {
        "essay": "The Psychology of the Child Archetype",
        "sections": [
            "The Archetype as Link with the Past",
            "The Function of the Archetype",
            "The Futurity of the Archetype",
            "Child God and Child Hero",
            "Abandonment, Invincibility, Hermaphroditism, Beginning and End",
        ],
    },
    "kore": {
        "essay": "The Psychological Aspects of the Kore",
        "sections": [],
    },
    "spirit": {
        "essay": "The Phenomenology of the Spirit in Fairytales",
        "sections": [],
        "note": "Maps to the Wise Old Man / Senex archetype",
    },
    "trickster": {
        "essay": "On the Psychology of the Trickster-Figure",
        "sections": [],
    },
}

# ── CW9.2 (Aion) archetypes ──────────────────────────────────────────────
# Aion focuses on the Self and its constituent archetypes
CW9_2_ARCHETYPES = ["self", "shadow", "anima", "animus", "syzygy"]

# ── Wikipedia Category:Jungian_archetypes ─────────────────────────────────
# Full enumeration of articles in the category (accessed 2025):
WIKIPEDIA_JUNGIAN_ARCHETYPES = [
    "Anima and animus",
    "Apollo archetype",
    "Apollonian and Dionysian",
    "Child archetype",
    "Cosmic Man",
    "Goddess",
    "Hero",
    "Jester",
    "Magician",
    "Martyr",
    "Mentor",
    "Mother goddess",
    "Persona (psychology)",
    "Puer aeternus",
    "Self (Jung)",
    "Shadow (psychology)",
    "Trickster",
]

# ── Candidate definitions ─────────────────────────────────────────────────
# Each candidate maps a Jungian archetype to its cross-domain structural
# parallels. The issue (#8) specifies the scope; we add the Shapeshifter
# and Senex which appear in secondary Jungian literature and have strong
# cross-domain mappings.

CANDIDATES = [
    {
        "slug": "the-self",
        "name": "The Self",
        "kind": "archetype",
        "source_frame": "mythology",
        "target_frame": "integration-and-wholeness",
        "categories": ["psychology", "organizational-behavior", "systems-thinking"],
        "source": "archive",
        "archive_refs": {
            "cw9_1": "Conscious, Unconscious, and Individuation; A Study in the Process of Individuation; Concerning Mandala Symbolism",
            "cw9_2": "Aion: Researches into the Phenomenology of the Self (entire volume)",
            "wikipedia": "Self (Jung)",
        },
        "description": "The archetype of wholeness and integration -- the "
        "organizing center of the psyche that transcends ego. Maps onto "
        "system architecture (the unified system vs. its components), "
        "organizational identity (mission as integrating principle), and "
        "the individuation process in personal development.",
    },
    {
        "slug": "the-shadow",
        "name": "The Shadow",
        "kind": "archetype",
        "source_frame": "mythology",
        "target_frame": "hidden-knowledge",
        "categories": ["psychology", "organizational-behavior", "software-engineering"],
        "source": "archive",
        "archive_refs": {
            "cw9_2": "Aion, Chapter 2: The Shadow",
            "wikipedia": "Shadow (psychology)",
        },
        "description": "The denied, repressed, or unacknowledged aspects of "
        "self or system. Maps onto technical debt, shadow IT, organizational "
        "denial, and the gap between stated values and actual behavior. "
        "The most structurally productive Jungian archetype for modern "
        "organizational analysis.",
    },
    {
        "slug": "the-persona",
        "name": "The Persona",
        "kind": "archetype",
        "source_frame": "mythology",
        "target_frame": "social-roles",
        "categories": ["psychology", "organizational-behavior", "software-engineering"],
        "source": "archive",
        "archive_refs": {
            "cw7": "Two Essays on Analytical Psychology, Chapter 2: The Persona",
            "wikipedia": "Persona (psychology)",
        },
        "description": "The social mask -- the public-facing identity adopted "
        "for social interaction. Maps onto public APIs, facade patterns, "
        "corporate branding, and the distinction between interface and "
        "implementation. Jung's term literally means 'mask' (from Latin "
        "theatrical masks).",
    },
    {
        "slug": "the-anima-animus",
        "name": "The Anima / Animus",
        "kind": "archetype",
        "source_frame": "mythology",
        "target_frame": "creative-tension",
        "categories": ["psychology", "organizational-behavior", "arts-and-culture"],
        "source": "archive",
        "archive_refs": {
            "cw9_1": "Concerning the Archetypes, with Special Reference to the Anima Concept",
            "cw9_2": "Aion, Chapter 3: The Syzygy: Anima and Animus",
            "wikipedia": "Anima and animus",
        },
        "description": "The inner complement -- the contrasexual aspect of the "
        "psyche that bridges conscious and unconscious. Maps onto creative "
        "tension in cross-functional teams, the relationship between "
        "analytical and intuitive modes, and the productive friction between "
        "complementary perspectives. Requires careful handling of Jung's "
        "gender essentialism in the 'Where It Breaks' section.",
    },
    {
        "slug": "the-hero",
        "name": "The Hero",
        "kind": "archetype",
        "source_frame": "mythology",
        "target_frame": "social-roles",
        "categories": ["psychology", "organizational-behavior", "arts-and-culture"],
        "source": "archive",
        "archive_refs": {
            "cw9_1": "The Psychology of the Child Archetype (Child God and Child Hero)",
            "cw5": "Symbols of Transformation (hero myth analysis)",
            "wikipedia": "Hero",
            "pearson": "The Warrior / Hero archetype",
        },
        "description": "The journey, the protagonist, the founder myth. Maps "
        "onto startup founder narratives, hero culture in engineering "
        "(hero-driven development), and the monomyth structure in product "
        "storytelling. The most commercially exploited Jungian archetype.",
    },
    {
        "slug": "the-great-mother",
        "name": "The Great Mother",
        "kind": "archetype",
        "source_frame": "mythology",
        "target_frame": "nurturing-and-creation",
        "categories": ["psychology", "organizational-behavior", "systems-thinking"],
        "source": "archive",
        "archive_refs": {
            "cw9_1": "Psychological Aspects of the Mother Archetype (full essay)",
            "wikipedia": "Mother goddess",
            "neumann": "Erich Neumann, The Great Mother (1955)",
        },
        "description": "Nurturing, creation, dependency, and the devouring "
        "aspect. Maps onto platforms (nurturing ecosystem but creating "
        "dependency), organizational culture as mother figure, and the "
        "dual nature of protective systems that also constrain. Jung's "
        "CW9.1 devotes its longest essay to this archetype.",
    },
    {
        "slug": "the-wise-old-man",
        "name": "The Wise Old Man",
        "kind": "archetype",
        "source_frame": "mythology",
        "target_frame": "authority-and-mentorship",
        "categories": ["psychology", "organizational-behavior"],
        "source": "archive",
        "archive_refs": {
            "cw9_1": "The Phenomenology of the Spirit in Fairytales",
            "wikipedia": "Mentor",
            "pearson": "The Sage archetype",
        },
        "description": "Authority, mentorship, and accumulated wisdom. Maps "
        "onto legacy systems (deprecated but containing irreplaceable "
        "knowledge), senior engineers as institutional memory, and the "
        "tension between wisdom and obsolescence. Jung discusses this as "
        "'the spirit' archetype in fairytales -- the old man who appears "
        "at the threshold with guidance.",
    },
    {
        "slug": "the-divine-child",
        "name": "The Divine Child",
        "kind": "archetype",
        "source_frame": "mythology",
        "target_frame": "potential-and-emergence",
        "categories": ["psychology", "organizational-behavior"],
        "source": "archive",
        "archive_refs": {
            "cw9_1": "The Psychology of the Child Archetype (full essay)",
            "wikipedia": "Child archetype",
            "pearson": "The Innocent archetype",
        },
        "description": "Potential, new beginnings, and the futurity of the "
        "archetype. Maps onto greenfield projects, startup energy, the "
        "junior engineer's fresh perspective, and the paradox of the "
        "vulnerable-yet-invincible new thing. Jung emphasizes both the "
        "abandonment motif (the child left to fend for itself) and the "
        "invincibility motif (the child that survives against all odds).",
    },
    {
        "slug": "the-maiden",
        "name": "The Maiden (Kore)",
        "kind": "archetype",
        "source_frame": "mythology",
        "target_frame": "potential-and-emergence",
        "categories": ["psychology", "arts-and-culture"],
        "source": "archive",
        "archive_refs": {
            "cw9_1": "The Psychological Aspects of the Kore (full essay)",
            "wikipedia": "Puer aeternus",
        },
        "description": "Innocence, untested potential, and the threshold of "
        "transformation. Maps onto untested systems, the junior engineer "
        "before first production incident, and products before market "
        "contact. Jung pairs the Kore with the Mother as complementary "
        "aspects of the feminine archetype. The Persephone myth (descent "
        "and return) is the defining narrative.",
    },
    {
        "slug": "the-senex",
        "name": "The Senex (Crone)",
        "kind": "archetype",
        "source_frame": "mythology",
        "target_frame": "authority-and-mentorship",
        "categories": ["psychology", "organizational-behavior"],
        "source": "llm",
        "archive_refs": {
            "note": "Not a standalone essay in CW9.1. The Senex is the "
            "polar opposite of the Puer Aeternus, developed primarily by "
            "James Hillman in post-Jungian archetypal psychology. Jung "
            "discusses the pattern in The Phenomenology of the Spirit in "
            "Fairytales but does not use the term 'senex' as a label.",
        },
        "description": "Wisdom through age, rigidity, and the tension between "
        "preservation and stagnation. Maps onto deprecated-but-valuable "
        "knowledge, legacy codebases, institutional processes that once "
        "served well but now constrain. The Senex-Puer polarity (order "
        "vs. chaos, age vs. youth) is one of the most productive "
        "structural tensions in organizational analysis.",
    },
    {
        "slug": "the-shapeshifter",
        "name": "The Shapeshifter",
        "kind": "archetype",
        "source_frame": "mythology",
        "target_frame": "social-roles",
        "categories": ["psychology", "organizational-behavior", "software-engineering"],
        "source": "llm",
        "archive_refs": {
            "note": "Not a standalone archetype in Jung's CW9.1. The "
            "Shapeshifter appears in Christopher Vogler's 'The Writer's "
            "Journey' (1992) as a narrative archetype derived from "
            "Campbell's monomyth, which itself draws on Jung. The "
            "shapeshifting quality is discussed by Jung as an attribute "
            "of the Anima/Animus and Trickster rather than a standalone "
            "archetype.",
        },
        "description": "Adaptability, polymorphism, and identity fluidity. "
        "Maps onto the consultant who adapts to each client's culture, "
        "polymorphic code, and organizational roles that shift based on "
        "context. Structurally related to the Persona (masks) and "
        "Trickster (boundary-crossing) but emphasizes continuous "
        "transformation rather than transgression.",
    },
]

# ── Existing catalog entries to exclude ───────────────────────────────────
ALREADY_IN_CATALOG = {"the-trickster"}


def build_manifest():
    """Build the manifest from the candidate definitions."""
    candidates = []
    for c in CANDIDATES:
        if c["slug"] in ALREADY_IN_CATALOG:
            continue
        candidates.append(c)

    return {
        "project": "jungian-archetypes",
        "project_issue": 8,
        "source_type": "archive",
        "archive_urls": [
            "https://en.wikipedia.org/wiki/Category:Jungian_archetypes",
            "https://en.wikipedia.org/wiki/Jungian_archetypes",
            "https://scottjeffrey.com/classic-jungian-archetypes/",
            "https://iaap.org/resources/academic-resources/collected-works-abstracts/volume-9-1-archetypes-collective-unconscious/",
            "https://carolspearson.com/about/the-pearson-12-archetype-system-human-development-and-evolution",
        ],
        "candidates": candidates,
    }


def main():
    manifest = build_manifest()
    json.dump(manifest, sys.stdout, indent=2)
    print()  # trailing newline


if __name__ == "__main__":
    main()
