---
slug: open-stairs
name: Open Stairs
summary: "Visible, central staircases invite use; hidden fire stairs get ignored. Abstraction layers people can see are abstraction layers people use."
kind: pattern
source_frame: architecture-and-building
applies_to:
  - software-abstraction
categories:
  - software-engineering
  - systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
  - staircase-as-a-stage
  - four-story-limit
  - degrees-of-publicness
created: '2026-03-21'
updated: '2026-03-21'
grounding: folk
harness: Claude Code
transfers:
  - '[source] open stairs are visible from the main circulation paths, so occupants discover them without signage -- the staircase advertises itself through spatial legibility rather than wayfinding aids'
  - '[source] enclosed fire stairs discourage casual use because the enclosure signals emergency-only access, creating a psychological barrier that is stronger than the physical one -- people avoid them even when they are unlocked and faster than the elevator'
  - '[source] an open staircase connects floors visually, so a person on the second floor can see activity on the first floor, maintaining awareness of the building''s life across levels without descending'
limits:
  - '[source] breaks because physical stairs enforce sequential traversal (you must pass through floor 2 to reach floor 3), while software navigation can jump to any layer directly -- the open stair''s virtue of encouraging incidental discovery during traversal has no structural analogue in random-access systems'
  - '[source] misleads by implying that visibility alone produces usage, when physical stair use also depends on bodily effort -- making a software abstraction layer visible does not mean developers will engage with it, because the cost of engagement is cognitive rather than caloric and scales differently'
embodied_patterns:
  - path
  - boundary
  - link
relation_types:
  - enable
  - coordinate
structure: network
abstraction_level: specific
---

## Transfers

Alexander's Pattern 133 in *A Pattern Language* argues that stairs should be
open, visible, and centrally placed -- not hidden behind fire doors in
windowless shafts. His reasoning is behavioral: people use what they can see.
When stairs are enclosed and tucked into corners, occupants default to
elevators even for a single floor, because the stairs are invisible and the
enclosure signals "emergency only." Open stairs, by contrast, invite use
through their spatial presence. They are social infrastructure -- you see
people on them, you encounter neighbors mid-flight, you maintain a
proprioceptive connection to the building's vertical structure.

Key structural parallels:

- **Visible abstraction layers** -- in software architecture, the equivalent
  of hiding stairs is burying important abstractions behind indirection that
  developers never encounter in normal workflows. An ORM that hides SQL
  entirely is an enclosed staircase: developers ride the elevator (the ORM
  API) and never learn the building's actual structure. An ORM that exposes
  its query plans or lets you drop to raw SQL when needed is an open
  staircase -- the lower layer is visible and reachable without breaking
  the abstraction. Django's `queryset.query` attribute and SQLAlchemy's
  `echo=True` mode are architectural open stairs.

- **Transparent escalation paths** -- in incident management and
  organizational design, open stairs map to escalation paths that are
  visible to everyone, not just to the person who needs to escalate. When
  an on-call engineer can see the entire escalation chain -- who is next,
  what they are responsible for, and how to reach them -- the path is an
  open staircase. When escalation requires navigating an undocumented
  phone tree or asking a manager to "handle it from here," the stairs
  are enclosed. The structural insight is that escalation should be
  self-service and legible, not gated by someone else's knowledge.

- **Discoverable APIs** -- a well-designed API with a browsable endpoint
  (GraphQL's introspection, REST's HATEOAS links, a Swagger UI) is an
  open staircase. The developer can see what is above and below without
  consulting external documentation. An API that requires reading a
  separate PDF to discover its endpoints has enclosed its stairs. The
  pattern's insight is that navigation infrastructure should be
  co-located with the thing being navigated, not separated into a
  different medium.

- **Open-source codebases as open stairs** -- the ability to "view
  source" on a library or framework is the ultimate open staircase.
  Closed-source dependencies are enclosed fire stairs: you can use
  them, but you cannot see what is happening inside. When a bug occurs
  at the boundary, the closed-source developer has no stairs to
  descend -- only an opaque elevator (the support ticket) that may
  or may not arrive at the right floor.

## Limits

- **Sequential traversal is not the norm in software** -- physical stairs
  enforce a specific path: to get from floor 1 to floor 3, you pass through
  floor 2. This is a feature, not a bug, because it creates incidental
  encounters with intermediate floors. Software navigation is random-access:
  a developer debugging a network call can jump from the application layer
  directly to the TCP socket without passing through the HTTP client. The
  open stair's value of incidental discovery during traversal has no
  structural equivalent in systems where you can teleport to any layer.

- **Visibility does not equal comprehensibility** -- Alexander's open stairs
  work because stairs are self-explanatory: you see them, you understand
  them, you use them. A visible software abstraction layer is not
  self-explanatory. Exposing the SQL behind an ORM query is only useful
  if the developer can read SQL. Making Kubernetes YAML visible to
  application developers does not help if they lack the context to
  interpret it. The pattern assumes that seeing is understanding, which
  holds for stairs but not for arbitrary technical abstractions.

- **Fire codes exist for good reasons** -- Alexander's aesthetic preference
  for open stairs conflicts with building codes that require enclosed
  stairwells for fire safety. The enclosed staircase is ugly but saves
  lives. In software, the analogous tension is between transparency and
  encapsulation. Hiding implementation details behind an interface is the
  fire door: it limits what you can see but protects you from cascading
  failures. The pattern's preference for openness does not account for
  the defensive value of enclosure.

- **The pattern blames the architecture for a cultural problem** -- people
  avoid enclosed stairs partly because building culture has trained them
  to use elevators. Making stairs open helps, but the deeper issue is
  habit and expectation. Similarly, developers avoid reading source code
  or descending abstraction layers not because the code is hidden but
  because the engineering culture rewards shipping features over
  understanding foundations. Open stairs are necessary but not sufficient
  for a culture of vertical navigation.

## Expressions

- "View source" -- the open staircase of the web: any user can descend
  from the rendered page to the underlying HTML
- "Leaky abstraction" -- Joel Spolsky's term for when the stairs are
  visible whether you want them or not, an involuntary open staircase
- "Escape hatch" -- a deliberate opening in an abstraction layer that
  lets you descend to the level below, a door in the fire wall
- "Browse the API" -- the discoverable endpoint pattern, making the
  system's structure navigable from within
- "You can always read the code" -- open-source culture's assumption
  that the stairs are always open

## Origin Story

Pattern 133 in *A Pattern Language* (1977) responded to the mid-century
modernist tendency to enclose stairs in concrete shafts, treating them
purely as functional infrastructure rather than social space. Alexander
observed that grand staircases in older buildings -- palazzo stairs,
Victorian hotel lobbies, university commons -- served as meeting places
and orientation devices. The modernist fire stair, by contrast, was
designed to be used only in emergencies and felt like it.

The pattern migrated to software through the broader Alexander-to-GoF
pipeline. While no specific design pattern maps directly to open stairs,
the principle of making structure visible and navigable runs through
documentation culture, API design, and the open-source movement. The
recurring tension between encapsulation (fire safety) and transparency
(social life) is one of software architecture's oldest debates.

## References

- Alexander, C., Ishikawa, S., and Silverstein, M. *A Pattern Language:
  Towns, Buildings, Construction* (1977), Pattern 133
- Spolsky, Joel. "The Law of Leaky Abstractions" (2002) -- the
  involuntary open staircase
- Fielding, Roy. "Architectural Styles and the Design of Network-based
  Software Architectures" (2000) -- HATEOAS as discoverable navigation
