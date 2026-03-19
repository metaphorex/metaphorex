---
applies_to:
- software-abstraction
author: agent:metaphorex-miner
categories:
- software-engineering
- systems-thinking
contributors:
- fshot
created: '2026-03-19'
harness: Claude Code
kind: pattern
name: Paths and Goals
related:
- a-place-to-wait
- entrance-transition
slug: paths-and-goals
source_frame: architecture-and-building
updated: '2026-03-19'
transfers:
  - '[source] a path that does not reveal its destination creates anxiety, while a path with a visible goal pulls the traveler forward without coercion'
  - '[source] the goal need not be the final destination -- intermediate visible landmarks sustain motivation across longer journeys'
  - '[source] paths that meander without purpose feel longer than direct paths of the same length, because perceived progress depends on visible approach toward a target'
limits:
  - '[source] breaks because physical paths offer continuous sensory feedback (the goal gets closer with each step), while digital navigation provides only discrete state changes (page 1, page 2, done)'
  - '[source] misleads by assuming a single visible goal per path, when digital interfaces often serve users with divergent intentions who need the same path to suggest different destinations'
---

## Transfers

Alexander's pattern #120, "Paths and Goals," observes that people will not
walk down a path unless they can see something at the end of it -- or at
least at the next turning. A path that disappears into featureless distance
repels; a path that curves toward a visible landmark invites. The goal gives
the path its purpose. The path gives the goal its approach.

Key structural parallels:

- **Visible goals create motivation without coercion** -- a garden path
  curving toward a bench under a tree does not need a sign saying "walk
  here." The visible destination does the work. In user interface design,
  this maps onto progressive disclosure: showing the user what comes next
  (a preview, a summary, a progress indicator) rather than asking them to
  proceed on faith. The visible goal replaces the instruction manual.
- **Intermediate landmarks sustain long journeys** -- Alexander notes that
  very long paths need intermediate goals: a fountain halfway down a
  corridor, a window at a landing. Without them, the path feels endless.
  In multi-step workflows (onboarding, checkout, application forms), this
  maps onto progress bars, step indicators, and section headers that tell
  the user "you are here, and here is what is ahead." Each intermediate
  goal is a micro-destination that renews the motivation to continue.
- **The path shapes the experience of the goal** -- a winding approach
  through a garden creates anticipation that a straight sidewalk does not.
  The path is not merely functional (getting you there) but experiential
  (shaping how arrival feels). In software, this maps onto the difference
  between a dashboard that dumps all data at once and a guided flow that
  reveals information in a sequence designed to build understanding. The
  path is the pedagogy.
- **Paths without goals become corridors** -- Alexander distinguishes
  between paths (which lead somewhere visible) and corridors (which are
  enclosed passages with no visible terminus). Corridors create anxiety:
  you cannot see where you are going. In software, this maps onto nested
  menu hierarchies where each click reveals another menu with no preview
  of the content behind it. The user is in a corridor, not on a path.
- **The pattern is bidirectional** -- a well-designed path also lets you
  see where you came from, which provides orientation and the option to
  return. In navigation design, this is the breadcrumb trail, the back
  button, the persistent header showing your location in the hierarchy.
  Alexander's pattern implies that wayfinding requires both forward
  visibility (where am I going?) and backward visibility (where have I
  been?).

## Limits

- **Physical paths provide continuous feedback; digital paths do not** --
  walking toward a visible tree, you see it grow larger with every step.
  The feedback is continuous and proportional. Clicking through a wizard,
  you get discrete jumps: step 1, step 2, step 3. There is no sense of
  gradual approach. The architectural pattern assumes analog feedback that
  digital interfaces can only simulate with progress bars and animations.
- **Digital goals serve divergent intentions** -- a garden path leads one
  place. A homepage serves users who want to buy, users who want support,
  users who want to learn, and users who arrived by accident. The pattern
  assumes a single visible goal, but digital navigation must somehow show
  multiple goals without overwhelming the traveler. This is a fundamental
  mismatch between architectural and digital wayfinding.
- **The pattern can justify over-guiding** -- Alexander's paths lead to
  specific goals. Applied naively to software, this produces wizard-style
  interfaces that force a linear path when the user actually needs lateral
  movement. Power users, in particular, resent being funneled down a path
  when they know exactly where they want to go. The pattern can be
  misapplied to constrain rather than invite.
- **Not all digital journeys have a spatial metaphor** -- Alexander's
  pattern depends on the physical experience of walking, seeing, and
  approaching. Some digital tasks (search, filtering, configuration) do
  not map naturally onto paths at all. Forcing a path-and-goal structure
  onto inherently non-linear interactions produces awkward metaphorical
  misfits.
- **Visible goals assume the designer knows what the user wants** -- the
  pattern works when the architect correctly anticipates where people want
  to go. When the anticipation is wrong, the visible goal becomes a
  distraction or a presumption. In software, this manifests as "helpful"
  suggestions that misread user intent and clutter the interface with
  goals the user did not ask for.

## Expressions

- "Can the user see where they're going?" -- the design review question,
  directly descended from Alexander's observation
- "Progressive disclosure" -- the UX principle of revealing information in
  stages, each stage a visible goal on the path
- "Breadcrumb trail" -- the backward-visibility component of the pattern,
  showing the path already traveled
- "Above the fold" -- the newspaper/web term for what is immediately
  visible, serving as the first goal on the path
- "Call to action" -- the visible goal made explicit: a button, a link,
  a prompt that tells the user where the path leads
- "Dead end" -- what happens when the path reaches a point with no visible
  next goal: the user stops

## Origin Story

Christopher Alexander's pattern #120, "Paths and Goals," appears in
*A Pattern Language* (1977). Alexander's observation was architectural:
people avoid paths that do not show them where they are going. He
recommended that every path in a building or town should lead toward
a visible goal -- a doorway, a tree, a view, a landmark -- and that
long paths should include intermediate goals at turnings and landings.

The pattern transferred to interface design through the general migration
of Alexander's work into software (via the Gang of Four and the pattern
language movement). Its specific application to UX design became explicit
in the 2000s, as web designers confronted the problem of users
abandoning multi-step processes. The insight that visibility of the
destination predicts completion of the journey proved as true for
checkout flows as for garden paths. The pattern remains active in UX
discourse, where "can the user see the goal?" is a standard heuristic.

## References

- Alexander, C. *A Pattern Language* (1977), Pattern #120: Paths and Goals
- Krug, S. *Don't Make Me Think* (2000) -- web usability principles
  that echo Alexander's wayfinding patterns
- Norman, D. *The Design of Everyday Things* (1988) -- affordances and
  visibility as design principles, closely related to Alexander's goals
