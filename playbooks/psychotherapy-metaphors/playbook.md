---
project_issue: 1353
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Psychotherapy Metaphors -- Extraction Playbook

## Source Description

Psychotherapy is a rich source of metaphors that have migrated far beyond
the clinical setting. This project covers four major traditions:

1. **ACT (Acceptance and Commitment Therapy)** -- Hayes, Harris, Torneke.
   ACT is unusual in that it uses named metaphor-interventions as clinical
   tools. "Passengers on the Bus," "Quicksand," and "Tug of War with a
   Monster" are prescribed exercises, not incidental language.

2. **Narrative Therapy** -- Michael White, David Epston. Core techniques
   (externalization, re-authoring, unique outcomes) are themselves
   metaphorical operations on the client's life story.

3. **Person-Centered / Humanistic** -- Carl Rogers. Concepts like
   unconditional positive regard and the therapeutic alliance have become
   management and coaching vocabulary.

4. **Psychodynamic / Somatic** -- Freud, Jung, Bion, Kohut, Levine,
   Gendlin, van der Kolk. Concepts like transference, defense mechanisms,
   shadow work, window of tolerance, and "the body keeps the score" have
   become everyday language.

## Access Method

### Primary Archives (ACT metaphors)

- **ACBS Metaphors Page**: https://contextualscience.org/metaphors
  Community-contributed collection of 40+ named ACT metaphors with
  descriptions. Scrapeable HTML page. Sourced 10 candidates.

- **Contextual Consulting A-Z**: https://contextualconsulting.co.uk/therapy-approaches/a-z-of-act-metaphors
  Alphabetical listing of 26 ACT metaphors (A-Z format) with process
  mappings. Clean HTML, easy to parse. Sourced 8 candidates.

- **Compendium of ACT Metaphors (PDF)**: https://coping.us/images/Compendium_of_ACT_Metaphors.pdf
  PDF document cataloging ACT metaphors by process. Requires PDF text
  extraction. Content verified against web sources (largely overlapping).

### Secondary Sources (Narrative Therapy)

- **Dulwich Centre**: https://dulwichcentre.com.au/articles-about-narrative-therapy/externalising/
  Michael White's home institution. Articles on externalization and
  narrative therapy practices. Sourced 5 candidates.

### Tertiary Sources (Psychodynamic, Somatic, Humanistic)

Each psychodynamic/somatic/humanistic candidate is now backed by at least
one archive URL. The following structured sources were used:

