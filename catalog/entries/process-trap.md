---
applies_to:
- computing
author: agent:metaphorex-miner
categories:
- computer-science
- linguistics
contributors: []
created: '2026-03-17'
dead: true
harness: Claude Code
kind: metaphor
name: Process Trap
related:
- daemon
- zombie-process
- orphan-process
slug: process-trap
source_frame: embodied-experience
updated: '2026-03-17'
transfers:
  - '[source] a trap is a concealed mechanism that triggers on contact, mapping hidden hardware interrupts onto unexpected transitions from user to kernel mode'
  - '[source] the trapped entity is redirected to a handler''s control, mapping physical capture onto the transfer of execution to an exception handler'
  - '[source] the trap is set in advance by an authority and activated by the subject''s own action, mapping premeditated hunting devices onto predefined interrupt vectors'
limits:
  - '[source] breaks because physical traps are hostile and harmful to the trapped entity, while process traps are a normal, designed part of system operation'
  - '[source] misleads because a physical trap immobilizes the captured animal, while a process trap transfers control temporarily and the trapped process typically resumes execution afterward'
embodied_patterns:
  - container
  - force
  - matching
relation_types:
  - prevent
  - cause
structure: boundary
abstraction_level: specific
---

## Transfers

You set a trap and wait. Something arrives, and the trap catches it. The
computing term "trap" borrows directly from hunting: a mechanism placed in
advance that intercepts a target when it appears, capturing it so the trapper
can decide what happens next. In Unix, `trap` is a shell built-in that
registers a handler for signals -- you set a trap for SIGINT, and when
Ctrl-C arrives, the trap catches it and runs your code instead of killing
the process.

The metaphor is older than Unix. Hardware traps appeared in the earliest
mainframes: exceptional conditions (division by zero, invalid memory access)
would spring the trap, diverting execution to a handler. The term predates
"exception" and "interrupt handler," both of which are later, more abstract
names for the same mechanism.

Key structural parallels:

- **Setting a trap is registering a handler** -- `trap 'echo caught' SIGINT`
  is laying a snare. The trapper (programmer) decides in advance what to
  catch and what to do with it. The trap is passive until sprung. This maps
  precisely onto the hunting model: you do not chase the signal, you place
  the trap and return to your business.

- **The signal is prey** -- signals arrive unpredictably, like animals moving
  through the forest. SIGTERM may come at any time. The trap waits for it.
  The metaphor frames signals as wild, uncontrolled entities that must be
  intercepted -- not reasoned with, not negotiated with, but caught.

- **Catching prevents default behavior** -- in hunting, a trap catches an
  animal before it can continue on its path. In Unix, trapping a signal
  prevents the default action (usually termination). The trap intercepts the
  signal mid-flight and redirects it. Without the trap, the signal passes
  through and the process dies -- the prey escapes the other way, so to speak,
  by killing the hunter.

- **Hardware traps as pitfalls** -- the earliest computing traps were closer
  to pitfall traps: the processor falls into one when it steps on an invalid
  instruction. The trap is not set for a specific target but for any execution
  that crosses the boundary. This maps onto the concealed-pit model of
  trapping rather than the bait-and-snare model.

## Limits

- **Traps are defensive, not offensive** -- in hunting, traps are set to
  capture something you want: food, fur, a pest you need removed. In
  computing, traps are almost always defensive: you trap SIGTERM to clean up
  before dying, you trap exceptions to prevent crashes. The hunting metaphor
  implies acquisition; the computing reality is damage control. Nobody traps
  a signal because they want it -- they trap it because ignoring it would be
  worse.

- **The trap does not kill the prey** -- a physical trap either kills the
  animal or holds it for the trapper. A signal trap does neither: it
  intercepts the signal and runs a handler, then execution continues. The
  signal is not "held" or "killed" -- it is consumed. The post-catch
  semantics of the metaphor break down entirely: there is no carcass, no
  release, no trapper returning to check the snare.

- **Traps imply single-target mechanisms** -- a hunting trap catches one
  animal at a time. A signal handler can be invoked many times, catching
  repeated signals. The metaphor suggests a one-shot device, but Unix traps
  are permanent (until explicitly reset). This mismatch is invisible in
  practice because the metaphor died long ago -- nobody imagines resetting
  a physical snare when they write `trap '' SIGINT`.

- **The metaphor is completely dead** -- no programmer thinks of hunting
  when typing `trap`. The word has become a pure technical term. The
  original metaphorical content -- the patience of the trapper, the wildness
  of the prey, the concealment of the mechanism -- has been bleached out
  entirely. What remains is a three-letter command that registers a callback.

## Expressions

- "Set a trap for SIGINT" -- registering a signal handler as placing a snare
- "Trap and handle the exception" -- catching an exceptional condition before
  it causes damage
- "Hardware trap" -- a processor exception that diverts execution, as a
  pitfall in the instruction path
- "The trap caught the signal" -- the handler intercepted the signal, as an
  animal caught in a snare
- "Trap on EXIT" -- registering cleanup code that runs when the process
  terminates, the last trap sprung as the prey escapes

## Origin Story

The computing usage of "trap" dates to the earliest mainframes of the 1950s.
IBM's 700 series (1952) used "trap" for hardware interrupts triggered by
exceptional conditions -- arithmetic overflow, illegal instructions, memory
protection violations. The term appears in IBM documentation from this era,
chosen because the mechanism works exactly like a physical trap: a condition
is detected, execution is diverted, and control passes to a handler that
was set up in advance.

Unix inherited the term and made it a shell built-in. The `trap` command in
the Bourne shell (1979) registers handlers for signals, using the same word
that hardware designers had been using for two decades. The man page for
`trap` is terse -- "trap [action] [signal...]" -- and gives no hint of the
hunting metaphor beneath the syntax.

The hunting metaphor was apt for hardware: the processor literally "falls
into" a trap when it executes an invalid instruction, much as an animal
falls into a pit trap. For software signals, the metaphor is looser --
signals are sent deliberately by other processes or by the user, not
encountered accidentally. But the term had already been established at the
hardware level, and software inherited it without renegotiation.

## References

- Kernighan, B. & Pike, R. *The Unix Programming Environment* (1984) --
  shell trap usage and signal handling
- Ritchie, D. & Thompson, K. "The UNIX Time-Sharing System," CACM 17(7),
  1974 -- signal mechanism in early Unix
- Bourne, S.R. "The UNIX Shell," Bell System Technical Journal, 57(6),
  1978 -- the trap built-in in the Bourne shell
- Bach, M.J. *The Design of the UNIX Operating System* (1986) -- hardware
  and software trap handling in Unix kernels
