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
- '[source] breaks because physical chairs are independent objects that do not interact with each other -- an armchair does not conflict with a stool -- while multiple software interface modes share underlying state, event handling, and rendering logic, creating interaction bugs that have no architectural equivalent'
- '[source] misleads by implying that adding variety is cheap and additive, when each additional software interface mode multiplies the testing surface combinatorially and creates maintenance burden that scales nonlinearly with the number of modes'
- '[source] assumes that users choose the right chair for their mood instinctively, but software interface mode selection requires explicit user action (toggling settings, choosing views, configuring preferences), introducing a meta-interface problem that physical furniture does not have'
name: Different Chairs
summary: "A single seating type forces a single posture. Varied interface modes support varied cognitive tasks."
provenance: alexander-pattern-language
related:
- natural-doors-and-windows
- ornament
slug: different-chairs
source_frame: architecture-and-building
transfers:
- '[source] imports the principle that a single seating option forces a single posture on all occupants at all times, framing one-size-fits-all interface design as a form of ergonomic coercion that serves the designer''s convenience rather than the user''s needs'
- '[source] carries the insight that variety in seating supports variety in activity -- a hard chair for focused work, a soft chair for reading, a bench for conversation -- mapping onto the observation that different interface modes support different cognitive tasks'
- '[source] establishes that the variety must be co-present and visible, not hidden behind a configuration screen, importing the principle that multiple modes should be discoverable through the environment itself rather than through documentation'
updated: '2026-03-21'
embodied_patterns:
  - matching
  - part-whole
  - container
relation_types:
  - select
  - coordinate
structure: network
abstraction_level: specific
---

## Transfers

Alexander's pattern #251, "Different Chairs," observes that a room furnished
with identical chairs serves only one posture and one mood. A living room
with nothing but a sofa accommodates lounging but not reading, conversation
but not solitary work. Alexander argues that a well-furnished room needs
different kinds of seating -- a hard chair for the desk, a soft armchair
for reading, a window seat for watching the street, a bench for
conversation -- because human activity is varied and a single seating type
cannot support the range of things people do in a room.

Key structural parallels:

- **One-size-fits-all design serves no one well** -- Alexander's core
  argument is that homogeneous furnishing optimizes for the average case
  and fails everyone else. In software, a single interface mode that
  balances simplicity for beginners with power for experts typically
  achieves neither. The pattern argues that multiple interface modes --
  a simple view and an advanced view, a GUI and a CLI, a wizard and a
  manual configuration -- are not design failures but design necessities.

- **Different chairs support different cognitive tasks** -- a hard,
  upright chair supports focused work; a soft chair supports relaxed
  reading; a window seat supports contemplation. In software, different
  interface modes support different cognitive tasks: a dashboard supports
  monitoring, a spreadsheet view supports analysis, a kanban board
  supports workflow management. The pattern frames interface variety as
  cognitive ergonomics, not feature bloat.

- **Variety must be co-present and visible** -- Alexander insists that the
  different chairs be in the same room, not stored in a closet. The user
  should see the options and choose based on current need. In software,
  this means interface modes should be discoverable -- visible tabs, mode
  toggles, or contextual alternatives -- not buried in settings menus or
  preference dialogs. The pattern distinguishes between available variety
  (options exist somewhere in the system) and accessible variety (options
  are visible in the current context).

- **The room determines what chairs are needed** -- Alexander does not
  prescribe a universal set of chairs. A kitchen needs different seating
  than a living room. The chairs should match the room's function. In
  software, the interface modes needed depend on the product's function:
  a code editor needs a command palette and a visual debugger; a project
  management tool needs a list view and a timeline view. The pattern
  argues against both uniformity (one mode) and gratuitous variety
  (every possible mode) in favor of functional variety calibrated to
  actual use cases.

- **Accessibility as a chair type** -- one of Alexander's different chairs
  might be a wheelchair-height surface or a seat with back support for
  someone with a bad back. The pattern naturally encompasses accessibility:
  screen reader support, keyboard navigation, high-contrast modes, and
  reduced-motion options are not accommodations bolted onto a finished
  design but additional "chairs" that make the room usable by more people.

## Limits

- **Physical chairs do not interact; software modes do** -- an armchair
  and a desk chair coexist peacefully in a room. But software interface
  modes share underlying state, event handling logic, rendering engines,
  and data models. A bug in the kanban view can corrupt data visible in
  the list view. The pattern's implication that variety is additive and
  non-interfering does not hold when multiple views must maintain
  consistency over shared mutable state.

- **Each additional mode multiplies testing surface** -- adding a chair
  to a room adds one chair. Adding an interface mode to software adds a
  combinatorial expansion of states to test: every feature must work in
  every mode, every mode must handle every edge case, every mode
  transition must be consistent. The pattern's architectural metaphor
  dramatically understates the cost of variety in software.

- **Chair selection is intuitive; mode selection is explicit** -- in a
  room with different chairs, you walk to the one that suits your current
  mood. No configuration required. In software, switching interface modes
  requires explicit user action: clicking a toggle, changing a setting,
  selecting a view. This introduces a meta-interface problem -- the
  interface for choosing interfaces -- that has no architectural
  equivalent. Users who need a different mode may not know it exists
  or how to activate it.

- **The pattern can justify feature bloat** -- Alexander's argument that
  a room needs different chairs can be misapplied to justify adding
  every requested interface mode. The pattern provides no principle for
  when to stop adding variety. In practice, too many modes create
  confusion, fragment the user base, and dilute engineering attention.
  The architectural metaphor of a room with twelve different chairs
  suggests hoarding, not design.

## Expressions

- "Multiple views" -- list view, grid view, calendar view, kanban view:
  the software realization of different chairs for different tasks
- "Power user mode" -- an advanced interface alongside a simple one,
  the desk chair next to the armchair
- "Accessibility modes" -- screen reader support, high contrast, reduced
  motion: chairs designed for bodies the default furniture ignores
- "Progressive disclosure" -- showing simple options first with advanced
  options available on demand, the equivalent of placing the comfortable
  chair in the foreground and the desk chair in the corner
- "Responsive design" -- adapting the interface to the device, giving
  the phone user a different chair than the desktop user

## Origin Story

Pattern #251 in *A Pattern Language* (1977) grew from Alexander's
observation that modern furniture design and interior decoration
favored matching sets -- identical dining chairs, matching sofas,
coordinated office seating. He argued that this aesthetic consistency
came at the cost of functional variety. Traditional homes, he observed,
accumulated different seating over time: a grandfather's armchair, a
kitchen bench, a window seat built into the wall, a stool by the fire.
Each served a different purpose and invited a different kind of use.
The pattern anticipated the software industry's discovery that
one-size-fits-all interfaces serve no one well -- a lesson learned
through the repeated failure of universal dashboards, single-mode
editors, and uniform administrative interfaces.

## References

- Alexander, Christopher. *A Pattern Language* (1977), Pattern #251:
  Different Chairs
- Cooper, Alan. *About Face* (1995) -- persona-based design as the
  argument for different interfaces serving different user types
- Nielsen, Jakob. "Usability for Senior Citizens" (2002) -- accessibility
  as a different-chairs problem
- Tidwell, Jenifer. *Designing Interfaces* (2005) -- pattern catalog of
  alternative interface modes for the same underlying function
