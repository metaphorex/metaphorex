---
project_issue: 642
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Playbook: Charlie Munger's Mental Models

## Source Description

Charlie Munger (1924-2023), vice chairman of Berkshire Hathaway, advocated
building a "latticework of mental models" drawn from multiple disciplines
for better decision-making. His key articulations appear in:

- **Poor Charlie's Almanack** (ed. Peter Kaufman, 2005/2023 Stripe Press
  edition) -- collected speeches and talks, especially "The Psychology of
  Human Misjudgment" (25 standard causes) and "A Lesson on Elementary
  Worldly Wisdom" (the latticework concept)
- **Seeking Wisdom: From Darwin to Munger** by Peter Bevelin (2007) --
  third-party synthesis of Munger's models organized by discipline
- Berkshire Hathaway annual meeting transcripts (1986-2023)

Munger never published a canonical numbered list. The ~100 models he
referenced come from many talks across decades. Several compilations exist
online that aggregate these into structured lists.

### What Makes This Different from Other Import Projects

Most Metaphorex import projects deal with metaphors or patterns that have
clear "X IS Y" structure. Munger's mental models are different: many are
cross-domain reasoning frameworks where a concept from one discipline
(physics, biology, economics) is applied as an analytical lens in another
domain (investing, business strategy, life decisions). Some are genuine
metaphors (Man with a Hammer, Cancer Surgery Formula). Others are formal
models (Bayesian Updating, Power Laws) that become metaphorical when applied
outside their native discipline.

The selection criteria for this manifest: models that have clear structural
mappings (source domain -> target domain) where one discipline's reasoning
patterns illuminate another. Pure heuristics without metaphorical structure
(e.g., "Basic Arithmetic Fluency") are excluded.

## Access Method

### Primary Archive: Sources of Insight (129 models)

**URL:** https://sourcesofinsight.com/charlie-munger-mental-models/

The most comprehensive structured compilation found. Lists 129 models
organized into 8 categories:

1. Psychology: Tendencies & Biases (34)
2. Thinking Tools & Meta-Frameworks (18)
3. Economics & Business: Core Principles (20)
4. Business: Competitive Advantage & Moats (19)
5. Mathematics & Probability (12)
6. Physics, Engineering & Systems (11)
7. Biology & Evolution (6)
8. Organizational & Institutional (9)

Each entry includes name, category, and brief description. The list appears
to synthesize models from Poor Charlie's Almanack, Seeking Wisdom, and
Farnam Street's compilation.

### Secondary Archive: Farnam Street (49+ models)

**URL:** https://fs.blog/mental-models/

Shane Parrish's compilation organized into: General Thinking Tools, Physics
Chemistry and Biology, Systems Thinking, Mathematics, Economics. More
detailed per-model descriptions than Sources of Insight, with links to
full articles. Not Munger-specific but heavily Munger-influenced. The
Great Mental Models book series (4 volumes) extends this further.

### Tertiary Source: Bourseiness (30 models)

**URL:** https://www.bourseiness.com/en/155/charlie-munger-mental-models

