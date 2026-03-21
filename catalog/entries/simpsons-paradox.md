---
slug: simpsons-paradox
name: Simpson's Paradox
kind: mental-model
source_frame: statistics
categories:
  - decision-making
author: agent:metaphorex-miner
contributors: []
related:
  - shut-up-and-calculate
created: '2026-03-19'
updated: '2026-03-19'
grounding: proven
harness: Claude Code
transfers:
  - '[model] demonstrates that a trend present in every subgroup can reverse when the subgroups are combined, making aggregation itself a source of causal error rather than a neutral summarization'
  - '[model] forces the reasoner to identify which level of analysis -- subgroup or aggregate -- is causally appropriate before drawing conclusions, preventing the default assumption that more data always clarifies'
  - '[model] reveals that the direction of an observed association can be an artifact of how the data was partitioned, making the choice of grouping variable a substantive causal commitment rather than a mere bookkeeping decision'
limits:
  - '[model] requires that the confounding variable be known and measurable, but in many real-world situations the lurking variable that would reveal the reversal is unobserved or unrecognized'
  - '[model] is sometimes invoked as a blanket skepticism toward all aggregate statistics, when in fact most aggregations do not reverse and the paradox applies only under specific distributional conditions'
embodied_patterns:
  - force
  - path
  - matching
relation_types:
  - cause
  - transform
structure: transformation
abstraction_level: generic
---

## Transfers

Simpson's paradox occurs when a statistical trend appears in several groups
of data but reverses when the groups are combined. The canonical example is
UC Berkeley's 1973 graduate admissions: the aggregate data showed that women
were admitted at a lower rate than men (apparent discrimination), but when
examined department by department, women were admitted at a slightly higher
rate in most departments. The reversal occurred because women
disproportionately applied to more competitive departments with lower
overall admission rates.

The paradox is not a statistical curiosity. It is a structural warning about
the relationship between aggregation and causation.

Key structural parallels:

- **Aggregation can invert causation** -- the most important transfer is
  negative: combining data does not always clarify; it can reverse the
  truth. A drug that helps patients in every age group can appear harmful
  in the aggregate if older patients (who have worse outcomes regardless)
  disproportionately receive treatment. A school district where every
  school improves its test scores can show declining district-wide scores
  if enrollment shifts toward lower-performing schools. The model forces
  the question: is the aggregate or the subgroup the right level of
  analysis? This is not a statistical question but a causal one.

- **Grouping is a causal commitment** -- to partition data is to claim
  that the grouping variable is causally relevant. At Berkeley, splitting
  by department was the right move because department was the causal
  mediator (departments had different selectivity, and applicant gender
  distribution varied across departments). In other contexts, the same
  split might be wrong. The model teaches that "controlling for X" is not
  a neutral act -- it is a claim that X is on the causal pathway, and
  different causal stories demand different partitions.

- **More data does not always mean better answers** -- naive empiricism
  holds that aggregating more observations reduces error. Simpson's
  paradox shows that aggregation across a confound increases error. The
  model is a counterexample to the intuition that bigger datasets are
  always better. A small, well-stratified dataset can reveal the truth
  that a large, undifferentiated one obscures.

- **The paradox has no purely statistical resolution** -- you cannot
  determine whether to aggregate or partition by looking at the numbers
  alone. You need a causal model: a theory about which variables
  influence which. This is the deepest transfer: statistics cannot
  replace causal reasoning. The numbers alone are ambiguous, and
  resolving the ambiguity requires domain knowledge and causal
  assumptions that lie outside the data.

## Limits

- **The confound must be known** -- Simpson's paradox is diagnosable only
  when the analyst knows which variable to condition on. If the confounding
  variable is unobserved (unrecognized socioeconomic factors, unmeasured
  genetic differences), the paradox is invisible. The model warns about
  aggregation errors but cannot tell you which aggregation errors you are
  currently making with your current data.

- **Not all aggregations are paradoxical** -- Simpson's paradox is dramatic
  precisely because it is rare in its strong form (complete reversal). In
  most datasets, aggregation attenuates a trend rather than reversing it.
  Invoking the paradox as a general reason to distrust all summary
  statistics is an overreaction that can paralyze decision-making. The
  model is a tool for specific diagnostic situations, not a license for
  universal skepticism.

- **The paradox can be used to manipulate** -- because the direction of an
  effect depends on how data is partitioned, a motivated analyst can choose
  the partition that supports their preferred conclusion. Both the
  aggregate and the stratified results are "real" in the sense that the
  numbers are correct. Simpson's paradox does not resolve which is
  causally appropriate; it only shows that they differ. Without a shared
  causal model, debate between aggregate and stratified results devolves
  into advocacy rather than analysis.

- **Causal models are themselves contestable** -- the model's resolution
  ("use a causal model to decide whether to aggregate") pushes the
  ambiguity one level up. Causal models are constructed from domain
  knowledge, prior research, and assumptions that are themselves
  debatable. At Berkeley, the causal story (women applied to harder
  departments) was relatively clear. In more complex settings
  (healthcare, criminal justice, hiring), the correct causal model is
  precisely what the parties disagree about, and Simpson's paradox
  becomes a tool in the argument rather than a resolution of it.

## Expressions

- "Simpson's paradox" -- the standard name in statistics, after Edward
  Simpson's 1951 paper, though the phenomenon was noted earlier by Yule
  (1903)
- "Ecological fallacy" -- a related error where aggregate-level
  correlations are incorrectly attributed to individuals, sometimes
  produced by the same mechanism
- "Confounding variable" -- the hidden third factor whose distribution
  across groups produces the reversal
- "Control for" -- the statistical operation of partitioning data by a
  variable, which resolves the paradox when the right variable is chosen
- "Lurking variable" -- informal term for the unobserved factor that
  creates a Simpson's reversal
- "The numbers don't lie, but they don't tell the whole truth" --
  folk acknowledgment that aggregate statistics can mislead

## Origin Story

The paradox is named after Edward Simpson, whose 1951 paper in the *Journal
of the Royal Statistical Society* formalized the reversal phenomenon. But
the observation is older: Karl Pearson noted cases in 1899, and George Udny
Yule described the mechanism in 1903. The UC Berkeley admissions case
(Bickel, Hammel, and O'Connell, 1975) became the canonical example because
it involved a politically charged question -- gender discrimination -- where
the reversal had real policy consequences.

Judea Pearl's work on causal inference, particularly *Causality* (2000) and
*The Book of Why* (2018), elevated Simpson's paradox from a statistical
curiosity to a central example of why causal reasoning cannot be replaced
by statistical reasoning. Pearl showed that the paradox cannot be resolved
within the probability calculus alone: you must specify a causal model
(a directed acyclic graph) to determine whether conditioning on a variable
is appropriate.

## References

- Simpson, E. H. "The Interpretation of Interaction in Contingency Tables."
  *Journal of the Royal Statistical Society, Series B* (1951)
- Bickel, P. J., Hammel, E. A., and O'Connell, J. W. "Sex Bias in
  Graduate Admissions: Data from Berkeley." *Science* (1975)
- Pearl, Judea. *Causality: Models, Reasoning, and Inference* (2000)
- Pearl, Judea and Mackenzie, Dana. *The Book of Why* (2018) -- accessible
  treatment of Simpson's paradox and causal inference
