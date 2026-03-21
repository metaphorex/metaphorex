# Structural Enrichment Eval Report

**Date:** 2026-03-21T15:46:24.553Z
**Embedding model:** openai/text-embedding-3-small
**Entries tagged:** 100
**Analogy triples:** 40

## Strategy Comparison

| Strategy | Passes | Rate |
|----------|--------|------|
| text-only (baseline) | 9/40 | 23% |
| blended (α=0.3) | 14/40 | 35% |
| blended (α=0.5) | 18/40 | 45% |
| blended (α=0.7) | 22/40 | 55% |
| faceted-only (tags) | 24/40 | 60% |

## Best Strategy vs Baseline

| Metric | Baseline (text-only) | faceted-only (tags) |
|--------|---------------------|—————————————————————|
| Passes | 9/40 (23%) | 24/40 (60%) |
| Improved (flipped F→P) | — | 17 |
| Regressed (flipped P→F) | — | 2 |
| Net improvement | — | +15 |
| Cross-domain passes | — | 22/24 |

## Detailed Results

| ID | Description | A | B (structural) | C (topical) | Base A↔B | Base A↔C | Base | Enr A↔B | Enr A↔C | Enr | Flip |
|----|-------------|---|----------------|-------------|----------|----------|------|---------|---------|-----|------|
| t01 | Force + competition across domains | argument-is-war | survival-of-the-fittest | trojan-war | 0.479 | 0.611 | F | 0.328 | 0.545 | F | = |
| t02 | Accumulation causing systemic problems | technical-debt | the-commons | code-smell | 0.477 | 0.549 | F | 0.170 | 0.070 | P | + |
| t03 | Flow constrained at narrowest point | bottleneck | kanban | data-flow-is-fluid-flow | 0.568 | 0.639 | F | 0.432 | 0.632 | F | = |
| t04 | Surface signal indicating hidden depth p | code-smell | the-shadow | technical-debt | 0.498 | 0.549 | F | 0.445 | 0.070 | P | + |
| t05 | Emergent order from additive contributio | stone-soup | yes-and | the-commons | 0.615 | 0.588 | P | 0.720 | 0.345 | P | = |
| t06 | Self-halting flow to prevent defect prop | andon | jidoka | kanban | 0.780 | 0.683 | P | 0.767 | 0.387 | P | = |
| t07 | Compounding small improvements over time | kaizen | yes-and | pdca-cycle | 0.604 | 0.733 | F | 0.412 | 0.340 | P | + |
| t08 | Boundary-crossing transformation | the-trickster | creative-destruction | the-hero | 0.578 | 0.640 | F | 0.450 | 0.650 | F | = |
| t09 | Translating between two systems | the-wise-old-man | entrance-transition | the-great-mother | 0.491 | 0.649 | F | 0.275 | 0.170 | P | + |
| t10 | Coordinating many-to-one through a hub | the-mediator-pattern | incident-command-system | the-observer-pattern | 0.468 | 0.567 | F | 0.415 | 0.440 | F | = |
| t11 | Cycle + balance + restore = homeostatic  | feedback-loops | ouroboros | second-order-thinking | 0.687 | 0.691 | F | 0.667 | 0.400 | P | + |
| t12 | Decomposing to fundamentals | first-principles-thinking | the-trickster | inversion | 0.487 | 0.625 | F | 0.345 | 0.345 | F | = |
| t13 | Boundary as enabling constraint | the-great-mother | mise-en-place | the-great-chain-of-being | 0.466 | 0.529 | F | 0.550 | 0.228 | P | + |
| t14 | Self-organization producing emergent str | garden-growing-wild | mosaic-of-subcultures | the-flow-through-rooms | 0.632 | 0.626 | P | 0.275 | 0.275 | F | - |
| t15 | Attraction pulling along a path | pied-piper | paths-and-goals | prometheus | 0.523 | 0.651 | F | 0.415 | 0.590 | F | = |
| t16 | Integrating opposites into wholeness | the-self | stone-soup | the-shadow | 0.503 | 0.730 | F | 0.377 | 0.100 | P | + |
| t17 | Pull-based flow with deliberate constrai | just-in-time | cleaning-as-you-go | kanban | 0.602 | 0.741 | F | 0.315 | 0.552 | F | = |
| t18 | Competitive iteration producing adaptati | red-queen-effect | creative-destruction | survival-of-the-fittest | 0.711 | 0.762 | F | 0.545 | 0.510 | P | + |
| t19 | Hierarchy connecting distinct levels | world-tree | brigade-system | the-great-chain-of-being | 0.467 | 0.682 | F | 0.660 | 0.592 | P | + |
| t20 | Structure matching social boundaries (Co | structure-follows-social-spaces | call-and-callback | mosaic-of-subcultures | 0.483 | 0.706 | F | 0.140 | 0.725 | F | = |
| t21 | Triage as decomposition under constraint | triage | brigade-system | virus | 0.536 | 0.571 | F | 0.228 | 0.228 | F | = |
| t22 | Contagion through network links — biolog | virus | pied-piper | ai-hallucination-is-perception-disorder | 0.501 | 0.558 | F | 0.425 | 0.087 | P | + |
| t23 | Boundary violation where untrusted cross | prompt-injection | invasive-species-as-metaphor | ai-hallucination-is-perception-disorder | 0.581 | 0.616 | F | 0.228 | 0.508 | F | = |
| t24 | Removal of one part collapses the whole | keystone-species | bus-factor | trophic-cascade | 0.619 | 0.724 | F | 0.392 | 0.167 | P | + |
| t25 | Boundary zones as generative spaces | edge-effect | entrance-transition | regime-shift | 0.561 | 0.667 | F | 0.382 | 0.187 | P | + |
| t26 | Escalating competitive displacement | invasive-species-as-metaphor | red-queen-effect | keystone-species | 0.644 | 0.694 | F | 0.277 | 0.100 | P | + |
| t27 | System flips between stable states when  | regime-shift | creative-destruction | adaptive-cycle | 0.682 | 0.725 | F | 0.228 | 0.423 | F | = |
| t28 | Causal contamination flowing from root t | fruit-of-the-poisonous-tree | false-in-one-thing-false-in-all | filesystem-tree | 0.618 | 0.614 | P | 0.210 | 0.120 | P | = |
| t29 | Emergent coordination from local rules,  | agent-swarm | the-ensemble | web | 0.562 | 0.602 | F | 0.592 | 0.667 | F | = |
| t30 | Confinement converts potential collabora | raptor-pit | the-commons | loose-cannon | 0.439 | 0.564 | F | 0.375 | 0.912 | F | = |
| t31 | Creation that escapes creator control | frankenstein-is-technology-risk | paperclip-maximizer-is-alignment-failure | ai-hallucination-is-perception-disorder | 0.609 | 0.563 | P | 0.325 | 0.287 | P | = |
| t32 | Sealed container on a multi-generational | generation-ship-is-long-horizon-institution | the-great-mother | big-brother-is-surveillance | 0.571 | 0.490 | P | 0.382 | 0.379 | P | = |
| t33 | Splitting evaluator from interested part | no-one-should-judge-their-own-case | talk-to-the-character-not-the-actor | hear-the-other-side | 0.559 | 0.755 | F | 0.345 | 0.550 | F | = |
| t34 | Selection quality dominates system perfo | casting-is-ninety-percent | triage | the-ensemble | 0.490 | 0.727 | F | 0.275 | 0.228 | P | + |
| t35 | Layered boundaries that slow penetration | defense-in-depth | copper-bottomed | attack-surface | 0.559 | 0.805 | F | 0.480 | 0.392 | P | + |
| t36 | Articulating forces you to see mismatche | rubber-duck-debugging | the-map-is-not-the-territory | spaghetti-code | 0.456 | 0.528 | F | 0.187 | 0.070 | P | + |
| t37 | Tool-body merger that amplifies capabili | ai-is-a-prosthesis | bicycle-for-the-mind | ai-is-a-black-box | 0.714 | 0.609 | P | 0.383 | 0.100 | P | = |
| t38 | Structureless mass where everything enta | big-ball-of-mud | spaghetti-code | technical-debt | 0.665 | 0.618 | P | 0.450 | 0.545 | F | - |
| t39 | Knowledge gap bridged by a more capable  | more-knowledgeable-other | master-and-apprentices | principal-agent-problem | 0.638 | 0.566 | P | 0.650 | 0.340 | P | = |
| t40 | Four-phase cycle of accumulation, releas | adaptive-cycle | ouroboros | regime-shift | 0.626 | 0.725 | F | 0.512 | 0.423 | P | + |

## Improvements (baseline F → enriched P)

### t02: Accumulation causing systemic problems

- **A:** technical-debt
- **B (correct):** the-commons
- **C (trap):** code-smell
- **Bridge:** accretion/accumulate + prevent — deposits degrade the system
- Baseline: A↔B 0.477, A↔C 0.549 → FAIL (topical trap won)
- Enriched: A↔B 0.170, A↔C 0.070 → PASS (structural match won)

### t04: Surface signal indicating hidden depth problem

- **A:** code-smell
- **B (correct):** the-shadow
- **C (trap):** technical-debt
- **Bridge:** surface-depth + boundary — visible symptom of denied/hidden structural issue
- Baseline: A↔B 0.498, A↔C 0.549 → FAIL (topical trap won)
- Enriched: A↔B 0.445, A↔C 0.070 → PASS (structural match won)

### t07: Compounding small improvements over time

- **A:** kaizen
- **B (correct):** yes-and
- **C (trap):** pdca-cycle
- **Bridge:** accretion + iteration + accumulate — small deposits accreting into transformation
- Baseline: A↔B 0.604, A↔C 0.733 → FAIL (topical trap won)
- Enriched: A↔B 0.412, A↔C 0.340 → PASS (structural match won)

### t09: Translating between two systems

- **A:** the-wise-old-man
- **B (correct):** entrance-transition
- **C (trap):** the-great-mother
- **Bridge:** translate + enable + center-periphery/boundary — mediating between domains
- Baseline: A↔B 0.491, A↔C 0.649 → FAIL (topical trap won)
- Enriched: A↔B 0.275, A↔C 0.170 → PASS (structural match won)

### t11: Cycle + balance + restore = homeostatic systems

- **A:** feedback-loops
- **B (correct):** ouroboros
- **C (trap):** second-order-thinking
- **Bridge:** iteration + restore + cycle structure — output becomes input, system self-corrects
- Baseline: A↔B 0.687, A↔C 0.691 → FAIL (topical trap won)
- Enriched: A↔B 0.667, A↔C 0.400 → PASS (structural match won)

### t13: Boundary as enabling constraint

- **A:** the-great-mother
- **B (correct):** mise-en-place
- **C (trap):** the-great-chain-of-being
- **Bridge:** container + boundary + enable + prevent — containment simultaneously nurtures and constrains
- Baseline: A↔B 0.466, A↔C 0.529 → FAIL (topical trap won)
- Enriched: A↔B 0.550, A↔C 0.228 → PASS (structural match won)

### t16: Integrating opposites into wholeness

- **A:** the-self
- **B (correct):** stone-soup
- **C (trap):** the-shadow
- **Bridge:** merging + part-whole + coordinate — diverse parts integrated into emergent whole
- Baseline: A↔B 0.503, A↔C 0.730 → FAIL (topical trap won)
- Enriched: A↔B 0.377, A↔C 0.100 → PASS (structural match won)

### t18: Competitive iteration producing adaptation

- **A:** red-queen-effect
- **B (correct):** creative-destruction
- **C (trap):** survival-of-the-fittest
- **Bridge:** force + iteration + compete — running to stay in place vs selected-for fitness
- Baseline: A↔B 0.711, A↔C 0.762 → FAIL (topical trap won)
- Enriched: A↔B 0.545, A↔C 0.510 → PASS (structural match won)

### t19: Hierarchy connecting distinct levels

- **A:** world-tree
- **B (correct):** brigade-system
- **C (trap):** the-great-chain-of-being
- **Bridge:** center-periphery + path + part-whole + hierarchy — vertical infrastructure connecting layers
- Baseline: A↔B 0.467, A↔C 0.682 → FAIL (topical trap won)
- Enriched: A↔B 0.660, A↔C 0.592 → PASS (structural match won)

### t22: Contagion through network links — biology meets technology

- **A:** virus
- **B (correct):** pied-piper
- **C (trap):** ai-hallucination-is-perception-disorder
- **Bridge:** flow + iteration + link + cause — something propagates through a network by exploiting connections, bypassing rational assessment
- Baseline: A↔B 0.501, A↔C 0.558 → FAIL (topical trap won)
- Enriched: A↔B 0.425, A↔C 0.087 → PASS (structural match won)

### t24: Removal of one part collapses the whole

- **A:** keystone-species
- **B (correct):** bus-factor
- **C (trap):** trophic-cascade
- **Bridge:** center-periphery + removal + part-whole + decompose — system integrity depends on a single element whose absence is catastrophic
- Baseline: A↔B 0.619, A↔C 0.724 → FAIL (topical trap won)
- Enriched: A↔B 0.392, A↔C 0.167 → PASS (structural match won)

### t25: Boundary zones as generative spaces

- **A:** edge-effect
- **B (correct):** entrance-transition
- **C (trap):** regime-shift
- **Bridge:** boundary + merging/surface-depth + enable + transform — liminal zones between domains produce novelty unavailable in either domain alone
- Baseline: A↔B 0.561, A↔C 0.667 → FAIL (topical trap won)
- Enriched: A↔B 0.382, A↔C 0.187 → PASS (structural match won)

### t26: Escalating competitive displacement

- **A:** invasive-species-as-metaphor
- **B (correct):** red-queen-effect
- **C (trap):** keystone-species
- **Bridge:** force + iteration + compete + accumulate — newcomer exploits absence of evolved constraints, compounding advantage through each cycle
- Baseline: A↔B 0.644, A↔C 0.694 → FAIL (topical trap won)
- Enriched: A↔B 0.277, A↔C 0.100 → PASS (structural match won)

### t34: Selection quality dominates system performance

- **A:** casting-is-ninety-percent
- **B (correct):** triage
- **C (trap):** the-ensemble
- **Bridge:** select + matching + cause + hierarchy — the initial sorting/matching decision propagates through the entire system; get it wrong and nothing downstream can compensate
- Baseline: A↔B 0.490, A↔C 0.727 → FAIL (topical trap won)
- Enriched: A↔B 0.275, A↔C 0.228 → PASS (structural match won)

### t35: Layered boundaries that slow penetration

- **A:** defense-in-depth
- **B (correct):** copper-bottomed
- **C (trap):** attack-surface
- **Bridge:** boundary + surface-depth + container + prevent — multiple protective layers where each absorbs some damage, the deeper ones never tested if the outer holds
- Baseline: A↔B 0.559, A↔C 0.805 → FAIL (topical trap won)
- Enriched: A↔B 0.480, A↔C 0.392 → PASS (structural match won)

### t36: Articulating forces you to see mismatches

- **A:** rubber-duck-debugging
- **B (correct):** the-map-is-not-the-territory
- **C (trap):** spaghetti-code
- **Bridge:** surface-depth + translate + matching — externalizing internal state (speaking/mapping) reveals discrepancies between representation and reality
- Baseline: A↔B 0.456, A↔C 0.528 → FAIL (topical trap won)
- Enriched: A↔B 0.187, A↔C 0.070 → PASS (structural match won)

### t40: Four-phase cycle of accumulation, release, and renewal

- **A:** adaptive-cycle
- **B (correct):** ouroboros
- **C (trap):** regime-shift
- **Bridge:** iteration + accretion + restore + cycle — system accumulates structure, collapses, and reorganizes in a repeating pattern where ending feeds beginning
- Baseline: A↔B 0.626, A↔C 0.725 → FAIL (topical trap won)
- Enriched: A↔B 0.512, A↔C 0.423 → PASS (structural match won)

## Regressions (baseline P → enriched F)

### t14: Self-organization producing emergent structure

- **A:** garden-growing-wild
- **B (correct):** mosaic-of-subcultures
- **C (trap):** the-flow-through-rooms
- Baseline: A↔B 0.632, A↔C 0.626 → PASS
- Enriched: A↔B 0.275, A↔C 0.275 → FAIL (regression)

### t38: Structureless mass where everything entangles

- **A:** big-ball-of-mud
- **B (correct):** spaghetti-code
- **C (trap):** technical-debt
- Baseline: A↔B 0.665, A↔C 0.618 → PASS
- Enriched: A↔B 0.450, A↔C 0.545 → FAIL (regression)

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
