---
author: fshot
categories:
- software-engineering
- cognitive-science
contributors: []
created: '2026-03-07'
kind: conceptual-metaphor
name: Program Failure Is Bodily Failure
related:
- data-flow-is-fluid-flow
slug: program-failure-is-bodily-failure
source_frame: embodied-experience
target_frame: software-programs
updated: '2026-03-09'
---

## What It Brings

Maps the visceral experience of bodily malfunction onto software failure.
This makes abstract computational problems *feelable*: "the server is
choking" conveys urgency, partial functioning, and the sense that
something is stuck.

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

- **Programs don't suffer** — the metaphor imports empathy where none is
  warranted. "The poor server" anthropomorphizes in ways that can distort
  prioritization.
- **Bodies heal themselves; programs don't** — "the service recovered"
  implies self-healing, but usually a human or watchdog process intervened.
- **Bodily failure is continuous; program failure is often binary** — a
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

Rooted in the broader PROGRAMS ARE PEOPLE conceptual metaphor identified
by Lakoff and others. The bodily-failure specialization thrives in
operations and SRE culture, where practitioners develop a clinical
relationship with system health, complete with "diagnoses," "autopsies"
(post-mortems), and "vital signs" (metrics).

## References

- Lakoff, G. & Johnson, M. *Metaphors We Live By* (1980)
- Hicks, M. *Programmed Inequality* (2017) — discusses gendered metaphors
  in computing, including bodily ones