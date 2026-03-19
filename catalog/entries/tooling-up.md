---
applies_to:
- software-engineering
- planning-and-preparation
author: agent:metaphorex-miner
categories:
- software-engineering
- organizational-behavior
contributors: []
created: '2026-03-19'
dead: true
harness: Claude Code
kind: metaphor
limits:
- '[source] breaks because sharpening a chisel has a clear endpoint (the edge bites cleanly into end grain), while infrastructure investment in software has no natural stopping point, making "tooling up" a rationalization for indefinite yak-shaving'
- '[source] misleads by implying a sequential phase model (first tool, then cut) when real projects interleave tooling and production, and the best moment to invest in tooling often only becomes apparent mid-project'
- '[source] obscures the social dimension: a carpenter tools up alone at the bench, but organizational tooling-up requires consensus, training, and adoption costs that the solitary-craftsperson metaphor hides'
name: Tooling Up
related:
- yak-shaving
- sharpening-the-saw
slug: tooling-up
source_frame: carpentry
transfers:
- '[source] maps the carpenter''s pre-work ritual of sharpening blades, squaring stock, and building jigs onto the infrastructure investment phase that precedes productive work, framing setup as a skilled activity rather than wasted time'
- '[source] imports the causal logic that dull tools cause poor joints regardless of the carpenter''s skill, transferring the principle that execution quality is bounded by preparation quality'
- '[source] carries the temporal structure of a distinct preparatory phase with a clear transition to production, framing the decision to stop investing in tools and start cutting as a deliberate threshold crossing'
updated: '2026-03-19'
---

## Transfers

Before a carpenter makes the first cut, there is a preparatory phase that
outsiders often mistake for delay: blades are sharpened, stock is squared
and dimensioned, jigs are built for repeated operations, and the workbench
itself is tuned. This is not procrastination. A dull chisel requires more
force, produces rougher surfaces, and is more likely to slip and injure
the worker. A poorly built jig means every subsequent cut introduces
cumulative error. The preparation phase is where quality is determined;
the cutting phase is where it is revealed.

Key structural parallels:

- **Setup as skilled work** -- sharpening a plane blade is itself a
  craft skill. It requires understanding of steel, abrasive grits,
  bevel angles, and the feel of a properly honed edge. When "tooling up"
  transfers to software, it frames CI/CD pipeline configuration,
  development environment setup, linting rules, and test harness
  construction as skilled engineering work, not administrative overhead.
  The metaphor resists the managerial tendency to classify all non-feature
  work as waste.

- **Tool quality bounds output quality** -- a carpenter with a dull
  chisel cannot produce a clean mortise regardless of skill. The chisel
  is the bottleneck. This transfers to software through build systems,
  deployment pipelines, debugging tools, and monitoring infrastructure:
  the quality of the toolchain sets a ceiling on the quality of the
  product. The metaphor argues that investing in tools has multiplicative
  returns because every subsequent operation benefits.

- **The jig as reusable investment** -- a jig is a custom-built fixture
  that guides a tool for a repeated operation: a dovetail jig ensures
  every joint is identical. The software equivalents are templates,
  scaffolding generators, code formatters, and CI pipelines. The jig
  metaphor encodes the principle that the first instance should be
  harder than subsequent ones, because the first instance includes
  the cost of building the jig.

- **The transition from preparation to production** -- in carpentry,
  there is a felt moment when tooling-up ends and cutting begins. The
  bench is set, the blades are sharp, the jigs are tested. The metaphor
  imports this threshold into project planning: "are we still tooling up
  or are we producing?" This framing is useful because it names a phase
  transition that is otherwise invisible in knowledge work.

## Limits

- **Carpentry tooling-up has a natural endpoint; software tooling does
  not** -- a chisel is either sharp or it is not. A workbench is either
  flat or it is not. These have objective termination conditions. Software
  infrastructure investment has no such ceiling: you can always add
  another layer of abstraction, another monitoring tool, another
  configuration option. The metaphor's clean phase boundary becomes a
  license for indefinite preparatory work in domains where "sharp enough"
  is hard to define.

- **The sequential model is often wrong** -- carpentry tooling-up is
  genuinely sequential: you sharpen before you cut. Software development
  is iterative: you discover what tools you need by trying to build the
  thing. Teams that insist on "tooling up" before writing any product
  code often build infrastructure for problems they do not actually have.
  The carpentry metaphor imports a waterfall-like phase structure that
  does not match iterative development.

- **The metaphor is solitary; organizational tooling is collective** --
  a carpenter sharpens their own chisels. When a software team "tools
  up," the cost includes training, documentation, consensus-building,
  and the productivity dip while everyone learns the new system. The
  carpentry metaphor hides these coordination costs by framing
  tooling-up as an individual activity.

- **It conflates maintenance with investment** -- a carpenter sharpens
  the same chisel repeatedly; the tool already exists and just needs
  upkeep. Much of what organizations call "tooling up" is actually
  building new infrastructure from scratch. The metaphor blurs the
  distinction between maintaining existing tools (low risk, known
  returns) and building new ones (high risk, uncertain returns).

## Expressions

- "We need to tool up before we can start" -- justifying infrastructure
  investment before feature work begins
- "Tooling up the CI pipeline" -- applying the carpentry preparation
  metaphor to build system configuration
- "Sharpen the saw" (Covey) -- the self-improvement variant, where the
  worker is both the carpenter and the tool
- "You can't cut with a dull blade" -- folk wisdom encoding the
  tool-quality-bounds-output-quality principle
- "Measure twice, cut once" -- the related carpentry proverb emphasizing
  preparation over speed, often used in software planning contexts
- "Dev tooling" -- the compound term, now so dead that the carpentry
  origin is invisible

## Origin Story

"Tooling up" entered English industrial vocabulary in the early 20th
century, originally referring to the process of equipping a factory with
the specialized machine tools, dies, and fixtures needed to produce a new
product. The phrase carried over from the craft tradition of carpentry and
metalwork, where preparing tools was understood as a distinct and necessary
phase of any project.

In software engineering, the term gained currency in the 1990s and 2000s
as development environments became increasingly complex. The phrase now
covers everything from IDE configuration to CI/CD pipeline setup to
developer experience engineering. The carpentry origin has become almost
entirely invisible -- "tooling" in software contexts rarely evokes
chisels and planes -- making it a thoroughly dead metaphor that still
structures how teams think about the relationship between preparation
and production.

## References

- Krenov, J. *A Cabinetmaker's Notebook* (1976) -- the craft philosophy
  of tool preparation as meditation and discipline
- Schwarz, C. *The Anarchist's Tool Chest* (2011) -- argument that tool
  selection and preparation is the foundation of craft
- Covey, S. *The 7 Habits of Highly Effective People* (1989) -- "Sharpen
  the Saw" as the self-renewal variant
- Forsgren, N. et al. *Accelerate* (2018) -- empirical evidence that
  CI/CD investment (tooling up) predicts software delivery performance
