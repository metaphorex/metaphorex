---
project_issue: 8
repo: metaphorex/metaphorex
source_type: book
status: draft
---

# Playbook: Jungian Archetypes

## Source Description

Carl Gustav Jung's theory of archetypes, developed across the Collected
Works but concentrated in:

- **CW9.1**: *The Archetypes and the Collective Unconscious* (1959) --
  the primary source. Contains dedicated essays on the Mother, Child,
  Kore (Maiden), Spirit (Wise Old Man), and Trickster archetypes, plus
  theoretical foundations and the individuation process.
- **CW9.2**: *Aion: Researches into the Phenomenology of the Self* (1951)
  -- the Self, Shadow, Anima/Animus, and Syzygy.
- **CW7**: *Two Essays on Analytical Psychology* -- the Persona.
- **CW5**: *Symbols of Transformation* -- the Hero myth.
- *Man and His Symbols* (1964) -- posthumous popular overview, especially
  Henderson's "Ancient Myths and Modern Man."

Secondary sources that systematize Jung's archetypes for applied use:
- Carol Pearson, *Awakening the Heroes Within* (1991) -- the 12-archetype
  system (Innocent, Orphan, Warrior, Caregiver, Seeker, Lover, Destroyer,
  Creator, Sage, Jester, Magician, Ruler)
- Erich Neumann, *The Great Mother* (1955) -- exhaustive study of the
  Mother archetype
- James Hillman, various works -- post-Jungian archetypal psychology,
  especially the Senex-Puer polarity

Important: Jung explicitly stated that archetypes cannot be exhaustively
enumerated. The candidate list represents the **core named figures** that
appear consistently across Jung's writings and have demonstrable cross-domain
structural parallels. This is a finite, scoped extraction -- not an attempt
to catalog every archetypal pattern Jung ever discussed.

## Access Method

### Primary Archives

**Wikipedia Category: Jungian archetypes**
URL: https://en.wikipedia.org/wiki/Category:Jungian_archetypes

Enumerates 17 archetype articles. Provides structured descriptions,
cross-references to Jung's works, and bibliographic citations. Used to
verify which archetypes have established academic recognition as distinct
Jungian constructs.

**IAAP Collected Works Abstracts (Vol. 9.1)**
URL: https://iaap.org/resources/academic-resources/collected-works-abstracts/volume-9-1-archetypes-collective-unconscious/

The International Association for Analytical Psychology hosts chapter-level
abstracts of Jung's collected works. CW9.1's table of contents confirms
which archetypes Jung devoted full essays to:
1. Psychological Aspects of the Mother Archetype
2. The Psychology of the Child Archetype
3. The Psychological Aspects of the Kore
4. The Phenomenology of the Spirit in Fairytales (Wise Old Man)
5. On the Psychology of the Trickster-Figure

**Scott Jeffrey: Classic Jungian Archetypes**
URL: https://scottjeffrey.com/classic-jungian-archetypes/

Secondary compilation that lists 15+ archetypes with CW citations. Cross-
referenced against CW9.1 and CW9.2 to verify each archetype's provenance.

**Carol Pearson's 12-Archetype System**
URL: https://carolspearson.com/about/the-pearson-12-archetype-system-human-development-and-evolution

Pearson's system bridges Jung's clinical archetypes to branding and narrative.
Used to identify which Jungian archetypes have active cross-domain usage in
commercial and organizational contexts.

### Cross-Reference Methodology

Each candidate was verified against at least two of the following:
1. CW9.1 or CW9.2 table of contents (archetype has a dedicated essay)
2. Wikipedia Category:Jungian_archetypes (archetype has a standalone article)
3. Scott Jeffrey's compilation (archetype included with CW citations)
4. Pearson's 12-archetype system (archetype has commercial/narrative usage)

Candidates present in the CW table of contents are tagged `source: "archive"`.
Candidates from secondary Jungian literature without a CW essay are tagged
`source: "llm"` (the Senex and Shapeshifter).

### Already in Catalog (1 entry -- skipped)

- `the-trickster` -- seed entry, high quality, serves as quality bar

## Extraction Strategy

### For Miners

Each candidate in the manifest has:
- `slug`: filename for `catalog/mappings/{slug}.md`
- `name`: human-readable archetype name
- `kind`: `archetype` (all entries)
- `source_frame`: `mythology` (all entries -- archetypes originate in
  mythological/psychic structures)
- `target_frame`: the modern domain where the archetype's structural
  parallels are most productive
- `archive_refs`: dict of primary source citations (CW essay titles,
  Wikipedia articles, Pearson equivalents)
- `description`: brief note on cross-domain mappings to develop

**Miner workflow:**

1. Read `the-trickster` entry as the quality bar. Match its depth,
   structural rigor, and tone -- especially the "Where It Breaks" section.
2. For each candidate, consult the `archive_refs` to identify the primary
   Jungian source material. The CW essay titles tell you exactly where
   Jung discusses the archetype.