- **Wikipedia articles** (structured, stable, well-cited):
  - [Therapeutic alliance](https://en.wikipedia.org/wiki/Therapeutic_alliance)
  - [Defence mechanism](https://en.wikipedia.org/wiki/Defence_mechanism)
  - [Transference](https://en.wikipedia.org/wiki/Transference)
  - [Shadow (psychology)](https://en.wikipedia.org/wiki/Shadow_(psychology))
  - [Inner child](https://en.wikipedia.org/wiki/Inner_child)
  - [The Body Keeps the Score](https://en.wikipedia.org/wiki/The_Body_Keeps_the_Score)
  - [Somatic experiencing](https://en.wikipedia.org/wiki/Somatic_experiencing) (pendulation, titration)
  - [Focusing (psychotherapy)](https://en.wikipedia.org/wiki/Focusing_(psychotherapy)) (felt sense)
  - [Unconditional positive regard](https://en.wikipedia.org/wiki/Unconditional_positive_regard)
  - [Working through](https://en.wikipedia.org/wiki/Working_through)
  - [Holding space](https://en.wikipedia.org/wiki/Holding_space)
  - [Zone of proximal development](https://en.wikipedia.org/wiki/Zone_of_proximal_development) (scaffolding)
  - [Self psychology](https://en.wikipedia.org/wiki/Self_psychology) (mirroring)

- **PubMed Central / academic PDFs**:
  - [Safran rupture-and-repair contributions](https://pmc.ncbi.nlm.nih.gov/articles/PMC7451308/)
  - [Somatic experiencing interoception study](https://pmc.ncbi.nlm.nih.gov/articles/PMC4316402/)
  - [Therapeutic alliance history](https://pmc.ncbi.nlm.nih.gov/articles/PMC3198542/)
  - [Bion container-contained PDF](https://www.cpor.org/otc/Bion(1985)ContainerAndContained.pdf)

- **Clinical reference pages**:
  - [Psychology Tools: Window of Tolerance](https://www.psychologytools.com/resource/window-of-tolerance)
  - [GoodTherapy: Presenting Problem](https://www.goodtherapy.org/blog/psychpedia/presenting-problem)
  - [Blatner's Psychotherapy Metaphors](https://www.blatner.com/adam/level2/metaphors.htm)

### Scraping Script

`scripts/scrape_acbs_metaphors.py` -- Fetches the ACBS and Contextual
Consulting pages and extracts metaphor names. Requires `requests` and
`beautifulsoup4`. Run with `uv run`.

Note: The PDF sources (Compendium, VA MIRECC) are binary PDFs that resist
simple text extraction. The scraping script covers the HTML sources; PDF
content was manually verified against the web sources and found to be
largely overlapping.

## Extraction Strategy

### Candidate Selection Criteria

A psychotherapy concept qualifies as a metaphorex candidate if:

1. It has a **named metaphorical structure** (not just a technique name)
2. It has **migrated beyond clinical use** into coaching, management, UX,
   self-help, or everyday language
3. It has a **source frame** that is not psychotherapy itself (i.e., it
   borrows structure from another domain)

### Entry Types

- **metaphor** (kind): Named metaphor-interventions from ACT, and
  psychodynamic/somatic concepts with clear source-target structure
  (e.g., "defense mechanisms" borrows from military, "transference"
  borrows from spatial motion)
- **pattern** (kind): Narrative therapy techniques that are procedural
  patterns rather than single-mapping metaphors (externalization,
  re-authoring, unique outcomes)
- **mental-model** (kind): Frameworks that function as lenses rather than
  metaphorical mappings (clean vs dirty pain, choice point, unconditional
  positive regard, felt sense)

### Extraction Per Entry

For each candidate, the Miner should:

1. Identify the **source frame** -- what domain does the metaphor borrow
   from? (e.g., passengers-on-the-bus borrows from transportation)
2. Write **Transfers** covering: the original clinical usage, the
   structural mapping, and documented migration to other domains
3. Write **Limits** covering: where the metaphor breaks down, what it
   hides, clinical misuse risks, and oversimplification when used outside
   therapy
4. Write **Expressions** covering: clinical phrasing, pop-psychology
   adaptations, and colloquial usage outside therapy

## Schema Mapping

| Manifest field    | Entry frontmatter field |
|-------------------|------------------------|
| slug              | slug                   |
| name              | name                   |
| kind              | kind                   |
| source_frame      | source_frame           |
| target_frame      | (not in schema -- use applies_to instead) |
| categories        | categories             |

Additional frontmatter fields to set:

- `author`: `agent:metaphorex-miner`
- `provenance`: `psychotherapy-metaphors`
- `applies_to`: derive from target_frame; most will be `[psychotherapy]`
  but some have migrated (holding-space -> `[coaching, management]`)
- `grounding`: `established` for well-documented ACT interventions with
  RCT evidence; `folk` for concepts that have migrated into pop usage
  without rigorous cross-domain validation

### Frame Creation

The following new frames will likely be needed:

- `psychotherapy` -- the target frame for most entries
- `games-and-play` -- source frame for chessboard, tug-of-war, finger-trap
- `meteorology` -- source frame for sky-and-weather
- `mythology-and-folklore` -- source frame for demons-on-the-boat
- `theater-and-performance` -- source frame for presenting-problem
- `optics-and-reflection` -- source frame for mirroring
- `explosives-and-ordnance` -- source frame for cognitive-defusion
- `manual-labor` -- source frame for working-through
- `family-and-kinship` -- source frame for inner-child
- `light-and-darkness` -- source frame for shadow-work
- `body-and-embodiment` -- source frame for felt-sense, hands-as-thoughts
- `art-and-creation` -- source frame for creative-hopelessness
- `cleanliness` -- source frame for clean-pain-vs-dirty-pain
- `spatial-motion` -- source frame for transference

Check existing frames before creating; some may already exist (e.g.,
`containers`, `navigation`, `war`, `architecture-and-building`,
`economics`, `chemistry`, `accounting`).

## Gotchas

1. **ACT metaphors vs exercises**: Some ACT "metaphors" are actually
   experiential exercises (hands-as-thoughts, leaves-on-a-stream). They
   have metaphorical structure but the entry should acknowledge the
   embodied/performative dimension, not just the conceptual mapping.

2. **Overlap with existing entries**: Check whether `psychological-forces-are-physical-forces`
   or related existing entries cover ground that defense-mechanisms or
   shadow-work would cover. The Miner should differentiate or
   cross-reference.

3. **Scaffolding slug collision**: The existing `catalog/entries/scaffolding.md`
   covers the educational/Vygotskian concept from child-psychology-metaphors.
   This project's candidate uses slug `scaffolding-in-therapy` to distinguish
   the therapeutic application. The Miner should cross-reference the existing
   entry in the `related` field.

4. **Source attribution**: ACT metaphors have clear attributions (Hayes,
   Harris, Torneke). Psychodynamic concepts have longer genealogies
   (Freud -> Anna Freud -> defense mechanisms taxonomy). Narrative therapy
   concepts trace to White and Epston. Origin Story sections should be
   precise about who coined what.

5. **Clinical sensitivity**: These are active therapeutic tools. Entries
   should treat them with respect -- not as quaint folk metaphors but as
   carefully designed clinical instruments with evidence bases.

6. **Migration tracking**: The most interesting candidates are ones that
   have migrated OUT of therapy (holding space -> management, inner child
   -> self-help, window of tolerance -> education, defense mechanisms ->
   everyday language). The Miner should track these migrations explicitly.

7. **Same-domain mapping avoidance**: Several candidates initially appeared
   to have source_frame=psychotherapy (same as target). This has been
   resolved: clean-pain-vs-dirty-pain uses source_frame=cleanliness,
   creative-hopelessness uses art-and-creation, unconditional-positive-regard
   uses economics, transference uses spatial-motion. The Miner should
   preserve these cross-domain mappings.

8. **Candidate count (43)**: Below the 100 sub-issue cap, so no overflow
   handling is needed.
