---
project_issue: 1352
repo: metaphorex/metaphorex
source_type: corpus
status: draft
---

# Playbook: Ecological Metaphors

## Source Description

Ecological concepts that have become load-bearing metaphors in other domains:
business, politics, technology, social systems, and policy. This is not a
single book but a corpus of ecological terms that have migrated beyond their
original discipline, carrying structural assumptions with them.

The project draws on ecology's unusually strong meta-literature about its own
metaphors. Ecologists have been self-conscious about metaphor since at least
Clements vs. Gleason (1920s succession debate), and the field has produced
sustained scholarly critique of how its language shapes reasoning -- from
Cuddington on "balance of nature" to Larson on militarized invasion biology
to the Resilience Alliance's work on adaptive cycles.

**Key academic sources:**

- Brendon Larson, *Metaphors for Environmental Sustainability* (Yale UP, 2011)
- Andrew Reynolds, *Understanding Metaphors in the Life Sciences* (Cambridge UP, 2022)
- Olson et al., "A User's Guide to Metaphors in Ecology and Evolution,"
  *Trends in Ecology & Evolution* 34:9 (2019)
- Kim Cuddington, "The 'Balance of Nature' Metaphor and Equilibrium in
  Population Ecology," *Biology & Philosophy* 16 (2001)
- C.S. Holling, "Resilience and Stability of Ecological Systems," *Annual
  Review of Ecology and Systematics* 4 (1973)
- Gunderson & Holling, *Panarchy* (Island Press, 2002)
- James F. Moore, "Predators and Prey: A New Ecology of Competition,"
  *Harvard Business Review* (1993)

## Access Method

### Primary: Wikipedia Ecology Glossaries (structured, scrapable)

- **Glossary of ecology:** https://en.wikipedia.org/wiki/Glossary_of_ecology
- **Outline of ecology:** https://en.wikipedia.org/wiki/Outline_of_ecology
- **Category: Ecology terminology:** https://en.wikipedia.org/wiki/Category:Ecology_terminology

These provide canonical definitions and are useful for verifying that
candidates are real ecological concepts (not invented by metaphor users).
However, Wikipedia does not track metaphorical migration -- it defines the
ecological concept, not its use as metaphor.

The scraping script (`scripts/scrape_wiki_ecology.py`) fetches the Glossary
of Ecology and verifies each manifest candidate against it. 18 of 29
candidates appear directly in the glossary. The remaining 11 are either
specialized resilience-theory terms (with their own Wikipedia articles) or
LLM-sourced candidates.

### Secondary: Academic meta-literature on ecological metaphors

- **Olson et al. (2019):** https://www.kokkonuts.org/wp-content/uploads/Olson-et-al.-2019.pdf
  Table 1 lists ecological metaphors with diagnostics for when they mislead.
  Covers: adaptive landscape, biological invasion, ecological niche, food web,
  tipping point, and others.

- **Cuddington (2001):** https://link.springer.com/article/10.1023/A:1011910014900
  Detailed analysis of "balance of nature" as a foundational metaphor that
  constrains equilibrium thinking.

- **Resilience Alliance:** https://www.resalliance.org/adaptive-cycle and
  https://www.resalliance.org/panarchy
  Canonical definitions of adaptive cycle and panarchy with diagrams.

- **Larson (2005):** https://esajournals.onlinelibrary.wiley.com/doi/10.1890/1540-9295(2005)003%5B0495:TWOTRD%5D2.0.CO;2
  "The War of the Roses: Demilitarizing Invasion Biology" -- critique of
  militarized language in ecology.

### Methodology

Unlike book-based projects (Lakoff-Johnson, Munger), this project has no
single canonical source to scrape. The candidate list was assembled by:

1. Starting with the issue's named examples (keystone species, tragedy of
   the commons, tipping points, adaptive cycle, balance of nature)
2. Cross-referencing Wikipedia's Glossary of Ecology to verify each candidate
   is a real ecological concept with a standard definition
