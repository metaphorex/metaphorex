---
slug: side-effects
name: Side Effects
summary: "Pharmacological center/periphery hierarchy mapped onto unintended consequences; the spatial 'side' demotes them by design"
kind: metaphor
dead: true
source_frame: medicine
applies_to:
- decision-making
- software-engineering
categories:
- health-and-medicine
- philosophy
author: agent:metaphorex-miner
contributors: []
related:
- triage
- do-as-much-nothing-as-possible
provenance: scheins-surgical-aphorisms
created: '2026-03-20'
updated: '2026-03-20'
grounding: established
harness: Claude Code
transfers:
  - '[source] a drug acts on the entire body but is prescribed for a specific target organ, so the pharmacologist distinguishes the intended therapeutic effect from the unintended effects on other systems, importing the structure where an intervention has a declared purpose and everything else it does is spatially pushed to the side'
  - '[source] the "side" in side effect encodes a spatial metaphor of centrality -- the therapeutic effect is the main event, other effects are peripheral -- importing a hierarchy of attention where some consequences are structurally designated as less important regardless of their actual magnitude'
  - '[source] pharmacological side effects are dose-dependent and predictable from the drug''s mechanism of action, importing the structure where unintended consequences are knowable in advance if one understands the system, not random bad luck'
limits:
  - '[source] breaks because pharmacological side effects are genuinely secondary to the drug''s mechanism of action -- aspirin reduces inflammation (primary) and thins blood (side) because COX inhibition has both consequences -- while in policy and software the "side effects" are often just effects the designer chose not to think about, not effects that are structurally peripheral'
  - '[source] misleads by importing a frame of inevitability: in medicine, side effects are accepted because the underlying mechanism cannot be made more selective with current technology, but in software and policy the "side effects" can often be eliminated by better design rather than tolerated as unavoidable'
  - '[source] obscures accountability by naturalizing the framing: calling something a "side effect" implies it was an unavoidable consequence of an otherwise good action, foreclosing the question of whether the actor should have anticipated and prevented it'
embodied_patterns:
  - matching
  - surface-depth
  - balance
relation_types:
  - cause
  - transform
structure: boundary
abstraction_level: specific
---

## Transfers

"Side effect" entered English medical vocabulary in the early twentieth
century to describe the pharmacological effects of a drug on organs and
systems other than the intended therapeutic target. The spatial metaphor
is precise: the desired effect is "main" or "central," and everything
else is pushed to the "side" -- peripheral, secondary, tolerated. The
term is now so thoroughly dead that it requires effort to hear the
spatial metaphor at all. People speak of "the side effects of the
policy," "the side effects of remote work," and "side effects in code"
without any awareness that they are importing a pharmacological model of
centrality and periphery.

Key structural parallels:

- **The center/periphery hierarchy** -- the most powerful feature of
  the metaphor is not that it acknowledges unintended consequences
  (any frame can do that) but that it spatially ranks them. The
  therapeutic effect is "main"; everything else is "side." This
  hierarchy is built into the word itself and transfers wherever the
  metaphor goes. When a product manager speaks of "side effects" of
  a feature launch, they are not merely noting unintended consequences
  but linguistically demoting them to peripheral status. The metaphor
  licenses inattention by design.
- **Predictability from mechanism** -- a pharmacologist who understands
  how a drug works can predict its side effects. Aspirin inhibits
  cyclooxygenase; this reduces inflammation (main effect) and thins
  blood (side effect) because COX is active in both systems. The
  side effect is not random; it is mechanistically entailed. The
  metaphor imports this into software ("side effects" of a function
  are the state changes beyond its return value) and policy
  ("side effects" of regulation are the downstream consequences
  predictable from the mechanism). In both cases, the framing implies
  that the consequences were knowable, which introduces accountability
  even as the word "side" tries to diminish it.
- **The therapeutic bargain** -- in medicine, side effects are
  tolerated because the main effect is valuable enough to justify them.
  The patient accepts nausea because the chemotherapy shrinks the tumor.
  The metaphor imports this bargaining structure: calling something a
  "side effect" frames it as the acceptable price of a greater good.
  This transfers to organizational decisions where leaders tolerate
  team disruption as a "side effect" of restructuring, or policymakers
  accept unemployment as a "side effect" of inflation control.

## Limits

