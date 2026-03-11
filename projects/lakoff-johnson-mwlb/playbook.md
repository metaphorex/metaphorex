---
project_issue: 1
repo: metaphorex/metaphorex
source_type: book
status: draft
---

# Playbook: Lakoff & Johnson -- Metaphors We Live By (1980)

## Source Description

George Lakoff and Mark Johnson, *Metaphors We Live By* (University of
Chicago Press, 1980; 2003 edition with Afterword). The foundational text on
conceptual metaphor theory. Introduces the claim that everyday language is
structured by conceptual metaphors and catalogs dozens of examples across
30 chapters organized into structural, orientational, and ontological types.

The book discusses approximately 60-70 distinct conceptual metaphors,
though the exact count varies depending on whether entailments (e.g., TIME
IS A LIMITED RESOURCE as an entailment of TIME IS MONEY) are counted as
separate metaphors. This manifest counts them separately, following the
Osaka archive's convention.

## Access Method

### Primary Archive: Osaka University Conceptual Metaphor Database

**URL:** https://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/MetaphorHome.html

The Osaka University archive (maintained by Prof. Sugimoto) hosts the
complete Master Metaphor List compiled by Lakoff, Espenson, and Schwartz
at UC Berkeley's Cognitive Linguistics Group (1991). It contains 207 HTML
pages, one per metaphor, organized into three indexes:

- **By metaphor name:** https://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/metaphors/
- **By source domain:** https://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/sources/index.html
- **By target domain:** https://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/targets/index.html

Each HTML page contains: metaphor name, source domain, target domain,
example expressions, and sometimes cross-references to related metaphors.
Pages do NOT cite which book each metaphor comes from -- the Master
Metaphor List is a compilation across all of Lakoff's work plus student
research.

### Secondary Archive: Master Metaphor List PDF (UIC)

**URL:** http://araw.mede.uic.edu/~alansz/metaphor/METAPHORLIST.pdf

The original PDF compiled by Lakoff, Espenson, and Schwartz (1991). Same
content as the Osaka HTML archive but in PDF format. Certificate issues
prevent automated fetching; the Osaka HTML version is preferred for
scraping.

### Cross-Reference Methodology

The Master Metaphor List (207 entries) is a **superset** of the metaphors
in MWLB (~60-70 entries). To identify the MWLB subset, this prospecting
used:

1. Multiple independent chapter-by-chapter summaries of MWLB:
   - Tomaszewski notes (tomeri.org) -- chapter-numbered references
   - WiseWords book summary (wisewords.blog) -- categorized list
   - Sloopie72 review (sloopie72.wordpress.com) -- annotated examples
   - Bookey chapter summaries (bookey.app) -- detailed per-chapter

2. The book's table of contents (30 chapters) mapped to metaphor types:
   - Ch 1-3: Structural metaphors (ARGUMENT IS WAR, TIME IS MONEY)
   - Ch 4-5: Orientational metaphors (HAPPY IS UP, MORE IS UP, etc.)
   - Ch 6-7: Ontological metaphors (INFLATION IS AN ENTITY, THE MIND IS A MACHINE)
   - Ch 8: Metonymy (excluded -- not metaphors)
   - Ch 9: Time metaphors and coherence
   - Ch 10: "Some Further Examples" -- the big chapter with 15+ metaphors
   - Ch 11-13: Partial structuring and grounding
   - Ch 14: Causation
   - Ch 15-17: Coherence across metaphors (LOVE cluster)
   - Ch 18-30: Philosophy of metaphor (fewer new metaphors introduced)

3. Cross-matching each MWLB metaphor against the 207 Osaka archive
   filenames. Matches are tagged `source: "archive"`. Metaphors discussed
   in MWLB but not present in the Osaka archive by a matching name are
   tagged `source: "llm"`.

### Already in Catalog (7 entries -- skipped)

The following MWLB metaphors already exist in the metaphorex catalog
and are excluded from the candidate manifest:

- `argument-is-war` (seed entry)
- `argument-is-dance` (seed entry)
- `time-is-money` (mined from prior run)
- `understanding-is-seeing` (mined from prior run)
- `love-is-a-journey` (mined from prior run)
- `ideas-are-food` (mined from prior run)
- `theories-are-buildings` (mined from prior run)

## Extraction Strategy

### For Miners

Each candidate in the manifest has:
- `slug`: the filename for `catalog/mappings/{slug}.md`
- `name`: the ALL-CAPS metaphor name (Lakoff convention)
- `kind`: `conceptual-metaphor`, `dead-metaphor`, or `paradigm`
- `source_frame` and `target_frame`: existing or needed frames
- `mwlb_chapters`: which chapters of MWLB discuss this metaphor
- `archive_file`: if `source: "archive"`, the Osaka HTML filename to fetch
  for expressions and structural detail
- `description`: brief note on what makes this entry distinctive

**Miner workflow:**

1. If `archive_file` is present, fetch
   `https://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/metaphors/{archive_file}`
   to get source/target domains and example expressions
2. Use MWLB chapter references to write the Origin Story section
3. Cross-reference related entries in the manifest (e.g., the LOVE cluster,
   the IDEAS cluster, the orientational cluster)
4. Set `related:` to link within clusters and to existing catalog entries

### Batching Recommendation

Process in thematic clusters rather than alphabetically:

- **Batch 1 -- Orientational (10):** happy-is-up, more-is-up, good-is-up,
  rational-is-up, conscious-is-up, status-is-up, health-is-up, virtue-is-up,
  having-control-is-up, unknown-is-up. These share a pattern and can reuse
  the same frame analysis.
