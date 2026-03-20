---
slug: planning-is-prime
name: Planning Is Prime
kind: mental-model
source_frame: food-and-cooking
categories:
  - systems-thinking
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - mise-en-place
  - prep
  - making-first-moves
created: '2026-03-19'
updated: '2026-03-19'
grounding: folk
harness: Claude Code
transfers:
  - '[model] every professional service begins with a planning session that sequences tasks, identifies dependencies, and assigns time blocks, because execution without a plan produces motion without progress'
  - '[model] the plan is not a forecast but a commitment device -- writing down the sequence forces the planner to confront conflicts, resource gaps, and impossible timings before they become crises during service'
  - '[model] planning has a natural saturation point (the "meeze point") beyond which adding more tasks degrades rather than improves execution, and recognizing this limit is itself a planning skill'
limits:
  - '[model] assumes that the work ahead is knowable and sequenceable in advance, which holds for a kitchen producing a fixed menu but fails for knowledge work where tasks emerge, change scope, or reveal dependencies only during execution'
  - '[model] treats planning as a solo activity (one chef plans one station), but most organizational work requires collaborative planning across interdependent teams, where one person''s plan constrains another''s options in ways the kitchen model does not capture'
---

## Transfers

In professional kitchens, the day begins not with cooking but with
planning. Before a single burner is lit, the chef reviews the
reservation book, counts the covers, reads the specials, sequences
the prep list, assigns tasks to stations, and estimates timing for
every dish. Dan Charnas, in *Work Clean*, identifies this as
Principle 1 of mise en place: planning is prime. Not first in
sequence merely, but first in importance. A chef who starts
cooking without planning will spend the service reacting to
emergencies that a ten-minute planning session would have
prevented.

Key structural parallels:

- **Planning is not optional overhead** -- the mental model's core
  claim is that planning is not a luxury that efficient workers
  can skip. It is the foundational act that makes efficient work
  possible. A chef who "saves time" by skipping the morning plan
  will lose that time tenfold during service: missing ingredients
  discovered mid-prep, timing conflicts between dishes, stations
  unprepared for the evening's volume. In software development,
  the equivalent is starting to code before understanding
  requirements, dependencies, and deployment constraints. The
  model argues that the planning session is not overhead subtracted
  from productive time -- it is the mechanism by which productive
  time is created.

- **The plan is a commitment device** -- writing down a sequence
  of tasks is not forecasting; it is committing. The chef who
  writes "butcher lamb at 2:00, reduce stock at 2:30, plate
  garnishes at 3:00" has not predicted the future but has created
  a structure that makes the future manageable. The act of writing
  forces the planner to confront conflicts: can the stock and the
  lamb share the same burner? Is there enough cold storage for
  butchered meat and reduced stock simultaneously? These conflicts
  are invisible in the head but visible on paper. In software, a
  sprint plan or a task board serves the same function: not
  predicting what will happen but creating a structure that makes
  conflicts visible before they become crises.

- **Planning has a saturation point** -- Charnas introduces the
  concept of the "meeze point": the maximum number of tasks a
  person can hold and execute in a given period before quality
  collapses. A chef who plans fifteen prep tasks for a two-hour
  window will execute none of them well. The mental model insists
  that knowing your meeze point -- and planning below it -- is
  itself a critical planning skill. In knowledge work, this maps
  onto the concept of work-in-progress limits: the number of
  concurrent tasks a person or team can sustain before throughput
  degrades. Planning is prime partly because it is the moment
  when WIP limits are enforced.

- **Daily planning, not project planning** -- the model specifies
  daily planning, not quarterly roadmaps or annual strategies. The
  chef plans for today's service with today's ingredients and
  today's staff. Tomorrow's plan will be different because
  tomorrow's conditions will be different. This maps onto daily
  standups, morning reviews, and beginning-of-day task sequencing
  in knowledge work. The model argues that the highest-value
  planning happens at the shortest time horizon, where the
  planner's information is most accurate and the plan's execution
  is most immediate.

