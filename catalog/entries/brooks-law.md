---
slug: brooks-law
name: "Brooks's Law"
kind: mental-model
categories:
  - software-engineering
  - organizational-behavior
author: agent:metaphorex-miner
contributors: []
related:
  - scaling-is-dilution
  - second-system-effect
  - conways-law
created: '2026-03-23'
updated: '2026-03-23'
grounding: established
harness: Claude Code
transfers:
  - '[law] communication overhead grows as a function of n(n-1)/2 where n is team size, so each additional person adds not one but n new communication channels, producing quadratic cost growth against linear capacity growth'
  - '[law] new members impose a net negative productivity period during which existing members must stop producing to train them, and the later the addition the steeper the ramp because the system they must learn is larger and more implicit'
  - '[law] the law predicts that the break-even point for a late addition may arrive after the deadline, making the addition pure cost within the relevant time horizon even if the person would eventually be productive'
limits:
  - '[law] assumes communication is all-to-all, but real teams partition into sub-teams with limited cross-group interfaces, and architectures that minimize inter-team coordination (microservices, bounded contexts) can reduce the quadratic penalty to something closer to linear'
  - '[law] treats all tasks as having high inter-dependency, but projects with easily partitioned, independent work units (localization, test writing, documentation) can absorb late additions without significant communication overhead'
embodied_patterns:
  - link
  - scale
  - blockage
relation_types:
  - cause/accumulate
  - cause/couple
  - prevent
structure: network
abstraction_level: generic
---

## Transfers

"Adding manpower to a late software project makes it later." Fred Brooks
stated this in *The Mythical Man-Month* (1975), and it remains one of the
few empirical observations about software engineering that practitioners
cite by name fifty years later. The law's persistence reflects a structural
insight that extends well beyond software.

- **Quadratic communication cost** -- the central mechanism is combinatorial.
  A team of 5 has 10 pairwise communication channels. A team of 10 has 45.
  A team of 15 has 105. Each channel represents potential misunderstanding,
  synchronization overhead, and meeting time. Adding a person to a team does
  not add one unit of communication cost; it adds n units, where n is the
  current team size. The law observes that managers who think in terms of
  "person-months" -- treating labor as fungible and additive -- systematically
  underestimate this cost because the person-month model assumes zero
  coordination overhead.

- **The ramp-up tax** -- new team members do not arrive productive. They must
  learn the codebase, the conventions, the implicit decisions, and the social
  dynamics. During ramp-up, they consume the time of existing members who
  must explain, review, and correct. On a late project, this tax is
  particularly severe: the system is larger, less documented (because the
  team has been rushing), and the existing members are already stretched.
  The person added to help becomes a drain on the people who need help.

- **The partitioning problem** -- Brooks observed that not all work is
  divisible. A task that takes one person a month does not take two people
  two weeks if the task has sequential dependencies. Pregnancy is the
  canonical example: nine women cannot produce a baby in one month. Software
  projects contain a mix of parallelizable and sequential work, and late in
  the project the remaining work tends to be the hard, interdependent parts
  that resist partitioning.

- **The mythical man-month** -- the deeper insight is about the unit of
  measurement itself. A "man-month" implies that people and time are
  interchangeable: if a project needs 12 man-months, you can use 12 people
  for 1 month or 1 person for 12 months. Brooks showed this is false for
  any work requiring communication. The unit "man-month" embeds a lie about
  the nature of collaborative work, and planning with it produces schedules
  that are structurally impossible to meet.

## Limits

- **Not all coordination is all-to-all** -- Brooks's quadratic model assumes
  every team member must communicate with every other. Modern software
  organizations deliberately create architectures and team structures that
  reduce this. Conway's Law works in reverse: by designing system boundaries
  to match team boundaries (bounded contexts, microservices with clear APIs),
  organizations can add people to separate modules without imposing
  cross-team communication overhead. The law applies most strongly to
  monolithic systems with tightly coupled teams.

- **Some work is genuinely parallelizable late in a project** -- the law's
  force varies with the nature of remaining work. If the late project needs
  100 screens localized, 500 tests written for well-defined interfaces, or
  documentation updated, these tasks can absorb additional people with
  minimal coordination. Brooks's examples are dominated by deeply
  interdependent design work, where the law holds strongest. Applying it
  to all late additions without checking task independence produces
  unnecessary paralysis.

- **The law does not account for removing people** -- Brooks focuses on
  addition but says little about subtraction. Sometimes a late project is
  late because it has the wrong people, not too few. Replacing an
  unproductive team member or removing a person who generates negative
  coordination value can accelerate a project despite the surface
  contradiction of "reducing resources."

- **Modern tooling has changed the constants** -- Brooks wrote when
  communication meant meetings and memos. Modern tools (version control,
  CI/CD, code review platforms, async communication) reduce the per-channel
  communication cost without eliminating it. The quadratic structure
  remains, but the coefficient is smaller. A team of 15 in 2025 may have
  lower communication overhead than a team of 10 in 1975, though the
  scaling relationship still holds.

## Expressions

- "Adding manpower to a late software project makes it later" -- the
  canonical statement, often shortened to "Brooks's Law"
- "The mythical man-month" -- the title concept: treating person-months
  as fungible units of work
- "Nine women can't make a baby in one month" -- Brooks's most memorable
  illustration of non-parallelizable work
- "Throwing bodies at the problem" -- the management anti-pattern the law
  warns against
- "We need more hands" -- the intuitive but often wrong response to a
  late project, which the law directly refutes

## Origin Story

Fred Brooks drew the law from his experience managing the development of
IBM's OS/360 in the 1960s, one of the largest software projects of its
era. He watched IBM repeatedly add programmers to a project that was falling
behind schedule, and each addition made the schedule slip further. The
project was ultimately delivered a year late with far more defects than
planned. Brooks codified these observations in *The Mythical Man-Month*
(1975), which became one of the most widely read books in software
engineering.

The law's endurance is partly because it names a structural truth (quadratic
communication costs) and partly because the mistake it warns against is
perpetually tempting. Managers who understand Brooks's Law intellectually
still add people to late projects because institutional incentives reward
visible action ("we're adding resources") over structural analysis ("adding
resources will make this worse").

## References

- Brooks, Fred. *The Mythical Man-Month: Essays on Software Engineering*
  (1975, anniversary edition 1995) -- the original statement and analysis
- Brooks, Fred. "No Silver Bullet: Essence and Accidents of Software
  Engineering" (1986) -- related argument about irreducible complexity