3. Write structural parallels as bullet points in "What It Brings" --
   each parallel should name the mythological pattern AND its modern
   counterpart (see the Trickster's "boundary crosser," "rule breaker as
   rule revealer," "sacred fool," "generative destruction" pattern).
4. "Where It Breaks" is the most important section. Every Jungian
   archetype has real limitations when mapped onto modern systems. Common
   failure modes:
   - **Gender essentialism** (especially Anima/Animus, Mother, Maiden)
   - **Cultural specificity presented as universal** (Jung's examples
     are overwhelmingly European/Christian)
   - **Romanticization of the archetype** (Hero worship, Shadow
     mystification)
   - **Flattening complexity** (reducing rich psychic structures to
     personality types or brand categories)
5. "Expressions" should include real-world terms that invoke the archetype:
   "shadow IT," "hero culture," "persona non grata," "greenfield project,"
   etc. These should be documented phrases, not invented examples.
6. Cross-reference `related:` links within the Jungian set and to existing
   catalog entries (especially `the-trickster` and `the-commons`).

### Batching Recommendation

Process in structural clusters:

- **Batch 1 -- The Psychic Structure (4):** the-self, the-shadow,
  the-persona, the-anima-animus. These are Jung's four core structural
  archetypes that describe the psyche's architecture. They relate to each
  other as a system.
- **Batch 2 -- The Figures (4):** the-hero, the-great-mother,
  the-wise-old-man, the-divine-child. These are the named figures that
  appear in myths and dreams. They map more directly onto narrative and
  organizational roles.
- **Batch 3 -- The Extended Set (3):** the-maiden, the-senex,
  the-shapeshifter. These require more careful sourcing (the Senex is
  post-Jungian, the Shapeshifter is Vogler/Campbell-derived).

### Frame Inventory

**Existing reusable frames:**
- `mythology` -- source frame for all entries
- `social-roles` -- target for Persona, Hero, Shapeshifter

**New frames needed:**
- `integration-and-wholeness` -- target for the Self
- `hidden-knowledge` -- target for the Shadow
- `creative-tension` -- target for Anima/Animus
- `nurturing-and-creation` -- target for Great Mother
- `authority-and-mentorship` -- target for Wise Old Man, Senex
- `potential-and-emergence` -- target for Divine Child, Maiden

These frames are cheap to create and structurally justified. Each captures
a distinct target domain that multiple archetypes (and future mappings)
can reference.

### Categories

All entries get `psychology` as primary category. Additional categories
per entry are specified in the manifest. The most common secondary
categories are:
- `organizational-behavior` -- for archetypes with strong org-design parallels
- `arts-and-culture` -- for archetypes prominent in narrative/branding
- `software-engineering` -- for archetypes with direct software pattern parallels
- `systems-thinking` -- for archetypes that describe system-level dynamics

## Schema Mapping

### Kind Assignment

All candidates are `kind: archetype`. This is consistent with the existing
`the-trickster` entry and with the Metaphorex schema, which defines
archetype as a valid kind alongside conceptual-metaphor, design-pattern,
paradigm, cross-field-mapping, and dead-metaphor.

### Author

All entries should use `author: jung` (or `author: jung-hillman` for the
Senex, `author: vogler-campbell` for the Shapeshifter).

## Gotchas

1. **The Trickster already exists.** It is a seed entry and the quality bar
   for this project. Miners should read it first and match its depth. New
   entries should cross-reference it in `related:`.

2. **Gender essentialism is a real problem.** The Anima/Animus archetype
   and the Mother/Maiden archetypes carry gender assumptions from 1920s-
   1950s Swiss psychiatry. The "Where It Breaks" sections must address
   this directly, not euphemistically. The structural insight (complementary
   inner aspects, creative tension) survives the critique; the gendered
   framing does not.

3. **Cultural specificity.** Jung's "universals" are drawn overwhelmingly
   from European mythology, Christian symbolism, and alchemical texts. The
   archetypes DO appear cross-culturally (the Trickster is the strongest
   example) but the specific expressions Jung uses are culturally bounded.
   Miners should note this and include non-European expressions where
   possible.

4. **The Pearson/branding flattening.** Carol Pearson's 12-archetype system
   and its branding derivatives (Harley-Davidson as "The Outlaw," Apple as
   "The Magician") have made these archetypes ubiquitous in marketing. This
   is useful context but should not be the primary framing. The entries
   should privilege Jung's structural depth over Pearson's applied
   simplification.

5. **The Senex and Shapeshifter are LLM-sourced.** The Senex comes from
   post-Jungian archetypal psychology (primarily Hillman), not from Jung's
   own named archetypes. The Shapeshifter comes from Vogler/Campbell
   narrative theory. Both have strong cross-domain mappings but the Surveyor
   should verify that their inclusion is warranted given the project's
   Jungian scope.

6. **No structured digital archive exists.** Unlike the Osaka University
   Metaphor List for Lakoff, there is no single HTML/JSON/CSV database of
   Jungian archetypes. The candidate list was compiled by cross-referencing
   the CW9.1 table of contents, Wikipedia's category page, and secondary
   compilations. The extraction script encodes these sources deterministically
   but cannot "scrape" a canonical list the way the MWLB playbook does.

7. **11 candidates is well under the 100 sub-issue cap.** No overflow
   handling needed.

8. **The Self is abstract.** Unlike the Hero or Shadow, the Self archetype
   is not a figure but a structural principle (integration, wholeness,
   mandala symbolism). The Miner will need to work harder to find concrete
   cross-domain mappings. Organizational mission statements, system
   architecture's "single source of truth," and the concept of personal
   integration are the most productive mapping targets.

9. **Related entries in the catalog.** Beyond `the-trickster`, several
   existing entries have structural connections:
   - `the-facade-pattern` -- structural parallel to the Persona
   - `technical-debt` -- structural parallel to the Shadow
   - `the-commons` -- archetypal thinking about shared resources
   - `creating-is-birthing` -- structural parallel to the Great Mother
   - `people-are-plants` -- developmental metaphors related to the Child
