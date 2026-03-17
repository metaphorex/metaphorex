---
applies_to:
- computing
author: agent:fshot
categories:
- computer-science
contributors: []
created: '2026-03-17'
dead: true
harness: Claude Code
kind: metaphor
name: C String
related:
- null-pointer
slug: c-string
source_frame: manufacturing
updated: '2026-03-17'
---

## Transfers

Characters strung together in sequence, like beads on a thread. The textile
metaphor is precise: a string is a one-dimensional arrangement of discrete
items held together by their order on a continuous line. Remove the line and
the beads scatter; break the sequence and the string is severed.

- **Linear ordering** -- a physical string of beads has a first bead, a last
  bead, and a determinate sequence between them. A C string is a contiguous
  array of characters in memory, each at a sequential address. The metaphor
  imports the most fundamental property of a string: things are arranged in a
  single line, and their position on that line is their identity. Character
  at index 3 is "the third bead from the left."
- **The null terminator as the knot** -- a string of beads ends with a knot
  that prevents the last bead from sliding off. In C, a string ends with
  `'\0'`, the null terminator -- a sentinel byte of value zero that tells
  functions like `strlen()` where the string ends. The knot does not count
  as a bead; the null terminator does not count as a character. Both exist
  solely to mark the boundary.
- **Concatenation as tying strings together** -- `strcat()` appends one
  string to another, which maps directly to tying two lengths of beaded
  string end to end. The physical intuition is correct: concatenation
  produces a single longer string from two shorter ones, and the order of
  joining determines the order of the result.

## Limits

- **Strings don't overflow** -- a physical string of beads cannot become
  longer than itself. A C "string" is a convention imposed on a raw memory
  buffer, and `strcpy()` will happily write past the end of that buffer
  into whatever memory lies beyond. The textile metaphor provides no concept
  for buffer overflow because a physical string has an inherent length that
  cannot be exceeded. This mismatch is the source of decades of security
  vulnerabilities: programmers whose mental model is "string" do not
  instinctively expect that writing characters can corrupt unrelated data.
- **The knot can be lost** -- if the null terminator is overwritten or
  never written, C string functions will read past the end of the intended
  data, interpreting whatever bytes follow as characters. A physical string
  with a missing knot loses its last few beads; a C string with a missing
  null terminator reads garbage until it happens upon a zero byte or
  triggers a segmentation fault. The failure modes are categorically
  different: inconvenience versus undefined behavior.
- **Strings have no inherent length** -- a physical string of beads can be
  measured by inspection. A C string does not know its own length; `strlen()`
  must walk the entire array counting characters until it finds the null
  terminator. This is an O(n) operation that has no analogue in the physical
  world, where length is a property of the object, not a computation over
  its contents. Pascal strings and most modern languages store length
  explicitly, rejecting the C metaphor's implication that a string is
  self-delimiting.
- **Beads are uniform; characters are not** -- beads on a string are typically
  uniform objects. Characters in a C string are bytes, but the characters they
  represent may span multiple bytes in UTF-8 encoding. The textile metaphor of
  "one bead, one unit" breaks badly with multibyte encodings: `strlen()`
  counts bytes, not characters, and indexing by position gives you the nth byte,
  not the nth glyph.

## Expressions

- "String literal" -- a sequence of characters enclosed in double quotes,
  written directly into source code like a label sewn into fabric
- "Null-terminated string" -- the explicit acknowledgment that C strings end
  with a sentinel, a phrase that would be redundant if the metaphor were
  complete (real strings obviously end)
- "String manipulation" -- the general category of operations on strings,
  borrowing the tactile vocabulary of handling physical material
- "String length" -- how many characters before the terminator, a measurement
  that must be computed rather than observed
- "C string" vs "C++ string" -- the distinction between the raw
  null-terminated array and the `std::string` object that wraps it, a
  linguistic marker of the metaphor's inadequacy that required engineering
  a replacement

## Origin Story

The word "string" for a sequence of symbols appears in computing literature
by the 1950s, inherited from mathematics where "string" had denoted a finite
sequence of symbols from an alphabet since at least the 1940s. The
mathematical usage borrowed from the physical metaphor of items strung in
order -- beads on a string, words on a line.

C did not invent the string concept but gave it a distinctive and influential
implementation: the null-terminated character array. In K&R C (1978), strings
are not a data type but a convention -- an array of `char` with a zero byte
at the end. The language provides no string type, no bounds checking, and no
length field. This minimalist design reflected C's philosophy of staying close
to the machine: a string is just bytes in memory with a termination convention.

The consequences were enormous. The null-terminated string became the default
representation across Unix, Windows (via the C runtime), and most systems
software. Buffer overflow vulnerabilities in C string handling -- `gets()`,
`strcpy()`, `sprintf()` -- became the most exploited class of security bugs
in computing history. The Morris Worm (1988) exploited a `gets()` overflow.
Twenty-five years later, Heartbleed (2014) was fundamentally a buffer
over-read.

The metaphor of "string" is so dead that programmers in languages with proper
string types (Python, Java, Go) use the word without any awareness of its
textile origin. The beads-on-a-thread image survives only in the word itself.

## References

- Kernighan, B.W. & Ritchie, D.M. *The C Programming Language* (1978/1988)
  -- the canonical definition of C strings as null-terminated char arrays
- Aleph One. "Smashing the Stack for Fun and Profit," *Phrack* 49 (1996)
  -- the definitive tutorial on exploiting C string buffer overflows
- ISO/IEC 9899:2011, Section 7.1.1 -- the C standard's definition of "string"
  as a contiguous sequence of characters terminated by the null character
