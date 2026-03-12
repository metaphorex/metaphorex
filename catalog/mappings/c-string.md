---
slug: c-string
name: "C String"
kind: dead-metaphor
source_frame: embodied-experience
target_frame: text-representation
categories:
  - computer-science
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - c-pointer
  - null-pointer
---

## What It Brings

Characters strung together like beads on a thread. The metaphor
borrows from the embodied experience of linear ordering: objects
arranged in a row along a single axis, held together by a common
medium. A "string" of pearls, a "string" of lights, a "string" of
boxcars -- in each case, distinct items are connected in sequence,
and the order matters. In C, a string is a null-terminated array of
characters: the characters are the beads, the contiguous memory is the
thread, and the null terminator `\0` is the knot at the end.

Key structural parallels:

- **Linear ordering** -- beads on a string have a first, a second, a
  next, and a last. Characters in a C string have the same structure:
  they are stored in consecutive memory addresses, and their order is
  their meaning. "cat" is not "tac" because the sequence matters. The
  metaphor imports the intuition that text is fundamentally sequential,
  which it is -- writing systems are linear even when the concepts they
  express are not.
- **The terminator as the knot** -- a physical string of beads ends
  with a knot or clasp. A C string ends with the null byte `\0`, a
  sentinel value that says "the string stops here." This is C's
  defining design choice for strings, and it maps directly onto the
  physical metaphor: you know where the string ends because there is a
  marker. The alternative -- storing the length separately, as Pascal
  did -- breaks the metaphor: counted strings are more like a manifest
  listing how many beads there are, rather than a physical string you
  can follow to its end.
- **Concatenation as joining strings together** -- the function
  `strcat` (string concatenate) joins two strings into one. The word
  "concatenate" comes from Latin *catena* (chain), reinforcing the
  linear-linkage metaphor. You are chaining two sequences together,
  tying the end of one to the beginning of another.
- **Immutability of the sequence** -- beads on a string are fixed in
  their order unless you restring them. C strings stored in read-only
  memory (string literals) are similarly immutable. Modifying a string
  literal causes undefined behavior -- you cannot rearrange the beads
  without making a new string.

## Where It Breaks

- **Strings have no inherent length** -- you know how many beads are
  on a physical string by counting them or measuring the string. But a
  C string carries no length information; you must scan for the null
  terminator to find its end. This means that `strlen()` is O(n) -- it
  must walk the entire string, bead by bead, to count them. The
  physical metaphor suggests that length is an obvious property; in C,
  it is an expensive computation. This mismatch is the root cause of
  countless performance bugs.
- **The null terminator is a trap** -- the knot at the end of a string
  is visible and obvious. The `\0` byte is invisible, occupies one
  byte of the array, and is easily overwritten or omitted. If a string
  is not properly null-terminated, functions that scan for the
  terminator will read past the end of the allocated memory,
  potentially crashing or leaking data. Buffer overflows in C string
  handling are one of the most exploited vulnerability classes in
  software history. The physical metaphor provides no warning of this
  danger because a missing knot on a physical string merely causes
  beads to fall off; it does not cause the string to consume
  neighboring objects.
- **Character is not a bead** -- the metaphor assumes each element is
  a uniform, discrete unit. ASCII characters fit this model, but
  Unicode does not: a single visible character (grapheme cluster) can
  span multiple bytes, and a multibyte encoding like UTF-8 means that
  "beads" come in different sizes. The beads-on-a-string metaphor
  collapses when a "character" is no longer a fixed-width unit. C's
  string model, designed for ASCII, was never updated for the
  variable-width encodings that modern text requires.
- **The metaphor hides memory management** -- a physical string
  occupies exactly as much space as its beads require. A C string must
  be allocated in memory, and the programmer is responsible for
  ensuring the buffer is large enough. Appending a bead to a physical
  string is trivial; appending a character to a C string may require
  reallocating the entire buffer. The embodied metaphor suggests that
  strings grow naturally; the implementation demands explicit, careful
  memory management that the metaphor does not predict.

## Expressions

- "String" -- the term itself, so thoroughly dead as a metaphor that
  most programmers have never considered why a sequence of characters
  is called a "string"
- "Null-terminated string" -- the defining characteristic of C's
  string convention, where "terminated" echoes the physical end of a
  cord
- "String concatenation" -- joining strings, from Latin *catena*
  (chain); `strcat` in C
- "Empty string" -- a string containing only the null terminator: a
  thread with no beads, just the knot
- "String literal" -- a string value written directly in source code,
  enclosed in double quotes; "literal" distinguishes the fixed text
  from a computed string
- "Buffer overflow" -- writing past the end of a string's allocated
  memory, the consequence of the metaphor's failure to encode length;
  the canonical C security vulnerability

## Origin Story

The term "string" for a sequence of characters predates C by decades.
It appears in the formal language theory literature of the 1950s and
1960s, used by Chomsky and others to describe sequences of symbols in
a grammar. ALGOL and its descendants used the term, and it entered
widespread programming language vocabulary before C was designed.

C's specific contribution was the null-terminated convention. Dennis
Ritchie and Ken Thompson chose to end strings with a `\0` byte rather
than storing a length prefix, partly because the PDP-7 and PDP-11
instruction sets made sentinel-scanned loops efficient, and partly
because it kept the representation minimal -- no extra bytes for a
length field. This decision, optimized for 1970s hardware constraints,
became the dominant string representation in systems programming and
the source of an entire class of security vulnerabilities that
persists fifty years later.

The word "string" itself likely derives from "string of symbols,"
which in turn borrows from the physical image of objects threaded onto
a cord. By the time C was written, the metaphor was already dead --
Ritchie did not need to explain why "string" meant "sequence of
characters." The term had achieved full lexical independence from its
source domain.

## References

- Kernighan, B. & Ritchie, D. *The C Programming Language* (2nd ed.),
  Prentice-Hall, 1988
- Ritchie, D. "The Development of the C Language," *ACM SIGPLAN
  Notices* 28(3), 1993
- One, A. "Smashing the Stack for Fun and Profit," *Phrack* 49, 1996
  -- the canonical exposition of C string buffer overflow exploitation
- ISO/IEC 9899:2011 (C11 Standard), Section 7.1.1 on string
  definitions
