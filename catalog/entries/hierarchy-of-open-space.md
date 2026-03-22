---
slug: hierarchy-of-open-space
name: Hierarchy of Open Space
kind: pattern
source_frame: architecture-and-building
applies_to:
  - software-abstraction
categories:
  - systems-thinking
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - alcoves
  - degrees-of-publicness
  - entrance-transition
created: '2026-03-19'
updated: '2026-03-19'
grounding: established
embodied_patterns:
  - container
  - center-periphery
  - scale
  - boundary
relation_types:
  - contain
  - decompose
structure:
  - hierarchy
abstraction_level: generic
harness: Claude Code
transfers:
  - '[source] open spaces must form a nested hierarchy from large public areas down to small private ones, because a flat collection of same-sized spaces fails to support the full range of human activities that differ in intimacy, group size, and noise tolerance'
  - '[source] each level of the hierarchy gains its character from its relationship to the levels above and below it -- a courtyard feels semi-private because it is smaller than the street and larger than the garden -- meaning the hierarchy is relational, not absolute'
  - '[source] skipping a level in the hierarchy (jumping from public plaza directly to private garden with no intermediate semi-public courtyard) creates a jarring transition that people avoid, leaving both spaces underused'
limits:
  - '[source] breaks because physical open spaces have natural capacity limits enforced by area and sightlines, while digital and organizational spaces can be resized arbitrarily, removing the physical constraint that makes the hierarchy legible'
  - '[source] assumes a stable population with shared cultural norms about public and private behavior, but multi-tenant systems and global organizations contain users with conflicting expectations about what "public" and "private" mean at each level'
  - '[source] implies that the hierarchy should be designed top-down and remain fixed, but software scoping and organizational boundaries frequently need to be restructured as usage patterns change'
---

## Transfers

Alexander's pattern #67 observes that the open spaces in a city or
building must form a hierarchy of sizes, from the largest public
squares down through neighborhood commons, shared courtyards, and
private gardens. When this hierarchy is absent -- when all open spaces
are the same size, or when the graduation from public to private is
missing intermediate steps -- people cannot find the right kind of
space for their activity, and the spaces go unused.

Key structural parallels:

- **Flat collections fail** -- a city with only large plazas and
  private backyards, but no intermediate-scale courtyards or pocket
  parks, forces people into a binary choice: fully public or fully
  private. The intermediate activities -- a conversation with
  neighbors, children playing within earshot of parents, a small
  gathering of friends -- have nowhere to happen. In software, a
  system with only global scope and function-local scope (but no
  module scope, package scope, or namespace scope) forces the same
  binary choice. Variables are either visible to everything or visible
  to nothing. The intermediate visibilities -- shared within a team's
  codebase, accessible to a subsystem, visible within a bounded
  context -- have no home. The pattern predicts that systems with
  more levels of scoping hierarchy will support more varied usage
  patterns.

- **Each level is defined relationally** -- a courtyard does not feel
  semi-private because of an absolute property. It feels semi-private
  because it is smaller than the street and larger than the doorstep,
  quieter than the market and louder than the bedroom. The hierarchy
  is a gradient, not a set of absolute categories. In access control
  systems, "team-visible" has no meaning in isolation; it gains meaning
  from being more restricted than "org-visible" and less restricted
  than "owner-only." The pattern argues that each level of access
  should be understood as a position in a gradient, not as an
  independent permission.

- **Skipped levels create dead zones** -- if a building opens
  directly onto a busy street with no entrance court, stoop, or
  porch, the transition from public to private is too abrupt. People
  linger neither on the street (too exposed) nor in the building
  (too enclosed). They rush past the boundary. In software, the
  equivalent is an API that exposes raw internal data structures to
  external consumers with no intermediate transformation layer. The
  jump from fully internal to fully external is too large, making
  both the internal structure and the external interface harder to
  use. The pattern predicts that introducing intermediate layers
  (DTOs, facade APIs, BFF services) will make both sides more usable.

- **The hierarchy supports simultaneous diverse use** -- a well-
  graduated open space system lets a political rally happen in the
  plaza while a couple reads in the courtyard and a child naps in
  the garden, all at the same time, without conflict. The hierarchy
  sorts activities by their appropriate scale and privacy level. In
  information architecture, nested scoping serves the same function:
  global configuration, service-level settings, and request-scoped
  overrides can coexist without collision because each operates at
  its appropriate level. Without the hierarchy, all configuration
  would compete in a single flat namespace.

