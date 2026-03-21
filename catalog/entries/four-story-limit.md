---
slug: four-story-limit
name: Four-Story Limit
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
  - the-facade-pattern
  - scaffolding
created: '2026-03-21'
updated: '2026-03-21'
grounding: folk
harness: Claude Code
embodied_patterns:
  - scale
  - surface-depth
  - near-far
relation_types:
  - prevent
  - cause
structure:
  - hierarchy
abstraction_level: specific
transfers:
  - '[source] buildings above four stories require elevators, which replace the continuous experience of climbing stairs with a discontinuous jump between floors, severing the occupant''s proprioceptive connection to the ground'
  - '[source] each additional story above the limit increases the structural engineering required disproportionately -- wind load, foundation depth, and fire-safety systems scale nonlinearly with height'
  - '[source] the four-story threshold marks where a building transitions from a structure whose occupants can see and be seen from the street to one that produces anonymity, because faces become unrecognizable beyond roughly 40 feet'
limits:
  - '[source] breaks because the specific number (four) is calibrated to human visual acuity and stair-climbing tolerance, which have no analogue in software -- there is no biomechanical basis for any particular depth limit on class hierarchies'
  - '[source] misleads by implying that height is the only dimension of complexity, when software abstraction hierarchies also have breadth (number of sibling classes) and coupling (dependencies between layers) that have no spatial equivalent in building height'
---

## Transfers

Alexander's Pattern 21 in *A Pattern Language* argues that buildings above
four stories are harmful to their inhabitants. His reasoning is spatial and
physiological: above four stories, you cannot see the ground clearly, you
cannot recognize faces on the street, and you depend on elevators rather
than stairs. The building becomes a machine for vertical transport rather
than a place to live. High-rise housing, Alexander argues, produces
alienation, isolation, and disconnection from community life.

Key structural parallels:

- **Depth creates disconnection** -- in software, deep inheritance
  hierarchies produce the same alienation Alexander describes. A developer
  working at the sixth level of a class hierarchy cannot "see the ground" --
  the base class behavior is obscured by overrides, mixins, and intermediate
  abstractions. The GoF's preference for composition over inheritance is
  Alexander's four-story limit restated for object-oriented design: keep
  the abstraction stack shallow enough that you can trace behavior to its
  source without mechanical assistance (debuggers as elevators).
- **Nonlinear cost scaling** -- a four-story building needs stairs and
  load-bearing walls. A forty-story building needs elevators, reinforced
  foundations, pressurized stairwells, and wind-load engineering. The cost
  per floor is not constant; it accelerates. Software abstraction layers
  exhibit the same nonlinearity: each additional layer of indirection adds
  cognitive load, increases the surface area for bugs, and makes the system
  harder to reason about. The first few layers are cheap; the subsequent
  layers are expensive in ways the first layers did not predict.
- **The elevator problem** -- above four stories, you need an elevator, which
  is a fundamentally different navigation mode from stairs. Stairs are
  continuous and self-paced; elevators are discontinuous and opaque (you
  enter a box, wait, and emerge somewhere else). In software, deep
  abstraction stacks force developers to use IDE navigation tools (go to
  definition, find all references) rather than reading code linearly.
  The tools work, but they replace understanding with lookup -- just as
  the elevator replaces the experience of ascending with the experience
  of teleporting.
- **Human-scale thresholds** -- Alexander's insight is that there is a
  threshold beyond which a building stops working for humans. The number
  is not arbitrary; it comes from human physiology. Software has analogous
  thresholds: Miller's 7 plus or minus 2 for working memory, the rule of
  three for refactoring triggers, the common guideline of no more than
  3-4 levels of nesting. These are cognitive rather than physiological
  limits, but the structural logic is the same: beyond a certain depth,
  the system exceeds the operator's capacity to hold it in mind.

## Limits

- **The number is not transferable** -- four stories is calibrated to
  specific human constraints: visual acuity at distance, willingness to
  climb stairs, the social range of face recognition. There is no
  biomechanical basis for a specific depth limit on software hierarchies.
  Claims like "never more than three levels of inheritance" borrow
  Alexander's rhetorical confidence without his empirical grounding.
  Software depth limits are heuristics, not physiological facts.
- **Height is one dimension; software complexity is many** -- a building
  is tall or short. A software system has depth (inheritance), breadth
  (number of classes at each level), coupling (dependencies between
  modules), and temporal complexity (state changes over time). The
  four-story limit addresses only one axis. A three-level hierarchy
  with fifty classes per level and tight coupling between all of them
  may be far worse than a six-level hierarchy with clean separations.
  The metaphor's single-axis framing is seductively simple but
  dimensionally impoverished.
- **Alexander was wrong on his own terms** -- Jane Jacobs and subsequent
  urbanists argued that Alexander's four-story limit romanticized
  low-density living. Dense, tall cities (Hong Kong, Tokyo, Manhattan)
  produce vibrant street life precisely because height concentrates
  population, which concentrates activity. The pattern confuses
  bad high-rise design (isolated towers in empty plazas) with height
  itself. The analogous software critique: deep abstractions are not
  inherently bad; badly designed deep abstractions are bad.
- **The pattern encourages sprawl** -- if you cannot build up, you
  build out. Alexander's low-rise vision requires more land. In
  software, avoiding deep hierarchies can produce sprawling,
  flat codebases where hundreds of classes sit at the same level
  with no organizing structure. The four-story limit solves one
  problem (disconnection from the base) by creating another
  (horizontal disorientation).

## Expressions

- "Deep hierarchy" -- the software term for too many inheritance levels,
  directly mapping to building height
- "Composition over inheritance" -- the GoF remedy, which is Alexander's
  low-rise prescription in software form
- "God class" -- the penthouse suite: a class at the top that tries to
  do everything because the hierarchy beneath it is too tall to navigate
- "Flat is better than nested" -- from the Zen of Python, a direct
  statement of the four-story principle
- "You can't see the ground from here" -- informal developer complaint
  about being lost deep in an abstraction stack

## Origin Story

Pattern 21 in *A Pattern Language* (1977) drew on post-war housing
research, particularly studies of high-rise public housing projects
like Pruitt-Igoe (demolished 1972) and Robin Hood Gardens. Alexander
cited research showing that residents of upper floors had fewer social
connections, that children in high-rises played outside less, and that
crime increased with building height. His four-story limit was an
attempt to codify the threshold where buildings stop being
human-scaled.

The pattern entered software discourse indirectly, through the design
patterns movement that explicitly acknowledged Alexander as an
intellectual ancestor. The GoF's *Design Patterns* (1994) cited
Alexander in its introduction. While no GoF pattern directly maps to
the four-story limit, the general preference for shallow, composable
structures over deep, rigid hierarchies reflects Alexander's
conviction that there are human-scale limits to structural complexity.

## References

- Alexander, C., Ishikawa, S., and Silverstein, M. *A Pattern Language:
  Towns, Buildings, Construction* (1977), Pattern 21
- Gamma, E. et al. *Design Patterns: Elements of Reusable Object-
  Oriented Software* (1994)
- Newman, Oscar. *Defensible Space: Crime Prevention Through Urban
  Design* (1972) -- empirical basis for Alexander's height arguments
- Jacobs, Jane. *The Death and Life of Great American Cities* (1961) --
  the counter-argument for density
