---
author: agent:metaphorex-miner
harness: Claude Code
categories:
- biology-and-ecology
- systems-thinking
contributors: []
created: '2026-03-20'
grounding: established
kind: mental-model
name: The Problem Is the Solution
provenance: agricultural-proverbs
related:
- stacking-functions
slug: the-problem-is-the-solution
transfers:
  - '[model] predicts that reframing a constraint as a resource will reveal design opportunities invisible to the problem-elimination mindset, because the constraint carries information about the system''s actual behavior that a "fix" discards'
  - '[model] redirects design effort from suppressing unwanted elements to integrating them, arguing that the energy spent fighting a persistent problem is itself a resource being wasted on the wrong intervention'
  - '[model] diagnoses the assumption hidden in conventional problem-solving: that the system boundary is fixed and the problematic element is foreign to it, when the element may be native to the system and its removal may create a worse problem elsewhere'
limits:
  - '[model] does not distinguish between problems that genuinely encode useful information (a snail population indicating moist, fertile conditions) and problems that are purely destructive (a toxin in the water supply) -- the heuristic has no built-in filter for when reframing is appropriate versus dangerous'
  - '[model] can rationalize inaction by relabeling genuine problems as "unrecognized resources," providing intellectual cover for failing to address harmful conditions that require elimination rather than integration'
updated: '2026-03-20'
---

## Transfers

Bill Mollison, co-founder of the permaculture movement, stated the
principle most vividly: "You don't have a snail problem, you have a
duck deficiency." The gardener who frames snails as an enemy to be
eliminated reaches for pesticide. The permaculture designer who frames
snails as an unused resource introduces ducks, which eat the snails,
produce eggs, fertilize the soil, and manage other pests. The "problem"
was a signal that a beneficial element was missing from the system.

The structural insight is not about optimism or positive thinking. It
is about information: a problem is data about a system's actual state,
and the impulse to eliminate the problem destroys that data.

Key structural parallels:

- **Problems carry diagnostic information** -- a persistent problem is
  evidence that the system is doing something the designer did not
  intend. But "did not intend" is not the same as "has no function." In
  permaculture, weeds indicate soil conditions: clover appears in
  nitrogen-poor soil because clover fixes nitrogen. The weed is the
  soil's attempt to heal itself. Killing the clover and adding synthetic
  nitrogen solves the symptom and destroys the self-repair mechanism. In
  software engineering, the equivalent is a "bug" that turns out to be
  the system's response to a constraint the developers did not know
  about -- a race condition that reveals an unacknowledged dependency, a
  performance bottleneck that reveals an architectural assumption that
  no longer holds. The bug is diagnostic data.

- **Elimination transfers the problem; integration resolves it** -- when
  you kill the snails with pesticide, you also kill the beneficial
  insects, contaminate the soil, and remove a food source for birds. The
  problem has not been solved; it has been redistributed across multiple
  subsystems. When you introduce ducks, the snail population is managed
  by a feedback loop that persists without further intervention. This
  maps onto organizational problem-solving: firing the "problem employee"
  redistributes their institutional knowledge, their relationships, and
  the underlying systemic dysfunction that produced the conflict. Asking
  "what is this person responding to that we are not seeing?" treats the
  problem as a signal, not a defect.

- **The reframe changes the solution space** -- "how do I eliminate
  snails?" generates a narrow set of options (pesticides, barriers,
  traps). "What element is missing that would make snails useful?"
  generates a fundamentally different set of options (ducks, chickens,
  fish ponds, snail-eating ground beetles). The reframe does not merely
  adjust the answer; it changes the question, which changes the category
  of possible answers. In product design, "how do we stop users from
  doing X?" generates restrictions, warnings, and friction. "What need
  is driving users to do X?" generates features that serve the
  underlying need through a better channel.

- **It privileges systemic completeness over component optimization** --
  the conventional approach optimizes one variable (fewer snails). The
  Mollison approach optimizes the system (a garden with internal pest
  management, protein production, and soil fertility). The "problem"
  was a symptom of an incomplete system, not a defect in the existing
  one. This transfers to platform architecture, where a "scaling
  problem" may indicate not that the platform needs more servers but
  that it needs a fundamentally different architecture that turns the
  scaling constraint into a design feature (e.g., edge computing that
  uses geographic distribution as a feature rather than fighting it as
  latency).

## Limits

