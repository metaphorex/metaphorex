---
applies_to:
- software-abstraction
author: agent:metaphorex-miner
categories:
- software-engineering
- systems-thinking
contributors: []
created: '2026-03-19'
harness: Claude Code
kind: metaphor
limits:
- '[source] breaks because glass panes are structural elements whose size is constrained by material strength and manufacturing limits, while software component size is a design choice unconstrained by material properties -- there is no physical reason a function cannot be 10,000 lines long'
- '[source] misleads by importing the aesthetic warmth of cottage windows as an argument for small components, when the actual value of small software units is testability and replaceability, not visual charm'
- '[source] implies that smaller is always better, but excessively small components create integration overhead -- a window made of hundreds of tiny panes leaks more air through its joints, just as a system of hundreds of microservices spends more time on serialization and network calls than on useful work'
name: Small Panes
provenance: alexander-pattern-language
related:
- deep-reveals
- gradual-stiffening
- the-composite-pattern
slug: small-panes
source_frame: architecture-and-building
transfers:
- '[source] maps the architectural preference for small glass panes over large sheets onto the software principle that small, composable units are more resilient and human-scaled than monolithic ones'
- '[source] imports the structural fact that when a small pane breaks, only that pane needs replacement, while a large sheet of glass requires replacing the entire surface -- mapping directly onto the maintenance advantage of modular software components'
- '[source] structures Alexander''s observation that small panes create a visible grid that helps the eye parse scale and proportion, mapping onto the cognitive benefit of small code units that help developers parse system structure'
updated: '2026-03-19'
embodied_patterns:
  - part-whole
  - boundary
  - container
relation_types:
  - cause
  - transform
structure: hierarchy
abstraction_level: specific
---

## Transfers

Alexander's pattern #239, "Small Panes," argues against the modernist
preference for large plate-glass windows. Large glass sheets are
impressive but fragile, expensive to replace, and create a harsh,
institutional quality. Small panes -- the mullioned windows of
traditional buildings -- are individually replaceable, structurally
forgiving, and create a human-scaled relationship between the inhabitant
and the view.

Mapped to software, this becomes an argument for small, composable units
over monolithic structures: small functions, small modules, small
commits, small services.

Key structural parallels:

- **Individual replaceability** -- when a small pane cracks, you replace
  that pane. When a large sheet of plate glass cracks, you replace the
  entire window -- an expensive, disruptive operation. The software
  parallel is direct: a bug in a small, well-bounded module can be fixed
  or replaced without touching the rest of the system. A bug in a
  monolithic component may require understanding and modifying thousands
  of lines. The metaphor frames modularity as a maintenance strategy,
  not an aesthetic preference.
- **Failure is contained** -- a crack in one small pane does not
  propagate to adjacent panes. The mullion grid acts as a natural
  firebreak. In software, well-defined module boundaries serve the same
  function: a failure in one microservice, one function, or one component
  does not cascade through the system. The metaphor imports the physical
  principle that the grid between panes is a structural asset, not just
  a visual artifact.
- **Human-scaled perception** -- Alexander argues that small panes help
  the eye parse the window's scale. A large sheet of glass has no
  internal reference points; you cannot tell whether it is three feet
  or thirty feet wide without external cues. Small panes provide a
  visual grid that communicates scale immediately. In software, small
  functions and small files provide the same cognitive benefit: a
  developer can hold a 50-line function in their head. A 5,000-line
  file provides no internal landmarks for orientation.
- **Small panes accommodate irregularity** -- a window opening that is
  slightly out of square can be glazed with small panes by adjusting the
  mullion spacing. A large sheet of glass demands precise, rigid
  openings. Software built from small components can accommodate
  irregular requirements -- edge cases, special conditions, platform
  differences -- by swapping or adjusting individual pieces. Monolithic
  systems demand that all requirements be accommodated within a single,
  rigid structure.
