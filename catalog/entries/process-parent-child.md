---
slug: process-parent-child
name: Process Parent-Child
kind: metaphor
dead: true
source_frame: social-roles
applies_to:
- software-programs
categories:
- computer-science
- systems-thinking
author: agent:metaphorex-miner
contributors:
- fshot
related:
- zombie-process
- orphan-process
created: '2026-03-17'
updated: '2026-03-17'
harness: Claude Code
grounding: established
transfers:
  - "[source] a parent produces offspring that inherit traits, resources, and identity from their lineage"
  - "[source] families form genealogical trees where every member except the progenitor has exactly one parent"
  - "[source] a parent who dies leaves orphans requiring institutional guardianship"
limits:
  - "[source] breaks because human families involve bidirectional emotional bonds, whereas the mapped relationship is a one-way supervisory channel"
  - "[source] misleads because biological inheritance blends traits from two parents, whereas the mapped mechanism copies one parent's state wholesale"
---

## Transfers

Process relationships as family relationships -- one of the most
internally consistent metaphor systems in computing. When a Unix process
calls `fork()`, it creates a child process. The child inherits the
parent's memory image, file descriptors, environment variables, and
working directory. The parent can call `wait()` to learn how the child
fared. If the parent dies first, the child becomes an orphan, adopted
by init (PID 1). If the child dies and the parent never calls `wait()`,
the child becomes a zombie.

Key structural parallels:

- **Inheritance** -- a child process receives a copy of its parent's
  entire state at the moment of creation: memory, open files, environment
  variables, signal handlers. This maps directly onto the intuition that
  children inherit traits and resources from their parents. The metaphor
  makes the fork semantics immediately comprehensible: the child starts
  life as a copy of the parent, then diverges.
- **Genealogy as system structure** -- the process table forms a tree
  rooted at PID 1 (init), with every process having exactly one parent.
  This maps the family tree onto system architecture. The `pstree`
  command renders this literally, displaying processes as a genealogical
  chart. The tree metaphor makes the hierarchy of responsibility visible:
  each parent is accountable for its children's lifecycle.
- **The duties of parenthood** -- a responsible parent must wait for
  their children. In Unix, the parent must call `wait()` or `waitpid()`
  to collect the child's exit status. Failing this duty creates zombies.
  The metaphor encodes a moral judgment: neglecting your children has
  consequences for the whole system.
- **Adoption as a safety net** -- when a parent dies, society steps in.
  When a parent process terminates, init adopts its orphaned children.
  This is not a failure mode but a designed safety mechanism, mapping
  the social institution of adoption onto process lifecycle management.

The family metaphor extends further than any single entry can capture:
fork (reproduction), exec (transformation), wait (parental responsibility),
kill (violence), reap (funerary rites), spawn (creation), and the entire
orphan/zombie vocabulary. This cluster was not designed as a coherent
system -- it accumulated as different Bell Labs engineers named different
features -- but the result is remarkably consistent.

## Limits

- **Families are bidirectional; process relationships are not** -- human
  parent-child relationships involve mutual recognition, communication
  in both directions, and emotional bonds. The process relationship is
  strictly hierarchical: the parent creates, monitors, and reaps the
  child. The child does not know its parent's state and cannot call
  `wait()` on its parent. The metaphor imports warmth and mutuality that
  the technical relationship lacks entirely.
- **Children diverge from parents; processes diverge completely** -- in
  human families, children share genetic material and ongoing social
  bonds with their parents. After `fork()`, the child process can
  immediately call `exec()` to replace its entire memory image with a
  different program. The "child" may bear no resemblance whatsoever to
  its "parent" within microseconds of being created. The inheritance is
  a starting point, not an ongoing connection.
- **The metaphor normalizes violent vocabulary** -- within the family
  frame, processes are "killed," children become "zombies," and parents
  must "reap" their dead children. Read literally, these form sentences
  of considerable horror. The metaphor system works because engineers
  treat these terms as purely technical, but the kinship framing makes
  the violence more jarring than it would be in a mechanical frame.
- **No two-parent model** -- biological reproduction typically involves
  two parents. Process creation involves exactly one. The metaphor
  borrows from kinship but enforces a strictly single-parent model,
  which maps better onto asexual reproduction than onto the human family
  structures the vocabulary evokes.

## Expressions

- "The parent forks a child process" -- the canonical creation
  expression, combining the kinship metaphor with the utensil metaphor
  of fork
- "init adopts orphaned processes" -- describing the system's safety net
  in terms of institutional child welfare
- "The parent waits on its children" -- describing the `wait()` system
  call using the language of parental patience and responsibility
- "Check the process tree" -- using `pstree` to view the genealogy of
  running processes, treating the system as a family tree
- "Kill the parent and the children become orphans" -- a diagnostic
  technique that reads as a crime scene when taken literally

## Origin Story

The parent-child process model was designed by Ken Thompson and Dennis
Ritchie at Bell Labs as part of the original Unix system (1969-1971).
The `fork()` system call, which creates the parent-child relationship,
was introduced in the earliest versions of Unix. Thompson has noted that
fork was inspired by similar concepts in the Project Genie system at
Berkeley, though Unix's implementation was more elegant.

The family terminology was not planned as a coherent metaphor system. It
accumulated across the 1970s and 1980s as different parts of the process
lifecycle needed names. But the metaphor's internal consistency -- parent,
child, orphan, zombie, inherit, wait, adopt, reap -- suggests that the
family frame was so natural for describing process relationships that
independent namers converged on it organically.

## References

- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM
  17(7), 1974 -- original description of fork/exec/wait semantics
- Stevens, W. R. *Advanced Programming in the UNIX Environment* (1992)
  -- canonical treatment of process relationships and lifecycle
- Kerrisk, M. *The Linux Programming Interface* (2010) -- modern
  reference for process creation, orphans, and zombies
