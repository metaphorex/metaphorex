---
author: agent:metaphorex-miner
categories:
- computer-science
contributors:
- fshot
created: '2026-03-15'
harness: Claude Code
kind: dead-metaphor
name: C String
related:
- c-pointer
- null-pointer
slug: c-string
source_frame: embodied-experience
target_frame: data-processing
updated: '2026-03-15'
---

## What It Brings

A string of beads, a string of pearls, a string of characters -- items
threaded onto a line in fixed order. The metaphor maps the linear,
sequential arrangement of physical objects on a cord onto the linear,
sequential arrangement of characters in memory. In C, a string is an
array of `char` values terminated by a null byte (`\0`), and the
metaphor encodes both the ordering and the endpoint: beads on a thread,
with a knot at the end.

Key structural parallels:

- **Linear ordering** -- beads on a string have a first, a second, a
  third, and a last. Characters in a C string have an index: `s[0]`,
  `s[1]`, `s[2]`. The metaphor maps physical sequence onto memory
  sequence. You can traverse a string from beginning to end, just as
  you can run your finger along a strand of beads.
- **Contiguity** -- beads on a string touch their neighbors. Characters
  in a C string occupy adjacent memory addresses. There are no gaps,
  no jumps, no out-of-order elements. The metaphor imports the
  physical constraint that a string holds its elements together in a
  continuous run.
- **The terminator as a knot** -- a physical string of beads needs
  something at the end to prevent the beads from sliding off. In C,
  the null terminator (`\0`) serves this role: it marks where the
  string ends. Without it, functions like `strlen()` and `printf()`
  would run past the end of the data, reading whatever happens to be
  in adjacent memory. The knot metaphor is implicit but structurally
  precise.
- **The string itself is not the beads** -- a physical string is the
  cord that holds the beads, not the beads themselves. Similarly, a C
  "string" is the *arrangement* -- the convention of null-terminated
  `char` array -- not the individual characters. You can remove beads
  from a string and restring them; you can copy characters from one
  array to another. The container and the contents are conceptually
  separable.

## Where It Breaks

- **Strings are not a type in C** -- in the physical world, a string
  of beads is a recognizable object. In C, there is no `string` type.
  A "string" is a convention: a `char *` that happens to point to a
  null-terminated sequence of bytes. The language provides no
  enforcement of this convention. A `char *` might point to a
  null-terminated string, a fixed-length buffer, a single character,
  or freed memory. The metaphor names something that the type system
  does not recognize.
- **Buffer overflows betray the metaphor** -- a physical string has a
  definite length and you can see where it ends. A C string's length
  is discovered only by scanning for the null terminator, and if the
  terminator is missing or the buffer is too small, functions will
  read or write past the end. This is the buffer overflow, the most
  exploited class of vulnerability in computing history. The string
  metaphor implies a bounded, self-contained object; the reality is
  an open-ended convention that trusts the programmer to get the
  boundaries right.
- **Encoding is invisible** -- beads on a string are what they appear
  to be. Characters in a C string are bytes, and bytes can encode
  different character sets. A C string of UTF-8 text looks identical
  to a C string of ASCII text at the byte level, but `s[3]` might be
  the fourth character (ASCII) or the middle of a multi-byte character
  (UTF-8). The metaphor of beads-on-a-string implies that each
  position holds one complete element, which is false for any
  multi-byte encoding.
- **The metaphor has been superseded** -- modern languages replace C
  strings with string objects that know their own length (Python's
  `str`, Rust's `String`, Go's `string`). These are closer to a
  "rope" or "ribbon" metaphor: a managed, self-describing sequence
  rather than a raw array with a sentinel. The bead-on-a-string
  metaphor's reliance on a null terminator is now understood as a
  design flaw, not a feature.
- **Mutation is unrestricted** -- beads on a physical string are
  fixed once strung. C strings are mutable: you can overwrite any
  character at any index, change the length by moving the terminator,
  or concatenate strings by copying bytes. The metaphor imports the
  stability of a physical arrangement but the implementation allows
  arbitrary modification, including modifications that silently
  corrupt the string.

## Expressions

- "Null-terminated string" -- the canonical description, naming both
  the metaphor (string) and the mechanism (null termination)
- "String literal" -- a sequence of characters enclosed in double
  quotes in C source code, like `"hello"`, which the compiler
  automatically null-terminates
- "String copy" -- `strcpy()`, which copies characters until it
  encounters the null terminator, trusting that the destination buffer
  is large enough (a frequent source of buffer overflows)
- "String length" -- `strlen()`, which counts characters by scanning
  for the null terminator, an O(n) operation that surprises
  programmers accustomed to languages where strings know their own
  length
- "Empty string" -- a string whose first byte is the null terminator,
  the string metaphor's representation of a cord with no beads
- "String manipulation" -- the general category of operations on
  strings, using "manipulation" (from Latin *manus*, hand) to
  reinforce the tactile metaphor of handling a physical object

## Origin Story

The word "string" for a sequence of characters predates C by decades.
It appears in ALGOL and FORTRAN documentation from the 1950s and 1960s,
borrowed from the mathematical concept of a "string" as a finite
sequence of symbols from an alphabet (formal language theory). The
mathematical use itself likely derives from the physical image of
symbols strung together in order.

C's contribution was not the term but the implementation: the
null-terminated character array. Dennis Ritchie inherited this from
B and BCPL, which treated strings as packed byte arrays. The null
termination convention was a pragmatic choice on the PDP-11: it
avoided storing a separate length field and made string functions
simple loops. This simplicity came at the cost of safety -- the
missing length field is the root cause of buffer overflow
vulnerabilities that have plagued C programs for fifty years.

Kernighan and Ritchie's *The C Programming Language* (1978)
established the conventions for C string handling that persist today,
including the standard library functions `strlen`, `strcpy`, `strcat`,
and `strcmp`. These functions all depend on null termination, and their
unsafe behavior when given unterminated input has been the subject of
innumerable security advisories.

## References

- Kernighan, B. & Ritchie, D. *The C Programming Language*, 1978/1988
  -- defines C string conventions and standard library functions
- Ritchie, D. "The Development of the C Language," ACM SIGPLAN, 1993
  -- historical context for C's string implementation
- One, A. "Smashing the Stack for Fun and Profit," Phrack 49, 1996
  -- the canonical description of buffer overflow exploitation, which
  depends on C string conventions
