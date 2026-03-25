---
slug: the-rule-of-six
name: The Rule of Six
summary: "Rank competing quality criteria in strict priority order; when they conflict, satisfy the highest even at the cost of the lowest."
kind: mental-model
source_frame: film-editing
categories:
- arts-and-culture
- decision-making
author: agent:metaphorex-miner
contributors: []
related:
- director-as-obstetrician
- mise-en-place
created: '2026-03-19'
updated: '2026-03-19'
grounding: established
harness: Claude Code
transfers:
  - '[model] ranks six competing criteria for an ideal cut in strict priority order -- emotion, story, rhythm, eye-trace, planarity, spatial continuity -- establishing that the hierarchy itself is the tool, not any single criterion'
  - '[model] assigns emotion 51% of the total weight, encoding the principle that a technically flawed cut that serves emotion is superior to a technically perfect cut that sacrifices it'
  - '[model] permits deliberate violation of lower-priority criteria when they conflict with higher ones, giving the practitioner a principled framework for breaking rules rather than following them blindly'
limits:
  - '[model] breaks because the six criteria and their weights were derived from one editor''s intuition about narrative cinema, and have no empirical validation -- the 51% figure is a pedagogical device, not a measurement'
  - '[model] misleads by implying that decision criteria can always be ranked in a stable linear hierarchy, when in practice the relative importance of emotion vs. story vs. rhythm shifts with genre, audience, and cultural context'
embodied_patterns:
  - part-whole
  - matching
  - scale
relation_types:
  - select
  - coordinate
structure: hierarchy
abstraction_level: specific
---

## Transfers

Walter Murch's Rule of Six, articulated in *In the Blink of an Eye*
(1995), proposes that every film edit should be evaluated against six
criteria, listed in descending priority: (1) emotion, (2) story,
(3) rhythm, (4) eye-trace, (5) two-dimensional plane of screen,
(6) three-dimensional space of action. Murch assigns emotion 51% of
the weight -- a deliberate majority stake -- and distributes the
remaining 49% across the other five. The insight is not in the
specific criteria but in the assertion that they form a strict
hierarchy, and that the editor's job is to satisfy the highest
possible criteria even at the cost of violating lower ones.

Key structural parallels:

- **The hierarchy is the tool** -- most decision frameworks list
  criteria without ranking them, which leaves the practitioner
  paralyzed when criteria conflict. Murch's contribution is to
  impose an explicit priority ordering. When rhythm demands a cut
  at frame 47 but eye-trace demands frame 52, the editor cuts at
  47 because rhythm outranks eye-trace. This transfers to any domain
  where multiple quality dimensions compete: product design (user
  delight vs. engineering elegance), hiring (culture fit vs. technical
  skill), writing (clarity vs. completeness). The model's value is
  not in Murch's specific ranking but in the discipline of ranking
  at all.

- **Emotion takes majority control** -- by assigning emotion 51%,
  Murch encodes a counterintuitive principle: technical excellence
  is subordinate to emotional truth. A cut that breaks spatial
  continuity but makes the audience feel the right thing at the
  right moment is a good cut. This transfers to any craft where
  practitioners can become so focused on technical correctness that
  they lose the human response. In software: a feature that delights
  users but has imperfect architecture may be better than one that
  satisfies every engineering principle but leaves users cold. In
  management: a decision that feels right to the team but violates
  a process may outperform the process-compliant alternative.

- **Lower criteria are expendable, not irrelevant** -- Murch does
  not say spatial continuity doesn't matter. He says it matters
  least. This permits principled compromise: the editor who violates
  continuity for emotional impact knows exactly which rule was broken
  and why. The model converts arbitrary rule-breaking into deliberate
  tradeoff-making, which transfers to any domain where "best
  practices" can become straitjackets.

- **The percentages are heuristic, not arithmetic** -- Murch's 51%
  is not a calculation but a metaphor for "more than everything else
  combined." The model teaches that in certain domains, one criterion
  should dominate so strongly that it outweighs all others. This
  transfers to strategic thinking: if your primary metric is customer
  retention, it should be worth more than all secondary metrics
  combined, not merely "the most important of several equals."

## Limits

- **The hierarchy was derived from one editor's intuition about
  narrative cinema** -- Murch edited *Apocalypse Now*, *The English
  Patient*, and *The Conversation*, all character-driven dramas. His
  hierarchy reflects that genre. In action cinema, rhythm might
  outrank emotion. In documentary, story might outrank everything.
  In experimental film, the hierarchy may invert entirely. The model
  does not account for genre-dependence, and applying it outside
  narrative drama requires substituting your own hierarchy, at which
  point you are using a different model.

- **The six criteria assume a single evaluator** -- Murch is
  describing the editor's internal decision process. When decisions
  involve multiple stakeholders with different priority hierarchies,
  the model provides no mechanism for reconciliation. A product team
  where the designer ranks emotion first, the engineer ranks
  technical soundness first, and the PM ranks story first cannot
  use the Rule of Six without first agreeing on a shared hierarchy,
  which is the hard part the model doesn't address.

- **"Emotion" is undefined** -- Murch treats emotion as
  self-evidently recognizable, but in practice it is the most
  contested criterion. What the editor considers emotionally right
  may not match the director's intent or the audience's response.
  In non-cinematic domains, the equivalent criterion -- "user
  delight," "team morale," "customer feel" -- is even harder to
  measure, making the highest-priority criterion simultaneously the
  hardest to evaluate.

- **Linear hierarchies oversimplify nonlinear interactions** --
  the six criteria interact. Rhythm affects emotion; eye-trace
  affects rhythm; spatial continuity affects story comprehension.
  Ranking them in a flat list treats them as independent when they
  are coupled. A cut that optimizes for emotion at the expense of
  spatial continuity may fail emotionally precisely because the
  audience is disoriented. The model's clean hierarchy hides these
  feedback loops.

- **The model can justify ignoring craft** -- in the hands of a
  beginner, "emotion outranks everything" can become an excuse for
  sloppy technique. Murch could afford to privilege emotion over
  continuity because his continuity was already excellent. The model
  assumes mastery of lower criteria as a precondition for
  deliberately violating them, but it does not state this explicitly.

## Expressions

- "Cut for emotion first" -- the colloquial summary of Murch's
  hierarchy, used in film schools and editing suites
- "Does it feel right?" -- the editor's test for criterion #1,
  applied before any technical evaluation
- "If it's emotionally right, the audience will forgive a lot" --
  Murch's defense of imperfect cuts that serve the scene
- "The 51% rule" -- shorthand for the principle that one criterion
  should outweigh all others combined
- "Sacrifice continuity for feeling" -- the practical directive
  that flows from the hierarchy

## Origin Story

Walter Murch developed the Rule of Six across decades of editing
work, beginning with *The Conversation* (1974) and *Apocalypse Now*
(1979). He codified it in *In the Blink of an Eye* (1995), a slim
book that became one of the most influential texts in film editing
pedagogy. Murch was unusual among editors for being both a
practitioner and a theorist -- he wanted to understand why certain
cuts worked and others didn't, and the Rule of Six was his answer.

The model gained traction beyond film because its structure -- a
strict priority hierarchy with emotion at the top -- resonated with
practitioners in design, music, and management who recognized the
same pattern in their own work: multiple quality dimensions that
compete for attention, with the most important one being the hardest
to measure.

## References

- Murch, Walter. *In the Blink of an Eye* (1995, revised 2001) --
  the primary source for the Rule of Six
- Ondaatje, Michael. *The Conversations: Walter Murch and the Art
  of Editing Film* (2002) -- extended dialogue on Murch's editing
  philosophy
