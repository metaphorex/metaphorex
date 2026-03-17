---
slug: pipeline
name: Pipeline
kind: metaphor
dead: true
source_frame: fluid-dynamics
applies_to:
  - systems-performance
categories:
  - linguistics
  - organizational-behavior
author: agent:metaphorex-miner
contributors: []
related:
  - the-pipeline-pattern
  - bottleneck
created: '2026-03-17'
updated: '2026-03-17'
harness: Claude Code
transfers:
  - "[source] fluid flows through a pipe in one direction from source to destination, with each section carrying the same material forward, mapping onto sequential stages that move items (deals, candidates, code) from start to finish"
  - "[source] a pipe has fixed capacity determined by its diameter, and exceeding that capacity causes pressure buildup or rupture, mapping onto process stages with throughput limits that create backlogs when overloaded"
  - "[source] physical pipelines cannot skip sections -- fluid must pass through every segment in order, mapping onto the assumption that pipeline stages are mandatory and sequential"
limits:
  - "[source] breaks because fluid in a pipe cannot reverse direction or exit mid-journey, while items in a business pipeline routinely drop out, loop back to earlier stages, or skip steps -- a sales lead can go cold at any point, which has no hydraulic analogue"
  - "[source] misleads because pipes carry homogeneous fluid (all oil molecules are equivalent), while business pipelines carry heterogeneous items (each candidate, deal, or feature is unique) that require different handling at each stage"
---

## Transfers

A pipe carries fluid from point A to point B. Oil pipelines, water mains,
gas lines -- the physical infrastructure is defined by three properties:
contents flow in one direction, the pipe has a fixed capacity, and what
enters one end must exit the other. The metaphor was adopted across
business and technology because sequential processes look like pipes if
you squint: things go in, things come out, and the stages are connected.

- **Directionality feels like physics** -- fluid flows downhill or under
  pressure. The pipeline metaphor makes sequential processing feel
  inevitable, governed by something like gravity. A sales pipeline flows
  from lead to prospect to qualified opportunity to close. A hiring pipeline
  flows from application to screen to interview to offer. The metaphor
  makes this sequence feel natural rather than designed, which discourages
  questioning whether the stages should exist at all.
- **Capacity constraints become intuitive** -- a pipe can only carry so
  much. When people say "the pipeline is full," they mean the process
  cannot accept more inputs without something backing up or bursting. The
  physical metaphor makes throughput limitations feel like natural law
  rather than organizational choice. This is useful (it legitimizes saying
  "we're at capacity") but also limiting (it implies that capacity is
  fixed, like pipe diameter, rather than expandable through redesign).
- **Stage-to-stage handoff** -- in a physical pipeline, each section
  connects to the next. The metaphor imports the assumption that work
  moves from stage to stage through defined handoff points. This maps
  well onto manufacturing (assembly lines) and poorly onto knowledge work
  (where "stages" overlap, reverse, and blur).

## Limits

- **Pipes don't leak on purpose** -- in a physical pipeline, leakage is a
  failure. In a sales pipeline, attrition at every stage is expected and
  healthy. A pipeline that converts 100% of leads would be suspicious, not
  efficient. The metaphor frames normal attrition as loss, which distorts
  how people evaluate pipeline health. Managers who internalize the pipe
  metaphor tend to see drop-off as a problem to fix rather than a feature
  of qualification.
- **The metaphor hides parallelism** -- a pipe processes fluid serially.
  Real organizational "pipelines" often have multiple items at different
  stages simultaneously, moving at different speeds. This is more like a
  multi-lane highway than a pipe, but the pipeline metaphor suppresses
  the parallel dimension, encouraging batch thinking and stage-gate
  processes that serialize what could be concurrent.
- **"Pipeline problem" reveals the metaphor's politics** -- in diversity
  discourse, "pipeline problem" frames the underrepresentation of certain
  groups as a supply issue: not enough qualified candidates entering the
  pipe. The hydraulic metaphor naturalizes this framing by making it seem
  like physics -- you can't get more out of a pipe than you put in. This
  obscures the possibility that the pipe itself (selection criteria,
  cultural barriers, retention failures) is the problem, not the supply
  of fluid.
- **The dead metaphor has split into two separate dead metaphors** -- in
  business, "pipeline" means a staged process (sales pipeline, talent
  pipeline). In software, "pipeline" means an automated workflow (CI/CD
  pipeline, data pipeline). These are structurally different uses: one
  is about human processes with judgment at each stage, the other is about
  automated sequences without human intervention. The single dead metaphor
  now covers two distinct concepts, creating confusion when the same word
  appears in both contexts.

## Expressions

- "Sales pipeline" -- the sequence from lead generation to closed deal,
  the canonical business usage
- "Talent pipeline" -- the flow of candidates through hiring stages or
  the development of future leaders
- "Pipeline review" -- a meeting to examine deals in progress, where
  managers inspect the contents of the pipe
- "What's in the pipeline?" -- what work is in progress, what's coming
  next
- "Pipeline problem" -- insufficient supply entering the first stage,
  used especially in diversity and workforce planning discussions
- "Fill the pipeline" -- add more inputs to the process, treating deal
  flow or candidate flow as a volume problem
- "The pipeline is broken" -- in CI/CD, the automated workflow has
  failed; in business, the staged process has stalled

## Origin Story

The physical pipeline -- a conduit for transporting oil, gas, or water
over long distances -- became a significant infrastructure technology in
the mid-19th century. The first major oil pipeline was built in
Pennsylvania in 1865, replacing horse-drawn barrel transport. The image
of fluid flowing through connected segments was vivid and well-known by
the early 20th century.

The metaphorical extension to business processes appears to have emerged
in mid-20th century sales management. The "sales pipeline" concept --
tracking prospects through stages from initial contact to closed deal --
was established vocabulary by the 1960s. The metaphor was attractive
because it made an abstract process (persuading someone to buy) feel
concrete and measurable: you could count what was "in the pipe" and
predict what would come out the other end.

The software usage came later. Doug McIlroy's 1964 memo proposing Unix
pipes used explicit plumbing language ("like garden hoses"), and Unix
pipes (1973) made the metaphor literal in code. But the CI/CD "pipeline"
-- Jenkins pipelines, GitHub Actions workflows -- arrived in the 2010s
and borrowed the word without any awareness of its fluid-dynamics origin.
When a developer says "the pipeline failed," they mean a YAML
configuration didn't execute properly. The fluid is gone.

## References

- McIlroy, M.D. "Summary -- Unimplemented Commands" (1964) -- the memo
  that brought pipe metaphor into computing
- Rackham, Neil. *SPIN Selling* (1988) -- early codification of the
  sales pipeline methodology
- Johnson, Stefanie K. "What the 'Pipeline' Problem Gets Wrong About
  Diversity," *Harvard Business Review* (2019) -- critique of the
  pipeline metaphor in diversity discourse
