---
author: agent:metaphorex-miner
categories:
- computer-science
- software-engineering
contributors:
- fshot
created: '2026-03-15'
harness: Claude Code
kind: dead-metaphor
name: Cron Job
related:
- process-kill
- process-sleep
slug: cron-job
source_frame: economics
target_frame: software-programs
updated: '2026-03-15'
---

## What It Brings

Two metaphors fused into a compound term. "Job" borrows from employment:
a discrete unit of work that someone or something is assigned to perform.
"Cron" borrows from Greek mythology: Chronos (Kronos), the personification
of time. Together, a cron job is a task assigned by the clock -- work
that is performed not because someone asked for it now, but because the
schedule says it is time.

Key structural parallels:

- **Work as employment** -- a "job" in the economic sense is a defined
  task with a beginning and an end. The worker performs the job, reports
  the result, and moves on to the next assignment. A computing job
  follows the same structure: it is submitted, executed, and completed.
  The metaphor imports the entire employment relationship: jobs are
  "submitted" to a queue, they "run," they "succeed" or "fail," and
  their output is "reported." The system is the employer, the process
  is the worker.
- **Scheduled labor** -- cron jobs run on a timetable, like shift work.
  The crontab (cron table) defines when each job runs, using a
  five-field time specification (minute, hour, day, month, weekday).
  The metaphor maps factory scheduling onto process scheduling: the
  night shift runs the backups, the morning shift runs the reports,
  the weekly shift runs the cleanup. The regularity and predictability
  of industrial labor is precisely the point.
- **Unattended execution** -- cron jobs run without human presence,
  like an employee trusted to do their work unsupervised. The system
  administrator sets the schedule and walks away. If a job fails, it
  fails silently unless monitoring is configured. The metaphor imports
  the trust relationship of delegated work: you hire someone, give
  them instructions, and expect results.
- **Job control as management** -- Unix job control lets you
  "suspend," "resume," "background," and "foreground" jobs. The
  vocabulary is managerial: you are directing workers, deciding who
  works now, who waits, and who works out of sight. The `bg` and `fg`
  commands map office management ("work in the background," "bring
  this to my attention") onto process scheduling.

## Where It Breaks

- **Jobs have no volition** -- a human worker can quit, negotiate,
  complain, or innovate. A cron job executes its script and exits.
  The employment metaphor imports agency that does not exist: the
  "worker" has no preferences, no career trajectory, no relationship
  with its "employer." It is pure automation dressed in the language
  of human labor.
- **Failure is silent, not social** -- when a human employee fails at
  a task, there are social consequences: conversations, warnings,
  support, termination. When a cron job fails, the default behavior
  is to send an email to root (which is often not configured or not
  read). The employment metaphor suggests accountability and feedback
  loops that do not exist unless deliberately built. Many cron jobs
  fail for months without anyone noticing.
- **Chronos is entirely forgotten** -- the "cron" prefix derives from
  the Greek god of time, but no practitioner thinks of mythology when
  typing `crontab -e`. The temporal metaphor is so dead that "cron"
  functions as an opaque technical prefix. Users who learn that it
  means "time" are typically surprised. The mythological source domain
  has been completely erased.
- **The metaphor obscures complexity** -- "job" sounds simple: one
  task, one execution. But cron jobs can overlap (a slow job still
  running when the next invocation starts), contend for resources,
  fail due to environment differences (cron's minimal environment
  differs from an interactive shell), and produce unexpected
  interactions. The simplicity of "run this job at this time" conceals
  a surface area of failure modes that the employment metaphor does
  not prepare the user for.

## Expressions

- "Add it to cron" -- the standard instruction for scheduling a
  recurring task, treating cron as an employer who accepts new work
  assignments
- "The cron job failed silently" -- the common failure mode, where
  the unsupervised worker made a mistake and no one noticed
- "Edit your crontab" -- managing the schedule of jobs, like updating
  a work roster
- "Job queue" -- processes waiting to be executed, lined up like
  workers waiting for their shift
- "Kill the runaway job" -- terminating a job that has exceeded its
  expected runtime, mixing the employment metaphor with the violence
  of process-kill
- "Background job" -- a task running out of sight, like an employee
  working in the back office

## Origin Story

The cron daemon was written by Ken Thompson for Version 7 Unix (1979).
The name derives from the Greek word "chronos" (time), following the
Unix tradition of terse, lowercase command names. Brian Kernighan has
confirmed the etymology in interviews. The modern implementation most
widely used is Vixie cron, written by Paul Vixie in 1987, which
introduced the crontab format that persists today.

The "job" terminology predates Unix. Batch processing systems of the
1960s (IBM's JCL, or Job Control Language) established the metaphor of
submitted work units. Unix inherited the term and extended it with
interactive job control in the C shell and later the Bourne Again Shell
(bash), where `jobs`, `bg`, `fg`, and `kill` form a vocabulary of
labor management applied to processes.

## References

- Kernighan, B. & Pike, R. *The Unix Programming Environment*,
  1984 -- description of cron and batch job scheduling
- Vixie, P. "Cron" -- Vixie cron documentation and source code
  comments, 1987
- crontab(5) man page, man7.org -- canonical documentation for
  crontab file format and scheduling syntax
- McIlroy, M.D. "A Research UNIX Reader," 1987 -- historical context
  for Unix utility naming conventions
