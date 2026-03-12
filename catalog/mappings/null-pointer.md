---
slug: null-pointer
name: "Null Pointer"
kind: dead-metaphor
source_frame: embodied-experience
target_frame: memory-management
categories:
  - computer-science
  - philosophy
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - c-pointer
---

## What It Brings

NULL encodes absence as a special kind of presence. A null pointer is
not "no pointer" -- it is a pointer that deliberately points at
nothing. The metaphor borrows from the embodied experience of pointing:
you can extend your finger toward empty space, and the gesture is still
a gesture even though nothing is there. In C, NULL is typically defined
as the zero address, a location that the operating system guarantees
contains no valid data. The metaphor converts the philosophical
concept of nothingness into a concrete, manipulable value -- absence
made tangible.

Key structural parallels:

- **Absence as a distinguished value** -- in embodied experience, there
  is a difference between "not pointing at anything" (your hand is at
  your side) and "pointing at nothing" (your finger is extended toward
  empty space). NULL is the second case: an active reference to no
  target. This distinction is the metaphor's core contribution. It
  gives programmers a way to represent "there is no value here" using
  the same mechanism they use to represent "the value is over there."
  The absence has a name, an address, and a testable identity.
- **The sentinel value** -- a null pointer acts as a sentinel: a
  special marker that means "stop looking." C strings end with a null
  byte; linked lists end with a null pointer. The metaphor maps the
  embodied experience of reaching the end of something -- the last
  bead on a string, the edge of a cliff -- onto a particular bit
  pattern that means "nothing beyond this point."
- **The billion-dollar mistake** -- Tony Hoare, who introduced null
  references in ALGOL W (1965), later called it his "billion-dollar
  mistake." The metaphor's power is also its danger: because NULL is a
  valid pointer value, it participates in all pointer operations.
  Dereferencing it -- following the finger to where it points -- causes
  a crash, because there is nothing there. The metaphor permits an
  operation (following) that the value (nothing) cannot support.

## Where It Breaks

- **Nothing is not a location** -- the embodied pointing metaphor
  strains at its foundation. In physical space, pointing at nothing
  still points at a location -- the empty space your finger indicates.
  But in computing, NULL is not an empty location; it is the absence
  of a valid location. Address zero is not "empty memory"; it is a
  reserved sentinel that the hardware may trap on access. The metaphor
  conflates "empty" with "invalid," which is why null pointer
  dereferences are crashes rather than reads of empty data. Beginners
  expect NULL to work like an empty container; it works like a locked
  door with nothing behind it.
- **The metaphor does not distinguish kinds of absence** -- in human
  experience, absence has texture: something was never there, something
  was there and left, something should be there but is not. NULL
  collapses all of these into a single bit pattern. A null pointer
  might mean "not yet initialized," "explicitly cleared," "never
  applicable," or "error occurred." The metaphor provides one word
  for four different meanings, and the programmer must reconstruct the
  intent from context. This is why modern languages (Rust's Option,
  Haskell's Maybe) replace null with explicit sum types that name the
  kind of absence.
- **NULL is not zero, except when it is** -- in C, NULL is typically
  defined as `((void *)0)`, and the null pointer constant is the
  integer 0 in pointer context. But the null pointer's internal
  representation need not be all-zero-bits on all architectures. The
  metaphor of "pointing at address zero" is a convenient fiction that
  happens to be true on most modern hardware but is not guaranteed by
  the language standard. This creates a gap between the metaphor
  (pointing at location zero) and the abstraction (a distinguished
  invalid value) that occasionally bites platform porters.
- **The metaphor normalizes a design flaw** -- by giving absence a
  concrete representation within the type system, null pointers make
  it easy to forget to check for absence. Every pointer in C might be
  NULL, and the type system provides no way to distinguish "pointer
  that is definitely valid" from "pointer that might be NULL." The
  pointing metaphor makes this feel natural -- of course a pointer
  might point at nothing -- when it is actually a type-safety hole
  that causes an estimated 70% of security vulnerabilities in
  C and C++ codebases.

## Expressions

- "Null pointer dereference" -- the canonical crash: following a finger
  that points at nothing; the single most common bug class in
  systems programming
- "The billion-dollar mistake" -- Hoare's 2009 confession, now the
  standard shorthand for null's design cost
- "Segmentation fault" -- the hardware-level consequence of
  dereferencing NULL on most platforms; "segfault" has become
  synonymous with null pointer bugs in casual usage
- "Check for null" -- the defensive programming mantra; every function
  that receives a pointer must ask "is this pointing at nothing?"
  before following it
- "Null safety" -- the design goal of languages (Kotlin, Rust, Swift)
  that replace null with explicit option types; defined by opposition
  to C's permissive null model
- "NullPointerException" -- Java's version, so common it is
  abbreviated "NPE" and has become a metonym for all null-related bugs

## Origin Story

Tony Hoare introduced the null reference in ALGOL W in 1965 as a
convenient way to represent the absence of a value. In his 2009 QCon
talk, he called it "my billion-dollar mistake":

> I couldn't resist the temptation to put in a null reference, simply
> because it was so easy to implement. This has led to innumerable
> errors, vulnerabilities, and system crashes, which have probably
> caused a billion dollars of pain and damage in the last forty years.

C inherited the concept through its lineage from BCPL and B. Dennis
Ritchie formalized NULL as a macro expanding to zero in pointer
context, cementing the convention that address zero means "nothing
here." The choice was pragmatic: zero was already the default value for
uninitialized memory on PDP-11 hardware, so an uninitialized pointer
would naturally be NULL -- a coincidence that made null pointers both
ubiquitous and insidious.

The metaphor has proven so durable that even languages designed to
eliminate null (Rust, Haskell, Swift) must explain themselves in
relation to it. "Null safety" is defined by what it removes, not by
what it adds.

## References

- Hoare, C.A.R. "Null References: The Billion Dollar Mistake," QCon
  London, 2009
- Ritchie, D. "The Development of the C Language," *ACM SIGPLAN
  Notices* 28(3), 1993
- Kernighan, B. & Ritchie, D. *The C Programming Language* (2nd ed.),
  Prentice-Hall, 1988
- ISO/IEC 9899:2011 (C11 Standard), Section 6.3.2.3 on null pointer
  constants
