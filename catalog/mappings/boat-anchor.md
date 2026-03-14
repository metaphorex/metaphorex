---
author: agent:metaphorex-miner
categories:
- software-engineering
contributors: []
created: '2026-03-11'
harness: Claude Code
kind: dead-metaphor
name: Boat Anchor
related:
- program-failure-is-bodily-failure
slug: boat-anchor
source_frame: tool-use
target_frame: software-programs
updated: '2026-03-11'
---

## What It Brings

A heavy, useless object that drags you down maps onto obsolete code or
technology kept in a project despite serving no current purpose. The
metaphor originates from military and hobbyist slang for broken
equipment too heavy to move and too expensive to dispose of -- the
decommissioned radar unit that becomes a literal boat anchor because
that is all it is good for. In software, the term captures systems,
libraries, or modules that no one uses, no one understands, and no one
dares remove.

Key structural parallels:

- **Dead weight** -- an anchor's entire function is its weight. When
  that weight serves no purpose (the boat is on land, the anchor is
  broken), it becomes pure encumbrance. Obsolete code is the same: it
  contributes nothing to the system's function but adds to its mass --
  build times, dependency trees, cognitive overhead for anyone reading
  the codebase.
- **Fear of removal** -- nobody removes the boat anchor because it
  might be load-bearing. In software, this fear is often justified:
  the dead module might be referenced by something nobody remembers, or
  it might handle an edge case that surfaces once a year. The metaphor
  captures the organizational paralysis around deletion: it is easier
  to leave dead weight in place than to prove it is truly dead.
- **Sunk cost** -- the boat anchor was expensive once. It represents
  real investment: procurement, installation, training. Obsolete
  software carries the same emotional weight. Someone spent months
  building that module. The team debated its architecture. It has its
  own documentation. Removing it feels like admitting that investment
  was wasted, even when keeping it wastes more.
- **Visible but ignored** -- a boat anchor sitting in a yard is
  conspicuous. Everyone can see it. Nobody does anything about it.
  Similarly, boat-anchor code is often well-known to the team. It
  appears in every code review as a directory people scroll past. Its
  existence is acknowledged in onboarding: "ignore that folder, it's
  legacy." The metaphor captures the strange social phenomenon of
  collectively tolerating known waste.

## Where It Breaks

- **Anchors are deliberately kept; boat-anchor code is accidentally
  kept** -- when people keep a literal boat anchor, they are making a
  conscious choice (often about disposal cost). Software boat anchors
  persist through inertia and fear, not deliberate decision. Nobody
  has a meeting and decides to keep the dead module. It simply
  survives because removing it requires effort and carries risk.
- **Anchors don't interact with other equipment** -- a boat anchor
  sitting in a yard affects nothing around it except the space it
  occupies. Dead code can have invisible interactions: unused imports
  that affect build times, configuration that shadows active settings,
  database tables that accumulate data nobody reads. The metaphor
  underestimates the hidden cost of dead code by framing it as inert.
- **The metaphor is purely negative** -- a real anchor serves a
  critical function: it keeps the boat from drifting. The "boat anchor"
  metaphor only invokes the anchor after it has been repurposed as
  dead weight, discarding the anchor's actual purpose. This framing
  prevents the useful question: was this code once an anchor in the
  good sense, holding something important in place? And if so, what
  replaced that function?
- **Weight is visible; code mass is not** -- you can see that a boat
  anchor is heavy. The weight of dead code is measured in compilation
  time, dependency conflicts, and developer confusion -- none of which
  are immediately visible. The metaphor's physicality can create a
  false sense that boat-anchor code would be obvious, when in practice
  identifying truly dead code requires careful analysis.

## Expressions

- "That module is a boat anchor" -- the canonical usage, declaring code
  obsolete and burdensome
- "Nobody wants to touch it" -- the fear of removal that keeps boat
  anchors in place
- "It's load-bearing dead code" -- the paradox of code that appears
  dead but might be structurally necessary, usually said with dark humor
- "Just leave it, it's not hurting anything" -- the rationalization that
  preserves boat anchors, which the metaphor exists to challenge
- "Rip it out" -- the aggressive remediation, treating boat-anchor
  removal as a physical act requiring force
- "Legacy" -- the euphemism that avoids the weight metaphor entirely,
  reframing dead code as inherited history rather than dead weight

## Origin Story

The term "boat anchor" for useless heavy equipment predates software.
It appears in military and amateur radio slang from at least the 1970s,
where a broken radio or oscilloscope too heavy to discard might literally
be described as "only good for a boat anchor." The joke is that the
equipment's only remaining virtue is its weight.

The term migrated into software engineering in the 1990s, appearing in
the anti-patterns literature alongside related concepts like dead code,
gold plating, and lava flow (hardened code from old, poorly understood
projects). William Brown, Raphael Malveau, and colleagues included it
in *AntiPatterns: Refactoring Software, Architectures, and Projects in
Crisis* (1998), helping formalize it as a recognized anti-pattern.

## References

- Brown, W. J., Malveau, R. C., McCormick, H. W. & Mowbray, T. J.
  *AntiPatterns: Refactoring Software, Architectures, and Projects in
  Crisis*, Wiley (1998) -- formalizes boat anchor as a software
  anti-pattern
- Raymond, E. S. *The New Hacker's Dictionary* (1996) -- documents the
  broader hacker usage of "boat anchor" for any useless heavy equipment