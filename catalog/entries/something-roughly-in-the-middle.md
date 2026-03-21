---
slug: something-roughly-in-the-middle
name: Something Roughly in the Middle
kind: pattern
source_frame: architecture-and-building
applies_to:
  - software-abstraction
  - organizational-behavior
categories:
  - systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
  - alcoves
  - common-areas-at-the-heart
created: '2026-03-19'
updated: '2026-03-19'
grounding: established
harness: Claude Code
transfers:
  - '[source] establishes that any collective space needs a physical anchor -- a fountain, a tree, a kiosk -- that gives people a reason to move toward the center rather than drifting to the edges'
  - '[source] carries the insight that the anchor need not be geometrically centered or symmetrically placed; "roughly" is load-bearing because an off-center anchor generates more natural circulation than a formally centered one'
  - '[source] imports the principle that the anchor must be a thing people interact with, not merely a landmark to look at, because gathering requires a pretext and passive monuments do not provide one'
limits:
  - '[source] breaks because physical spaces have a single perceivable center while digital and organizational spaces often have no spatial intuition at all, making "the middle" a metaphor that must be constructed rather than discovered'
  - '[source] misleads by implying that a single anchor suffices for any scale of gathering, when large-enough spaces require multiple anchors (Alexander himself nests this pattern within hierarchy-of-open-space) and a single central object in a vast space becomes lost rather than focal'
  - '[source] assumes the anchor is shared -- everyone converges on the same thing -- but in organizations and software systems, different constituencies may need different anchors, and forcing a single one can privilege one group''s needs over another''s'
embodied_patterns:
  - center-periphery
  - balance
  - scale
relation_types:
  - coordinate
  - contain
structure: hierarchy
abstraction_level: specific
---

## Transfers

Alexander's pattern #126 observes that public squares, courtyards, and
gathering spaces fail when they are empty expanses of pavement or grass. People
do not naturally walk to the center of an open space and stand there. They need
something to go to -- a tree to sit under, a fountain to meet at, a market
stall to browse. Without an anchor, the center becomes dead space and all
activity migrates to the edges.

The critical structural insight is in the word "roughly." Alexander is not
prescribing a geometric centroid. He is saying the anchor should be
approximately in the middle -- close enough to feel central, but placed with
enough asymmetry to create natural paths of approach from multiple directions.
A perfectly centered, perfectly symmetrical anchor produces formal space; an
off-center one produces lived space.

Key structural parallels:

- **Empty centers repel activity** -- a town square with nothing in it is a
  shortcut, not a destination. An organization with no shared artifact or
  ritual at its center -- no common standup, no shared dashboard, no communal
  lunch -- becomes a collection of edge-dwellers who interact only with their
  immediate neighbors. A software system with no central registry, event bus,
  or shared data model forces every component to know about every other
  component, because there is no middle to route through. The pattern predicts
  that adding something to the center will make the whole system more
  connected, not less.

- **The anchor must be interactive, not decorative** -- Alexander
  distinguishes between a statue (people look at it and walk past) and a
  fountain (people sit on its edge, children play in it, couples meet
  beside it). The anchor works only if it gives people a reason to linger.
  In software, a shared logging dashboard that no one checks is a statue; a
  shared deployment pipeline that every team runs through daily is a
  fountain. In organizations, an all-hands meeting where leadership talks
  and everyone else listens is a statue; a weekly demo where teams show
  work-in-progress is a fountain.

- **Approximate placement outperforms precise placement** -- a perfectly
  centered conference table in a perfectly square room creates a formal,
  rigid atmosphere. The same table shifted slightly off-center, near a
  window, with a whiteboard on one side, creates zones: a presentation
  area, a discussion area, a quiet corner. In software architecture, a
  message bus that sits exactly at the center of every service graph
  becomes a bottleneck; one that sits "roughly in the middle" -- handling
  the high-traffic paths while allowing some point-to-point connections --
  performs better because it matches actual usage patterns rather than
  topological purity.

- **The anchor defines the character of the space** -- what you put in the
  middle determines what happens around it. A market stall produces commerce;
  a playground produces play; a stage produces performance. In organizations,
  a company that puts its customer support dashboard at the center of its
  office culture will behave differently from one that puts its revenue
  dashboard there. The choice of anchor is a values statement.

## Limits

- **Digital and organizational spaces have no natural center** -- a physical
  courtyard has a perceivable middle that humans intuit without measurement.
  A software system's "center" is a topological abstraction that must be
  defined before it can be populated. Putting "something in the middle" of
  an API landscape requires first deciding what "middle" means -- most
  connected? most depended-upon? most frequently accessed? Different
  definitions produce different centers, and the pattern offers no guidance
  on which to choose.

- **Scale defeats single anchors** -- Alexander's pattern works for
  neighborhood-scale spaces. A city-scale space (a 10-acre park, a
  10,000-person organization, a platform with 500 microservices) cannot be
  anchored by a single thing in the middle. At sufficient scale, the pattern
  must be applied recursively -- each sub-space gets its own anchor -- and
  the question shifts from "what goes in the middle" to "how many middles
  are there," which is a different and harder problem.

- **Anchors can become bottlenecks** -- if everything routes through the
  center, the center becomes a chokepoint. A central event bus that handles
  every inter-service message, a single manager through whom all decisions
  flow, a shared database that every service reads and writes -- these are
  anchors that became single points of failure. The pattern's emphasis on
  centrality can lead designers to over-centralize, creating fragility in
  the name of coherence.

- **The pattern conflates gathering with coordination** -- Alexander's
  courtyard anchor makes people gather, which is socially valuable. But in
  software and organizations, gathering is not always the goal. Sometimes
  the right architecture is deliberately decentralized, with no middle at
  all. Peer-to-peer systems, federated organizations, and autonomous teams
  can function well without a center, and imposing one introduces
  unnecessary coupling.

## Expressions

- "Hub-and-spoke architecture" -- software and logistics term for a topology
  with a central node, directly encoding the "something in the middle"
  principle
- "Town square" -- organizational metaphor for a shared space (Slack channel,
  wiki, all-hands) that serves as a gathering anchor
- "Single source of truth" -- data architecture principle that puts one
  authoritative record at the center
- "Water cooler" -- the informal office anchor where unplanned interactions
  happen; the organizational equivalent of Alexander's fountain
- "Central registry" -- software pattern where services register themselves
  with a central directory, placing discovery "in the middle"
- "Rally point" -- military term for a predetermined gathering location,
  functioning as an anchor in uncertain terrain

## Origin Story

Christopher Alexander's pattern #126, "Something Roughly in the Middle,"
appears in *A Pattern Language* (1977). The pattern sits within a cluster
about the internal structure of public outdoor space, between patterns about
activity nodes (#30) and positive outdoor space (#106). Alexander's examples
are characteristically physical: a fountain in a piazza, a great tree in a
village green, a market stall in a plaza.

The pattern's migration to software is indirect. Unlike "pattern language"
itself (which the Gang of Four adopted explicitly), "something roughly in the
middle" was not named in software design literature. But the structural
principle appears everywhere: service meshes with central control planes,
event-driven architectures with central brokers, and organizational designs
with shared platforms. The pattern names a tendency that software architects
enact without citing.

## References

- Alexander, Christopher. *A Pattern Language* (1977), Pattern #126:
  Something Roughly in the Middle
- Alexander, Christopher. *The Timeless Way of Building* (1979) -- the
  theoretical foundation for pattern languages
- Fowler, Martin. "Event-Driven Architecture" -- central brokers as
  architectural anchors
