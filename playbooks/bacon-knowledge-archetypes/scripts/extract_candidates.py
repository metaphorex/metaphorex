#!/usr/bin/env python3
"""
Extract Francis Bacon knowledge archetype candidates for the Metaphorex catalog.

Source: Francis Bacon, *Novum Organum* (1620), Book I, Aphorism XCV.

Primary archive references:
1. Online Library of Liberty (Liberty Fund) -- full text of Novum Organum
   https://oll.libertyfund.org/titles/bacon-novum-organum
2. Hanover College History Department -- Novum Organum selections
   https://history.hanover.edu/texts/bacon/novorg.html
3. Wikipedia: Novum Organum
   https://en.wikipedia.org/wiki/Novum_Organum
4. Stanford Encyclopedia of Philosophy: Francis Bacon
   https://plato.stanford.edu/entries/francis-bacon/
5. Wikisource: Novum Organum Book I (Spedding translation)
   https://en.wikisource.org/wiki/Novum_Organum/Book_I_(Spedding)

Bacon's Aphorism XCV distinguishes three approaches to knowledge production
using animal archetypes:

    "Those who have handled sciences have been either men of experiment or
    men of dogmas. The men of experiment are like the ant, they only collect
    and use; the reasoners resemble spiders, who make cobwebs out of their
    own substance. But the bee takes a middle course: it gathers its material
    from the flowers of the garden and of the field, but transforms and
    digests it by a power of its own."

This is a small, self-contained project: 3 core archetypes from a single
canonical aphorism. No scraping needed -- the source text is public domain
and the candidate set is definitionally complete (Bacon names exactly three).

Additionally, Bacon's Four Idols (Aphorisms XXXIX-XLIV) are rich
metaphorical constructs about cognitive bias that warrant inclusion as
related candidates. These use theatrical, architectural, and commercial
metaphors for epistemic error.

Usage:
    python3 extract_candidates.py > candidates.json
"""

import json
import sys

# -- Primary source: Novum Organum, Book I, Aphorism XCV ----------------
# Bacon names exactly three animal archetypes. This is exhaustive.
APHORISM_XCV_TEXT = (
    "Those who have handled sciences have been either men of experiment "
    "or men of dogmas. The men of experiment are like the ant, they only "
    "collect and use; the reasoners resemble spiders, who make cobwebs "
    "out of their own substance. But the bee takes a middle course: it "
    "gathers its material from the flowers of the garden and of the "
    "field, but transforms and digests it by a power of its own."
)

# -- Primary source: Novum Organum, Book I, Aphorisms XXXIX-XLIV --------
# Bacon names exactly four "idols" (systematic cognitive biases).
IDOLS_SOURCE = {
    "tribe": {
        "aphorism": "XLI",
        "text": (
            "The idols of the tribe have their foundation in human nature "
            "itself... The human understanding is like a false mirror, "
            "which, receiving rays irregularly, distorts and discolors the "
            "nature of things by mingling its own nature with it."
        ),
    },
    "cave": {
        "aphorism": "XLII",
        "text": (
            "The idols of the cave are the idols of the individual man. "
            "For everyone has a cave or den of his own, which refracts "
            "and discolors the light of nature."
        ),
    },
    "marketplace": {
        "aphorism": "XLIII",
        "text": (
            "There are also idols formed by the intercourse and association "
            "of men with each other, which I call idols of the marketplace, "
            "on account of the commerce and consort of men there."
        ),
    },
    "theatre": {
        "aphorism": "XLIV",
        "text": (
            "Lastly, there are idols which have immigrated into men's minds "
            "from the various dogmas of philosophies... These I call idols "
            "of the theatre, because in my judgment all the received systems "
            "are but so many stage plays, representing worlds of their own "
            "creation after an unreal and scenic fashion."
        ),
    },
}

# -- Candidate definitions -----------------------------------------------

