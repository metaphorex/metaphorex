---
slug: process-thread
name: "Process Thread"
kind: dead-metaphor
source_frame: manufacturing
target_frame: concurrent-execution
categories:
  - computer-science
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - race-condition
---

## What It Brings

A thread is a single continuous strand of fiber -- spun from raw material,
drawn out into a long thin line, and woven together with other threads to
form fabric. The computing term "thread of execution" borrows this textile
image to describe a single sequential flow of control within a program.
Multiple threads run within a single process, interleaving like threads in
cloth. The metaphor predates its computing use: "thread of argument" and
"thread of conversation" have been English idioms since at least the
sixteenth century, meaning a continuous line of thought running through a
larger discourse. Computing inherited both the textile and the
conversational senses.

Key structural parallels:

- **Continuous strand** -- a textile thread is an unbroken line from start
  to end. A thread of execution is an unbroken sequence of instructions
  from creation to termination. The metaphor encodes the fundamental
  property of sequential execution: one thing follows another along a
  single continuous path. This is why we say a thread "runs" -- it
  traces a path through the code.
- **Multiple threads, one fabric** -- threads in a loom run in parallel,
  each following its own path, but they are woven into a single piece of
  fabric. Threads in a process run concurrently, each following its own
  instruction sequence, but they share a single address space and
  contribute to a single program's behavior. The metaphor captures both
  the parallelism and the unity.
- **Spinning up** -- textile threads are produced by spinning: drawing
  out and twisting raw fiber into a continuous strand. "Spinning up a
  thread" in computing means creating a new thread of execution. The
  metaphor imports the idea that thread creation is a manufacturing
  process -- it takes effort and produces something that did not exist
  before.
- **Tangling as failure mode** -- when textile threads tangle, the fabric
  is ruined. When execution threads interfere with each other through
  unsynchronized shared-state access, the program produces incorrect
  results. "Thread safety" is the property of code that will not tangle
  when accessed by multiple threads simultaneously. The metaphor makes
  the danger intuitive: tangled threads are a mess that is hard to
  untangle.

## Where It Breaks

- **Threads do not weave** -- textile threads are physically interlocked
  by the loom in a structured pattern (warp and weft). Execution threads
  are interleaved by the OS scheduler in a pattern that is essentially
  unpredictable from the programmer's perspective. The weaving metaphor
  implies structure and intentionality in how threads combine; the reality
  is nondeterministic scheduling. A loom produces the same fabric every
  time. Running the same multithreaded program twice can produce different
  interleavings and, if the code is not thread-safe, different results.
- **Threads share state; textile threads do not** -- physical threads in
  fabric are independent objects that happen to be near each other.
  Execution threads share memory, file descriptors, and other process
  resources. The textile metaphor provides no vocabulary for this sharing,
  which is the source of nearly every concurrency bug. "Thread safety"
  is a compound that makes sense only in the computing domain -- textile
  threads cannot be "unsafe" in the way execution threads can.
- **The metaphor obscures the scheduler** -- in weaving, the loom
  determines how threads interact. In computing, the OS scheduler
  determines how threads are interleaved on CPU cores. The textile
  metaphor makes the scheduler invisible: we talk about threads as if
  they run independently, but their behavior depends entirely on a
  component the metaphor does not name. This is why reasoning about
  concurrency is so difficult -- the metaphor suggests autonomous
  threads when the reality is mediated execution.
- **"Lightweight" threads undermine the metaphor** -- the distinction
  between kernel threads, user-space threads (green threads), and
  coroutines maps poorly onto textiles. A thread is a thread in fabric;
  there is no "lightweight thread" that is somehow less of a thread. The
  computing domain's proliferation of thread-like abstractions
  (goroutines, fibers, virtual threads) stretches the metaphor past its
  structural limits. The textile source domain has no vocabulary for
  "a thing that is like a thread but cheaper."
- **The metaphor died into the API** -- programmers creating
  `std::thread` or `threading.Thread` do not think about looms or
  spinning wheels. "Thread" is experienced as a primitive technical term
  meaning "unit of concurrent execution." The textile origin surfaces
  only in explanatory contexts and the occasional etymology note.

## Expressions

- "Multithreading" -- running multiple threads of execution, the direct
  analog of weaving multiple threads into fabric
- "Thread pool" -- a pre-created collection of threads waiting for work,
  mixing textile and aquatic metaphors
- "Thread safety" -- the property of being safe for concurrent thread
  access, a term that only makes sense within the computing metaphor
- "Spinning up a thread" -- creating a new thread, borrowing from
  textile fiber production
- "Thread starvation" -- a thread unable to get scheduled, mixing the
  thread metaphor with biological need
- "Single-threaded" -- executing on one thread only, like a fabric made
  of a single strand (which is not fabric at all -- rope, perhaps)
- "Thread of execution" -- the full form, now almost never used, that
  preserves the metaphor's textile origin

## Origin Story

The use of "thread" for a sequential flow of control appears in computing
literature from the late 1960s, though the exact origin is difficult to
pin down. The term was likely influenced by the existing English idiom
"thread of argument" (tracing back to the Greek myth of Theseus following
Ariadne's thread through the labyrinth) as much as by direct textile
analogy. By the time POSIX threads (pthreads) were standardized in 1995
(IEEE Std 1003.1c), "thread" was the universally accepted term.

The textile metaphor proved generative. It spawned "fiber" (a lighter-
weight thread -- fibers are thinner than threads in textiles), "spinlock"
(a lock where a thread "spins" waiting), and indirectly influenced Go's
"goroutine" naming (which deliberately broke from the thread metaphor to
signal different semantics). Java's `Thread` class (1996) and C++'s
`std::thread` (2011) cemented the term in the two most widely used
systems programming languages.

## References

- IEEE Std 1003.1c-1995, "POSIX Threads" (pthreads)
- Dijkstra, E.W. "Cooperating Sequential Processes," 1965 -- early
  formalization of concurrent execution
- Butenhof, D.R. *Programming with POSIX Threads*, Addison-Wesley, 1997
- Herlihy, M. & Shavit, N. *The Art of Multiprocessor Programming*,
  Morgan Kaufmann, 2008
