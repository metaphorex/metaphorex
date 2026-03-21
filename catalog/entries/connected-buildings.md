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
name: Connected Buildings
provenance: alexander-pattern-language
related:
- building-complex
- circulation-realms
- family-of-entrances
grounding: established
slug: connected-buildings
source_frame: architecture-and-building
updated: '2026-03-21'
transfers:
  - '[source] connected buildings share walls, covered walkways, or bridging structures so that occupants can move between them without leaving the protected environment'
  - '[source] the connections between buildings create shared boundaries that allow independent structures to function as a unified whole while retaining their separate identities'
  - '[source] disconnected buildings on the same site force occupants outdoors for every inter-building trip, making collaboration between occupants of different buildings costly and weather-dependent'
limits:
  - '[source] physical connections between buildings are permanent and expensive to modify, whereas software integrations can be added, reconfigured, or severed at deployment time with no structural demolition'
  - '[source] connecting buildings creates shared load paths where structural failure can propagate across the connection, but the pattern presents connection as purely beneficial without addressing this coupling risk'
---

## Transfers

Alexander's pattern #108, "Connected Buildings," argues that buildings
in a complex should not be freestanding objects separated by outdoor
space. They should be physically connected -- by shared walls, covered
walkways, arcades, or bridging structures -- so that movement between
them is sheltered and continuous. When buildings are isolated, the
effort of crossing between them discourages interaction: departments
in separate buildings drift apart, shared resources go unused, and
the complex becomes a collection of silos that happen to share a
mailing address. Mapped to software, this is the structural argument
for service integration: isolated systems that share an organization
but lack designed connections produce the same organizational drift
that isolated buildings produce on a campus.

Key structural parallels:

- **Service mesh as covered walkway** -- a service mesh (Istio,
  Linkerd) provides the infrastructure for services to communicate
  reliably without each pair building its own connection logic. This
  is the covered walkway between buildings: a shared, maintained
  connection that makes inter-service communication as easy as
  intra-service communication. Without it, each service-to-service
  call requires its own retry logic, circuit breaking, and
  observability -- the equivalent of each building constructing its
  own bridge.
- **Shared authentication as a common wall** -- when buildings share
  a wall, occupants can pass through an internal door rather than
  going outside and re-entering. Single sign-on (SSO) is the shared
  wall of software systems: authenticated in one service, you pass
  through to connected services without re-authenticating. When
  systems lack SSO, every transition between services requires a
  new login -- the digital equivalent of leaving one building, walking
  through the rain, and presenting credentials at the next door.
- **Integration platforms as arcades** -- an arcade in Alexander's
  sense is a covered passage between buildings that is itself a
  useful space: shops, cafes, places to pause. Integration platforms
  (message queues, event buses, ETL pipelines) are the arcades of
  software: they connect systems while adding their own functionality
  -- message transformation, routing, buffering. The connection is
  not just a pipe but a productive space.
- **Isolated systems produce organizational silos** -- Alexander
  observes that when university departments are in disconnected
  buildings, interdisciplinary collaboration withers. The physical
  barrier becomes a social barrier. In software, when teams own
  isolated services with no integration layer, data sharing happens
  through manual exports, duplicated databases, or not at all.
  Conway's Law in reverse: the system's disconnection shapes the
  organization's disconnection.
- **Connection enables serendipitous interaction** -- in a connected
  building complex, people encounter colleagues from other departments
  in the shared walkways. These unplanned encounters produce
  cross-pollination. In software, well-designed event buses and shared
  data streams enable serendipitous integration: a service can
  subscribe to events it wasn't originally designed for, discovering
  connections that rigid point-to-point integrations would never
  produce.

## Limits

- **Connection creates coupling; isolation enables independence** --
  Alexander frames connection as purely positive. But connected
  buildings share structural loads: renovating one may require
  shoring up the connection to its neighbor. In software, integrated
  services share failure modes: a downstream service's outage
  propagates through the connection to upstream consumers. The
  pattern does not acknowledge that isolation is sometimes a
  deliberate architectural choice to prevent cascade failures.
