---
applies_to:
- software-programs
author: agent:metaphorex-miner
categories:
- software-engineering
contributors: []
created: '2026-03-21'
grounding: folk
harness: Claude Code
kind: metaphor
name: Jig
summary: "A custom guide that encodes a decision once so the operator never re-decides. Tooling quality bounds product quality."
provenance: carpentry-woodworking
related:
- shim
- scaffolding
slug: jig
source_frame: carpentry
updated: '2026-03-21'
transfers:
  - '[source] a jig is a custom-built guide that constrains a tool''s movement to produce identical results on every repetition -- it encodes a decision once so the operator does not re-decide each time'
  - '[source] building a good jig often requires as much skill and time as the product it helps produce, because the jig must anticipate every variation in the raw material'
  - '[source] the jig is not part of the finished product -- it stays in the shop while the workpiece ships, invisible to the end user'
limits:
  - '[source] breaks because a physical jig constrains movement along fixed physical dimensions, while a software test harness or build script constrains behavior through logic that can itself contain bugs -- the metaphor hides the fact that the "guide" needs its own verification'
  - '[source] misleads by implying the jig is stable once built, when software tooling requires continuous maintenance as the codebase it serves evolves -- a wooden jig does not need updating when the wood species changes'
---

## Transfers

A jig is a custom device that holds a workpiece or guides a tool to ensure
repeatable, accurate results. A dovetail jig clamps to a board and guides
the router bit at the precise angle and spacing needed for the joint. A
crosscut sled on a table saw holds stock square to the blade. The jig
does not cut; it constrains the cut.

Key structural parallels:

- **Encoding a decision into a device** -- when a carpenter builds a jig,
  they are taking a complex decision (angle, spacing, depth, sequence)
  and embedding it in a physical object so that future operations do not
  require re-deciding. In software, test harnesses, build scripts, CI
  pipelines, and code generators serve the same function: they encode
  decisions about how to build, test, or deploy so that individual
  developers do not re-decide each time. The parallel is structural,
  not cosmetic. A Makefile is a jig: it constrains the build so that
  "make release" produces the same artifact regardless of who runs it.
- **Craftsmanship in the tooling** -- experienced woodworkers spend
  significant time building jigs, sometimes more time than on the
  workpieces themselves. A poorly made jig produces poor work at scale,
  which is worse than poor work on a single piece. In software, the same
  dynamic applies: a test harness that is flaky, a CI pipeline that is
  fragile, or a code generator that produces subtly incorrect output
  multiplies errors across every use. The metaphor correctly encodes the
  insight that tooling quality bounds product quality.
- **Invisible to the customer** -- the jig stays in the workshop. The
  customer sees the dovetail joint, not the dovetail jig. In software,
  build systems, test frameworks, deployment scripts, and development
  environments are invisible to the end user. They are pure production
  infrastructure. The metaphor captures the economic tension this
  creates: investment in tooling is hard to justify to stakeholders who
  only see the product, yet the tooling determines whether the product
  can be produced reliably.
- **Shop-specific, not universal** -- a jig is built for a specific
  workshop's tools, a specific project's dimensions, and a specific
  woodworker's workflow. It rarely transfers cleanly to another shop.
  In software, internal tooling is similarly specific: a company's
  deployment scripts assume its infrastructure, its testing framework
  assumes its architecture, its code generators assume its conventions.
  "Just use our jig" is as problematic in software as in woodworking.

## Limits

- **A wooden jig is mechanically verifiable; a software jig is not** --
  you can measure a physical jig with calipers and confirm its accuracy
  before using it. A software test harness or build script is itself a
  program that can contain logic errors, race conditions, and
  environmental dependencies. The metaphor encourages trust in tooling
  ("we have a jig for that") without encoding the need to test the
  tooling itself. In practice, untested test infrastructure is a common
  source of false confidence.
- **Physical jigs are stable; software jigs require maintenance** -- a
  dovetail jig built from Baltic birch plywood will work for decades
  without modification. A software build script must be updated when
  dependencies change, when the language runtime is upgraded, when the
  deployment target changes, and when new team members need to use it.
  The metaphor's implication of build-once-use-forever understates the
  ongoing cost of software tooling, which is often the dominant
  maintenance burden in mature codebases.
- **The jig metaphor hides the abstraction layer** -- a physical jig
  operates on the same level of reality as the workpiece: both are
  physical objects in three-dimensional space. A software "jig" often
  operates at a different level of abstraction than the code it tests
  or builds (mocking, virtualization, containerization). The gap between
  the jig's model of the system and the system's actual behavior is a
  source of subtle bugs that has no carpentry analog.
- **Jigs imply batch production** -- the economic case for building a
  carpentry jig is that you are making many identical cuts. In software,
  some "jigs" (CI pipelines, test suites) are used continuously, but
  others (one-off migration scripts, scaffolding generators) may be used
  once. Calling a one-use script a "jig" borrows the connotation of
  repeatability without the substance.

## Expressions

- "Test harness" -- the most common software equivalent of a jig:
  infrastructure that holds code under test and constrains how tests
  are executed
- "Build jig" -- informal term for a build system or script that
  produces consistent outputs from consistent inputs
- "We need a jig for that" -- expressing the need for repeatable tooling
  before attempting manual repetition
- "Scaffolding code" -- sometimes used interchangeably with jig, though
  scaffolding implies temporary structure while jig implies permanent
  tooling
- "The fixture" -- in both testing (test fixtures) and woodworking
  (workholding fixtures), the same word describes apparatus that holds
  the subject in position during work
- "Tooling debt" -- the accumulated cost of undermaintained jigs in a
  software project

## Origin Story

"Jig" in the woodworking sense dates to the 16th century, with the
broader meaning of "a device that holds something in place." The term
entered software engineering informally, never through a single coinage
but through the natural vocabulary of engineers who also worked with
their hands or recognized the structural parallel. Its use remains more
colloquial than formal -- "test harness" and "fixture" are the standard
terms in software testing literature -- but the jig metaphor persists
in workshop-culture engineering teams and in writing about craft-oriented
software development (see Matthew Crawford's *Shop Class as Soulcraft*,
2009, and Richard Sennett's *The Craftsman*, 2008).

## References

- Pye, David. *The Nature and Art of Workmanship* (1968) -- jigs as
  the mechanism that converts workmanship of risk into workmanship of
  certainty
- Sennett, Richard. *The Craftsman* (2008) -- the role of tooling in
  skilled practice
- Crawford, Matthew. *Shop Class as Soulcraft* (2009) -- carpentry as
  a model for engaged, embodied work
