---
slug: work-in-progress
name: Work in Progress
summary: "Starting work creates ongoing liability; WIP limits apply Little's Law to cut lead time by stopping starts before finishing starts."
kind: metaphor
dead: true
source_frame: manufacturing
applies_to:
  - organizational-behavior
  - creative-process
categories:
  - software-engineering
  - systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
  - kanban
  - continuous-flow
  - just-in-time
  - bottleneck
created: '2026-03-23'
updated: '2026-03-23'
grounding: established
harness: Claude Code
transfers:
  - '[source] WIP in manufacturing is inventory that has entered the production process but has not yet exited as finished goods -- it occupies floor space, ties up capital, and accrues carrying costs while generating zero revenue, importing the frame where started-but-unfinished items are liabilities rather than assets'
  - '[source] WIP accumulates at bottlenecks -- when a downstream station is slower than upstream stations, partially completed items pile up between them, making the constraint visible through physical accumulation, importing the diagnostic insight that WIP concentration reveals system constraints'
  - '[source] reducing WIP reduces lead time (Little''s Law: lead time = WIP / throughput), importing the counterintuitive structural insight that doing fewer things simultaneously makes the whole system faster, not slower'
limits:
  - '[source] breaks because manufacturing WIP is homogeneous and measurable (100 partially assembled widgets are 100 units of WIP), while knowledge-work WIP varies enormously in size, complexity, and completion state -- a half-written novel and a half-debugged function are both "WIP" but share no meaningful unit of measurement'
  - '[source] misleads by framing all WIP as waste to be minimized, when some domains require parallel exploration (research, creative work, early-stage startups) where maintaining multiple incomplete efforts is a deliberate strategy, not a system pathology'
  - '[source] imports a factory-floor spatial metaphor (items physically accumulating between stations) that obscures the invisible WIP of knowledge work -- context-switching costs, cognitive load, and attention fragmentation have no physical analog and are therefore harder to see and manage'
embodied_patterns:
  - flow
  - blockage
  - container
relation_types:
  - cause/accumulate
  - cause/constrain
  - prevent
structure: pipeline
abstraction_level: generic
---

## Transfers

In manufacturing, work in progress (WIP) is the inventory of items that
have entered the production process but have not yet emerged as finished
goods. Raw materials on the loading dock are not WIP. Completed products
in the shipping area are not WIP. WIP is specifically the material that
is between the first and last production step -- partially assembled,
partially processed, in transit between stations. In accounting, WIP
appears on the balance sheet as an asset, but in lean manufacturing, it
is treated as a liability: capital tied up in unfinished goods that
cannot yet be sold.

The term has migrated far beyond manufacturing into software development,
project management, creative work, and personal productivity, where it
now functions as a dead metaphor -- most users of "WIP" in a Jira board
or a knitting circle have no mental image of a factory floor.

Key structural parallels:

- **Started-but-unfinished as a category of cost** -- WIP's fundamental
  insight is that starting something creates an ongoing obligation. An
  unfinished item consumes resources (floor space in a factory, cognitive
  attention in knowledge work, emotional energy in relationships) without
  delivering value. The metaphor makes visible a cost that intuition
  often misses: the assumption that starting more work means more will
  get done. WIP accounting reveals that starting more work often means
  less gets done, because each item competes for the same finite
  processing capacity.

- **Accumulation reveals constraints** -- in a factory, WIP piles up in
  front of the slowest station. If the painting booth processes 10 units
  per hour and the assembly line feeds it 15, a growing pile of
  unpainted assemblies forms at the booth entrance. The pile is a
  diagnostic signal: it tells you where the bottleneck is. This
  transfers to software teams (a growing "In Review" column means code
  review is the constraint), to publishing (a growing manuscript backlog
  means editorial is the constraint), and to any system where work flows
  through sequential stages.

- **Little's Law as structural insight** -- the relationship between WIP,
  throughput, and lead time is captured by Little's Law (John Little,
  1961): average lead time equals average WIP divided by average
  throughput. This means that if throughput is constant, reducing WIP
  directly reduces lead time. The counterintuitive implication: doing
  fewer things at once makes each thing finish faster. This is the
  structural insight that kanban systems, WIP limits, and "stop starting,
  start finishing" slogans all derive from.

