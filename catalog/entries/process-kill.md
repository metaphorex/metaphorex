---
slug: process-kill
name: Process Kill
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
- zombie-process
- orphan-process
- process-parent-child
created: '2026-03-17'
updated: '2026-03-17'
harness: Claude Code
grounding: established
transfers:
  - "[source] killing is an irreversible act that ends a living entity's autonomous existence"
  - "[source] killing varies in force -- from a polite request to leave to immediate lethal violence -- and the target may or may not comply with lesser force"
  - "[source] killing a caretaker leaves dependents without supervision, creating a cascade of consequences"
limits:
  - "[source] breaks because biological killing destroys the entity permanently, whereas the mapped target can be restarted immediately with no loss of template"
  - "[source] misleads because the moral weight of killing imports unjustified alarm into a routine administrative action"
embodied_patterns:
  - force
  - removal
  - boundary
relation_types:
  - cause
  - prevent
structure: transformation
abstraction_level: specific
---

## Transfers

Terminating a process as killing a living thing. The Unix `kill` command
and system call send signals to processes, and the naming choice frames
process termination as an act of violence against a living entity. The
metaphor is built on a prior metaphor -- that processes are alive -- and
extends it to its logical conclusion: if processes live, they must die,
and someone must do the killing.

Key structural parallels:

- **Graduated force** -- killing in the real world ranges from a polite
  "please leave" to immediate lethal violence. Unix signals mirror this
  spectrum exactly. `SIGTERM` (signal 15) is a polite request: the
  process can catch it, clean up resources, save state, and exit
  gracefully. `SIGKILL` (signal 9) is immediate and absolute: the
  process cannot catch, block, or ignore it. The kernel terminates it
  unconditionally. The metaphor makes the difference between these
  signals viscerally clear: one is asking someone to die; the other is
  killing them on the spot.
- **The finality of death** -- a killed process ceases to exist as a
  running entity. Its memory is reclaimed, its file descriptors close,
  its CPU allocation vanishes. The metaphor imports the irreversibility
  and completeness of death: nothing of the process's runtime state
  survives, only the corpse in the process table (the zombie entry)
  awaiting the parent's acknowledgment.
- **Cascade of consequences** -- killing a parent process orphans its
  children. Killing a session leader may terminate an entire process
  group. The metaphor imports the social reality that killing someone
  has consequences beyond the immediate victim: dependents are left
  without their provider, and the system must handle the aftermath.
- **The executioner has authority** -- only the process owner or root
  can send a kill signal. This maps the real-world principle that the
  power to kill is restricted to those with authority. An unprivileged
  user cannot kill another user's processes, just as a citizen cannot
  execute another citizen.

## Limits

- **Processes can be restarted; the dead cannot** -- the most
  fundamental break in the metaphor. A killed process can be restarted
  immediately. The binary still exists on disk. The configuration is
  unchanged. `kill` in Unix is more like firing an employee than
  murdering a person: the role can be refilled. The metaphor imports
  permanence and tragedy that the technical reality does not warrant.
- **The violence is disproportionate to the action** -- `kill -9` is a
  routine administrative command. System administrators kill processes
  dozens of times a day. The violent metaphor frames a mundane
  housekeeping task as an act of lethal force. This creates jarring
  sentences: "Kill all the children" means "terminate the child
  processes," but the language sounds sociopathic to outsiders.
- **SIGTERM is not really "killing"** -- sending SIGTERM is a request,
  not an execution. The process can ignore it entirely. The metaphor
  collapses the distinction between requesting termination and forcing
  it under the single word "kill," which obscures the fact that most
  "kills" are cooperative shutdowns, not forced terminations.
- **The metaphor obscures what signals actually are** -- `kill` is
  really a general-purpose signal delivery mechanism. `kill -SIGUSR1`
  sends a user-defined signal that has nothing to do with termination.
  The name "kill" for the signal-sending interface misleads users into
  thinking the command can only terminate processes, when it is actually
  the Unix mechanism for inter-process communication.

## Expressions

- "Kill the process" -- the universal expression for forced termination,
  so thoroughly dead as a metaphor that it requires no explanation
- "kill -9" -- the nuclear option, SIGKILL, which cannot be caught or
  ignored; spoken as an idiom even outside Unix contexts to mean
  "terminate with extreme prejudice"
- "Kill it with fire" -- humorous escalation of the kill metaphor,
  used when a process or service refuses to terminate gracefully
- "The OOM killer reaped it" -- the Linux out-of-memory killer, which
  automatically kills processes to free memory, framed as a grim reaper
- "Send it a SIGTERM first, then SIGKILL if it doesn't die" -- the
  standard two-step termination protocol, narrated as escalating force

## Origin Story

The `kill` system call was present in the earliest versions of Unix at
Bell Labs (1970s). The naming was Dennis Ritchie and Ken Thompson's,
following the life/death metaphor already established by the process
model. The man page for `kill(2)` has always described it as sending a
signal to a process, but the name stuck because the most common use was
termination.

The violence of the vocabulary -- kill, terminate, abort, die, signal,
trap, interrupt -- reflects a broader pattern in Unix naming: the
process lifecycle borrows from biological life and death. This was not a
deliberate design decision for the metaphor system as a whole, but
"kill" specifically was a conscious choice. The word is short, memorable,
and conveys the finality of forced termination. It has since become
universal: Windows, macOS, and every major operating system uses "kill"
in its process management vocabulary.

## References

- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM
  17(7), 1974 -- establishes the signal and process termination model
- kill(2) man page, man7.org -- definitive specification of the kill
  system call and signal delivery semantics
- Stevens, W. R. *Advanced Programming in the UNIX Environment* (1992)
  -- canonical treatment of signals and process termination
- Raymond, E. S. *The Art of Unix Programming* (2003) -- cultural
  context for Unix naming conventions
