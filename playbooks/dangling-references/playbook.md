---
project_issue: 2475
repo: metaphorex/metaphorex
source_type: catalog-internal
status: draft
---

# Dangling References

## Source Description

This project mines entries that are already referenced in `related:` fields
by existing catalog entries but have no corresponding entry file. These are
the catalog's "most wanted" entries -- creating them immediately improves
the knowledge graph's connectivity by resolving broken links.

The source is the catalog itself: `catalog/entries/*.md` files contain
`related:` arrays that reference slugs. When a referenced slug has no
matching entry file, the validator reports a warning. This project creates
entries for all such dangling references.

## Access Method

**Primary source:** Run the validator (`uv run scripts/validate.py validate`)
and extract warnings matching `related entry 'X' not found in entries/`.

**Deterministic extraction script:**
`playbooks/dangling-references/scripts/extract_dangling.py`

This script scans all catalog entries, collects `related:` references,
checks which ones have no corresponding entry file, applies consolidation
rules, excludes entries in pending PRs, and outputs structured JSON.

The script is idempotent: as entries are created and merged, they
automatically disappear from the dangling list on the next run.

## Extraction Strategy

1. Run the extraction script to get the current dangling reference list
2. Cross-reference against open PRs to avoid duplicating work in flight
3. Mine entries in priority order (highest ref_count first)
4. Each entry should be mined using standard catalog conventions
5. Since these span many domains, batch by thematic group (5-8 per batch)

### Priority Tiers

**Tier 1 (6 refs):** single-point-of-failure

**Tier 2 (2 refs, 18 entries):** analysis-paralysis, antifragile,
boundary-object, canary-in-a-coal-mine, feedback-loop, five-s,
free-rider-problem, impostor-syndrome, normalization-of-deviance, ooda-loop,
planning-fallacy, psychological-safety, resilience, signal-to-noise,
sky-and-weather, striking-while-the-iron-is-hot, sunk-cost-fallacy,
training-wheels

**Tier 3 (1 ref, 81 entries):** everything else

### Thematic Groups for Batching

**Cognitive biases and decision-making:**
analysis-paralysis, anchoring, confirmation-bias, decoy-effect,
groupthink, hawthorne-effect, planning-fallacy, sunk-cost-fallacy,
contrarian-thinking

**Systems thinking and engineering:**
single-point-of-failure, feedback-loop, homeostasis, leverage-point,
resilience, antifragile, strange-loop, circuit-breaker, dead-mans-switch

**Ecology and biology:**
competitive-exclusion, cross-pollination, mutualism, natural-selection,
predator-prey, symbiosis, biodiversity-loss, vestigial-structure,
parasitic-architecture, strangler-fig

**Software engineering patterns:**
bounded-context, chain-of-responsibility, facade, prototype, spike,
staging-environment, dead-code, easter-egg, work-in-progress,
second-system-effect, conways-law, brooks-law, kiss

**Military and strategy:**
chain-of-command, concentration-of-force, divide-and-conquer, ooda-loop,
first-mover-advantage

**Mythology and archetypes:**
apocalypse, frankenstein, heros-journey, pandoras-box, scapegoat, siren,
coming-of-age

**Psychology and organizational behavior:**
burnout, impostor-syndrome, normalization-of-deviance,
psychological-safety, rupture-and-repair, looking-glass-self,
information-overload

**Folk expressions and dead metaphors:**
canary-in-a-coal-mine, death-by-a-thousand-cuts, gilding-the-lily,
hammer-and-nail, hedging-your-bets, hit-the-nail-on-the-head,
red-herring, slippery-slope, straw-that-broke-the-camels-back,
striking-while-the-iron-is-hot, sugar-coating, when-pigs-fly,
white-elephant, whitewash, sowing-seeds

**Leadership and management:**
servant-leadership, t-shaped-people, sharpening-the-saw,
five-s, free-rider-problem, barn-raising

**Miscellaneous:**
ai-alignment-is-training-an-animal, applause-line, argument-from-authority,
daemon-is-a-background-spirit, grok, knowledge-is-a-landscape, ladder,
murphys-law, goodharts-law, goedels-incompleteness, patina,
panning-for-gold, quis-custodiet-ipsos-custodes, show-dont-tell,
signal-to-noise, sky-and-weather, training-wheels

## Schema Mapping

| Field | Mapping |
|-------|---------|
| slug | The referenced slug from the `related:` field (after consolidation) |
| name | Human-readable form of the slug |
| kind | Determined per-entry: metaphor, mental-model, pattern, archetype, or paradigm |
| source_frame | Best-fit existing frame from `catalog/frames/` |
| applies_to | Context-dependent; many of these apply broadly |
| categories | 1-3 categories from existing `catalog/categories/` |
| author | fshot (or original contributor if identifiable) |
| related | Back-link to the entries that reference this slug, plus thematic peers |

### Kind Assignment Rationale

- **metaphor**: entries with clear source-to-target mapping (burnout, canary-in-a-coal-mine, signal-to-noise)
- **mental-model**: frameworks for thinking about problems (OODA loop, feedback loop, planning fallacy)
- **pattern**: reusable solutions with clear structure (circuit-breaker, facade, bounded-context)
- **archetype**: universal narrative/symbolic figures (hero's journey, scapegoat, siren, frankenstein)
- **paradigm**: worldview-level orientations (servant-leadership, show-dont-tell)

## Consolidations

Three pairs of slugs in the dangling list refer to the same concept:

| Variants | Canonical Slug | Rationale |
|----------|---------------|-----------|
| antifragile, antifragility | antifragile | Prefer adjective; matches common usage |
| canary-in-a-coal-mine, canary-in-the-coal-mine | canary-in-a-coal-mine | Indefinite article is canonical phrasing |
| free-rider, free-rider-problem | free-rider-problem | Problem framing is more useful for the catalog |

After consolidation, existing entries referencing the non-canonical slug
should have their `related:` fields updated. This is a follow-up task,
not part of initial mining.

## Excluded (In Pending PRs)

The following 10 entries appear in the dangling list but already exist in
open PRs. They are excluded from the manifest:

| Slug | PR |
|------|----|
| dichotomy-of-control | #2444 |
| life-is-a-play | #2444 |
| memento-mori | #2444 |
| negative-visualization | #2444 |
| the-mind-is-a-citadel | #2444 |
| cognitive-defusion | #2291 |
| tug-of-war-with-a-monster | #2291 |
| the-line | #2241 |
| pendulation | #2297 |
| jig | #2368 |

Once these PRs merge, the extraction script will automatically exclude
them from subsequent runs.

## Gotchas

1. **Sub-issue cap.** 100 candidates exceeds GitHub's 100-sub-issue limit.
   The Surveyor should plan for batch parent issues or body-text linkage
   for overflow.

2. **Consolidation follow-up.** After mining the canonical entry (e.g.,
   `antifragile`), the entries referencing `antifragility` need their
   `related:` fields updated. This is a separate cleanup pass.

3. **Self-depleting source.** As entries are created and merged, they
   disappear from the dangling list. Re-run the extraction script before
   each mining batch to get the current state.

4. **Broad domain spread.** These 100 entries span 10+ thematic areas.
   Miners should batch by theme to maintain consistent voice and depth
   within each group.

5. **Some entries are well-known.** Many of these (feedback loop, sunk cost
   fallacy, Murphy's law) are so widely known that the Miner must focus on
   what makes the metaphorical framing interesting, not just defining the
   concept. The Limits section is especially important.

6. **Frame creation.** Most source_frames already exist in the catalog.
   The extraction script verified only `aviation` is used for KISS -- this
   frame already exists. No new frames should be needed.
