---
slug: teslers-law
name: "Tesler's Law"
kind: mental-model
source_frame: physics
categories:
- software-engineering
- systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
- law-of-leaky-abstractions
created: '2026-03-21'
updated: '2026-03-21'
grounding: folk
transfers:
  - '[law] Every system has a minimum irreducible complexity that cannot be eliminated, only redistributed between components'
  - '[law] Simplifying one part of a system necessarily transfers complexity to another part -- the interface, the implementation, or the user'
  - '[law] Apparent simplicity in a user-facing layer is paid for by hidden complexity in the layers beneath it'
limits:
  - '[law] Assumes total complexity is conserved, when good design can genuinely reduce overall complexity by reframing the problem rather than just redistributing it'
  - '[law] The "irreducible minimum" is not a fixed quantity -- it depends on the problem framing, and a different framing can reveal that what seemed irreducible was actually an artifact of the original decomposition'
embodied_patterns:
  - balance
  - container
  - surface-depth
relation_types:
  - transform
  - contain
structure: equilibrium
abstraction_level: generic
---

## Transfers

Every application has an inherent amount of irreducible complexity. The
only question is who deals with it -- the user, the application developer,
or the platform developer. Larry Tesler's observation maps the physics of
conservation laws onto system design: complexity, like energy, cannot be
created or destroyed, only moved from one place to another.

Key structural parallels:

- **Conservation of complexity** -- in physics, conservation laws state
  that certain quantities (energy, momentum, charge) cannot be created or
  destroyed within a closed system. Tesler applies this logic to
  complexity: the total complexity of a problem is fixed, and design
  decisions merely redistribute it. Making a user interface simpler does
  not reduce the system's complexity; it transfers complexity from the
  user's experience to the developer's implementation. The complexity
  is conserved.
- **The redistribution tradeoff** -- the law frames design as a
  zero-sum redistribution game with three parties: the end user, the
  application developer, and the platform/infrastructure. Each design
  decision shifts complexity between them. Auto-formatting in a word
  processor moves complexity from user (manual formatting) to developer
  (formatting algorithms). A spreadsheet's formula language moves
  complexity from developer (building specialized tools) to user
  (learning formulas). The question is never "how do we eliminate
  complexity?" but "who should bear it?"
- **The hidden cost of simplicity** -- a corollary of the conservation
  law is that visible simplicity implies hidden complexity. Apple's
  one-button mouse was simple for the user but required enormous
  engineering effort to make single-click, double-click, click-and-hold,
  and drag all work correctly through one control. The simplicity is
  real for the user but the complexity did not disappear; it migrated
  to Cupertino.
- **The irreducibility claim** -- the most provocative structural
  element. Tesler does not merely say complexity moves; he says there
  is a minimum below which it cannot go. Some problems are inherently
  complex, and no amount of clever design can make them simple. Tax
  preparation is inherently complex because tax law is complex.
  Scheduling is inherently complex because constraint satisfaction is
  computationally hard. The law warns against the delusion that "good
  design" can eliminate fundamental complexity.

## Limits

- **Conservation is too strong a claim** -- physics conservation laws
  hold because they reflect deep symmetries of nature. Complexity
  "conservation" has no such grounding. In practice, good design can
  genuinely reduce total complexity, not just move it. Replacing a
  complex configuration system with sensible defaults does not move
  complexity to the developer; it eliminates unnecessary options. The
  insight that complexity cannot be destroyed is approximately useful
  but literally false.
- **The framing problem** -- what counts as "irreducible" depends
  entirely on how you frame the problem. Before spreadsheets, the
  "irreducible complexity" of financial modeling included manual
  recalculation of dependent cells. VisiCalc did not merely redistribute
  this complexity; it reframed the problem so that the complexity
  dissolved. Tesler's Law assumes a fixed problem definition, but the
  most powerful design interventions change the problem.
- **The measurement problem** -- "complexity" is not a well-defined
  quantity like energy. It has no units, no agreed measurement, and no
  way to verify conservation. Two designers can look at the same system
  and disagree about its total complexity, making the "conservation"
  claim unfalsifiable. The law provides intuition but not a calculable
  constraint.
- **Asymmetric redistribution** -- the law implies that moving complexity
  is neutral, but in practice the cost of complexity varies enormously
  by location. Complexity borne by one expert developer is far cheaper
  than the same complexity borne by a million users. The law's
  conservation framing obscures the fact that redistribution is often a
  net benefit, not a zero-sum trade.

## Expressions

- "You can't reduce complexity, only move it" -- the common paraphrase,
  used to push back on demands for "simpler" solutions
- "Tesler's Law" -- invoked in design reviews when stakeholders request
  simplification without acknowledging where the complexity will go
- "The Law of Conservation of Complexity" -- the formal name, drawing
  the physics analogy explicitly
- "Someone has to deal with it" -- the pragmatic formulation, forcing
  the question of who bears the complexity cost
- "Simple for whom?" -- the design-thinking corollary, reframing
  simplicity claims as redistribution decisions

## Origin Story

Larry Tesler was a computer scientist at Xerox PARC and later Apple,
where he championed user interface simplicity. He formulated the Law of
Conservation of Complexity based on his experience designing the Lisa
and Macintosh interfaces in the early 1980s. Tesler observed that every
attempt to simplify the user's experience required corresponding
complexity in the implementation, and that this tradeoff was inescapable.
The principle was influential in the interaction design community and was
popularized through Dan Saffer's 2009 design writing, which gave it the
name "Tesler's Law." Tesler himself described the insight as arising
from watching users struggle with interfaces: the complexity they
struggled with did not disappear when the interface was redesigned; it
moved to the developer's codebase. Tesler died in 2020, but the law
remains a standard reference in UX design and systems architecture
discussions.

## References

- Saffer, Dan. "The Law of Conservation of Complexity" -- cited in
  *Designing for Interaction* (2009)
- Tesler, Larry. Personal website and interviews documenting the
  principle's origin at Xerox PARC
- Kerr, Dave. "Hacker Laws" -- https://github.com/dwmkerr/hacker-laws
