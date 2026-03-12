---
slug: race-condition
name: "Race Condition"
kind: dead-metaphor
source_frame: competition
target_frame: software-programs
categories:
  - software-engineering
  - systems-thinking
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - heisenbug
  - software-rot
---

## What It Brings

A footrace where the outcome depends entirely on who crosses the
finish line first -- mapped onto concurrent systems where the result
depends on the relative timing of operations that were never meant to
compete. The metaphor takes an accidental ordering dependency and makes
it legible by framing it as a contest, even though the "contestants"
(threads, processes, signals) do not know they are racing and the
"prize" (a shared resource) is corrupted by the competition itself.

Key structural parallels:

- **Outcome depends on arrival order** -- in a footrace, first place
  goes to whoever reaches the finish line first. In a race condition,
  the program's behavior depends on which thread or process reaches a
  critical section first. The metaphor captures the essential property:
  the system is nondeterministic not because the components are
  random, but because their relative timing is uncontrolled. The same
  inputs can produce different outputs depending on who wins the race.
- **The competition is unintended** -- footraces are designed to be
  competitive; race conditions are not. The metaphor highlights the
  irony: components that were supposed to cooperate are instead
  competing for access to shared state, and the program's correctness
  depends on an ordering that no one specified. The race was never
  meant to happen, which is exactly what makes it a bug.
- **Speed masks the problem** -- in a footrace, a close finish is
  exciting but the outcome is still valid. In a race condition, a
  "close finish" is where the bug manifests: when two operations
  arrive at nearly the same time, one overwrites the other's work, or
  both read stale data. On faster or slower hardware, the timing
  changes and the race may never manifest -- which is why race
  conditions are notoriously difficult to reproduce.
- **No single component is wrong** -- in a footrace, both runners are
  doing exactly what they are supposed to do: running as fast as they
  can. In a race condition, each thread is executing correct code in
  isolation. The bug exists only in the interaction, in the space
  between components that no one owns. The metaphor captures this
  distributed blame: the race condition is nobody's fault and
  everybody's problem.

## Where It Breaks

- **Races have winners; race conditions have only losers** -- a
  footrace produces a satisfying outcome: someone wins, someone loses,
  the result is clear. A race condition produces corruption, data loss,
  or undefined behavior. There is no winner. The competitive framing
  imports a structure (winner/loser, fair contest) that does not exist
  in the technical domain. The "race" is not a contest between equals
  but an uncoordinated collision.
- **The metaphor is so embedded it has become invisible** -- most
  engineers do not experience "race condition" as a metaphor at all.
  It has passed through the dead-metaphor threshold where the source
  domain (athletic competition) no longer activates in the listener's
  mind. This means the metaphor's structural implications -- that
  timing is a contest, that components are adversaries -- shape
  thinking without being examined. The framing may subtly discourage
  cooperative models of concurrency (like CSP or actors) in favor of
  competitive ones (locks, semaphores, priority).
- **Races are observable; race conditions often are not** -- you can
  watch a footrace and see the outcome. Race conditions are
  notoriously difficult to observe: they depend on timing windows of
  microseconds, they may manifest only under specific load conditions,
  and the act of observing them (adding logging, attaching a debugger)
  changes the timing enough to make them disappear. The metaphor
  imports the visibility of athletic competition into a domain
  characterized by invisibility.
- **The metaphor does not scale to complex interleavings** -- a
  footrace has a clear start, a clear finish, and a linear track. Real
  concurrency bugs involve multiple shared resources, nested locks,
  reentrant calls, and interleaving sequences that grow combinatorially
  with the number of threads. The race metaphor handles two-thread
  scenarios well but becomes strained when describing deadlocks,
  livelocks, priority inversions, and ABA problems.

## Expressions

- "There's a race condition between the read and the write" -- the
  canonical diagnostic, identifying two operations that should be
  atomic but are not
- "Data race" -- the more specific term for unsynchronized access to
  shared memory, distinguished from the broader "race condition" in
  formal concurrency theory
- "Race to the bottom" -- borrowed from economics, occasionally used
  to describe cascading concurrency failures
- "Time-of-check to time-of-use" (TOCTOU) -- a specific race
  condition pattern where a check (e.g., file permissions) is
  invalidated before the subsequent action, named with its own
  temporal metaphor
- "Thread-safe" -- the defensive counterpart, describing code that
  cannot lose the race because it has eliminated the competition
  through synchronization
- "It works on my machine" -- the indirect expression of a race
  condition, where different hardware timing masks or reveals the bug

## Origin Story

The term "race condition" predates software. It originates in
electronics engineering, where it described the behavior of logic
circuits whose output depended on the relative timing of input
signals arriving through different paths. If two signals "raced" to
reach a gate, the output was indeterminate. The term appears in
electronics literature from the 1950s and 1960s.

The concept migrated to software with the advent of multiprogramming
in the 1960s. Edsger Dijkstra's 1965 paper "Solution of a Problem in
Concurrent Programming Control" addressed what we now call race
conditions, though he did not use that exact term. The term became
standard in operating systems textbooks through the 1970s and 1980s,
appearing in Andrew Tanenbaum's *Operating Systems: Design and
Implementation* (1987) and subsequent editions.

Today, "race condition" is so deeply embedded in computing vocabulary
that it is used without metaphorical awareness. The MITRE CWE
(Common Weakness Enumeration) catalogs race conditions as CWE-362,
treating the term as purely technical rather than metaphorical.

## References

- Dijkstra, E. W. "Solution of a Problem in Concurrent Programming
  Control," *Communications of the ACM* 8(9) (1965) -- foundational
  work on mutual exclusion
- Tanenbaum, A. S. *Modern Operating Systems*, 4th ed. (2014) --
  standard textbook treatment of race conditions
- Netzer, R. H. B. & Miller, B. P. "What Are Race Conditions?"
  *ACM Letters on Programming Languages and Systems* 1(1) (1992) --
  formal definition distinguishing data races from general race
  conditions
- MITRE CWE-362: "Concurrent Execution using Shared Resource with
  Improper Synchronization" -- the institutional classification
