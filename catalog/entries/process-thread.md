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
name: Process Thread
related:
- race-condition
slug: process-thread
source_frame: manufacturing
updated: '2026-03-17'
---

## Transfers

A thread of execution as a literal thread -- a fiber spun from raw material,
running alongside other fibers, capable of being woven together into fabric.
The textile metaphor structures how programmers think about concurrent
execution: threads are parallel strands that may interleave, tangle, or be
woven into a coherent whole.

- **Parallel strands** -- in a loom, multiple threads run side by side, each
  following its own path but contributing to a shared fabric. In a process,
  multiple threads of execution run concurrently, each following its own
  instruction sequence but sharing the same address space. The metaphor
  encodes the essential architecture: threads are independent paths that
  coexist within a common structure. A single thread is a strand; many
  threads woven together are a program.
- **Spinning up** -- in textile manufacturing, spinning is the act of drawing
  out raw fiber and twisting it into thread. "Spinning up a thread" in
  computing means creating a new execution context from the raw material of
  the process's resources (memory, file descriptors, signal handlers). The
  metaphor captures the transformation: something that was potential (fiber,
  resources) becomes actual (thread, execution path).
- **Thread safety as threads not tangling** -- tangled thread is the
  fundamental failure mode of textile work. Thread safety in computing means
  that concurrent threads will not corrupt shared data -- that they will run
  alongside each other without entanglement. The metaphor maps the physical
  disaster (a tangled skein that must be painstakingly unwound) to the
  computational disaster (a race condition that must be painstakingly
  debugged).

## Limits

- **Textile threads don't share material** -- each physical thread is its own
  fiber. Computing threads within a process share the same memory space. This
  is the fundamental departure from the textile metaphor: real threads cannot
  reach into each other and modify each other's substance. Computing threads
  can and do read and write each other's data, which is both their primary
  advantage (cheap communication) and their primary hazard (data races). The
  metaphor of separate strands running in parallel actively misleads about
  the degree of entanglement.
- **Weaving is deterministic** -- a loom produces the same fabric from the
  same threads every time. Multithreaded programs are non-deterministic: the
  exact interleaving of operations depends on scheduling decisions made by
  the operating system at runtime. Two runs of the same program may produce
  different results. The textile metaphor implies a craft with predictable
  outcomes; concurrent programming is closer to a craft where the loom
  rearranges threads at random.
- **Thread death is nothing like thread cutting** -- cutting a physical thread
  ends it cleanly at a known point. Killing a computing thread can leave
  shared data in an inconsistent state, hold unreleased locks, or leak
  resources. The textile metaphor of clean severance maps onto the computing
  reality of messy, dangerous termination. This is why thread cancellation
  is one of the hardest problems in concurrent programming -- there is no
  computational equivalent of scissors.
- **The fiber predates the loom** -- in textiles, thread exists before it is
  woven. In computing, a thread does not exist until it is created within a
  process. There is no independent existence for a thread outside its
  process, no spool of execution context waiting to be loaded into a loom.
  The textile metaphor implies that threads are primitive and looms are
  secondary; in computing, the process (the "loom") must exist before any
  thread can.

## Expressions

- "Multithreading" -- running multiple threads within a single process,
  described as if multiple fibers are being worked simultaneously on a loom
- "Thread pool" -- a pre-created collection of threads awaiting work, like
  a basket of prepared threads beside a loom
- "Thread safety" -- code that can be executed by multiple threads without
  corruption, the computational equivalent of tangle-free thread
- "Spinning up a thread" -- creating a new thread, drawing out a new fiber
  from the process's resources
- "Deadlock" -- two threads each holding a resource the other needs, a
  tangle so severe that neither can proceed (though "deadlock" itself is
  from canal lock navigation, not textiles)
- "Thread-local storage" -- data private to a single thread, the one
  departure from the shared-address-space norm, as if each fiber carried
  its own dye

## Origin Story

The term "thread" for a lightweight execution context emerged in the early
1970s. The concept was present in earlier systems -- what Multics called
"execution points" and what some researchers called "lightweight processes"
-- but "thread" became the dominant term through its adoption in Unix-derived
systems and academic literature.

The textile metaphor was chosen for its intuitive mapping: a thread is thinner
than a rope (a full process), many threads can run in parallel, and they can
be woven together into something stronger than any single strand. The word
itself carries centuries of figurative use -- "thread of argument," "thread
of narrative," "thread of thought" -- all denoting a single continuous line
of progression through a larger structure.

The POSIX threads (pthreads) standard, formalized in IEEE 1003.1c (1995),
cemented "thread" as the canonical term. The pthreads API -- `pthread_create`,
`pthread_join`, `pthread_mutex_lock` -- became the standard interface for
multithreaded programming on Unix systems. Java's `Thread` class (1995) and
Windows threads brought the term to mainstream application programming.

By the 2000s, "thread" was universal. The rise of multi-core processors
(Intel Core 2 Duo, 2006) made threading a practical necessity rather than
an optimization, and "multithreaded" became a standard adjective for
performant software. The textile metaphor is now completely dead: no
programmer pictures a loom when creating a thread. The word has been
fully absorbed into technical vocabulary, its etymological fiber invisible.

## References

- IEEE Std 1003.1c-1995 "Threads Extension" -- the POSIX threads standard
  that canonized the term
- Butenhof, D.R. *Programming with POSIX Threads* (1997) -- the canonical
  reference for pthreads programming
- Ritchie, D.M. & Thompson, K. "The UNIX Time-Sharing System," *CACM*
  17(7), 1974 -- the process model from which threads were eventually split
