---
project_issue: 4
repo: metaphorex/metaphorex
source_type: corpus
status: draft
---

# Playbook: Cross-Domain Conceptual Metaphors (Cognitive Linguistics Canon)

## Source Description

The cognitive linguistics canon -- the body of work originating with Lakoff
and Johnson (1980) and extended by Kovecses, Grady, Sweetser, Turner,
Fauconnier, and others -- is the primary theoretical source for conceptual
metaphor theory. This project catalogs the metaphors documented across that
literature: primary metaphors (universal, embodied), complex metaphors
(culturally constructed, compositional), and the event structure metaphor
system.

### Primary Sources
- Lakoff, G. & Johnson, M. *Metaphors We Live By* (1980)
- Lakoff, G. *Women, Fire, and Dangerous Things* (1987)
- Lakoff, G. & Turner, M. *More Than Cool Reason* (1989)
- Lakoff, G., Espenson, J. & Schwartz, A. *Master Metaphor List* (1991)
- Lakoff, G. & Johnson, M. *Philosophy in the Flesh* (1999)
- Grady, J.E. *Foundations of Meaning: Primary Metaphors and Primary Scenes* (1997)
- Kovecses, Z. *Metaphor: A Practical Introduction* (2002, 2nd ed. 2010)
- Sweetser, E. *From Etymology to Pragmatics* (1990)
- Turner, M. *The Literary Mind* (1996)
- Lakoff, G. *Moral Politics* (1996, 2nd ed. 2002)

### Structured Archives Found
- **Osaka University Conceptual Metaphor Home Page** (primary archive)
- **UC Berkeley Master Metaphor List PDF**
- **MetaNet Metaphor Wiki** (ICSI Berkeley)

This is a **vein** project: the cognitive linguistics literature continues
to produce new documented metaphors. This batch covers the canonical core
(~200 candidates). Future batches should target domain-specific extensions
(politics, medicine, law, religion, education).

Estimated yield for this batch: 200 candidates. Approximately 179 from
structured archives, 21 from LLM knowledge filling gaps in the archives
(primarily Grady's primary metaphors and Lakoff's political metaphors).

## Access Method

### Primary Archive: Osaka University Conceptual Metaphor Home Page

**URL:** https://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/MetaphorHome.html

Maintained by Masako Sugimoto at Osaka University. A hypertext version of
the Berkeley Master Metaphor List with 207 individual metaphor pages, each
containing examples, source/target domain links, and cross-references.

**Directory indexes:**
- Metaphor name index: http://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/metaphors/index.html
- Source domain index: http://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/sources/index.html
- Target domain index: http://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/targets/index.html

**Scraping script:** `scripts/scrape_osaka_archive.py`

The script fetches the HTML directory listing, extracts all `.html` file
names, and produces a JSON array of candidates with slug, name, and
source/target stubs derived from the filename convention `Target_Is_Source.html`.
Falls back to a cached file listing if the archive is unreachable.

**Access notes:**
- The archive is HTTP (not HTTPS) and occasionally slow
- File names use underscores for spaces and parentheses for qualifiers
- Some entries have duplicate files differing only by trailing dots
- The archive dates from the early 2000s and reflects the 1991 Master
  Metaphor List with some additions

### Secondary Archive: UC Berkeley Master Metaphor List PDF

**URL:** http://araw.mede.uic.edu/~alansz/metaphor/METAPHORLIST.pdf

The original 1991 compilation by Lakoff, Espenson, and Schwartz. Second
draft, ~200 pages. Organized into four sections: Event Structure, Mental
Events, Emotions, and Others. Contains the same metaphors as the Osaka
archive (which is a hypertext rendering of this document) plus additional
commentary and examples.

**Access notes:**
- PDF format, not easily machine-parseable
- The Osaka HTML archive is the preferred structured source
- Useful for miners who need extended examples and commentary

### Tertiary Archive: MetaNet Metaphor Wiki

**URL:** https://metaphor.icsi.berkeley.edu/pub/en/index.php/MetaNet_Metaphor_Wiki

A MediaWiki-based repository at ICSI Berkeley. Contains structured metaphor
entries with formal frame specifications, hierarchical relationships
(subcases, inherited structure), and multilingual data. More comprehensive
than the Master Metaphor List for some domains (especially political and
social metaphors).

**Access notes:**
- The wiki was intermittently unreachable during prospecting (timeouts)
- When accessible, individual metaphor pages contain rich structured data
- Future batches should attempt to scrape MetaNet via the MediaWiki API
  for metaphors not covered by the Osaka archive