- **WIP as hidden inventory** -- in manufacturing, WIP is physically
  visible. You can see it piling up on the factory floor. But in
  knowledge work, WIP is invisible: it exists as open browser tabs,
  unfinished documents, half-read books, partially planned projects,
  and unresolved decisions. The migration of WIP from manufacturing to
  knowledge work has been only partially successful because the
  diagnostic power of physical accumulation is lost. Kanban boards
  attempt to restore visibility by making knowledge-work WIP spatially
  explicit.

## Limits

- **Knowledge-work WIP is not measurable in uniform units** -- factory
  WIP can be counted: 47 partially assembled engines. Knowledge-work
  WIP resists quantification. A half-finished feature, a half-written
  proposal, and a half-resolved architectural decision are all "WIP"
  but have no common unit. Treating them as interchangeable items on
  a kanban board imports a false homogeneity from manufacturing.

- **Some WIP is strategic, not pathological** -- the lean manufacturing
  frame treats all WIP as waste to be minimized. But in research,
  creative work, and early-stage product development, maintaining
  multiple incomplete efforts is often deliberate. A researcher with
  five half-formed hypotheses is not suffering from poor flow; they
  are exploring a possibility space. An artist with three unfinished
  paintings is not blocked at a bottleneck; they are allowing ideas
  to cross-pollinate. The WIP-as-waste frame can be actively harmful
  in these domains, pressuring premature closure.

- **Context-switching costs are invisible** -- manufacturing WIP has a
  visible spatial cost (floor space) but minimal cognitive cost. A
  factory worker can walk past a pile of unfinished parts without
  mental distraction. Knowledge-work WIP imposes a cognitive cost
  that has no manufacturing analog: each open task consumes attention,
  generates anxiety, and degrades performance on the current task
  (Zeigarnik effect). The manufacturing metaphor captures the
  inventory cost but misses the cognitive cost, which in knowledge
  work is often the dominant expense.

- **WIP limits assume defined process stages** -- in a factory, the
  production stages are physically distinct stations with clear
  handoffs. In knowledge work, stages blur: is a feature "in
  development" when the developer is thinking about it in the shower?
  Is a decision "in review" when the reviewer has read the document
  but not yet formed an opinion? The manufacturing metaphor's clean
  stage boundaries do not transfer well to fluid, cognitive processes.

## Expressions

- "WIP" -- the abbreviation, universally used in software and project
  management, now functioning as an independent term disconnected from
  its expansion
- "WIP limit" -- a maximum number of items allowed in a given process
  stage, derived from kanban's card-count constraints
- "Too much WIP" -- the diagnosis, used when a team or individual has
  started more tasks than they can complete efficiently
- "Work in progress, not work in perfection" -- the self-compassion
  variant, reframing the manufacturing term as permission to be
  incomplete
- "WIP it" -- informal verb meaning to mark something as work in
  progress, used in pull request titles ("WIP: refactor auth module")
- "Stop starting, start finishing" -- the kanban community slogan that
  encodes the WIP-reduction insight from Little's Law
- "I'm a work in progress" -- the personal-development usage, meaning
  "I acknowledge my flaws and am improving," which inverts the
  manufacturing frame by treating WIP as a positive state

## Origin Story

The term "work in progress" originates in cost accounting and
manufacturing management, where it designates a specific balance-sheet
category: goods that have begun but not completed the manufacturing
process. The abbreviation "WIP" became standard in operations management
by the mid-20th century.

The term gained new prominence through the Toyota Production System in
the 1950s-70s, where reducing WIP was a core principle. Taiichi Ohno
treated WIP as the enemy: excess WIP hid problems, slowed flow, and
tied up capital. The kanban system was specifically designed to limit
WIP by making it physically impossible to start work without a card
authorizing it.

David Anderson's adaptation of kanban for software development (2010)
brought WIP and WIP limits into mainstream software vocabulary. The
term subsequently migrated into personal productivity (Getting Things
Done, bullet journaling), creative practice (writers and artists
tracking their WIP count), and even self-help ("I'm a work in
progress"), where it has lost all connection to its manufacturing
origins.

## References

- Hopp, W. and Spearman, M. *Factory Physics* (3rd ed., 2008) --
  definitive treatment of WIP, throughput, and Little's Law in
  manufacturing systems
- Ohno, T. *Toyota Production System: Beyond Large-Scale Production*
  (1988) -- WIP reduction as a core lean principle
- Anderson, D. *Kanban: Successful Evolutionary Change for Your
  Technology Business* (2010) -- WIP limits in software development
- Little, J.D.C. "A Proof for the Queuing Formula: L = lambda W" (1961)
  -- the theorem that formalizes the WIP-lead time relationship
