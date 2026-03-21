---
slug: site-repair
name: Site Repair
kind: pattern
source_frame: architecture-and-building
applies_to:
  - software-abstraction
categories:
  - systems-thinking
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - piecemeal-growth
  - strangler-fig
dead: false
created: '2026-03-19'
updated: '2026-03-19'
grounding: established
harness: Claude Code
transfers:
  - '[source] each new construction should be placed on the part of the site that is in worst condition, preserving the parts that are already alive and functional, mapping the principle of targeted remediation onto any system where resources must be allocated between maintenance of the good and repair of the bad'
  - '[source] the pattern treats the site as a whole with varying quality across regions, rather than as a blank canvas to be redesigned from scratch, encoding the insight that existing systems contain valuable structure that rebuilding would destroy'
  - '[source] repeated application of the rule produces a ratchet effect: each intervention raises the floor of the weakest area while leaving strong areas undisturbed, so overall quality increases monotonically over successive iterations'
limits:
  - '[source] breaks when the worst part of the site is worst precisely because it is structurally unsuitable for building (a flood plain, a contaminated plot), and placing construction there will produce a new building that is also compromised -- the analogous risk in software is investing refactoring effort in code that is fundamentally misconceived rather than merely neglected'
  - '[source] assumes that "worst" is diagnosable and locally remediable, but in software systems the worst area is often the result of distributed entanglement (circular dependencies, shared mutable state) that cannot be repaired by working on one region alone'
embodied_patterns:
  - container
  - matching
  - accretion
relation_types:
  - restore
  - transform
structure: growth
abstraction_level: specific
---

## Transfers

Christopher Alexander's pattern #104, "Site Repair," states: "Buildings
must always be built on those parts of the land which are in the worst
condition, not the best." Leave the healthy trees, the good drainage,
the natural gardens untouched. Put the parking lot, the foundation, the
heavy construction on the part that is already degraded. Over time, this
rule transforms the site: the bad parts get built over and improved, the
good parts are preserved, and the overall quality of the place increases.

Key structural parallels:

- **Build on the worst, preserve the best** -- the core heuristic. When
  deciding where to invest effort in an existing system, target the
  weakest area rather than improving what already works. In software,
  this means refactoring the most tangled module rather than polishing
  the clean one, investing documentation effort in the most confusing
  subsystem rather than the most transparent one, assigning the
  strongest developers to the worst codebase rather than the greenfield
  project. The pattern directly contradicts the natural tendency to work
  where conditions are already pleasant.

- **The site is not a blank canvas** -- Site Repair assumes you are
  working with an existing landscape that has both good and bad areas.
  It rejects the tabula rasa assumption that underlies ground-up
  rewrites. The pattern encodes the insight that existing systems
  contain emergent value -- working relationships between components,
  accumulated institutional knowledge, proven-in-production behavior --
  that a rewrite would destroy. The goal is repair, not replacement.

- **Monotonic improvement through targeted iteration** -- each round
  of Site Repair raises the quality floor. The worst area gets better;
  the best areas stay the same. Over many iterations, the gap between
  the best and worst parts narrows, and the overall quality increases.
  This is the refactoring ratchet: each sprint's technical debt
  reduction makes the codebase slightly more uniform, and the
  uniformity itself reduces future maintenance cost.

- **The pattern is self-directing** -- Site Repair tells you where to
  work next without requiring a master plan. Just identify the worst
  area and work there. This is powerful in complex systems where global
  optimization is computationally intractable but local diagnosis is
  feasible. The pattern converts the overwhelming question "how do we
  improve the whole system?" into the tractable question "what's the
  worst part right now?"

## Limits

- **Sometimes the worst part is worst for a reason** -- Alexander's
  pattern assumes that degraded land can be improved by building on it.
  But some land is degraded because it floods, sits on unstable soil,
  or is contaminated. Building there may produce a compromised
  structure. In software, the worst module may be worst because it
  handles intrinsically complex domain logic, sits at a convergence
  point of many concerns, or reflects genuinely contradictory
  requirements. Pouring refactoring effort into such a module may
  produce cleaner code that is still the worst module, because the
  difficulty is essential rather than accidental.

- **Local repair cannot fix systemic entanglement** -- the pattern
  assumes that "worst" is a local property that can be addressed
  locally. But in software systems, the worst area is often worst
  because of its relationships with everything else: circular
  dependencies, shared global state, implicit coupling. Repairing
  one module without addressing the entanglement just moves the
  mess to the boundary.

- **The pattern undervalues strategic investment in strengths** -- Site
  Repair is a pure remediation strategy. It never says "invest in your
  best asset to create competitive advantage." In business and
  technology, there are times when doubling down on what already works
  (the best part of the site) produces more value than fixing what is
  broken. The pattern's exclusive focus on weakness repair can lead to
  mediocrity everywhere rather than excellence somewhere.

- **Identifying "the worst part" requires agreement** -- the pattern
  assumes that "worst" is self-evident. In practice, teams disagree
  about what constitutes the worst area of a codebase. Is it the
  module with the most bugs? The one with the worst test coverage?
  The one that is hardest to understand? The one that blocks the most
  feature work? The pattern's apparent simplicity conceals a
  prioritization problem.

## Expressions

- "Build on the worst part of the site" -- the core heuristic,
  applicable to any allocation of improvement effort
- "Don't polish the silver while the roof leaks" -- the folk version,
  prioritizing structural repair over cosmetic improvement
- "Refactor the worst module first" -- the software application,
  directing technical debt reduction effort
- "The codebase improves one bad module at a time" -- the ratchet
  effect, describing monotonic improvement through targeted iteration
- "We're not rewriting; we're repairing the site" -- distinguishing
  incremental improvement from ground-up replacement

## Origin Story

Site Repair is pattern #104 in Christopher Alexander, Sara Ishikawa,
and Murray Silverstein's *A Pattern Language* (1977). The book presents
253 patterns for designing buildings, neighborhoods, and towns, each
framed as a problem-solution pair with a confidence rating. Site Repair
appears early in the building-level patterns and establishes a principle
that recurs throughout Alexander's work: work with what exists, improve
the worst parts, preserve the best. The pattern was adopted by the
software engineering community along with Alexander's broader pattern
language concept, though it is less frequently cited than the structural
and organizational patterns. Its closest software analogue is the
"strangler fig" pattern (Martin Fowler, 2004), which shares the
principle of incremental replacement rather than wholesale rewrite.

## References

- Alexander, C., Ishikawa, S. & Silverstein, M. *A Pattern Language*
  (1977) -- pattern #104, the primary source
- Alexander, C. *The Timeless Way of Building* (1979) -- the theoretical
  framework underlying the pattern language
- Fowler, M. "StranglerFigApplication" (2004) -- the software parallel,
  applying incremental replacement to legacy systems