### Cross-Reference Methodology

1. Scraped the Osaka archive directory listing (207 files)
2. Parsed filenames to extract metaphor names, slugs, and source/target stubs
3. Deduplicated (trailing-dot variants), yielding 203 unique entries
4. Cross-referenced against existing catalog (139 mappings), excluding
   24 entries that already exist
5. Assigned frames using the Osaka source/target domain indexes and
   existing frame inventory
6. Added 21 LLM-sourced candidates for metaphors documented in the
   literature but absent from the Osaka archive (Grady's primary metaphors,
   Lakoff's political metaphors, Lakoff & Turner's literary metaphors)

### Already in Catalog (excluded from manifest)

The following metaphors from the Osaka archive already exist in the catalog:

- `action-is-motion` -- EVENT STRUCTURE seed entry
- `activities-are-containers` -- seed entry
- `argument-is-war` -- seed entry (the ur-example)
- `argument-is-a-building` -- seed entry
- `argument-is-a-journey` -- seed entry
- `argument-is-dance` -- seed entry
- `causes-are-forces` -- recently mined (unix-c project cross-ref)
- `change-is-motion` -- EVENT STRUCTURE seed entry
- `communication-is-sending` -- THE CONDUIT METAPHOR variant
- `conscious-is-up` -- orientational metaphor
- `difficulties-are-impediments-to-motion` -- EVENT STRUCTURE
- `emotional-stability-is-balance` -- emotion metaphor
- `emotions-are-entities-within-a-person` -- emotion metaphor
- `existence-is-a-location` -- EVENT STRUCTURE
- `good-is-up`, `happy-is-up`, `more-is-up` -- orientational core
- `ideas-are-*` (9 entries) -- IDEAS cluster
- `life-is-a-journey` -- the canonical complex metaphor
- `love-is-a-journey`, `love-is-madness`, etc. -- LOVE cluster
- `obligations-are-forces` -- moral/social
- `people-are-machines` -- embodied cognition
- `properties-are-possessions` -- EVENT STRUCTURE (object case)
- `psychological-forces-are-physical-forces` -- primary metaphor
- `purposes-are-destinations` -- EVENT STRUCTURE
- `rational-is-up`, `status-is-up`, etc. -- orientational cluster
- `seeing-is-touching` -- perceptual metaphor
- `states-are-locations` -- EVENT STRUCTURE core
- `the-conduit-metaphor` -- communication
- `the-mind-is-a-brittle-object`, `the-mind-is-a-machine` -- MIND
- `the-visual-field-is-a-bounded-region`, `the-visual-field-is-a-container` -- PERCEPTION
- `theories-are-buildings` -- variant of existing entry
- `time-is-money`, `time-is-a-limited-resource` -- TIME cluster
- `understanding-is-seeing` -- epistemic metaphor

Miners should use `related:` links to connect new entries to these existing
ones where the metaphors share source or target domains.

## Extraction Strategy

### For Miners

Each candidate in the manifest has:
- `slug`: filename for `catalog/mappings/{slug}.md`
- `name`: the ALL-CAPS metaphor name
- `kind`: `primary-metaphor` (embodied, universal) or `conceptual-metaphor`
  (complex, potentially culture-specific)
- `source_frame` and `target_frame`: existing or needed frames
- `archive_ref`: where to find the source material
- `description`: brief note for context

**Miner workflow:**

1. For `source: archive` candidates, start with the Osaka archive page
   linked in `archive_ref`. Each page contains:
   - The metaphor name and its source/target domains
   - Linguistic examples with citations
   - Cross-references to related metaphors
   - Links to the source and target domain pages

