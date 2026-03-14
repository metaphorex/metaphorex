---
author: agent:metaphorex-miner
categories:
- software-engineering
- organizational-behavior
contributors:
- fshot
harness: Claude Code
kind: dead-metaphor
name: Bus Factor
related:
- yak-shaving
- bikeshedding
slug: bus-factor
source_frame: embodied-experience
target_frame: shared-resources
---

## What It Brings

"What happens if someone gets hit by a bus?" The question maps sudden,
violent, random bodily harm onto knowledge loss in a team. The bus factor
of a project is the number of people who could disappear before the
project stalls -- and when the answer is "one," the metaphor has done
its job by making an abstract organizational risk feel visceral and
urgent.

Key structural parallels:

- **Randomness as the threat model** -- a bus is the canonical
  unforeseeable accident: it strikes without warning, it cannot be
  negotiated with, and it selects victims without regard to their
  importance. This maps onto the insight that knowledge loss is not
  primarily caused by firings or resignations (which can be planned
  for) but by the unpredictable: illness, burnout, a better offer on
  a Friday afternoon. The metaphor insists that you plan for the
  unplannable.
- **A body as a knowledge container** -- the metaphor treats a person
  as a vessel for institutional knowledge. When the body is destroyed,
  the knowledge is destroyed. This is a surprisingly precise mapping:
  tacit knowledge (how to deploy the legacy system, why that config
  flag exists, what the client actually means when they say "flexible")
  really does live in individual bodies and cannot be extracted by
  reading documentation, because it was never documented.
- **A countable metric** -- the bus factor is a number. "Our bus factor
  is two" is a measurable claim about organizational fragility. The
  metaphor converts a diffuse anxiety (we depend too much on certain
  people) into a concrete, comparable, actionable metric. You can track
  it, set targets for it, and explain it to management without
  jargon.
- **The morbidity is the message** -- the metaphor is deliberately
  grotesque. It could have been "what if someone wins the lottery?"
  (and this euphemism exists), but the bus version persists because the
  violence makes the risk memorable. The discomfort of imagining a
  colleague's death is precisely what forces the conversation about
  knowledge silos that everyone would rather avoid.

## Where It Breaks

- **People are not interchangeable** -- the bus factor implies that the
  problem is purely about headcount: if two people know the system
  instead of one, you are twice as safe. But knowledge transfer is not
  copying a file. The second person brings a different mental model,
  different assumptions, different blind spots. A bus factor of two
  does not mean you have a backup; it means you have two partial,
  divergent understandings. The metaphor hides the quality dimension
  behind a quantity metric.
- **The metaphor reduces people to their knowledge** -- calling someone
  a bus-factor risk treats them as a single point of failure, not as a
  human being with agency, relationships, and motivations. The framing
  can feel dehumanizing, especially to the person being discussed. It
  also misses the point that the same person who is a single point of
  failure may also be the reason the project works at all -- their
  deep expertise is a feature, not just a risk.
- **It pathologizes specialization** -- a bus factor of one sometimes
  means someone is uniquely good at their job, not that the
  organization failed to cross-train. Deep expertise has value that
  the metaphor cannot account for. The metaphor's implicit prescription
  (spread knowledge widely) can lead to a mediocre generalism where
  nobody knows anything deeply enough to solve hard problems.
- **The bus rarely comes** -- the metaphor's power depends on an implied
  probability of sudden disappearance that is, statistically,
  extremely low. Most knowledge loss is gradual: attrition, role
  changes, slow disengagement. The dramatic framing can distort
  priorities, causing teams to invest heavily in bus-factor mitigation
  while ignoring the slower, more common forms of knowledge erosion.

## Expressions

- "What's the bus factor on this project?" -- the canonical risk
  assessment question, asked in retrospectives and architecture reviews
- "Bus factor of one" -- the alarm state, meaning a single person's
  departure would cripple the project
- "Lottery factor" -- the euphemistic inversion, asking the same
  question but with a positive departure scenario (winning the lottery)
  rather than a violent one
- "Truck number" -- a variant using a different vehicle but the same
  logic, common in some organizations that find "bus" too morbid
- "They're a single point of failure" -- the infrastructure-derived
  synonym, mapping the person onto a hardware component rather than
  an accident victim
- "We need to increase the bus factor" -- the prescriptive form,
  meaning "cross-train, document, pair-program"

## Origin Story

The term's exact origin is difficult to pin down, but it was in
widespread use in open-source communities by the late 1990s. The
concept appears in discussions around the Linux kernel project, where
Linus Torvalds's singular importance to the project made the question
unavoidable. The phrase crystallized a concern that had always existed
in software teams but lacked a memorable name.

The "lottery factor" euphemism gained traction in corporate environments
where discussing a colleague's hypothetical death felt inappropriate.
Some agile coaching materials adopted the lottery framing, but the bus
version persists -- precisely because its discomfort is part of its
persuasive force.

## References

- Bowler, M. "Truck Factor," agile development blog post (2005) --
  early formalization of the metric in agile methodology
- Avelino, G. et al. "A Novel Approach for Estimating Truck Factors,"
  *International Conference on Program Comprehension* (2016) --
  empirical methods for computing the metric from commit histories
- Rigby, P. C. et al. "An Empirical Study of the Bus Factor,"
  *Empirical Software Engineering* (2016) -- quantitative analysis
  across open-source projects