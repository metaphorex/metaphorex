---
slug: all-day
name: All Day
summary: "The expeditor's running total across all active tickets. Aggregates demand to enable batching, but only works for homogeneous items at earshot scale."
kind: metaphor
source_frame: food-and-cooking
applies_to:
  - organizational-behavior
categories:
  - systems-thinking
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - mise-en-place
  - a-la-minute
  - in-the-weeds
dead: false
embodied_patterns:
  - part-whole
  - scale
  - flow
relation_types:
  - accumulate
  - coordinate
  - select
structure: pipeline
abstraction_level: specific
created: '2026-03-19'
updated: '2026-03-19'
grounding: folk
harness: Claude Code
transfers:
  - '[source] the call aggregates demand across all active tickets into a single running total ("I need six salmon all day"), forcing the cook to think in terms of total capacity rather than sequential orders, mapping the shift from per-request to system-level resource planning'
  - '[source] the count is shouted and updated in real time as new tickets arrive and dishes are completed, making demand visible and audible to the entire line rather than trapped in individual order slips'
  - '[source] "all day" abstracts away the identity of individual orders to surface the total workload on a single station, enabling the cook to batch, sequence, and prioritize based on aggregate load rather than arrival order'
limits:
  - '[source] breaks because kitchen all-day counts track a single homogeneous item (six salmon, four risotto), while most organizational and software resource planning must aggregate across heterogeneous work items that consume different amounts of capacity -- "twelve tickets all day" is meaningless if three are trivial and one will take all afternoon'
  - '[source] misleads by implying that real-time shouted totals scale beyond the kitchen, when in practice the technique depends on a small team in earshot with shared context about what each item means -- the mechanism does not survive the transition to distributed teams or asynchronous communication'
---

## Transfers

In professional kitchen communication, "all day" is the running total
of a particular item across all active orders. When the expeditor
calls "six salmon all day," they are telling the fish station that
six portions of salmon are needed across all current tickets -- not
six on one order, but six total. The call strips away per-ticket
detail to surface the aggregate demand on a station.

Key structural parallels:

- **Aggregate versus per-ticket thinking** -- the core structural
  move of "all day" is abstraction upward. A cook receiving individual
  tickets sees a sequence of isolated orders: two salmon here, one
  there, three on that six-top. The "all day" call forces a shift to
  system-level thinking: how many total salmon must I produce in the
  next fifteen minutes? This maps directly onto the difference between
  task-level and capacity-level planning. A developer working through
  a sprint backlog ticket by ticket may not realize that seven of the
  twelve tickets require database migrations until someone calls the
  "all day" count for that resource.

- **Real-time demand visibility** -- the call is shouted across the
  kitchen and updated continuously as new tickets arrive and dishes
  leave the pass. The information is ambient, shared, and current.
  This contrasts with systems where demand data is trapped in
  individual queues, dashboards that nobody watches, or status
  reports compiled after the fact. The "all day" model says: make
  total demand visible, audible, and updated in real time, not
  aggregated after the service is over.

- **Enabling batching and sequencing** -- knowing the all-day count
  allows the cook to make production decisions that per-ticket
  thinking cannot support. If six salmon are needed in the next ten
  minutes, it may be more efficient to fire all six together than
  to cook them in three batches of two as each ticket arrives. The
  aggregate view reveals batching opportunities that the sequential
  view hides. In software operations, this maps to batching
  deployments, combining database migrations, or scheduling related
  infrastructure changes together rather than executing them as
  isolated tasks.

- **Abstracting away identity** -- the "all day" count deliberately
  discards information about which ticket each item belongs to. This
  is a feature, not a bug: the fish cook does not need to know that
  two salmon are for table 12 and four are for table 7. They need
  to know the total. The abstraction maps onto any system where
  individual request identity is less important than aggregate
  resource demand -- load balancers, capacity planners, and
  scheduling algorithms all benefit from thinking in totals rather
  than individual transactions.

## Limits

- **Homogeneity assumption** -- "all day" works because the items
  being counted are identical. Six salmon all day means six of the
  same preparation. In most organizational contexts, work items are
  not homogeneous. "Twelve tickets all day" is uninformative if the
  tickets vary wildly in complexity, required skills, and resource
  consumption. The metaphor imports a false equivalence between
  units that the kitchen enforces (through standardized recipes) but
  that other domains do not.

- **Small-team, co-located constraint** -- the call works because a
  professional kitchen is a small team in a shared physical space
  with real-time verbal communication. The expeditor can shout and
  every station hears immediately. This mechanism does not survive
  distribution: remote teams, asynchronous communication, or
  organizations with hundreds of contributors. The "all day" model
  is a broadcast protocol for small groups, not a scalable
  information architecture.

- **Snapshot fragility** -- the all-day count is accurate at the
  moment it is called and begins degrading immediately as new tickets
  arrive and completed dishes leave. In the kitchen, this works
  because the cycle time is minutes and the next call is seconds
  away. In domains with longer cycle times (sprints, quarters,
  fiscal years), the all-day equivalent becomes stale before it can
  be acted upon, and the effort of continuously updating it may
  exceed its informational value.

- **Aggregation hides priority** -- by collapsing individual orders
  into a total, "all day" erases the temporal and priority
  information attached to each order. The cook knows six salmon are
  needed but not which ones are urgent (the ticket that has been
  waiting) and which have just arrived. In contexts where priority
  differentiation matters more than total count -- triage, incident
  response, customer escalations -- the aggregation actively
  degrades decision quality.

## Expressions

- "How many all day?" -- requesting the total count of a resource
  or work item across all active work streams
- "Six deploys all day" -- applying kitchen terminology to release
  management, counting total deployments planned across teams
- "What's our all-day count on bugs?" -- aggregating defect load
  across a team or sprint
- "I need an all-day number before I can plan" -- requesting
  aggregate demand data before making resource allocation decisions
- "Heard, six all day" -- the acknowledgment protocol, confirming
  receipt of the aggregate count

## Origin Story

"All day" is standard kitchen brigade terminology, transmitted
through professional culinary training and the apprenticeship
tradition. It appears in culinary school curricula (Culinary
Institute of America, Le Cordon Bleu) and in popular accounts of
professional kitchen life, most notably Anthony Bourdain's *Kitchen
Confidential* (2000), which introduced a wide audience to the
communication protocols of the professional line.

The term's migration into technology and operations language is
informal and recent, driven by the broader adoption of kitchen
metaphors into agile and lean discourse. Dan Charnas's *Work Clean*
(2016) explicitly treats kitchen communication protocols as models
for knowledge work coordination. The "all day" concept also appears
implicitly in capacity planning literature: the practice of summing
demand across work streams before allocating resources is the same
cognitive operation the expeditor performs when calling the all-day
count.

## References

- Bourdain, A. *Kitchen Confidential: Adventures in the Culinary
  Underbelly* (2000) -- popularized kitchen communication protocols
- Charnas, D. *Work Clean: The Life-Changing Power of Mise-en-Place*
  (2016) -- explicit bridge between kitchen systems and knowledge work
- Culinary Institute of America, *The Professional Chef*, current
  edition -- standard reference for kitchen terminology
- Ruhlman, M. *The Soul of a Chef* (2001) -- kitchen culture and
  communication under pressure
