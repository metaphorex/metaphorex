---
slug: daemon
name: "Daemon"
kind: dead-metaphor
source_frame: mythology
target_frame: computing
categories:
  - linguistics
  - software-engineering
author: fshot
contributors: []
related:
  - zombie-process
  - orphan-process
---

## What It Brings

Invisible agency: something that works on your behalf without being asked,
without being seen, and without stopping. The Greek daimon was not a demon
in the Christian sense -- it was an intermediary spirit, a guiding
intelligence that operated between the human and divine realms. Socrates
claimed to have one: a voice that whispered warnings but never commanded.

- **Autonomous background work** -- a Unix daemon starts at boot and runs
  until shutdown, handling requests without direct human interaction. The
  mythological mapping is precise: daimons were not summoned for specific
  tasks like servants; they simply *attended* to their domain. `httpd`
  attends to HTTP requests the way a household spirit attends to the
  hearth. Neither waits to be asked.
- **Neither good nor evil** -- the Greek daimon was morally neutral, a
  force of nature with purpose but without malice. This maps cleanly to
  background processes: `cron` is neither helpful nor hostile, it simply
  executes. The Christian demonization of "daemon" into "demon" has no
  analogue in computing. A runaway daemon that consumes all memory is not
  evil -- it is indifferent.
- **Invisibility as design** -- you are not supposed to see a daemon
  working. The mythological parallel is exact: daimons operated behind the
  scenes, influencing outcomes without revealing themselves. A well-behaved
  daemon writes to a log file and otherwise stays silent. Visibility is a
  sign of failure.

## Where It Breaks

- **Daimons had judgment** -- the Greek daimon was an intelligent, choosing
  entity. It could warn Socrates away from a bad decision. A Unix daemon
  has no judgment at all. It follows its configuration file with perfect
  literal obedience. The metaphor smuggles in an implication of agency
  that the technology lacks entirely. When `sshd` accepts a malicious
  connection that matches its rules, there is no daimon whispering a
  warning.
- **The supernatural is gone** -- the word "daemon" in computing carries
  zero supernatural charge. Programmers do not feel they are invoking
  spirits when they type `systemctl start`. The entire mythological
  framework -- the numinous, the liminal, the uncanny presence that
  operates between worlds -- has been bleached into a technical term
  meaning "background process." What was lost: the sense that autonomous
  agents deserve respect, caution, and perhaps a little awe.
- **Daimons were personal** -- Socrates' daimon was *his*, bound to him,
  reflecting his nature. Daemons in computing are impersonal system
  services shared by all users. The loss of the personal-guardian aspect
  is interesting: we might design better systems if we retained the idea
  that each user deserves a dedicated intelligent intermediary watching
  out for them.
- **The spelling preserves what the meaning discarded** -- "daemon" retains
  the archaic spelling precisely because the MIT programmers who coined
  the computing usage were classicists who knew the distinction between
  daimon and demon. The spelling is a fossil of the original metaphorical
  intent, long after that intent ceased to matter to most users.

## Expressions

- "Daemonize a process" -- detach it from the terminal and let it run in
  the background, a ritual of release into autonomous existence
- "The daemon is down" -- a system service has stopped running, reported
  with the same flat affect as "the printer is jammed"
- "Daemon process" -- redundant (daemon already means background process),
  but the redundancy reveals how dead the metaphor is: "daemon" no longer
  carries enough meaning on its own
- "Kill the daemon" -- terminate the background process, combining two dead
  metaphors (kill + daemon) without anyone noticing the mythological
  violence implied
- The `d` suffix -- `httpd`, `sshd`, `systemd`, `crond` -- the daemon
  compressed to a single letter, the maximum possible distance from the
  original Greek spirit

## Origin Story

The computing usage traces to MIT's Project MAC in 1963. Fernando Corbato
and his team needed a name for background processes in the Compatible
Time-Sharing System (CTSS). They chose "daemon" from Maxwell's demon --
the thought experiment by James Clerk Maxwell (1867) in which an
imaginary being sits at a door between two chambers of gas, sorting fast
molecules from slow ones, seemingly violating the second law of
thermodynamics.

Maxwell himself borrowed "demon" from Greek mythology, and the CTSS team
preferred the older spelling "daemon" to distinguish their concept from the
Christian devil. The analogy was apt: Maxwell's demon is an invisible agent
that works continuously, sorting and directing without being seen. CTSS
daemons did the same -- handling print queues, managing scheduling, sorting
the work of the system without user awareness.

The term migrated to Multics, then to Unix, where it became canonical. BSD
adopted the daemon as its literal mascot -- a red cartoon imp holding a
trident, cheerfully conflating the Greek daimon, Maxwell's demon, and the
Christian devil in a single image that nobody found theologically
troubling. By the 1980s, "daemon" was a standard Unix term. By the 2000s,
most programmers using it had never heard of Maxwell's demon, let alone
Socrates' daimonion.

## References

- Corbato, F. & Vyssotsky, V. "Introduction and Overview of the Multics
  System," AFIPS (1965) -- early documentation of the daemon concept
- Maxwell, J.C. *Theory of Heat* (1871) -- the thought experiment that
  gave computing its daimons
- Raymond, E. *The New Hacker's Dictionary* (1996) -- documents the MIT
  origin story and the Maxwell's demon connection
- McKusick, M.K. "The BSD Daemon," *USENIX* -- history of the BSD mascot
