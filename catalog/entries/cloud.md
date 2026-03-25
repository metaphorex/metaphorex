---
applies_to:
- computing
author: agent:metaphorex-miner
categories:
- linguistics
- software-engineering
- systems-thinking
contributors: []
created: '2026-03-17'
dead: true
harness: Claude Code
kind: metaphor
name: Cloud
summary: "Someone else's computer, named after something nobody owns. The opacity of the source domain maps perfectly onto the product."
related: []
slug: cloud
source_frame: natural-phenomena
updated: '2026-03-17'
transfers:
  - "[source] clouds are overhead and visible but their internal structure is opaque -- you cannot see what happens inside them"
  - "[source] clouds are amorphous, with no fixed boundaries, expanding and contracting without clear edges"
  - "[source] clouds form, dissolve, and reform elsewhere without any single cloud being permanent or uniquely addressable"
limits:
  - "[source] breaks because real clouds have no owner, no operator, and no billing department, while cloud computing runs on privately owned infrastructure with specific physical locations"
  - "[source] misleads because clouds are weightless and immaterial, hiding the enormous energy consumption, water usage, and hardware footprint of data centers"
  - "[source] obscures that clouds in nature are local weather phenomena, while cloud computing spans continents with precisely routed traffic between specific facilities"
embodied_patterns:
  - container
  - surface-depth
  - scale
relation_types:
  - contain
  - translate
structure: boundary
abstraction_level: specific
---

## Transfers

Network engineers drew clouds on architecture diagrams to represent
"someone else's infrastructure you don't need to understand." The
cloud symbol meant: here is a boundary beyond which the internals
are not your concern. The amorphous, overhead, opaque nature of real
clouds maps onto remote computing that is amorphous (scalable, no
fixed shape), overhead (accessible from anywhere below), and opaque
(you don't see the servers).

- **Opacity as abstraction** -- you cannot see inside a cloud. You
  see its exterior surface -- white, grey, towering -- but its internal
  convection currents, water droplet density, and ice crystal
  formation are hidden. Cloud computing works the same way: you see
  an API, a dashboard, a service endpoint, but the servers, racks,
  cooling systems, and fiber optic cables are hidden behind the
  abstraction layer. The metaphor maps visual opacity onto
  architectural opacity. This is genuinely useful: the whole point
  of cloud computing is that you shouldn't need to understand the
  internals.
- **Amorphous scalability** -- clouds have no fixed size or shape.
  They grow, shrink, merge, and split continuously. Cloud computing
  promises the same: elastic scaling, no fixed capacity, resources
  that expand and contract with demand. "Auto-scaling" is the cloud
  computing equivalent of a cumulus cloud growing into a cumulonimbus
  on a hot afternoon. The metaphor correctly imports the idea of
  formless, demand-responsive capacity.
- **Ubiquity and overhead position** -- clouds are everywhere above
  you. Cloud computing is everywhere above your local machine. The
  spatial metaphor of "up in the cloud" vs. "on-premise" maps
  altitude onto abstraction level. Uploading and downloading are
  vertical metaphors: data goes up to the cloud and comes down to
  your device. The cloud is heaven; your laptop is earth.

## Limits

- **Clouds have no owners** -- this is the most consequential structural
  failure. Real clouds are natural phenomena, owned by no one, governed
  by physics. Cloud computing is owned by Amazon, Microsoft, and Google,
  governed by terms of service and pricing tiers. The metaphor's
  implication of natural, free, ownerless infrastructure disguises the
  reality that "the cloud" is a small number of corporations renting
  you access to their hardware. "There is no cloud, just other people's
  computers" is the resurrection of this dead metaphor's suppressed
  truth.
- **Clouds are weightless; data centers are not** -- a cloud floats
  because water vapor is lighter than surrounding air. A data center
  weighs thousands of tons, consumes megawatts of electricity, and
  requires millions of gallons of cooling water. The metaphor's
  implication of weightlessness -- ethereal, clean, immaterial --
  hides the enormous physical footprint of cloud computing. When
  people say they "moved to the cloud," the metaphor encourages
  them to think they dematerialized their infrastructure. They
  didn't. They relocated it to a warehouse in Virginia or Oregon
  and stopped looking at it.
- **Clouds are local; cloud computing is global** -- a cloud is a
  local weather phenomenon. You can see it, it has a location, it
  affects the area directly below it. Cloud computing spans
  continents with precisely routed traffic between availability
  zones, regions, and edge locations. The metaphor imports locality
  (the cloud is "up there, above me") but the reality is distributed
  geography (your data is in us-east-1, your compute in eu-west-2,
  your CDN edge nodes everywhere). The atmospheric metaphor provides
  no vocabulary for the actual geography of cloud infrastructure.
- **Clouds dissipate; data centers persist** -- real clouds form and
  dissolve within hours. They are transient by nature. Cloud computing
  infrastructure persists for decades. The buildings, the fiber, the
  cooling systems are permanent installations. The metaphor's
  implication of ephemerality is precisely wrong: cloud computing is
  the most physically permanent form of computing infrastructure
  ever built.

## Expressions

- "In the cloud" -- stored or running on remote servers, where "cloud"
  means "not on your device" and nobody thinks about weather
- "Cloud-native" -- software designed for cloud infrastructure, where
  "native" adds a citizenship metaphor to the weather metaphor
- "Cloud migration" -- moving systems to remote infrastructure, where
  "migration" adds a biological metaphor (birds migrating to clouds)
- "Multi-cloud" -- using multiple cloud providers, a term that in the
  source domain would mean "multiple overlapping clouds," which is
  just called "overcast"
- "Cloud storage" -- remote file storage, where the ethereal metaphor
  is applied to very concrete spinning disks and flash memory
- "Hybrid cloud" -- mixing on-premise and remote infrastructure, a
  distinction that has no atmospheric analogue

## Origin Story

The cloud symbol in network diagrams predates cloud computing by
decades. Telephone network engineers in the 1970s used a cloud shape
to represent the public switched telephone network (PSTN) on diagrams:
a boundary beyond which the network topology was someone else's
problem. The cloud was not a metaphor for any particular technology
but for ignorance -- deliberate, productive ignorance of what
happened inside the boundary.

The symbol migrated from telecom to internet networking in the 1990s.
Network architects drew clouds to represent the internet itself: the
amorphous mass of routers and links between your network edge and your
destination. Again, the cloud meant "not our concern."

Amazon Web Services (2006) turned the diagram symbol into a product
category. When Amazon offered compute and storage as a service, the
existing cloud symbol became the name for the business model. "Cloud
computing" was not coined by a single person but emerged from the
collective vocabulary of network engineering diagrams. The metaphor
was already dead when it became a product name -- nobody at AWS was
thinking about weather when they named their services.

The death was completed by marketing. "The Cloud" became a brand
promise: freedom from hardware, infinite scalability, pay-as-you-go
simplicity. The atmospheric metaphor was useful precisely because it
was vague. Nobody argues about what a cloud's SLA should be. The
metaphor's opacity -- its central structural feature -- served the
vendor's interest in keeping customers from asking too many questions
about what was behind the abstraction.

## References

- Regalado, A. "Who Coined 'Cloud Computing'?" MIT Technology Review
  (2011) -- traces the term's origins in network engineering diagrams
- Etymonline, "cloud" -- traces Old English clud (rock, hill) through
  its atmospheric and computing senses
- Hogan, M. et al. "NIST Cloud Computing Standards Roadmap" (2011) --
  the formal definition that tried to pin down what the metaphor meant
