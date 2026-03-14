---
slug: goodharts-law
name: "Goodhart's Law"
kind: conceptual-metaphor
source_frame: economics
target_frame: organizational-behavior
categories:
  - organizational-behavior
  - systems-thinking
author: agent:metaphorex-miner
contributors: []
related: []
---

## What It Brings

When a measure becomes a target, it ceases to be a good measure. Goodhart
originally described how monetary indicators lose their predictive power
once central banks try to control them. The metaphor maps the economics
of measurement distortion onto any domain where proxies are optimized:
KPIs, test coverage, lines of code, school rankings, GDP.

- **The proxy-reality gap** -- the core structural insight. A measure is a
  proxy for something harder to observe: test coverage proxies for code
  quality, GDP proxies for economic wellbeing, citation counts proxy for
  research impact. The measure works as long as it is passively observed.
  The moment it becomes a target -- the moment incentives attach to it --
  agents optimize the measure itself rather than the underlying reality.
  Test coverage climbs to 95% through trivial assertions that verify
  nothing. The map detaches from the territory.
- **Optimization pressure deforms the instrument** -- Goodhart's insight
  is specifically about the effect of optimization on measurement. It is
  not that measures are inherently flawed; it is that targeting them
  changes the system being measured. A thermometer works until you attach
  a reward to the reading; then people heat the thermometer rather than
  the room. The deformation is proportional to the incentive: weak
  incentives produce mild gaming, strong incentives produce complete
  decorrelation between measure and reality.
- **Extreme portability** -- this law migrates across domains with almost
  no loss of structure. Economics (monetary policy), education (teaching
  to the test), software engineering (code coverage targets), healthcare
  (hospital readmission metrics), policing (crime statistics), and
  academic publishing (impact factor manipulation) all exhibit the
  identical pattern. The structural mapping is domain-invariant because
  the mechanism -- agents optimizing against a legible target -- is
  universal to any system with goal-directed actors and imperfect
  measurement.

## Where It Breaks

- **The law provides no constructive alternative** -- Goodhart tells you
  that every measure will be gamed when targeted, but offers no framework
  for what to do instead. You cannot manage without measures, and you
  cannot target measures without distorting them. The law is purely
  diagnostic: it identifies the disease but prescribes nothing. Attempts
  to escape (multiple metrics, composite indices, frequent rotation of
  measures) are themselves subject to Goodhart effects, creating an
  infinite regress.
- **Not all measures are equally gameable** -- the law is stated as an
  absolute, but in practice some measures are much harder to game than
  others. A measure that is expensive to falsify (actual customer
  retention over years), tightly coupled to the underlying reality
  (physical measurements like weight), or verified by independent
  observers (audited financial statements) resists Goodhart effects more
  than a measure that is cheap to game (lines of code, click-through
  rates). The law's absolutist framing obscures this important variation.
- **The economic origin assumes rational agents** -- Goodhart's original
  context was central banking, where the "gamers" are sophisticated
  financial institutions with strong incentives and information
  advantages. In contexts with less sophisticated actors or weaker
  incentives -- a small team with high trust, a classroom with intrinsic
  motivation -- the gaming effect may be negligible. The law imports an
  economics-flavored model of human behavior (strategic, self-interested,
  responsive to incentives) that is not universally applicable.
- **Sometimes gaming the metric IS the desired outcome** -- when a
  company sets a target for response time and engineers optimize for it,
  the response time actually improves. The measure and the reality move
  together because the metric is directly actionable. Goodhart's Law
  assumes a gap between proxy and reality, but for sufficiently direct
  measures, that gap may not exist. The law is most powerful for
  indirect proxies and weakest for direct ones.

## Expressions

- "When a measure becomes a target, it ceases to be a good measure" --
  the canonical formulation, actually Marilyn Strathern's paraphrase of
  Goodhart's more technical original
- "Teaching to the test" -- the education-domain instance, so common it
  has become its own idiom independent of Goodhart
- "Gaming the metrics" -- the generic verb phrase for Goodhart effects,
  used across management, engineering, and policy
- "Campbell's Law" -- the sociological parallel: "The more any
  quantitative social indicator is used for social decision-making, the
  more subject it will be to corruption pressures"
- "Hitting the numbers" -- business jargon for meeting metric targets,
  with the subtle implication that the numbers may have been hit without
  the underlying reality improving
- "Vanity metrics" -- startup jargon for measures that look impressive
  but do not correlate with business health, a Goodhart-aware term

## Origin Story

Charles Goodhart, an economist and former advisor to the Bank of England,
formulated the law in a 1975 paper on monetary policy in the United
Kingdom. His original statement was narrowly technical: "Any observed
statistical regularity will tend to collapse once pressure is placed
upon it for control purposes." He was describing how monetary aggregates
lose their predictive relationship to inflation when central banks try
to target them.

The law gained broader recognition through Marilyn Strathern's 1997
reformulation: "When a measure becomes a target, it ceases to be a
good measure." This version stripped away the monetary economics context
and revealed the universal structure. The simplified version is now far
more widely cited than the original, and Goodhart's name has become
attached to a law considerably broader than anything he stated.

The software engineering community adopted the law in the 2000s and
2010s, primarily in discussions of code coverage targets, velocity
metrics in Agile, and KPI-driven management. It pairs naturally with
discussions of technical debt and perverse incentives.

## References

- Goodhart, C.A.E. "Problems of Monetary Management: The U.K.
  Experience," *Papers in Monetary Economics*, Reserve Bank of Australia,
  1975 -- the original formulation
- Strathern, M. "'Improving Ratings': Audit in the British University
  System," *European Review* 5(3), 1997 -- the widely-cited paraphrase
- Campbell, D.T. "Assessing the Impact of Planned Social Change,"
  *Evaluation and Program Planning* 2(1), 1979 -- the parallel
  sociological formulation (Campbell's Law)
- Muller, J.Z. *The Tyranny of Metrics*, Princeton University Press,
  2018 -- book-length treatment of Goodhart effects across domains
