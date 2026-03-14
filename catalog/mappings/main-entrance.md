---
author: agent:metaphorex-miner
categories:
- software-engineering
contributors:
- fshot
harness: Claude Code
kind: conceptual-metaphor
name: Main Entrance
related:
- the-facade-pattern
- a-place-to-wait
slug: main-entrance
source_frame: architecture-and-building
target_frame: software-abstraction
---

## What It Brings

Alexander's pattern #110, "Main Entrance," argues that a building's
primary entry should be immediately visible, easy to find, and
unmistakably the front door. When the main entrance is hidden around
the side, accessed through a parking garage, or indistinguishable from
service doors, people feel disoriented and unwelcome. The mapping to
software is direct: APIs, applications, and documentation all have
"front doors," and the quality of the entry experience determines
whether users feel invited or lost.

Key structural parallels:

- **The front door should be obvious** -- Alexander insists that you
  should be able to see the main entrance from the street. The software
  equivalent: a new user should immediately know where to start.
  Documentation landing pages, API root endpoints, CLI help commands,
  and application home screens are all main entrances. When they're
  obvious, onboarding feels natural. When they're buried, users feel
  like they're looking for a side door.
- **The entrance shapes first impressions** -- in architecture, the
  front door communicates the building's character: a grand portico says
  "institution," a modest wooden door says "home." An API's root
  endpoint, a framework's getting-started guide, or an app's onboarding
  flow communicates the software's character. The metaphor frames first
  contact as an architectural statement.
- **There should be one main entrance, not many** -- Alexander
  distinguishes the main entrance from service doors, side entrances,
  and fire exits. Software that presents users with multiple equally
  prominent starting points creates confusion. The pattern argues for a
  clear hierarchy: one primary path in, with secondary paths visible but
  subordinate.
- **The path to the entrance should be legible** -- Alexander cares
  about the approach: the walkway, the signage, the sight lines. In
  software, the path to the entry point includes search results,
  README files, marketing pages, and link destinations. A broken link
  to the documentation is a walkway that dead-ends.
- **The entrance transitions you from outside to inside** -- a good
  entrance has a threshold: a porch, a vestibule, a lobby. In software,
  onboarding flows, authentication screens, and welcome tutorials serve
  this function. The metaphor frames the transition from "not using the
  software" to "using the software" as an architectural passage.

## Where It Breaks

- **Buildings have one physical entrance axis; software has many access
  vectors** -- people approach a building from the street, on foot or
  by car. Users find software through search engines, direct links,
  app stores, API documentation, CLI package managers, or someone
  else's tutorial. The single-entrance metaphor is too simple for
  software's multi-channel reality. Every link to your software is
  potentially someone's front door.
- **Architectural entrances are permanent; software entry points
  change** -- a building's front door doesn't move. An API endpoint
  can be versioned, deprecated, or redesigned. Documentation URLs
  break. The metaphor suggests stability where software offers
  impermanence.
- **Alexander's pattern assumes a visitor who wants to enter; software
  users may be forced** -- someone approaching a building's front door
  has chosen to be there. Software users are often compelled: mandated
  by their employer, forced by a dependency, or redirected by an
  ecosystem. The welcoming metaphor doesn't map to coerced adoption.
- **The metaphor centers human visitors; APIs serve machines** -- API
  endpoints are "entered" by HTTP clients, not humans. The front-door
  metaphor imports a human-scale warmth that doesn't apply to
  machine-to-machine communication. A well-designed API root is more
  like a well-labeled loading dock than a welcoming front porch.
- **"Main entrance" implies a building worth entering; not all software
  invites exploration** -- Alexander's pattern assumes the building has
  an interior worth discovering. Some software is a single-purpose tool:
  there's nothing to explore. The architectural metaphor suggests depth
  where a simple utility just has a function to call.
- **Physical entrances provide sensory orientation; software can't** --
  walking through a door, you feel the temperature change, hear the
  acoustics shift, smell the interior. Software entry points offer no
  sensory transition. The metaphor invokes an embodied experience that
  screens can only gesture toward.

## Expressions

- "The API entry point" -- the front door of a service, the first
  endpoint you call
- "Onboarding flow" -- the designed path from outside to inside,
  the vestibule of software
- "Where do I even start?" -- the user's complaint when the main
  entrance isn't visible
- "Landing page" -- the architectural ground floor, where visitors
  first touch down
- "Front door of the application" -- explicit use of the architectural
  metaphor for the primary user interface
- "Getting started guide" -- the walkway to the entrance, the path
  Alexander says must be legible
- "Deep linking" -- bypassing the front door entirely, entering through
  a window

## Origin Story

Pattern #110 in *A Pattern Language* (1977) reflects Alexander's
conviction that buildings should communicate clearly with their
surroundings. He documents how modernist architecture often hid or
de-emphasized entrances, creating buildings that felt fortress-like or
corporate. His prescription is simple: make the main entrance visible
from the main approach, distinguish it from other doors, and mark the
transition from public to private space.

The metaphor migrated to software design naturally. As web applications
replaced desktop software, the question of "where does the user enter?"
became an active design problem. Jakob Nielsen's usability research in
the late 1990s echoed Alexander without citing him: users should be
able to tell what a site does and where to start within seconds. The
developer-facing equivalent -- API design, documentation structure, CLI
help text -- adopted the same principle. Every framework that ships
with a "Getting Started" tutorial is implementing Alexander's pattern,
whether it knows it or not.

## References

- Alexander, Christopher. *A Pattern Language* (1977), Pattern #110:
  Main Entrance
- Nielsen, Jakob. *Designing Web Usability* (1999) -- usability
  principles for web entry points
- Fielding, Roy. "Architectural Styles and the Design of Network-based
  Software Architectures" (2000) -- REST's emphasis on discoverable
  entry points