---
applies_to:
- organizational-structure
author: agent:metaphorex-miner
categories:
- software-engineering
- organizational-behavior
- systems-thinking
contributors: []
created: '2026-03-21'
harness: Claude Code
kind: pattern
limits:
- '[source] breaks because physical green space is non-rivalrous up to a crowd threshold -- many people can use a park simultaneously without degrading each other''s experience -- while shared digital resources like open-source libraries, shared infrastructure, and internal platforms become congested, contentious, or degraded as usage scales'
- '[source] misleads by implying that proximity alone ensures access, when shared digital resources require skills, permissions, and cultural norms that function as invisible fences: an open-source library within walking distance of every developer is useless to those who cannot read the documentation or understand the API'
- '[source] assumes that the green space is maintained by a commons-like stewardship, but shared digital resources suffer from the tragedy of the commons -- everyone uses them, nobody funds them, and they degrade until a crisis forces investment'
name: Accessible Green
provenance: alexander-pattern-language
related:
- quiet-backs
- work-community
slug: accessible-green
source_frame: architecture-and-building
transfers:
- '[source] establishes that shared open space must be within a short, barrier-free journey of every inhabitant, importing the principle that access is defined by travel cost, not nominal availability'
- '[source] imports the structural insight that green spaces must be distributed throughout the built environment rather than concentrated in a single large park, because a distant resource -- no matter how grand -- is not accessible in daily practice'
- '[source] carries the principle that the green space belongs to no single household or institution but to the surrounding community collectively, framing shared ownership as a design requirement rather than an ideological preference'
updated: '2026-03-21'
embodied_patterns:
  - center-periphery
  - near-far
  - part-whole
relation_types:
  - enable
  - coordinate
  - accumulate
structure: network
abstraction_level: specific
---

## Transfers

Alexander's pattern #60, "Accessible Green," argues that every person
should have access to a piece of open green space within a three-minute
walk from their home or workplace. Not a distant park across town, not a
private garden behind a fence, but a genuinely public, genuinely nearby
open space where anyone can sit, walk, or simply see trees. When this
access is absent, Alexander claims, people become subtly but measurably
more stressed, more isolated, and less connected to their neighborhood.
The pattern is not about nature romanticism; it is a structural claim
about the spatial distribution of shared resources.

Key structural parallels:

- **Shared infrastructure must be distributed, not centralized** -- a city
  with one magnificent park and no neighborhood greens has not solved the
  access problem. The park is too far from most residents to be part of
  daily life. In software organizations, a centralized platform team that
  owns all shared infrastructure (CI/CD, observability, deployment tooling)
  is the single large park: nominally available to everyone, practically
  accessible only to those who can navigate the ticket queue. The pattern
  argues for distributed shared resources -- team-level tooling, local
  caches of documentation, embedded platform engineers -- that are within
  "walking distance" of every developer.

- **Open-source libraries as public greens** -- an open-source library is
  a shared resource that anyone can use without permission or payment. The
  pattern's structural parallel is precise: the library must be discoverable
  (within walking distance), well-maintained (not overgrown), and genuinely
  open (no hidden licensing traps that function as fences). When the
  open-source ecosystem is healthy, every developer has access to high-quality
  shared components within a short search. When it degrades -- abandoned
  packages, license ambiguity, security vulnerabilities in unmaintained
  code -- the "green" is overgrown and unsafe.

- **Commons require collective stewardship** -- Alexander's green space
  is maintained not by a single owner but by the surrounding community.
  This maps onto the governance challenges of shared resources in
  organizations and in open source. A shared internal library that belongs
  to "everyone" often belongs to no one: nobody upgrades it, nobody writes
  documentation, nobody triages issues. The pattern imports the
  architectural insight that shared ownership must be designed (with
  maintenance schedules, stewardship roles, and community norms) rather
  than assumed.

