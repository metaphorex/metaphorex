---
project_issue: 971
repo: metaphorex/metaphorex
source_type: book
status: draft
---

# Playbook: Francis Bacon's Knowledge Archetypes

## Source Description

Francis Bacon, *Novum Organum* (1620), Book I. Two clusters of metaphorical
constructs from a single canonical work:

**Cluster 1: The Three Animal Archetypes (Aphorism XCV)**

Bacon distinguishes three approaches to knowledge production using animal
archetypes:

> "Those who have handled sciences have been either men of experiment or
> men of dogmas. The men of experiment are like the ant, they only collect
> and use; the reasoners resemble spiders, who make cobwebs out of their
> own substance. But the bee takes a middle course: it gathers its material
> from the flowers of the garden and of the field, but transforms and
> digests it by a power of its own."

- **The Ant** -- pure empiricist, collects without transforming
- **The Spider** -- pure rationalist, spins from within without grounding
- **The Honeybee** -- Bacon's ideal, gathers AND transforms

**Cluster 2: The Four Idols of the Mind (Aphorisms XXXIX-XLIV)**

Bacon's taxonomy of systematic cognitive error, each named with a vivid
metaphor:

- **Idols of the Tribe** -- biases inherent in human nature (the mind as
  "false mirror")
- **Idols of the Cave** -- individual biases from temperament and education
  (each person's private "cave or den," echoing Plato)
- **Idols of the Marketplace** -- distortions from imprecise language
  (words traded like commerce)
- **Idols of the Theatre** -- dogma from received philosophical systems
  ("stage plays" mistaken for reality)

These are among the earliest explicit uses of animal archetypes and
metaphorical taxonomy to map epistemological strategies. They remain active
in science studies, research methodology, knowledge management, and
cognitive bias discourse.

## Access Method

### Primary Archives

**Online Library of Liberty (Liberty Fund) -- Novum Organum full text**
URL: https://oll.libertyfund.org/titles/bacon-novum-organum

Complete English translation of Novum Organum. Public domain. The canonical
reference for the aphorism text.

**Hanover College History Department -- Novum Organum selections**
URL: https://history.hanover.edu/texts/bacon/novorg.html

Accessible HTML selections including the Four Idols aphorisms.

**Wikipedia: Novum Organum**
URL: https://en.wikipedia.org/wiki/Novum_Organum

Summary article with structured overview of both the animal archetypes
and the Four Idols. Cross-references to modern epistemological concepts.

**Wikipedia: Idola theatri**
URL: https://en.wikipedia.org/wiki/Idola_theatri

Dedicated article on the Four Idols with scholarly context.

**Stanford Encyclopedia of Philosophy: Francis Bacon**
URL: https://plato.stanford.edu/entries/francis-bacon/

Academic treatment of Bacon's epistemology. Contextualizes the Novum
Organum within Bacon's broader philosophical program.

**Farnam Street: Francis Bacon and the Four Idols of the Mind**
URL: https://fs.blog/francis-bacon-four-idols-mind/

Modern treatment mapping Bacon's idols onto contemporary cognitive bias
research. Useful for the "Expressions" section of each idol entry.

### Cross-Reference Methodology

All 7 candidates come directly from the Novum Organum text. The three
animal archetypes are from a single aphorism (XCV). The four idols are
from a contiguous set of aphorisms (XXXIX-XLIV). Every candidate is
verifiable against multiple public-domain translations.

0 of 7 candidates are LLM-sourced. All are `source: "archive"`.

## Extraction Strategy

### For Miners

Each candidate in the manifest has:
- `slug`: filename for `catalog/mappings/{slug}.md`
- `name`: human-readable name
- `kind`: `archetype` (animal trio) or `conceptual-metaphor` (idols)
- `source_frame`: the metaphorical source domain
- `target_frame`: the target domain Bacon maps onto
- `archive_refs`: primary source citations with URLs

**Miner workflow:**

1. Read `the-trickster` entry as the general quality bar for archetypes.
   For the idols (conceptual-metaphor kind), look at entries like
   `argument-is-war` for tone and structure.

2. For the **animal trio**, the three entries form a system. Each should
   cross-reference the other two in `related:`. The key structural insight
   is that Bacon is not merely describing three styles but arguing that
   only one (the bee) produces real knowledge. The ant and spider entries
   should foreground why Bacon thinks they fail; the bee entry should
   foreground what integration looks like.

3. For the **Four Idols**, each idol is a distinct metaphor for a class
   of cognitive error. The "What It Brings" section should map Bacon's
   17th-century language onto modern cognitive science terminology
   (confirmation bias, Dunning-Kruger, Sapir-Whorf, paradigm lock-in).
   The "Where It Breaks" section should note the limits of Bacon's own
   framework.

4. **"Where It Breaks" guidance for the animal trio:**
   - The ant/spider/bee trichotomy is elegant but oversimplified. Real
     knowledge work is not three discrete modes.
   - The bee metaphor implies a linear sequence (gather then transform),
     but actual scientific practice is iterative and messy.
   - Bacon's framing privileges natural philosophy (what we now call
     science) and undervalues the spider's mode in mathematics, logic,
     and formal systems where spinning from first principles IS the method.
   - The "digestion" metaphor obscures what transformation actually
     involves -- Bacon's inductive method was itself criticized by later
     philosophers (Hume, Popper) as insufficient.

