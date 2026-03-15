---
author: agent:metaphorex-miner
categories:
- computer-science
contributors:
- fshot
created: '2026-03-15'
harness: Claude Code
kind: dead-metaphor
name: Memory Heap
related:
- memory-stack
- memory-leak
- buffer-overflow
slug: memory-heap
source_frame: embodied-experience
target_frame: software-programs
updated: '2026-03-15'
---

## What It Brings

A heap is a disordered pile of things -- clothes on a floor, rubble after
a demolition, potatoes in a market bin. The "heap" in memory management
borrows this image of unstructured accumulation to describe the region of
memory where dynamically allocated blocks are placed and retrieved in
arbitrary order. The metaphor gains its meaning primarily through contrast
with the stack, which is orderly, sequential, and automatic. The heap is
the stack's disorderly counterpart.

Key structural parallels:

- **Disorder as defining characteristic** -- a heap of objects has no
  inherent ordering. You can grab any item from any position. The memory
  heap similarly allows allocation and deallocation in any order: you can
  free block 3 before block 1, leave block 2 alive indefinitely, and
  allocate block 4 into the gap left by block 3. This distinguishes it
  from the stack, where allocation and deallocation follow strict LIFO
  order. The metaphor makes the distinction visceral: imagine a neat
  stack of plates versus a heap of laundry.
- **Manual management** -- you have to sort through a heap yourself;
  nobody organizes it for you. The memory heap requires manual
  management: the programmer calls `malloc()` to allocate and `free()`
  to deallocate. Forgetting to free produces a memory leak (the heap
  grows with unclaimed debris). Freeing twice produces corruption (like
  pulling a load-bearing item from a pile). The embodied experience of
  rummaging through a disordered pile maps onto the programmer's burden
  of tracking what was allocated where.
- **Fragmentation as scattered debris** -- a heap of objects that has
  been partially removed has gaps. The memory heap fragments similarly:
  after many allocations and deallocations, free memory is scattered in
  small, non-contiguous blocks. A large allocation may fail even when
  total free memory is sufficient, because no single contiguous gap is
  large enough. This is like trying to lay a large board on top of a
  heap of irregularly shaped objects -- there is space, but not the
  right shape of space.
- **The heap as the place where things accumulate** -- in everyday
  experience, heaps grow when things are tossed rather than placed.
  The memory heap accumulates objects that outlive their creating
  function: anything that needs to persist beyond a single function
  call gets tossed onto the heap. Over time, long-running programs
  accumulate substantial heaps, just as a household accumulates piles.

## Where It Breaks

- **The memory heap is actually structured** -- this is the central
  irony. Despite the name, the memory heap is not a disordered pile.
  Memory allocators (like glibc's ptmalloc, jemalloc, or tcmalloc) use
  sophisticated data structures -- free lists, buddy systems, slab
  allocators, size-class bins -- to manage the heap efficiently. The
  "heap" is one of the most heavily engineered regions of a running
  program. Calling it a heap understates the complexity of its internal
  organization and misleads programmers into thinking it is simpler
  than it is.
- **Confusion with the heap data structure** -- computer science also
  uses "heap" to describe a specific tree-based data structure (a
  binary heap, used in priority queues and heapsort). The memory heap
  and the heap data structure are entirely unrelated, despite sharing
  a name. This homonymy causes genuine confusion among students, who
  reasonably assume that the memory heap must use the heap data
  structure internally. It usually does not.
- **The metaphor suggests passive accumulation; allocation is active** --
  a physical heap grows passively: things are tossed on it. Memory
  allocation is an active, computationally expensive operation that
  involves searching free lists, splitting blocks, and maintaining
  metadata. The heap metaphor hides this cost, encouraging programmers
  to treat allocation as free when it is not.
- **"Heap corruption" oversimplifies the failure mode** -- "the pile
  collapsed" is an intuitive image for heap corruption, but actual heap
  corruption is far more insidious. A buffer overrun writes past one
  allocation into the metadata of the next, causing failures that
  manifest much later and far from the actual bug. A collapsing pile
  fails at the point of collapse; heap corruption fails at an
  unpredictable remove from the cause. The metaphor understates the
  diagnostic difficulty.

## Expressions

- "Heap allocation" -- placing an object on the heap, so routine that
  the spatial metaphor is completely invisible
- "Heap corruption" -- the pile has been damaged, usually by writing
  past the bounds of an allocation
- "Heap fragmentation" -- the free space is scattered in unusable
  small pieces, like debris gaps in a pile
- "On the heap" vs "on the stack" -- the fundamental allocation
  dichotomy, expressed as two spatial locations
- "Heap dump" -- a snapshot of everything on the heap, used for
  debugging memory issues, like inventorying the pile
- "Grow the heap" -- requesting more memory from the operating system,
  extending the pile's territory

## Origin Story

The term "heap" for dynamically allocated memory dates to the 1960s and
is attributed to early work on LISP and Algol implementations, where
memory that was not managed by the call stack needed a name. The
contrast with "stack" was already established: the stack was orderly
(LIFO discipline), so the non-stack region was the heap -- disordered,
manually managed, the place where everything else went. The term was
well established by the time Kernighan and Ritchie described C's
`malloc()` and `free()` functions in *The C Programming Language* (1978),
though K&R did not dwell on the metaphor. The name stuck because the
contrast with "stack" was too useful to abandon: two spatial metaphors,
one for order and one for disorder, that together cover all of a
program's memory needs.

## References

- Kernighan, B. & Ritchie, D. *The C Programming Language* (1978/1988)
  -- the canonical description of C's dynamic memory allocation
- Knuth, D. *The Art of Computer Programming*, Vol. 1 (1968) -- early
  formal treatment of dynamic storage allocation algorithms
- Wilson, P. et al. "Dynamic Storage Allocation: A Survey and Critical
  Review," Springer LNCS 986 (1995) -- comprehensive survey of heap
  allocation techniques