- **Batch 2 -- Ideas cluster (8):** ideas-are-people, ideas-are-plants,
  ideas-are-products, ideas-are-commodities, ideas-are-money,
  ideas-are-cutting-instruments, ideas-are-fashions, ideas-are-light-sources.
  All from Ch 10.
- **Batch 3 -- Love cluster (5):** love-is-madness, love-is-war,
  love-is-a-physical-force, love-is-a-unity,
  love-is-a-collaborative-work-of-art, love-is-a-patient
- **Batch 4 -- Ontological (8):** the-mind-is-a-machine,
  the-mind-is-a-brittle-object, inflation-is-an-entity,
  the-visual-field-is-a-container, emotions-are-entities-within-a-person,
  activities-are-containers, life-is-a-container, properties-are-possessions
- **Batch 5 -- Event structure (10):** the-conduit-metaphor,
  communication-is-sending, ideas-are-objects, ideas-are-resources,
  action-is-motion, change-is-motion, states-are-locations,
  purposes-are-destinations, difficulties-are-impediments-to-motion,
  causation
- **Batch 6 -- Remaining structural (10):** life-is-a-journey,
  life-is-a-gambling-game, argument-is-a-journey, argument-is-a-building,
  time-is-a-moving-object, time-is-stationary-and-we-move-through-it,
  time-is-a-limited-resource, labor-is-a-resource, seeing-is-touching,
  significant-is-big
- **Batch 7 -- Miscellaneous (6):** people-are-machines,
  emotional-stability-is-balance, existence-is-a-location,
  obligations-are-forces, psychological-forces-are-physical-forces,
  an-instrument-is-a-companion, foreseeable-future-is-up, finished-is-up,
  problems-are-puzzles, longterm-purposeful-change-is-a-journey,
  the-visual-field-is-a-bounded-region

## Schema Mapping

### Kind Assignment

| Category | Kind | Count | Criteria |
|----------|------|-------|----------|
| Structural | `conceptual-metaphor` | ~42 | Complex source-target mapping |
| Orientational | `dead-metaphor` | ~10 | Spatial orientation, deeply embedded |
| Paradigm | `paradigm` | 1 | The conduit metaphor (a system of metaphors) |

Orientational metaphors are classified as `dead-metaphor` because they are
so deeply embedded in language that speakers rarely recognize them as
metaphorical. "Happy is up" is not experienced as a metaphor the way
"Argument is war" is.

### Frame Inventory

**Existing reusable frames (in catalog):**
- `war`, `argumentation`, `economics`, `journeys`, `food-and-cooking`,
  `vision`, `architecture-and-building`, `containers`, `embodied-experience`,
  `collaborative-work`, `competition`, `manufacturing`, `social-roles`,
  `social-behavior`, `intellectual-inquiry`, `horticulture`,
  `love-and-relationships`, `time-and-temporality`

**New frames potentially needed:**
- `spatial-orientation` -- for the orientational metaphor cluster
- `mental-processes` -- for mind/cognition target domain
- `communication` -- for conduit metaphor system
- `physical-forces` -- for force-dynamic source domain
- `causation` -- for causal metaphors

### Categories

All entries get `cognitive-linguistics` as primary category. Additional:
- Orientational metaphors: `embodied-cognition`
- Love cluster: `social-dynamics`
- Event structure: `philosophy`

## Gotchas

1. **Entailment chains:** TIME IS MONEY entails TIME IS A LIMITED RESOURCE
   entails TIME IS A VALUABLE COMMODITY. These are separate entries in the
   Osaka archive but L&J treat them as a single system. Miners should
   document the entailment relationships in the body text and use `related:`
   links.

2. **Naming conventions:** The Osaka archive uses long descriptive names
   (e.g., "Longterm_Purposeful_Activity_Is_A_Journey") while MWLB uses
   shorter names (e.g., "LIFE IS A JOURNEY"). The manifest uses MWLB-style
   names. Miners should note both conventions.

3. **Orientational metaphors come in pairs:** HAPPY IS UP / SAD IS DOWN,
   GOOD IS UP / BAD IS DOWN. L&J always discuss both poles. The manifest
   lists the positive pole as the primary entry with the negative pole in
   the name (e.g., "HAPPY IS UP; SAD IS DOWN"). Miners should cover both
   poles in a single entry.

4. **Chapter 10 density:** "Some Further Examples" is the longest chapter
   and introduces ~15 new metaphors rapidly. Miners should not rush these --
   each deserves the same depth as the Ch 1-3 examples.

5. **The Afterword (2003):** The 2003 edition includes a new Afterword by
   the authors reflecting on 23 years of developments. It introduces some
   refinements but no new metaphors. Miners may reference it for context.

6. **Metonymy is excluded:** Chapter 8 discusses metonymy (FACE FOR PERSON,
   PRODUCER FOR PRODUCT, etc.). These are NOT conceptual metaphors and are
   excluded from the manifest.

7. **ARGUMENT IS DANCE:** L&J introduce this as a thought experiment, not
   as a live metaphor. It's already in the catalog as a seed entry.

8. **Osaka archive availability:** The archive has been stable for 20+
   years but has no HTTPS. Scripts should handle connection failures
   gracefully. The archive is read-only and static.

9. **LLM-sourced entries (27 of 63):** The orientational metaphors and
   several Ch 10 entries don't have exact Osaka archive matches. These were
   identified from multiple independent summaries but should be verified
   against the actual book text. The Surveyor should cross-check these.

10. **Already-mined entries:** 7 entries from the previous (rejected)
    prospecting run were already merged into the catalog. These are excluded
    from this manifest. The Miner should link new entries to them via
    `related:`.