2. For additional depth, consult the Berkeley Master Metaphor List PDF
   (http://araw.mede.uic.edu/~alansz/metaphor/METAPHORLIST.pdf) for the
   same metaphor. The PDF often has more extended discussion than the HTML.

3. For `source: llm` candidates, the `archive_ref` field lists specific
   publications to consult. The LLM-sourced entries are metaphors that are
   well-documented in the literature but absent from the Osaka archive.

4. The "What It Brings" section should explain the structural mapping:
   what correspondences exist between source and target, and how the
   metaphor structures thinking. Use the Osaka page's examples but go beyond
   them to show how the metaphor operates in everyday language.

5. The "Where It Breaks" section should identify:
   - What aspects of the target domain the metaphor cannot capture
   - What the metaphor hides or distorts
   - Cases where the metaphor leads to bad reasoning

6. The "Origin Story" section should cite the original theorists and
   explain when/how the metaphor was first identified. Most entries trace
   to Lakoff & Johnson (1980) or the Master Metaphor List (1991).

7. Primary metaphors (kind: `primary-metaphor`) should emphasize:
   - The embodied grounding (what sensorimotor experience correlates with
     what subjective experience)
   - Universality (cross-linguistic evidence if available)
   - How they compose into complex metaphors

### Batching Recommendation

Process in thematic clusters for coherence:

**Batch 1 -- Primary Metaphors (12):**
`affection-is-warmth`, `knowing-is-seeing`, `understanding-is-grasping`,
`categories-are-containers`, `similarity-is-closeness`, `help-is-support`,
`importance-is-size`, `bad-is-stinky`, `intimacy-is-closeness`,
`difficulties-are-burdens`, `time-is-motion`, `purposes-are-desired-objects`

These are the most universal, most structurally clear, and most foundational.
They compose into everything else.

**Batch 2 -- Event Structure System (15):**
`event-structure-location-case`, `event-structure-object-case`,
`action-is-self-propelled-motion`, `actions-are-self-propelled-motions`,
`change-is-replacement`, `change-of-state-is-change-of-direction`,
`causation-is-control-over-relative-location`, `causation-is-commercial-transaction`,
and related entries. These form a coherent system.

**Batch 3 -- Emotion Metaphors (20):**
`anger-is-heat`, `anger-is-a-heated-fluid-in-a-container`, `fear-is-cold`,
`desire-is-hunger`, `disgust-is-nausea`, `hope-is-light`,
`strong-emotions-are-madness`, `intense-emotions-are-heat`,
`emotional-intimacy-is-physical-closeness`, and related entries.
The emotion domain is among the most thoroughly studied in CMT.

**Batch 4 -- Belief and Knowledge (12):**
`beliefs-are-possessions`, `beliefs-are-locations`, `beliefs-are-guides`,
`beliefs-are-fashions`, `beliefs-are-beings-with-a-life-cycle`,
`dangerous-beliefs-are-contagious-diseases`, and related entries.

**Batch 5 -- Morality and Society (8):**
`morality-is-purity`, `morality-is-cleanliness`, `morality-is-straightness`,
`morality-is-accounting`, `nation-is-a-person`, `nation-is-a-family`,
`society-is-a-body`, `relationship-is-kinship`

**Batch 6 -- Theory and Intellectual Life (10):**
`theories-are-constructed-objects`, `theories-are-cloth`,
`theories-are-covers-for-the-facts`, `theories-are-beings-with-life-cycles`,
`conducting-research-is-solving-a-puzzle`, `subjects-are-areas`,
`theoretical-debate-is-competition`, and related entries.

**Batch 7 -- Remaining Archive Entries (varied):**
All remaining Osaka archive entries not covered above.

**Batch 8 -- Complex/Political Metaphors (LLM-sourced):**
`nation-is-a-person`, `nation-is-a-family`, `life-is-a-story`,
`the-great-chain-of-being`, `death-is-departure`, `argument-is-a-container`.
These need extra verification since they are LLM-sourced.

### Future Batches (vein continuation)

After completing this batch, the next prospecting run should target:
1. **MetaNet Wiki scraping** -- the wiki contains hundreds of metaphors
   not in the Osaka archive, especially political and social metaphors
2. **Kovecses's domain-specific lists** -- metaphors of emotion (Kovecses
   1986, 2000), anger across cultures, happiness metaphors
3. **Sweetser's historical metaphors** -- Indo-European perception-to-
   cognition shifts documented in *From Etymology to Pragmatics*
4. **Fauconnier & Turner's blending examples** -- conceptual blending
   theory produces metaphor-adjacent constructions
5. **Cross-cultural metaphors** -- Boroditsky, Yu, Ibarretxe-Antunano
   on metaphors that vary across languages

## Schema Mapping

### Kind Assignment

| Kind | Count | Criteria |
|------|-------|----------|
| `primary-metaphor` | ~20 | Universal, embodied, from Grady (1997) or Lakoff & Johnson (1999) table |
| `conceptual-metaphor` | ~180 | Complex, culturally constructed, from Master Metaphor List |

The distinction matters for the catalog: primary metaphors are building
blocks that compose into complex metaphors. The `kind` field should help
readers understand whether a metaphor is a universal cognitive primitive
or a culturally constructed composite.

### Frame Inventory