- **Not all connections are walkways; some are chains** -- the pattern
  romanticizes connection as enabling free movement. But mandated
  integrations -- forced data sharing, required API calls, compliance
  reporting pipelines -- can feel less like walkways and more like
  chains that constrain rather than enable. The pattern's language
  of connection obscures the distinction between voluntary
  collaboration and mandatory coupling.
- **Physical connection requires physical proximity; software has no
  such constraint** -- Alexander's argument depends on the fact that
  disconnected buildings impose a real cost: you must walk outside,
  get rained on, spend time in transit. Software services can
  communicate across continents in milliseconds. The urgency of
  physical connection does not map to systems where "disconnected"
  services can still communicate freely over a network. The problem
  the pattern solves (traversal cost) is orders of magnitude smaller
  in software.
- **The pattern assumes a known set of buildings; software evolves** --
  Alexander's connections work because the buildings are designed
  together. But software systems evolve: new services appear, old
  ones are deprecated, and the topology changes continuously. A
  covered walkway built to connect two buildings becomes a dead end
  when one is demolished. Similarly, tight integrations between
  services become liabilities when one service is retired. The
  pattern does not account for the evolutionary dynamics of software
  systems.
- **Too much connection produces a monolith in disguise** -- if every
  building is connected to every other, the complex becomes a single
  megastructure with internal partitions -- not the collection of
  semi-independent buildings the building-complex pattern calls for.
  In software, if every service is tightly integrated with every
  other through synchronous calls and shared state, the "microservices
  architecture" is a distributed monolith. The pattern provides no
  principle for optimal connectivity, only the injunction to connect.

## Expressions

- "Service mesh" -- the infrastructure that provides covered walkways
  between services, handling routing, retries, and observability
- "Single sign-on" -- the shared wall that lets users pass between
  systems without re-authenticating
- "Integration bus" -- the arcade connecting services, adding
  transformation and routing functionality to the connection itself
- "Data silo" -- the disconnected building whose occupants cannot
  share resources with adjacent systems
- "Tight coupling" -- when the connection between systems is so
  rigid that they cannot be modified independently, the walkway
  that became a load-bearing wall
- "API federation" -- connecting multiple independent APIs into a
  unified graph, the architectural bridge between autonomous services

## Origin Story

Pattern #108 in *A Pattern Language* (1977) responds to the modernist
campus-planning approach of placing freestanding buildings on open
lawns, connected only by paths and roads. Alexander observed that
traditional building complexes -- medieval monasteries, Mediterranean
market towns, Oxford and Cambridge colleges -- physically connected
their buildings with cloisters, arcades, and shared walls. These
connections were not merely convenient; they created the social fabric
of the institutions. When buildings were disconnected, the institution
fragmented into isolated departments that happened to share a name.

The pattern's relevance to software integration became apparent with
the rise of enterprise architecture in the 1990s and 2000s. The
enterprise service bus (ESB) was an explicit attempt to build
"covered walkways" between enterprise applications. The subsequent
microservices movement (2010s) initially emphasized service
independence, but the emergence of service meshes, API gateways,
and event-driven architectures represents a rediscovery of
Alexander's principle: independence without connection produces
isolation, and isolation produces silos.

## References

- Alexander, Christopher. *A Pattern Language* (1977), Pattern #108:
  Connected Buildings
- Hohpe, Gregor and Woolf, Bobby. *Enterprise Integration Patterns*
  (2003) -- the canonical catalog of software connection patterns
- Newman, Sam. *Building Microservices* (2015) -- the tension between
  service independence and service integration
- Dragoni, Nicola et al. "Microservices: Yesterday, Today, and
  Tomorrow" (2017) -- evolution of service connectivity patterns
