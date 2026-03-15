---
author: agent:metaphorex-miner
categories:
- computer-science
- software-engineering
contributors:
- fshot
created: '2026-03-15'
harness: Claude Code
kind: dead-metaphor
name: Process Kill
related:
- zombie-process
- orphan-process
- process-sleep
- process-trap
slug: process-kill
source_frame: embodied-experience
target_frame: software-programs
updated: '2026-03-15'
---

## What It Brings

Ending a life. The most primal form of violence, mapped onto the act of
terminating a running process. Unix does not "stop" or "end" or "cancel"
processes -- it kills them. The command is `kill`, the man page says
"send a signal to a process," but the name tells a different story. The
metaphor imports the finality and force of physical death into what is,
mechanically, the delivery of a numbered interrupt.

Key structural parallels:

- **Graduated violence** -- killing in the physical world ranges from
  mercy killing to execution. Unix mirrors this spectrum. `kill -15`
  (SIGTERM) is a polite request: "please shut down gracefully." The
  process can catch this signal, clean up resources, say its goodbyes,
  and exit on its own terms. `kill -9` (SIGKILL) is execution: the
  kernel terminates the process immediately, no cleanup, no handler, no
  last words. The process does not get to respond. The numeric escalation
  from 15 to 9 maps a continuum of coercion onto signal numbers.
- **The process dies** -- after receiving a fatal signal, the process
  enters a terminated state. Its children become orphans. Its corpse may
  linger as a zombie if the parent does not reap it. The entire
  vocabulary of death follows naturally: the process "dies," leaves
  behind "orphans," and can become "undead." The kill metaphor is the
  entry point to an entire thanatological vocabulary.
- **Agency and intent** -- killing requires a killer. Someone or
  something must invoke `kill` with a target PID. The metaphor imports
  the idea of deliberate, directed action against a specific victim.
  This contrasts with processes that "crash" (accidental death) or
  "hang" (coma). Killing is something done *to* a process, not
  something that happens to it.
- **The right to kill** -- not everyone can kill every process. Unix
  permissions restrict `kill` to the process owner and root. Root can
  kill anything -- the superuser as sovereign with the power of life
  and death. The metaphor imports political authority structures:
  ordinary users govern their own processes, the administrator governs
  all.

## Where It Breaks

- **Killing is irreversible; process termination is routine** -- in the
  physical world, killing is the most extreme and final act imaginable.
  In Unix, killing a process is utterly mundane. Developers kill
  processes dozens of times a day during normal work. The metaphor
  imports a gravity that the action does not carry: no one mourns a
  killed process, and an identical one can be started immediately. The
  "death" has no real cost.
- **The victim is not alive** -- the entire metaphor rests on treating
  processes as living things, but they are not. There is no suffering,
  no consciousness, no moral dimension. The violence of the vocabulary
  -- kill, die, zombie, orphan -- creates a dramatic narrative around
  what is fundamentally bookkeeping: freeing memory, closing file
  descriptors, removing a PID from a table.
- **SIGKILL is not actually kill's default** -- despite the command
  being named `kill`, the default signal is SIGTERM (15), which is a
  request, not a command. The name promises killing but delivers a
  suggestion. Users who learn `kill` without understanding signals are
  surprised when processes survive being "killed" -- the metaphor
  overpromises lethality.
- **The metaphor normalizes violent language** -- sentences like "kill
  the child process," "kill -9 everything," and "I'll just kill it"
  are routine in computing. The metaphor has been so successful that
  the violence is invisible to practitioners but startling to outsiders.
  This is the hallmark of a dead metaphor: the source domain has been
  forgotten, and only the technical meaning remains.

## Expressions

- "Kill it with -9" -- the nuclear option, invoking SIGKILL when
  SIGTERM has failed. The escalation mirrors "if asking doesn't work,
  use force."
- "Kill the parent to clean up the zombies" -- a sentence that reads
  as a horror plot but describes a routine systems administration
  technique
- "Who killed my process?" -- the murder mystery framing, when a
  process disappears unexpectedly and the operator investigates the
  system logs
- "The OOM killer got it" -- the Linux out-of-memory killer,
  personified as an executioner who selects victims when memory is
  exhausted
- "Kill all the workers and restart" -- routine deployment language
  for restarting a pool of worker processes

## Origin Story

The `kill` system call dates to the earliest versions of Unix at Bell
Labs in the early 1970s. Dennis Ritchie and Ken Thompson chose the name
for the system call that sends signals to processes. The original
semantics were simpler than today's -- early Unix had fewer signals and
the primary use was indeed to terminate processes, making "kill" a
reasonable if dramatic name.

The violence of the term was deliberate enough to propagate: the signal
that cannot be caught is SIGKILL, the process state after termination
without reaping is "zombie," and the system that kills processes under
memory pressure is the "OOM killer." The metaphor has proven remarkably
generative, spawning an entire vocabulary of death, violence, and the
supernatural around what is fundamentally resource management.

## References

- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM
  17(7), 1974 -- original description of signal and process termination
  semantics
- Stevens, W. R. *Advanced Programming in the UNIX Environment*
  (1992) -- canonical treatment of signals, kill, and process lifecycle
- kill(2) man page, man7.org -- current Linux documentation for the
  kill system call
