---
slug: catch-and-store-energy
name: Catch and Store Energy
kind: mental-model
categories:
- systems-thinking
- biology-and-ecology
author: agent:metaphorex-miner
contributors: []
related:
- observe-and-interact
- make-hay-while-the-sun-shines
provenance: agricultural-proverbs
created: '2026-03-20'
updated: '2026-03-20'
grounding: established
harness: Claude Code
embodied_patterns:
  - container
  - flow
  - accretion
relation_types:
  - accumulate
  - contain
  - enable
structure: cycle
abstraction_level: generic
transfers:
  - '[model] resources arrive in pulses -- sun, rain, seasonal abundance -- and must be captured during the pulse and stored in durable form for use during scarcity, importing the structure where value creation depends on recognizing temporal asymmetry between supply and demand'
  - '[model] storage always involves transformation and loss -- grain must be dried to prevent rot, water must be contained to prevent evaporation -- importing the structure where preservation requires active investment and every storage medium has characteristic decay rates'
  - '[model] the ratio of capture capacity to pulse magnitude determines system resilience -- a cistern too small for the rainstorm wastes most of the water -- importing the structure where preparedness is measured by infrastructure built before the abundance arrives'
limits:
  - '[model] breaks in domains where the resource is non-depletable or always available on demand -- digital information can be copied at near-zero cost and does not degrade -- because the principle assumes scarcity cycling between abundance and shortage'
  - '[model] misleads when it encourages hoarding by framing all accumulation as prudent storage, because the agricultural original assumes a known cycle (seasons) while many domains lack predictable scarcity rhythms, making it impossible to distinguish stockpiling from waste'
---

## Transfers

Catch and Store Energy is Holmgren's second permaculture design principle.
In its agricultural origin, the instruction is about infrastructure: build
the pond before the rains come, dry the grain before the mold sets in,
plant the windbreak before winter. Energy and resources arrive in pulses --
sunlight is abundant in summer, rain falls in storms, fruit ripens all at
once -- and the farmer's core challenge is capturing these pulses in durable
form for use when the supply stops.

The principle articulates a structure that appears across many domains:

- **Knowledge management.** Lessons learned from a project are abundant
  during the retrospective and scarce six months later when the next
  project needs them. The "energy" is institutional knowledge; the
  "storage" is documentation, wikis, or trained people. Organizations that
  do not capture knowledge when it is fresh lose it to turnover and
  forgetting -- the intellectual equivalent of letting grain rot in the
  field.
- **Financial planning.** "Make hay while the sun shines" and "save for a
  rainy day" are folk expressions of the same principle. Income arrives
  unevenly; expenses arrive continuously. The structure of catch-and-store
  applies directly: surplus in good periods must be converted into reserves
  for lean ones.
- **Software engineering.** Caching, buffering, and queuing are all
  catch-and-store patterns. A CDN caches content close to users during
  low-traffic periods so it is available during demand spikes. A message
  queue stores events during bursts so downstream processors can consume
  them at a sustainable rate.
- **Attention and learning.** Insight arrives in bursts -- during reading,
  conversation, or focused work -- and decays rapidly if not captured.
  Note-taking, journaling, and spaced repetition are storage technologies
  for cognitive energy that would otherwise dissipate.

The key structural insight is the temporal mismatch between supply and
demand. The principle names the discipline of building capture and storage
infrastructure during the interval between pulses, when the need for it
is not yet felt.

## Limits

- **Not all resources are cyclical.** The principle assumes alternating
  abundance and scarcity with a predictable rhythm. This fits agriculture
  (seasons), energy (day/night), and some economic cycles, but not domains
  where abundance is secular (information on the internet) or where scarcity
  is permanent (water in a desert with no rainy season). Applying
  catch-and-store to an always-abundant resource produces unnecessary
  hoarding.
- **Storage has costs that the principle underemphasizes.** Every storage
  medium degrades, consumes maintenance energy, and occupies space. Grain
  silos attract pests. Knowledge bases go stale. Financial reserves earn
  below-market returns. The principle emphasizes the cost of not storing
  but underplays the cost of storing, which can lead to over-investment
  in inventory and reserves at the expense of current operations.
- **The principle does not distinguish between storing and hoarding.**
  In agriculture, the distinction is clear: you store enough grain to
  survive until next harvest, and surplus beyond that is waste or trade
  goods. In other domains -- capital, information, talent -- the boundary
  between prudent reserves and pathological accumulation is ambiguous.
  Organizations that internalize catch-and-store without a release mechanism
  become stagnant rather than resilient.
- **Transformation losses are not uniform.** The principle implies that
  captured energy can be stored with acceptable loss. But some forms of
  energy resist storage entirely: team morale cannot be banked, creative
  momentum cannot be frozen and thawed, and trust cannot be stockpiled
  for future withdrawal. The principle works best for material and
  informational resources and poorly for relational and emotional ones.

## Expressions

- "Make hay while the sun shines" -- folk agricultural encoding of
  the catch-and-store imperative (English proverb, attested 1546)
- "Save for a rainy day" -- financial catch-and-store (English proverb)
- "Build the cistern before the rains" -- permaculture instruction on
  infrastructure timing (Holmgren, 2002)
- "Document while the knowledge is fresh" -- knowledge management
  application of the same temporal logic (organizational best practice)
- "Cache invalidation is one of the two hard problems" -- software
  engineering acknowledgment that storage creates its own complexity
  (attributed to Phil Karlton)

## Origin Story

Holmgren codified Catch and Store Energy as Principle 2 in *Permaculture:
Principles and Pathways Beyond Sustainability* (2002). The principle
generalizes from the most fundamental challenge of pre-industrial
agriculture: how to survive the period between harvests. Every agricultural
civilization developed storage technologies -- granaries in Egypt, root
cellars in Northern Europe, dried fish in Scandinavia -- and the adequacy
of these stores was often the difference between survival and famine.

The metaphorical extension to energy is Holmgren's innovation. By framing
the principle in terms of energy rather than just food, he connected
agricultural wisdom to thermodynamics: energy flows through systems and
dissipates unless captured and stored in a more durable form. This framing
makes the principle applicable to any domain where resources arrive in
pulses and must be preserved across intervals of scarcity.

## References

- Holmgren, D. *Permaculture: Principles and Pathways Beyond Sustainability*
  (2002) -- Principle 2
- Mollison, B. *Permaculture: A Designers' Manual* (1988) -- foundational
  permaculture design
- Meadows, D. *Thinking in Systems: A Primer* (2008) -- stocks and flows
  as the general form of catch-and-store