3. Consulting Olson et al. (2019) and Larson (2011) for the academic
   inventory of ecology's most-studied metaphors
4. Identifying additional ecological concepts that have demonstrable
   metaphorical migration to other domains (business ecosystem, food chain
   hierarchy, pioneer species as first-mover, etc.)
5. Flagging LLM-sourced candidates (5 of 29) that lack direct citation in
   the archive sources

### Already in Catalog (3 entries -- cross-reference, do not duplicate)

- `the-commons` -- covers tragedy of the commons and Ostrom's governance
- `system-resilience-vs-fragility` -- covers Holling resilience from the
  Munger/Taleb angle
- `niche-specialization` -- covers ecological niche as Munger mental model

New entries should use `related:` links to these existing entries. The
ecological-niche and ecological-resilience candidates are distinct from their
existing counterparts because they focus on the metaphor's ecological origins
and migration critique rather than treating them as generic mental models.

## Extraction Strategy

### For Miners

Each candidate in the manifest has:
- `slug`: the filename for `catalog/entries/{slug}.md`
- `name`: human-readable name
- `kind`: metaphor, paradigm, or mental-model
- `source_frame`: always `ecology`
- `target_frame`: the primary domain the metaphor migrated to
- `categories`: always includes `biology-and-ecology`
- `source`: `archive` (24) or `llm` (5) -- indicates provenance
- `description`: brief note on what makes this entry distinctive

**Miner workflow:**

1. For each candidate, consult the Wikipedia article on the ecological
   concept to get the canonical ecological definition (origin, discoverer,
   mechanism)
2. Use the `description` field to identify the metaphorical migration:
   what domains adopted this concept, and what structural assumptions did
   it carry?
3. For `source: "archive"` entries, cross-reference the academic sources
   listed above for scholarly analysis of how the metaphor shapes reasoning
4. Write Transfers that explain what structural mappings the ecological
   concept imports into the target domain
5. Write Limits that explain where the mapping breaks -- ecological systems
   differ from social/economic/technological systems in specific ways
6. Write Expressions with real-world usage examples
7. Set `source_frame: ecology` and use appropriate frames for target_frame
8. Cross-link with `related:` to other entries in this project and to the
   existing catalog entries (the-commons, system-resilience-vs-fragility,
   niche-specialization)

**Key thematic clusters to preserve in related links:**

- **Trophic cluster:** food-chain, apex-predator, trophic-cascade,
  ecological-arms-race
- **Succession cluster:** ecological-succession, pioneer-species,
  old-growth-vs-clear-cut
- **Resilience cluster:** ecological-resilience, adaptive-cycle, panarchy,
  regime-shift, tipping-point, balance-of-nature
- **Inter-species relations:** symbiosis-as-metaphor, mutualism-as-metaphor,
  parasitism-as-metaphor, invasive-species-as-metaphor, ecological-arms-race
- **Ecosystem structure:** ecosystem-as-metaphor, keystone-species,
  ecological-niche, indicator-species, monoculture, edge-effect
- **Accounting metaphors:** ecological-footprint, natural-capital,
  carrying-capacity

### Batching Recommendation

Process in thematic clusters:

- **Batch 1 -- Core concepts (5):** keystone-species, tipping-point,
  ecosystem-as-metaphor, carrying-capacity, balance-of-nature
- **Batch 2 -- Trophic and predation (4):** food-chain, apex-predator,
  trophic-cascade, ecological-arms-race
- **Batch 3 -- Succession and disturbance (3):** ecological-succession,
  pioneer-species, old-growth-vs-clear-cut
- **Batch 4 -- Resilience theory (4):** ecological-resilience, adaptive-cycle,
  panarchy, regime-shift
- **Batch 5 -- Inter-species relations (4):** symbiosis-as-metaphor,
  mutualism-as-metaphor, parasitism-as-metaphor, invasive-species-as-metaphor
- **Batch 6 -- Structure and measurement (5):** ecological-niche, monoculture,
  indicator-species, edge-effect, dead-zone
