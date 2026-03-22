# Structural Enrichment Eval Report

**Date:** 2026-03-22T04:26:20.036Z
**Embedding model:** openai/text-embedding-3-small
**Entries tagged:** 100
**Analogy triples:** 40

## Strategy Comparison

| Strategy | Passes | Rate |
|----------|--------|------|
| text-only (baseline) | 9/40 | 23% |
| blended (α=0.3) | 16/40 | 40% |
| blended (α=0.5) | 22/40 | 55% |
| blended (α=0.7) | 22/40 | 55% |
| faceted-only (tags) | 24/40 | 60% |

## Best Strategy vs Baseline

| Metric | Baseline (text-only) | faceted-only (tags) |
|--------|---------------------|—————————————————————|
| Passes | 9/40 (23%) | 24/40 (60%) |
| Improved (flipped F→P) | — | 18 |
| Regressed (flipped P→F) | — | 3 |
| Net improvement | — | +15 |
| Cross-domain passes | — | 22/24 |

## Detailed Results

| ID | Description | A | B (structural) | C (topical) | Base A↔B | Base A↔C | Base | Enr A↔B | Enr A↔C | Enr | Flip |
|----|-------------|---|----------------|-------------|----------|----------|------|---------|---------|-----|------|
| t01 | Force + competition across domains | argument-is-war | survival-of-the-fittest | trojan-war | 0.479 | 0.611 | F | 0.340 | 0.534 | F | = |
| t02 | Accumulation causing systemic problems | technical-debt | the-commons | code-smell | 0.477 | 0.549 | F | 0.185 | 0.007 | P | + |
| t03 | Flow constrained at narrowest point | bottleneck | kanban | data-flow-is-fluid-flow | 0.568 | 0.639 | F | 0.445 | 0.601 | F | = |
| t04 | Surface signal indicating hidden depth p | code-smell | the-shadow | technical-debt | 0.498 | 0.549 | F | 0.388 | 0.007 | P | + |
| t05 | Emergent order from additive contributio | stone-soup | yes-and | the-commons | 0.615 | 0.588 | P | 0.728 | 0.354 | P | = |
| t06 | Self-halting flow to prevent defect prop | andon | jidoka | kanban | 0.780 | 0.683 | P | 0.775 | 0.408 | P | = |
| t07 | Compounding small improvements over time | kaizen | yes-and | pdca-cycle | 0.604 | 0.733 | F | 0.451 | 0.308 | P | + |
| t08 | Boundary-crossing transformation | the-trickster | creative-destruction | the-hero | 0.578 | 0.640 | F | 0.463 | 0.528 | F | = |
| t09 | Translating between two systems | the-wise-old-man | entrance-transition | the-great-mother | 0.491 | 0.649 | F | 0.372 | 0.170 | P | + |
| t10 | Coordinating many-to-one through a hub | the-mediator-pattern | incident-command-system | the-observer-pattern | 0.468 | 0.567 | F | 0.386 | 0.452 | F | = |
| t11 | Cycle + balance + restore = homeostatic  | feedback-loops | ouroboros | second-order-thinking | 0.686 | 0.691 | F | 0.597 | 0.288 | P | + |
| t12 | Decomposing to fundamentals | first-principles-thinking | the-trickster | inversion | 0.487 | 0.625 | F | 0.344 | 0.283 | P | + |
| t13 | Boundary as enabling constraint | the-great-mother | mise-en-place | the-great-chain-of-being | 0.466 | 0.529 | F | 0.522 | 0.223 | P | + |
| t14 | Self-organization producing emergent str | garden-growing-wild | mosaic-of-subcultures | the-flow-through-rooms | 0.632 | 0.626 | P | 0.279 | 0.213 | P | = |
| t15 | Attraction pulling along a path | pied-piper | paths-and-goals | prometheus | 0.523 | 0.651 | F | 0.374 | 0.412 | F | = |
| t16 | Integrating opposites into wholeness | the-self | stone-soup | the-shadow | 0.503 | 0.730 | F | 0.368 | 0.100 | P | + |
| t17 | Pull-based flow with deliberate constrai | just-in-time | cleaning-as-you-go | kanban | 0.602 | 0.742 | F | 0.296 | 0.545 | F | = |
| t18 | Competitive iteration producing adaptati | red-queen-effect | creative-destruction | survival-of-the-fittest | 0.711 | 0.762 | F | 0.540 | 0.534 | P | + |
| t19 | Hierarchy connecting distinct levels | world-tree | brigade-system | the-great-chain-of-being | 0.468 | 0.682 | F | 0.663 | 0.630 | P | + |
| t20 | Structure matching social boundaries (Co | structure-follows-social-spaces | call-and-callback | mosaic-of-subcultures | 0.483 | 0.706 | F | 0.134 | 0.706 | F | = |
| t21 | Triage as decomposition under constraint | triage | brigade-system | virus | 0.537 | 0.571 | F | 0.251 | 0.145 | P | + |
| t22 | Contagion through network links — biolog | virus | pied-piper | ai-hallucination-is-perception-disorder | 0.501 | 0.558 | F | 0.273 | 0.010 | P | + |
| t23 | Boundary violation where untrusted cross | prompt-injection | invasive-species-as-metaphor | ai-hallucination-is-perception-disorder | 0.581 | 0.616 | F | 0.179 | 0.508 | F | = |
| t24 | Removal of one part collapses the whole | keystone-species | bus-factor | trophic-cascade | 0.620 | 0.724 | F | 0.457 | 0.167 | P | + |
| t25 | Boundary zones as generative spaces | edge-effect | entrance-transition | regime-shift | 0.561 | 0.667 | F | 0.283 | 0.119 | P | + |
| t26 | Escalating competitive displacement | invasive-species-as-metaphor | red-queen-effect | keystone-species | 0.644 | 0.693 | F | 0.298 | 0.100 | P | + |
| t27 | System flips between stable states when  | regime-shift | creative-destruction | adaptive-cycle | 0.682 | 0.725 | F | 0.162 | 0.316 | F | = |
| t28 | Causal contamination flowing from root t | fruit-of-the-poisonous-tree | false-in-one-thing-false-in-all | filesystem-tree | 0.618 | 0.614 | P | 0.179 | 0.114 | P | = |
| t29 | Emergent coordination from local rules,  | agent-swarm | the-ensemble | web | 0.562 | 0.602 | F | 0.641 | 0.656 | F | = |
| t30 | Confinement converts potential collabora | raptor-pit | the-commons | loose-cannon | 0.439 | 0.564 | F | 0.369 | 0.875 | F | = |
| t31 | Creation that escapes creator control | frankenstein-is-technology-risk | paperclip-maximizer-is-alignment-failure | ai-hallucination-is-perception-disorder | 0.609 | 0.563 | P | 0.177 | 0.211 | F | - |
| t32 | Sealed container on a multi-generational | generation-ship-is-long-horizon-institution | the-great-mother | big-brother-is-surveillance | 0.571 | 0.490 | P | 0.354 | 0.417 | F | - |
| t33 | Splitting evaluator from interested part | no-one-should-judge-their-own-case | talk-to-the-character-not-the-actor | hear-the-other-side | 0.559 | 0.755 | F | 0.329 | 0.522 | F | = |
| t34 | Selection quality dominates system perfo | casting-is-ninety-percent | triage | the-ensemble | 0.490 | 0.727 | F | 0.203 | 0.229 | F | = |
| t35 | Layered boundaries that slow penetration | defense-in-depth | copper-bottomed | attack-surface | 0.559 | 0.805 | F | 0.466 | 0.343 | P | + |
| t36 | Articulating forces you to see mismatche | rubber-duck-debugging | the-map-is-not-the-territory | spaghetti-code | 0.456 | 0.528 | F | 0.232 | 0.066 | P | + |
| t37 | Tool-body merger that amplifies capabili | ai-is-a-prosthesis | bicycle-for-the-mind | ai-is-a-black-box | 0.714 | 0.609 | P | 0.317 | 0.100 | P | = |
| t38 | Structureless mass where everything enta | big-ball-of-mud | spaghetti-code | technical-debt | 0.666 | 0.618 | P | 0.472 | 0.598 | F | - |
| t39 | Knowledge gap bridged by a more capable  | more-knowledgeable-other | master-and-apprentices | principal-agent-problem | 0.638 | 0.566 | P | 0.691 | 0.352 | P | = |
| t40 | Four-phase cycle of accumulation, releas | adaptive-cycle | ouroboros | regime-shift | 0.625 | 0.725 | F | 0.440 | 0.316 | P | + |

## Improvements (baseline F → enriched P)

### t02: Accumulation causing systemic problems

- **A:** technical-debt
- **B (correct):** the-commons
- **C (trap):** code-smell
- **Bridge:** accretion/accumulate + prevent — deposits degrade the system
- Baseline: A↔B 0.477, A↔C 0.549 → FAIL (topical trap won)
- Enriched: A↔B 0.185, A↔C 0.007 → PASS (structural match won)

### t04: Surface signal indicating hidden depth problem

- **A:** code-smell
- **B (correct):** the-shadow
- **C (trap):** technical-debt
- **Bridge:** surface-depth + boundary — visible symptom of denied/hidden structural issue
- Baseline: A↔B 0.498, A↔C 0.549 → FAIL (topical trap won)
- Enriched: A↔B 0.388, A↔C 0.007 → PASS (structural match won)

### t07: Compounding small improvements over time

- **A:** kaizen
- **B (correct):** yes-and
- **C (trap):** pdca-cycle
- **Bridge:** accretion + iteration + accumulate — small deposits accreting into transformation
- Baseline: A↔B 0.604, A↔C 0.733 → FAIL (topical trap won)
- Enriched: A↔B 0.451, A↔C 0.308 → PASS (structural match won)

### t09: Translating between two systems

- **A:** the-wise-old-man
- **B (correct):** entrance-transition
- **C (trap):** the-great-mother
- **Bridge:** translate + enable + center-periphery/boundary — mediating between domains
- Baseline: A↔B 0.491, A↔C 0.649 → FAIL (topical trap won)
- Enriched: A↔B 0.372, A↔C 0.170 → PASS (structural match won)

### t11: Cycle + balance + restore = homeostatic systems

- **A:** feedback-loops
- **B (correct):** ouroboros
- **C (trap):** second-order-thinking
- **Bridge:** iteration + restore + cycle structure — output becomes input, system self-corrects
- Baseline: A↔B 0.686, A↔C 0.691 → FAIL (topical trap won)
- Enriched: A↔B 0.597, A↔C 0.288 → PASS (structural match won)

### t12: Decomposing to fundamentals

- **A:** first-principles-thinking
- **B (correct):** the-trickster
- **C (trap):** inversion
- **Bridge:** removal + part-whole/decompose — stripping away to find what's structural
- Baseline: A↔B 0.487, A↔C 0.625 → FAIL (topical trap won)
- Enriched: A↔B 0.344, A↔C 0.283 → PASS (structural match won)

### t13: Boundary as enabling constraint

- **A:** the-great-mother
- **B (correct):** mise-en-place
- **C (trap):** the-great-chain-of-being
- **Bridge:** container + boundary + enable + prevent — containment simultaneously nurtures and constrains
- Baseline: A↔B 0.466, A↔C 0.529 → FAIL (topical trap won)
- Enriched: A↔B 0.522, A↔C 0.223 → PASS (structural match won)

### t16: Integrating opposites into wholeness

- **A:** the-self
- **B (correct):** stone-soup
- **C (trap):** the-shadow
- **Bridge:** merging + part-whole + coordinate — diverse parts integrated into emergent whole
- Baseline: A↔B 0.503, A↔C 0.730 → FAIL (topical trap won)
- Enriched: A↔B 0.368, A↔C 0.100 → PASS (structural match won)

### t18: Competitive iteration producing adaptation

- **A:** red-queen-effect
- **B (correct):** creative-destruction
- **C (trap):** survival-of-the-fittest
- **Bridge:** force + iteration + compete — running to stay in place vs selected-for fitness
- Baseline: A↔B 0.711, A↔C 0.762 → FAIL (topical trap won)
- Enriched: A↔B 0.540, A↔C 0.534 → PASS (structural match won)

### t19: Hierarchy connecting distinct levels

- **A:** world-tree
- **B (correct):** brigade-system
- **C (trap):** the-great-chain-of-being
- **Bridge:** center-periphery + path + part-whole + hierarchy — vertical infrastructure connecting layers
- Baseline: A↔B 0.468, A↔C 0.682 → FAIL (topical trap won)
- Enriched: A↔B 0.663, A↔C 0.630 → PASS (structural match won)

### t21: Triage as decomposition under constraint — kitchen meets ER

- **A:** triage
- **B (correct):** brigade-system
- **C (trap):** virus
- **Bridge:** select + decompose + pipeline — routing work to specialized stations under resource pressure
- Baseline: A↔B 0.537, A↔C 0.571 → FAIL (topical trap won)
- Enriched: A↔B 0.251, A↔C 0.145 → PASS (structural match won)

### t22: Contagion through network links — biology meets technology

- **A:** virus
- **B (correct):** pied-piper
- **C (trap):** ai-hallucination-is-perception-disorder
- **Bridge:** flow + iteration + link + cause — something propagates through a network by exploiting connections, bypassing rational assessment
- Baseline: A↔B 0.501, A↔C 0.558 → FAIL (topical trap won)
- Enriched: A↔B 0.273, A↔C 0.010 → PASS (structural match won)

### t24: Removal of one part collapses the whole

- **A:** keystone-species
- **B (correct):** bus-factor
- **C (trap):** trophic-cascade
- **Bridge:** center-periphery + removal + part-whole + decompose — system integrity depends on a single element whose absence is catastrophic
- Baseline: A↔B 0.620, A↔C 0.724 → FAIL (topical trap won)
- Enriched: A↔B 0.457, A↔C 0.167 → PASS (structural match won)

### t25: Boundary zones as generative spaces

- **A:** edge-effect
- **B (correct):** entrance-transition
- **C (trap):** regime-shift
- **Bridge:** boundary + merging/surface-depth + enable + transform — liminal zones between domains produce novelty unavailable in either domain alone
- Baseline: A↔B 0.561, A↔C 0.667 → FAIL (topical trap won)
- Enriched: A↔B 0.283, A↔C 0.119 → PASS (structural match won)

### t26: Escalating competitive displacement

- **A:** invasive-species-as-metaphor
- **B (correct):** red-queen-effect
- **C (trap):** keystone-species
- **Bridge:** force + iteration + compete + accumulate — newcomer exploits absence of evolved constraints, compounding advantage through each cycle
- Baseline: A↔B 0.644, A↔C 0.693 → FAIL (topical trap won)
- Enriched: A↔B 0.298, A↔C 0.100 → PASS (structural match won)

### t35: Layered boundaries that slow penetration

- **A:** defense-in-depth
- **B (correct):** copper-bottomed
- **C (trap):** attack-surface
- **Bridge:** boundary + surface-depth + container + prevent — multiple protective layers where each absorbs some damage, the deeper ones never tested if the outer holds
- Baseline: A↔B 0.559, A↔C 0.805 → FAIL (topical trap won)
- Enriched: A↔B 0.466, A↔C 0.343 → PASS (structural match won)

### t36: Articulating forces you to see mismatches

- **A:** rubber-duck-debugging
- **B (correct):** the-map-is-not-the-territory
- **C (trap):** spaghetti-code
- **Bridge:** surface-depth + translate + matching — externalizing internal state (speaking/mapping) reveals discrepancies between representation and reality
- Baseline: A↔B 0.456, A↔C 0.528 → FAIL (topical trap won)
- Enriched: A↔B 0.232, A↔C 0.066 → PASS (structural match won)

### t40: Four-phase cycle of accumulation, release, and renewal

- **A:** adaptive-cycle
- **B (correct):** ouroboros
- **C (trap):** regime-shift
- **Bridge:** iteration + accretion + restore + cycle — system accumulates structure, collapses, and reorganizes in a repeating pattern where ending feeds beginning
- Baseline: A↔B 0.625, A↔C 0.725 → FAIL (topical trap won)
- Enriched: A↔B 0.440, A↔C 0.316 → PASS (structural match won)

## Regressions (baseline P → enriched F)

### t31: Creation that escapes creator control

- **A:** frankenstein-is-technology-risk
- **B (correct):** paperclip-maximizer-is-alignment-failure
- **C (trap):** ai-hallucination-is-perception-disorder
- Baseline: A↔B 0.609, A↔C 0.563 → PASS
- Enriched: A↔B 0.177, A↔C 0.211 → FAIL (regression)

### t32: Sealed container on a multi-generational path

- **A:** generation-ship-is-long-horizon-institution
- **B (correct):** the-great-mother
- **C (trap):** big-brother-is-surveillance
- Baseline: A↔B 0.571, A↔C 0.490 → PASS
- Enriched: A↔B 0.354, A↔C 0.417 → FAIL (regression)

### t38: Structureless mass where everything entangles

- **A:** big-ball-of-mud
- **B (correct):** spaghetti-code
- **C (trap):** technical-debt
- Baseline: A↔B 0.666, A↔C 0.618 → PASS
- Enriched: A↔B 0.472, A↔C 0.598 → FAIL (regression)

## Methodology

Each analogy triple contains:
- **A** — query entry
- **B** — structural match from a different source domain (should rank higher)
- **C** — topical trap from the same/similar domain (should rank lower)

**Strategies tested:**

| Strategy | How it scores |
|----------|---------------|
| text-only (baseline) | cosine_sim of transfers+limits text embeddings |
| faceted-only (tags) | Weighted Jaccard: 0.35×embodied_patterns + 0.35×relation_types + 0.20×structure + 0.10×abstraction_level |
| blended (α=N) | α × faceted_sim + (1-α) × text_sim |

A triple "passes" when sim(A, B) > sim(A, C).
An "improvement" is a triple that fails baseline but passes the best strategy.
The Structural Surprise Rate counts how many passes involve entries from different source frames.
