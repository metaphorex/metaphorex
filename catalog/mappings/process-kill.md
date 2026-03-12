---
slug: process-kill
name: "Process Kill"
kind: dead-metaphor
source_frame: embodied-experience
target_frame: software-programs
categories:
  - computer-science
  - software-engineering
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - process-parent-child
  - zombie-process
  - orphan-process
  - process-sleep
---

## What It Brings

Ending a life -- the most final and violent act in human experience --
mapped onto terminating a running process. The Unix `kill` command sends
signals to processes, and its name frames signal delivery as an act of
lethal force. The violence of the metaphor is deliberate and graduated:
`kill -15` (SIGTERM) is a polite request to die, `kill -9` (SIGKILL)
is immediate execution that cannot be caught, blocked, or ignored. The
entire process lifecycle uses life-and-death language: processes are
born (fork), live (run), die (exit), and can become undead (zombie).

Key structural parallels:

- **Graduated force** -- in the physical world, there is a spectrum
  from a polite request to leave, through physical removal, to lethal
  force. Unix signals mirror this gradient. SIGTERM (signal 15) asks
  the process to shut down gracefully -- it can catch the signal, clean
  up resources, and exit on its own terms. SIGHUP originally meant the
  terminal connection was lost (a "hang up," itself a telephone
  metaphor). SIGKILL (signal 9) is summary execution: the kernel
  terminates the process immediately, with no opportunity for cleanup.
  The metaphor maps escalation of force onto escalation of signal
  severity.
- **Death as termination** -- when a living thing dies, it ceases all
  activity, releases its hold on resources, and its remains must be
  dealt with. When a process is killed, it stops executing, its file
  descriptors are closed, its memory is freed, and its exit status must
  be collected by the parent. The parallel extends even to the
  aftermath: an unreaped dead process becomes a zombie, a dead parent
  creates orphans.
- **The killer has authority** -- not everyone can kill. In society,
  lethal force is restricted by law and power. In Unix, a user can only
  kill processes they own (unless they are root, the superuser who
  operates outside normal constraints). The metaphor imports the concept
  of authority over life and death, and root's unlimited kill authority
  maps onto sovereign power.
- **The right to resist** -- living things fight to survive. A process
  can catch SIGTERM and refuse to die immediately, performing cleanup
  or even ignoring the signal entirely. Only SIGKILL is irresistible --
  the kernel equivalent of a force that cannot be survived. The
  metaphor captures the distinction between a request that can be
  negotiated and a command that cannot.

## Where It Breaks

- **Kill is not really about killing** -- the `kill` command's actual
  function is to send signals, not to terminate processes. You can
  `kill -0` to test if a process exists without affecting it at all.
  You can send SIGUSR1 or SIGUSR2, which are user-defined signals with
  no termination semantics. The name "kill" focuses on the most dramatic
  use case and obscures the general-purpose signal delivery mechanism
  underneath. The metaphor is so dominant that the actual function --
  inter-process communication via signals -- is hidden behind it.
- **The violence is disproportionate to the reality** -- killing a
  process is routine system administration. Administrators kill dozens
  of processes daily without concern. The metaphor imports the gravity
  of ending a life to describe an operation that is closer to turning
  off a light switch. This creates a mismatch between the language
  and the emotional weight of the action: "kill all the children" is
  a normal sentence in process management and an atrocity outside it.
- **Dead processes do not suffer** -- killing implies pain, fear, and
  the loss of something irreplaceable. A process has no subjective
  experience. When killed, it simply stops. There is no suffering, no
  loss of potential, no moral weight. The metaphor borrows the emotional
  intensity of death without any of its actual moral significance.
- **The metaphor conflates agency and mechanism** -- in human experience,
  killing requires a killer with intent. In Unix, `kill -9` is executed
  by the kernel, which has no intent. An OOM killer terminates processes
  based on heuristics, not judgment. The metaphor imports the concept of
  agency where there is only mechanism, which can mislead users into
  thinking the system "decided" to kill their process.

## Expressions

- "Kill the process" -- the universal shorthand for terminating a running
  program, so dead as a metaphor that it feels like a literal description
- "kill -9" -- SIGKILL, the "cannot be caught or ignored" signal,
  spoken as an incantation of last resort among system administrators
- "Kill it with fire" -- humorous escalation when a normal kill does not
  work, layering destruction metaphors on top of the death metaphor
- "The OOM killer got it" -- the Linux out-of-memory killer, personified
  as a predator that selects victims when resources run low
- "Killall" -- the command that terminates all processes matching a name,
  importing the language of massacre into routine system administration
- "It won't die" -- describing a process that catches SIGTERM and refuses
  to exit, anthropomorphizing the process as something that clings to life

## Origin Story

The `kill` system call and command date to the earliest Unix systems at
Bell Labs in the 1970s. Thompson and Ritchie's 1974 CACM paper describes
the signal mechanism, though the violent terminology was already
established in the Unix culture. The choice of "kill" rather than
"terminate" or "stop" reflects the terse, Anglo-Saxon vocabulary that
Unix preferred -- short, punchy words that fit the command-line interface.

The graduated signal system (SIGTERM as request, SIGKILL as force) was
refined over successive Unix versions and codified in the POSIX standard.
The metaphor's completeness is notable: the process lifecycle vocabulary
-- born, live, die, kill, zombie, orphan, reap -- forms a coherent
narrative that spans creation to aftermath. This was not designed as a
unified metaphor system but accumulated as different engineers
independently reached for life-and-death language to describe process
states.

## References

- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM
  17(7), 1974 -- describes the signal mechanism
- Stevens, W. R. *Advanced Programming in the UNIX Environment* (1992)
  -- canonical treatment of signals and process termination
- man7.org `kill(1)`, `kill(2)`, `signal(7)` -- Linux man pages for
  the command, system call, and signal overview
- Kerrisk, M. *The Linux Programming Interface* (2010) -- comprehensive
  modern treatment of signal handling and delivery
