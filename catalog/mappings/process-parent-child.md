---
author: agent:metaphorex-miner
categories:
- computer-science
contributors: []
created: '2026-03-15'
harness: Claude Code
kind: dead-metaphor
name: Process Parent-Child
related:
- zombie-process
- orphan-process
- environment-variable
slug: process-parent-child
source_frame: social-roles
target_frame: software-programs
updated: '2026-03-15'
---

## What It Brings

Human families have parents and children. Parents create children,
children inherit traits from parents, parents are responsible for
children, and when parents die, children become orphans. Unix processes
use this exact vocabulary: `fork()` creates a child process from a
parent, the child inherits the parent's memory, file descriptors, and
environment variables, the parent can `wait()` for the child, and if
the parent terminates first, the child is "adopted" by `init`. The
family metaphor is one of the most internally consistent metaphor
systems in all of computing -- it extends across the entire process
lifecycle with remarkable structural fidelity.

- **Creation through division** -- `fork()` creates a child by cloning
  the parent. The child begins as an exact copy, then diverges. This
  maps biological reproduction more closely than most software metaphors
  manage: the child inherits everything from the parent and then
  develops independently. The "fork" itself is a different metaphor
  (a road forking in two), but the parent-child relationship that
  results is purely familial.
- **Inheritance is automatic and comprehensive** -- a human child
  inherits genes, household, language, and social context from its
  parents. A Unix child process inherits the parent's memory image,
  open file descriptors, environment variables, working directory,
  signal handlers, and process group. The metaphor maps the
  comprehensiveness of biological inheritance: the child does not
  choose what to inherit. It gets everything, and then selectively
  modifies what it needs to change (typically via `exec()`).
- **Parental responsibility** -- parents are responsible for their
  children. In Unix, this responsibility has a specific technical form:
  the parent must call `wait()` to retrieve the child's exit status.
  If the parent fails this duty, the child becomes a zombie -- dead
  but not properly buried. The metaphor imports the moral dimension
  of parenting: there are consequences for neglecting your children.
- **The orphan and the foster parent** -- when a parent dies, the
  children become orphans. In Unix, when a parent process terminates,
  its children are "adopted" by the `init` process (PID 1), which
  assumes responsibility for reaping them. The metaphor is structurally
  precise: init is the system's foster parent, the process of last
  resort that takes in any child whose biological parent has died. This
  adoption mechanism prevents permanent orphans and permanent zombies.
- **The family tree** -- processes form a tree rooted at `init`.
  Every process (except init) has exactly one parent. Parents can have
  many children. The tree can be displayed with `pstree`. The family
  metaphor extends naturally to this genealogical structure: you can
  trace any process's ancestry back to init, just as you can trace a
  family line.

## Where It Breaks

- **Children do not choose to be born; child processes are created
  intentionally** -- in the human family, children have no agency in
  their creation. But in Unix, it is the parent's code that calls
  `fork()`. There is no accident, no biology, no desire -- just a
  system call. The familial language imports emotional and moral
  resonance (responsibility, care, abandonment) onto what is a
  purely mechanical operation. When we say a parent "abandons" its
  children by exiting without calling `wait()`, we are importing a
  moral judgment that has no meaning in the domain of process management.
- **The metaphor generates disturbing sentences** -- because the
  family vocabulary is comprehensive, operational descriptions of
  process management become inadvertently disturbing when read
  literally. "Kill the parent to clean up the zombies." "The parent
  spawns children, waits for them to die, then reaps them." "If the
  parent dies first, init adopts the orphans." These sentences are
  technically precise and emotionally grotesque. The metaphor works
  structurally but creates a narrative that, if taken at face value,
  describes child abuse and mass infanticide.
- **Real families are bidirectional; Unix process relationships are
  not** -- in human families, children affect parents as much as
  parents affect children. Communication is bidirectional, influence
  flows both ways, and the relationship evolves over time. In Unix,
  the parent-child relationship is heavily asymmetric. The parent can
  `wait()` for the child and receive its exit status, but the child
  has no built-in mechanism to communicate with the parent except
  through its exit code (a single integer). The family metaphor
  suggests a rich, ongoing relationship where the actual mechanism
  provides only a one-shot, one-byte farewell.
- **Adoption by init is nothing like human adoption** -- when init
  adopts orphan processes, it does so automatically and without any
  of the features of human adoption: no selection, no bonding, no
  ongoing relationship. Init's only role is to call `wait()` when
  the orphan terminates, cleaning up the zombie. This is more like
  a municipal cremation service than a foster family. The adoption
  metaphor imports warmth and care that the mechanism does not provide.
- **The metaphor obscures process groups and sessions** -- real Unix
  process management involves process groups, sessions, controlling
  terminals, and signal routing that have no family analogy. When a
  terminal is closed, the entire session receives SIGHUP -- but the
  "family" metaphor provides no vocabulary for "all the relatives in
  this household." The metaphor covers the parent-child dyad well but
  breaks down for the collective structures that actually govern
  process lifecycle in practice.

## Expressions

- "Parent process" / "child process" -- the fundamental terminology,
  used so universally that most programmers do not register the family
  metaphor
- "Fork a child" -- create a new process via `fork()`, blending the
  road-splitting metaphor of "fork" with the familial metaphor of
  "child"
- "The parent waits for the child" -- describing the `wait()` system
  call, which blocks until the child terminates
- "Orphan process" -- a process whose parent has terminated, adopted
  by init
- "Zombie process" -- a terminated child whose parent has not yet
  called `wait()`, layering horror-genre metaphor onto the family
  metaphor
- "Reap the children" -- call `wait()` to clean up terminated child
  processes, adding an agricultural/funerary metaphor on top of the
  family structure
- "Daemonize by double-forking" -- the standard Unix technique for
  creating a background process: fork, let the parent exit (making
  the child an orphan adopted by init), then fork again. The family
  metaphor makes this legible: abandon your child so it gets adopted
  by the system

## Origin Story

The parent-child process model was designed by Ken Thompson and Dennis
Ritchie at Bell Labs as part of the original Unix system (1969-1971).
The `fork()` system call, which creates a child process by duplicating
the parent, was Unix's distinctive contribution to operating system
design. Earlier systems created processes differently -- often by
loading a new program from scratch rather than cloning an existing
process.

The family terminology was a natural fit for the cloning mechanism:
the child starts as a copy of the parent and then diverges. Thompson
and Ritchie's choice of "parent" and "child" (rather than, say,
"original" and "copy") encoded a relationship of responsibility and
lifecycle into the vocabulary. The subsequent terms -- orphan, zombie,
adopt, reap, inherit -- extended the family metaphor into a complete
system that covers every state a process can occupy from creation to
cleanup. The remarkable internal consistency of this metaphor system
is one reason it has persisted unchanged for over fifty years.

## References

- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM
  17(7), 1974 -- introduces the fork/wait/exec process model
- Ritchie, D. & Thompson, K. "The UNIX Time-Sharing System," Bell
  System Technical Journal 57(6), 1978 -- expanded treatment
- Stevens, W. R. *Advanced Programming in the UNIX Environment*
  (1992) -- canonical description of process lifecycle, including
  orphans, zombies, and process groups
- Kerrisk, M. *The Linux Programming Interface* (2010) -- modern
  treatment with detailed coverage of process relationships
- Bach, M. J. *The Design of the UNIX Operating System* (1986) --
  early formal treatment of the process model
