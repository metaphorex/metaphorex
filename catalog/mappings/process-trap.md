---
slug: process-trap
name: "Process Trap"
kind: dead-metaphor
source_frame: hunting
target_frame: software-programs
categories:
  - computer-science
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - unix-pipe
---

## What It Brings

In Unix, the `trap` builtin catches signals before they can terminate or
disrupt a process. The metaphor imports the full logic of physical trapping:
you set a trap in advance, specifying what you want to catch and what should
happen when you catch it. The signal arrives like prey entering the snare,
and the trap handler executes -- the catch is made. The same vocabulary
extends to hardware traps (CPU interrupts triggered by exceptional
conditions) and, later, to exception handling in languages descended from
C's ecosystem.

Key structural parallels:

- **Setting a trap before the event** -- a hunter sets traps before prey
  arrives. A programmer sets signal traps before signals arrive. In both
  domains, the act is anticipatory: you must decide in advance what to
  catch and how to respond. `trap 'cleanup' EXIT` declares intent the way
  placing a snare declares intent -- the mechanism waits passively until
  triggered. This temporal structure (prepare, then wait, then act) is the
  metaphor's core contribution.
- **Specificity of the catch** -- traps are set for specific prey. You do
  not set a rabbit snare and expect to catch a deer. Similarly, `trap`
  handlers are registered for specific signals: SIGINT, SIGTERM, SIGHUP.
  Catching SIGINT does not catch SIGTERM. The metaphor imports the
  principle that defense must be targeted -- you must know what you are
  defending against.
- **The trap as interception** -- when prey triggers a trap, its natural
  trajectory (movement through the forest) is interrupted. When a signal
  triggers a trap handler, the process's normal execution is interrupted.
  In both cases, something was heading in one direction and the trap
  redirected it. The metaphor makes signal handling feel like a physical
  interception rather than an abstract control-flow transfer.
- **Defensive trapping** -- the computing usage emphasizes the defensive
  variant of trapping: catching something harmful before it causes damage.
  `trap 'rm -f $tmpfile' EXIT` ensures cleanup happens even if the process
  is killed. The trap is a safety mechanism, catching the destructive
  signal and performing orderly shutdown instead of abrupt termination.

## Where It Breaks

- **Signals are not agents; prey are** -- a rabbit has intent, behavior,
  and the ability to avoid traps. A Unix signal is a one-bit notification
  with no intelligence, no behavior, and no ability to evade. The hunting
  metaphor imports an adversarial dynamic (clever hunter vs. wary prey)
  where there is only a mechanical dispatch. SIGTERM does not "try" to
  kill the process; it is a notification that the process may choose to
  handle. The adversarial framing misleads when reasoning about signal
  delivery semantics.
- **Traps in computing are not destructive to the signal** -- a physical
  trap kills or immobilizes the prey. A signal trap handler intercepts the
  signal but the signal itself is not "destroyed" -- it was a notification,
  not an entity. After handling SIGINT, the process continues running. The
  metaphor suggests that catching something neutralizes it, but in
  computing the "catching" is really "responding to." A caught signal
  produces a response; a caught rabbit produces dinner. The outcomes are
  structurally different.
- **Multiple signals of the same type collapse** -- if two SIGINTs arrive
  while the handler is executing, the second may be lost (standard signals
  are not queued). In hunting, two rabbits do not collapse into one rabbit
  because you are already processing the first. The metaphor provides no
  intuition for signal coalescing, which is one of the subtlest bugs in
  signal-handling code.
- **The "trap" and "catch" vocabularies come from different eras** -- Unix
  `trap` (1970s) and Java/C++ `try/catch` (1980s-90s) use related but
  distinct hunting metaphors. A trap is passive (set and wait); a catch is
  active (something is thrown and you catch it). The evolution from trapping
  to throwing-and-catching shifted the metaphor from hunting to a ball game,
  but the two vocabularies are often conflated, creating confusion about
  whether exception handling is about anticipation (traps) or reflexes
  (catching).

## Expressions

- "Trap the signal" -- register a handler for a specific signal; pure
  hunting vocabulary
- "Caught SIGINT" -- the process intercepted the interrupt signal
- "Set a trap for EXIT" -- prepare a handler that fires when the process
  terminates
- "Hardware trap" -- a CPU interrupt triggered by an exceptional condition
  (division by zero, page fault); the trap is built into the silicon
- "Trap handler" -- the code that executes when a signal is caught;
  analogous to what the hunter does after checking the trap
- "Untrapped signal" -- a signal with no registered handler; like prey
  passing through territory with no snares set

## Origin Story

The `trap` command has been part of the Unix shell since the Bourne shell
(sh) in Version 7 Unix, 1979. The concept of trapping signals, however,
dates to hardware interrupt handling in the earliest computers. The PDP-11,
on which Unix was developed, used "trap" to describe the CPU's response to
exceptional conditions -- a usage that predates Unix itself.

The hunting metaphor was natural for hardware engineers: an unexpected
condition "triggers" a trap, just as an animal triggers a snare. Ken
Thompson and Dennis Ritchie extended this hardware vocabulary into software
when they designed Unix's signal mechanism. The shell's `trap` builtin
made the metaphor accessible to users, not just kernel programmers.

The later development of structured exception handling (C++ `try/catch`,
Java `throws`) shifted the dominant metaphor from passive trapping to
active throwing and catching, but the Unix `trap` command preserves the
older, more predatory framing. In shell scripting, you still "set traps"
rather than "catch exceptions."

## References

- Bourne, S.R. "The UNIX Shell," Bell System Technical Journal, 57(6),
  1978
- Ritchie, D. & Thompson, K. "The UNIX Time-Sharing System," CACM 17(7),
  1974
- Kerrisk, M. *The Linux Programming Interface*, No Starch Press, 2010
- Raymond, E.S. *The Art of Unix Programming*, Addison-Wesley, 2003
