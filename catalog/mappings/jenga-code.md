---
author: agent:metaphorex-miner
categories:
- software-engineering
contributors:
- fshot
harness: Claude Code
kind: conceptual-metaphor
name: Jenga Code
related:
- spaghetti-code
- big-ball-of-mud
- boat-anchor
slug: jenga-code
source_frame: puzzles-and-games
target_frame: software-programs
---

## What It Brings

A Jenga tower is a stack of wooden blocks where players take turns
removing pieces from lower levels and placing them on top. The tower
grows taller and more precarious with each move until someone's
extraction causes collapse. This maps onto codebases where every
component is load-bearing, every change risks catastrophe, and the
system grows more fragile with each modification.

Key structural parallels:

- **Every piece is structural** -- in a Jenga tower, there are no
  decorative blocks. Every piece bears load, and removing any one of
  them redistributes stress to the remaining structure. In jenga code,
  there are no isolated modules: every function, every class, every
  configuration value is depended upon by something else. You cannot
  remove or modify anything without potentially destabilizing the whole
  system. The metaphor captures the specific horror of code with no
  safe deletion candidates.
- **Increasing fragility over time** -- a Jenga tower starts stable
  and becomes progressively more precarious as pieces are rearranged.
  Each successful extraction makes the next one riskier. This maps
  precisely onto codebases that accumulate technical workarounds: each
  patch succeeds locally but makes the global structure more fragile.
  The system's history of surviving changes is not evidence of
  robustness; it is evidence of luck running out.
- **Visible precariousness** -- a Jenga tower in its late stages
  *looks* dangerous. It leans, it wobbles, gaps yawn where blocks
  were removed. Jenga code has the same quality: developers can often
  see the fragility without needing analysis tools. The test suite is
  brittle, the deployment process is a 47-step manual checklist, the
  error handling consists of catch-all blocks that swallow exceptions.
  The visual wobble of the tower maps onto the experiential wobble
  of working with the code.
- **Collapse is total** -- when a Jenga tower falls, it does not
  partially collapse. The whole thing comes down. This maps onto
  systems where failure is not graceful: one bug does not produce a
  degraded experience but a complete outage, a corrupted database, or
  a cascade that takes down dependent services.

## Where It Breaks

- **Jenga is a game with rules; software development is not** -- in
  Jenga, you must remove a block and place it on top. You cannot add
  new blocks, reinforce existing ones, or rebuild sections while
  playing. Software developers have options that Jenga players do not:
  they can add tests, introduce abstractions, refactor incrementally,
  and run the system in staging before touching production. The
  metaphor imports a helplessness that software engineering does not
  actually impose.
- **The metaphor suggests uniform fragility** -- in Jenga, any block
  might be the critical one. In real codebases, fragility is uneven:
  some modules are genuinely robust and well-tested, while others are
  held together by coincidence. The metaphor flattens this
  heterogeneity, suggesting that the entire system is equally
  dangerous to touch, which can paralyze developers who would
  otherwise refactor the safe parts confidently.
- **Jenga towers have no functionality** -- a Jenga tower's only
  purpose is to stand up. Software exists to do things. The metaphor
  captures structural integrity but misses functional complexity: the
  reason jenga code is hard to change is not just that it might fall
  down but that it does useful work in ways nobody fully understands.
  Structural fragility and functional opacity are different problems,
  and the metaphor conflates them.
- **Collapse in Jenga is entertaining; in software it is costly** --
  Jenga is a game precisely because the collapse is fun. The stakes
  are zero. This mismatch of affect can trivialize real engineering
  risk: calling a production system "jenga code" might generate
  knowing laughter when it should generate urgent investment in
  stabilization.

## Expressions

- "This codebase is a Jenga tower" -- the diagnosis, usually delivered
  while staring at a dependency graph or a failed deployment
- "Don't pull that block" -- warning a colleague away from modifying a
  particularly load-bearing component
- "It's one pull request away from collapse" -- the crisis framing,
  expressing that any change could be the one that brings the system
  down
- "We're playing Jenga with production" -- escalating the metaphor to
  signal that risky changes are being made to live systems
- "Which block do we remove first?" -- the refactoring planning
  question, acknowledging that improvement requires accepting risk

## Origin Story

Jenga was created by Leslie Scott and first sold in 1983, based on a
game her family played with wooden blocks in Ghana in the 1970s. The
name comes from the Swahili word *kujenga*, meaning "to build." The
game became globally popular and culturally ubiquitous, making the
tower a universally recognized image of precarious balance.

The application to software emerged naturally in developer culture as
codebases aged and accumulated the kind of tight coupling and fragile
interdependence that the game embodies. The metaphor gained traction in
blog posts and conference talks from the 2010s onward, particularly in
discussions about legacy systems and the costs of deferred maintenance.

## References

- Scott, L. *About Jenga* (2010) -- the creator's account of the
  game's origins and design philosophy
- Feathers, M. *Working Effectively with Legacy Code* (2004) --
  describes the structural fragility that the Jenga metaphor names
- Kim, G. et al. *The Phoenix Project* (2013) -- fictional account of
  a system with Jenga-like characteristics and the organizational
  changes needed to stabilize it