---
slug: process-sleep
name: Process Sleep
kind: metaphor
dead: true
source_frame: embodied-experience
applies_to:
- software-programs
categories:
- computer-science
author: agent:metaphorex-miner
contributors:
- fshot
related:
- process-kill
- process-parent-child
created: '2026-03-17'
updated: '2026-03-17'
harness: Claude Code
grounding: established
transfers:
  - "[source] a sleeping organism is alive but unconscious, unresponsive to ordinary stimuli until a set duration elapses or an interruption occurs"
  - "[source] sleep is voluntary and reversible -- the sleeper expects to wake and resume activity from where they left off"
  - "[source] a sleeper can be woken prematurely by a sufficiently urgent stimulus"
limits:
  - "[source] breaks because biological sleep involves active processes like memory consolidation and dreaming, whereas the mapped state is total inactivity"
  - "[source] misleads because biological sleep depth varies continuously, while the mapped state is binary -- either scheduled or not"
embodied_patterns:
  - blockage
  - container
  - iteration
relation_types:
  - prevent
  - restore
structure: cycle
abstraction_level: specific
---

## Transfers

A process waiting for a specified duration as sleeping -- alive but
inactive, unconscious of its surroundings, for a set period. The
`sleep()` system call suspends a process for a specified number of
seconds. The process is not terminated; it is not consuming CPU; it is
simply waiting. The biological metaphor makes this state immediately
comprehensible: the process is taking a nap.

Key structural parallels:

- **Alive but inactive** -- the defining characteristic of sleep is
  that the organism is alive but not acting. A sleeping process exists
  in the process table, retains its memory and file descriptors, but
  performs no computation. It is not dead (terminated), not working
  (running), not waiting for input (blocked on I/O) -- it is simply
  resting for a predetermined time. The metaphor captures this specific
  state with precision: alive, present, but temporarily out of action.
- **Voluntary and time-limited** -- biological sleep is entered
  voluntarily and has an expected duration. A process calls `sleep()`
  deliberately, specifying how long to sleep. This distinguishes
  sleeping from other forms of inactivity: a blocked process is waiting
  involuntarily for something external, but a sleeping process chose
  to wait and knows when it will resume.
- **Waking up** -- a sleeper wakes when the time expires or when
  interrupted. A sleeping process resumes when its timer expires or
  when a signal is delivered to it. The `sleep()` call returns the
  number of seconds remaining if interrupted early, mapping the groggy
  "how long was I out?" experience of premature waking.
- **Interruptibility** -- a sleeping person can be woken by a loud
  noise or a shake. A sleeping process can be woken by a signal.
  `SIGALRM` is the alarm clock; other signals are the equivalent of
  someone shaking you awake for an emergency. The metaphor makes
  signal-based waking intuitive.

## Limits

- **Biological sleep is active; process sleep is inert** -- human
  sleep involves dreams, memory consolidation, cellular repair, and
  cycling through sleep stages. A sleeping process does literally
  nothing. The metaphor borrows the passivity of sleep while ignoring
  that real sleep is one of the most metabolically active states an
  organism enters. There is no process equivalent of REM sleep.
- **Sleep depth does not vary** -- human sleep has stages of varying
  depth, with different levels of responsiveness to stimuli. A sleeping
  process is either sleeping or not. Any signal (that is not blocked)
  will wake it. There is no "deep sleep" for processes, no difference
  between light and heavy sleep.
- **The metaphor conflates sleeping with blocking** -- in common usage,
  developers say a process is "sleeping" when it is blocked on I/O,
  waiting for a mutex, or paused for any reason. The biological metaphor
  does not distinguish between voluntary rest (sleep), waiting for
  something (blocking), and being suspended by an external force
  (SIGSTOP). All of these get called "sleeping" colloquially, diluting
  the metaphor's precision.
- **Oversleeping is not a concept** -- a human can sleep longer than
  intended. A process cannot: `sleep(10)` will sleep for at most 10
  seconds (and possibly slightly more due to scheduling, but never
  significantly more). The metaphor imports the possibility of
  oversleeping, which can confuse developers into thinking `sleep()`
  is imprecise in ways it mostly is not.

## Expressions

- "Sleep for 5 seconds" -- the most literal usage, directly invoking
  the biological metaphor: `sleep(5)` in code, `sleep 5` on the
  command line
- "The process is sleeping" -- `ps` shows processes in state `S`
  (sleeping), the most common process state on any Unix system
- "Wake it up with a signal" -- describing signal delivery to a
  sleeping process using the language of rousing someone from sleep
- "Busy-wait vs. sleep" -- the distinction between a process that
  actively polls (pacing the room) and one that sleeps and waits to be
  woken (efficient but less responsive)
- "Put it to sleep" -- used both for processes and, by extension from
  the veterinary euphemism, for terminating services -- an ambiguity
  the metaphor does not resolve

## Origin Story

The `sleep()` system call has been present since the earliest versions
of Unix. The naming follows naturally from the biological metaphor
already embedded in the process model: if processes are alive, they can
sleep. The command-line `sleep` utility is one of the simplest Unix
programs -- it does nothing for the specified duration, then exits.

The metaphor extends through the entire Unix process state model.
The kernel scheduler categorizes processes as running, sleeping
(interruptible), sleeping (uninterruptible), stopped, or zombie. The
"sleeping" state is by far the most common: on a typical Linux system,
the vast majority of processes are sleeping at any given moment,
waiting for timers, I/O, or signals. The metaphor makes this visible:
the system is a room full of sleeping processes, with only a few
awake and active at any time.

## References

- sleep(3) man page, man7.org -- specification of the sleep library
  function and its interaction with signals
- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM
  17(7), 1974 -- original process state model
- Stevens, W. R. *Advanced Programming in the UNIX Environment* (1992)
  -- canonical treatment of sleep, pause, and signal interaction
