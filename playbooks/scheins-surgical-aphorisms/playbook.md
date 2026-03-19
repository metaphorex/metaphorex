---
project_issue: 1229
repo: metaphorex/metaphorex
source_type: book
status: draft
---

# Playbook: Schein's Surgical Aphorisms -- Medical Wisdom as Metaphor

## Source Description

This project draws on the surgical and medical aphorism tradition to
extract conceptual metaphors that have genuine cross-domain transfer
beyond medicine. The primary source is Moshe Schein's *Aphorisms &
Quotations for the Surgeon* (tfm Publishing, 2003; ~1,500 items across
94 chapters), supplemented by:

- William Bean (ed.), *Sir William Osler: Aphorisms from His Bedside
  Teachings and Writings* (Henry Schuman, 1950; ~280 sayings)
- Samuel Shem, *The House of God* (1978; 13 numbered Laws)
- The Mayo Brothers (William J. and Charles H. Mayo) aphorism tradition
- Traditional surgical folklore (unattributed sayings passed down in
  residency training)
- Merrell & McGreevy, "Surgical Aphorisms" (West J Med, 1991)
- Campbell, "Surgical aphorisms" (BJS, 2013)

The combined source pool is ~2,100+ items. However, the vast majority
are domain-specific clinical advice. The issue's selectivity guidance is
clear: import only aphorisms that encode reasoning patterns that transfer
beyond medicine.

**Estimated yield: 22 entries.**

### What Makes This Source Distinctive

Medical aphorisms are unusual in the metaphor landscape because:

1. **Life-or-death stakes compress wisdom.** These are not armchair
   philosophies but decision heuristics tested under mortal pressure.
2. **Medicine is the original applied epistemology.** Diagnosis *is*
   reasoning under uncertainty. Triage *is* resource allocation. The
   metaphorical transfer is structural, not decorative.
3. **Many have already crossed over.** "Triage," "first do no harm,"
   "diagnosis," "vital signs," "second opinion," and "side effects" are
   dead metaphors in business and technology -- so deeply embedded that
   people forget they are medical.

## Access Method

### Primary Archive: House of God Laws (Wanderings.net)

**URL:** https://www.wanderings.net/notebook/Main/HouseOfGodLaws

All 13 Laws from Shem's novel. Scraping script verifies against this
page. 4 of 13 laws qualify for cross-domain extraction.

**Script:** `scripts/scrape_house_of_god.py` -- fetches page, verifies
law texts present, outputs qualifying laws as JSON.

### Secondary Archive: LITFL Oslerisms

**URL:** https://litfl.com/eponymictionary/oslerisms/

Curated selection of Osler quotations maintained by the Life in the Fast
Lane medical education site. Key quote verified: "We miss more by not
seeing than we do by not knowing."

### Tertiary Archive: Mayo Clinic Library Aphorisms Guide

**URL:** https://libraryguides.mayo.edu/historicalunit/aphorisms

Extensive collection of William J. Mayo and Charles H. Mayo quotations
(190+ items). 1 qualifying candidate extracted.

**Script:** `scripts/scrape_mayo_aphorisms.py` -- fetches page, verifies
Mayo content present, outputs qualifying aphorisms as JSON.

### PMC Archives (Academic Sources)

**URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC2760177/

"Facts and ideas from anywhere" -- extensive collection of surgical
quotations with attributions. Source for multiple candidates including
James Gregory's "Young men kill their patients; old men let them die"
and Theodor Kocher's "A good surgeon knows when not to operate."

**URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC1422679/

Book review of Schein's collection confirming 1,500+ items across 94
chapters. Quotes specific aphorisms including Judah Folkman's "We may
be wrong, but we are never in doubt."

### Wikipedia (Zebra Medicine)

**URL:** https://en.wikipedia.org/wiki/Zebra_(medicine)

Documents Theodore Woodward's "hoofbeats" aphorism with attribution
and historical context.

### No Structured Digital Archive Exists for Schein

Schein's book is copyrighted and not digitized in any open archive. The
PMC book review confirms 1,500+ items across 94 alphabetically-ordered
chapters but quotes only a handful. No table of contents or chapter
listing is publicly available online.

**Consequence:** Candidates sourced from Schein are tagged `"llm"` in the
manifest because they cannot be verified against a scraping script. The
archive-sourced candidates are tagged `"archive"` where the exact text
or attribution was found in the archive sources above.

### Surgical Folklore (Unattributed)

Many of the most potent surgical aphorisms circulate without clear
attribution. The BJS article by Campbell (2013) and the West J Med
article by Merrell & McGreevy (1991) document these as oral tradition.
Candidates from this tradition are tagged `"archive"` when attested in
at least one published academic source, `"llm"` otherwise.

## Extraction Strategy

### Selection Criteria

An aphorism qualifies for the manifest ONLY if it meets ALL of:

1. **Cross-domain transfer.** The saying must encode a reasoning pattern
   that has demonstrable use outside medicine. "NPO after midnight" does
   not qualify. "When you hear hoofbeats, think horses not zebras"
   encodes base-rate reasoning used in debugging, investing, and
   engineering.

2. **Structural mapping, not just analogy.** The metaphorical transfer
   must involve a source frame (medicine/surgery) mapping onto a target
   frame (decision-making, organizational behavior, epistemology, etc.)
   with specific structural correspondences.

3. **Active usage.** The concept must be currently used metaphorically
   in at least one non-medical domain. Historical curiosities that
   never left medicine are excluded.

### Source Attribution in Manifest

Each candidate has a `source` field:

- `"archive"` -- the aphorism text or attribution was verified in at least
  one of the archive URLs listed above. The `archive_ref` field specifies
  where.
