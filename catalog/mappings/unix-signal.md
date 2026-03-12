---
slug: unix-signal
name: "Unix Signal"
kind: dead-metaphor
source_frame: communication
target_frame: software-programs
categories:
  - computer-science
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - zombie-process
  - orphan-process
---

## What It Brings

A Unix signal is an asynchronous notification sent to a process -- a tap on
the shoulder, an air-raid siren, a phone hanging up. The metaphor borrows
from physical communication: signals are things you send to get someone's
attention, and the recipient must decide how to respond. The naming of
individual signals extends the metaphor into specific communicative acts,
each with its own social register.

Key structural parallels:

- **Interruption as the core mechanism** -- a signal does not wait for the
  process to be ready. It arrives asynchronously, like someone tapping you
  mid-sentence. The process must stop what it is doing and handle the
  interruption. This maps the social dynamics of interruption onto
  inter-process communication: some interruptions are polite (SIGTERM),
  some are urgent (SIGINT), and some cannot be ignored (SIGKILL).
- **The telephone metaphor in SIGHUP** -- "hang up" is explicitly
  telephonic. When a user disconnected their terminal (literally hung up
  the phone on a modem connection), the kernel sent SIGHUP to the
  process. The physical act of placing a telephone receiver back on its
  cradle mapped directly onto the severing of a terminal session. Today
  SIGHUP is used to tell daemons to reload their configuration -- a
  meaning that has drifted far from any telephone.
- **Kill as escalation** -- SIGTERM asks a process to terminate; it can
  refuse. SIGKILL forces termination; it cannot be caught or ignored.
  This maps a social escalation pattern: first a polite request, then
  an order that cannot be disobeyed. The vocabulary is deliberately
  violent (kill, terminate, abort) because the metaphor frames process
  management as an authority relationship where the operating system has
  ultimate coercive power.
- **Trapping signals** -- a process can "trap" a signal, catching it
  before it takes effect. The trapping metaphor comes from hunting: you
  set a trap for something that would otherwise pass through your
  territory uncontrolled. A signal handler is a trap -- it intercepts
  the signal and executes custom code instead of the default action.

## Where It Breaks

- **Signals are not messages** -- in human communication, a signal carries
  content: words, gestures, meaning. A Unix signal carries almost no
  information -- just a number identifying which signal it is. You cannot
  attach a message to SIGTERM explaining *why* the process should stop.
  The metaphor implies communicative richness that the mechanism does not
  provide. This is why signals are poor for actual inter-process
  communication and why sockets, pipes, and message queues exist.
- **The sender is often invisible** -- in human communication, you
  typically know who is signaling you. In Unix, a process receiving
  SIGTERM may not know (or care) who sent it: the kernel, another
  process, the user pressing Ctrl+C, or a system shutdown sequence. The
  signal arrives without a return address. The communication metaphor
  implies a dyadic relationship (sender and receiver) but Unix signals
  are often fire-and-forget broadcasts with anonymous senders.
- **Default actions are not "responses"** -- when a person receives a
  signal, they interpret it and choose a response. When a process
  receives a signal it has not explicitly handled, the kernel applies
  a default action (usually termination). There is no interpretation,
  no choice -- just a hardcoded consequence. The communication metaphor
  implies agency on the receiver's side that exists only if the
  programmer explicitly wrote a signal handler.
- **The telephone is gone** -- SIGHUP's telephonic origin is
  incomprehensible to programmers who have never used a modem. The signal
  now means "reload configuration" in most daemon conventions, a meaning
  that has no connection to hanging up a phone. The metaphor has not just
  died but been repurposed, its original source domain completely
  detached from its current use.

## Expressions

- "Send it a signal" -- the standard phrasing, preserving the
  communication metaphor in everyday Unix administration
- "Kill the process" -- the most common signal-related expression, so
  naturalized that programmers do not register the violence of the
  metaphor
- "Trap SIGINT" -- the hunting metaphor for installing a signal handler
- "Caught a segfault" -- SIGSEGV described as something you catch, like
  a thrown ball or a trapped animal
- "Nohup" -- "no hang up," a command that immunizes a process against
  SIGHUP, preserving the telephone metaphor in its negation
- "The process was sent SIGTERM but wouldn't die" -- the full
  personification: the process receives communication, exercises agency,
  and resists death

## Origin Story

Signals appeared in early Unix (First Edition, 1971) as a mechanism for
the kernel to notify processes of exceptional events. The original set was
small: interrupt, quit, and a few hardware exceptions. The naming followed
the communication metaphor naturally -- these were notifications, and
"signal" was already the standard engineering term for an information-
carrying transmission.

The signal vocabulary expanded through successive Unix versions. SIGHUP
came from the literal experience of timesharing terminals connected via
telephone lines -- when the line dropped, the terminal "hung up." SIGKILL
and SIGTERM formalized the escalation pattern. The full POSIX signal set
(31 standard signals) represents decades of accretion, each new signal
extending the metaphor into new territory while the original telephonic
context receded further into history.

## References

- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM 17(7),
  1974
- IEEE Std 1003.1 (POSIX), Signal Concepts, various editions
- signal(7) -- Linux man page, man7.org
- Kernighan, B. & Pike, R. *The Unix Programming Environment*,
  Prentice-Hall, 1984
