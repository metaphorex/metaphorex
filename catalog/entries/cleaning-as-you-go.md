---
applies_to:
- software-programs
- organizational-behavior
author: agent:metaphorex-miner
categories:
- software-engineering
- organizational-behavior
contributors: []
created: '2026-03-19'
grounding: established
harness: Claude Code
kind: pattern
name: Cleaning As You Go
summary: "Deferred cleanup compounds nonlinearly. One dirty pan is a nuisance; five block the station. Cleaning is production, not overhead."
related:
- technical-debt
slug: cleaning-as-you-go
source_frame: food-and-cooking
transfers:
  - '[source] in professional kitchens, deferred cleanup compounds geometrically: one dirty pan becomes a blocked station becomes a missed ticket becomes a crashed service, because workspace contamination spreads faster than the cook can contain it'
  - '[source] the practice is enforced by physical constraint -- a cook with no clean cutting board cannot start the next prep task -- making the cost of deferral immediate and visible rather than abstract and deferred'
  - '[source] cleaning is not interrupting the cooking; it is part of the cooking, integrated into the rhythm of production rather than treated as a separate post-production phase'
limits:
  - '[source] breaks because kitchen mess is visible and physical (a dirty station is immediately obvious to anyone), while code mess is abstract and invisible until someone reads the code, making the feedback loop much weaker in software'
  - '[source] misleads because professional kitchens clean to a known standard (health code compliance, mise en place reset), while "clean code" is subjective and contested, so "clean as you go" in software lacks the objective stopping criterion that makes it workable in kitchens'
updated: '2026-03-19'
embodied_patterns:
  - removal
  - iteration
  - flow
relation_types:
  - restore
  - prevent
  - coordinate
structure: cycle
abstraction_level: generic
---

## Transfers

In a professional kitchen during service, a cook who lets dirty pans
accumulate, who leaves spills unwiped and cutting boards cluttered,
will crash within the hour. The station becomes unusable. Orders back
up. The line breaks down. This is not a matter of aesthetics or
discipline for its own sake -- it is a structural constraint. A cook
cannot plate a dish on a dirty surface. A cook cannot saute in a pan
coated with burnt fond from the last order. The work demands
continuous maintenance of the workspace as a prerequisite for
continued production.

Dan Charnas documented this as the third principle of *mise en place*
in *Work Clean* (2016): "Clean as you go." The principle is older
than the book -- it is fundamental to the brigade system Escoffier
formalized in the 1890s -- but Charnas articulated its cross-domain
structure explicitly.

Key structural parallels:

- **Deferred cleanup compounds nonlinearly** -- one dirty pan is a
  nuisance. Three dirty pans block a burner. Five dirty pans mean
  the cook is reaching across the station, bumping neighbors, slowing
  down. The cost of mess grows faster than the mess itself, because
  each piece of clutter reduces the available workspace for managing
  the remaining clutter. In software, deferred refactoring behaves
  the same way: one hack is tolerable, three hacks interact, five
  hacks make the codebase resistant to any change at all.
- **The constraint is spatial, not moral** -- professional cooks do
  not clean because they are virtuous. They clean because they
  literally cannot do the next task if they do not. The cutting
  board is full. The pan is dirty. The principle works because the
  feedback is immediate and physical. When this pattern transfers
  to software, the most effective implementations create analogous
  physical constraints: CI pipelines that reject code below a
  complexity threshold, linters that block merges, pair programming
  that makes mess immediately visible to another person.
- **Cleaning is production, not overhead** -- the novice cook treats
  cleaning as something that happens after cooking. The professional
  treats it as part of cooking. Wiping down the board between cuts,
  deglazing the pan between orders, resetting the station between
  courses -- these are movements integrated into the cooking rhythm,
  not interruptions of it. The Boy Scout Rule in software ("leave
  the code cleaner than you found it") attempts the same integration,
  but often fails because developers treat refactoring as separate
  from feature work rather than as part of it.

## Limits

- **Kitchen mess is visible; code mess is not** -- a dirty station
  announces itself to everyone in the kitchen. A messy codebase
  looks the same as a clean one to anyone who is not reading it
  closely. This difference in visibility means that "cleaning as you
  go" in kitchens is socially enforced (the chef will see your mess)
  while in code it requires deliberate inspection (code review, static
  analysis). The pattern transfers the behavior but not the
  enforcement mechanism.
- **Kitchen cleanliness has an objective standard** -- health codes
  define clean. Mise en place has a reset state. A cook knows when
  the station is clean. "Clean code" is contested territory: what
  counts as clean depends on the team, the language, the project
  phase, and personal taste. Without an agreed standard, "clean as
  you go" becomes "refactor according to my preferences," which
  creates conflict rather than reducing entropy.
- **The kitchen resets every service** -- a kitchen starts each
  service from a known clean state. Software accumulates. There is
  no "end of service" that forces a full reset. The pattern works
  in kitchens partly because the cleaning cycle has a hard endpoint;
  in software, code persists indefinitely and "cleaning as you go"
  must contend with years of accumulated decisions, not just
  tonight's orders.
- **Over-cleaning wastes capacity** -- a cook who cleans obsessively
  during a rush will fall behind on orders. The skill is knowing
  when to clean (between tickets, during natural pauses) and when
  to push through the mess. In software, the analogous risk is
  premature refactoring: cleaning code that is about to be thrown
  away, or polishing code that works fine but offends someone's
  sensibility. The pattern does not include a throttle, and
  uncritical application creates its own waste.

## Expressions

- "Clean as you go" -- the direct kitchen imperative, used in
  software teams that adopt culinary metaphors for development
  discipline
- "Leave it cleaner than you found it" -- the Boy Scout Rule,
  an independent formulation of the same structural pattern from
  a different source domain
- "Wipe down your station" -- kitchen shorthand for resetting
  workspace to a known state, adopted metaphorically in Agile
  retrospectives
- "Don't let it pile up" -- generic version applied to email,
  code review queues, and technical debt
- "Mise en place your desk" -- productivity culture borrowing
  from Charnas, applying kitchen discipline to knowledge work

## References

- Charnas, D. *Work Clean: The Life-Changing Power of Mise-en-Place
  to Organize Your Life, Work, and Mind* (2016) -- the cross-domain
  articulation
- Escoffier, A. *Le Guide Culinaire* (1903) -- codification of the
  brigade system and station discipline
- Martin, R.C. *Clean Code* (2008) -- the Boy Scout Rule as an
  independent software formulation
