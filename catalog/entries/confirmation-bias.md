---
slug: confirmation-bias
name: Confirmation Bias
summary: "People seek and recall evidence that confirms existing beliefs. The bar for changing your mind is systematically higher than for reinforcing it."
kind: mental-model
categories:
  - cognitive-science
  - psychology
  - decision-making
author: agent:metaphorex-miner
harness: Claude Code
contributors: []
related:
  - anchoring
  - gamblers-fallacy
  - incentive-caused-bias
  - dunning-kruger-effect
created: '2026-03-21'
updated: '2026-03-21'
grounding: proven
transfers:
  - '[model] predicts that when searching for evidence relevant to a hypothesis, people will disproportionately seek and notice information that supports what they already believe, while overlooking or discounting equally available disconfirming evidence'
  - '[model] explains why two people examining the same body of evidence can reach opposite conclusions -- each selectively attends to the subset that confirms their prior position, producing the illusion that the evidence itself is one-sided'
  - '[model] identifies an asymmetry in cognitive processing where confirming instances are accepted at face value while disconfirming instances trigger critical scrutiny, so the evidentiary bar for changing one''s mind is systematically higher than the bar for reinforcing it'
limits:
  - '[model] overpredicts the bias in domains where practitioners have fast, unambiguous feedback loops -- experienced weather forecasters and bridge players show remarkably calibrated beliefs because reality corrects them quickly and unambiguously, suggesting confirmation bias is strongest where feedback is delayed, noisy, or absent'
  - '[model] conflates several distinct mechanisms under one label: motivated reasoning (wanting to be right), selective exposure (choosing friendly media), biased assimilation (interpreting ambiguous evidence favorably), and positive test strategy (testing by looking for confirming cases) -- these have different causes, different boundary conditions, and different interventions'
embodied_patterns:
  - container
  - force
  - matching
relation_types:
  - select
  - prevent
  - cause/constrain
structure: cycle
abstraction_level: generic
---

## Transfers

The tendency to search for, interpret, favor, and recall information in
a way that confirms or supports one's prior beliefs or values. First
experimentally demonstrated by Peter Wason (1960), confirmation bias is
among the most extensively replicated findings in cognitive psychology.