- **The plan sequences dependencies** -- a kitchen plan is not a
  flat to-do list. It is a dependency graph: the sauce requires
  the stock, the stock requires the bones, the bones require
  butchering. The plan's value is in surfacing these dependencies
  and sequencing tasks so that no chef waits for another chef's
  output. In software, this is the build order, the migration
  sequence, the deployment pipeline. The mental model insists that
  sequencing -- not just listing -- is the essential act of
  planning.

## Limits

- **The model assumes knowable work** -- a kitchen produces a fixed
  menu. The chef knows exactly which dishes will be ordered (within
  statistical bounds) and exactly how to make each one. Knowledge
  work often lacks this stability: a developer may start a task
  only to discover that the requirements were misunderstood, the
  API has changed, or the problem is harder than estimated. Planning
  under uncertainty requires different tools (spikes, timeboxes,
  iterative refinement) that the kitchen model does not provide.
  The model works best when the work is repeatable and well-
  understood.

- **Solo planning does not scale** -- the model frames planning as
  a personal discipline: one chef, one station, one plan. In
  organizations, most work involves interdependent teams whose
  plans must be coordinated. One team's "plan to deploy Tuesday"
  constrains another team's "plan to migrate Wednesday." The
  kitchen model provides no mechanism for this coordination because
  in a well-run kitchen, the head chef sequences all stations. In
  a decentralized organization, no single planner has that
  authority.

- **Overplanning is a real failure mode** -- the model's emphasis
  on planning as prime can become a license for indefinite
  preparation. A developer who spends three days planning a two-
  day task has not applied the model correctly, but the model
  provides no internal check against this failure. The kitchen
  provides a natural check (service starts at 6 PM whether you
  are ready or not), but knowledge work often lacks a fixed
  service time, allowing planning to expand into procrastination.

- **The meeze point is a personal constant the model cannot
  predict** -- the model introduces the meeze point as a critical
  planning parameter but provides no method for determining it
  other than experience and self-observation. A junior developer
  and a senior developer have very different meeze points, and
  the model offers no way to estimate them in advance. The
  concept is descriptively useful but operationally vague.

## Expressions

- "Plan the work, work the plan" -- the general formulation of
  planning primacy, used across industries
- "Mise en place starts with the list" -- culinary expression for
  the planning discipline that precedes all physical preparation
- "Morning pages" / "daily review" -- knowledge-work adaptations
  of the chef's morning planning ritual
- "Sprint planning" -- Scrum ceremony that institutionalizes
  planning-is-prime for software teams
- "Meeze point" -- Charnas's term for the cognitive saturation
  threshold, the maximum number of concurrent commitments
- "WIP limit" -- Kanban term for the maximum work in progress,
  the organizational version of the meeze point
- "Sequence the dependencies" -- planning language for ordering
  tasks by their prerequisite relationships

## Origin Story

The discipline of daily planning in professional kitchens predates
its formalization. Escoffier's brigade system (1903) implicitly
required planning: the *chef de cuisine* reviewed the menu, assigned
stations, and sequenced prep before service. But the explicit
articulation of planning as the first and most important principle
of mise en place comes from Dan Charnas's *Work Clean* (2016),
where he observed that the most successful chefs -- those who
remained calm during the most chaotic services -- were invariably
the ones who planned most rigorously before service began.

Charnas connected this to the Eisenhower principle ("Plans are
useless, but planning is indispensable") and to David Allen's
*Getting Things Done* (2001), arguing that the culinary tradition
had independently discovered what productivity systems were
teaching knowledge workers: that the act of planning creates
cognitive clarity, surfaces hidden conflicts, and transforms a
mass of undifferentiated obligations into a sequenced, actionable
program.

## References

- Charnas, Dan. *Work Clean: The Life-Changing Power of Mise-en-
  Place to Organize Your Life, Work, and Mind* (2016) -- planning
  is prime as Principle 1
- Allen, David. *Getting Things Done* (2001) -- knowledge-work
  planning methodology with structural parallels
- Escoffier, Auguste. *Le Guide Culinaire* (1903) -- the brigade
  system that implicitly required daily planning
- Anderson, David J. *Kanban* (2010) -- WIP limits as the
  organizational expression of the meeze point