Focused on the models Munger emphasized most in speeches and Berkshire
meetings. Includes models not prominent in other lists (e.g., "Physics
Envy," "Parimutuel Betting," "The Iron Prescription").

### Cross-Reference Methodology

1. Started with the Sources of Insight 129-model list as the base
2. Cross-referenced against Farnam Street's list for model descriptions
   and category assignments
3. Checked Bourseiness for models emphasized in primary sources but
   missing from the other lists
4. Filtered to models with clear structural mappings (source domain ->
   target domain), excluding pure heuristics and bare cognitive biases

### Already in Catalog (4 entries -- skipped)

- `the-map-is-not-the-territory` -- paradigm, already in catalog
- `survival-of-the-fittest` -- paradigm, already in catalog
- `bottleneck` -- dead-metaphor, already in catalog
- `golden-hammer` -- conceptual-metaphor, already in catalog (note: closely
  related to man-with-a-hammer but approaches from different angle)

## Extraction Strategy

### Kind Classification Decision

**Recommendation: use `paradigm` for all candidates.**

The existing kinds in the validator are: `conceptual-metaphor`, `archetype`,
`dead-metaphor`, `paradigm`.

Rationale for `paradigm`:

- Munger's mental models are not conceptual metaphors in the Lakoff sense
  (they are not primarily about how language structures thought)
- They are not archetypes (recurring patterns in software/design)
- They are not dead metaphors (not lexicalized into everyday language)
- `paradigm` fits: "a system-level framework from one domain applied as an
  analytical lens in another" -- this is exactly what Munger advocates
- Precedent: `the-map-is-not-the-territory` and `survival-of-the-fittest`
  are both already cataloged as `paradigm` entries and are both Munger models
- `cross-field-mapping` does not exist in the validator. Adding it would
  require schema changes. `paradigm` covers the intent without changes.

**No validator or schema changes needed.** All 43 candidates use `paradigm`.

If the Surveyor wants a new kind (e.g., `mental-model` or
`cross-field-mapping`), the changes would be:
1. Add the kind to `VALID_KINDS` in `scripts/validate.py`
2. Add it to the `kind` enum in CLAUDE.md and CONTRIBUTING.md
3. Create a new category `mental-models` or `decision-science`

This is flagged as a decision point for the Surveyor, not a blocker.

### For Miners

Each candidate in the manifest has:

- `slug`: the filename for `catalog/mappings/{slug}.md`
- `name`: human-readable name
- `kind`: `paradigm` (all entries)
- `source_frame` and `target_frame`: the source discipline and the
  target domain where the model is applied
- `categories`: typically `systems-thinking` plus discipline-specific
- `archive_ref`: which archive source(s) list this model, with item
  numbers for Sources of Insight
- `description`: brief note on the structural mapping and why it matters

**Miner workflow:**

1. Read the `description` field for the core structural mapping
2. For models with Sources of Insight references, fetch the full article
   at `https://sourcesofinsight.com/charlie-munger-mental-models/` for
   context
3. For models also on Farnam Street, fetch the dedicated article at
   `https://fs.blog/{slug-variant}/` for detailed treatment
4. Use Poor Charlie's Almanack chapter references (where given in
   `archive_ref`) to write the Origin Story section
5. Cross-reference related entries in the manifest (e.g., the psychology
   cluster, the physics cluster, the economics cluster)
6. Set `related:` to link within clusters and to existing catalog entries
   (especially `the-map-is-not-the-territory` and `survival-of-the-fittest`)

**Writing guidance for Munger entries:**

- The "What It Brings" section should explain the structural mapping:
  what does the source domain's structure illuminate about the target?
- The "Where It Breaks" section is critical -- Munger himself warned about
  over-applying any single model. Each entry should describe where this
  model misleads, not just where it helps.
- The "Expressions" section should include Munger's own phrasing (from
  speeches/Almanack) plus common usage in business/investing contexts.
- Author: `munger` (create author entry if needed)

### Batching Recommendation

Process in thematic clusters:

- **Batch 1 -- Core Thinking Tools (8):** inversion, circle-of-competence,
  man-with-a-hammer, first-principles-thinking, second-order-thinking,
  two-track-analysis, falsification, checklist-approach.
  These are the meta-models -- the ones about how to think. Do first.

- **Batch 2 -- Physics & Systems (8):** feedback-loops, critical-mass,
  leverage, activation-energy, catalysts, nonlinearity, redundancy,
  system-resilience-vs-fragility.
  Physical models applied as reasoning tools.

- **Batch 3 -- Economics & Business (8):** margin-of-safety, mr-market,
  economic-moats, compounding, opportunity-cost, creative-destruction,
  switching-costs, scale-economies.
  The investing/business application cluster.

- **Batch 4 -- Psychology & Social (8):** incentive-caused-bias,
  lollapalooza-effect, social-proof, reciprocity, information-asymmetry,
  principal-agent-problem, culture-as-a-control-system, scenario-analysis.
  Human behavior models.

- **Batch 5 -- Mathematics & Biology (6):** regression-to-the-mean,
  power-laws, bayesian-updating, red-queen-effect, niche-specialization,
  comparative-advantage.
  Formal models applied cross-domain.

- **Batch 6 -- Meta & Remaining (5):** latticework-of-mental-models,
  occams-razor, hanlons-razor, cancer-surgery-formula,
  checklist-approach.
  The meta-model and the metaphorical models.

## Schema Mapping

### Kind Assignment

| Kind | Count | Criteria |
|------|-------|----------|
| `paradigm` | 43 | Cross-domain reasoning framework with clear structural mapping |

### Frame Inventory

**Existing reusable frames (in catalog):**

- `physics` -- source frame for leverage, feedback-loops, critical-mass,
  activation-energy, catalysts, nonlinearity, second-order-thinking,
  first-principles-thinking, two-track-analysis, scale-economies,
  switching-costs, culture-as-a-control-system, lollapalooza-effect
- `economics` -- source/target for compounding, opportunity-cost,
  incentive-caused-bias, reciprocity, comparative-advantage,
  information-asymmetry, principal-agent-problem; target for
  margin-of-safety, mr-market, economic-moats, creative-destruction,
  leverage, niche-specialization, network-effects, scale-economies,
  switching-costs, cancer-surgery-formula