- **Asymmetric search** -- when testing a hypothesis, people
  preferentially seek evidence that would confirm it rather than evidence
  that would disconfirm it. Wason's 2-4-6 task is the canonical
  demonstration: participants who believe the rule is "ascending by two"
  test triples like 8-10-12 and 14-16-18 (confirming) rather than
  1-2-3 or 10-8-6 (disconfirming). The actual rule ("any ascending
  sequence") can only be discovered through disconfirmation. Most
  participants never find it because they never look for what would
  prove them wrong.

- **Biased assimilation** -- when encountering mixed evidence, people
  judge evidence that supports their position as stronger, more relevant,
  and more methodologically sound than evidence that contradicts it. Lord,
  Ross, and Lepper (1979) showed that partisans on both sides of the
  death penalty debate became *more* polarized after reading the same
  balanced research summary, because each side accepted the supportive
  study and criticized the opposing one. The evidence is filtered, not
  weighed.

- **Belief perseverance** -- once formed, beliefs survive the total
  discrediting of the evidence that created them. Ross, Lepper, and
  Hubbard (1975) showed that after participants were told their initial
  evidence was fabricated, they continued to hold the beliefs that
  evidence had generated. Confirmation bias operates not just at the
  intake stage but at the retention stage: confirming memories are more
  accessible, creating a self-reinforcing loop.

- **Institutional amplification** -- confirmation bias scales beyond
  individual cognition. Intelligence agencies that "fix the intelligence
  around the policy" (the Downing Street Memo), medical teams that anchor
  on an initial diagnosis and fail to reassess, hiring panels that
  decide in the first 30 seconds and spend the remaining interview
  confirming -- the bias is organizational as well as psychological.
  The structure of most institutions (hierarchical authority, sunk cost
  reasoning, reputation risk) amplifies rather than corrects individual
  bias.

## Limits

- **Expertise with fast feedback suppresses it** -- the model's most
  important boundary condition. Confirmation bias is not a fixed property
  of human cognition; it varies dramatically with the feedback structure
  of the environment. Bridge players, weather forecasters, and
  experienced livestock judges show well-calibrated beliefs because they
  receive rapid, unambiguous, repeated feedback on the accuracy of their
  predictions. In these "kind" learning environments (Hogarth 2001),
  reality corrects the bias faster than the bias can compound. The model
  overpredicts in exactly these domains. Its predictive power is highest
  where feedback is delayed (policy), ambiguous (psychotherapy), or
  absent (political opinion).

- **Multiple mechanisms, one label** -- "confirmation bias" is an
  umbrella term covering at least four distinct phenomena: motivated
  reasoning (I want to be right, so I filter), selective exposure (I
  choose information sources that agree with me), biased assimilation
  (I interpret ambiguous evidence as supporting my view), and positive
  test strategy (I test hypotheses by looking for confirming rather
  than disconfirming instances). These have different causes and
  different interventions. A debiasing technique that works for
  positive test strategy (structured devil's advocacy) may not work
  for motivated reasoning, which has emotional rather than cognitive
  roots. The unified label obscures the need for distinct countermeasures.

- **Not always irrational** -- in many real-world environments,
  confirmation of a working hypothesis is the efficient search strategy.
  A doctor who suspects pneumonia and orders a chest X-ray is engaging
  in "positive test strategy," but this is medically sound when the base
  rate is high and the test is informative. Bayesian reasoning sometimes
  *recommends* attending more to confirming evidence when priors are
  strong and well-calibrated. The model's framing of all confirmatory
  search as "bias" conflates contexts where it is genuinely distorting
  with contexts where it is simply efficient.

- **Debiasing is harder than naming** -- the model is widely known but
  poorly counteracted. "Consider the opposite" (the standard
  recommendation) reduces the bias in laboratory settings but has
  limited durability in real decisions where emotional stakes are high.
  Naming the bias creates an illusion of control: teams that announce
  "let's watch out for confirmation bias" often feel inoculated without
  actually changing their information search behavior. The model
  diagnoses more readily than it cures.

## Expressions

- "People see what they want to see" -- the folk version, predating the
  formal concept by centuries
- "Cherry-picking the evidence" -- selective citation of confirming data,
  common in policy debates and corporate strategy documents
- "We need a red team" -- the institutional countermeasure, assigning a
  group specifically to disconfirm the prevailing hypothesis
- "Echo chamber" -- the information-environment consequence of
  confirmation bias at scale, where selective exposure creates
  self-reinforcing communities of belief
- "The Wason selection task" -- the laboratory paradigm that made
  confirmation bias experimentally tractable
- "Are you looking for reasons to believe this, or reasons not to?" --
  the simplest debiasing prompt, rarely asked

## Origin Story

The concept has ancient roots -- Francis Bacon described the tendency in
*Novum Organum* (1620): "The human understanding when it has once adopted
an opinion draws all things else to support and agree with it." But the
modern experimental tradition begins with Peter Wason's 2-4-6 task
(1960), which demonstrated that intelligent adults systematically fail to
seek disconfirming evidence even when instructed to find the rule.

The term "confirmation bias" was popularized by Wason and subsequently
elaborated by a generation of researchers. Lord, Ross, and Lepper's 1979
study on biased assimilation became one of the most cited papers in
social psychology. Nickerson's 1998 review paper, "Confirmation Bias: A
Ubiquitous Phenomenon in Many Guises," consolidated the sprawling
literature and remains the standard reference. Kahneman's *Thinking, Fast
and Slow* (2011) brought the concept to a mass audience.

## References

- Wason, P.C. "On the failure to eliminate hypotheses in a conceptual
  task." *Quarterly Journal of Experimental Psychology* 12 (1960)
- Lord, C.G., Ross, L. & Lepper, M.R. "Biased assimilation and attitude
  polarization." *Journal of Personality and Social Psychology* 37 (1979)
- Nickerson, R.S. "Confirmation Bias: A Ubiquitous Phenomenon in Many
  Guises." *Review of General Psychology* 2.2 (1998)
- Kahneman, D. *Thinking, Fast and Slow* (2011)
