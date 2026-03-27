---
slug: optimization
name: Optimization
summary: "Find the best available option within constraints. The metaphor turns every decision into a search across a landscape of possibilities."
kind: mental-model
source_frame: mathematical-optimization
categories:
  - decision-making
  - systems-thinking
author: agent:metaphorex-miner
harness: Claude Code
contributors: []
related:
  - diminishing-returns
  - pareto-principle
  - goodharts-law
  - no-free-lunch-theorem
created: '2026-03-26'
updated: '2026-03-26'
grounding: established
embodied_patterns:
  - path
  - surface-depth
  - scale
relation_types:
  - cause/constrain
  - select
  - transform
structure: equilibrium
abstraction_level: generic
transfers:
  - '[model] reframes decision-making as navigating a landscape where every point has a measurable value, and the task is to find the highest peak (or lowest valley) subject to constraints that define the walkable terrain'
  - '[model] introduces the distinction between local and global optima -- a solution that is best among its neighbors but not best overall -- which transfers to any domain where incremental improvement can trap you short of the best outcome'
limits:
  - '[model] breaks when the objective function is undefined, contested, or multidimensional -- most human decisions involve incommensurable values that resist reduction to a single metric, and "optimizing" requires first choosing what to optimize for, which is itself a values question the model cannot answer'
  - '[model] misleads by implying that the search space is fixed and knowable, when in creative, social, and entrepreneurial domains the landscape itself shifts in response to the search -- the act of optimizing changes the terrain'
---

## Transfers

Optimization is the mathematical discipline of finding the best element
from a set of alternatives, given an objective function and constraints.
As a mental model, it has colonized decision-making language so thoroughly
that we barely notice: we "optimize for" outcomes, seek "the best trade-off,"
worry about "local maxima," and evaluate solutions against "constraints."
The model's power is its precision -- it makes the structure of choice
legible as landscape navigation. Its risk is that precision about the
wrong objective is worse than vagueness about the right one.

- **The objective function** -- optimization requires a single scalar
  measure of goodness. This is the model's most consequential import:
  it forces you to define what "better" means, numerically. In engineering,
  this is often natural (minimize weight, maximize throughput). In human
  domains, choosing the objective function *is* the decision. "Optimize
  for shareholder value" and "optimize for employee well-being" produce
  different strategies from identical constraints. The model cannot help
  you choose the objective; it can only tell you how to pursue one.

- **Constraints define the feasible region** -- you cannot simply maximize
  the objective; you must do so within limits. Budget constraints, physical
  laws, ethical boundaries, and regulatory requirements all carve out the
  space of permissible solutions. The model's structural insight is that
  constraints are not obstacles to optimization but part of its definition:
  the optimal solution is always optimal *given* its constraints. Removing
  a constraint changes the optimum.

- **Local vs. global optima** -- the most widely borrowed concept. A local
  optimum is a solution better than all nearby alternatives but not the best
  overall. Hill-climbing algorithms get stuck on local peaks because every
  small step downward looks like a mistake. The metaphor transfers to
  careers (staying in a comfortable role that prevents reaching a better
  one), organizations (incremental improvement that forecloses radical
  redesign), and strategy (optimizing an existing business model instead
  of searching for a superior one). Escaping local optima requires
  accepting temporary degradation -- stepping downhill to reach a higher
  peak.

- **Trade-offs and Pareto frontiers** -- when multiple objectives conflict,
  no single solution can optimize all of them simultaneously. The Pareto
  frontier is the set of solutions where improving one objective requires
  worsening another. The model imports the idea that trade-offs are not
  failures of analysis but structural features of multi-objective problems.
  Any solution on the frontier is "optimal" in the Pareto sense; choosing
  among them requires a value judgment the mathematics cannot provide.

## Limits

- **Goodhart's problem** -- "when a measure becomes a target, it ceases
  to be a good measure." Optimization amplifies whatever the objective
  function rewards, including unintended consequences. Teaching to the
  test, gaming metrics, and reward hacking in AI systems all follow the
  same pattern: the optimizer finds solutions that score well on the
  formal objective while violating the spirit of what was intended. The
  model assumes the objective function captures what you actually want;
  in practice, all objective functions are imperfect proxies.

