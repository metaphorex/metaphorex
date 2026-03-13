#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""
Extract mythology/folklore metaphor candidates from structured web archives.

Sources:
1. Wikipedia: Category "Words and phrases derived from Greek mythology"
   (encoded as static dataset -- Wikipedia returns 403 on scraping)
2. Wikipedia: List of Greek mythological figures (filtered to those with
   modern metaphorical usage)
3. Cross-cultural mythology terms with active modern usage

Outputs JSON to stdout. Idempotent: same output on each run.
"""

import json
import sys

# --- Source 1: Wikipedia "Words and phrases derived from Greek mythology" ---
# Category page lists ~39 entries. Encoded from manual extraction since
# Wikipedia blocks automated scraping. URL:
# https://en.wikipedia.org/wiki/Category:Words_and_phrases_derived_from_Greek_mythology

WIKIPEDIA_GREEK_MYTH_PHRASES = [
    {
        "term": "Achilles' heel",
        "tradition": "Greek",
        "myth_source": "Achilles dipped in River Styx, held by heel",
        "modern_meaning": "A critical vulnerability in an otherwise strong system or person",
        "url": "https://en.wikipedia.org/wiki/Achilles%27_heel",
    },
    {
        "term": "Pandora's box",
        "tradition": "Greek",
        "myth_source": "Pandora opens jar releasing all evils, only Hope remains",
        "modern_meaning": "An action that unleashes irreversible unintended consequences",
        "url": "https://en.wikipedia.org/wiki/Pandora%27s_box",
    },
    {
        "term": "Trojan horse",
        "tradition": "Greek",
        "myth_source": "Greeks hide soldiers inside wooden horse gift to Troy",
        "modern_meaning": "Something that appears benign but conceals a hidden threat; foundational cybersecurity term",
        "url": "https://en.wikipedia.org/wiki/Trojan_Horse",
    },
    {
        "term": "Sisyphean task",
        "tradition": "Greek",
        "myth_source": "Sisyphus condemned to roll boulder uphill eternally",
        "modern_meaning": "Futile, endlessly repetitive labor that never reaches completion",
        "url": "https://en.wikipedia.org/wiki/Sisyphus",
    },
    {
        "term": "Midas touch",
        "tradition": "Greek",
        "myth_source": "King Midas granted wish that everything he touches turns to gold",
        "modern_meaning": "Ability to make everything profitable; also warns of monomaniacal optimization",
        "url": "https://en.wikipedia.org/wiki/Midas",
    },
    {
        "term": "Siren song",
        "tradition": "Greek",
        "myth_source": "Sirens lure sailors to destruction with irresistible singing",
        "modern_meaning": "A dangerously attractive temptation that leads to ruin",
        "url": "https://en.wikipedia.org/wiki/Siren_(mythology)",
    },
    {
        "term": "Prometheus",
        "tradition": "Greek",
        "myth_source": "Titan steals fire from gods, gives it to humanity, eternally punished",
        "modern_meaning": "Democratizing dangerous/powerful technology at personal cost; the cost of innovation",
        "url": "https://en.wikipedia.org/wiki/Prometheus",
    },
    {
        "term": "Hydra",
        "tradition": "Greek",
        "myth_source": "Lernaean Hydra regrows two heads for every one severed",
        "modern_meaning": "A problem that multiplies when you try to fix it",
        "url": "https://en.wikipedia.org/wiki/Lernaean_Hydra",
    },
    {
        "term": "Labyrinth",
        "tradition": "Greek",
        "myth_source": "Daedalus builds maze to contain the Minotaur",
        "modern_meaning": "Impenetrable complexity; bureaucratic or system complexity that traps you",
        "url": "https://en.wikipedia.org/wiki/Labyrinth",
    },
    {
        "term": "Icarus",
        "tradition": "Greek",
        "myth_source": "Icarus flies too close to sun on wax wings, falls to death",
        "modern_meaning": "Hubris in overreaching; ambition that ignores structural limits",
        "url": "https://en.wikipedia.org/wiki/Icarus",
    },
    {
        "term": "Phoenix",
        "tradition": "Greek/Egyptian",
        "myth_source": "Firebird dies in flames and is reborn from its own ashes",
        "modern_meaning": "Renewal or rebirth from destruction; comeback from catastrophic failure",
        "url": "https://en.wikipedia.org/wiki/Phoenix_(mythology)",
    },
    {
        "term": "Nemesis",
        "tradition": "Greek",
        "myth_source": "Goddess of divine retribution against hubris",
        "modern_meaning": "An inescapable rival or agent of downfall; karmic consequence",
        "url": "https://en.wikipedia.org/wiki/Nemesis",
    },
    {
        "term": "Herculean task",
        "tradition": "Greek/Roman",
        "myth_source": "Twelve Labors of Heracles, each seemingly impossible",
        "modern_meaning": "A task requiring extraordinary effort or strength",
        "url": "https://en.wikipedia.org/wiki/Labours_of_Hercules",
    },
    {
        "term": "Odyssey",
        "tradition": "Greek",
        "myth_source": "Odysseus's ten-year journey home from Troy",
        "modern_meaning": "A long, eventful, transformative journey; often implies the journey matters more than the destination",
        "url": "https://en.wikipedia.org/wiki/Odyssey",
    },
    {
        "term": "Cassandra",
        "tradition": "Greek",
        "myth_source": "Prophetess cursed to speak true prophecies no one believes",
        "modern_meaning": "Someone who correctly predicts disaster but is ignored",
        "url": "https://en.wikipedia.org/wiki/Cassandra",
    },
    {
        "term": "Narcissism",
        "tradition": "Greek",
        "myth_source": "Narcissus falls in love with his own reflection and wastes away",
        "modern_meaning": "Pathological self-absorption; clinical personality disorder",
        "url": "https://en.wikipedia.org/wiki/Narcissus_(mythology)",
    },
    {
        "term": "Chimera",
        "tradition": "Greek",
        "myth_source": "Fire-breathing creature with lion head, goat body, serpent tail",
        "modern_meaning": "An impossible or fantastical hybrid; unrealizable fantasy; also genetics term",
        "url": "https://en.wikipedia.org/wiki/Chimera_(mythology)",
    },
    {
        "term": "Cornucopia",
        "tradition": "Greek",
        "myth_source": "Horn of the goat Amalthea that suckled Zeus, magically produces abundance",
        "modern_meaning": "Inexhaustible supply; abundance",
        "url": "https://en.wikipedia.org/wiki/Cornucopia",
    },
    {
        "term": "Aegis",
        "tradition": "Greek",
        "myth_source": "Zeus's shield or breastplate, symbol of divine protection",
        "modern_meaning": "Protection, sponsorship, or authority ('under the aegis of')",
        "url": "https://en.wikipedia.org/wiki/Aegis",
    },
    {
        "term": "Mentor",
        "tradition": "Greek",
        "myth_source": "Mentor is the old friend Odysseus entrusts with his son's guidance; Athena disguises herself as Mentor",
        "modern_meaning": "A trusted guide or teacher; the concept of mentorship itself",
        "url": "https://en.wikipedia.org/wiki/Mentor_(Odyssey)",
    },
]

# --- Source 2: Non-Greek mythology and folklore ---
# These come from multiple Wikipedia articles on Norse, Arthurian, Jewish,
# Eastern, and modern fantasy traditions. URLs cited per entry.

CROSS_CULTURAL_MYTH = [
    {
        "term": "Ragnarok",
        "tradition": "Norse",
        "myth_source": "Twilight of the gods: cosmic battle destroying and remaking the world",
        "modern_meaning": "Catastrophic system collapse followed by rebirth; total reset",
        "url": "https://en.wikipedia.org/wiki/Ragnar%C3%B6k",
    },
    {
        "term": "Berserker",
        "tradition": "Norse",
        "myth_source": "Warriors who fought in trance-like fury, possibly shape-shifting into bears",
        "modern_meaning": "Uncontrolled destructive force; going berserk",
        "url": "https://en.wikipedia.org/wiki/Berserker",
    },
    {
        "term": "Valhalla",
        "tradition": "Norse",
        "myth_source": "Hall of the slain where warriors feast after dying in battle",
        "modern_meaning": "Ultimate reward for those who give everything; hall of fame",
        "url": "https://en.wikipedia.org/wiki/Valhalla",
    },
    {
        "term": "World tree",
        "tradition": "Norse/cross-cultural",
        "myth_source": "Yggdrasil connects nine worlds; axis mundi in many traditions",
        "modern_meaning": "Hierarchical interconnection; tree data structures; organizational hierarchy",
        "url": "https://en.wikipedia.org/wiki/Yggdrasil",
    },
    {
        "term": "Holy Grail",
        "tradition": "Arthurian",
        "myth_source": "Sacred cup from the Last Supper, sought by Arthurian knights",
        "modern_meaning": "The ultimate unattainable goal that justifies the quest itself",
        "url": "https://en.wikipedia.org/wiki/Holy_Grail",
    },
    {
        "term": "Excalibur",
        "tradition": "Arthurian",
        "myth_source": "Sword in the stone that proves Arthur's right to rule",
        "modern_meaning": "A tool or artifact that confers legitimacy; the right tool proving the right person",
        "url": "https://en.wikipedia.org/wiki/Excalibur",
    },
    {
        "term": "Round table",
        "tradition": "Arthurian",
        "myth_source": "Arthur's table with no head position, all knights equal",
        "modern_meaning": "Egalitarian governance or discussion format; flat hierarchy",
        "url": "https://en.wikipedia.org/wiki/Round_Table",
    },
    {
        "term": "Golem",
        "tradition": "Jewish folklore",
        "myth_source": "Clay servant animated by inscription, follows instructions literally",
        "modern_meaning": "Artificial servant that obeys the letter not the spirit of commands; ur-metaphor for AI alignment",
        "url": "https://en.wikipedia.org/wiki/Golem",
    },
    {
        "term": "Karma",
        "tradition": "Hindu/Buddhist",
        "myth_source": "Moral causation: actions in this life determine future consequences",
        "modern_meaning": "What goes around comes around; moral cause and effect",
        "url": "https://en.wikipedia.org/wiki/Karma",
    },
    {
        "term": "Yin and yang",
        "tradition": "Chinese/Taoist",
        "myth_source": "Complementary forces: dark/light, passive/active, female/male",
        "modern_meaning": "Complementary opposition; balance of contrasts; dual nature",
        "url": "https://en.wikipedia.org/wiki/Yin_and_yang",
    },
    {
        "term": "Koan",
        "tradition": "Zen Buddhist",
        "myth_source": "Paradoxical statement or question used to provoke enlightenment",
        "modern_meaning": "A productive paradox; a question that resists logical resolution but produces insight",
        "url": "https://en.wikipedia.org/wiki/K%C5%8Dan",
    },
    {
        "term": "Emperor's new clothes",
        "tradition": "European fairy tale (Andersen)",
        "myth_source": "Swindlers sell invisible clothes; everyone pretends to see them until a child speaks truth",
        "modern_meaning": "Collective delusion maintained by social pressure; the power of dissent",
        "url": "https://en.wikipedia.org/wiki/The_Emperor%27s_New_Clothes",
    },
    {
        "term": "Sorcerer's apprentice",
        "tradition": "European folklore (Goethe/Dukas)",
        "myth_source": "Apprentice enchants broom to do chores, cannot stop it, causes flood",
        "modern_meaning": "Automation that exceeds its operator's ability to control it",
        "url": "https://en.wikipedia.org/wiki/The_Sorcerer%27s_Apprentice",
    },
    {
        "term": "Rumpelstiltskin",
        "tradition": "Germanic fairy tale (Grimm)",
        "myth_source": "Creature demands firstborn child; defeated only when his true name is discovered",
        "modern_meaning": "The power of naming; control through identification; naming as power",
        "url": "https://en.wikipedia.org/wiki/Rumpelstiltskin",
    },
    {
        "term": "Alchemy",
        "tradition": "Medieval/cross-cultural",
        "myth_source": "Transmuting base metals into gold through secret knowledge",
        "modern_meaning": "Transformation of something common into something valuable; also implies pseudoscience",
        "url": "https://en.wikipedia.org/wiki/Alchemy",
    },
    {
        "term": "Dragon hoard",
        "tradition": "European/Norse folklore",
        "myth_source": "Dragons guard vast treasure hoards in caves, hoarding wealth they cannot use",
        "modern_meaning": "Wealth accumulation beyond use; rent-seeking; monopolistic resource capture",
        "url": "https://en.wikipedia.org/wiki/European_dragon",
    },
    {
        "term": "Chosen One",
        "tradition": "Cross-cultural (monomyth)",
        "myth_source": "Prophesied hero destined to save the world; Campbell's hero's journey",
        "modern_meaning": "Founder mythology; messianic leadership narrative in tech and politics",
        "url": "https://en.wikipedia.org/wiki/Chosen_one",
    },
    {
        "term": "Dark forest",
        "tradition": "European folklore / Liu Cixin",
        "myth_source": "Forest as realm of unknown danger (fairy tales); Liu Cixin's Dark Forest theory",
        "modern_meaning": "Game-theoretic hostility: hide or be destroyed; internet dark forest theory",
        "url": "https://en.wikipedia.org/wiki/Dark_forest_hypothesis",
    },
    {
        "term": "Trickster",
        "tradition": "Cross-cultural",
        "myth_source": "Loki, Coyote, Anansi, Hermes -- figures who subvert rules through cleverness",
        "modern_meaning": "Creative disruption; hacking social systems; the role of the provocateur",
        "url": "https://en.wikipedia.org/wiki/Trickster",
    },
    {
        "term": "Shapeshifter",
        "tradition": "Cross-cultural folklore",
        "myth_source": "Beings who change form: werewolves, selkies, kitsune, Proteus",
        "modern_meaning": "Adaptive identity; pivoting; strategic flexibility; also deception",
        "url": "https://en.wikipedia.org/wiki/Shapeshifting",
    },
]

# --- Source 3: Modern fantasy that has become metaphorical vocabulary ---
# These are from Tolkien, gaming culture, and modern fantasy that have
# crossed into general-purpose metaphorical usage.

MODERN_FANTASY_METAPHORS = [
    {
        "term": "The One Ring",
        "tradition": "Tolkien",
        "myth_source": "Ring of Power that corrupts its bearer; must be destroyed, not wielded",
        "modern_meaning": "Power that corrupts anyone who tries to use it for good; the case for destroying rather than capturing dangerous capabilities",
        "url": "https://en.wikipedia.org/wiki/One_Ring",
    },
    {
        "term": "Palantir",
        "tradition": "Tolkien",
        "myth_source": "Seeing-stones that enable remote surveillance but also expose the viewer to manipulation",
        "modern_meaning": "Surveillance technology that is bidirectional: watching makes you visible",
        "url": "https://en.wikipedia.org/wiki/Palant%C3%ADr",
    },
    {
        "term": "Mordor",
        "tradition": "Tolkien",
        "myth_source": "Industrialized wasteland ruled by Sauron; formerly beautiful land corrupted by power",
        "modern_meaning": "Industrial dystopia; a system optimized for control at the cost of all else",
        "url": "https://en.wikipedia.org/wiki/Mordor",
    },
    {
        "term": "The Shire",
        "tradition": "Tolkien",
        "myth_source": "Pastoral hobbit homeland, peaceful but threatened by industrial progress",
        "modern_meaning": "The pastoral ideal threatened by progress; what we fight to protect but cannot return to unchanged",
        "url": "https://en.wikipedia.org/wiki/The_Shire",
    },
    {
        "term": "Necromancy",
        "tradition": "Medieval/fantasy",
        "myth_source": "Magic that raises and controls the dead",
        "modern_meaning": "Reviving dead code, projects, companies, or ideas; maintaining zombie systems",
        "url": "https://en.wikipedia.org/wiki/Necromancy",
    },
]

# --- Source 4: Additional Greek/classical metaphors from archive research ---
# From YourDictionary, Examples.com, and Wikipedia category pages

ADDITIONAL_CLASSICAL = [
    {
        "term": "Damocles' sword",
        "tradition": "Greek",
        "myth_source": "Sword hung by single horsehair above Damocles to show precariousness of power",
        "modern_meaning": "Ever-present danger that comes with power or privilege; existential risk",
        "url": "https://en.wikipedia.org/wiki/Damocles",
    },
    {
        "term": "Gordian knot",
        "tradition": "Greek",
        "myth_source": "Impossibly complex knot; Alexander cuts it with his sword",
        "modern_meaning": "An intractable problem solved by bold, unconventional action rather than analysis",
        "url": "https://en.wikipedia.org/wiki/Gordian_Knot",
    },
    {
        "term": "Pyrrhic victory",
        "tradition": "Greek",
        "myth_source": "King Pyrrhus defeats Romans but at such devastating cost that he cannot continue",
        "modern_meaning": "A victory that costs so much it is effectively a defeat",
        "url": "https://en.wikipedia.org/wiki/Pyrrhic_victory",
    },
    {
        "term": "Procrustean bed",
        "tradition": "Greek",
        "myth_source": "Procrustes stretches or amputates travelers to fit his iron bed",
        "modern_meaning": "Forcing conformity to an arbitrary standard; one-size-fits-all approaches",
        "url": "https://en.wikipedia.org/wiki/Procrustes",
    },
    {
        "term": "Augean stables",
        "tradition": "Greek",
        "myth_source": "Stables of 3000 cattle, never cleaned; Heracles diverts a river to clean them",
        "modern_meaning": "Massive accumulated mess requiring radical rather than incremental cleanup",
        "url": "https://en.wikipedia.org/wiki/Augean_stables",
    },
    {
        "term": "Cerberus",
        "tradition": "Greek",
        "myth_source": "Three-headed dog guarding the gates of the underworld",
        "modern_meaning": "A fierce gatekeeper; authentication/access control systems (Kerberos protocol)",
        "url": "https://en.wikipedia.org/wiki/Cerberus",
    },
    {
        "term": "Elysium",
        "tradition": "Greek",
        "myth_source": "Paradise for the heroic dead; the blessed afterlife",
        "modern_meaning": "An ideal state or place; utopian aspiration",
        "url": "https://en.wikipedia.org/wiki/Elysium",
    },
    {
        "term": "Pandemonium",
        "tradition": "Christian/Milton",
        "myth_source": "Capital city of Hell in Paradise Lost; 'all demons'",
        "modern_meaning": "Complete chaos and disorder; originally a place-name, now a state of being",
        "url": "https://en.wikipedia.org/wiki/Pandemonium_(Paradise_Lost)",
    },
    {
        "term": "Scylla and Charybdis",
        "tradition": "Greek",
        "myth_source": "Sea monster and whirlpool on opposite sides of a strait; Odysseus must choose",
        "modern_meaning": "Being forced to choose between two equally dangerous options",
        "url": "https://en.wikipedia.org/wiki/Between_Scylla_and_Charybdis",
    },
    {
        "term": "Tantalus",
        "tradition": "Greek",
        "myth_source": "Punished to stand in water beneath fruit that recedes when he reaches for it",
        "modern_meaning": "Perpetual temptation without satisfaction; 'tantalizing'",
        "url": "https://en.wikipedia.org/wiki/Tantalus",
    },
    {
        "term": "Sphinx riddle",
        "tradition": "Greek/Egyptian",
        "myth_source": "Sphinx guards Thebes with a riddle; death for wrong answers",
        "modern_meaning": "A test that must be passed to proceed; gatekeeping through intellectual challenge",
        "url": "https://en.wikipedia.org/wiki/Sphinx",
    },
    {
        "term": "Trojan War",
        "tradition": "Greek",
        "myth_source": "Decade-long war launched over Helen; massive cost for a single cause",
        "modern_meaning": "Disproportionate conflict triggered by a seemingly minor cause",
        "url": "https://en.wikipedia.org/wiki/Trojan_War",
    },
    {
        "term": "Faustian bargain",
        "tradition": "Germanic/Christian",
        "myth_source": "Faust sells his soul to the devil for knowledge and power",
        "modern_meaning": "Trading long-term well-being for short-term gain; deals with moral cost",
        "url": "https://en.wikipedia.org/wiki/Faust",
    },
    {
        "term": "Pied Piper",
        "tradition": "Germanic folklore",
        "myth_source": "Piper rids town of rats, then leads children away when payment is refused",
        "modern_meaning": "Charismatic leader who attracts followers but whose true agenda is hidden or harmful",
        "url": "https://en.wikipedia.org/wiki/Pied_Piper_of_Hamelin",
    },
    {
        "term": "Ouroboros",
        "tradition": "Egyptian/Greek",
        "myth_source": "Serpent eating its own tail, symbol of eternal cyclic renewal",
        "modern_meaning": "Self-referential loops; infinite recursion; something that consumes itself to sustain itself",
        "url": "https://en.wikipedia.org/wiki/Ouroboros",
    },
]


def build_candidate(entry: dict) -> dict:
    """Convert a source entry into a manifest candidate."""
    term = entry["term"]
    tradition = entry["tradition"]

    # Generate slug from term
    slug = (
        term.lower()
        .replace("'s ", "-")
        .replace("' ", "-")
        .replace("the ", "")
        .replace(" ", "-")
        .replace("'", "")
        .strip("-")
    )

    # Determine target frame based on modern meaning keywords
    meaning = entry["modern_meaning"].lower()
    if any(w in meaning for w in ["software", "code", "computing", "cyber", "debug", "protocol"]):
        target_frame = "software-programs"
    elif any(w in meaning for w in ["organization", "governance", "hierarchy", "leadership", "bureaucra"]):
        target_frame = "governance"
    elif any(w in meaning for w in ["danger", "risk", "threat", "vulnerability", "security"]):
        target_frame = "technology-risk"
    elif any(w in meaning for w in ["power", "corrupt", "control"]):
        target_frame = "social-control"
    elif any(w in meaning for w in ["quest", "journey", "goal"]):
        target_frame = "journeys"
    elif any(w in meaning for w in ["paradox", "balance", "dual"]):
        target_frame = "integration-and-wholeness"
    elif any(w in meaning for w in ["wealth", "cost", "profit", "economic"]):
        target_frame = "economics"
    elif any(w in meaning for w in ["renewal", "rebirth", "transform"]):
        target_frame = "destruction"
    elif any(w in meaning for w in ["chaos", "disorder"]):
        target_frame = "destruction"
    elif any(w in meaning for w in ["knowledge", "insight", "prediction"]):
        target_frame = "hidden-knowledge"
    elif any(w in meaning for w in ["tempt", "attract", "desire"]):
        target_frame = "mental-experience"
    elif any(w in meaning for w in ["effort", "labor", "task", "futile", "repetit"]):
        target_frame = "event-structure"
    elif any(w in meaning for w in ["identity", "adapt", "flex"]):
        target_frame = "social-roles"
    elif any(w in meaning for w in ["automat", "servant", "instruct", "obey"]):
        target_frame = "rule-following"
    elif any(w in meaning for w in ["name", "naming"]):
        target_frame = "language"
    elif any(w in meaning for w in ["surveillance", "watch", "visible"]):
        target_frame = "surveillance"
    elif any(w in meaning for w in ["ideal", "pastoral", "utopi", "paradise"]):
        target_frame = "social-behavior"
    elif any(w in meaning for w in ["choice", "choose", "dilemma"]):
        target_frame = "causal-reasoning"
    elif any(w in meaning for w in ["conform", "standard", "force", "arbitrary"]):
        target_frame = "social-control"
    else:
        target_frame = "social-behavior"

    # Determine kind
    kind = "conceptual-metaphor"

    # Determine categories
    categories = ["mythology-and-religion"]
    if any(w in meaning for w in ["software", "code", "computing", "cyber", "protocol"]):
        categories.append("computer-science")
    if any(w in meaning for w in ["leadership", "governance", "founder"]):
        categories.append("organizational-behavior")
    if any(w in meaning for w in ["psychology", "narcis", "clinical"]):
        categories.append("psychology")

    return {
        "slug": slug,
        "name": term,
        "kind": kind,
        "source_frame": "mythology",
        "target_frame": target_frame,
        "categories": categories,
        "source": "archive",
        "archive_url": entry["url"],
        "tradition": tradition,
        "description": entry["modern_meaning"],
    }


def main():
    all_entries = (
        WIKIPEDIA_GREEK_MYTH_PHRASES
        + CROSS_CULTURAL_MYTH
        + MODERN_FANTASY_METAPHORS
        + ADDITIONAL_CLASSICAL
    )

    candidates = [build_candidate(e) for e in all_entries]

    # Deduplicate by slug
    seen = set()
    unique = []
    for c in candidates:
        if c["slug"] not in seen:
            seen.add(c["slug"])
            unique.append(c)

    output = {
        "project": "fantasy-mythology-folklore",
        "project_issue": 219,
        "source_type": "vein",
        "batch": 1,
        "entry_count": len(unique),
        "sources": [
            "https://en.wikipedia.org/wiki/Category:Words_and_phrases_derived_from_Greek_mythology",
            "https://www.yourdictionary.com/articles/english-words-greek-mythology",
            "https://en.wikipedia.org/wiki/Ragnar%C3%B6k",
            "https://en.wikipedia.org/wiki/Holy_Grail",
            "https://en.wikipedia.org/wiki/Golem",
            "https://en.wikipedia.org/wiki/One_Ring",
        ],
        "candidates": unique,
    }

    json.dump(output, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