- **The three-minute-walk radius as a design constraint** -- Alexander's
  pattern is specific about distance: three minutes' walk, roughly 750
  feet. The constraint is not about distance per se but about the
  threshold beyond which daily use drops to near zero. In software, this
  translates to "steps to access": a shared resource that requires filing
  a ticket, waiting for approval, and configuring a VPN is too far away.
  A shared resource accessible via a single import statement or a one-click
  deployment is within walking distance. The pattern predicts that shared
  resources behind more than two or three steps of friction will be
  underused regardless of their quality.

- **Green space makes the surrounding built environment livable** -- the
  park does not just serve the people who sit in it; it improves the
  quality of every building that faces it. Similarly, a healthy internal
  commons (good shared libraries, reliable CI, clear documentation) does
  not just help the people who directly use it; it raises the quality floor
  for every team that builds adjacent to it. The pattern frames shared
  infrastructure as an externality generator, not just a direct service.

## Limits

- **Digital commons are rivalrous in ways that green space is not** --
  many people can sit in a park simultaneously. A shared staging
  environment, a shared CI pipeline, or a single open-source maintainer's
  attention span are all rivalrous: more users mean slower builds, longer
  queues, and slower response times. The pattern's assumption that shared
  space can accommodate many users without degradation does not hold for
  most shared digital resources.

- **Access requires capability, not just proximity** -- a park is
  accessible to anyone who can walk into it. A shared software library
  requires understanding its API, reading its documentation, and
  integrating it into a specific technology stack. The architectural
  pattern treats proximity as the primary barrier to access, but in
  software, the primary barriers are often cognitive (the library is
  too complex to learn quickly) or political (the team that owns it is
  unresponsive to integration requests). Making a resource "nearby" does
  not make it accessible if the skills to use it are unevenly distributed.

- **The tragedy of the commons applies more aggressively to digital
  resources** -- Alexander's green space is maintained by community norms
  and, in practice, by municipal funding. Digital commons -- especially
  open-source software -- are maintained by volunteer labor that is
  chronically underfunded. The pattern's optimistic assumption that
  shared resources will be maintained by the community they serve is
  contradicted by the endemic burnout and funding crises in open-source
  maintenance.

- **Distributing resources means duplicating costs** -- Alexander's
  prescription to have many small greens rather than one large park
  is spatially straightforward but financially expensive. In software,
  distributing shared resources (giving each team its own CI, its own
  test environment, its own copy of the platform) multiplies
  infrastructure costs and creates configuration drift. The pattern
  prescribes distribution without adequately weighing the cost of
  maintaining many small instances versus one large one.

## Expressions

- "Inner source" -- the practice of sharing code across teams within an
  organization using open-source norms, the organizational equivalent of
  neighborhood green space
- "Shared services" -- organizational term for centralized resources
  available to all teams, the equivalent of a municipal park
- "Commons" -- the term itself, borrowed from land use, for any shared
  resource that is collectively maintained
- "Public API" -- an open interface that any consumer can access, the
  digital equivalent of a public green
- "Everyone's problem is no one's problem" -- the organizational expression
  of the commons stewardship failure the pattern warns about

## Origin Story

Pattern #60 in *A Pattern Language* (1977) reflects Alexander's study of
the relationship between open space and residential satisfaction in cities.
He cited research showing that families with access to nearby green space
used it daily, while families whose nearest green was more than three
minutes away used it almost never. The pattern was a direct response to
mid-century urban planning that concentrated open space in large parks
separated from residential areas by highways and commercial zones.
Alexander's insistence on distributed, accessible, collectively-maintained
open space anticipated the modern discourse on digital commons, platform
cooperativism, and the infrastructure sustainability challenges of open
source.

## References

- Alexander, Christopher. *A Pattern Language* (1977), Pattern #60:
  Accessible Green
- Ostrom, Elinor. *Governing the Commons* (1990) -- governance structures
  for shared resources
- Eghbal, Nadia. *Working in Public* (2020) -- the maintenance crisis in
  open-source commons
- Hardin, Garrett. "The Tragedy of the Commons" (1968) -- the degradation
  dynamic that unstewardarded commons face
