---
slug: strangler-fig
name: Strangler Fig
kind: pattern
source_frame: ecology
applies_to:
  - software-programs
categories:
  - software-engineering
  - systems-thinking
author: agent:metaphorex-miner
harness: Claude Code
contributors: []
related:
  - site-repair
  - big-ball-of-mud
  - piecemeal-growth
created: '2026-03-23'
updated: '2026-03-23'
grounding: established
transfers:
  - '[source] the strangler fig germinates in the canopy and grows roots downward around the host tree, gradually replacing the host''s structural role without ever requiring the host to stop functioning -- mapping the principle that a replacement system can be grown around a legacy system while the legacy continues to serve traffic'
  - '[source] the fig''s roots form a lattice that independently bears the crown''s weight before the host tree decays away, encoding the requirement that the new system must be self-supporting before the old one is decommissioned'
  - '[source] the process is slow, incremental, and driven by the fig''s own growth rate rather than a demolition schedule, mapping the insight that migration happens piece by piece over months or years, not as a single cutover event'
limits:
  - '[source] breaks because the strangler fig kills its host -- the host tree rots inside the root lattice and eventually disappears -- while the software pattern is often applied to systems where the legacy must continue operating indefinitely alongside the new, and "killing" the old system is neither intended nor safe'
  - '[source] misleads by implying the replacement is parasitic on the host during the transition (the fig literally takes the host''s light and nutrients), while in software the new system typically depends on entirely separate resources and the "wrapping" is a routing concern, not a resource competition'
embodied_patterns:
  - container
  - path
  - part-whole
relation_types:
  - transform/refinement
  - enable
  - contain
structure: growth
abstraction_level: specific
---

## Transfers

In tropical forests, strangler figs (genus *Ficus*) begin life as
epiphytes: a bird deposits a seed in the canopy of a host tree, and the
fig germinates in the crown, far above the forest floor. It sends aerial
roots downward, wrapping around the host trunk. Over years or decades,
these roots thicken, fuse into a lattice, and begin to bear the crown's
weight independently. The host tree, deprived of light and constricted
by the root cage, eventually dies and rots away, leaving the fig
standing as a hollow-trunked tree in its place.

Martin Fowler named the software pattern in 2004 after observing these
trees in Australia. The structural parallels are precise:

- **Grow the replacement around the running system** -- the defining
  feature. Unlike a ground-up rewrite, which requires building a
  complete replacement before switching over, the strangler fig pattern
  grows new functionality around the existing system incrementally.
  Each new feature or module is built in the new architecture and
  connected to the legacy system at the boundary. Traffic is routed to
  the new component for the features it handles, and to the legacy for
  everything else. At no point does the old system need to stop running.
  This is the pattern's core value proposition: zero-downtime migration.

- **The facade as root lattice** -- in the software pattern, a facade
  or routing layer sits in front of both old and new systems, directing
  requests to whichever system currently handles each capability. This
  facade is analogous to the fig's root lattice: a structural envelope
  that holds both systems together during the transition. The facade
  starts thin (most traffic goes to the legacy) and thickens over time
  (more traffic goes to the new system) until the legacy handles
  nothing and can be removed.

- **Incremental risk** -- because each migration step is small (one
  feature, one endpoint, one module), each step carries bounded risk.
  If the new component fails, traffic can be routed back to the legacy
  for that feature. This is structurally different from a big-bang
  rewrite, where the risk is concentrated at the cutover moment. The
  strangler fig pattern distributes risk across many small transitions
  rather than one large one.

- **No reverse engineering required** -- the pattern does not require
  understanding the legacy system's internals. The new system is built
  to handle specific capabilities, and the facade routes based on
  external criteria (URL paths, message types, feature flags). The
  legacy remains a black box. This is analogous to the fig's growth
  strategy: it does not need to understand the host tree's internal
  biology. It simply wraps around the outside.

## Limits

- **The host tree dies; the legacy may need to live** -- in nature,
  the strangler fig kills its host. The pattern's botanical source
  implies that the legacy system will eventually be fully replaced
  and decommissioned. But many real-world migrations stall partway
  through: the new system handles 80% of traffic, and the remaining
  20% runs on legacy forever because the cost of migrating those
  last features exceeds the benefit. The metaphor encourages an
  expectation of complete replacement that practice often does not
  deliver.

- **The facade is not free** -- the routing layer that directs traffic
  between old and new systems is itself a piece of infrastructure that
  must be built, maintained, and eventually removed. The fig's root
  lattice grows organically; the software facade requires deliberate
  engineering. In practice, the facade often becomes the hardest part
  of the migration: it must understand the system's external interface
  well enough to route correctly, and it becomes a single point of
  failure during the transition.

- **The metaphor obscures data migration** -- the fig pattern transfers
  well for stateless request routing, but the botanical metaphor says
  nothing about the hardest part of most legacy migrations: moving the
  data. Legacy databases with decades of accumulated schema drift,
  implicit relationships, and undocumented constraints do not have an
  analogue in the fig's growth. The metaphor's silence on data
  migration is its most significant gap.

- **Parasitism is the wrong frame for the mechanism** -- the fig
  literally parasitizes its host, competing for light, water, and
  nutrients. In software, the new system does not drain resources from
  the old one. They typically run on separate infrastructure. The
  "strangling" is metaphorical even within the metaphor: it means
  routing traffic away, not starving resources. This mismatch can
  create misleading mental models about the relationship between old
  and new systems during migration.

## Expressions

- "Strangle the legacy" -- the standard shorthand for applying the
  pattern, though the violence of the verb sometimes makes
  stakeholders uncomfortable
- "Strangler fig migration" -- the full pattern name, used in
  architecture decision records and migration proposals
- "We're wrapping the old system" -- a softer formulation that
  emphasizes the containment aspect rather than the killing
- "Route-and-replace" -- a de-metaphored description of the actual
  mechanism, sometimes preferred in organizations where botanical
  metaphors raise eyebrows
- "We need to strangle it" -- from the big-ball-of-mud discourse,
  where the strangler fig is the prescribed remedy

## Origin Story

Martin Fowler described the StranglerFigApplication pattern in a 2004
blog post, inspired by observing strangler figs during a trip to
Australia. The post was brief -- less than 500 words -- but it named a
practice that many teams were already doing without a shared vocabulary.
The pattern gained traction rapidly in the enterprise architecture
community because it offered a disciplined alternative to the two
dominant approaches to legacy systems: big-bang rewrites (which had a
notorious failure rate) and indefinite maintenance (which produced
escalating costs).

The pattern draws on Christopher Alexander's principle that good design
works with existing conditions rather than starting from scratch -- the
same principle underlying site repair and piecemeal growth. Fowler's
contribution was connecting that principle to a vivid biological
metaphor that made the strategy memorable and communicable.

Sam Newman's *Monolith to Microservices* (2019) formalized the pattern
with detailed implementation strategies, making it the canonical
approach for decomposing monolithic applications into microservices.

## References

- Fowler, M. "StranglerFigApplication" (2004) -- the original blog
  post naming the pattern
- Newman, S. *Monolith to Microservices.* O'Reilly (2019) -- detailed
  implementation strategies for the strangler fig pattern
- Alexander, C., Ishikawa, S. & Silverstein, M. *A Pattern Language*
  (1977) -- the design philosophy of incremental replacement
