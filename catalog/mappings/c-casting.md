---
slug: c-casting
name: "C Casting"
kind: dead-metaphor
source_frame: manufacturing
target_frame: type-system
categories:
  - computer-science
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - c-pointer
---

## What It Brings

To "cast" a value is to pour it into a new mold. The metaphor comes
from metalwork and foundry practice: molten metal is poured into a
shaped mold (a cast), and when it solidifies, it takes the shape of
the mold. In C, casting converts a value from one type to another --
an integer becomes a float, a void pointer becomes a char pointer, a
wider type is forced into a narrower one. The manufacturing metaphor
frames type conversion as a process of reshaping: the raw material
(the value) is forced into a new form (the target type) by the
constraint of the mold.

Key structural parallels:

- **Transformation through constraint** -- in metal casting, the
  liquid takes the shape of whatever mold it is poured into. The mold
  does not change the material; it changes the shape. A C cast does
  not change the underlying bits (in most cases); it changes how the
  compiler interprets them. The value takes the "shape" of the new
  type. This structural parallel is the metaphor's core insight: type
  conversion is not creation of a new value but reinterpretation of
  existing material under a new constraint.
- **The mold determines the result** -- a metalworker chooses the mold
  based on the desired output shape. A C programmer chooses the target
  type based on the desired interpretation. `(float)3` and `(char)3`
  apply different "molds" to the same raw material, producing different
  shapes. The cast operator in C syntax -- `(type)expression` --
  visually places the mold (the type in parentheses) before the
  material (the expression), mirroring the physical sequence of
  preparing the mold before pouring.
- **Widening as safe casting** -- pouring metal into a larger mold
  always works; there is room for the material. Widening conversions
  (int to long, float to double) are similarly safe: no information is
  lost because the target type can represent everything the source type
  can. The metaphor maps physical fit onto type compatibility.
- **Narrowing as dangerous casting** -- forcing metal into a mold
  smaller than the piece risks overflow, cracking, or loss of detail.
  Narrowing conversions (double to int, long to short) are similarly
  dangerous: the target type may not be able to represent the source
  value, causing truncation or undefined behavior. The metaphor imports
  the physical intuition that forcing material into an undersized
  container is destructive.

## Where It Breaks

- **Metal casting is irreversible; C casting is often reversible** --
  once metal has solidified in a mold, you cannot pour it back into
  its original shape without remelting it. But many C casts are freely
  reversible: cast an int to a float and back, and you may recover
  the original value (precision permitting). The metaphor imports a
  permanence that the operation does not have. Programmers who
  internalize the manufacturing metaphor may overestimate the
  commitment involved in a cast.
- **Reinterpret casts have no manufacturing analog** -- C allows
  casting a pointer from one type to another, reinterpreting the same
  memory as a different structure. This is not reshaping material; it
  is relabeling it. The bits do not change; only the compiler's
  interpretation changes. Metal casting always physically transforms
  the material. `*(float *)&int_val` does not reshape anything -- it
  reads the same bytes as if they were a different type. The metaphor
  provides no vocabulary for this "relabeling" operation, which is why
  reinterpret casts confuse beginners: the manufacturing metaphor
  suggests something should change, but nothing does.
- **The metaphor hides information loss** -- when you cast metal into
  a smaller mold, the excess is visibly wasted (flash, overflow,
  trimming). When you cast a double to an int in C, the fractional
  part silently disappears. There is no visible "waste" -- the
  truncation happens without warning unless the programmer explicitly
  checks. The manufacturing metaphor suggests that loss should be
  obvious; in C, it is silent and often undetected.
- **C++ exposed the metaphor's poverty** -- C has one cast syntax
  that covers all conversion types. C++ introduced four distinct cast
  operators: `static_cast`, `dynamic_cast`, `reinterpret_cast`, and
  `const_cast`. This proliferation reveals that the single
  manufacturing metaphor was conflating at least four different
  operations. The original metaphor was too coarse: "casting" elided
  the distinction between safe conversion, runtime-checked conversion,
  bit reinterpretation, and const removal. The C++ names are explicit
  admissions that a single metaphor was insufficient.

## Expressions

- "Cast it to int" -- the standard idiom, using "cast" as a verb
  meaning "convert the type of"; the metallurgical origin is invisible
  to most speakers
- "Type cast" -- the noun form, still echoing the foundry meaning of
  "cast" as the shaped output of a mold
- "Implicit cast" / "explicit cast" -- the compiler performing a
  conversion automatically versus the programmer requesting it with
  syntax; implicit casts strain the metaphor because the metalworker
  is absent
- "Unsafe cast" -- a cast that may lose information or violate type
  safety; the "unsafe" label imports the physical danger of forcing
  material into an ill-fitting mold
- "Downcasting" / "upcasting" -- object-oriented terms for casting
  within a type hierarchy; the spatial metaphor (up/down) overlays the
  manufacturing metaphor, creating a mixed-domain expression
- "Cast away const" -- C++'s `const_cast`, where "cast away" means
  "remove a constraint"; the manufacturing metaphor is barely present,
  replaced by the idiom of discarding something unwanted

## Origin Story

The term "cast" for type conversion appears in early programming
language literature, likely entering through Fortran and its
contemporaries in the 1950s and 1960s. The metallurgical metaphor was
a natural fit for the computing culture of the era: many early
programmers had engineering backgrounds and would have recognized the
foundry reference immediately. By the time C formalized the cast
operator in the early 1970s, the term was already established in
programming vocabulary.

C's cast syntax -- placing the target type in parentheses before the
expression -- was Ritchie's design. It is terse, powerful, and
dangerous: a C cast can convert between any scalar types and between
any pointer types, with no runtime checking. This permissiveness
reflects C's philosophy of trusting the programmer, but it also means
that the "mold" in C has no safety rails. Bjarne Stroustrup's decision
to split C's single cast into four named operators in C++ was an
explicit acknowledgment that the original metaphor was doing too much
work. Each C++ cast names a specific kind of conversion, replacing one
overloaded metaphor with four specific ones.

## References

- Kernighan, B. & Ritchie, D. *The C Programming Language* (2nd ed.),
  Prentice-Hall, 1988
- Ritchie, D. "The Development of the C Language," *ACM SIGPLAN
  Notices* 28(3), 1993
- Stroustrup, B. *The Design and Evolution of C++*, Addison-Wesley,
  1994
- ISO/IEC 9899:2011 (C11 Standard), Section 6.5.4 on cast operators