- **Most metaphorical "side effects" are just effects** -- in
  pharmacology, the distinction between main effect and side effect is
  grounded in the drug's molecular mechanism and the prescriber's
  therapeutic intent. Aspirin's blood-thinning is genuinely a
  consequence of the same mechanism that reduces inflammation -- the
  "side" designation reflects real biochemistry. In policy, technology,
  and organizational management, the distinction is almost always
  about the actor's attention rather than the system's structure.
  When a factory's pollution is called a "side effect" of production,
  the spatial metaphor frames environmental damage as peripheral to
  the "main" activity of manufacturing. But ecologically, the
  pollution is not peripheral -- it is a direct output of the same
  process. The medical metaphor provides a vocabulary for dismissing
  primary consequences as secondary ones.
- **The frame naturalizes avoidable harm** -- medical side effects
  often cannot be eliminated with current pharmacology because the
  drug's mechanism is insufficiently selective. The metaphor imports
  this inevitability into domains where it does not apply. A software
  function's side effects (writing to disk, modifying global state)
  can be eliminated by pure functional design. A policy's "side
  effects" on vulnerable populations can be mitigated by inclusive
  design. Calling these "side effects" frames them as the unavoidable
  cost of mechanism rather than design choices that could be made
  differently.
- **It forecloses accountability** -- "the policy had unfortunate
  side effects" places the consequences in a grammatical structure
  where no agent caused them. The policy acted; the side effects
  happened. The medical frame, where side effects genuinely are
  properties of the drug rather than decisions of the prescriber,
  licenses this agentless grammar. But in organizations, someone
  designed the policy, someone could have modeled the consequences,
  and someone chose not to. The dead metaphor provides rhetorical
  cover for this evasion.
- **In computer science, "side effect" is precise but inverted** --
  functional programming defines "side effect" as any observable state
  change beyond a function's return value. Here the metaphor has been
  revived and given technical precision: the "main" effect is the
  return value, and "side" effects are I/O, mutation, and state change.
  But the value hierarchy is inverted from medicine -- in software,
  side effects are often the entire point (writing to a database,
  displaying to a screen). The medical framing of "side = lesser"
  creates a misleading connotation in a domain where side effects
  are frequently the primary purpose.

## Expressions

- "Side effects may include..." -- the pharmacological disclaimer,
  now parodied so widely it has become a cultural template for listing
  unintended consequences
- "Side effects of the policy" -- standard political and organizational
  usage, fully dead as a metaphor
- "Function with side effects" -- computer science term for a function
  that modifies state beyond its return value
- "Side-effect free" -- functional programming's ideal, meaning a
  function that produces only its return value with no external state
  changes
- "That's a feature, not a side effect" -- the ironic inversion,
  reframing an unintended consequence as a deliberate benefit
- "Collateral damage" -- the military synonym, importing a different
  spatial metaphor (lateral vs. central) for the same structural idea

## Origin Story

The term "side effect" (German: *Nebenwirkung*, literally "beside-effect")
emerged in pharmacology in the late nineteenth and early twentieth century
as the science of drug action became precise enough to distinguish a
drug's intended therapeutic target from its broader physiological impact.
Paul Ehrlich's concept of the "magic bullet" (1900) -- a drug that would
target only the diseased tissue -- defined the ideal against which
"side effects" were the acknowledged failure of selectivity.

The metaphor crossed into general English by mid-century and was fully
dead by the 1970s. Today it is the default frame for unintended
consequences in policy, technology, and organizational life. Its death
is so complete that the spatial metaphor ("side") is invisible, and
alternative framings -- "secondary effects," "externalities," "unintended
consequences" -- each carry their own metaphorical baggage without
replacing the pharmacological original.

The term's migration into computer science (via the lambda calculus
and functional programming traditions of the 1960s-1970s) gave it a
second, more precise life. In this domain, "side effect" is a technical
term with a formal definition, even as it retains the connotation of
something undesirable inherited from medicine.

## References

- Ehrlich, Paul. "Chemotherapy" (1900) -- the "magic bullet" concept
  that defines the ideal of effect without side effect
- Church, Alonzo. *The Calculi of Lambda Conversion* (1941) -- the
  formal foundation for the CS usage of "side effect"
- Schein, Moshe. *Aphorisms & Quotations for the Surgeon*. tfm
  Publishing, 2003 -- documents the medical tradition
