---
slug: goodharts-law
name: "Goodhart's Law"
summary: "When a metric becomes a target, agents optimize the metric rather than the quality it measured, collapsing the correlation."
kind: mental-model
categories:
  - economics-and-finance
  - systems-thinking
  - organizational-behavior
author: agent:metaphorex-miner
harness: Claude Code
contributors: []
related:
  - confirmation-bias
  - conways-law
  - peter-principle
created: '2026-03-22'
updated: '2026-03-22'
grounding: proven
transfers:
  - '[law] when a metric is selected as a target, agents optimize for the metric rather than the underlying quality it was designed to measure, causing the statistical relationship between metric and quality to break down'
  - '[law] the corruption is not random but directional: agents find the cheapest way to move the number, which systematically diverges from the most effective way to improve the reality, so the metric increasingly overstates actual performance'
  - '[law] the effect intensifies with the stakes attached to the metric -- low-stakes indicators remain informative because no one bothers to game them, while high-stakes targets attract the most aggressive optimization and degrade fastest'
limits:
  - '[law] overpredicts gaming in domains where the metric and the underlying quality are tightly coupled by physical law -- a bridge''s load-bearing capacity cannot be gamed because the measurement IS the thing, and the law applies most strongly where the gap between proxy and reality is exploitable'
  - '[law] does not distinguish between gaming (deliberately exploiting the metric) and displacement (unconsciously narrowing focus to what is measured), which have different causes and different remedies -- bundling them under one law obscures the intervention design'
embodied_patterns:
  - path
  - force
  - matching
relation_types:
  - cause/misfit
  - transform/corruption
  - compete
structure: cycle
abstraction_level: generic
---

## Transfers

"When a measure becomes a target, it ceases to be a good measure."
Charles Goodhart originally stated this as an observation about monetary
policy in 1975: any statistical regularity that the Bank of England tried
to exploit for policy purposes would collapse once market participants
anticipated the policy. Marilyn Strathern generalized it in 1997 to its
now-famous form. The law describes a feedback loop in which measurement,
incentive, and behavior co-corrupt.

- **The proxy gap** -- all measurement involves choosing a proxy for an
  underlying quality. Student learning is proxied by test scores.
  Policing quality is proxied by arrest rates. Software quality is
  proxied by code coverage. As long as the proxy is only observed, the
  correlation between proxy and quality holds. The moment the proxy
  becomes a target -- with rewards, punishments, or career consequences
  attached -- agents begin optimizing the proxy directly, and the
  correlation degrades. The proxy and the reality drift apart precisely
  because the proxy was trusted.

- **Directional corruption** -- the degradation is not random noise.
  Agents find the lowest-cost path to improving the metric, which is
  systematically different from the highest-value path to improving the
  underlying quality. Teaching to the test is cheaper than teaching
  understanding. Juking crime stats (downgrading felonies to
  misdemeanors) is easier than reducing crime. Writing trivial unit
  tests to hit coverage targets is faster than writing meaningful tests.
  The law predicts that the cheapest-to-game dimension of the metric
  will be exploited first.

- **Escalation dynamics** -- once agents begin gaming a metric, the
  metric's administrators typically respond by adding more metrics,
  creating composite scores, or tightening definitions. This provokes
  more sophisticated gaming. Schools that gamed standardized tests
  faced value-added models, which were then gamed in different ways.
  The measurement system and the gaming behavior co-evolve in an arms
  race that consumes increasing resources on both sides.

- **Campbell's Law convergence** -- Donald Campbell stated a closely
  related principle in 1979: "The more any quantitative social indicator
  is used for social decision-making, the more subject it will be to
  corruption pressures and the more apt it will be to distort and
  corrupt the social processes it is intended to monitor." Campbell
  emphasizes corruption of the social process; Goodhart emphasizes
  breakdown of the statistical relationship. Together they describe a
  system where measurement intended to improve performance ends up
  degrading both the measure and the measured.