- **Batch 7 -- Accounting and value (4):** ecological-footprint,
  natural-capital, seed-and-soil, pollinator-as-metaphor

## Schema Mapping

### Kind Assignment

| Category | Kind | Count | Criteria |
|----------|------|-------|----------|
| Conceptual metaphors | `metaphor` | 24 | Ecological concept with active source-target mapping in other domains |
| Paradigms | `paradigm` | 2 | balance-of-nature, panarchy -- systems of metaphors that structure entire worldviews |
| Mental models | `mental-model` | 3 | adaptive-cycle -- used as explicit analytical framework |

### Frame Inventory

**Existing reusable frames:**
- `biology` (exists, but ecology-specific entries need an ecology frame)
- `economics`, `organizational-behavior`, `social-dynamics`,
  `systems-thinking`, `competition`, `philosophy`

**New frames needed:**
- `ecology` -- the primary source frame for all entries. Roles: species,
  population, community, ecosystem, habitat, niche, trophic-level,
  disturbance, succession, resilience, carrying-capacity, food-web

**Target frames (existing):**
- `economics` (for carrying-capacity, natural-capital, ecological-footprint,
  ecosystem-as-metaphor, pioneer-species, apex-predator, ecological-niche,
  dead-zone)
- `organizational-behavior` (for keystone-species, ecosystem-as-metaphor,
  symbiosis, mutualism, monoculture, edge-effect, pollinator, old-growth,
  adaptive-cycle, ecological-succession)
- `social-dynamics` (for tipping-point, invasive-species, parasitism,
  food-chain)
- `systems-thinking` (for trophic-cascade, indicator-species, regime-shift,
  panarchy, ecological-resilience)
- `competition` (for ecological-arms-race)
- `philosophy` (for balance-of-nature)
- `health-and-medicine` (for seed-and-soil)

### Categories

All entries get `biology-and-ecology` as primary category. Additional
categories per cluster:
- Resilience cluster: `systems-thinking`
- Inter-species relations: `social-dynamics` or `organizational-behavior`
- Accounting metaphors: `economics-and-finance`
- Balance of nature: `philosophy`

## Gotchas

1. **Overlap with existing entries.** Three catalog entries already cover
   ecological concepts from non-ecological angles (the-commons,
   system-resilience-vs-fragility, niche-specialization). New entries must
   be distinct: focus on the ecological origins and the metaphor's migration
   history, not on the target-domain application. Use `related:` links
   generously.

2. **The ecology frame does not exist yet.** Miners will need to create
   `catalog/frames/ecology.md` with the first PR. All 29 entries use
   `source_frame: ecology`.

3. **"Ecosystem" is both a metaphor and a literal term.** The
   ecosystem-as-metaphor entry must distinguish between the ecological
   concept (Tansley 1935) and its metaphorical use in business/tech.
   The entry is about the metaphorical migration, not the ecology.

4. **Invasion biology is politically sensitive.** The invasive-species entry
   must handle the xenophobia critique carefully. Present both sides: the
   ecological concern is real (invasive species cause genuine damage), AND
   the military/nativist language carries real social freight. Do not
   editorialize.

5. **LLM-sourced candidates (5 of 29).** These are: dead-zone,
   natural-capital, seed-and-soil, pollinator-as-metaphor,
   old-growth-vs-clear-cut. They are real ecological concepts with real
   metaphorical use, but their selection was not driven by an archive source.
   The Surveyor should verify these are worth including.

6. **Ecological resilience vs. existing resilience entry.** The catalog has
   `system-resilience-vs-fragility` from the Munger project. The new
   `ecological-resilience` entry must focus on Holling's specific ecological
   distinction (engineering resilience vs. ecological resilience) and its
   migration to organizational theory, not re-cover the Taleb/Munger ground.

7. **The "balance of nature" is a paradigm, not a single metaphor.** It is
   a system of assumptions (equilibrium, harmony, self-regulation) that
   structures how people think about ecosystems. Kind should be `paradigm`.

8. **Candidate count (29) is within GitHub sub-issue limits.** No overflow
   handling needed.
