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
- '[source] breaks because architectural doors and windows are constrained by physics -- load-bearing walls, structural headers, weather exposure -- while software entry points have no physical constraints, making "natural" placement a matter of convention and expectation rather than structural necessity'
- '[source] misleads by implying that there is one natural place for each interface point, when software usage patterns are diverse and contradictory -- power users want keyboard shortcuts where beginners want wizard dialogs, and no single placement satisfies both'
- '[source] assumes that the room (module) is designed before the openings (interfaces), but in software the interface is often designed first and the implementation built behind it, reversing the architectural sequence entirely'
name: Natural Doors and Windows
provenance: alexander-pattern-language
related:
- a-place-to-wait
- good-materials
slug: natural-doors-and-windows
source_frame: architecture-and-building
transfers:
- '[source] imports the principle that entry and exit points should be placed where movement naturally wants to occur, not where the builder finds it structurally convenient, framing API design as a response to usage gravity rather than implementation convenience'
- '[source] carries the insight that a misplaced door forces occupants into unnatural circulation patterns that persist for the life of the building, mapping onto the observation that a poorly designed API forces workarounds that calcify into permanent usage patterns'
- '[source] establishes that the number and placement of openings should match the room''s function -- a kitchen needs different openings than a bedroom -- importing the principle that interface surface area should be proportional to the diversity of legitimate use cases'
updated: '2026-03-21'
---

## Transfers

Alexander's pattern #221, "Natural Doors and Windows," observes that doors
and windows work best when they are placed where the room's use naturally
demands them -- where people want to walk, where light needs to enter, where
a view would be welcome. When builders place openings to suit structural
convenience (avoiding load-bearing walls, aligning with plumbing runs), the
room fights its occupants. People walk awkward paths around furniture to
reach a badly placed door. Light falls in the wrong places. The room never
feels right, and no amount of decoration fixes it.

Key structural parallels:

- **APIs should follow usage gravity** -- Alexander's "natural" placement
  means observing how people actually move through a room before deciding
  where to put the door. In software, this maps to designing APIs by studying
  how consumers actually want to interact with a system rather than exposing
  whatever the internal architecture makes convenient. An API endpoint that
  requires three calls to accomplish what users think of as one operation has
  its door in the wrong place.

- **Misplaced interfaces create permanent workarounds** -- a door in the
  wrong wall forces furniture arrangements and traffic patterns that persist
  for the building's lifetime. A poorly designed API forces consumers to
  write adapter layers, caching hacks, and wrapper functions that become
  permanent infrastructure. Alexander's insight is that the cost of a
  misplaced opening compounds over time as every occupant independently
  reinvents the same workaround.

- **Interface surface area should match functional diversity** -- a kitchen
  needs multiple openings: a door to the dining room, a door to the outside,
  windows for ventilation and light. A storage closet needs one door and no
  windows. Alexander calibrates the number of openings to the room's
  functional complexity. In software, this maps to the principle that a
  module's public interface should be proportional to the diversity of its
  legitimate use cases -- neither a god-object with hundreds of methods nor
  an over-encapsulated black box with a single narrow entry point.

- **Affordance over documentation** -- a well-placed door is obvious. You
  do not need a sign saying "enter here." Alexander's natural openings are
  self-documenting because they align with expectation. In software, an API
  whose method names, parameter order, and return types match the user's
  mental model requires less documentation. The pattern frames good interface
  design as the elimination of the need for explanation.

- **Windows are read-only interfaces** -- architecturally, a window lets
  you see in or out but does not let you pass through. This maps precisely
  to read-only API surfaces: dashboard views, status endpoints, monitoring
  interfaces. The pattern distinguishes between openings that permit
  traversal (doors/write APIs) and openings that permit observation
  (windows/read APIs), and argues that both need natural placement.

## Limits

- **Physical constraints make "natural" legible; software has no walls** --
  in architecture, the natural place for a door is constrained by physics:
  load paths, weather, structural members. These constraints make "natural"
  discoverable through the design process. Software interfaces have no
  physical constraints, so "natural" becomes a matter of convention,
  expectation, and taste -- far harder to agree on and far more susceptible
  to subjective dispute.

- **Software users are diverse; room occupants are not** -- a living room
  is used in roughly similar ways by most people. A software API is used
  by beginners, experts, automated systems, and other APIs, each with
  radically different notions of "natural." The pattern assumes a relatively
  homogeneous user population, which rarely holds for software interfaces
  that serve multiple audiences.

- **In software, the interface often precedes the implementation** --
  Alexander designs the room first and then places openings where the room's
  use demands them. In software, API-first design (OpenAPI specs, protocol
  buffers, interface definitions) often precedes the implementation. The
  architectural sequence -- build the room, then place the doors -- is
  reversed, and the pattern's guidance about observing natural use cannot
  apply before the room exists.

- **Changing a door in software is cheap; in architecture it is expensive**
  -- Alexander's pattern carries urgency because moving a door in a built
  wall is a major renovation. Moving an API endpoint is a versioning
  exercise. The pattern's emphasis on getting placement right the first time
  is less critical in software, where iteration and deprecation cycles allow
  interfaces to migrate. This can lead to overengineering the initial
  design when rapid iteration would serve better.

## Expressions

- "Principle of least astonishment" -- the software design heuristic that
  an interface should behave the way users expect, Alexander's natural
  placement applied to method semantics
- "Affordance" -- Don Norman's term for design elements that suggest their
  own use, the door handle that tells you whether to push or pull
- "API surface area" -- the total set of public interfaces a module
  exposes, Alexander's count of doors and windows
- "Developer experience (DX)" -- the modern framing of API usability that
  imports Alexander's concern for the occupant's daily experience
- "Convention over configuration" -- the Rails principle that defaults
  should match expected usage patterns, doors in the obvious places

## Origin Story

Pattern #221 in *A Pattern Language* (1977) grew from Alexander's observation
of postwar housing where doors and windows were placed to minimize
structural cost rather than to serve the rooms' functions. He documented
kitchens with no window over the sink, bedrooms with doors that opened
into the middle of the room forcing awkward furniture placement, and living
rooms where the window faced a parking lot instead of the garden. The
pattern insists that openings be placed in response to how the room will
be lived in, not how the structure is most cheaply assembled. The principle
found direct application in software through the affordance-driven design
tradition and the API usability movement.

## References

- Alexander, Christopher. *A Pattern Language* (1977), Pattern #221:
  Natural Doors and Windows
- Norman, Don. *The Design of Everyday Things* (1988) -- affordance theory
  as the cognitive basis for "natural" interface placement
- Bloch, Joshua. "How to Design a Good API and Why It Matters" (2006) --
  the software equivalent of placing doors where users expect them