**Existing frames that cover most of the source domains:**
- `embodied-experience` -- balance, motion, warmth/cold, grasping, etc.
- `physics` -- forces, moving objects, gravity
- `fluid-dynamics` -- substances, fluids, liquids
- `containers` -- containment, bounded regions, shapes
- `journeys` -- paths, destinations, locations, forward motion
- `war` -- weapons, adversaries, fighting
- `economics` -- possessions, resources, money, commercial transactions
- `architecture-and-building` -- constructed objects
- `manufacturing` -- making, machines
- `horticulture` -- cultivation, plants
- `life-course` -- birth, death, life cycles
- `social-roles` -- kinship, people, family structure
- `vision` -- light, perception, visibility
- `food-and-cooking` -- food, eating, hunger
- `medicine` -- disease, illness
- `creative-process` -- musical harmony
- `competition` -- races, physical aggression

**New frame potentially needed:**
- `ethics-and-morality` -- for MORALITY IS PURITY, MORALITY IS CLEANLINESS,
  MORAL ACCOUNTING target domains. Currently no frame covers moral reasoning
  as a target domain. The Miner for batch 5 should create this frame.

### Categories

All entries get `cognitive-science` and `linguistics` as primary categories.
Additional categories by domain:
- Emotion metaphors: `psychology`
- Morality metaphors: `philosophy`
- Political metaphors: `philosophy`, `social-dynamics`
- Perception metaphors: `philosophy` (epistemology)
- Time metaphors: `philosophy`

## Gotchas

1. **The Osaka archive reflects the 1991 Master Metaphor List.** It predates
   Grady's primary metaphor theory (1997), Lakoff & Johnson's *Philosophy
   in the Flesh* (1999), and MetaNet. Many important primary metaphors
   (KNOWING IS SEEING, UNDERSTANDING IS GRASPING, CATEGORIES ARE CONTAINERS)
   are absent from the archive. The LLM-sourced candidates fill this gap,
   but miners should verify them against the cited publications.

2. **The EVENT STRUCTURE system is a system, not a list.** The Osaka archive
   has two entries: `Event_Structure_(location_Case).html` and
   `Event_Structure_(object_Case).html`. These are not individual metaphors
   but documented metaphor systems containing many sub-mappings. Miners
   handling these entries should produce a single rich entry that describes
   the system, not try to split it into separate metaphors (the component
   metaphors like STATES ARE LOCATIONS already have their own entries).

3. **Duplicate variants.** Some metaphors appear in both location-case and
   object-case forms (e.g., `Change_Is_Motion.html` and
   `Change_Is_Motion_(location).html`). The script deduplicates by slug,
   but miners should check both archive pages for complementary content.

4. **Misspellings in the Osaka archive.** "Complience" (should be
   "Compliance") appears in three filenames. The manifest preserves the
   original filenames in `archive_ref` but uses corrected slugs.

5. **Frame assignment is approximate.** The `source_frame` and `target_frame`
   assignments in the manifest are derived from keyword matching against
   existing frames. Miners should verify and adjust frame assignments
   based on the actual content of each metaphor. Some entries (e.g.,
   A FORCE IS A MOVING OBJECT) have both source and target in the same
   frame, which likely indicates a mapping error that the Miner should fix.

6. **Cross-references are essential.** Many metaphors in this project are
   related to entries already in the catalog (see "Already in Catalog"
   above). Miners must populate the `related:` field to create a connected
   graph of metaphors. The Osaka archive's own cross-reference links
   provide a starting point.

7. **The Master Metaphor List is not exhaustive.** It represents "approximately
   20% of available compiled metaphor research" (per its own introduction).
   This is why the project is typed as `vein`, not `archive`. Future batches
   will expand the coverage.

8. **Primary metaphors compose.** LOVE IS A JOURNEY composes from multiple
   primary metaphors: PURPOSES ARE DESTINATIONS + RELATIONSHIPS ARE
   ENCLOSURES + INTIMACY IS CLOSENESS + etc. Miners working on complex
   metaphors should note which primary metaphors they compose from, linking
   via `related:`.

9. **Cultural specificity varies.** Primary metaphors (batch 1) are
   hypothesized to be universal. Complex metaphors (batches 2-7) may be
   English-specific or Western-culture-specific. Miners should note any
   known cross-linguistic variation in the "Origin Story" section.

10. **The Osaka archive may go offline.** It is an academic personal page
    from the early 2000s. The scraping script includes a full cached file
    listing as fallback. If the archive becomes permanently unreachable,
    the PDF at UIC remains the authoritative source.
