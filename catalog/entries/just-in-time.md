---
slug: just-in-time
name: "Just-in-Time"
summary: "Produce only what is needed, when needed; treat inventory as a liability that hides problems."
kind: paradigm
source_frame: manufacturing
applies_to:
  - organizational-behavior
categories:
  - systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
  - jidoka
  - kanban
  - continuous-flow
created: '2026-03-18'
updated: '2026-03-18'
grounding: established
harness: Claude Code
transfers:
  - "[paradigm] producing only what the next process needs, when it needs it, in the quantity it needs, treats inventory as a liability that hides problems rather than an asset that buffers against uncertainty"
  - "[paradigm] a pull-based system where downstream demand triggers upstream production inverts the traditional push model and makes overproduction visible as the most fundamental waste"
  - "[paradigm] reducing buffer inventory between process steps exposes hidden problems (machine breakdowns, quality defects, supplier delays) that inventory previously masked, forcing their resolution"
limits:
  - "[paradigm] assumes a stable, predictable demand signal that allows production to be synchronized, which breaks in environments with high demand variability, unpredictable disruptions, or long lead times"
  - "[paradigm] the deliberate removal of buffers that exposes problems also removes the resilience that buffers provide, making the system fragile to disruptions it has not yet learned to prevent"
embodied_patterns:
  - flow
  - balance
  - iteration
relation_types:
  - coordinate
  - prevent
structure: equilibrium
abstraction_level: specific
---

## Transfers

Just-in-time -- produce only what is needed, when it is needed, in the
amount needed -- is the flow pillar of the Toyota Production System,
paired with jidoka as the quality pillar. The principle sounds like
simple common sense, but it encodes a radical inversion: inventory is
not safety, it is danger. Stockpiles do not protect you from problems;
they hide problems from you.

Key structural principles:

- **Inventory is waste** -- conventional manufacturing wisdom treats
  inventory as an asset: buffer stock protects against supply disruptions,
  demand spikes, and production variability. JIT inverts this: inventory
  is the most dangerous form of waste because it conceals the problems
  that necessitate it. A large parts inventory masks unreliable suppliers.
  A queue of work-in-progress masks unbalanced production stages. Excess
  inventory is not a solution; it is a symptom that something upstream
  is broken. Taiichi Ohno compared inventory to water level in a river:
  when the water is high (inventory is large), the rocks (problems) are
  invisible. Lower the water and the rocks appear.
- **Pull, not push** -- traditional production pushes output downstream:
  each station produces as much as it can and passes it forward.
  JIT pulls: each station produces only when the next station signals
  demand. The kanban card is the physical mechanism for this pull signal.
  The structural insight is about information flow: in a push system,
  production decisions are made upstream based on forecasts; in a pull
  system, they are made downstream based on actual consumption. This
  maps to software as event-driven architectures, demand-paged memory,
  and lazy evaluation -- systems that do work only when results are
  actually needed.
- **Small batches expose problems** -- JIT requires small production
  batches and frequent changeovers. Large batches are efficient within
  each production step but create inventory between steps. Small batches
  flow through the system faster, with less work-in-progress and shorter
  feedback loops. When something goes wrong, fewer units are affected.
  This maps to software as continuous delivery, small pull requests, and
  frequent releases: the smaller the batch, the faster the feedback, the
  lower the risk.
- **Synchronization through takt time** -- takt time (from the German
  "Takt," meaning rhythm or meter) is the rate of customer demand:
  available production time divided by customer demand. JIT synchronizes
  every production step to takt time, so the whole system pulses at the
  same rhythm. This maps to capacity planning in services, sprint
  cadences in agile development, and throughput-based scheduling. The
  structural insight: rhythm creates flow, and flow enables quality.

## Limits

- **Fragility by design** -- JIT deliberately removes the buffers that
  provide resilience. When the system works, this is elegant: problems
  surface and get fixed, flow improves, waste decreases. When the system
  is hit by a disruption it has not yet resolved -- a natural disaster,
  a pandemic, a supplier bankruptcy -- the lack of buffer inventory means
  the entire chain stops. The 2011 Tohoku earthquake and the 2020 COVID
  supply chain crisis demonstrated that JIT systems are optimized for
  normal conditions and catastrophically brittle under black swan events.
  The structural trade-off is real: the same inventory reduction that
  exposes small problems amplifies large disruptions.
- **Demand must be stable enough to synchronize** -- JIT assumes that
  customer demand is relatively predictable and that production can be
  leveled (heijunka) to smooth out spikes. In environments with highly
  variable demand -- fashion, entertainment, venture-backed startups --
  the pull signal is too erratic for synchronized production. Software
  teams adopting JIT-inspired practices (no backlog, work only on what
  is needed now) can starve strategic work that has no immediate pull
  signal.
