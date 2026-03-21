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
name: Circulation Realms
provenance: alexander-pattern-language
related:
- intimacy-gradient
- building-complex
- family-of-entrances
grounding: established
slug: circulation-realms
source_frame: architecture-and-building
updated: '2026-03-21'
transfers:
  - '[source] circulation realms nest hierarchically so that movement within an inner realm does not require passing through the outer realm''s main corridor, structuring the principle that local traffic should stay local'
  - '[source] each realm has its own internal circulation logic independent of adjacent realms, meaning changes to one realm''s layout do not force changes to another''s'
  - '[source] the boundary between realms acts as a legibility marker -- crossing a threshold tells the traveler they have entered a different zone with different rules'
limits:
  - '[source] architectural circulation is constrained by physical adjacency -- you cannot jump from one realm to a non-adjacent realm -- whereas network routing can create shortcuts that violate hierarchical nesting'
  - '[source] the pattern assumes tree-like nesting, but real circulation often requires cross-cutting paths that break the hierarchy, just as software systems need cross-cutting concerns (logging, auth) that span multiple bounded contexts'
---

## Transfers

Alexander's pattern #98, "Circulation Realms," observes that large
buildings and campuses need nested zones of movement, not a single
undifferentiated corridor system. A hospital organizes circulation into
realms: the public lobby realm, the ward realm, the surgical realm, the
service realm. Each has its own internal paths, and the transitions
between realms are marked by thresholds -- a change in flooring, a set
of doors, a reception desk. Without this nesting, everyone shares the
same hallways: patients, surgeons, delivery trucks, and visitors all
competing for the same corridors. Mapped to software and network
architecture, this is the structural argument for segmentation,
layered routing, and hierarchical namespace design.

Key structural parallels:

- **Network segmentation as nested realms** -- a corporate network
  with VLANs, subnets, and DMZs is a direct implementation of
  circulation realms. Public traffic stays in the DMZ realm. Internal
  application traffic moves within the application subnet realm.
  Database traffic is confined to the data tier realm. Each realm has
  its own routing rules, and crossing from one to another requires
  passing through a controlled boundary (firewall, load balancer,
  gateway). The architectural insight is that undifferentiated flat
  networks, like undifferentiated flat corridors, create congestion and
  security exposure.
- **Hierarchical routing as nested circulation** -- the internet's
  routing architecture mirrors circulation realms at scale. Autonomous
  systems (AS) are realms with internal routing protocols (OSPF, IS-IS)
  that differ from the inter-realm protocol (BGP). Traffic within a
  realm is handled locally; only inter-realm traffic reaches the
  backbone. Alexander's principle -- local movement should stay local --
  is exactly the engineering rationale for hierarchical routing.
- **Module and package namespaces** -- programming languages organize
  code into nested namespaces (packages, modules, classes) that function
  as circulation realms for the developer's attention. When working
  inside a module, you navigate its internal structure without needing
  to traverse the entire codebase. Imports and exports are the
  thresholds between realms. The pattern explains why flat, global
  namespaces feel overwhelming: they are undifferentiated corridors
  where every symbol competes for attention.
- **Organizational communication hierarchies** -- Conway's Law observes
  that software architecture mirrors organizational structure. Teams
  are circulation realms: most communication stays within the team
  (local circulation), and inter-team communication passes through
  designated interfaces (team leads, shared channels, API contracts).
  When these realms break down -- everyone in a Slack channel with
  everyone else -- the result is the architectural equivalent of one
  giant corridor.
- **Thresholds create legibility** -- Alexander argues that the
  transition between realms should be physically marked so that
  occupants know which realm they are in. In software, this maps to
  clear API boundaries, environment indicators (staging vs. production
  banners), and permission prompts that signal a transition to a
  different trust realm.

## Limits

- **Architectural realms are physically nested; software realms overlap**
  -- in a building, you are in exactly one circulation realm at a time.
  In software, a request may simultaneously traverse the API gateway
  realm, the authentication realm, and the application logic realm.
  The clean nesting that makes Alexander's pattern intuitive does not
  map to the layered, concurrent nature of software request processing.
- **The pattern assumes tree-structured hierarchy; real systems need
  cross-cutting paths** -- Alexander's realms nest cleanly: the ward
  realm is inside the hospital realm. But software systems need
  cross-cutting concerns (logging, authentication, metrics) that span
  all realms simultaneously. The pattern provides no vocabulary for
  these horizontal pathways that break the vertical hierarchy.
- **Too many realms create their own overhead** -- Alexander warns
  against undifferentiated corridors, but over-segmented networks
  create the opposite problem: excessive firewall rules, complex
  routing tables, and operational overhead that slows both traffic and
  troubleshooting. The pattern argues for segmentation without
  providing a principle for when segmentation becomes over-engineering.
- **Physical circulation is continuous; digital routing is discrete** --
  walking through a building, you experience the transition between
  realms as a gradual spatial change. A network packet either passes
  through a firewall or it doesn't. The continuous, experiential
  quality of architectural circulation does not translate to the
  binary pass/fail nature of digital access control.
- **The metaphor naturalizes hierarchy** -- framing segmentation as
  "circulation realms" imports the assumption that hierarchical nesting
  is the natural way to organize movement. Peer-to-peer architectures,
  mesh networks, and flat organizational structures deliberately reject
  this assumption. The pattern's architectural intuition can make
  hierarchical designs feel inevitable when they are a choice.

## Expressions

- "Network segmentation" -- dividing a flat network into circulation
  realms with controlled boundaries
- "Defense in depth" -- nested security realms, each with its own
  access controls
- "Blast door" -- a hard boundary between circulation realms, the
  architectural threshold that prevents cascade
- "Namespace collision" -- what happens when two realms share an
  undifferentiated circulation space for identifiers
- "Cross-cutting concern" -- a function that breaks the realm hierarchy
  by needing access across all zones simultaneously
- "DMZ" -- the demilitarized zone, a specific circulation realm
  between the public internet and the private network

## Origin Story

Pattern #98 in *A Pattern Language* (1977) addresses a problem that
emerged with modernist institutional architecture: large buildings
designed with efficient but undifferentiated corridor systems that
force incompatible traffic streams into the same space. Alexander
observed that traditional buildings -- medieval monasteries, Ottoman
caravanserais, Japanese temple complexes -- naturally organized
circulation into nested realms, each with its own character and logic.

The pattern's transfer to computing was formalized through network
engineering. The development of VLANs in the early 1990s and the
subsequent rise of network segmentation as a security practice directly
implemented Alexander's circulation realms in digital infrastructure.
The zero-trust networking movement (circa 2010s) represents a further
evolution: rather than assuming that being inside a realm grants trust,
zero-trust treats every boundary crossing as a threshold requiring
verification -- Alexander's marked transitions taken to their logical
extreme.

## References

- Alexander, Christopher. *A Pattern Language* (1977), Pattern #98:
  Circulation Realms
- Newman, Sam. *Building Microservices* (2015) -- service boundaries
  as circulation realm thresholds
- Gilman, Evan and Barth, Doug. *Zero Trust Networks* (2017) -- the
  evolution of network segmentation beyond perimeter-based realms
