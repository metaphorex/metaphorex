---
author: agent:metaphorex-miner
categories:
- software-engineering
contributors:
- fshot
harness: Claude Code
kind: archetype
name: The Visitor Pattern
related:
- the-observer-pattern
- the-strategy-pattern
slug: the-visitor-pattern
source_frame: social-roles
target_frame: object-oriented-design
---

## What It Brings

A visitor is someone who arrives from outside. They come to your house,
your hospital room, your office -- and they bring capabilities the
residents lack. A plumber visits to fix the pipes. A doctor visits to
examine the patient. The GoF Visitor pattern maps this social
transaction onto software: an external object traverses a data structure,
performing operations at each node without the nodes needing to know how
to perform those operations themselves.

Key structural parallels:

- **The visitor brings the skill; the host provides access** -- when a
  home inspector visits, you open doors and the inspector evaluates.
  In the pattern, the element exposes its structure via an `accept`
  method, and the visitor carries the operation logic. This division
  of responsibility is the pattern's defining insight: operations live
  outside the structures they operate on.
- **Different visitors do different things in the same rooms** -- a
  real estate appraiser and an electrician walk the same house but see
  different things. Multiple visitor implementations traverse the same
  object structure with entirely different behaviors. The metaphor
  makes this multiplicity feel natural -- of course different guests
  have different purposes.
- **Visiting follows protocol** -- you knock, the host answers, you
  are received. Double dispatch in the Visitor pattern mirrors this
  social protocol: the client calls `accept(visitor)`, the element
  calls `visitor.visit(this)`. The handshake is rigid but necessary.
  The metaphor frames this as etiquette, not bureaucracy.
- **Visitors are temporary; residents are permanent** -- the guest
  leaves. The structure persists. Visitors don't modify the class
  hierarchy; they add behavior transiently. The metaphor captures
  this ephemerality: the visit changes what happens, not what exists.
- **The host structure determines the route** -- a visitor to a
  museum follows the floor plan. The composite object structure
  determines traversal order. The metaphor naturalizes the idea
  that the data structure, not the operation, controls navigation.

## Where It Breaks

- **Real visitors choose where to go; software visitors are dragged
  through every room** -- a house guest can decline the basement
  tour. A Visitor object's `visit` method is called on every element
  in the structure. The pattern turns a social visit into a forced
  march. The metaphor implies selectivity where the implementation
  enforces exhaustiveness.
- **Adding a new room breaks every visitor** -- if you add a wing to
  your house, existing guests can still visit. But adding a new
  element type to the object structure requires updating every visitor
  class with a new `visit` overload. The metaphor of hospitality
  suggests graceful accommodation; the pattern demands rigid
  foreknowledge of every element type.
- **The double-dispatch protocol has no social analogue** -- the
  knock-answer-enter sequence of a real visit is simple. Double
  dispatch -- where the call bounces from `accept` to `visit` and
  back -- is a mechanical indirection that the social metaphor
  doesn't prepare you for. Developers encountering the Visitor
  pattern for the first time find the back-and-forth confusing
  precisely because visiting someone is straightforward and this is
  not.
- **Visitors in life don't need to know the floor plan in advance**
  -- you can visit a house you've never seen. A Visitor class must
  declare overloads for every concrete element type at compile time.
  The metaphor suggests improvisation; the pattern requires complete
  structural knowledge.
- **The power dynamic is reversed** -- in social visiting, the host
  controls the experience. In the pattern, the visitor carries all
  the interesting logic. The host's `accept` method is a hollow
  formality -- one line of code that just calls back. The metaphor
  puts the host in charge; the pattern puts the visitor in charge.

## Expressions

- "Accept a visitor" -- the host's side of the protocol, opening the
  door to the external operation
- "Visit each node" -- traversal as a social call, stopping at every
  element in the structure
- "Double dispatch" -- the handshake protocol, two method calls that
  resolve the right operation for the right element
- "Adding a new visitor" -- extending behavior without modifying the
  structure, the ease of inviting a new guest
- "The visitor walks the tree" -- traversal as physical movement
  through a spatial structure

## Origin Story

The Visitor pattern was codified in *Design Patterns* (1994) by the
Gang of Four. It was born from the frustration of needing to add
operations to complex object structures (particularly abstract syntax
trees in compilers) without modifying the element classes. The social
metaphor of visiting was chosen to emphasize that the operation comes
from outside the structure -- a guest, not a resident. The pattern is
notoriously difficult to understand on first encounter, in part because
the double-dispatch mechanism doesn't map cleanly onto the simplicity
of the visiting metaphor. It remains one of the most debated GoF
patterns, with many developers preferring pattern matching or
multimethods where available.

## References

- Gamma, E. et al. *Design Patterns: Elements of Reusable Object-
  Oriented Software* (1994), Chapter 5: Behavioral Patterns
- Palsberg, J. & Jay, C.B. "The Essence of the Visitor Pattern"
  (1998) -- formal analysis of the pattern's type-theoretic structure
- Buchlovsky, P. & Thielecke, H. "A Type-Theoretic Reconstruction of
  the Visitor Pattern" (2005)