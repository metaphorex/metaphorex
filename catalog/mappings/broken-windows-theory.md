---
slug: broken-windows-theory
name: "Broken Windows Theory"
kind: conceptual-metaphor
source_frame: architecture-and-building
target_frame: software-programs
categories:
  - software-engineering
  - organizational-behavior
author: agent:metaphorex-miner
contributors: []
related: []
---

## What It Brings

A broken window left unrepaired signals that nobody cares, inviting
further vandalism and accelerating neighborhood decline. The metaphor
maps visible physical disorder onto visible code disorder: dead code,
inconsistent naming, missing tests, and suppressed warnings all function
as broken windows in a codebase. The structural insight is that decay is
self-reinforcing through a signaling mechanism.

- **Disorder as signal** -- the core mapping. A broken window is not
  dangerous in itself; it is dangerous because it communicates permission.
  It tells the next person that standards are not enforced here. In a
  codebase, a function with no tests, a TODO comment from three years ago,
  or a suppressed linter warning sends the same signal: this is a place
  where shortcuts are tolerated. The next developer who encounters it
  feels licensed to cut their own corner. The mechanism is social and
  perceptual, not technical -- the window does not cause the next act of
  vandalism, it lowers the psychological cost of committing one.
- **Entropy cascade** -- one broken window leads to two, two lead to a
  dozen, and eventually the whole structure is abandoned. In software,
  this manifests as the codebase that "nobody wants to touch." Once
  enough disorder accumulates, each new contributor inherits a signal
  environment that says maintenance is futile. The cascade is not linear;
  it accelerates as the ratio of signal-to-disorder tips past a threshold.
  Teams describe this as the codebase "going bad," as if decay were
  organic rather than social.
- **The repair-first intervention** -- the theory prescribes immediate
  repair of small disorders to prevent escalation. In software, this
  maps to the Boy Scout Rule ("leave the code better than you found it"),
  aggressive linting, zero-warning policies, and refactoring sprints.
  The prescription works because it operates on the signal, not the
  substance: fixing a trivial naming inconsistency does not improve
  performance, but it communicates that someone is watching and standards
  are enforced.

## Where It Breaks

- **The criminology original is deeply contested** -- Wilson and Kelling's
  1982 theory was used to justify aggressive policing strategies (New York
  City's "zero tolerance" era under Giuliani and Bratton) that
  disproportionately targeted minority communities. Subsequent empirical
  research has found weak or no causal link between disorder and serious
  crime. The software community borrowed the theory at the height of its
  political popularity and has largely ignored its empirical collapse.
  Using "broken windows" in a software context inadvertently endorses a
  framework whose real-world application caused documented harm.
- **The metaphor conflates aesthetic disorder with structural failure** --
  a broken window is cosmetic damage; it does not compromise the
  building's structural integrity. But in software, the "broken windows"
  people point to -- missing tests, unhandled errors, race conditions --
  are often genuinely dangerous, not merely ugly. The metaphor frames
  structural defects as signaling problems, suggesting that their primary
  harm is psychological (lowering standards) rather than technical
  (causing failures). This can lead to prioritizing visible tidiness
  over invisible correctness.
- **Signal-based reasoning assumes observers** -- the broken window
  mechanism requires someone to see the window and update their behavior.
  In a solo developer's codebase, or in a rarely-modified module, the
  signaling mechanism has no audience. Dead code in a library that nobody
  reads does not cascade into further disorder because there is nobody to
  receive the signal. The theory is implicitly about teams, not code.
- **"Zero tolerance" in codebases has its own pathologies** -- the
  prescribed intervention (fix every small disorder immediately) can
  produce obsessive refactoring, bikeshedding over style, and a culture
  where cosmetic consistency is valued above functional progress. Teams
  that treat every linter warning as a broken window may spend more time
  polishing than building. The theory offers no framework for
  distinguishing between disorders that genuinely cascade and disorders
  that are inert.

## Expressions

- "Don't leave broken windows" -- the standard admonition in code review,
  usually meaning: fix the small thing now, don't leave it for later
- "The Boy Scout Rule" -- a closely related principle: leave the campsite
  (codebase) cleaner than you found it, often cited alongside broken
  windows theory
- "Code rot" -- the observed phenomenon that broken windows theory
  attempts to explain: codebases deteriorate over time even without
  external damage
- "Tech debt entropy" -- the accumulated disorder that signals abandonment,
  framed as a financial-thermodynamic hybrid metaphor
- "Zero-warning policy" -- the organizational intervention derived from
  the theory: treat every compiler or linter warning as a broken window
  to be fixed immediately

## Origin Story

James Q. Wilson and George L. Kelling introduced broken windows theory
in a 1982 Atlantic Monthly article, arguing that visible disorder in
urban environments signals social neglect and invites escalating criminal
behavior. The theory was enormously influential in criminology and
policing throughout the 1990s, particularly in New York City.

The software adaptation appeared in Andrew Hunt and David Thomas's
The Pragmatic Programmer (1999), which explicitly cited Wilson and
Kelling and proposed that codebases follow the same entropy dynamics
as neighborhoods. The metaphor resonated powerfully with developers
who had observed the phenomenon empirically -- that codebases with
visible neglect deteriorate faster than codebases that are actively
maintained -- and it became a standard reference in software craftsmanship
discussions.

The irony is that broken windows theory entered software discourse just
as criminologists were beginning to challenge its empirical foundations.
The software community adopted the metaphor as established social science;
the social science community was in the process of questioning whether
it was true.

## References

- Wilson, J.Q. & Kelling, G.L. "Broken Windows," *The Atlantic Monthly*,
  March 1982 -- the original criminology article
- Hunt, A. & Thomas, D. *The Pragmatic Programmer*, Addison-Wesley,
  1999 -- the migration to software engineering
- Harcourt, B.E. & Ludwig, J. "Broken Windows: New Evidence from New
  York City and a Five-City Social Experiment," *University of Chicago
  Law Review* 73(1), 2006 -- empirical challenge to the original theory
