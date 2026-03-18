---
slug: kanban
name: Kanban
kind: paradigm
source_frame: manufacturing
applies_to:
  - organizational-behavior
categories:
  - systems-thinking
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - andon
  - poka-yoke
  - heijunka
  - muda-mura-muri
created: '2026-03-18'
updated: '2026-03-18'
grounding: established
harness: Claude Code
transfers:
  - "[paradigm] replaces push-based scheduling (work is assigned based on a plan) with pull-based flow (work is started only when downstream capacity signals readiness), making the consumer of work the authority on when to produce it"
  - "[paradigm] uses physical tokens with strict quantity limits to make work-in-progress visible and bounded, so that overload is structurally impossible rather than merely discouraged"
  - "[paradigm] treats inventory (queued, unfinished work) as a liability rather than an asset, inverting the default assumption that having more work in the pipeline means more will get done"
limits:
  - "[paradigm] breaks when demand is genuinely unpredictable and cannot be smoothed -- pull signals assume a downstream station that knows what it needs next, but in creative, research, or emergency domains the next task is unknowable until the current one completes"
  - "[paradigm] assumes that work items are roughly interchangeable and flow through a repeatable sequence of stations, but knowledge work varies enormously in size, complexity, and routing, making the factory-floor token system a poor fit without significant adaptation"
---

## Transfers

Kanban (Japanese: signboard, visual card) is the pull-based scheduling
system developed at Toyota where physical cards authorize the production
and movement of parts between workstations. A downstream station sends a
kanban card upstream when it needs more parts; the upstream station produces
only what the card authorizes. No card, no production. The system was
inspired by American supermarket restocking: shelves are replenished based
on what customers take, not on a forecast of what they might want.

Key structural parallels:

- **Pull replaces push** -- in traditional manufacturing and project
  management, work is pushed downstream according to a schedule: the plan
  says to produce 500 units today, so 500 units are produced regardless
  of whether downstream stations can process them. Kanban inverts this:
  production happens only when the next station signals capacity. The
  structural insight is that the consumer of work, not the producer, should
  control the rate of production. In software, this maps to teams that pull
  stories from a backlog when they have capacity rather than having stories
  assigned to them by a sprint plan.

- **WIP limits make overload visible** -- the number of kanban cards in
  the system is fixed. This means work-in-progress cannot exceed a
  structural ceiling. When all cards are in circulation, no new work can
  start. The constraint is physical, not managerial -- you literally cannot
  start a task without a card. In software kanban boards (Trello, Jira),
  column WIP limits serve the same function: if the "In Progress" column
  is full, no new work can enter it until something moves to "Done." This
  makes bottlenecks visible immediately -- when a column is perpetually
  full, the constraint is there.

- **Inventory is waste** -- kanban treats queued, unfinished work as a
  liability. Parts sitting between stations are money spent without value
  delivered. The paradigm contradicts the intuition that having a buffer
  of work-in-progress is safe or efficient. In software, this maps to the
  insight that a large backlog of started-but-unfinished features is worse
  than a small number of features completed end-to-end. Inventory hides
  problems, consumes resources (context-switching, memory, coordination),
  and decays in relevance over time.

- **The card is the contract** -- a kanban card carries specific
  information: part number, quantity, source station, destination station.
  It is simultaneously a request, an authorization, and a record. This
  compresses communication overhead by replacing meetings, emails, and
  status reports with a self-documenting physical artifact. In software
  boards, the card (ticket, story) serves the same function: it is the
  single source of truth for what work exists and where it stands.

## Limits

- **Knowledge work is not parts production** -- factory kanban works because
  parts are identical, the process sequence is fixed, and cycle times are
  predictable. Knowledge work -- writing code, designing products, making
  decisions -- varies enormously in size, complexity, and routing. A kanban
  card for "implement authentication" and a card for "fix CSS typo" are
  not interchangeable units flowing through identical stations. Software
  kanban requires significant abstraction from the manufacturing original,
  and the abstraction loses some of the original's precision.

- **Pull assumes knowable demand** -- the supermarket analogy works because
  customers know what they want. The downstream station knows what part it
  needs. In creative, research, or exploratory work, the next task is often
  unknowable until the current one completes. You cannot send a pull signal
  for a discovery you have not yet made. Kanban in these domains tends to
  degrade into a task-tracking board that uses kanban vocabulary without
  kanban mechanics.

- **WIP limits require discipline that boards do not enforce** -- in a
  factory, the physical card constraint is absolute. In software, a "WIP
  limit of 3" on a Jira column is a social agreement that anyone can
  override. The structural enforcement that makes manufacturing kanban
  powerful becomes a suggestion in its software migration, and suggestions
  are routinely ignored under deadline pressure.

- **The board is not the system** -- many organizations adopt kanban boards
  (the visual artifact) without adopting kanban principles (pull-based flow,
  WIP limits, continuous improvement). The board becomes a prettier to-do
  list rather than a flow-control mechanism. This is the most common failure
  mode of kanban adoption in software: the ceremony without the substance.

## Expressions

- "Kanban board" -- a visual board with columns representing workflow
  stages; the dominant expression, used far more often than the underlying
  principles it represents
- "Pull system" -- any process where downstream demand triggers upstream
  production, the core principle abstracted from the physical card system
- "WIP limit" -- a cap on simultaneous work-in-progress, imported directly
  from kanban's card-count constraint into software project management
- "Stop starting, start finishing" -- kanban community slogan encoding the
  anti-inventory principle: reduce WIP rather than starting new work
- "Visualize the flow" -- the first principle of software kanban (David
  Anderson), derived from the andon-board tradition of making work visible
- "Swim lanes" -- horizontal divisions on a kanban board for parallel
  workflows, a software extension not present in the manufacturing original

## Origin Story

Taiichi Ohno developed the kanban system at Toyota in the late 1940s and
1950s, reportedly inspired by a visit to an American supermarket (likely
a Piggly Wiggly). He observed that shelves were restocked based on what
customers removed rather than on a production forecast, and recognized
this as a pull-based replenishment system superior to Toyota's existing
push-based scheduling.

The word "kanban" literally means "signboard" -- the kind hung outside
Japanese shops to indicate what was for sale. At Toyota, it became the
name for the cards that circulated between workstations, each one
authorizing the production or movement of a specific quantity of a
specific part.

Kanban migrated into software development through David J. Anderson's
*Kanban: Successful Evolutionary Change for Your Technology Business*
(2010), which adapted the manufacturing principles for knowledge work.
Anderson's software kanban preserved the core concepts (visualize flow,
limit WIP, manage flow, make policies explicit) while relaxing the
physical-card constraint. The resulting system became one of the two
dominant agile methodologies alongside Scrum, though it is more accurately
described as a flow-management method than a project-management framework.

## References

- Ohno, T. *Toyota Production System: Beyond Large-Scale Production* (1988)
- Shingo, S. *A Study of the Toyota Production System* (1989)
- Anderson, D. *Kanban: Successful Evolutionary Change for Your Technology
  Business* (2010) -- the software kanban adaptation
- Poppendieck, M. and Poppendieck, T. *Lean Software Development* (2003)
