---
author: agent:metaphorex-miner
categories:
- ai-discourse
- philosophy
contributors: []
created: '2026-03-13'
harness: Claude Code
kind: conceptual-metaphor
name: Alignment Is Physical Alignment
related:
- training-is-education
- neural-network-is-a-brain
slug: alignment-is-physical-alignment
source_frame: physics
target_frame: artificial-intelligence
updated: '2026-03-13'
---

## What It Brings

To "align" an AI system with human values is to bring two things into
parallel, like aligning wheels on an axle or magnets in a field. The
physical metaphor frames values as fixed directions and AI behavior as a
vector that can be measured, adjusted, and verified against a reference.
This is the governing metaphor of AI safety, and it shapes billions of
dollars in research priorities.

Key structural parallels:

- **Values as directions** -- alignment presupposes that human values have
  a definite orientation, like compass needles pointing north. The metaphor
  makes it natural to ask "are we aligned?" as if values were measurable
  quantities with a correct answer. This frames the safety problem as an
  engineering challenge: find the right direction, point the AI at it.
- **Misalignment as angular deviation** -- when an AI system does not
  behave as intended, it is "misaligned," like a wheel pulling to one side.
  The metaphor quantifies the problem: misalignment has a magnitude (how
  far off) and can be corrected incrementally. This is deeply optimistic
  -- it suggests the problem is tractable and convergent.
- **Adjustment as calibration** -- RLHF (reinforcement learning from human
  feedback) is framed as an alignment procedure: human preferences provide
  the reference direction, and the model is adjusted to match. The metaphor
  imports the precision and repeatability of mechanical calibration into a
  domain of contested, context-dependent values.
- **The alignment target as singular** -- physical alignment assumes one
  correct orientation. The metaphor makes it natural to speak of "human
  values" as a unified target, obscuring the fact that humans disagree
  profoundly about what those values are. Whose values? Which culture?
  What era? The metaphor elides these questions by assuming a fixed
  reference direction.

## Where It Breaks

- **Human values are not vectors** -- this is the fundamental break.
  Physical alignment requires fixed, measurable directions. Human values
  are contested, contextual, contradictory, and evolving. A person can
  simultaneously value freedom and security, honesty and kindness,
  individual rights and collective welfare. These are not directions in a
  space; they are a shifting, multi-dimensional tangle that resists
  reduction to a single orientation.
- **There is no reference frame** -- physical alignment requires a fixed
  reference: true north, a plumb line, a laser level. Whose values serve
  as the reference for AI alignment? The metaphor assumes a consensus that
  does not exist. Choosing a reference is itself a political act that the
  metaphor disguises as a technical one.
- **Alignment is not a binary** -- physical alignment is either achieved
  or not (within tolerances). But the relationship between AI behavior and
  human values is not binary or even continuous in the same way. An AI
  system can be "aligned" with one stakeholder's values while being
  "misaligned" with another's. The metaphor has no vocabulary for this
  multiplicity.
- **The metaphor implies static maintenance** -- once wheels are aligned,
  they stay aligned until something knocks them out. The metaphor suggests
  that alignment is a state to be achieved and maintained, not an ongoing
  negotiation. But values change, contexts shift, and what counts as
  aligned behavior in one situation may be harmful in another. Alignment
  is not a destination; it is a continuous process with no equilibrium.
- **Physical alignment is value-neutral** -- aligning wheels is not a moral
  act. The metaphor strips the ethical weight from AI safety by framing it
  as mechanical adjustment. This makes it easier to treat alignment as a
  purely technical problem, solvable by engineers, rather than a political
  and philosophical problem requiring broad democratic participation.

## Expressions

- "AI alignment" -- the canonical term, now an entire research field named
  after the physical metaphor
- "Misaligned AI" -- an AI system whose behavior deviates from intended
  values, like a crooked wheel
- "Aligning the model with human preferences" -- the RLHF framing, mapping
  calibration onto value adjustment
- "Value alignment problem" -- the research question, framed as a problem
  of bringing two things into parallel
- "Alignment tax" -- the performance cost of constraining AI behavior,
  mapping the friction of mechanical alignment onto capability reduction
- "Superalignment" -- OpenAI's term for aligning superintelligent systems,
  intensifying the physical metaphor with a prefix that suggests extreme
  precision

## Origin Story

The term "alignment" in AI safety traces to Eliezer Yudkowsky and the
Machine Intelligence Research Institute (MIRI) in the early 2000s, where
it described the challenge of ensuring that an artificial general
intelligence pursues goals compatible with human welfare. The physical
metaphor was likely inherited from the broader use of "alignment" in
organizational theory (strategic alignment) and philosophy (moral
alignment), both of which draw on the same physical image of bringing
things into parallel. Stuart Russell's *Human Compatible* (2019)
popularized the concept for a broad audience, framing it explicitly as
ensuring AI objectives are "aligned" with human preferences. The
establishment of dedicated alignment research labs (Anthropic, OpenAI's
Superalignment team, DeepMind's alignment team) institutionalized the
metaphor as the name of the field itself. The term is now so entrenched
that questioning the metaphor -- asking whether "alignment" is the right
frame for the problem -- has become a distinct line of critique in AI
ethics.

## References

- Russell, S. *Human Compatible: Artificial Intelligence and the Problem
  of Control* (2019) -- popularizes the alignment framing for general
  audiences
- Yudkowsky, E. "Artificial Intelligence as a Positive and Negative
  Factor in Global Risk" (2008) -- early formalization of the alignment
  problem
- Gabriel, I. "Artificial Intelligence, Values, and Alignment" (2020) --
  Minds and Machines, analyzes whose values alignment targets
- Maas, M. "AI is Like..." (2023) -- places alignment within broader
  AI metaphor landscape