## Limits

- **Not all metrics are equally gameable** -- the law's force varies with
  how tightly coupled the metric is to the underlying reality. A bridge's
  load-bearing test cannot be gamed because the test *is* the thing. A
  school's graduation rate can be gamed because graduation and learning are
  loosely coupled. Invoking Goodhart's Law against all measurement
  indiscriminately -- as sometimes happens in anti-metric rhetoric --
  ignores this crucial variation and can justify abandoning measurement
  entirely, which is worse.

- **Gaming vs. displacement** -- the law bundles two distinct phenomena.
  Gaming is deliberate: agents consciously exploit the gap between metric
  and reality. Displacement is unconscious: well-meaning agents narrow
  their attention to what is measured and neglect unmeasured dimensions,
  not because they are cheating but because measurement focuses attention.
  A teacher who teaches to the test out of cynical careerism and a teacher
  who does so because the test genuinely seems important are exhibiting
  different behaviors with different remedies. The law does not
  distinguish them.

- **The law is not an argument against measurement** -- it is an argument
  for humility about what measurement can do when coupled with incentives.
  Organizations that invoke Goodhart to abandon metrics entirely often
  replace them with subjective judgment, which introduces different biases
  (favoritism, recency, halo effect) without the transparency that metrics
  at least provide. The law's prescription is not "don't measure" but
  "don't attach high stakes to any single metric without expecting
  distortion."

- **Context collapse** -- the law was formulated for macroeconomic policy,
  where the relationship between central bank actions and market behavior
  is mediated by rational anticipating agents. Extending it to education,
  policing, and software development assumes that the gaming dynamic is
  structurally identical across these domains. In some cases it is; in
  others the mechanism differs enough that the prescription ("rotate
  metrics," "use multiple indicators") may not apply.

## Expressions

- "When a measure becomes a target, it ceases to be a good measure" --
  Strathern's formulation, the canonical version
- "Teaching to the test" -- the education-sector instance, where
  standardized test scores drive curriculum narrowing
- "Juking the stats" -- from *The Wire*: deliberately manipulating crime
  statistics to meet targets
- "You get what you measure" -- the management cliche, which is Goodhart's
  Law stated as if it were a feature rather than a bug
- "Campbell's Law" -- the sociological cousin, emphasizing corruption of
  the social process rather than the statistical relationship
- "Hitting the number" -- corporate shorthand for optimizing the metric at
  the expense of the business
- "Metric fixation" -- Jerry Muller's term for the institutional syndrome
  of excessive reliance on quantitative indicators

## Origin Story

Charles Goodhart, an advisor to the Bank of England, first articulated
the principle in a 1975 paper on monetary policy in the UK. His original
formulation was narrowly technical: "Any observed statistical regularity
will tend to collapse once pressure is placed upon it for control
purposes." He was describing how the Bank's attempts to target specific
monetary aggregates caused those aggregates to lose their predictive
relationship with inflation, because market participants adjusted their
behavior in response to the policy.

The law remained obscure outside economics until anthropologist Marilyn
Strathern restated it in 1997 in a broader, pithier form: "When a measure
becomes a target, it ceases to be a good measure." This generalization
connected Goodhart's monetary observation to Campbell's Law (1979), the
Lucas critique in macroeconomics (1976), and a growing body of evidence
about perverse incentives in education, healthcare, and policing. The
concept became a standard reference in behavioral economics, public
policy, and technology management.

## References

- Goodhart, C. "Problems of Monetary Management: The U.K. Experience"
  (1975) -- the original formulation
- Campbell, D. "Assessing the Impact of Planned Social Change" (1979) --
  the parallel principle in sociology
- Strathern, M. "'Improving Ratings': Audit in the British University
  System" (1997) -- the generalized formulation
- Muller, J.Z. *The Tyranny of Metrics* (2018) -- book-length treatment
  of Goodhart/Campbell dynamics across institutions
