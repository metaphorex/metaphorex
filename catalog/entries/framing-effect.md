---
slug: framing-effect
name: Framing Effect
summary: "The same facts, presented differently, produce different decisions. The frame is not decoration -- it is the decision."
kind: mental-model
categories:
- psychology
- decision-making
- cognitive-science
author: agent:metaphorex-miner
contributors: []
related:
- anchoring
- decoy-effect
- loss-aversion
- straw-man
created: '2026-03-26'
updated: '2026-03-26'
grounding: proven
harness: Claude Code
transfers:
  - "[model] demonstrates that logically equivalent descriptions of the same outcome produce systematically different choices, revealing that human decision-making operates on representations rather than on underlying reality"
  - "[model] imports the architectural metaphor of a frame -- what is included inside the border receives attention, what falls outside is invisible -- to explain how presentation boundaries determine which features of a choice become salient"
  - "[model] predicts that gain frames produce risk aversion while loss frames produce risk seeking, providing a specific and testable mechanism for how presentation alters preference"
limits:
  - "[model] breaks because the original experiments used carefully constructed scenarios with precise numerical equivalence, while real-world framing involves genuinely different emphasis, context, and connotation that may carry legitimate informational content -- not all framing is manipulation"
  - "[model] misleads by implying a 'frame-free' presentation is possible, when in practice every description of a situation necessarily foregrounds some features and backgrounds others -- the choice is never between framing and not framing but between frames"
  - "[model] overpredicts by treating all humans as equally susceptible, when expertise, numeracy, and domain familiarity substantially reduce framing effects -- experts in a field are less swayed by how options in that field are presented"
embodied_patterns:
  - boundary
  - container
  - surface-depth
relation_types:
  - cause
  - transform
structure: hierarchy
abstraction_level: generic
---

## Transfers

Amos Tversky and Daniel Kahneman demonstrated in 1981 that people make
different choices depending on whether outcomes are described as gains or
losses, even when the underlying options are mathematically identical.
In the classic "Asian disease problem," the same public health intervention
is preferred when framed as "saving 200 lives" and rejected when framed as
"400 people will die" -- though the two descriptions are logically
equivalent. This is not a minor laboratory curiosity; it is one of the
most robust findings in behavioral science, replicated across cultures,
domains, and decades.

Key structural parallels:

- **The frame determines what counts as salient** -- a picture frame
  includes some of the visual field and excludes the rest. Similarly, a
  decision frame determines which features of a choice become prominent
  and which recede. Describing a medical procedure as having a "90%
  survival rate" versus a "10% mortality rate" presents the same fact but
  makes different features salient: the first foregrounds the survivors,
  the second foregrounds the dead. The structural insight is that salience
  is not a property of the information but of its presentation.

- **Gain frames and loss frames activate different risk profiles** --
  Tversky and Kahneman showed a specific asymmetry: when outcomes are
  framed as gains (lives saved, money earned), people become risk-averse
  and prefer the certain option. When framed as losses (lives lost, money
  spent), people become risk-seeking and prefer the gamble. The same
  person, facing the same choice, shifts between conservative and
  aggressive strategies depending entirely on how the question is worded.
  This maps onto negotiations, marketing, medical consent, and policy
  design wherever someone controls how options are presented.

- **Reference point dependence** -- the framing effect reveals that people
  do not evaluate outcomes in absolute terms but relative to a reference
  point. "Saving 200 out of 600" uses 0 saved as the reference (a gain);
  "400 out of 600 will die" uses 600 alive as the reference (a loss). The
  same objective state -- 200 alive, 400 dead -- is experienced differently
  depending on where you start counting. This structural feature explains
  why reframing is so powerful: changing the reference point changes the
  experienced value without changing the actual outcome.

