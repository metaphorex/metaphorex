---
applies_to:
- software-abstraction
author: agent:metaphorex-miner
categories:
- software-engineering
- systems-thinking
contributors:
- fshot
created: '2026-03-21'
harness: Claude Code
kind: pattern
limits:
- '[source] breaks because physical materials degrade predictably along known curves -- wood rots, stone weathers, copper patinas -- while software dependencies fail discontinuously when a maintainer abandons a project, a license changes overnight, or a security vulnerability is disclosed with no patch'
- '[source] misleads by implying that material quality is intrinsic and observable at selection time, when software dependency quality is emergent and temporal: a library that is excellent today may become a liability next year through no fault of its original design'
- '[source] assumes materials are passive recipients of wear, but software dependencies are active agents that push updates, change APIs, and introduce breaking changes -- the "material" reshapes itself while you are building with it'
name: Good Materials
provenance: alexander-pattern-language
related:
- accessible-green
- accidental-complexity
slug: good-materials
source_frame: architecture-and-building
transfers:
- '[source] imports the principle that material selection determines long-term maintenance cost, not just initial construction cost, framing technology choice as a lifecycle decision rather than a feature comparison'
- '[source] carries the structural insight that repairability requires material homogeneity and standardization -- you can patch a brick wall with matching bricks but not with proprietary composites whose manufacturer has gone bankrupt'
- '[source] establishes that good materials are those whose failure modes are visible and gradual rather than hidden and catastrophic, importing the architectural preference for honest degradation over brittle perfection'
updated: '2026-03-21'
---

## Transfers

Alexander's pattern #207, "Good Materials," argues that buildings should be
made of materials which age well, can be repaired by ordinary people with
ordinary tools, and whose properties are well understood through centuries
of use. He distrusts novel composites and proprietary systems whose long-term
behavior is unknown. The pattern is not anti-innovation; it is pro-legibility.
A material is "good" if you can predict how it will fail, fix it when it does,
and source replacements without depending on a single supplier.

Key structural parallels:

- **Lifecycle cost over acquisition cost** -- Alexander observes that cheap
  materials often cost more over a building's lifetime because they require
  frequent replacement, specialized repair, or complete removal when they fail.
  In software, choosing a dependency because it has the most features today
  ignores the maintenance cost of keeping it updated, patching its
  vulnerabilities, and migrating away when it is abandoned. The pattern
  reframes technology selection as a total-cost-of-ownership calculation.

- **Repairability requires standardization** -- a brick wall can be repaired
  by anyone who can lay bricks. A proprietary cladding system can only be
  repaired by the manufacturer. Alexander's preference for standard, widely
  understood materials maps onto the "boring technology" argument in software:
  choose PostgreSQL over a novel database not because it is better in the
  abstract, but because any developer can operate it, any consultant can
  debug it, and its failure modes are documented in thousands of postmortems.

- **Honest degradation over brittle perfection** -- good materials show their
  age visibly. Wood darkens. Stone erodes. Copper turns green. These signals
  allow preventive maintenance before catastrophic failure. In software, this
  maps to observability and graceful degradation: a well-designed system shows
  you its stress (rising latency, growing queues, increasing error rates)
  before it collapses. A system that appears perfectly healthy until it falls
  over completely is made of "bad materials" in Alexander's sense.

- **Proven over novel** -- Alexander explicitly favors materials with centuries
  of track record over materials with decades or less. The structural parallel
  is the preference for mature, battle-tested frameworks over new ones with
  impressive benchmarks but no production history. The pattern predicts that
  novelty carries hidden risks that only emerge at timescales longer than the
  initial enthusiasm cycle.

- **Sourceable from multiple suppliers** -- good materials are commodities,
  available from many vendors. Proprietary materials create vendor lock-in.
  In software, this maps to preferring open standards and widely-implemented
  protocols over single-vendor solutions. A dependency with one implementation
  controlled by one company is a proprietary composite; a dependency
  implementing an open standard is brick.

## Limits

- **Software dependencies are not passive materials** -- wood does not push
  updates to your house. A software dependency issues new versions, deprecates
  APIs, and changes behavior. The "material" metaphor frames dependencies as
  inert substances you build with, but they are more like living organisms
  with their own development trajectory. Selecting a "good material" does not
  protect you from the material deciding to change itself.

- **Quality is temporal, not intrinsic** -- Alexander can examine a piece of
  oak and assess its quality through observable properties. Software library
  quality is a function of its maintenance trajectory: current activity,
  bus factor, funding model, community health. None of these are visible in
  the artifact itself. The pattern implies that material quality can be judged
  at selection time, but software dependency quality is a bet on the future.

- **The "boring technology" argument can become an excuse for stagnation** --
  Alexander's preference for proven materials makes sense for buildings that
  stand for centuries. Software systems that last decades are rare, and the
  cost of modernization increases with age. A team that always chooses the
  oldest, most proven technology may find itself unable to hire developers
  or integrate with modern systems. The pattern does not account for
  ecosystem evolution that makes "proven" materials obsolete.

- **Repairability in software is not just a materials problem** -- a brick
  wall is repairable because the interface between bricks is simple (mortar).
  Software repairability depends on architecture (modularity, encapsulation,
  clear interfaces), not just on the quality of individual components. You
  can build an unrepairable system entirely from "good materials" if the
  architecture is tangled. The pattern overstates the contribution of
  component selection relative to structural design.

## Expressions

- "Boring technology" -- Dan McKinley's essay, the direct software descendant
  of Alexander's preference for proven materials
- "Battle-tested" -- the military-architectural metaphor for software that has
  survived production use, Alexander's centuries of track record compressed
  into deployment cycles
- "Vendor lock-in" -- the proprietary-materials problem applied to cloud
  services and single-source dependencies
- "Technical debt" -- the accumulated cost of choosing materials that cannot
  be cheaply maintained or replaced, Alexander's lifecycle cost made visible
- "Choose the right tool for the job" -- the folk version of Alexander's
  material selection principle, though it often ignores his emphasis on
  repairability and longevity

## Origin Story

Pattern #207 in *A Pattern Language* (1977) reflects Alexander's deep
suspicion of industrial building materials -- plywood, synthetic composites,
proprietary cladding systems -- that promised performance but delivered
opacity. He observed that traditional materials (brick, stone, wood, tile)
had known failure modes, could be repaired locally, and aged in ways that
people found acceptable or even beautiful. The pattern anticipated the
software industry's recurring discovery that novel, high-performance
dependencies create maintenance burdens that outweigh their initial
advantages -- a lesson relearned with every abandoned framework and
every left-pad incident.

## References

- Alexander, Christopher. *A Pattern Language* (1977), Pattern #207:
  Good Materials
- McKinley, Dan. "Choose Boring Technology" (2015) -- the software
  equivalent of Alexander's proven-materials argument
- Henney, Kevlin. "Old Is the New New" (various talks) -- on the value
  of mature technology in software
