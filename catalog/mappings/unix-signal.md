---
author: agent:metaphorex-miner
categories:
- computer-science
contributors:
- fshot
created: '2026-03-15'
harness: Claude Code
kind: dead-metaphor
name: Unix Signal
related:
- process-fork
- zombie-process
- orphan-process
slug: unix-signal
source_frame: communication
target_frame: software-programs
updated: '2026-03-15'
---

## What It Brings

A signal in the physical world is a gesture, sound, or sign that conveys
information across distance -- a raised hand, a whistle, a flashing light.
In Unix, a signal is an asynchronous notification sent to a process,
interrupting whatever it is doing to deliver a message. The metaphor
imports the urgency and physicality of real-world signaling into an
abstract inter-process communication mechanism.

Key structural parallels:

- **Interruption as communication** -- signals in the physical world
  interrupt: a tap on the shoulder stops your conversation, a fire alarm
  overrides whatever you were doing. Unix signals work identically. When
  a process receives SIGTERM, its current execution is suspended and the
  signal handler runs. The metaphor captures the defining characteristic
  of signals versus other IPC mechanisms: they are intrusive. They do not
  wait in a queue to be politely read; they barge in.
- **The message is the medium** -- real-world signals carry minimal
  content. A whistle means "stop." A red light means "danger." Unix
  signals are the same: they carry a number and nothing else. SIGKILL is
  9, SIGTERM is 15, SIGHUP is 1. There is no payload, no explanation, no
  context. The metaphor's mapping is tight: signals are blunt instruments
  for simple messages, not vehicles for complex communication.
- **Named signals encode specific social scripts** -- the signal names
  import specific human interaction patterns. SIGTERM is a polite request
  to terminate -- like asking someone to leave. SIGKILL is forced removal
  -- like being physically ejected. SIGHUP originally meant the terminal
  "hung up" the phone. SIGSTOP is "freeze." Each signal name maps a human
  social interaction onto a process management operation.
- **The sender-receiver asymmetry** -- in physical signaling, the sender
  chooses when to signal; the receiver must react. Unix signals preserve
  this asymmetry. The `kill` command sends; the receiving process must
  handle or die. The receiver cannot refuse to receive (though it can
  choose its response for most signals). This power asymmetry -- the
  signaler controls the interaction -- is central to both the metaphor
  and the mechanism.

## Where It Breaks

- **Real signals are perceived; Unix signals are imposed** -- when someone
  taps your shoulder, you perceive the tap and choose how to respond. A
  deaf person might not hear a whistle. But Unix signals cannot be missed
  (except when blocked). They are not perceptions; they are forced state
  changes. The metaphor implies a communication between agents, but the
  reality is closer to a remote control: the sender pushes a button, and
  the receiver's behavior changes whether it consents or not.
- **SIGKILL violates the metaphor entirely** -- you cannot signal someone
  to death. A whistle does not kill the listener. But SIGKILL (signal 9)
  terminates a process immediately and unconditionally -- the process
  cannot catch, block, or ignore it. This is not signaling; it is
  execution. The metaphor of communication breaks down completely for the
  most commonly discussed signal, which is really an exercise of absolute
  power dressed in the language of messaging.
- **The telephone metaphor in SIGHUP is obsolete** -- SIGHUP (hangup)
  originally meant the modem connection was lost, borrowing from the
  telephone act of hanging up the receiver. Modern systems have no modems,
  no telephone lines, and often no physical terminals. SIGHUP has been
  repurposed to mean "reload your configuration" for daemon processes --
  a meaning that has nothing to do with hanging up anything. The metaphor
  has been recycled beyond recognition.
- **Signals are not really communication** -- real communication is
  bidirectional: the receiver can respond, ask for clarification, or
  signal back. Unix signals are fire-and-forget. The sender does not
  know if the signal was received, how it was handled, or what happened
  next (unless it explicitly waits). Calling this "signaling" dignifies
  what is really a one-way interrupt mechanism with the vocabulary of
  human interaction.

## Expressions

- "Send a signal to the process" -- the canonical phrasing, using the
  conduit metaphor (signals are sent like messages)
- "Kill -9" -- the most famous Unix command, sending SIGKILL. The
  combination of "kill" and a bare number has a clinical finality
- "Caught the signal" -- the process installed a handler that intercepted
  the signal, using the metaphor of catching a thrown object
- "Trap the signal" -- install a signal handler, borrowing from hunting
  vocabulary (setting a trap for something that will arrive)
- "Hang up" -- SIGHUP, the telephone metaphor fossilized in a system
  call
- "The process was interrupted" -- SIGINT, from Ctrl-C, the keyboard
  interrupt that enters daily programming vocabulary as casually as
  pressing a button

## Origin Story

Signals appeared in the earliest versions of Unix at Bell Labs in the
early 1970s. Thompson and Ritchie needed a mechanism for the kernel to
notify processes of exceptional events -- terminal disconnection,
arithmetic errors, and user interrupts. The physical-world signal metaphor
was a natural choice: these were brief, urgent notifications that demanded
immediate attention.

The original Unix signal set was small: interrupt, quit, hangup, and a
few others. The names drew on concrete physical metaphors -- "hangup"
from the telephone, "interrupt" from conversation, "kill" from violence.
As Unix evolved, more signals were added (POSIX defines over 30), and
the metaphor strained. SIGUSR1 and SIGUSR2 -- "user-defined signals" --
are semantically empty, mere numbered slots. SIGPIPE -- sent when a
process writes to a broken pipe -- layers the plumbing metaphor on top
of the signaling metaphor.

The signal mechanism was significantly redesigned in BSD Unix (the
"reliable signals" of 4.2BSD) and again in POSIX, but the metaphorical
vocabulary remained intact. The original naming choices from the early
1970s still govern how every Unix programmer talks about asynchronous
process notification half a century later.

## References

- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM 17(7),
  1974 -- introduces signals as part of the Unix process model
- Stevens, W. R. *Advanced Programming in the UNIX Environment* (1992)
  -- canonical treatment of signal handling, including BSD vs. System V
  differences
- Kerrisk, M. *The Linux Programming Interface* (2010) -- modern
  comprehensive treatment of signal semantics
- IEEE Std 1003.1 (POSIX) -- formal specification of signal names and
  behavior