- **The invisibility of the frame** -- the most important structural
  feature is that people typically do not notice the frame. Subjects in
  Tversky and Kahneman's experiments did not realize they were being
  presented with equivalent options. The frame works precisely because it
  is transparent -- like a window frame, you look through it, not at it.
  This means that the most consequential frames are the ones that are
  treated as natural, obvious, or "just how things are" rather than as
  deliberate choices about presentation.

## Limits

- **Frame equivalence is rare outside the lab** -- the classic experiments
  work because the researchers constructed descriptions that are
  mathematically identical. In practice, different descriptions of the
  same situation usually carry genuinely different information, emphasis,
  or connotation. Saying "this neighborhood has a 2% crime rate" versus
  "this neighborhood has a 98% safety rate" are equivalent, but "this is
  a safe neighborhood" versus "crime happens here" are not -- they imply
  different speakers, different purposes, and different evidential bases.
  Treating all framing as cognitive bias ignores the informational content
  of how things are described.

- **There is no view from nowhere** -- the framing effect implies there
  is a "correct" frame-free way to present information, but this does not
  exist. Every description of a choice necessarily includes some features
  and excludes others, uses some reference point, and adopts some unit of
  measurement. The question is never "should we frame this?" but "which
  frame should we use?" Awareness of the framing effect does not eliminate
  framing; it just makes you more deliberate about which frame to choose.

- **Expertise reduces susceptibility** -- the framing effect is strongest
  among novices and weakest among experts in the relevant domain.
  Experienced physicians show smaller framing effects for medical
  decisions, experienced investors for financial ones. This suggests
  that the effect is partly a function of surface processing: when people
  lack the knowledge to evaluate options on their merits, they rely more
  heavily on presentational cues. The model overpredicts if applied
  uniformly across all decision-makers.

- **The model can justify manipulation** -- awareness of the framing
  effect has been enthusiastically adopted by marketers, politicians, and
  "choice architects" who use it to steer decisions. The descriptive
  finding (people are affected by frames) slides into a prescriptive
  program (we should frame things to produce the "right" choice). This
  raises significant ethical problems: who decides what the right choice
  is, and what distinguishes "nudging" from manipulation? The model itself
  is silent on this question, which is its most important omission.

## Expressions

- "It's all in how you frame it" -- folk recognition that presentation
  affects perception, used in negotiation and persuasion advice
- "Reframe the conversation" -- deliberate strategy of shifting the
  reference point or salient features in a discussion
- "Spin" -- pejorative term for framing in political and media contexts,
  implying deliberate manipulation
- "Glass half full / glass half empty" -- the oldest folk expression of
  the framing effect, predating the formal research by centuries
- "Position it as an investment, not a cost" -- business framing advice,
  shifting from loss frame to gain frame
- "Framing the debate" -- in political discourse, the act of establishing
  which reference point and vocabulary will be used before substantive
  argument begins

## Origin Story

The framing effect was formally identified by Amos Tversky and Daniel
Kahneman in their 1981 paper "The Framing of Decisions and the Psychology
of Choice," published in *Science*. It built on their earlier prospect
theory (1979), which showed that people evaluate outcomes relative to
reference points and weight losses more heavily than equivalent gains.
The framing effect demonstrated that the reference point itself could be
manipulated through presentation. The finding challenged the economic
assumption of "description invariance" -- that rational agents should
make the same choice regardless of how options are described. It became
a cornerstone of behavioral economics and contributed to Kahneman's 2002
Nobel Prize in Economics. The concept has since been applied in medicine
(how surgical risks are communicated), law (jury instructions), public
policy (organ donation defaults), and marketing (pricing presentation).

## References

- Tversky, A. and Kahneman, D. "The Framing of Decisions and the
  Psychology of Choice" (1981) -- the foundational paper
- Kahneman, D. and Tversky, A. "Prospect Theory: An Analysis of Decision
  under Risk" (1979) -- the theoretical foundation
- Kahneman, D. *Thinking, Fast and Slow* (2011) -- accessible summary
  for general audiences
- Thaler, R. and Sunstein, C. *Nudge* (2008) -- applied framing to
  policy design
