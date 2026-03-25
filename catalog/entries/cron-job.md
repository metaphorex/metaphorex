---
slug: cron-job
name: Cron Job
summary: "Scheduled tasks framed as time-governed employment. Combines the labor metaphor of 'jobs' with Chronos the timekeeper."
kind: metaphor
dead: true
source_frame: economics
applies_to:
- software-programs
categories:
- computer-science
author: agent:metaphorex-miner
contributors:
- fshot
related: []
created: '2026-03-17'
updated: '2026-03-17'
harness: Claude Code
grounding: established
transfers:
  - "[source] a job is a discrete unit of work assigned to a worker, with a defined start, execution, and completion"
  - "[source] jobs are scheduled, queued, dispatched, and may succeed or fail -- the full lifecycle of managed labor"
  - "[source] a timekeeper (chronos) determines when each job begins, imposing external temporal discipline on the workers"
limits:
  - "[source] breaks because employment involves ongoing negotiation, compensation, and worker agency, whereas the mapped entity executes a fixed script with no capacity to refuse or renegotiate"
  - "[source] misleads because the 'job' framing implies a human-scale task with meaningful duration, when the mapped entity may execute in milliseconds"
embodied_patterns:
  - iteration
  - path
  - force
relation_types:
  - coordinate
  - cause
structure: cycle
abstraction_level: specific
---

## Transfers

Scheduled tasks as jobs -- discrete units of work performed on a
schedule. The Unix `cron` daemon (from Chronos, the Greek personification
of time) executes commands at specified times. A "cron job" is a task
that the system performs on a recurring schedule: every minute, every
hour, at 3 AM on Sundays. The metaphor combines two source domains:
the employment metaphor of "jobs" (units of work) and the mythological
metaphor of Chronos (the master of time who governs when work happens).

Key structural parallels:

- **Work as employment** -- a "job" in computing is a discrete task the
  system performs, borrowing directly from the employment sense of the
  word. Jobs are "submitted" to the system, "queued" for execution,
  "dispatched" to processors, and "completed" or "failed." The
  employment metaphor frames the computer as a workplace and processes
  as workers performing assigned tasks. Job control commands (`jobs`,
  `fg`, `bg`, `suspend`) treat processes as employees who can be
  reassigned, sent to the background, or told to pause.
- **The schedule as discipline** -- cron imposes temporal discipline on
  jobs, specifying exactly when they run. The crontab (cron table) is
  a work schedule: a timetable of tasks and their assigned times. The
  metaphor maps the industrial practice of scheduling labor onto
  automated task execution. The five-field crontab syntax (minute, hour,
  day, month, weekday) reads like a shift schedule.
- **Chronos as timekeeper** -- the name "cron" invokes Chronos, the
  Greek personification of time. This is a deliberate classical
  allusion: the daemon that governs when things happen is named after
  the god of time. The mythological metaphor adds gravitas to what is
  essentially a timer-based task scheduler.
- **Fire and forget** -- a cron job runs without supervision. No one
  watches it execute. If it fails, the failure may go unnoticed unless
  monitoring is configured. This maps the industrial reality of shift
  work: the night shift runs without the boss present, and problems may
  not be discovered until morning.

## Limits

- **Jobs imply a worker; cron has none** -- the employment metaphor
  implies a person performing the work. A cron job is a script or
  command executed by the operating system. There is no worker in any
  meaningful sense: no one who can exercise judgment, adapt to
  unexpected conditions, or decide that the job is not worth doing
  today. The metaphor imports human agency into a purely mechanical
  process.
- **The schedule is rigid; employment schedules are not** -- a crontab
  entry fires at exactly the specified time, every time, without
  variation. Real work schedules involve sick days, holidays, overtime,
  and negotiation. Cron has no concept of "the job ran too long
  yesterday, so let's skip today." The metaphor borrows the structure
  of scheduling while stripping out all the flexibility that makes
  real scheduling a social negotiation.
- **Failure is silent** -- when a cron job fails, it often fails
  silently. The default behavior is to email output to the local user,
  but on most modern systems this email goes nowhere. The employment
  metaphor implies accountability (a failed job has consequences for
  the worker), but cron jobs fail and no one notices. This is one of
  the most common operational problems in Unix systems, and the "job"
  metaphor's implication of supervised work obscures it.
- **Chronos vs. Kronos** -- the name "cron" may conflate Chronos (time)
  with Kronos (the Titan who devoured his children). The mythological
  metaphor is imprecise, and some sources disagree on which figure is
  referenced. This is a minor point, but it illustrates how metaphorical
  names can carry unintended connotations from their source domain.

## Expressions

- "Set up a cron job" -- the universal phrase for scheduling a
  recurring task, used far beyond Unix into web development, DevOps,
  and cloud computing
- "Edit the crontab" -- modifying the cron table, the work schedule
  for automated tasks
- "The cron job failed silently" -- a common operational complaint,
  combining the employment metaphor with the reality of unsupervised
  automated work
- "Cron expression" -- the five-field time specification syntax
  (e.g., `0 3 * * 0` for 3 AM every Sunday), treated as a scheduling
  language
- "Job scheduler" -- the generic term for cron-like systems, fully
  dead as a metaphor: no one thinks of a person scheduling employees
  when they say "job scheduler"

## Origin Story

The `cron` daemon was created by Ken Thompson for Version 7 Unix
(1979). The name derives from Chronos, the Greek personification of
time. The modern implementation used in most Linux systems was written
by Paul Vixie in 1987 (Vixie cron) and became the de facto standard.

The "job" terminology predates Unix entirely. Batch processing systems
of the 1960s (IBM OS/360 and its JCL -- Job Control Language) used
"job" as the fundamental unit of work submitted to the computer. The
metaphor was natural: you submitted a job to the computer the way you
submitted work to a contractor. Unix inherited this vocabulary and
embedded it in its process control system: `jobs`, `fg`, `bg`, and the
cron daemon all treat computation as employment.

The combination of Chronos (time) with job (work) in "cron job"
creates a compact metaphorical phrase: time-governed work. It has
become so standard that every major cloud platform (AWS CloudWatch
Events, Google Cloud Scheduler, Azure Logic Apps) uses "cron
expression" to mean a time specification, even though these systems
have no connection to the original Unix cron daemon.

## References

- cron(8) and crontab(5) man pages, man7.org -- specification of the
  cron daemon and crontab syntax
- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM
  17(7), 1974 -- context for Unix's job and scheduling model
- Raymond, E. S. *The Art of Unix Programming* (2003) -- cultural
  history of Unix naming conventions including mythological allusions
