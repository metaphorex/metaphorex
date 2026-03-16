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

The combined source pool is ~2,100+ items. However, the vast majority
are domain-specific clinical advice. The issue's selectivity guidance is
clear: import only aphorisms that encode reasoning patterns that transfer
beyond medicine.

**Estimated yield: 20-25 mappings.**

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

### Primary Archive: Internet Archive -- Osler Aphorisms (full text)

**URL:** https://archive.org/stream/in.ernet.dli.2015.63933/2015.63933.Osler-Aphorisms-From-His-Bedside-Teachings-And-Writings_djvu.txt

Full OCR text of Bean's 1950 edition of Osler's aphorisms, organized
into sections: The Medical Student, The Ethos, The Patient, The Great
Republic of Medicine, Epitomes. Free access, no authentication required.

### Secondary Archive: LITFL Oslerisms

**URL:** https://litfl.com/eponymictionary/oslerisms/

Curated selection of Osler quotations maintained by the Life in the Fast
Lane medical education site. 27+ aphorisms with context.

### Tertiary Archive: Mayo Clinic Library Aphorisms Guide

**URL:** https://libraryguides.mayo.edu/historicalunit/aphorisms

Extensive collection of William J. Mayo and Charles H. Mayo quotations
(190+ items), organized by speaker.

### House of God Laws

**URL:** https://litfl.com/house-of-god/

The 13 Laws from Shem's novel, widely known in medical culture.

### No Structured Digital Archive Exists for Schein

Schein's book is copyrighted and not digitized in any open archive. The
PMC book review (https://pmc.ncbi.nlm.nih.gov/articles/PMC1422679/)
confirms 1,500+ items across 94 alphabetically-ordered chapters but
quotes only a handful. No table of contents or chapter listing is
publicly available online.

**Consequence:** Candidates sourced from Schein are tagged `"llm"` in the
manifest because they cannot be verified against a scraping script. The
Osler, Mayo, and House of God candidates are tagged `"archive"` where
the exact text was found in the archive sources above.

### Surgical Folklore (Unattributed)

Many of the most potent surgical aphorisms circulate without clear
attribution. The BJS article by Campbell (2013) and the West J Med
article by Merrell & McGreevy (1991) document these as oral tradition.
Candidates from this tradition are tagged `"llm"` but are well-attested
in multiple independent sources.

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

### For Miners

Each candidate in the manifest has:
- `slug`: the filename for `catalog/mappings/{slug}.md`
- `name`: human-readable name
- `kind`: `conceptual-metaphor`, `dead-metaphor`, or `paradigm`
- `source_frame`: the medical/surgical domain
- `target_frame`: the domain where the metaphor has migrated
- `categories`: primary categorization
- `aphorism_text`: the canonical form of the saying (where applicable)
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
- **Batch 2 -- Temporal wisdom (4):** all-bleeding-stops, the-tincture-
  of-time, never-let-the-sun-set-on-undrained-pus, a-chance-to-cut-is-a-
  chance-to-cure
- **Batch 3 -- Composure and judgment (5):** take-your-own-pulse,
  the-enemy-of-good-is-better, the-retrospectoscope,
  experience-is-the-great-teacher, we-may-be-wrong-but-never-in-doubt
- **Batch 4 -- Systemic/organizational (5):** side-effects,
  vital-signs, prognosis-as-forecast, surgical-precision,
  see-one-do-one-teach-one

## Schema Mapping

### Kind Assignment

| Pattern | Kind | Criteria |
|---------|------|----------|
| Active aphorism with clear source-target structure | `conceptual-metaphor` | Clear structural mapping between medicine and another domain |
| Medical term so embedded it is no longer felt as metaphorical | `dead-metaphor` | "Triage," "diagnosis," "side effects" in business |
| Systematic framework | `paradigm` | Triage as a complete decision system |

Most entries will be `conceptual-metaphor`. A few high-frequency dead
metaphors (triage, diagnosis, vital signs) are `dead-metaphor`.

### Frame Inventory

**Existing reusable frames:**
- `medicine` -- source frame for most entries
- `decision-making` -- target for diagnostic/triage metaphors
- `social-behavior` -- target for organizational metaphors
- `time-and-temporality` -- target for temporal aphorisms
- `ethics-and-morality` -- target for "first do no harm"
- `education` -- target for "see one, do one, teach one"

**New frames potentially needed:**
- `surgery` -- more specific than `medicine` for operative aphorisms
- `organizational-management` -- target for management metaphors
- `epistemology` -- target for reasoning-under-uncertainty metaphors

### Categories

Primary category for all entries: `health-and-medicine`.

Additional categories by cluster:
- Decision heuristics: `cognitive-science`
- Temporal wisdom: `philosophy`
- Composure/judgment: `psychology`
- Systemic: `organizational-behavior`

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
   people do not experience these as metaphors. The "What It Brings"
   section needs to defamiliarize the concept: explain why the medical
   origin matters and what structural baggage it carries into the
   target domain.

4. **"First do no harm" is misattributed.** Commonly attributed to
   Hippocrates, it does not appear in the Hippocratic corpus in that
   exact form. The Latin "primum non nocere" is of uncertain origin.
   Miners should address this in the Origin Story.

5. **Overlapping entries.** Some candidates overlap conceptually (e.g.,
   "triage" and "differential diagnosis" both involve prioritization).
   Use `related:` links to connect them rather than merging.

6. **The House of God is satire.** Shem's Laws are satirical and often
   dark. The ones included here (Law III: "take your own pulse"; Law
   XIII: "do as much nothing as possible") have transcended their
   satirical origin to become genuine wisdom. Miners should acknowledge
   the satirical source while treating the cross-domain insight
   seriously.

7. **Candidate count is under 100.** No sub-issue cap concerns for
   this project.
