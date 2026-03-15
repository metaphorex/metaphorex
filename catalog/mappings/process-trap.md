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
name: Process Trap
related:
- process-kill
- process-sleep
- zombie-process
slug: process-trap
source_frame: embodied-experience
target_frame: software-programs
updated: '2026-03-15'
---

## What It Brings

A hunting device -- a mechanism placed in the path of prey to catch it
when it arrives. In Unix, the shell builtin `trap` registers a handler
for a specified signal: when that signal arrives, it is "caught" and
the handler executes instead of the default behavior. The metaphor maps
the patience and specificity of hunting onto defensive programming: you
anticipate what might come, prepare a response, and wait.

Key structural parallels:

- **Preparation before the event** -- a hunter sets a trap before the
  animal arrives. A programmer sets a trap before the signal is sent.
  In both cases, the preparation must happen in advance; you cannot
  trap something after it has already passed. `trap 'cleanup' EXIT`
  must be declared before the script exits. The metaphor captures the
  temporal logic of defensive programming: anticipate, prepare, then
  proceed.
- **Specificity of target** -- a physical trap is set for a particular
  kind of animal, in a particular location, baited for particular
  behavior. A signal trap is set for a specific signal number or name:
  `trap '' SIGINT` catches only interrupt signals, ignoring everything
  else. The metaphor imports the idea that trapping is selective and
  deliberate, not a blanket defense.
- **Catching as interception** -- the trapped signal is "caught"
  before it can cause its default damage. SIGTERM's default action is
  to kill the process, but a trap handler can intercept it, run
  cleanup code, and then exit gracefully. The physical metaphor is
  precise: the trap catches the signal mid-flight, preventing it from
  reaching its intended target (the process's default behavior).
- **Hardware traps** -- the metaphor extends below the shell into
  hardware. CPU exceptions (division by zero, page faults, invalid
  opcodes) are called "traps" -- the processor "traps" the exceptional
  condition and diverts execution to an exception handler. The hunting
  metaphor unifies software signal handling and hardware exception
  handling under a single conceptual frame.

## Where It Breaks

- **Traps in hunting are hostile; traps in code are protective** --
  a physical trap is set to harm or capture prey. A signal trap in
  a shell script is defensive: it protects the program by catching
  signals that would otherwise terminate it abruptly. The hunter's
  intent is predatory; the programmer's intent is protective. The
  metaphor imports aggression where the reality is self-defense.
- **The hunter and the prey are separate; the trapper and the trapped
  are the same** -- in hunting, the trap-setter and the thing being
  trapped are different entities with opposing interests. In signal
  handling, the process traps signals sent to itself. It is both
  hunter and prey, which collapses the adversarial structure that
  gives the hunting metaphor its force.
- **Traps are passive; trap handlers are active** -- a physical trap
  sits and waits. A signal trap handler executes arbitrary code: it
  can write files, send messages, spawn processes, or even ignore
  the signal entirely. The metaphor suggests a mechanical catch, but
  the reality is a programmable response. The "trap" is less like a
  snare and more like a sentry with complex standing orders.
- **The metaphor is dead in everyday usage** -- most shell programmers
  use `trap` without thinking of hunting. The word has become a pure
  technical verb meaning "register a signal handler." The hunting
  source domain contributes nothing to most practitioners'
  understanding of the feature; they learn `trap` as syntax, not as
  metaphor.

## Expressions

- "Trap SIGINT to clean up temp files" -- the canonical usage,
  registering a cleanup handler for the interrupt signal
- "Set a trap for EXIT" -- preparing code to run when the script
  terminates, regardless of how. The hunting language ("set a trap")
  is preserved intact.
- "The signal was caught" -- the complement of trapping, where the
  passive construction mirrors the animal caught in the snare
- "Trap and ignore" -- `trap '' SIGTERM` registers an empty handler,
  making the process immune to the signal. The trap catches the signal
  and does nothing with it -- catch and release.
- "Hardware trap" -- a CPU exception that diverts execution to a
  kernel handler, extending the metaphor from software signals to
  processor-level events
- "It fell through because nobody trapped it" -- when a signal
  reaches its default handler because no trap was set, echoing the
  hunting scenario of prey passing through an unset trap location

## Origin Story

The `trap` command appears in the Bourne shell (sh), written by
Stephen Bourne at Bell Labs for Version 7 Unix (1979). The concept of
trapping signals was present in Unix from its earliest versions -- the
ability to catch and handle signals was part of the process model
designed by Thompson and Ritchie.

The hunting metaphor predates Unix. Hardware "traps" were used in
computing terminology as early as the 1960s, referring to processor
mechanisms that catch exceptional conditions. The PDP-11 (the machine
Unix was first developed on) used "trap" for its exception handling
mechanism, and Unix inherited the term. The shell's `trap` builtin
applied the same metaphor at a higher level of abstraction: trapping
software signals rather than hardware exceptions.

The word "trap" is one of computing's more vivid surviving metaphors.
Unlike "kill" (which has become so common it is invisible) or "sleep"
(which is entirely intuitive), "trap" retains a slight strangeness --
enough that newcomers pause at it, which makes it technically a dying
metaphor rather than a fully dead one. But among experienced Unix
users, the hunting connotation is thoroughly extinct.

## References

- Bourne, S. R. "The UNIX Shell," Bell System Technical Journal,
  1978 -- original description of the Bourne shell including trap
- Stevens, W. R. *Advanced Programming in the UNIX Environment*
  (1992) -- canonical treatment of signal handling and trap semantics
- trap(1p) man page, POSIX specification -- formal definition of
  the trap shell builtin
- Intel 64 and IA-32 Architectures Software Developer's Manual --
  hardware trap and exception handling mechanisms
