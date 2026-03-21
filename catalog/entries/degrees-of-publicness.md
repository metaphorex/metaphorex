---
slug: degrees-of-publicness
name: Degrees of Publicness
kind: pattern
source_frame: architecture-and-building
applies_to:
  - information-security
categories:
  - software-engineering
  - systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
  - the-facade-pattern
  - sacred-sites
  - alcoves
created: '2026-03-21'
updated: '2026-03-21'
grounding: established
harness: Claude Code
transfers:
  - '[source] well-designed spaces transition gradually from fully public to fully private through intermediate zones (porch, foyer, hallway, room), and each transition provides an opportunity for the occupant to control who proceeds further'
  - '[source] a space that jumps directly from public to private with no gradient (street to bedroom, no foyer) feels violating because the occupant has no buffer zone in which to assess and filter visitors'
  - '[source] the gradient is directional -- it is easy to move from private toward public but each step toward private requires increasing permission, creating an asymmetry that protects the interior without fortifying the exterior'
limits:
  - '[source] breaks because physical transitions between zones are experienced sequentially (you must pass through the foyer to reach the hallway), while digital access controls can be bypassed entirely if a single credential grants access to the innermost zone'
  - '[source] misleads by implying that the gradient is spatial and continuous, when digital access is typically discrete (you either have the API key or you do not) with no meaningful intermediate states'
embodied_patterns:
  - boundary
  - container
  - center-periphery
relation_types:
  - contain
  - prevent
  - select
structure: hierarchy
abstraction_level: specific
---

## Transfers

Alexander's Pattern 36 in *A Pattern Language* observes that successful
buildings and neighborhoods create a gradual transition from public to
private space. A well-designed house moves from the sidewalk (fully public)
through a front garden (semi-public), to a porch (semi-private), to a
front hall (private but visible), to inner rooms (fully private). Each
transition zone gives the occupant more control over who proceeds further.
The pattern breaks when buildings omit these gradients -- when an apartment
door opens directly onto a busy corridor, or when a house has no front
yard between the sidewalk and the living room.

Key structural parallels:

- **API visibility levels** -- modern software platforms implement
  Alexander's gradient directly: public APIs (the sidewalk), partner APIs
  (the front garden, accessible with a relationship), internal APIs (the
  hallway, accessible within the organization), and private APIs (the
  inner room, accessible only to the owning team). Each level requires
  increasing authorization. The pattern's structural insight -- that
  access should be a gradient, not a binary -- is exactly the logic of
  tiered API visibility.
- **Defense in depth** -- information security's "defense in depth"
  principle is degrees of publicness applied to threat modeling. A
  network perimeter (fence), a DMZ (front garden), an application
  firewall (front door), role-based access control (hallway), and
  encryption at rest (locked room) create layered transitions. Each
  layer provides an opportunity to detect and stop unauthorized
  access. The alternative -- a single hard perimeter with no internal
  zones -- is Alexander's building with no foyer: once the door is
  breached, everything is exposed.
- **Progressive disclosure in UX** -- interface design applies the
  gradient to information rather than space. A dashboard shows summary
  metrics (public view); clicking reveals detail panels (semi-private);
  administrative controls are behind authentication (private). The user
  moves through degrees of informational publicness, each step
  revealing more and requiring more commitment or authorization.
- **Organizational transparency gradients** -- companies operate with
  degrees of publicness for information: press releases (public), all-hands
  meeting content (internal), team-level strategy documents (semi-private),
  executive discussions (private). When organizations skip levels --
  announcing layoffs publicly before telling affected employees -- the
  violation feels structural, not just procedural. It is the informational
  equivalent of removing the foyer.

## Limits

- **Digital access is discrete, not continuous** -- in physical space,
  moving from the sidewalk to the front hall is a continuous experience
  with visible cues at each transition (gate, path, door, threshold).
  In digital systems, access is typically binary at each gate: you have
  the credential or you do not. There is no "partially inside" the
  API. This means the gradient metaphor implies a smoothness that
  digital access control does not possess. A user with a valid OAuth
  token is fully inside; one without is fully outside. The foyer
  experience -- being inside but not yet deep -- is architecturally
  natural but digitally artificial.
- **Gradients can produce false security** -- multiple layers of
  transition create the feeling of robust defense, but if each layer
  checks the same credential, they are functionally a single gate
  with decorative foyers. Alexander's physical transitions are
  genuinely independent (a gate, a door, and a lock are three
  different mechanisms). Digital "defense in depth" can degenerate
  into defense in breadth -- many checkpoints, one key.
- **The pattern assumes a single direction of approach** -- Alexander's
  gradient runs from the street to the interior. Physical space has a
  front and a back; you approach from a predictable direction. Digital
  systems can be approached from any direction: an attacker who
  compromises an internal service is already past all the outer
  gradients. The pattern's spatial linearity does not map to the
  graph topology of networked systems.
- **Privacy gradients conflict with transparency values** -- Alexander's
  pattern assumes that deeper means more private, and that this is
  desirable. In organizations committed to radical transparency, the
  gradient runs in the opposite direction: the default is public,
  and privacy requires justification. The pattern encodes a
  conservative assumption about information flow that not all
  contexts share.

## Expressions

- "Public, internal, private" -- the API visibility tiers that directly
  implement Alexander's gradient in software platforms
- "Defense in depth" -- the security architecture principle of layered
  boundaries, each adding a transition zone
- "DMZ" (demilitarized zone) -- the network security term for the
  semi-public zone between the internet and the internal network,
  functionally Alexander's front garden
- "Progressive disclosure" -- the UX pattern of revealing information
  in stages, applying the gradient to interface design
- "Zero trust" -- the modern security paradigm that rejects the
  gradient entirely, treating every request as originating from the
  public sidewalk regardless of where it appears to come from

## Origin Story

Pattern 36 in *A Pattern Language* (1977) drew on Alexander's study of
vernacular architecture, particularly the traditional Islamic house with
its sequence of gates, courtyards, and inner chambers, and the European
townhouse with its graduated movement from street to parlor to private
quarters. Alexander argued that modernist architecture, with its direct
transitions (elevator to apartment door, corridor to office), had
eliminated these gradients, producing spaces that felt either exposed or
fortress-like, with nothing in between.

The pattern's migration to information security was natural: the concept
of defense in depth predates Alexander (it originates in military
strategy), but Alexander's contribution was the insight that the gradient
serves the inhabitant's psychological comfort as much as their physical
safety. This transfers to UX design and organizational policy, where the
gradient's value is not just in stopping intruders but in giving
legitimate users the experience of controlled, comprehensible transitions
between levels of access.

## References

- Alexander, C., Ishikawa, S., and Silverstein, M. *A Pattern Language:
  Towns, Buildings, Construction* (1977), Pattern 36
- Saltzer, J.H. and Schroeder, M.D. "The Protection of Information in
  Computer Systems," *Proceedings of the IEEE* 63.9 (1975): 1278-1308
  -- foundational access control principles
- NIST SP 800-207. "Zero Trust Architecture" (2020) -- the paradigm
  that questions whether gradients are sufficient
