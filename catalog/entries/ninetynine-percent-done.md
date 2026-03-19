---
slug: ninetynine-percent-done
name: Ninety-Nine Percent Done
kind: mental-model
source_frame: mathematical-estimation
categories:
- software-engineering
- mathematics-and-logic
author: agent:metaphorex-miner
contributors: []
related:
- spherical-cow
- accidental-complexity
created: '2026-03-19'
updated: '2026-03-19'
grounding: folk
harness: Claude Code
provenance: mathematical-folklore
transfers:
  - '[model] reveals that progress reporting conflates proportional completion with proportional effort, since the mapping from percentage-complete to percentage-of-effort-remaining is nonlinear and typically convex'
  - '[model] identifies a systematic bias in estimation: early tasks produce visible output that inflates the perceived completion rate, while late tasks (integration, edge cases, testing) consume disproportionate effort with minimal visible change'
  - '[model] reframes "almost done" as an unreliable signal by showing that the last reported 10% routinely contains as much or more work as the first reported 90%'
limits:
  - '[model] breaks when applied to genuinely linear processes (manufacturing runs, rote data entry, physical construction with known materials) where proportional completion does track proportional effort'
  - '[model] can become a self-fulfilling prophecy: teams that internalize "the last 10% takes 90% of the effort" may stop investing in estimation improvement, treating nonlinear cost curves as inevitable rather than symptomatic of poor decomposition'
---

## Transfers

Tom Cargill's aphorism -- "The first 90% of the code accounts for
the first 90% of the development time. The remaining 10% of the
code accounts for the other 90% of the development time" -- encodes
a structural observation about nonlinear effort distribution in
creative and engineering work. The joke's arithmetic is deliberately
impossible (180% of the time), which is the point: progress
reporting deceives because it measures the wrong thing.

Key structural parallels:

- **Progress metrics measure output, not remaining effort** -- when
  a developer says "I'm 90% done," they typically mean "90% of the
  visible functionality exists." But the remaining 10% of
  functionality often includes error handling, edge cases,
  performance tuning, integration testing, documentation, and
  deployment configuration -- work that is invisible to demos but
  dominates the schedule. The model names the systematic gap between
  "fraction of features implemented" and "fraction of total work
  completed." This transfers to any domain where early work produces
  visible artifacts and late work is invisible: writing (the first
  draft comes fast; editing takes forever), research (data collection
  is tangible; analysis is not), construction (framing is fast;
  finish work is slow).

- **The nonlinearity is structural, not accidental** -- Cargill's
  joke is not about bad developers or poor planning. It reflects a
  genuine property of complex systems: the easy parts are done first
  (because they are easy), and the hard parts are left for last
  (because they depend on the easy parts, or because their difficulty
  is only apparent once the easy parts exist). This is a selection
  effect: any rational sequencing puts low-risk, high-visibility work
  first, which means progress curves are inherently front-loaded.

- **The estimate stalls near completion** -- the most damaging
  consequence is the "90% done for weeks" phenomenon, where a
  project reports 90% completion and then stays at 90% for longer
  than the first 90% took. The model explains why: the remaining
  work was never 10% of the total effort. It was always 50% or more,
  but the progress metric couldn't see it. This transfers to
  organizational planning: any roadmap that shows a project
  "nearly complete" should be treated with extreme skepticism unless
  the remaining work has been independently estimated.

- **The 90% threshold is where estimation breaks down** -- early in
  a project, estimates are calibrated against visible work. Late in
  a project, the remaining work is precisely the work that resisted
  estimation: the integration bugs, the performance cliffs, the
  requirements that only become clear when the system is nearly
  assembled. The model identifies 90% completion as a cognitive
  hazard: the point at which confidence is highest and accuracy is
  lowest.

## Limits

- **The model does not apply to linear processes** -- assembly
  lines, batch processing, data entry, and physical construction
  with known materials often have genuinely linear effort
  distributions. 90% of the widgets assembled means approximately
  90% of the effort expended. Applying the 90/90 heuristic to
  these domains produces unnecessary pessimism. The model is
  specific to creative, design, and integration work where late
  tasks interact with early decisions.

- **Treating nonlinearity as inevitable discourages better
  estimation** -- if teams internalize "the last 10% always takes
  as long as the first 90%," they may stop trying to estimate
  accurately and instead simply double all schedules. This is
  pragmatically useful but intellectually lazy: the nonlinearity
  is partly a consequence of poor decomposition, deferred risk,
  and inadequate integration testing. Better engineering practices
  (continuous integration, test-driven development, incremental
  delivery) can genuinely reduce the nonlinearity, and the model
  can discourage investment in those practices by presenting the
  problem as structural rather than addressable.

- **The joke conflates all sources of delay** -- Cargill's aphorism
  lumps together genuinely hard technical work (integration,
  performance tuning), organizational friction (approvals, context
  switching), and scope creep (requirements discovered late). These
  have different causes and different solutions. Treating them as a
  single phenomenon -- "the last 10%" -- can misdirect effort toward
  the wrong root cause.

- **The model assumes a single delivery moment** -- the 90/90 rule
  imagines a project that is "done" at one point in time. Iterative
  delivery (shipping increments, deploying continuously) partially
  dissolves the problem by redefining "done" as a series of smaller
  completions. The model is most dangerous in waterfall-style
  planning where a single completion date is promised.

## Expressions

- "The last 10% takes 90% of the time" -- the canonical form of
  Cargill's aphorism
- "We're almost done" -- the warning signal that triggers the
  model; veteran managers hear it as "we have no idea how much is
  left"
- "90% done for three weeks" -- the empirical evidence that
  validates the model in retrospectives
- "The long tail of completion" -- a more formal name for the
  same phenomenon in project management
- "It's just polish" -- the dismissive label for the remaining
  work that turns out to be 50% of the total effort
- "Integration hell" -- the specific form of last-10% work that
  occurs when separately developed components must work together

## Origin Story

Tom Cargill, a researcher at Bell Labs, originated the aphorism,
which was popularized by Jon Bentley in his "Programming Pearls"
column in *Communications of the ACM* during the 1980s. The joke
entered common usage in software engineering and project management,
where it is cited so frequently that most practitioners know it
without attribution.

The observation predates software. Frederick Brooks noted the same
nonlinearity in *The Mythical Man-Month* (1975): projects that
appear to be on schedule until the final integration phase, when
they suddenly fall months behind. The 90/90 formulation gave the
phenomenon a memorable, quotable form that spread through engineering
culture as folk wisdom.

## References

- Bentley, Jon. "Programming Pearls," *Communications of the ACM*
  (1985) -- where Cargill's aphorism was widely published
- Brooks, Frederick. *The Mythical Man-Month* (1975) -- the
  nonlinear effort curve in software project management
- McConnell, Steve. *Software Estimation: Demystifying the Black Art*
  (2006) -- systematic treatment of estimation bias in software
