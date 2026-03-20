---
slug: making-first-moves
name: Making First Moves
kind: mental-model
source_frame: food-and-cooking
categories:
  - organizational-behavior
author: agent:metaphorex-miner
contributors: []
related:
  - mise-en-place
  - just-in-time
  - servant-leadership
provenance: culinary-mise-en-place
created: '2026-03-20'
updated: '2026-03-20'
grounding: folk
harness: Claude Code
transfers:
  - '[model] distinguishes process work (tasks that unblock others) from product work (tasks that produce output), and prioritizes the former because a blocked downstream worker wastes more total time than a slightly delayed upstream one'
  - '[model] reframes urgency: the most important task is not the one closest to completion but the one whose delay will idle the most other people or processes'
  - '[model] imports the kitchen''s temporal logic where stocks must start before sauces, and sauces before plating, so that sequencing errors compound rather than average out'
limits:
  - '[model] assumes a kitchen-like dependency structure where the critical path is known in advance, and breaks in exploratory work where you cannot identify which task will unblock others until you have started'
  - '[model] can justify premature commitment -- starting process work before requirements are clear -- which produces rework that costs more than the idle time it was meant to prevent'
---

## Transfers

Dan Charnas's fourth principle of "Work Clean" (his mise-en-place-derived
productivity system): make first moves. In a professional kitchen, this
means starting the processes that take the longest and that other tasks
depend on. The stock goes on first because the sauce cannot begin until the
stock is ready, and the dish cannot be plated until the sauce is done. A
cook who starts with the quickest, easiest task feels productive but creates
a bottleneck downstream.

Key structural parallels:

- **Process work before product work** -- the cook's first move is not the
  thing that will be served (the plated dish) but the thing that enables
  the thing that will be served (the stock). In software, this maps to
  setting up the CI pipeline before writing features, provisioning the
  staging environment before coding the integration, writing the test
  harness before writing the code it tests. These are first moves: they
  produce no visible output but they unblock everything that follows. The
  model diagnoses a common failure mode where teams optimize for visible
  progress (features shipped) at the expense of enabling work (infrastructure,
  tooling, documentation) and then wonder why everything takes so long.

- **Urgency is relational, not absolute** -- a task's urgency depends not
  on its own deadline but on how many other tasks it blocks. The stock is
  not urgent because it must be done first in wall-clock time; it is urgent
  because every minute it is delayed pushes back every downstream task. The
  model reframes prioritization from "what is due soonest?" to "what will
  idle the most capacity if delayed?" In project management, this is the
  critical-path insight, but the kitchen version is more visceral: you can
  see the downstream cook standing idle, waiting for your output.

- **Sequencing errors compound** -- in a kitchen, starting the wrong thing
  first does not merely delay one dish; it cascades. The stock is late, so
  the sauce is late, so the entree is late, so the entire table waits, so
  the dining room backs up, so the front of house is overwhelmed. Small
  sequencing errors at the top of the dependency chain amplify into large
  delays at the bottom. The model predicts the same in any pipeline:
  starting with low-dependency tasks because they are easy produces a
  false sense of progress that conceals growing bottlenecks.

- **First moves require confidence in the sequence** -- a cook can make
  first moves because the menu is written and the dependency graph is known.
  Stock before sauce before plate is not a guess; it is a fact of culinary
  physics. The model's power depends on knowing the critical path. When the
  sequence is uncertain -- when you do not know which task blocks which --
  the model provides no guidance on what counts as a "first move."

## Limits

- **Requires a known dependency graph** -- the kitchen knows its menu
  before service. The cook can sequence confidently because the recipes
  are fixed and the dependencies are physical (you cannot reduce a sauce
  that does not exist). In exploratory work -- research, design
  exploration, early-stage product development -- the dependency graph is
  unknown. Making first moves requires knowing which tasks are upstream,
  and in genuinely novel work, you often cannot determine that without
  starting. The model applies to execution, not discovery.

- **Premature commitment is its own failure mode** -- eagerness to make
  first moves can push teams to begin process work before requirements are
  stable. Setting up a CI pipeline for a codebase whose architecture is
  still in flux, or provisioning infrastructure before the service contract
  is defined, creates rework that may cost more than the idle time it
  prevented. The model needs a readiness check: is the sequence confident
  enough to justify commitment?

- **The model undervalues learning from quick wins** -- sometimes the
  easiest, fastest task is the right first move, not because it unblocks
  others but because it teaches you something about the problem space. A
  prototype, a spike, a quick experiment -- these are not "first moves" in
  the culinary sense (they do not unblock downstream work) but they may be
  first moves in the epistemic sense (they reduce uncertainty). The
  kitchen model has no concept of this because the kitchen's uncertainty
  is zero by design.

## Expressions

- "Start the stock" -- culinary shorthand for beginning the longest-lead
  process work first
- "What's blocking downstream?" -- the project management translation,
  common in standups and sprint planning
- "Unblock before you build" -- engineering culture advice encoding the
  first-moves principle
- "Critical path first" -- project management jargon for the same insight,
  arrived at through CPM (Critical Path Method) rather than kitchen practice
- "Front-load the long poles" -- program management term for the same
  sequencing discipline

## Origin Story

Dan Charnas codified "Making First Moves" as Principle 4 of his ten
principles of Work Clean in *Work Clean: The Life-Changing Power of
Mise-en-Place to Organize Your Life, Work, and Mind* (2016). He drew
the principle from observing professional chefs, particularly at the
Culinary Institute of America, where the sequencing of prep work is
taught as a foundational skill. The same insight appears independently
in project management as Critical Path Method (CPM), developed by
DuPont and Remington Rand in the late 1950s, and in lean manufacturing
as the identification of bottleneck resources. The kitchen version is
distinctive because the feedback is immediate and visceral: if you
sequence wrong, the chef screams at you in ten minutes, not ten sprints.

## References

- Charnas, D. *Work Clean: The Life-Changing Power of Mise-en-Place to
  Organize Your Life, Work, and Mind* (2016) -- Principle 4
- Goldratt, E. *The Goal: A Process of Ongoing Improvement* (1984) --
  Theory of Constraints and bottleneck identification
- Kelley, J.E. and Walker, M.R. "Critical-Path Planning and Scheduling"
  (1959) -- the formal CPM method
