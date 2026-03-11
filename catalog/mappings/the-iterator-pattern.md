---
slug: the-iterator-pattern
name: "The Iterator Pattern"
kind: dead-metaphor
source_frame: social-roles
target_frame: object-oriented-design
categories:
  - software-engineering
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related: []
---

## What It Brings

An iterator, etymologically, is "one who goes" (Latin *iter*, journey).
The word once evoked a traveler moving through a landscape, visiting
each location in turn. The GoF Iterator pattern maps this onto
collection traversal: an iterator moves through a data structure,
visiting each element without exposing the structure's internals.
Today, most developers use iterators without thinking about journeys
at all — the metaphor has fossilized.

Key structural parallels (when the metaphor was alive):

- **The iterator travels through the collection** — like a traveler
  visiting towns along a road, the iterator moves from element to
  element. The journey metaphor made sequential access feel like
  physical movement.
- **The iterator maintains position** — a traveler knows where they
  are. The iterator tracks its current position in the collection. The
  metaphor of location mapped onto array indices and node pointers.
- **The iterator doesn't own the territory** — a traveler passing
  through doesn't own the towns. The iterator accesses elements without
  copying or controlling the collection. The metaphor distinguished
  traversal from ownership.
- **Multiple iterators can traverse independently** — two travelers can
  be at different points on the same road. Multiple iterators over the
  same collection maintain separate positions. The journey metaphor
  made this independence intuitive.
- **The iterator knows only "next"** — a traveler on a road knows
  "forward," not the whole map. Forward-only iterators embody this:
  they can advance but can't jump or backtrack. The metaphor
  naturalized the limitation.

## Where It Breaks

The Iterator pattern's metaphor broke long before most developers
encountered it. The word "iterator" has become a pure technical term,
as divorced from its Latin roots as "computer" is from "one who
computes." But examining the original metaphor reveals its limits:

- **Travelers are embodied; iterators are abstract** — a traveler
  occupies space, gets tired, needs food. An iterator is a position
  variable plus a next() method. The journey metaphor imports
  physicality that doesn't exist.
- **Journeys are irreversible by default; iteration can reset** —
  you can't easily un-travel a road. Most iterators can be reset or
  recreated trivially. The metaphor suggests commitment that isn't
  there.
- **Travelers have agency; iterators are controlled externally** — a
  traveler decides when to move. An iterator's next() is called by
  client code. The metaphor anthropomorphizes a passive data structure.
- **The landscape metaphor hides the structure** — the iterator pattern
  specifically exists to hide collection internals. But the journey
  metaphor suggests a landscape that could be perceived differently —
  as a map, from above, all at once. The metaphor tensions against the
  pattern's core purpose.

The real evidence of metaphor death: developers now use "iterate" as
a transitive verb meaning "process sequentially" ("iterate the array")
with no sense that anyone is traveling anywhere. The word has been
fully absorbed into technical vocabulary.

## Expressions

These expressions persist, but few developers consciously invoke the
journey metaphor:

- "Iterate over the collection" — traversal as movement, though the
  spatial sense has faded
- "The iterator is exhausted" — end of journey, though "exhausted"
  now just means "no more elements"
- "Cursor" — the database equivalent, retaining the spatial metaphor
  of a position marker
- "next()" — the fundamental operation, movement reduced to a method
  name
- "Iterator invalidation" — when modification breaks traversal, like
  a road destroyed mid-journey
- "Lazy iteration" — visiting elements only when needed, though "lazy"
  no longer suggests a leisurely traveler

## Origin Story

Iteration as a concept predates the GoF pattern. The word entered
computing through FORTRAN's DO loops and COBOL's PERFORM statements
in the 1950s, already technical. The object-oriented Iterator pattern
crystallized in Smalltalk's collection classes, which provided
do: blocks for traversal. By the time Gamma et al. formalized the
pattern in 1994, "iterator" was standard vocabulary. The metaphorical
origin in journeys and travelers had been dead for decades. The GoF
book doesn't even explain the etymology — it treats "iterator" as a
self-evident technical term, which by then it was.

## References

- Gamma, E. et al. *Design Patterns: Elements of Reusable Object-
  Oriented Software* (1994), Chapter 5: Behavioral Patterns
- Goldberg, A. & Robson, D. *Smalltalk-80: The Language and Its
  Implementation* (1983) — early iterator implementations
- Latin *iterāre*, "to journey" — the forgotten root