- **The water metaphor misleads about problem severity** -- Ohno's
  river-and-rocks analogy suggests that lowering inventory will reveal
  problems you can then fix. But some "rocks" are not fixable: a sole-
  source supplier with a six-month lead time, a regulatory constraint,
  a seasonal demand spike. Removing the buffer does not fix these
  problems; it just makes the system vulnerable to them. The metaphor
  works for problems caused by insufficient discipline (the Toyota
  context); it fails for problems caused by structural constraints
  outside the organization's control.
- **JIT assumes the whole chain participates** -- the system works when
  every link in the supply chain operates on pull signals. When Toyota
  operates JIT but its suppliers stockpile inventory "just in case,"
  the waste has not been eliminated -- it has been pushed upstream to
  suppliers with less bargaining power. The paradigm can optimize one
  organization's flow at the cost of the whole chain, which is the
  opposite of its stated systems-thinking philosophy.
- **Knowledge work has invisible inventory** -- in manufacturing,
  inventory is physical and countable. In knowledge work, inventory
  takes invisible forms: half-finished designs, unreviewed documents,
  open tasks in a project management tool, context in someone's head
  that has not been shared. JIT's core mechanism (make inventory visible,
  then reduce it) is harder to apply when the inventory is cognitive
  rather than physical.

## Expressions

- "Just in time" -- so widely adopted that it is used colloquially for
  anything that arrives precisely when needed, entirely detached from
  its manufacturing origin
- "JIT compilation" -- a compiler that translates code to machine
  instructions only when needed for execution, directly borrowing the
  temporal principle
- "Pull system" vs. "push system" -- the fundamental JIT distinction,
  migrated to project management (pull-based kanban boards vs. push-based
  assignment), marketing (inbound vs. outbound), and supply chain design
- "Lowering the water level" -- Ohno's river-and-rocks metaphor for
  reducing inventory to expose problems, a metaphor within the paradigm
- "Zero inventory" -- the aspirational extreme of JIT, used both
  literally (in manufacturing) and metaphorically (in agile: "no backlog")
- "Lean" -- the broader management philosophy derived from TPS, where JIT
  is the central operational principle

## Origin Story

Just-in-time has a disputed origin. The most common narrative attributes
it to Taiichi Ohno, who developed the system at Toyota in the 1950s and
1960s, reportedly inspired by American supermarkets: shelves are
restocked only when customers take items, pulling inventory forward
rather than pushing it from the warehouse. Ohno saw that the supermarket
model inverted the conventional factory logic, and he spent two decades
adapting the principle to automotive production.

The term "just in time" was likely coined by Toyota's own management,
though some trace it to Kiichiro Toyoda (founder of Toyota Motor
Corporation) in the 1930s. Ohno gives Kiichiro credit in *Toyota
Production System* (1988), noting that Kiichiro articulated the ideal
of having parts arrive exactly when needed, though the full system
required decades of development.

JIT entered Western manufacturing vocabulary through the Japanese
industrial miracle of the 1970s and 1980s. As American manufacturers
lost market share to Toyota, consultants and academics studied TPS and
brought its concepts back. Richard Schonberger's *Japanese Manufacturing
Techniques* (1982) and Womack, Jones, and Roos's *The Machine That
Changed the World* (1990) popularized JIT in the English-speaking world.
The term migrated to software through JIT compilation (first implemented
in the 1960s but named retrospectively using the manufacturing term)
and to general management through lean methodology.

The "house of TPS" places JIT and jidoka as the two pillars supporting
the roof of customer satisfaction, with heijunka and standardized work
as the foundation. The house metaphor makes the point visually: neither
pillar stands alone. JIT without jidoka produces defects faster. Jidoka
without JIT creates quality without flow.

## References

- Ohno, T. *Toyota Production System: Beyond Large-Scale Production*
  (1988) -- the canonical text, with the supermarket analogy and
  river-and-rocks metaphor
- Womack, J., Jones, D. & Roos, D. *The Machine That Changed the World*
  (1990) -- brought TPS/JIT to a Western audience
- Schonberger, R. *Japanese Manufacturing Techniques* (1982) -- early
  Western documentation of JIT
- Lean Enterprise Institute. "Just-in-Time" lexicon entry --
  https://www.lean.org/lexicon-terms/just-in-time/
- Shingo, S. *A Study of the Toyota Production System* (1989) -- detailed
  engineering perspective on JIT mechanisms