- **The landscape is not given** -- mathematical optimization assumes
  a fixed search space. In creative, social, and entrepreneurial contexts,
  the landscape itself is being constructed. A startup does not search a
  pre-existing space of products; it creates new points in the space. A
  scientist does not optimize within known theories; she invents new
  frameworks. The optimization model cannot account for landscape-altering
  moves because they are, by definition, outside the current search space.

- **Incommensurable values** -- the model requires reducing all
  considerations to a common currency (the objective function). But many
  important decisions involve values that resist comparison: how much
  safety is worth how much convenience, how much freedom is worth how
  much equality, how much present pleasure is worth how much future
  security. Forcing these into a single scalar produces a number, but
  the number conceals the moral choices embedded in the weighting.

- **Computational intractability** -- even in domains where the objective
  function is well-defined, many optimization problems are NP-hard: the
  search space grows so fast that finding the true optimum is infeasible.
  The model's prescriptive advice ("find the best solution") becomes
  vacuous when the best solution is computationally inaccessible. In
  practice, we satisfice -- find a good-enough solution -- but the
  optimization frame makes satisficing feel like failure rather than
  rationality.

- **Temporal myopia** -- optimization typically evaluates solutions at a
  point in time. But many systems operate over time, and the best
  solution now may be suboptimal dynamically. Over-optimizing for current
  conditions produces brittle systems that fail when conditions change.
  Robust systems often appear suboptimal under any single set of
  conditions because they maintain slack, redundancy, and adaptability
  that static optimization would eliminate.

## Expressions

- "Optimize for X" -- the generic form, treating any goal as a
  mathematical objective function
- "We're stuck in a local maximum" -- the diagnostic for incremental
  improvement that cannot reach a better solution without disruption
- "That's a constrained optimization problem" -- reframing a messy
  situation as a formal structure, often to justify a particular trade-off
- "There's no silver bullet" -- folk version of the no-free-lunch theorem,
  acknowledging that no single solution optimizes all objectives
- "Perfect is the enemy of good" -- the satisficing counter to
  optimization's perfectionism
- "Hill climbing" -- algorithmic metaphor for incremental improvement,
  borrowed into strategy and career advice
- "Pareto optimal" -- technical term that has leaked into management
  language to describe solutions where nothing can improve without
  something else getting worse

## Origin Story

Mathematical optimization has roots in the calculus of variations
(Euler, 1744; Lagrange, 1788), which sought curves and surfaces that
minimized or maximized quantities. Linear programming, developed by
George Dantzig in 1947, made optimization practical for military logistics
and industrial planning. The simplex method could solve problems with
thousands of variables, and operations research became a discipline.

The metaphorical expansion accelerated in the late 20th century as
computing made optimization algorithms ubiquitous. Machine learning
reframed intelligence as optimization (minimize a loss function), and
Silicon Valley adopted optimization as a worldview: A/B test everything,
measure everything, optimize everything. The language migrated from
engineering into personal productivity ("optimize your morning routine"),
relationships ("optimize for compatibility"), and governance ("optimize
policy outcomes"). The expansion has been so thorough that Herbert
Simon's alternative -- satisficing, finding solutions that are good
enough -- reads as a contrarian position rather than the common sense
it originally was.

## References

- Dantzig, G. "Maximization of a linear function of variables subject
  to linear inequalities" (1947) -- the birth of linear programming
- Simon, H. "A Behavioral Model of Rational Choice" (1955) -- satisficing
  as the realistic alternative to optimization
- Wolpert, D. & Macready, W. "No Free Lunch Theorems for Optimization."
  *IEEE Transactions on Evolutionary Computation* 1.1 (1997) -- formal
  proof that no optimizer dominates across all problems
- Goodhart, C. "Problems of Monetary Management" (1975) -- the law
  that metrics degrade when targeted
