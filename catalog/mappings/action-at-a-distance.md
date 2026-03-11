---
slug: action-at-a-distance
name: "Action at a Distance"
kind: conceptual-metaphor
source_frame: physics
target_frame: software-programs
categories:
  - software-engineering
  - systems-thinking
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - heisenbug
  - spaghetti-code
  - god-object
---

## What It Brings

Einstein called quantum entanglement "spooky action at a distance" --
the idea that measuring a particle here could instantaneously affect a
particle there, with no visible connection between them. The phrase
captured his discomfort with a universe that violated locality: the
principle that effects should be traceable to nearby causes.

In programming, action at a distance names the same violation: you change
something here and something breaks over there, with no visible causal
chain connecting them. The metaphor imports the physicist's expectation of
locality into software design and names the specific way that expectation
is violated.

Key structural parallels:

- **Non-local causation** -- in physics, action at a distance means a
  force operates without a medium, across empty space. In code, it means
  a modification in one module causes a behavior change in a distant,
  seemingly unrelated module. The cause and effect are separated by layers
  of abstraction, and no reading of the local code explains what happened.
  The developer must search outward, sometimes across the entire codebase,
  to find the connection.
- **Hidden coupling** -- quantum entanglement creates a correlation
  between particles that is invisible to any observation of the individual
  particles. Global state, shared mutability, and implicit dependencies
  create the same invisible correlation in software. Two modules that
  appear independent are secretly coupled through a global variable, a
  database row, a shared file, or an event bus. The coupling is real but
  invisible to the reader of either module in isolation.
- **Spookiness as epistemic failure** -- Einstein used "spooky" because
  action at a distance violated his model of how the universe should work.
  Developers use the same word for the same reason: action at a distance
  in code feels uncanny because it violates the mental model of modular,
  local causation that good software design is supposed to provide. The
  spookiness is not in the code itself but in the gap between the
  developer's expectations and the code's actual behavior.
- **The measurement problem** -- in quantum mechanics, the act of
  observing a system changes it. In code with action-at-a-distance bugs,
  adding logging or debugging instrumentation can change the timing or
  state enough to mask or alter the bug. This parallel to the Heisenbug
  is not accidental: both metaphors draw on physics to name the
  frustration of systems that behave differently when you try to observe
  them.

## Where It Breaks

- **Quantum non-locality is fundamental; software non-locality is a bug**
  -- action at a distance in physics is a real property of the universe,
  not a design flaw. In software, it is always a design flaw or an
  unintended consequence. The metaphor borrows gravity from physics (this
  is deep and real) but applies it to something that is merely poorly
  engineered. This can make action-at-a-distance bugs feel more
  mysterious and intractable than they actually are.
- **The physics metaphor implies no medium; the software reality has one**
  -- quantum entanglement genuinely operates without a connecting medium.
  Software action at a distance always has a mechanism: a global variable,
  a shared database, an event bus, a side effect. The "distance" is in the
  developer's perception, not in the system's structure. If you traced
  every pointer and every state mutation, the causal chain would be
  visible. The metaphor grants false mysteriousness to what is really just
  insufficient tracing.
- **Locality is not always desirable** -- the metaphor assumes that local
  causation is the correct default. But event-driven architectures,
  reactive programming, and observer patterns deliberately create non-local
  effects. Calling these "action at a distance" pathologizes a design
  choice that may be entirely appropriate. The metaphor does not
  distinguish between accidental and intentional non-locality.
- **The metaphor can discourage understanding** -- labeling a bug as
  "action at a distance" can become a stopping point rather than a
  starting point. The physics term names a fundamental mystery; applying it
  to code can suggest the bug is similarly irreducible, when in fact it
  has a concrete, discoverable cause. The metaphor can license giving up.

## Expressions

- "That's action at a distance" -- the diagnosis, applied when a change
  in one module causes an unexpected failure in another
- "Spooky action at a distance" -- the full Einstein quote, deployed for
  emphasis when the coupling is particularly hidden and surprising
- "Who's mutating this from over there?" -- the detective question that
  follows the diagnosis, the search for the hidden coupling
- "Side effects at a distance" -- variant emphasizing that the mechanism
  is typically an uncontrolled side effect rather than an explicit
  dependency
- "This global is causing action at a distance" -- the common resolution,
  identifying shared mutable state as the coupling mechanism

## Origin Story

The phrase originates with Newton, who was uncomfortable with his own
theory of gravity implying that masses attract each other across empty
space with no intervening medium. He called this "action at a distance"
and considered it philosophically unsatisfying. Einstein revived the
phrase in the 1930s and 1940s to criticize quantum entanglement, calling
it "spukhafte Fernwirkung" ("spooky action at a distance") in a 1947
letter to Max Born.

The term entered programming vocabulary through the broader cultural
absorption of quantum physics language. It appears in anti-pattern
catalogs, code review discussions, and linting rule descriptions (some
static analysis tools flag global variable mutations as "action at a
distance"). The metaphor was a natural fit for the programming community
because locality -- the principle that a function's behavior should
depend only on its inputs and local state -- is a core value of software
engineering, and violations of locality are among the most common sources
of bugs.

## References

- Einstein, A. letter to Max Born (1947) -- the "spukhafte Fernwirkung"
  phrase in its original context
- Wikipedia, "Action at a distance (computer programming)" -- overview
  of the anti-pattern with examples
- Hunt, A. & Thomas, D. *The Pragmatic Programmer* (1999) -- discusses
  coupling and the importance of locality in software design
- McConnell, S. *Code Complete*, 2nd ed. (2004) -- treats global
  variables and hidden dependencies as primary sources of defects