- `"llm"` -- the aphorism is well-known but could not be verified against
  a scraping-accessible archive. These need extra scrutiny from the Surveyor.

**Breakdown:** 14 archive-sourced, 8 LLM-sourced.

### For Miners

Each candidate in the manifest has:
- `slug`: the filename for `catalog/entries/{slug}.md`
- `name`: human-readable name
- `kind`: `conceptual-metaphor`, `dead-metaphor`, or `paradigm`
- `source_frame`: the medical/surgical domain
- `target_frame`: the domain where the metaphor has migrated
- `categories`: primary categorization
- `source`: `"archive"` or `"llm"`
- `description`: what makes this interesting as a cross-domain mapping

**Miner workflow:**

1. For `source: "archive"` entries, fetch the archive URL listed and
   extract the original context
2. Research the medical origin: when was this concept first articulated,
   by whom, under what circumstances?
3. Document the cross-domain migration: how did this medical concept
   enter business/technology/everyday language? What structural parallels
   does the borrowing exploit?
4. **"Where It Breaks" is critical.** Medical metaphors often import
   false authority ("the diagnosis is...") or false precision ("vital
   signs show..."). The Miner must interrogate what the medical framing
   smuggles into the target domain.
5. Set `author: schein-surgical-aphorisms` as provenance
6. Set `related:` links to other entries from this project and to
   existing catalog entries where relevant

### Batching Recommendation

Process in thematic clusters:

- **Batch 1 -- Decision heuristics (6):** triage, differential-diagnosis,
  hoofbeats-think-horses, first-do-no-harm, second-opinion,
  treat-the-patient-not-the-test
- **Batch 2 -- Temporal wisdom (4):** all-bleeding-stops, tincture-of-time,
  never-let-the-sun-set-on-undrained-pus, a-chance-to-cut-is-a-chance-to-cure
- **Batch 3 -- Composure and judgment (6):** take-your-own-pulse,
  the-retrospectoscope, the-patient-is-the-one-with-the-disease,
  do-as-much-nothing-as-possible, young-doctors-kill-old-doctors-let-die,
  knowing-when-not-to-operate
- **Batch 4 -- Dead metaphors (4):** side-effects, vital-signs,
  prognosis-as-forecast, surgical-precision
- **Batch 5 -- Learning and expertise (2):** see-one-do-one-teach-one,
  if-you-dont-look-you-wont-find
- **Standalone:** the-cure-is-worse-than-the-disease

## Schema Mapping

### Kind Assignment

| Pattern | Kind | Criteria |
|---------|------|----------|
| Active aphorism with clear source-target structure | `conceptual-metaphor` | Clear structural mapping between medicine and another domain |
| Medical term so embedded it is no longer felt as metaphorical | `dead-metaphor` | "Triage," "diagnosis," "side effects" in business |
| Systematic framework | `paradigm` | None in this batch |

Most entries are `conceptual-metaphor` (16). Six are `dead-metaphor`
(triage, differential-diagnosis, second-opinion, side-effects,
vital-signs, prognosis-as-forecast, surgical-precision).

### Frame Inventory

**Existing reusable frames:**
- `medicine` -- source frame for all entries
- `decision-making` -- target for most entries
- `ethics-and-morality` -- target for first-do-no-harm
- `education` -- target for see-one-do-one-teach-one

**New frames potentially needed:**
- `surgery` -- more specific than `medicine` for operative aphorisms
  (a-chance-to-cut, surgical-precision, knowing-when-not-to-operate)

### Categories

Primary category for all entries: `health-and-medicine`.

Additional categories by cluster:
- Decision heuristics: `cognitive-science`
- Temporal wisdom: `philosophy`
- Composure/judgment: `psychology`
- Dead metaphors: `systems-thinking` or `organizational-behavior`
- Learning: `education-and-learning`

## Gotchas

1. **Copyright on Schein.** The book is copyrighted and not freely
   available online. Miners should not attempt to reproduce verbatim
   content from Schein. The aphorisms themselves are traditional sayings
   (not copyrightable), but Schein's commentary and selection are his
   intellectual property. Miners should cite Schein as a collector, not
   quote his prose.

2. **Attribution is fuzzy.** Many surgical aphorisms circulate without
   clear attribution. "All bleeding eventually stops" is variously
   attributed to multiple surgeons. Miners should note the attribution
   uncertainty in the Origin Story section rather than asserting false
   precision.

3. **Dead metaphors require extra work.** For entries like "triage" and
   "diagnosis," the metaphorical transfer happened so long ago that
   people do not experience these as metaphors. The Transfers section
   needs to defamiliarize the concept: explain why the medical origin
   matters and what structural baggage it carries into the target domain.

4. **"First do no harm" is misattributed.** Commonly attributed to
   Hippocrates, it does not appear in the Hippocratic corpus in that
   exact form. The Latin "primum non nocere" is of uncertain origin.
   Miners should address this in the Origin Story.

5. **Overlapping entries.** Some candidates overlap conceptually (e.g.,
   "triage" and "differential diagnosis" both involve prioritization;
   "tincture of time" and "do as much nothing as possible" both encode
   restraint). Use `related:` links to connect them rather than merging.

6. **The House of God is satire.** Shem's Laws are satirical and often
   dark. The ones included here (Law III, IV, X, XIII) have transcended
   their satirical origin to become genuine wisdom. Miners should
   acknowledge the satirical source while treating the cross-domain
   insight seriously.

7. **Candidate count is under 100.** No sub-issue cap concerns for
   this project (22 candidates).

8. **LLM-sourced entries need Surveyor scrutiny.** 8 of 22 candidates
   are tagged `"llm"` because they could not be verified against a
   publicly accessible structured archive. These are all well-known
   medical terms or aphorisms, but the Surveyor should verify their
   cross-domain transfer claims.
