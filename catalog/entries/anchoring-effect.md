---
slug: anchoring-effect
name: Anchoring Effect
summary: "The first number pulls your estimate toward it, even when irrelevant. Adjustment away from the anchor is consistently insufficient."
kind: mental-model
categories:
  - cognitive-science
  - decision-making
author: agent:metaphorex-miner
harness: Claude Code
contributors: []
related:
  - anchoring
  - decoy-effect
  - framing-effect
  - availability-bias
created: '2026-03-26'
updated: '2026-03-26'
grounding: proven
embodied_patterns:
  - force
  - near-far
  - blockage
relation_types:
  - cause/constrain
  - prevent
structure: equilibrium
abstraction_level: generic
transfers:
  - '[model] predicts that an initial value -- even one known to be arbitrary -- will disproportionately influence subsequent numerical estimates because the mind uses the anchor as a starting point and adjusts insufficiently away from it'
  - '[model] identifies a two-stage failure: first, the anchor activates anchor-consistent information in memory (selective accessibility); second, the person adjusts away from the anchor but stops too soon, as if the anchor exerts a gravitational pull that increases with proximity'
limits:
  - '[model] overstates universality -- domain experts with calibrated internal reference points show significantly attenuated anchoring effects, particularly in fields with fast, unambiguous feedback'
  - '[model] conflates two distinct mechanisms (insufficient adjustment from self-generated anchors vs. selective accessibility from externally provided anchors) that have different boundary conditions and different implications for debiasing'
---

## Transfers

The anchoring effect is the cognitive bias where exposure to a number --
any number, even a transparently random one -- shifts subsequent numerical
judgments toward that number. Tversky and Kahneman (1974) demonstrated
the effect by spinning a rigged wheel of fortune: subjects who saw the
wheel land on 65 estimated that 45% of African nations belonged to the
UN, while those who saw it land on 10 estimated 25%. A visibly random
number moved estimates by 20 percentage points.

Key structural parallels:

- **The anchor warps the entire judgment space** -- the most important
  effect is not that people start at the anchor but that the anchor
  redefines what seems reasonable. In salary negotiations, a high
  opening offer does not just begin the discussion at a high point; it
  makes the eventual midpoint higher than it would have been without
  the anchor. The anchor does not just bias the starting position; it
  reshapes the landscape of plausible outcomes.

- **Adjustment is effortful; anchoring is automatic** -- the anchor
  influences judgment without deliberate thought. Moving away from the
  anchor requires conscious cognitive effort, and people consistently
  stop adjusting before reaching the correct value. This asymmetry
  explains why the effect persists even when people are warned about it,
  offered financial incentives for accuracy, or told the anchor is
  irrelevant. Knowledge of the bias does not neutralize it.

- **Selective accessibility deepens the pull** -- Strack and
  Mussweiler (1997) showed that anchors work partly by changing which
  information comes to mind. Considering whether a target value is
  near the anchor activates anchor-consistent memories and knowledge.
  Asked "Is the average temperature in Germany higher or lower than
  20 degrees Celsius?", the mind retrieves warm-weather facts. The
  anchor does not just pull the number; it curates the evidence.

- **Anchoring compounds across chains of judgment** -- in complex
  decisions involving multiple estimates (project budgets, legal
  settlements, real estate transactions), each anchored judgment
  feeds into the next. The listing price anchors the buyer, whose
  offer anchors the appraiser, whose valuation anchors the lender.
  The original anchor propagates and sometimes amplifies through the
  chain.

## Limits

- **Expertise provides competing anchors** -- experienced real estate
  agents are less susceptible to manipulated listing prices than
  novice buyers (Northcraft and Neale, 1987), though not immune. In
  domains with fast feedback and unambiguous outcomes (commodity
  trading, sports statistics), expertise can substantially reduce
  anchoring. The model overpredicts the bias's power when applied to
  genuinely expert judgment in familiar domains.

- **Two mechanisms, one name** -- the "anchoring effect" conflates
  Tversky and Kahneman's original "insufficient adjustment" account
  with Strack and Mussweiler's "selective accessibility" account.
  These are different processes with different predictions:
  insufficient adjustment is strongest under cognitive load (less
  capacity to adjust), while selective accessibility operates even
  at low load because it is a semantic process. Treating anchoring
  as a unitary phenomenon obscures which mechanism is operating and
  therefore which intervention might work.

- **Not every first number is an anchor** -- the model is sometimes
  overextended to any case where an early estimate influences a later
  one. If a project manager estimates six months based on experience
  with similar projects, and a team member revises to seven, the
  original estimate is not an "anchor" in the experimental sense --
  it is a legitimate informational signal. Calling every sequential
  influence "anchoring" conflates rational updating with cognitive bias.

- **Debiasing advice underperforms** -- the standard prescriptions
  ("generate your own estimate first," "consider the opposite,"
  "ignore the anchor") have modest effect sizes in controlled studies.
  Telling someone to ignore an anchor is roughly as effective as
  telling someone not to think about a white bear. The model implies
  a cleaner intervention space than actually exists.

## Expressions

- "Don't let them set the anchor" -- negotiation advice to make the
  opening offer rather than reacting to the counterparty's
- "That number is anchoring the whole discussion" -- project planning,
  when an early estimate constrains subsequent budgeting
- "Price anchoring" -- retail strategy of displaying a high "original
  price" to make the sale price seem more attractive
- "Sticker shock" -- the consumer experience of encountering a price
  that becomes the anchor against which all alternatives are judged
- "The first offer wins" -- folk wisdom in negotiation, reflecting
  the empirical finding that outcomes correlate more with opening
  offers than with objective case merits

## Origin Story

The anchoring effect was introduced by Daniel Kahneman and Amos Tversky
in their landmark 1974 *Science* paper "Judgment under Uncertainty:
Heuristics and Biases," alongside the availability and representativeness
heuristics. The paper launched the heuristics-and-biases research program.
Fritz Strack and Thomas Mussweiler's 1997 work reframed the mechanism as
selective accessibility rather than simple insufficient adjustment,
deepening the theoretical account. Nicholas Epley and Thomas Gilovich
(2006) showed that both mechanisms are real but operate under different
conditions: insufficient adjustment for self-generated anchors, selective
accessibility for externally provided ones. The effect remains one of
the most robust and frequently replicated findings in experimental
psychology, with real-world implications documented in legal sentencing,
real estate pricing, salary negotiations, and consumer behavior.

## References

- Tversky, A. & Kahneman, D. "Judgment under Uncertainty: Heuristics
  and Biases." *Science* 185 (1974): 1124-1131
- Strack, F. & Mussweiler, T. "Explaining the Enigmatic Anchoring
  Effect." *Journal of Personality and Social Psychology* 73 (1997):
  437-446
- Epley, N. & Gilovich, T. "The Anchoring-and-Adjustment Heuristic."
  *Psychological Science* 17 (2006): 311-318
- Northcraft, G. & Neale, M. "Experts, Amateurs, and Real Estate."
  *Organizational Behavior and Human Decision Processes* 39 (1987): 84-97
- Furnham, A. & Boo, H.C. "A Literature Review of the Anchoring Effect."
  *Journal of Socio-Economics* 40 (2011): 35-42
