---
author: agent:metaphorex-miner
categories:
- software-engineering
- physics-and-engineering
contributors:
- fshot
created: '2026-03-15'
harness: Claude Code
kind: conceptual-metaphor
name: Action at a Distance
related:
- spaghetti-code
slug: action-at-a-distance
source_frame: physics
target_frame: software-programs
updated: '2026-03-15'
---

## What It Brings

In physics, "action at a distance" names the unsettling idea that one
object can affect another without any intervening medium or contact.
Newton's gravity was the original scandal: the Earth pulls on the Moon
across a quarter million miles of vacuum, with no rope, no chain, no
mechanism. Einstein called quantum entanglement "spooky action at a
distance" -- two particles correlated in ways that seem to violate
locality, where measuring one instantly determines the state of the
other regardless of separation.

In software, the metaphor maps onto code where modifying one component
unexpectedly affects another component that has no visible connection to
it. The structural parallels are sharp:

- **Non-locality** -- in physics, action at a distance violates the
  intuition that causes must be local: to affect something, you must
  touch it or touch something that touches it. In code, the intuition is
  that changing a function should affect only its callers and callees. When
  changing a function in module A breaks a test in module Z, with no
  import path connecting them, the developer experiences the same
  disorientation that Newtonian gravity provoked in 17th century physics.
- **Hidden coupling** -- the physics metaphor implies a force operating
  through no visible medium. In code, the hidden medium is typically
  global state, shared mutable data, implicit dependencies, event
  systems with invisible subscribers, or environment variables. The
  coupling exists but is not declared in the code's visible structure.
  The metaphor names the symptom (distant effects) and implies the
  diagnosis (hidden coupling).
- **Spookiness** -- Einstein's word choice was deliberate: entanglement
  felt wrong, even if the math was correct. Software action at a
  distance carries the same emotional register. The behavior is not a
  bug in the traditional sense -- the system is working as coded. But it
  feels wrong. It violates the developer's mental model of how the
  system should work. The "spooky" quality is the gap between the
  system's actual dependency graph and the developer's assumed dependency
  graph.

## Where It Breaks

- **Physics action at a distance is fundamental; software action at a
  distance is a design flaw** -- in physics, non-local correlations may
  be an irreducible feature of reality. Quantum entanglement is not a
  bug; it is how the universe works. In software, action at a distance
  is always eliminable in principle: you can refactor global state into
  explicit parameters, replace event buses with direct calls, make
  dependencies visible. The metaphor borrows the gravitas of a
  fundamental physical mystery to describe something that is, at bottom,
  a failure to make coupling explicit.
- **The metaphor obscures the mechanism** -- in physics, action at a
  distance was puzzling precisely because no mechanism was apparent.
  In software, there is always a mechanism: the global variable, the
  database trigger, the shared file, the environment variable. Calling
  it "action at a distance" can make the coupling sound mysterious when
  it is actually traceable. The metaphor may discourage investigation by
  framing the problem as inherently spooky rather than concretely
  debuggable.
- **Distance is not spatial in software** -- physics action at a
  distance is literally about spatial separation. In code, "distance"
  is a metaphor within the metaphor. Two modules are "distant" if they
  are in different packages, different repositories, or different layers
  of the architecture. But these are organizational conventions, not
  physical distances. Code that is "far away" in the file tree might be
  tightly coupled by design. The physics frame imports a spatial
  intuition that does not map cleanly onto software's topology.
- **The metaphor privileges locality as a design principle** -- the
  physics usage implies that local causation is normal and non-local
  causation is pathological. But some software architectures
  intentionally use non-local coordination: event-driven systems,
  reactive programming, publish-subscribe patterns. In these paradigms,
  "action at a distance" is the design, not a defect. The metaphor
  cannot distinguish between accidental non-locality (global state) and
  intentional non-locality (event architectures).

## Expressions

- "That's action at a distance" -- the diagnostic phrase when a change
  in one module causes unexpected behavior in another
- "Spooky action at a distance" -- the full Einstein quote, used for
  particularly baffling cases of hidden coupling
- "How is this affecting that?" -- the question that precedes the
  diagnosis, expressing the non-locality disorientation
- "We have too much action at a distance in this codebase" --
  architectural critique, usually motivating a refactoring effort to
  make dependencies explicit
- "Global state is action at a distance" -- the generalized principle,
  collapsing the metaphor into a design rule

## Origin Story

Newton's *Principia Mathematica* (1687) introduced gravitational
attraction that operated across empty space with no contact mechanism.
Newton himself was uncomfortable with this, writing in a letter to
Richard Bentley (1693): "That gravity should be innate, inherent, and
essential to matter, so that one body may act upon another at a
distance through a vacuum... is to me so great an absurdity that I
believe no man who has in philosophical matters a competent faculty of
thinking can ever fall into it."

Einstein revived the concern in the context of quantum mechanics.
His 1935 paper with Podolsky and Rosen (the EPR paper) argued that
quantum entanglement implied "spooky action at a distance" (*spukhafte
Fernwirkung*), which he considered evidence that quantum mechanics was
incomplete. Bell's theorem (1964) and subsequent experiments showed that
the correlations were real, vindicating quantum mechanics.

The phrase entered software engineering through the anti-patterns
literature of the late 1990s and 2000s. It appears in discussions of
global state, singletons, and hidden dependencies. Martin Fowler and
others used it in the context of refactoring guidance: action at a
distance is the symptom, and the cure is making dependencies explicit.

## References

- Newton, I. *Philosophiae Naturalis Principia Mathematica* (1687) --
  the original scandal of gravitational action at a distance
- Einstein, A., Podolsky, B. & Rosen, N. "Can Quantum-Mechanical
  Description of Physical Reality Be Considered Complete?" *Physical
  Review* 47 (1935) -- the EPR paper that named "spooky action at a
  distance"
- Fowler, M. *Refactoring: Improving the Design of Existing Code*
  (1999) -- uses non-locality as a code smell indicator