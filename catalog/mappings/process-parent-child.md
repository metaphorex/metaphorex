---
slug: process-parent-child
name: "Process Parent-Child"
kind: dead-metaphor
source_frame: social-roles
target_frame: software-programs
categories:
  - computer-science
  - software-engineering
  - systems-thinking
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - orphan-process
  - zombie-process
  - process-kill
  - process-sleep
  - environment-variable
---

## What It Brings

The most fundamental human social structure -- parent and child -- mapped
onto the relationship between a process and the processes it creates. In
Unix, `fork()` creates a child process that is a near-exact copy of its
parent. The child inherits the parent's memory, file descriptors,
environment, and working directory. The parent can wait for the child to
finish, and if it neglects this duty, the child becomes a zombie. If the
parent dies first, the child becomes an orphan. The family metaphor is
one of the most internally consistent metaphor systems in all of computing.

Key structural parallels:

- **Creation through division** -- biological reproduction creates a new
  organism from an existing one, carrying forward the parent's traits.
  `fork()` creates a new process by duplicating the parent, and the child
  begins life as an almost-identical copy. The parallel is remarkably
  precise: the child starts with everything the parent has, then diverges
  through its own execution path. The naming of `fork()` itself
  (a branching metaphor) reinforces the idea of a single lineage
  splitting into two.
- **Inheritance of traits** -- children inherit their parent's genetic
  material, temperament, and sometimes social position. A child process
  inherits file descriptors, environment variables, signal handlers,
  the current working directory, and resource limits. The biological
  metaphor makes these technical details intuitive: of course a child
  has what its parent had. The metaphor also extends to what is *not*
  inherited -- process locks, pending alarms, and memory locks are not
  passed to the child, just as acquired skills are not genetically
  transmitted.
- **The parent's duty to wait** -- responsible parents watch over their
  children and acknowledge their completion. In Unix, a parent must call
  `wait()` or `waitpid()` to collect the child's exit status. This act
  is called "reaping" -- itself a metaphor from agriculture layered onto
  the family metaphor. If the parent does not wait, the child's remains
  linger as a zombie. If the parent dies without waiting, the child is
  adopted by init (PID 1), the system's universal foster parent.
- **The process tree as a family tree** -- the `pstree` command displays
  all running processes as a genealogical tree, with init at the root.
  Every process (except init) has exactly one parent, and may have zero
  or more children. This tree structure mirrors a patrilineal family
  tree, and the metaphor is so deeply embedded that "process tree" is
  experienced as a literal description rather than a figure of speech.
- **The complete lifecycle** -- the family metaphor covers the entire
  process lifecycle with uncanny consistency: a process is born (fork),
  inherits its parent's traits, lives (executes), may spawn its own
  children, dies (exit), and must be mourned by its parent (wait). It
  can become an orphan (parent dies first) or a zombie (dies but is
  not reaped). No other metaphor system in computing covers so many
  states with such coherence.

## Where It Breaks

- **Processes are copies; children are not** -- a human child is a new
  combination of genetic material from two parents, developing into a
  unique individual from conception. A forked process begins as a
  byte-for-byte copy of a single parent, including its instruction
  pointer. The metaphor imports the concept of parentage but not the
  concept of individuation through genetic recombination. Processes
  have one parent, not two, and start as clones, not as novel beings.
- **The family metaphor normalizes violence** -- within the family
  frame, parents routinely "kill" their children (send termination
  signals), children become "zombies" (undead), and the system "reaps"
  the dead. Reading Unix process management documentation literally
  produces sentences that are grotesque: "the parent kills its children
  and waits for them to die." The family metaphor makes the process
  lifecycle intuitive, but it does so by borrowing emotional gravity
  from human kinship and then treating it casually.
- **There is no childhood development** -- human children grow, learn,
  and change over years. A child process has no developmental arc. It
  is fully capable from the moment of creation and executes its task
  immediately. The parent-child metaphor implies a nurturing
  relationship and a period of dependency, but the child process is
  independent from its first instruction. The only dependency is the
  bureaucratic one: the parent must collect the exit status.
- **Adoption by init is not really adoption** -- when a parent dies,
  init "adopts" the orphaned children. But init does not supervise,
  nurture, or interact with the orphan in any meaningful way. Its sole
  function is to call `wait()` when the orphan terminates, preventing
  zombie accumulation. The metaphor imports the warmth of adoption but
  the reality is janitorial: init is not a foster parent, it is a
  cleanup service.
- **The metaphor assumes a nuclear family** -- the parent-child model
  in Unix is strictly hierarchical and single-parent. There is no
  concept of co-parenting, extended family, or community child-rearing.
  Process groups and sessions add some complexity, but the core model
  is one parent per child. The metaphor naturalizes a specific family
  structure as the only possible one.

## Expressions

- "The parent forks a child" -- the canonical creation expression,
  combining the branching metaphor (fork) with the family metaphor
- "Wait for the child to finish" -- the parent's responsibility to
  collect the exit status, mapping parental duty onto process management
- "The child inherits the parent's file descriptors" -- biological
  inheritance language for a technical copying operation
- "Kill the parent and the children become orphans" -- a sentence that
  is technically precise and emotionally disturbing in equal measure
- "The child process called exec and became a completely different
  program" -- a developmental narrative: the child starts as a copy of
  the parent but transforms into something entirely new, like a child
  choosing its own path in life
- "Process tree" -- the genealogical display of parent-child
  relationships, so thoroughly dead as a metaphor that no one sees
  "tree" or "family" in it anymore

## Origin Story

The parent-child process model was designed by Ken Thompson and Dennis
Ritchie at Bell Labs as part of the original Unix system in the early
1970s. The `fork()` system call, which creates the parent-child
relationship, was described in Thompson and Ritchie's seminal 1974 CACM
paper "The UNIX Time-Sharing System." The paper uses "parent" and "child"
terminology matter-of-factly, as if the family metaphor were self-evident.

The metaphor's coherence was not planned but emergent. As Unix evolved,
different engineers independently reached for family terminology to
describe process states: "orphan" for a process whose parent died,
"zombie" for a terminated process not yet reaped, "adoption" for init
taking over orphans. The result is a metaphor system that feels designed
but was actually accumulated -- each term was chosen because the family
analogy was the most natural way to describe the relationship, and the
terms happened to compose into a consistent whole.

## References

- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM
  17(7), 1974 -- introduces fork(), parent/child terminology
- Stevens, W. R. *Advanced Programming in the UNIX Environment* (1992)
  -- canonical treatment of process relationships, orphans, and zombies
- Kerrisk, M. *The Linux Programming Interface* (2010) -- comprehensive
  modern treatment of process creation and lifecycle
- man7.org `fork(2)`, `wait(2)` -- Linux man pages for the core system
  calls that implement the parent-child relationship
