---
slug: program-failure-is-bodily-failure
name: "Program Failure Is Bodily Failure"
kind: conceptual-metaphor
source_frame: embodied-experience
target_frame: software-programs
categories:
  - software-engineering
  - cognitive-science
author: fshot
contributors: []
related:
  - data-flow-is-fluid-flow
---

## What It Brings

Maps the visceral, universal experience of bodily malfunction onto software
failure. This makes abstract computational problems *feelable* — when someone
says "the server is choking," every listener immediately grasps the urgency,
the partial functioning, the sense that something is stuck.

Key structural parallels:

- **Symptoms are observable** — just as a body shows signs of illness, a
  failing program shows error messages, slow responses, corrupted output.
- **Causes are often hidden** — the symptom (crash) and the cause (memory
  leak) are different things, just as a fever doesn't tell you which
  infection caused it.
- **Severity has a spectrum** — from mild ("it's a bit sluggish") to
  catastrophic ("it shit the bed"), mirroring the range from fatigue to
  organ failure.

## Where It Breaks

- **Programs don't suffer.** The metaphor imports empathy where none is
  warranted. "The poor server" anthropomorphizes in ways that can distort
  prioritization.
- **Bodies heal themselves; programs don't.** Saying a service "recovered"
  implies self-healing, but usually a human or watchdog process intervened.
- **Bodily failure is continuous; program failure is often binary.** A
  process is running or it isn't. The metaphor can obscure this by suggesting
  gradual degradation where there's actually a hard crash.

## Expressions

- "The ETL script shit the bed" — catastrophic, undignified failure
  (infantile or pathological loss of bodily control)
- "The server is choking" — partial processing failure, something is stuck
- "Kill the process" — euthanasia as resource management
- "The service died" — cessation of function as death
- "Zombie process" — a process that has died but hasn't been cleaned up,
  still occupying resources (the undead consuming without contributing)
- "The system is on life support" — barely functional, requiring constant
  manual intervention

## Origin Story

Deeply rooted in the broader PROGRAMS ARE PEOPLE conceptual metaphor
identified by Lakoff and others. The bodily-failure specialization is
particularly common in operations and SRE culture, where practitioners
develop an almost clinical relationship with system health — complete
with "diagnoses," "autopsies" (post-mortems), and "vital signs" (metrics).

## References

- Lakoff, G. & Johnson, M. *Metaphors We Live By* (1980)
- Hicks, M. *Programmed Inequality* (2017) — discusses gendered metaphors
  in computing, including bodily ones
