---
slug: spaghetti-code
name: "Spaghetti Code"
kind: dead-metaphor
source_frame: food-and-cooking
target_frame: software-programs
categories:
  - software-engineering
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - data-flow-is-fluid-flow
  - program-failure-is-bodily-failure
---

## What It Brings

Tangled pasta maps onto tangled control flow. The metaphor is instantly
legible to anyone who has pulled a forkful of spaghetti from a plate and
watched half the dish follow: you cannot extract one strand without
dragging everything else with it. This is precisely the experience of
reading code with unstructured jumps, deeply nested conditionals, and
invisible dependencies.

Key structural parallels:

- **Entanglement as topology** -- spaghetti's defining property is that
  individual strands are indistinguishable and intertwined. In code, this
  maps to control flow that cannot be traced linearly: goto statements,
  deeply nested callbacks, circular dependencies. You cannot follow one
  thread of execution without encountering every other thread.
- **Resistance to decomposition** -- you cannot neatly separate one
  strand from the mass. Similarly, spaghetti code resists refactoring
  because every function is coupled to every other function. Extracting a
  module means untangling the entire plate.
- **A food-metaphor family** -- the metaphor spawned a taxonomy. Lasagna
  code has too many layers (excessive abstraction). Ravioli code is
  well-encapsulated (small, self-contained units). Baklava code has
  excessive thin layers. The pasta metaphor became a design vocabulary,
  with different dishes encoding different structural pathologies or
  virtues.
- **Visceral disgust** -- the metaphor carries affect. "Spaghetti code"
  isn't neutral; it conveys revulsion. The mess is not just hard to work
  with, it is aesthetically offensive. This emotional loading does real
  work: it motivates refactoring and signals social disapproval of
  unstructured programming.

## Where It Breaks

- **Spaghetti is homogeneous; code is not** -- every strand of spaghetti
  is the same. Real tangled code has heterogeneous components: database
  queries interleaved with UI logic, business rules embedded in
  infrastructure. The metaphor suggests uniform messiness, but real
  spaghetti code is messy in specific, structured ways that the pasta
  image obscures.
- **Spaghetti has no semantics** -- a strand of pasta doesn't *mean*
  anything. A line of code does. The metaphor captures structural
  entanglement but misses semantic entanglement: the problem isn't just
  that things are tangled, it's that the *meanings* are tangled. A
  function called `calculatePrice` that also sends emails and updates a
  cache is spaghetti not because of control flow but because of semantic
  incoherence.
- **The metaphor blames the code, not the conditions** -- spaghetti code
  is often produced by reasonable people under unreasonable constraints:
  deadline pressure, changing requirements, accumulated patches. Calling
  it spaghetti implies carelessness or incompetence, when it's often the
  rational output of an irrational process. The metaphor moralizes a
  systemic problem.
- **Not all entanglement is bad** -- tightly coupled systems sometimes
  perform better than loosely coupled ones. The metaphor assumes that
  separation is always virtuous, but some "spaghetti" is just dense,
  efficient code that trades readability for performance. The metaphor
  has no vocabulary for justified entanglement.

## Expressions

- "This codebase is pure spaghetti" -- the canonical developer
  complaint, usually uttered while reading someone else's code
- "Spaghetti architecture" -- extending the metaphor from code to system
  design, where services are tangled rather than lines
- "Lasagna code" -- too many layers of abstraction, each thin and
  adding indirection without value
- "Ravioli code" -- the positive inversion: small, self-contained,
  well-encapsulated units, each with its own filling
- "Untangling the spaghetti" -- refactoring as separating individual
  strands, implying patience and care
- "Who wrote this spaghetti?" -- the rhetorical question that is really
  an accusation, often answered by `git blame`

## Origin Story

The term appears in print as early as 1978 in the proceedings of the ACM,
though it was certainly in oral use before that. It emerged alongside the
structured programming movement of the 1960s and 1970s, when Dijkstra's
"Go To Statement Considered Harmful" (1968) gave the programming
community a villain (the goto) and the spaghetti metaphor gave them a
name for the crime scene. The metaphor was a rhetorical weapon in the
structured programming wars: if your code uses gotos, it's *spaghetti*,
and spaghetti is disgusting.

The food-family extensions (lasagna, ravioli, baklava) emerged later in
blog posts and conference talks, as developers realized that structure
itself could be pathological -- you could have too much of it, not just
too little.

## References

- Dijkstra, E.W. "Go To Statement Considered Harmful," *Communications
  of the ACM* 11:3 (1968) -- the polemic that made spaghetti code a
  recognizable sin
- Steele, G.L. "Debunking the 'Expensive Procedure Call' Myth,"
  *Proceedings of the ACM* (1977) -- early usage of pasta-architecture
  metaphors in computing discourse
