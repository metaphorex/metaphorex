---
slug: galls-law
name: "Gall's Law"
kind: conceptual-metaphor
source_frame: natural-selection
target_frame: systems-design
categories:
  - systems-thinking
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - conways-law
---

## What It Brings

A complex system that works is invariably found to have evolved from a
simple system that worked. A complex system designed from scratch never
works and cannot be patched up to make it work. You have to start over
with a working simple system. Gall maps the logic of biological evolution
onto systems design: complexity must be grown, not manufactured.

- **Evolution as design method** -- the core metaphor. Biological
  complexity does not appear fully formed; it accumulates through
  generations of small, tested variations. Each intermediate form must
  be viable. Gall maps this onto engineered systems: a complex system
  must pass through a sequence of simpler working states, each validated
  by actual use. The web began as static HTML pages. Unix began as a
  two-user system on a spare PDP-7. TCP/IP began as a four-node
  experiment. Each grew into enormous complexity, but each started as
  something simple that actually worked.
- **The anti-waterfall insight** -- Gall's Law is a structural argument
  against the waterfall model of system design, where the complete system
  is specified in advance and built to specification. The evolutionary
  metaphor says this cannot work because you cannot predict which
  interactions between components will cause emergent failures. Only
  running the system reveals these interactions, so only iterative
  development -- building, testing, extending -- can navigate the
  complexity landscape. The metaphor reframes the designer as a breeder,
  not an architect.
- **Fitness as the criterion** -- in natural selection, the only test is
  survival in the actual environment. Gall imports this criterion: a
  system is validated not by conformance to specification but by working
  in the real world. The simple system that works has passed the fitness
  test. The complex system designed from scratch has not been tested at
  any intermediate stage and has accumulated untested interactions that
  are overwhelmingly likely to fail. "Working" is the evolutionary
  filter, and you cannot skip it.

## Where It Breaks

- **Evolution has no goal; design does** -- the deepest disanalogy.
  Natural selection is undirected: it has no target phenotype, no
  intended outcome, no roadmap. System design is goal-directed: you know
  what you want the system to do. Gall's Law borrows evolution's
  iterative mechanism but smuggles in teleology that the source domain
  lacks. A designer who "evolves" a system is still steering toward a
  goal; a biological system is not steered at all. This means the
  designer can take shortcuts -- making non-incremental leaps when the
  target is clear -- that natural selection cannot.
- **Some complex systems ARE designed from scratch and work** -- the
  Apollo Guidance Computer, the Boeing 747, the Golden Gate Bridge. These
  were not evolved from simpler working systems; they were designed,
  built, and tested as complete systems (with extensive simulation and
  component testing). Gall's Law holds most strongly for software and
  sociotechnical systems where emergent interactions are hard to predict.
  For systems governed by well-understood physics, comprehensive design
  from specification is possible because the interaction space is
  modelable.
- **"Simple system that worked" is defined in retrospect** -- every
  complex system has a history, and it is always possible to find
  a simpler predecessor and declare it the "simple system that worked."
  This makes the law unfalsifiable: any successful complex system can
  be narrated as having evolved from something simpler, even if the
  evolution was not the cause of the success. The evolutionary narrative
  is imposed after the fact, not tested prospectively.
- **Evolution is wasteful; design cannot afford to be** -- natural
  selection works by producing vast numbers of variations and discarding
  most of them. The process is profligate with resources and time. System
  designers operate under budget and schedule constraints that rule out
  evolutionary exploration at the biological scale. "Evolve your system"
  is only actionable advice if you can afford the many failures that
  evolution requires. Most projects cannot.

## Expressions

- "A complex system that works is invariably found to have evolved from
  a simple system that worked" -- the canonical formulation from
  Systemantics
- "Do a simple thing first" -- the operational version of Gall's Law,
  common in startup culture ("launch early, iterate")
- "Make it work, make it right, make it fast" -- Kent Beck's formulation
  of the iterative principle, structurally aligned with Gall's Law
- "Big bang rewrite" -- the anti-pattern that Gall's Law predicts will
  fail: discarding a working system and replacing it wholesale with a
  designed-from-scratch replacement
- "Minimum viable product" -- the startup methodology that operationalizes
  Gall's Law: build the simplest thing that works, then evolve it
- "Second-system effect" -- Brooks's related observation that the second
  system designed by a team tends to be over-engineered, a specific
  failure mode Gall's Law predicts

## Origin Story

John Gall, a pediatrician and systems theorist, published Systemantics:
How Systems Work and Especially How They Fail in 1975. The book was
written as a satirical taxonomy of system failures, deliberately modeled
on Murphy's Law in tone. Gall derived his principles from observing
failures in healthcare administration, government bureaucracy, and
military logistics -- not from software, which was barely a discipline
at the time.

The software engineering community adopted Gall's Law in the 1990s and
2000s, finding in it a theoretical justification for iterative and agile
development methods. The law gained particular currency in the
microservices and startup communities, where "start simple and evolve"
became a foundational principle. Eric Raymond cited it in The Cathedral
and the Bazaar (1999) as support for the open-source development model.

Gall published two subsequent editions of the book -- Systemantics: The
Underground Text of Systems Lore (1986) and The Systems Bible (2002) --
each expanding the catalog of system pathologies. The law named after him
is the only one that escaped the book into general circulation.

## References

- Gall, J. *Systemantics: How Systems Work and Especially How They
  Fail*, Quadrangle, 1975 -- the original text
- Gall, J. *The Systems Bible*, General Systemantics Press, 2002 --
  the third edition, renamed and expanded
- Raymond, E.S. *The Cathedral and the Bazaar*, O'Reilly, 1999 --
  Gall's Law applied to open-source software development
- Beck, K. *Extreme Programming Explained*, Addison-Wesley, 1999 --
  iterative development as practice, Gall's Law as theory
