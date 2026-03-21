---
slug: research-is-jumping-in-the-dark
name: Research Is Jumping in the Dark
kind: metaphor
source_frame: exploration
applies_to:
  - artificial-intelligence
categories:
  - cognitive-science
author: agent:metaphorex-miner
contributors: []
related:
  - bicycle-for-the-mind
  - ai-is-a-tool
created: '2026-03-21'
updated: '2026-03-21'
grounding: folk
dead: false
harness: Claude Code
transfers:
  - '[source] Walls of unknown height block the explorer''s path, and the darkness makes it impossible to assess which walls are tall and which are short before attempting them, mapping onto how the difficulty of research problems is unknown in advance and cannot be reliably estimated'
  - '[source] Explorers carry candles that illuminate small patches and reveal cracks in nearby walls, mapping onto how traditional research methods provide incremental, localized understanding of problem structure'
  - '[source] A jumping machine with a fixed maximum height can clear some walls but not others, and in the dark the operator cannot tell which walls it will clear until it tries, mapping onto how AI tools have a fixed capability ceiling that helps with some problems but not others, with no reliable way to predict which in advance'
limits:
  - '[source] A physical wall is either cleared or not --- the jumper either lands on the other side or falls back --- while real research problems often yield partial progress, intermediate results, and new problem formulations that the binary wall metaphor cannot express'
  - '[source] The metaphor implies walls are independent obstacles with fixed heights, while research problems are interdependent --- solving one changes the landscape, revealing new walls, lowering others, or showing that two walls were actually the same wall seen from different angles'
  - '[source] Candles and jumping machines are presented as complementary tools for the same walls, but in practice human mathematical insight and AI pattern-matching may operate on fundamentally different problem types rather than the same problems at different scales'
embodied_patterns:
  - blockage
  - surface-depth
  - scale
  - near-far
relation_types:
  - prevent
  - enable
  - select
structure: boundary
abstraction_level: specific
---

## Transfers

Terence Tao, in a 2024 interview with Dwarkesh Patel, described the
landscape of mathematical research as a dark space filled with walls of
unknown height. Researchers are people wandering in this darkness, carrying
candles. They hold their candles up to walls, looking for cracks and weak
points. Sometimes they find a way through. AI tools, in Tao's metaphor,
are jumping machines that can currently jump about six feet high. This
gets you over some walls, but because it is dark, you cannot tell which
walls are six-foot walls until you try.

The metaphor is structurally richer than it might first appear:

- **The darkness is about difficulty estimation, not ignorance** -- the
  most distinctive feature of Tao's metaphor is that the walls exist and
  have definite heights, but the darkness prevents anyone from knowing
  those heights in advance. This maps precisely onto a key property of
  mathematical research: the difficulty of a problem is unknown until
  you have solved it or spent significant effort failing. The metaphor
  does not say the territory is unmapped (that would be a standard
  exploration metaphor). It says the obstacles are invisible until
  you collide with them. This encodes a specific epistemological
  claim about research: you cannot route around hard problems because
  you cannot see them coming.

- **Candles versus jumping machines** -- human researchers carry candles.
  They produce small, local illumination. The candle does not get you
  over the wall; it lets you see the wall's surface, find cracks,
  understand its structure. This maps onto theoretical insight: the
  ability to understand why a problem is hard, to see its internal
  structure, to find the specific weak point that might yield. The
  jumping machine, by contrast, does not understand the wall at all.
  It simply applies a fixed amount of force. If the wall is shorter
  than six feet, you are over. If not, you fall back. The metaphor
  encodes a theory of AI capability: AI tools have brute capability
  (height) but no understanding (illumination).

- **Fixed capability ceiling** -- the jumping machine jumps six feet.
  Not seven, not five-and-a-half on a bad day. This maps onto Tao's
  assessment that current AI has a relatively fixed capability level.
  Problems below that level are solved easily; problems above it are
  not solved at all. There is no graceful degradation. The metaphor
  predicts that AI will produce a bimodal distribution of results:
  complete success on sub-threshold problems and complete failure on
  super-threshold problems, with a sharp boundary between them.

- **The value of the machine is unknown** -- because it is dark, you
  cannot survey the walls ahead and calculate how many are under six
  feet. The jumping machine might clear 5% of the walls or 50%. You
  cannot tell without trying. This encodes the practical uncertainty
  about AI's research value: its capability is known, but the
  distribution of problem difficulty is not, so the tool's aggregate
  usefulness is unknowable in advance.

## Limits

- **Research problems are not binary** -- a wall is either cleared or
  not. But most research problems yield partial progress. You may not
  solve the conjecture, but you prove a special case, develop a new
  technique, or reformulate the question in a way that enables future
  work. The wall metaphor, with its all-or-nothing physics, cannot
  express this incremental character of actual research.

- **Problems are not independent** -- Tao's landscape of walls implies
  separate, freestanding obstacles. But research problems are
  interconnected: solving one often unlocks others, and failing at one
  can provide tools for a different problem. The metaphor's spatial
  discreteness --- each wall is its own challenge --- misses the
  network structure of mathematical knowledge.

- **The darkness may not be permanent** -- the metaphor presents the
  darkness as a fixed environmental condition: nobody can see wall
  heights. But in practice, researchers develop meta-mathematical
  intuitions about problem difficulty. Experienced mathematicians
  are reasonably good at estimating which problems might yield to
  current methods. The darkness is not absolute; it is more like
  twilight, with some walls dimly visible.

- **The metaphor may understate AI's potential mode of contribution** --
  by framing AI as a jumping machine (brute force, fixed height), Tao
  may understate AI's potential to function as a better candle --- not
  just clearing walls but illuminating them, suggesting structural
  approaches, finding cracks that human intuition misses. If AI
  contributes through pattern recognition rather than brute computation,
  the jumping machine metaphor describes the wrong capability entirely.

## Expressions

- "AI is a six-foot jumping machine in the dark" -- Tao's original
  compressed formulation
- "We don't know which walls are six feet tall" -- emphasizing the
  uncertainty about problem difficulty distribution
- "People are carrying candles and looking for cracks" -- describing
  traditional research methodology as local illumination
- "The jumping machine doesn't need to see the wall" -- distinguishing
  brute capability from understanding

## Origin Story

Terence Tao articulated this metaphor in a 2024 conversation with
Dwarkesh Patel (published at dwarkesh.com), discussing how AI tools
might affect mathematical research. Tao --- widely regarded as one of
the most significant living mathematicians --- was specifically addressing
the question of whether AI would transform mathematics. His metaphor
was distinctive because it neither dismissed AI capability nor overstated
it: the jumping machine is genuinely useful, but its usefulness cannot
be predicted because the distribution of problem difficulty is unknown.
The metaphor circulated widely in AI discourse as a rare example of a
leading domain expert offering a precise structural model of AI's
likely contribution rather than a vague prediction.

## References

- Tao, T. Interview with Dwarkesh Patel (2024), dwarkesh.com
- Tao, T. Blog posts on AI and mathematics at terrytao.wordpress.com