- **The smallest spaces anchor the hierarchy** -- Alexander notes
  that the hierarchy works only if the smallest, most private spaces
  are genuinely intimate: a garden bench, a window seat, a doorstep.
  Without these anchors, the larger spaces lose their meaning because
  there is nothing for the gradient to terminate in. In software, a
  scoping hierarchy that includes package scope and module scope but
  not block scope or closure scope is incomplete -- the finest-grained
  privacy level gives the coarser levels their semantic weight.

## Limits

- **Digital spaces have no natural capacity** -- a physical courtyard
  holds twenty people; add fifty more and it feels crowded, signaling
  that you have exceeded its level in the hierarchy. A Slack channel
  has no such physical constraint. It can hold five people or five
  thousand, and the name "team-discussion" provides no felt sense of
  appropriate scale. The physical feedback that enforces the hierarchy
  in architecture is absent in digital systems, requiring explicit
  rules (member limits, access reviews) to substitute for spatial
  intuition.

- **Cultural norms about privacy vary** -- Alexander's hierarchy
  assumes a shared understanding of what constitutes public, semi-
  public, and private behavior. A courtyard in Barcelona functions
  differently from a courtyard in Tokyo. In global organizations
  and multi-tenant systems, the users at each level may have
  conflicting expectations about what belongs there. A "team-visible"
  channel in a high-context culture and a low-context culture will
  develop very different norms, and the hierarchy alone cannot
  resolve this.

- **The hierarchy assumes top-down design** -- Alexander presents
  the hierarchy as something an architect plans in advance, with
  each level sized and positioned to serve its purpose. Software
  scoping and organizational boundaries, however, emerge and change
  as usage evolves. A namespace hierarchy designed for one product
  may need restructuring when the product splits into two. The
  pattern provides no guidance for how to refactor a hierarchy when
  the underlying activities change, which is one of the hardest
  problems in software architecture.

- **Over-graduation creates friction** -- a scoping system with
  seven levels of access (public, org, department, team, project,
  module, owner) may be more graduated than necessary, creating
  bureaucratic overhead in deciding which level each artifact belongs
  to. The pattern diagnoses the problem of too few levels but does
  not adequately warn against too many, which trades the original
  problem (no intermediate scope) for a new one (decision paralysis
  about which scope to use).

## Expressions

- "Nested scoping" -- programming language term for hierarchical
  variable visibility (block, function, module, package, global)
- "Defense in depth" -- security architecture principle that layers
  protections hierarchically from perimeter to asset
- "Information architecture" -- the design of hierarchical content
  organization in websites and applications
- "Graduated access control" -- security model with multiple levels
  of permission (public, internal, confidential, restricted)
- "The funnel" -- product design metaphor for hierarchical narrowing
  from broad awareness to specific conversion
- "Peel the onion" -- describing hierarchical exploration from
  outer layers to inner core

## Origin Story

Christopher Alexander's pattern #67, "Hierarchy of Open Space,"
appears in *A Pattern Language* (1977). Alexander observed that
modernist urban planning had flattened the rich hierarchy of
traditional cities -- which graduated smoothly from public square
through market street, neighborhood lane, shared courtyard, private
garden, and doorstep -- into a binary of public parks and private
lots. The result was that intermediate-scale social life (the
neighborhood conversation, the courtyard gathering, the stoop-
sitting) had no spatial support and withered.

The pattern's influence on software is indirect but pervasive.
When programming language designers created nested scoping rules
(Algol's block structure, Java's package-private access, Rust's
module visibility), they solved the same problem Alexander
identified: a flat namespace (all variables global) supports only
two modes (everything visible or nothing visible), while a nested
hierarchy supports the full range of intermediate visibilities that
real programs need.

## References

- Alexander, Christopher. *A Pattern Language* (1977), Pattern #67:
  Hierarchy of Open Space
- Parnas, David L. "On the Criteria to Be Used in Decomposing
  Systems into Modules" (1972) -- the software parallel for
  hierarchical information hiding
- Saltzer, Jerome H. & Schroeder, Michael D. "The Protection of
  Information in Computer Systems" (1975) -- graduated access
  control as a design principle
