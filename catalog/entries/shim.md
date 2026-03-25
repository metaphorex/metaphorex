---
applies_to:
- software-programs
author: agent:metaphorex-miner
categories:
- software-engineering
- computer-science
contributors: []
created: '2026-03-21'
grounding: established
harness: Claude Code
kind: metaphor
name: Shim
summary: "A thin wedge absorbing the mismatch between two surfaces not built to fit. Minimum material for maximum alignment; stacking signals deeper problems."
provenance: carpentry-woodworking
related:
- scaffolding
- jig
slug: shim
source_frame: carpentry
updated: '2026-03-21'
transfers:
  - '[source] a shim is a thin, precisely sized piece of material inserted into a gap between two surfaces that were not manufactured to fit each other -- it adapts without altering either surface'
  - '[source] shims are selected or trimmed to the exact dimension of the mismatch, doing the minimum necessary to achieve alignment -- a shim that is too thick creates a new misalignment'
  - '[source] shims are secondary to the joint they serve: they carry no structural load themselves but enable load-bearing contact between the primary members'
limits:
  - '[source] breaks because a physical shim is passive and inert, while a software shim actively translates calls, transforms data, and can introduce its own bugs -- the metaphor hides the computational complexity behind a word that implies a dumb wedge'
  - '[source] misleads by implying the mismatch is a manufacturing defect, when in software the "gap" is often a deliberate design difference between two systems built for different purposes at different times'
---

## Transfers

In carpentry, a shim is a thin wedge -- often a tapered piece of cedar or
plastic -- driven into a gap between two surfaces to bring them into
alignment. When hanging a door, the carpenter shims the frame to plumb
even though the rough opening is not square. The shim does not replace the
frame or the wall; it occupies the precise space between them.

Key structural parallels:

- **Gap-filling without alteration** -- a shim does not modify either
  surface it contacts. It sits between them, absorbing the mismatch.
  In software, a shim (or polyfill, or adapter) sits between two
  interfaces that were not designed to fit each other and translates
  between them without requiring changes to either side. The Windows
  Application Compatibility Toolkit literally ships "shim" layers that
  intercept API calls from legacy applications and translate them for
  modern Windows. The structural parallel is precise: the shim adapts
  the relationship, not the components.
- **Minimum material for maximum alignment** -- a good shim is the
  thinnest piece that closes the gap. A shim thicker than the gap
  creates a new problem. In software, the principle maps to the ideal
  compatibility layer: it should do the minimum transformation necessary.
  A shim that grows in scope -- adding logging, caching, business logic
  -- has become something else (a middleware layer, a service), and the
  metaphor no longer applies. When engineers say "it's just a shim," they
  invoke this minimality constraint.
- **Disposable by intention** -- shims are meant to be temporary in many
  contexts. A construction shim is often removed once concrete sets or
  fasteners are tightened. In software, shims are ideally removed when
  the upstream interface is fixed or the legacy system is retired. The
  metaphor encodes a temporal expectation: shims should not become
  permanent architecture.
- **Stacking as a warning sign** -- in carpentry, needing multiple shims
  stacked together signals that the underlying framing is badly off and
  needs structural correction, not more shimming. In software, layered
  compatibility shims (a shim wrapping a shim wrapping a shim) signal
  accumulated technical debt where the real fix is to redesign the
  interface. The metaphor correctly predicts the failure mode.

## Limits

- **Software shims are computationally active, not inert** -- a wooden
  shim sits passively in a gap. A software shim executes code: it
  intercepts calls, transforms arguments, converts data formats, and
  returns modified responses. This active translation can introduce
  latency, bugs, and security vulnerabilities. The carpentry metaphor
  makes this complexity invisible by suggesting the shim is "just a thin
  piece wedged in," which leads to under-engineering and under-testing of
  compatibility layers that are actually critical code paths.
- **The "gap" in software is often intentional** -- in carpentry, the gap
  between frame and wall is an imperfection to be corrected. In software,
  two systems often have different interfaces because they were designed
  for different purposes, by different teams, at different times. The
  mismatch is not a defect but a consequence of independent design
  decisions. Calling the compatibility layer a "shim" frames it as
  fixing an error, when it is often accommodating legitimate diversity.
  This framing can lead to pressure to "eliminate the shim" by
  standardizing interfaces, which may be neither possible nor desirable.
- **Shims imply the problem is at the boundary** -- a physical shim
  addresses a surface-level gap. But many software compatibility problems
  are not at the interface boundary; they are semantic mismatches deep
  in the data model or behavioral assumptions. A shim that translates
  API calls but does not reconcile different transactional semantics
  gives a false sense of compatibility. The thinness metaphor encourages
  shallow fixes to deep problems.
- **The "temporary" expectation is almost always violated** -- in
  practice, software shims persist for years or decades. The Windows
  compatibility shim database contains thousands of entries, many dating
  back to Windows 95 era applications. Calling something a shim creates
  an expectation of removal that the organizational and economic reality
  rarely supports.

## Expressions

- "It's just a shim" -- minimizing the complexity of a compatibility
  layer, invoking the carpentry sense of a thin, simple insert
- "Shim layer" -- an explicit architectural term for a thin compatibility
  adapter between two systems
- "Polyfill" -- web development term for a JavaScript shim that provides
  modern browser APIs in older browsers (coined by Remy Sharp, 2009)
- "We'll shim it for now" -- declaring a compatibility fix as temporary,
  with the implication of a future proper solution
- "Shim hell" -- accumulated layers of compatibility adapters that have
  become load-bearing and unmaintainable
- "API shim" -- a translation layer between two versions of the same
  interface, common during deprecation periods

## Origin Story

The word "shim" in carpentry dates to at least the early 18th century,
likely from a dialectal English or Germanic root meaning "thin strip."
Its adoption into computing appears to have occurred organically in the
1990s as operating system vendors -- particularly Microsoft -- needed
vocabulary for the compatibility layers they were building to support
legacy applications on new platforms. Microsoft's Application
Compatibility Toolkit formalized the term, using "shim" as the official
name for interceptor DLLs that modify API behavior for specific
applications. The web development community adopted "polyfill" (Remy
Sharp, 2009) as a domain-specific synonym, explicitly referencing the
building trade product Polyfilla used to fill cracks in walls -- a
parallel metaphor from the same source domain.

## References

- Microsoft. "Understanding Shims," Application Compatibility Toolkit
  documentation
- Sharp, Remy. "What is a Polyfill?" (2010) -- origin of the polyfill
  term and its relationship to the shim concept
- Pye, David. *The Nature and Art of Workmanship* (1968) -- context for
  the carpentry source domain