- **The grid creates rhythm** -- a wall of small-paned windows has visual
  rhythm that a wall of plate glass does not. The mullion grid is not
  decoration; it is the visible expression of the structural logic. In
  software, a codebase of small, consistently sized modules creates a
  navigational rhythm: each module has a similar scope, a similar
  interface pattern, a similar test structure. This rhythm makes the
  unfamiliar module predictable because it follows the pattern of every
  other module.

## Limits

- **Glass pane size is materially constrained; code unit size is not** --
  historical small panes existed partly because glassmaking could not
  produce large, flat sheets. The constraint was technological, not
  purely aesthetic. Software has no equivalent material constraint on
  unit size. A function can be any length. The metaphor romanticizes a
  constraint that was originally practical, not philosophical, and
  applies it to a medium with no such constraint.
- **Small panes leak more** -- every mullion joint is a potential point
  for air and water infiltration. More panes mean more joints mean more
  potential leaks. The software parallel is real: more module boundaries
  mean more interface contracts, more serialization, more network calls,
  more opportunities for integration bugs. A system of 500 microservices
  spends substantial effort just managing the connections between them.
  The metaphor celebrates the grid but underplays the cost of joints.
- **Plate glass has real advantages** -- large windows provide
  unobstructed views, more light, and a sense of openness that small
  panes cannot match. Modernist architects chose plate glass deliberately,
  not from ignorance of tradition. Similarly, monolithic architectures
  have genuine advantages: simpler deployment, no distributed systems
  complexity, easier debugging, better performance for cross-cutting
  concerns. The metaphor frames large-scale approaches as always
  inferior, which is not true.
- **The metaphor can justify excessive decomposition** -- taken to its
  logical extreme, "smaller is better" produces panes so small they
  obscure the view entirely. Software decomposed into functions of three
  lines each, or services that each handle one HTTP endpoint, can become
  harder to understand than the monolith it replaced. The metaphor
  provides no guidance on the right pane size -- only the direction
  (smaller).
- **Small panes are a static structure; software components interact
  dynamically** -- glass panes sit inertly in their mullion grid. They
  do not call each other, share state, or fail in coordination. Software
  components have complex runtime interactions that the static,
  architectural metaphor does not capture. The real difficulty of
  distributed systems is not decomposition but coordination, and the
  small-panes metaphor has nothing to say about coordination.

## Expressions

- "Microservices" -- the architectural style that takes small panes to
  their logical conclusion in system design
- "Small functions" -- the coding practice of keeping functions short
  and focused, each one a single pane
- "Microcommits" -- the version control practice of committing small,
  self-contained changes, each individually revertible
- "Single Responsibility Principle" -- the SOLID principle that each
  module should have one reason to change, one pane doing one job
- "Component-based UI" -- React, Vue, and similar frameworks that
  decompose interfaces into small, reusable panes
- "The monolith is a single sheet of plate glass" -- diagnostic framing
  of monolithic systems as fragile large-scale structures

## Origin Story

Pattern #239 in *A Pattern Language* (1977) reflects Alexander's
suspicion of industrial-scale solutions. Large sheets of plate glass
became available through industrial manufacturing; traditional builders
used small panes because that was what glassmaking could produce.
Alexander argues that the traditional solution was better not despite
its technological limitations but partly because of them: the
constraint produced a more human result.

The pattern migrated powerfully to software through the microservices
movement of the 2010s and the long-standing software engineering
principle of decomposition. Unix's philosophy of "small, sharp tools"
(programs that do one thing well) is an earlier expression of the same
structural intuition. The tension between small panes and plate glass
maps precisely onto the ongoing debate between microservices and
monoliths -- a debate in which neither side is entirely wrong, because
both the pane size and the joint quality matter.

## References

- Alexander, Christopher. *A Pattern Language* (1977), Pattern #239:
  Small Panes
- Martin, Robert C. "The Single Responsibility Principle" -- the
  software design principle most closely aligned with small panes
- Newman, Sam. *Building Microservices* (2015) -- the architectural
  argument for decomposition into small, independent services
- McIlroy, Doug. "Unix Philosophy" -- the predecessor tradition of
  small, composable tools