- `natural-selection` -- source for red-queen-effect, niche-specialization,
  social-proof
- `geometry` -- source for circle-of-competence, inversion,
  regression-to-the-mean, power-laws, bayesian-updating
- `architecture-and-building` -- source for margin-of-safety,
  latticework-of-mental-models, redundancy, system-resilience-vs-fragility
- `tool-use` -- source for man-with-a-hammer, occams-razor, hanlons-razor
- `war` -- source for economic-moats, scenario-analysis
- `medicine` -- source for cancer-surgery-formula, checklist-approach
- `causal-reasoning` -- target for inversion, second-order-thinking,
  opportunity-cost, regression-to-the-mean, falsification,
  two-track-analysis, scenario-analysis, nonlinearity, checklist-approach
- `social-behavior` -- target for incentive-caused-bias, lollapalooza-effect,
  social-proof, reciprocity, critical-mass, activation-energy, catalysts,
  hanlons-razor, comparative-advantage, information-asymmetry
- `intellectual-inquiry` -- target for circle-of-competence,
  man-with-a-hammer, latticework-of-mental-models, first-principles-thinking,
  occams-razor, bayesian-updating
- `governance` -- target for principal-agent-problem,
  culture-as-a-control-system
- `systems-thinking` -- target for feedback-loops, redundancy,
  system-resilience-vs-fragility, power-laws; category on many entries
- `competition` -- target for red-queen-effect
- `life-course` -- target for compounding
- `network-communication` -- source for network-effects
- `destruction` -- source for creative-destruction
- `social-roles` -- source for mr-market

**New frames potentially needed:** None. All 42 candidates map to existing
frames.

### Categories

Most entries get `systems-thinking` as primary or secondary category.
Additional by cluster:

- Thinking tools: `philosophy`, `cognitive-science`
- Psychology models: `psychology`, `social-dynamics`
- Business/economics: `organizational-behavior`
- Math/stats: `cognitive-science`

All categories already exist in the catalog.

## Gotchas

1. **Not a canonical list.** Unlike Lakoff & Johnson's book (finite,
   enumerable), Munger never published a master list. The 129 models
   from Sources of Insight include models Munger referenced once in passing
   alongside models he discussed for decades. The manifest selects the
   43 with the clearest structural mappings.

2. **Overlap with existing entries.** Four models already exist in the
   catalog (`the-map-is-not-the-territory`, `survival-of-the-fittest`,
   `bottleneck`, `golden-hammer`). Miners should add `related:` links
   to these from new entries. The existing entries should NOT be
   re-created.

3. **Author attribution.** Many of these models were not invented by
   Munger -- he popularized them. Inversion is Jacobi's, Margin of Safety
   is Graham's, Bayesian Updating is Bayes's. The `author` field should
   be `munger` (as the curator) with the originator noted in the Origin
   Story section.

4. **Frame reuse is heavy.** `physics` and `economics` appear as source
   frames for ~20 entries each. This is intentional -- Munger explicitly
   draws from these disciplines. But it means the frame files should be
   checked for adequate role coverage before mining begins.

5. **The `paradigm` kind decision.** This playbook recommends `paradigm`
   for all 42 entries. If the Surveyor prefers a new kind like
   `mental-model` or `cross-field-mapping`, all manifest entries and the
   validator will need updating. This is a policy decision, not a
   technical one.

6. **Sub-issue count is well within the 100-issue GitHub cap.** 43
   candidates, no overflow handling needed.

7. **LLM-sourced gap analysis.** All 42 candidates trace to at least one
   of the three archive sources (Sources of Insight, Farnam Street,
   Bourseiness). The descriptions include LLM-synthesized context about
   why each mapping is interesting, but the candidate selection itself is
   archive-driven. The `source` field is `"archive"` for all entries.

8. **Some models are meta-models.** "Latticework of Mental Models" is
   a model about models. "Man with a Hammer" is a model about the danger
   of having too few models. These recursive entries should be written
   with awareness of their self-referential nature.

9. **Munger's psychology list (25 tendencies) is mostly excluded.**
   Only 4 of the 25 standard causes of misjudgment made the manifest
   (incentive-caused-bias, lollapalooza-effect, social-proof,
   reciprocity). The rest are cognitive biases without clear structural
   domain mappings. If the Surveyor wants them included, they could be
   added as `conceptual-metaphor` entries where the bias name contains
   a metaphorical frame (e.g., "Doubt-Avoidance" implies DOUBT IS A
   THREAT TO AVOID).
