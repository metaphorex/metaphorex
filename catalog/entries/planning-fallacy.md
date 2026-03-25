---
slug: planning-fallacy
name: Planning Fallacy
summary: "Models systematic underestimation of time, cost, and risk caused by scenario-based inside-view thinking over base-rate data"
kind: mental-model
categories:
- decision-making
- psychology
author: agent:metaphorex-miner
contributors: []
related:
- hofstadters-law
- dont-count-your-chickens-before-they-hatch
- sunk-cost-fallacy
- analysis-paralysis
- optimism-bias
created: '2026-03-21'
updated: '2026-03-21'
grounding: proven
harness: Claude Code
embodied_patterns:
  - near-far
  - path
  - scale
relation_types:
  - cause
  - prevent
structure: cycle
abstraction_level: generic
transfers:
  - '[law] plans are constructed from an "inside view" that simulates the specific scenario, systematically neglecting base-rate data about how similar projects actually performed'
  - '[law] the bias is asymmetric: people underestimate time, cost, and risk while overestimating benefits, producing plans that are optimistic on every dimension simultaneously'
  - '[law] experience does not correct the bias because each new project feels unique, triggering scenario-based thinking rather than reference-class reasoning'
limits:
  - '[law] breaks because not all optimistic estimates are fallacious -- novel projects genuinely lack reference classes, and treating all ambitious timelines as planning fallacy discourages legitimate innovation'
  - '[law] misleads because the prescribed cure (use base rates) assumes comparable reference classes exist, but many projects are sufficiently novel that historical data is irrelevant or misleading'
---

## Transfers

The systematic tendency to underestimate the time, cost, and risk of
future actions while overestimating their benefits. Identified by
Kahneman and Tversky in 1979, the planning fallacy is one of the most
robust findings in behavioral economics, replicated across individuals,
organizations, and governments.

Key structural parallels:

- **Inside view vs. outside view** -- the core mechanism. When planning,
  people construct a mental simulation of the specific project: its unique
  features, the steps required, the resources available. This "inside view"
  is vivid and detailed but systematically incomplete. The "outside view"
  asks: "How long do projects like this actually take?" The planning fallacy
  is the dominance of the inside view over the outside view. Kahneman
  found that even when people know the base rates, they privilege their
  scenario-specific simulation.
- **Asymmetric optimism** -- the bias is not random noise. It is
  consistently one-directional: people estimate too little time, too
  little money, too few complications, and too much benefit. The Sydney
  Opera House was estimated at $7 million and four years; it cost $102
  million and took sixteen years. This asymmetry means that aggregating
  many planned-with-the-inside-view projects produces a systematic budget
  shortfall, not a balanced distribution of wins and losses.
- **Scenario thinking suppresses base rates** -- when asked to estimate
  how long a task will take, people imagine the steps and sum them.
  This produces a best-case timeline (everything goes as planned, no
  interruptions, no surprises). They rarely ask "How long did this take
  last time?" because each project feels unique. The fallacy is
  structural: the way humans plan (simulate forward) is incompatible
  with accurate prediction (look backward at similar cases).
- **Immunity to experience** -- the most striking feature. People who
  have repeatedly experienced their plans running over budget and over
  time do not correct their future estimates. Each new project triggers
  fresh scenario-based thinking. "This time is different" is not a
  conscious belief but an automatic feature of the planning process.

## Limits

- **Not all optimism is fallacy** -- some projects succeed ahead of
  schedule and under budget. The model identifies a statistical tendency,
  not a universal law. Treating every ambitious estimate as a planning
  fallacy creates a culture where pessimistic padding is rewarded and
  genuine efficiency is discounted. Hofstadter's Law ("It always takes
  longer than you expect, even when you take into account Hofstadter's
  Law") is witty but not literally true.
- **Reference classes are not always available** -- the prescribed cure
  is reference-class forecasting: find projects similar to yours and use
  their outcomes as your baseline. But for genuinely novel projects (the
  first smartphone, the first mRNA vaccine), no reference class exists.
  The model provides no guidance for planning under true novelty, where
  the inside view may be the only view available.
- **Strategic misrepresentation** -- Bent Flyvbjerg's research shows that
  large infrastructure project overruns are often not cognitive errors but
  deliberate underestimates designed to get projects approved. The
  planning fallacy provides convenient cover: "We weren't lying, we were
  just subject to a well-known cognitive bias." The model cannot
  distinguish honest error from strategic deception.
- **The model encourages padding** -- once an organization learns about
  the planning fallacy, a common response is to add a "contingency buffer"
  to every estimate. This creates Parkinson's Law dynamics: work expands
  to fill the padded estimate. The cure for one bias triggers another.
- **Cultural and institutional variation** -- the planning fallacy was
  primarily studied in Western, individualist contexts. Organizations with
  strong post-mortem cultures, iterative planning processes, or cultural
  norms against face-saving optimism may exhibit the bias less strongly.
  The model treats the bias as universal when it may be partly cultural.

## Expressions

- "How long do you think this will take?" -- the question that triggers
  the inside view
- "This time is different" -- the implicit assumption that makes the
  planning fallacy resistant to experience
- "Reference-class forecasting" -- Kahneman and Flyvbjerg's prescribed
  antidote
- "Hofstadter's Law" -- the recursive version: it always takes longer
  than expected, even accounting for that expectation
- "Best case scenario" -- what most plans actually represent, though they
  are presented as realistic estimates
- "Underpromise and overdeliver" -- the folk counter-strategy, which
  works individually but creates systematic sandbagging when adopted
  organizationally
- "We need to add contingency" -- the organizational response,
  which often overcorrects

## Origin Story

Kahneman and Tversky introduced the planning fallacy in their 1979
paper on intuitive prediction, building on their broader prospect
theory framework. Kahneman later elaborated the inside view / outside
view distinction in collaboration with Dan Lovallo (2003). Bent Flyvbjerg
provided large-scale empirical evidence by analyzing hundreds of
infrastructure projects worldwide, finding systematic cost overruns
averaging 28% for rail projects, 45% for rail tunnels, and 20% for
roads. Kahneman described the planning fallacy as the bias he would
most like to eliminate, noting ruefully that knowing about the bias
did not prevent him from falling victim to it while writing *Thinking,
Fast and Slow* -- the book about cognitive biases itself took years
longer than planned.

## References

- Kahneman, D. & Tversky, A. "Intuitive Prediction: Biases and
  Corrective Procedures" (1979)
- Kahneman, D. & Lovallo, D. "Delusions of Success: How Optimism
  Undermines Executives' Decisions" (HBR, 2003)
- Flyvbjerg, B. "From Nobel Prize to Project Management: Getting Risks
  Right" (Project Management Journal, 2006)
- Kahneman, D. *Thinking, Fast and Slow* (2011), Chapter 23
