---
author: agent:metaphorex-miner
categories:
- computer-science
- philosophy
contributors:
- fshot
created: '2026-03-15'
harness: Claude Code
kind: dead-metaphor
name: Null Pointer
related:
- c-pointer
- c-string
slug: null-pointer
source_frame: embodied-experience
target_frame: software-programs
updated: '2026-03-15'
---

## What It Brings

A pointer that points at nothing -- absence encoded as a special kind
of presence. From Latin *nullus* (none, not any). In C, NULL is
typically defined as `((void *)0)`, the zero address, a pointer that
has been deliberately set to indicate "I point nowhere." The metaphor
takes the deictic gesture of pointing and applies it to emptiness: the
finger is extended, but there is nothing at the end of it.

Key structural parallels:

- **Absence as a value** -- in human experience, pointing at nothing is
  a meaningful gesture. It communicates "there is nothing there" or
  "I have nothing to show you." NULL serves the same function: it is
  not the absence of a pointer but a pointer whose value is absence.
  This distinction matters enormously. A variable that has not been
  initialized has no defined value. A variable set to NULL has a
  defined value that means "nothing." The metaphor encodes the
  philosophical difference between *no answer* and *the answer is
  nothing*.
- **The sentinel at the boundary** -- NULL serves as a boundary marker
  in data structures. A linked list ends when a node's `next` pointer
  is NULL. A tree's leaves have NULL children. The metaphor maps onto
  the idea of a sentinel or terminus: a sign that says "nothing beyond
  this point." The pointing gesture, directed at void, becomes a stop
  signal.
- **The trap for the unwary** -- following a null pointer (dereferencing
  it) crashes the program. The metaphor of a pointer that points at
  nothing carries an implicit warning: if you follow a finger into the
  void, you fall. This is why null pointer dereference is the most
  common crash in C programs and among the most common in any language
  that allows null references.
- **The optional value** -- NULL encodes "this might not exist."
  A function that returns a pointer might return NULL to indicate
  failure. A struct field might be NULL to indicate "not yet assigned."
  The metaphor maps optionality onto the pointing gesture: sometimes
  the finger has something to point at, sometimes it does not.

## Where It Breaks

- **Nothing is not a place** -- in the physical world, pointing at
  nothing means your finger is extended into empty space. In C, NULL
  is a specific value (zero) stored in a specific memory location.
  "Nothing" has a concrete representation, which is philosophically
  incoherent. The metaphor says "this points nowhere" but the
  implementation says "this points at address zero." The map and the
  territory diverge: nowhere has an address.
- **Null is not safe to follow, but the type system does not prevent
  it** -- in the physical world, pointing at nothing is harmless. In C,
  dereferencing NULL causes undefined behavior -- typically a
  segmentation fault that terminates the program. The metaphor imports
  the innocuousness of an empty gesture but hides the lethality of
  the implementation. This mismatch is the source of Tony Hoare's
  famous regret: he introduced null references in ALGOL W (1965) and
  later called them his "billion-dollar mistake" because the metaphor
  made them seem benign.
- **Null conflates multiple kinds of absence** -- NULL means "not
  initialized," "not found," "not applicable," "error occurred," and
  "end of data structure" depending on context. The pointing-at-nothing
  metaphor provides no way to distinguish between these. In human
  communication, there is a vast difference between "I have nothing to
  show you" (empty result), "I refuse to show you" (error), and "I
  have not looked yet" (uninitialized). NULL collapses all of these
  into a single value.
- **Modern languages are abandoning the metaphor** -- Rust has no null;
  it uses `Option<T>`. Kotlin has nullable types with compile-time
  checks. Swift has optionals. These languages reject the idea that a
  pointer can point at nothing, replacing it with an explicit container
  that either holds a value or does not. The shift from null to
  `Option` is a shift from "a pointer to nothing" to "a box that might
  be empty" -- a different metaphor entirely, and one that the type
  system can enforce.
- **The zero address is an arbitrary convention** -- NULL is typically
  zero, but there is no deep reason why the absence of a referent
  should be represented by the number zero. Some historical systems
  used different null representations. The metaphor of "pointing at
  nothing" is clean and intuitive, but it is implemented by a numeric
  convention that has no metaphorical justification.

## Expressions

- "Null pointer exception" -- the most common runtime error in C-family
  languages, caused by following a pointer that points at nothing
  (Java uses NullPointerException, though Java does not have pointers
  in the C sense)
- "Check for null" -- the defensive programming ritual of verifying
  that a pointer actually points at something before following it
- "The billion-dollar mistake" -- Tony Hoare's name for his invention
  of null references, measuring the cumulative cost of null-related
  bugs across the history of software
- "Null-terminated" -- using NULL as an end-of-data marker, as in C
  strings, where the pointing-at-nothing metaphor becomes a stop sign
- "Nullable" -- a type system annotation indicating that a value might
  be null, making the possibility of absence explicit in the type
- "Segfault on null deref" -- the terse diagnostic for the most
  common consequence of following a pointer into the void

## Origin Story

Tony Hoare introduced null references in ALGOL W in 1965, describing
the decision decades later in his 2009 QCon talk: "I call it my
billion-dollar mistake. It was the invention of the null reference in
1965. At that time, I was designing the first comprehensive type system
for references in an object oriented language (ALGOL W). My goal was to
ensure that all use of references should be absolutely safe, with
checking performed automatically by the compiler. But I couldn't resist
the temptation to put in a null reference, simply because it was so
easy to implement."

C inherited the concept through its lineage from BCPL and B. In C, NULL
is a macro defined in `<stddef.h>`, typically expanding to `((void *)0)`.
The choice of address zero as the null value was pragmatic: on most
systems, address zero is not a valid data location, so dereferencing it
reliably produces a fault rather than silent corruption.

The metaphor has proven so problematic that the history of programming
language design since the 1990s can partly be read as a series of
attempts to eliminate null: option types in ML (1973), Maybe in Haskell
(1990), Optional in Java 8 (2014), Option in Rust (2015). Each
represents a rejection of the "pointer to nothing" metaphor in favor of
an explicit "presence or absence" container.

## References

- Hoare, C.A.R. "Null References: The Billion Dollar Mistake," QCon
  London, 2009 -- the creator's retrospective on null
- Kernighan, B. & Ritchie, D. *The C Programming Language*, 1978/1988
  -- defines NULL and its conventions in C
- Ritchie, D. "The Development of the C Language," ACM SIGPLAN, 1993
  -- the lineage from BCPL through B to C