CANDIDATES = [
    # === The three animal archetypes (Aphorism XCV) ===
    {
        "slug": "ant-is-pure-empiricist",
        "name": "The Ant Is the Pure Empiricist",
        "kind": "archetype",
        "source_frame": "animal-behavior",
        "target_frame": "intellectual-inquiry",
        "categories": ["philosophy", "cognitive-science"],
        "source": "archive",
        "archive_refs": {
            "novum_organum": "Book I, Aphorism XCV",
            "liberty_fund": "https://oll.libertyfund.org/titles/bacon-novum-organum",
            "wikipedia": "https://en.wikipedia.org/wiki/Novum_Organum",
        },
        "description": (
            "The ant collects and stores without transforming. Bacon's "
            "archetype for pure empiricism: data accumulation without "
            "synthesis. Maps onto data hoarding, measurement without "
            "theory, the researcher who gathers endlessly but never "
            "publishes. The critique is that collection without "
            "transformation is not yet knowledge."
        ),
    },
    {
        "slug": "spider-is-pure-rationalist",
        "name": "The Spider Is the Pure Rationalist",
        "kind": "archetype",
        "source_frame": "animal-behavior",
        "target_frame": "intellectual-inquiry",
        "categories": ["philosophy", "cognitive-science"],
        "source": "archive",
        "archive_refs": {
            "novum_organum": "Book I, Aphorism XCV",
            "liberty_fund": "https://oll.libertyfund.org/titles/bacon-novum-organum",
            "wikipedia": "https://en.wikipedia.org/wiki/Novum_Organum",
        },
        "description": (
            "The spider spins webs from its own substance. Bacon's "
            "archetype for pure rationalism: theory-building from first "
            "principles without empirical grounding. Maps onto armchair "
            "philosophy, unfalsifiable frameworks, the theorist who never "
            "tests. Elegant but disconnected from reality."
        ),
    },
    {
        "slug": "honeybee-is-ideal-scientist",
        "name": "The Honeybee Is the Ideal Scientist",
        "kind": "archetype",
        "source_frame": "animal-behavior",
        "target_frame": "intellectual-inquiry",
        "categories": ["philosophy", "cognitive-science"],
        "source": "archive",
        "archive_refs": {
            "novum_organum": "Book I, Aphorism XCV",
            "liberty_fund": "https://oll.libertyfund.org/titles/bacon-novum-organum",
            "wikipedia": "https://en.wikipedia.org/wiki/Novum_Organum",
        },
        "description": (
            "The bee gathers from the world AND transforms through "
            "digestion. Bacon's ideal: empirical collection plus rational "
            "synthesis. Maps onto the scientific method itself, design "
            "thinking (research + prototyping), curation (selection + "
            "arrangement), and ML pipelines (data collection + model "
            "training). The most productive of the three archetypes "
            "because it names the integration that makes knowledge."
        ),
    },
    # === The Four Idols (Aphorisms XXXIX-XLIV) ===
    {
        "slug": "idols-of-the-tribe",
        "name": "Idols of the Tribe",
        "kind": "conceptual-metaphor",
        "source_frame": "religion",
        "target_frame": "intellectual-inquiry",
        "categories": ["philosophy", "cognitive-science"],
        "source": "archive",
        "archive_refs": {
            "novum_organum": "Book I, Aphorisms XXXIX and XLI",
            "liberty_fund": "https://oll.libertyfund.org/titles/bacon-novum-organum",
            "fs_blog": "https://fs.blog/francis-bacon-four-idols-mind/",
        },
        "description": (
            "The mind as 'false mirror' -- systematic distortions built "
            "into human nature itself. Bacon's term for what we now call "
            "cognitive biases. The tribe is the human species; these idols "
            "afflict everyone. Anticipates confirmation bias, anchoring, "
            "and the availability heuristic by 350 years."
        ),
    },
    {
        "slug": "idols-of-the-cave",
        "name": "Idols of the Cave",
        "kind": "conceptual-metaphor",
        "source_frame": "architecture-and-building",
        "target_frame": "intellectual-inquiry",
        "categories": ["philosophy", "cognitive-science", "psychology"],
        "source": "archive",
        "archive_refs": {
            "novum_organum": "Book I, Aphorisms XXXIX and XLII",
            "liberty_fund": "https://oll.libertyfund.org/titles/bacon-novum-organum",
            "fs_blog": "https://fs.blog/francis-bacon-four-idols-mind/",
            "plato_allusion": "Explicit reference to Plato's cave allegory",
        },
        "description": (
            "Each person's private 'cave or den' that refracts the light "
            "of nature. Individual biases from temperament, education, and "
            "habit. Bacon deliberately echoes Plato's cave allegory but "
            "personalizes it: not humanity trapped in one cave, but each "
            "person trapped in their own. Maps onto filter bubbles, "
            "specialization blindness, and the curse of expertise."
        ),
    },
    {
        "slug": "idols-of-the-marketplace",
        "name": "Idols of the Marketplace",
        "kind": "conceptual-metaphor",
        "source_frame": "economics",
        "target_frame": "language",
        "categories": ["philosophy", "linguistics", "cognitive-science"],
        "source": "archive",
        "archive_refs": {
            "novum_organum": "Book I, Aphorisms XXXIX and XLIII",
            "liberty_fund": "https://oll.libertyfund.org/titles/bacon-novum-organum",
            "fs_blog": "https://fs.blog/francis-bacon-four-idols-mind/",
        },
        "description": (
            "Language distorts thought through 'the ill and unfit choice "
            "of words.' The marketplace is where people trade words as "
            "commerce; imprecise terms 'force and overrule the "
            "understanding.' Anticipates the Sapir-Whorf hypothesis, "
            "Wittgenstein's language games, and modern concerns about "
            "jargon, buzzwords, and euphemism as cognitive obstacles."
        ),
    },
    {
        "slug": "idols-of-the-theatre",
        "name": "Idols of the Theatre",
        "kind": "conceptual-metaphor",
        "source_frame": "narrative",
        "target_frame": "intellectual-inquiry",
        "categories": ["philosophy", "cognitive-science"],
        "source": "archive",
        "archive_refs": {
            "novum_organum": "Book I, Aphorisms XXXIX and XLIV",
            "liberty_fund": "https://oll.libertyfund.org/titles/bacon-novum-organum",
            "fs_blog": "https://fs.blog/francis-bacon-four-idols-mind/",
            "wikipedia": "https://en.wikipedia.org/wiki/Idola_theatri",
        },
        "description": (
            "Received philosophical systems as 'stage plays, representing "
            "worlds of their own creation after an unreal and scenic "
            "fashion.' Dogma as performance. Maps onto paradigm lock-in, "
            "cargo cult science, and the way intellectual fashions ossify "
            "into orthodoxy. The theatrical metaphor implies that the "
            "audience mistakes the performance for reality."
        ),
    },
]


def build_manifest():
    """Build the manifest from the candidate definitions."""
    return {
        "project": "bacon-knowledge-archetypes",
        "project_issue": 971,
        "source_type": "archive",
        "archive_urls": [
            "https://oll.libertyfund.org/titles/bacon-novum-organum",
            "https://en.wikipedia.org/wiki/Novum_Organum",
            "https://history.hanover.edu/texts/bacon/novorg.html",
            "https://plato.stanford.edu/entries/francis-bacon/",
            "https://fs.blog/francis-bacon-four-idols-mind/",
        ],
        "candidates": CANDIDATES,
    }


def main():
    manifest = build_manifest()
    json.dump(manifest, sys.stdout, indent=2)
    print()  # trailing newline


if __name__ == "__main__":
    main()