5. **"Where It Breaks" guidance for the Four Idols:**
   - Bacon presents the idols as removable obstacles, but cognitive biases
     are features of human cognition, not merely errors to be purged.
   - The idol metaphor (from religious false worship) carries a moralistic
     tone that frames cognitive error as quasi-sinful -- a framing that
     does not survive contact with modern cognitive science.
   - Bacon's own method was not immune to his idols -- he rejected
     Copernican heliocentrism, showing that awareness of bias does not
     prevent it.

6. **"Expressions" should include:**
   - For the ant: "data hoarding," "analysis paralysis" (collecting more
     instead of synthesizing), "measurement without theory"
   - For the spider: "armchair philosophy," "pure theory," "castles in
     the air," "not even wrong"
   - For the bee: "evidence-based," "research and development" (R+D as
     institutional honeybee), "design thinking," "full-stack"
   - For each idol: modern cognitive bias terms that correspond to the
     Baconian category

### Batching Recommendation

Process in two batches matching the two clusters:

- **Batch 1 -- The Animal Trio (3):** ant-is-pure-empiricist,
  spider-is-pure-rationalist, honeybee-is-ideal-scientist. These form
  a coherent system and should be written together so the Miner can
  ensure consistent cross-referencing.

- **Batch 2 -- The Four Idols (4):** idols-of-the-tribe,
  idols-of-the-cave, idols-of-the-marketplace, idols-of-the-theatre.
  These also form a system and should cross-reference each other.

### Frame Inventory

**Existing reusable frames:**
- `animal-behavior` -- source frame for the animal trio
- `intellectual-inquiry` -- target frame for 6 of 7 entries
- `religion` -- source frame for Idols of the Tribe (idol = false god)
- `architecture-and-building` -- source frame for Idols of the Cave
- `economics` -- source frame for Idols of the Marketplace
- `narrative` -- source frame for Idols of the Theatre
- `language` -- target frame for Idols of the Marketplace

**New frames needed:** None. All source and target frames already exist.

### Categories

All entries get `philosophy` as primary category (Bacon is a philosopher;
the Novum Organum is a work of epistemology). Secondary categories:

- `cognitive-science` -- all entries (Bacon anticipates modern cognitive
  bias research)
- `psychology` -- Idols of the Cave (individual psychological distortion)
- `linguistics` -- Idols of the Marketplace (language as cognitive obstacle)

No new categories needed.

## Schema Mapping

### Kind Assignment

- **Animal trio:** `kind: archetype`. These are archetypes in the
  Metaphorex sense -- named figures that function as structural parallels
  across domains. Consistent with the existing `the-trickster` entry.

- **Four Idols:** `kind: conceptual-metaphor`. Each idol uses a specific
  metaphorical source domain (mirror, cave, marketplace, theatre) to
  structure understanding of a target domain (cognitive error). These are
  active conceptual metaphors, not archetypes or design patterns.

### Author

All entries: `author: bacon`

## Gotchas

1. **The animal trio is a system, not three independent entries.** The
   ant and spider are defined primarily by contrast with the bee. Miners
   should write all three together and ensure the cross-references are
   tight. Each entry's `related:` should include the other two slugs.

2. **The Four Idols are also a system.** Each idol's `related:` should
   include the other three slugs. Additionally, the idols relate to the
   animal trio: the spider is especially susceptible to idols of the cave
   and theatre; the ant is susceptible to idols of the tribe. These
   cross-references should be noted.

3. **"Idol" is itself a metaphor.** Bacon chose the word "idol" (Latin:
   idolum, from Greek eidolon = image, phantom) deliberately. The
   cognitive errors are false images worshipped as truth. This meta-
   metaphorical layer should be noted in entries but not belabored.

4. **Bacon rejected Copernicus.** This is the most pointed "Where It
   Breaks" fact for the entire project. The man who wrote the definitive
   early-modern guide to overcoming cognitive error was himself subject
   to idols of the theatre (accepting geocentrism from tradition). Miners
   should use this.

5. **The bee metaphor has been widely adopted.** It appears in science
   studies, design thinking, curation theory, and AI/ML framing ("data
   collection + model training = honey"). The honeybee entry should
   document these modern adoptions as expressions.

6. **7 candidates is well under the 100 sub-issue cap.** No overflow
   handling needed.

7. **No structured digital archive to scrape.** The Novum Organum is a
   single text, not a database. The extraction script encodes the
   candidates as static data derived from reading the primary source.
   The script is included for manifest reproducibility, not for dynamic
   scraping.

8. **The issue originally scoped to 3 candidates.** This playbook
   expands to 7 by including the Four Idols, which come from the same
   work, use the same metaphorical strategy (animal/architectural
   archetypes for epistemological concepts), and are arguably more
   influential than the animal trio in modern discourse. The Surveyor
   should confirm this scope expansion is warranted.