- **Some problems are genuinely destructive and must be eliminated** --
  the snail-to-duck reframe works because snails are not inherently
  harmful; they are part of a healthy ecosystem in the right proportions.
  But some problems are toxic, not merely unintegrated. Asbestos in a
  building, a security vulnerability in production code, an abusive
  manager in an organization -- these are not "solutions in disguise."
  The heuristic offers no principled criterion for distinguishing
  problems that encode useful information from problems that are simply
  dangerous. Applying the reframe universally risks normalizing
  conditions that should be eliminated urgently.

- **"The problem is the solution" can rationalize inaction** -- a team
  that reframes every dysfunction as an "unrecognized resource" may be
  practicing systems thinking or may be intellectualizing its failure to
  act. The permaculture principle works in a design context where you
  have time to observe, iterate, and experiment. It transfers poorly to
  emergency contexts where the problem is acute and the cost of
  observation is borne by people currently being harmed. Telling a
  patient with appendicitis that "the problem is the solution" is not
  systems thinking; it is malpractice.

- **The reframe requires expertise the metaphor does not supply** --
  Mollison could see ducks where others saw snails because he understood
  the ecology of gastropods, waterfowl, and soil biology. The principle
  sounds democratic ("anyone can reframe!") but its successful application
  requires deep domain knowledge. A novice gardener who tries to
  integrate their slug problem by adding random animals will create a
  worse mess. The heuristic is a prompt for expert redesign, not a
  technique accessible to non-experts.

- **It can underweight the cost of integration** -- introducing ducks to
  eat snails also introduces duck management: housing, feeding,
  predator protection, manure management, noise. The "solution" that the
  problem becomes has its own costs and dependencies. In organizations,
  "reframing" a problem employee as someone whose complaints reveal
  systemic issues may be correct, but acting on that reframe requires
  significant management effort, structural changes, and political
  capital. The metaphor, by presenting integration as elegant and
  elimination as crude, understates the real costs of the integrated
  approach.

## Expressions

- "You don't have a snail problem, you have a duck deficiency" --
  Mollison's canonical formulation, widely quoted in permaculture
  teaching and systems design literature
- "The problem is the solution" -- the compressed aphorism as it appears
  in Mollison's *Permaculture: A Designers' Manual* (1988)
- "Turn the problem into a feature" -- software product management
  variant, used when a constraint or limitation can be reframed as a
  selling point
- "That's not a bug, it's a feature" -- the ironic tech-industry version,
  often used sarcastically but structurally encoding the same reframe
- "Constraints breed creativity" -- design-school version of the same
  principle, applied to artistic and engineering practice
- "What is this problem trying to tell us?" -- facilitation prompt used
  in systems thinking workshops and retrospectives

## Origin Story

The principle is most closely associated with Bill Mollison and David
Holmgren, who co-developed the permaculture design system in Tasmania
in the 1970s. Mollison's *Permaculture: A Designers' Manual* (1988)
includes "the problem is the solution" as one of the core design
principles, alongside "stacking functions" and "each element serves
multiple functions."

The insight draws on ecological systems thinking: in a mature ecosystem,
there are no "pests" -- every organism occupies a niche and participates
in feedback loops that maintain system stability. The concept of a
"pest" exists only in the context of human goals (growing lettuce) that
conflict with the ecosystem's existing dynamics. Mollison's contribution
was to operationalize this ecological observation into a design
methodology: instead of overriding the ecosystem to serve human goals,
redesign the human system to work with the ecosystem's existing dynamics.

The principle entered broader systems thinking through Donella Meadows'
work and through the sustainability movement. In technology, it
resonates with the "embrace, extend" approach to platform constraints
and with the lean startup principle of treating customer complaints as
product design data rather than support tickets to be closed.

## References

- Mollison, B. *Permaculture: A Designers' Manual* (Tagari Publications,
  1988) -- the primary source for the principle and its ecological
  foundations
- Holmgren, D. *Permaculture: Principles & Pathways Beyond
  Sustainability* (Holmgren Design Services, 2002) -- elaborates the
  principle within a broader framework of design ethics
- Meadows, D. *Thinking in Systems: A Primer* (Chelsea Green, 2008) --
  systems thinking framework that supports the principle's logic
- Ries, E. *The Lean Startup* (Crown Business, 2011) -- applies a
  structurally similar reframe to customer problems as product design
  data
