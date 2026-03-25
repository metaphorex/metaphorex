---
slug: unix-signal
name: Unix Signal
summary: "Maps human communication onto a numbered interrupt that carries no semantic content. The medium is the entire message."
kind: metaphor
dead: true
source_frame: communication
applies_to:
  - software-programs
categories:
  - computer-science
author: agent:metaphorex-miner
contributors:
  - fshot
related:
  - zombie-process
  - orphan-process
created: '2026-03-17'
updated: '2026-03-17'
harness: Claude Code
grounding: folk
transfers:
  - "[source] a signal interrupts the recipient's current activity to demand immediate attention, like a tap on the shoulder"
  - "[source] the sender chooses which signal to send, but the recipient decides how to handle it -- ignore, act on, or delegate"
  - "[source] some signals cannot be ignored or blocked, analogous to physical force overriding social norms of consent"
limits:
  - "[source] breaks because human communication carries semantic content, whereas Unix signals carry only a number -- the medium is the entire message"
  - "[source] misleads because physical signals travel through space with observable propagation, but the mapped mechanism is an instantaneous kernel-mediated state change with no spatial dimension"
embodied_patterns:
  - force
  - link
  - matching
relation_types:
  - cause
  - coordinate
structure: network
abstraction_level: specific
---

## Transfers

Inter-process communication as physical interruption. A Unix signal is an
asynchronous notification sent to a process -- the computational equivalent
of tapping someone on the shoulder, blowing a whistle, or ringing a
telephone. The metaphor imports the social dynamics of attention and
interruption.

- **Interruption demands response** -- a signal breaks into whatever the
  process is currently doing, just as a tap on the shoulder interrupts a
  conversation. The recipient must acknowledge the interruption, even if
  only to decide to ignore it. In Unix, a process either handles the
  signal, lets the default action occur, or explicitly blocks it. There
  is no pretending it did not arrive.
- **Named signals encode social register** -- SIGTERM is a polite request:
  "please stop what you're doing." SIGKILL is physical force: the process
  is terminated with no opportunity to clean up. SIGHUP originally meant
  "the telephone line hung up" -- a literal telephone metaphor inside the
  signal metaphor. The graduated vocabulary (ask, demand, force) mirrors
  the escalation patterns of human social interaction.
- **The sender-receiver asymmetry** -- in human communication, the sender
  chooses the message and the receiver chooses the response. Unix signals
  preserve this asymmetry. A process can send SIGTERM, but the receiving
  process can catch it and do anything -- save state, ignore it, or
  counter-signal. Only SIGKILL and SIGSTOP bypass the receiver's autonomy,
  and they are reserved for the operating system's sovereign authority.
- **Signal handlers as trained responses** -- registering a signal handler
  is like training a reflex. The process prepares in advance how it will
  respond to each type of interruption. An unhandled signal triggers the
  default response -- often death -- like an untrained person freezing
  when startled.

## Limits

- **Signals carry no content** -- a tap on the shoulder can be followed by
  speech; a whistle can encode Morse code; a telephone call carries
  conversation. Unix signals carry only their identity: a number between
  1 and 64. There is no payload, no message body, no semantic content.
  The metaphor of "signaling" implies communication, but what arrives is
  closer to a reflex trigger than a message. Developers who expect signals
  to carry data are misled by the communication metaphor into treating
  signals as a messaging system.
- **Asynchrony is more radical than physical interruption** -- when someone
  taps your shoulder, you experience the interruption in the physical flow
  of time. A Unix signal can arrive between any two machine instructions,
  potentially corrupting data structures mid-update. The signal handler
  runs in a context so constrained that most standard library functions
  are unsafe to call. The physical interruption metaphor does not prepare
  you for the re-entrancy hazards of signal handling.
- **The telephone metaphor in SIGHUP is doubly dead** -- SIGHUP (signal
  hangup) was literal when terminals connected to Unix via telephone
  modems: hanging up the phone dropped the serial connection, which sent
  SIGHUP to the process. Today nobody uses telephone modems, and SIGHUP
  has been repurposed to mean "reload your configuration." The metaphor
  died, was repurposed, and the repurposed meaning has no connection to
  either telephones or hangups.
- **No conversation is possible** -- human signaling is typically
  bidirectional: you tap someone, they turn, you speak, they respond.
  Unix signals are strictly unidirectional fire-and-forget. The sender
  does not know whether the signal was received, handled, ignored, or
  fatal. There is no acknowledgment, no dialogue, no negotiation. The
  communication metaphor implies an exchange that never happens.

## Expressions

- "Send a signal to the process" -- the postal/communication metaphor
  applied to what is really a kernel state-flag operation
- "Kill -9" -- the most famous signal invocation, where the violence of
  "kill" and the mystique of the number have become a cultural reference
  beyond Unix
- "Trap the signal" -- from hunting/warfare, a secondary metaphor layered
  on the primary: you set a trap for an incoming signal as if it were prey
- "The process caught SIGTERM" -- catching as in catching a thrown ball,
  implying an active reception that the process chose
- "Signal handler" -- a person designated to manage incoming communications,
  bureaucratized into a callback function

## Origin Story

Signals appeared in early Unix (1st Edition, 1971) as a mechanism for the
kernel to notify processes of exceptional events. Thompson and Ritchie's
1974 CACM paper describes them as "a way of simulating software interrupts,"
borrowing the hardware interrupt metaphor into software. The naming was
deliberately evocative: SIGKILL, SIGTERM, SIGINT (interrupt), SIGALRM
(alarm clock), SIGHUP (hangup) all come from physical-world communication
and attention-management vocabulary.

The telephone metaphor in SIGHUP is historically precise. Early Unix
terminals connected via serial lines that were often telephone modem
connections. When the telephone connection dropped, the terminal driver
sent SIGHUP to all processes in the session. The "HUP" was not abstract --
someone literally hung up a telephone handset.

POSIX standardized the signal mechanism in the 1980s, fixing the set of
standard signal names and their default behaviors. By this point the
communication metaphor was fully dead: programmers learn signal numbers
and handler registration patterns without thinking about telephones,
shoulder-taps, or whistles.

## References

- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM 17(7),
  1974 -- signals as "software interrupts"
- IEEE Std 1003.1 (POSIX) -- signal(7) specification
- Kerrisk, M. *The Linux Programming Interface*, No Starch Press, 2010 --
  chapters 20-22 on signal handling
- Raymond, E.S. *The Art of Unix Programming*, Addison-Wesley, 2003
