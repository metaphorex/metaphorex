---
author: agent:metaphorex-miner
harness: Claude Code
categories:
- organizational-behavior
- systems-thinking
contributors: []
created: '2026-03-18'
grounding: established
kind: mental-model
name: Eliminate Numerical Quotas
summary: "Quotas substitute a number for understanding of the process. The number becomes the goal, and the underlying work degrades."
provenance: tps-deming
related:
- eliminate-slogans
- a-bad-system-beats-a-good-person
- pride-of-workmanship
slug: eliminate-numerical-quotas
source_frame: measurement
updated: '2026-03-18'
embodied_patterns:
  - blockage
  - iteration
  - flow
relation_types:
  - prevent
  - cause
structure:
  - cycle
  - hierarchy
abstraction_level: generic
transfers:
  - "[model] reveals that numerical quotas set on outputs substitute measurement for understanding, guaranteeing mediocrity by treating the system's current capability as a fixed ceiling to aim at rather than a baseline to improve"
  - "[model] predicts that management by numerical objectives will produce gaming, data falsification, or quality sacrifice, because hitting the number becomes the goal rather than improving the process that generates the number"
  - "[model] distinguishes process metrics that diagnose system health from output targets imposed as performance standards, arguing only the former lead to genuine improvement"
limits:
  - "[model] underweights the coordination value of quantitative targets in complex organizations where teams need shared benchmarks to synchronize effort across dependencies"
  - "[model] assumes management has the statistical sophistication to replace quotas with process understanding, but in practice many organizations lack the capability to manage by process and quotas serve as an imperfect but functional substitute"
---

## Transfers

Deming's Points 11a and 11b call for the elimination of work standards
(quotas) on the factory floor and the elimination of management by
objective and management by numbers. The core insight: quotas substitute
a number for understanding. They tell workers and managers what outcome
to produce without addressing the system's capability to produce it.

Key structural parallels:

- **Quotas are ceilings disguised as floors** -- a production quota of 200
  units per day is presented as a minimum standard, but in practice it
  functions as a ceiling. Workers who can produce 250 slow down to avoid
  raising the bar. Workers who struggle to reach 200 cut corners on
  quality. The quota converges everyone toward the average, eliminating
  both excellence and the information that variation would provide about
  the system. This dynamic appears wherever numerical targets are imposed:
  lines of code per day, tickets closed per sprint, papers published per
  year.
- **The number becomes the goal** -- Deming's critique anticipates what
  later became known as Goodhart's Law: when a measure becomes a target,
  it ceases to be a good measure. Workers and managers who are evaluated on
  a number will optimize for the number rather than for the quality it was
  meant to represent. Call center agents measured on calls per hour will
  hang up on difficult cases. Software teams measured on velocity will
  inflate story points. Schools measured on test scores will teach to
  the test. The underlying process degrades while the metric improves.
- **Measurement without theory is noise** -- Deming argued that numbers are
  meaningful only in the context of a theory about the process that
  generates them. A defect rate of 3% means nothing unless you understand
  the sources of variation in the process. Quotas strip away the
  theoretical context and present the number as self-explanatory. This is
  the epistemological core of the critique: management by numbers is
  management without understanding.
- **Process capability versus arbitrary targets** -- Deming introduced the
  distinction between what a system is capable of producing (its
  statistical capability) and what management demands it produce. If the
  demand exceeds the capability, the only options are to falsify data, cut
  quality, or fail. Improving the capability requires understanding the
  system -- which quotas actively discourage because they focus attention
  on the output rather than the process.

## Limits

- **Not all numerical targets are quotas** -- Deming's critique targets
  arbitrary numerical standards imposed without process understanding. But
  some numbers represent genuine constraints: a delivery deadline, a
  regulatory threshold, a budget limit. These are not arbitrary quotas but
  real boundaries that must be respected. The model does not clearly
  distinguish imposed quotas from genuine constraints.
- **Some domains need output targets for coordination** -- in complex
  organizations with many interdependent teams, quantitative targets
  serve as coordination mechanisms. If the logistics team does not know
  how many units manufacturing will produce, they cannot plan shipping.
  Deming's manufacturing context often had simpler coordination needs
  than modern knowledge-work organizations.
- **Removing quotas without replacing them leaves a vacuum** -- Deming
  prescribed replacing quotas with leadership and process understanding.
  But this requires statistical literacy and management skill that many
  organizations lack. In practice, eliminating quotas without building
  the capability to manage by process can produce aimlessness or even
  worse outcomes than the quotas did.
- **The Goodhart dynamic is not inevitable** -- while measurement
  corruption is real and common, some organizations maintain healthy
  relationships with metrics by using them as diagnostics rather than
  evaluations. OKRs in well-run organizations, for example, are
  explicitly aspirational and divorced from compensation. The model can
  lead to an overcorrection where all measurement is viewed as toxic.
- **Individual accountability still matters** -- the model's emphasis on
  system-caused variation can be used to deflect accountability for
  genuinely individual failures. A developer who consistently introduces
  bugs is not solely a system problem. The model provides no framework
  for distinguishing system variation from individual performance issues
  in specific cases.

## Expressions

- "You get what you measure" -- the folk version of Goodhart's Law,
  encoding both the power and the corruption of measurement
- "Making the numbers" -- corporate shorthand for achieving quotas,
  revealing that the number itself has become the objective
- "Teaching to the test" -- education's version of quota corruption,
  where test scores replace learning as the goal
- "Velocity" in agile teams -- a process diagnostic that frequently
  degrades into a quota, with teams gaming story points to hit targets
- "Stack ranking" -- forced distribution of performance ratings, a
  numerical quota applied to human evaluation
- "Management by spreadsheet" -- pejorative describing organizations
  that substitute numerical reporting for process understanding
- "Hitting quota" in sales -- the paradigmatic example of numerical
  targets shaping behavior, for better and worse

## Origin Story

Points 11a and 11b of Deming's 14 Points (published in *Out of the
Crisis*, 1986) target two distinct but related practices: work standards
(quotas) on the factory floor (11a) and management by objective /
management by numbers for management (11b). Deming argued that both
substitute a number for understanding and guarantee that the system will
never improve beyond its current capability.

Deming's critique was grounded in Walter Shewhart's statistical process
control framework. Shewhart had shown that every process has a natural
capability -- a range of outcomes determined by the system's design. Asking
for outcomes outside this range without changing the system is asking for
either miracles or fraud. Deming extended this insight from the factory
floor to management practice, arguing that MBO (Management by Objectives,
popularized by Peter Drucker) committed the same error at the executive
level: setting numerical targets without understanding or improving the
processes that generate the numbers.

The critique gained renewed relevance in software engineering with the
adoption of velocity as an agile metric. Originally intended as a planning
tool (how much work can this team typically complete in a sprint?), velocity
was widely corrupted into a performance quota, producing exactly the
dynamics Deming predicted: point inflation, quality sacrifice, and
adversarial relationships between teams and management.

## References

- Deming, W. Edwards. *Out of the Crisis* (1986), pp. 70-75
- Deming, W. Edwards. *The New Economics for Industry, Government,
  Education* (1993), Chapter 2
- Goodhart, Charles. "Problems of Monetary Management: The U.K.
  Experience" (1975) -- the measurement corruption that Deming anticipated
- Drucker, Peter. *The Practice of Management* (1954) -- MBO as Deming's
  foil
- ASQ. "Deming's 14 Points for Total Quality Management."
  https://asq.org/quality-resources/tqm/deming-points
