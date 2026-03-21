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
name: Family of Entrances
provenance: alexander-pattern-language
related:
- building-complex
- circulation-realms
- intimacy-gradient
- main-entrance
grounding: established
slug: family-of-entrances
source_frame: architecture-and-building
updated: '2026-03-21'
transfers:
  - '[source] a family of entrances gives each entrance its own character suited to the traffic it serves, so delivery entrances are wide and utilitarian while guest entrances are welcoming and legible'
  - '[source] multiple entrances distribute arrival load across the building perimeter rather than funneling everyone through a single bottleneck'
  - '[source] each entrance in the family connects directly to the realm it serves, reducing the need for internal corridors that route people past spaces irrelevant to their purpose'
limits:
  - '[source] architectural entrances are physically fixed and expensive to add or remove, whereas API endpoints can be created, versioned, and deprecated with minimal physical constraint'
  - '[source] the pattern assumes entrances are discoverable by spatial context (you see the delivery entrance at the loading dock), but software endpoints require explicit documentation because there is no spatial affordance to guide discovery'
---

## Transfers

Alexander's pattern #102, "Family of Entrances," argues that a
building complex should not have one grand entrance and a collection
of back doors. Instead, each entrance should be a real entrance --
visible, welcoming, and designed for the specific kind of arrival it
serves. The front entrance serves visitors, the garden entrance
serves the family, the kitchen entrance serves deliveries. Each is
dignified and purposeful. When this pattern is violated -- one
monumental entrance and everything else a fire exit -- most arrivals
feel like they are sneaking in. Mapped to software, this is the
argument for multiple well-designed API surfaces rather than one
overloaded entry point.

Key structural parallels:

- **Multiple API endpoints as a family of entrances** -- a well-designed
  system offers different interfaces for different consumers. A REST
  API for web clients, a GraphQL endpoint for mobile apps, a gRPC
  interface for internal services, a CLI for operators, and a webhook
  system for integrations. Each is a purpose-built entrance, not a
  degraded version of the "real" one. The pattern argues against the
  one-API-to-rule-them-all approach that forces every consumer through
  the same interface regardless of their needs.
- **Polyglot interfaces respect different arrival patterns** -- a
  delivery entrance is designed for trucks: wide, at loading-dock
  height, with space to turn. A guest entrance is designed for people
  on foot: at ground level, with a path and a doorbell. In software,
  a batch processing interface has different ergonomics (file upload,
  progress tracking, retry logic) than a real-time streaming interface
  (websockets, backpressure, heartbeats). The pattern insists that
  each consumer type deserves an entrance shaped for their arrival
  pattern, not a one-size-fits-all door.
- **Each entrance connects to its own circulation realm** -- Alexander
  argues that an entrance should lead directly to the spaces its users
  need, without forcing them through irrelevant corridors. A delivery
  entrance leads to the kitchen, not through the living room. In
  software, a public API should route to public resources without
  traversing internal service boundaries. An admin interface should
  connect directly to management functions. The pattern frames
  unnecessary internal traversal as a design failure.
- **Entrance dignity prevents second-class citizens** -- when a
  building has one grand entrance and everything else is a service
  door, the people who use service doors feel second-class. In
  software, when the web app gets a polished UI and the API gets
  auto-generated documentation, API consumers feel second-class. The
  pattern argues that every entrance in the family deserves care --
  each SDK, each CLI, each integration surface should be thoughtfully
  designed, not an afterthought.
- **The family is discoverable as a family** -- Alexander wants all
  entrances to be visible from the approach, not hidden around back.
  You should be able to see the building complex and understand where
  to go based on who you are. In software, this maps to a developer
  portal or API catalog that presents the full family of interfaces,
  helping each consumer find their entrance rather than forcing
  everyone through the front door to be redirected.

## Limits

- **Maintaining multiple entrances multiplies maintenance** -- each
  architectural entrance needs its own weatherproofing, lighting,
  signage, and security. Each API endpoint needs its own
  authentication, documentation, versioning, rate limiting, and
  monitoring. The pattern advocates for entrance proliferation without
  accounting for the operational cost of maintaining multiple surfaces.
  A single well-designed API can be more maintainable than five
  specialized ones.
- **Entrances create security surface area** -- every entrance is a
  potential point of unauthorized entry. In architecture, this is why
  high-security buildings deliberately minimize entrances. In software,
  every API endpoint is an attack surface. The pattern's preference
  for multiple entrances conflicts with the security principle of
  minimizing exposure.
- **The pattern assumes stable, known consumer types** -- Alexander's
  family of entrances works because the building's user types are
  known at design time: residents, guests, deliveries. Software
  systems often cannot predict their consumer types in advance. A
  startup building its first API doesn't know whether mobile apps,
  IoT devices, or third-party integrations will be the primary
  consumers. Premature entrance specialization builds the wrong
  doors.
- **Architectural entrances are spatially separated; API endpoints
  share infrastructure** -- a delivery entrance and a guest entrance
  are physically distant. Two API endpoints often share the same
  server, authentication middleware, and database connection pool. The
  spatial separation that makes architectural entrances independent
  does not translate to software, where "different entrances" may be
  thin routing layers over shared infrastructure.
- **The metaphor can justify API sprawl** -- taken too far, the
  pattern produces a building with so many entrances that no one knows
  which to use. In software, this is the API proliferation problem:
  REST and GraphQL and gRPC and SOAP and webhooks and WebSockets,
  each partially maintained, none complete. The pattern provides no
  principle for when to stop adding entrances.

## Expressions

- "API gateway" -- the architectural foyer that routes arrivals to
  the appropriate entrance in the family
- "Developer portal" -- the signage and wayfinding that helps
  consumers discover which entrance is theirs
- "SDK" -- a purpose-built entrance for a specific language community,
  wrapping the raw API in idioms native to the consumer
- "Polyglot persistence" -- different storage interfaces for different
  data access patterns, each an entrance suited to its consumer
- "Backend for frontend" -- a dedicated API entrance shaped for the
  specific needs of a particular client type
- "Service mesh ingress" -- the infrastructure that manages the family
  of network entrances into a cluster

## Origin Story

Pattern #102 in *A Pattern Language* (1977) addresses the modernist
tendency to create buildings with one heroic entrance -- a grand
lobby, a monumental staircase -- and to treat all other access points
as service doors to be hidden. Alexander observed that traditional
buildings, particularly farmhouses and Mediterranean villas, had
multiple equally dignified entrances, each serving a different
relationship to the building: the street entrance for strangers, the
garden entrance for the family, the stable entrance for animals and
supplies.

In software, the pattern resonates with the API design evolution of
the 2010s. Early web services typically offered a single SOAP or
REST endpoint. The proliferation of client types -- web browsers,
mobile apps, IoT devices, partner integrations -- forced the
recognition that a single interface cannot serve all consumers well.
The Backend-for-Frontend (BFF) pattern, popularized by Sam Newman
around 2015, is the most explicit software adoption of Alexander's
principle: build a dedicated entrance for each consumer type rather
than forcing everyone through the same door.

## References

- Alexander, Christopher. *A Pattern Language* (1977), Pattern #102:
  Family of Entrances
- Newman, Sam. "Backends for Frontends" (2015) -- dedicated API
  entrances per consumer type
- Sturgeon, Phil. *Build APIs You Won't Hate* (2015) -- API surface
  design as entrance architecture
