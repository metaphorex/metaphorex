---
slug: cron-job
name: "Cron Job"
kind: dead-metaphor
source_frame: labor
target_frame: software-programs
categories:
  - computer-science
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - labor-is-a-resource
  - process-parent-child
---

## What It Brings

Unix's `cron` daemon (from Chronos, the Greek personification of time)
schedules "jobs" -- units of computational work treated as employment tasks
assigned to the system. The metaphor imports the entire vocabulary of
managed labor: jobs are submitted, queued, scheduled, running, suspended,
completed, or failed. The system is the employer; the processes are workers;
cron is the shift supervisor consulting the schedule and dispatching workers
at the appointed times.

Key structural parallels:

- **Job as discrete unit of work** -- in employment, a job has defined
  scope, a beginning, and an end. You are hired to do a job, you perform
  it, you finish. In Unix, a cron job is a defined command that runs at
  specified times, does its work, and exits. The metaphor gives
  computational tasks the shape of employment: bounded, purposeful, and
  completable. This framing excludes long-running services, which are not
  "jobs" but "daemons" -- a different metaphor entirely.
- **Scheduling as shift management** -- a crontab is a schedule: it
  specifies which jobs run at which times, the way a factory shift
  schedule specifies which workers report when. The five-field crontab
  syntax (minute, hour, day, month, weekday) mirrors the temporal
  granularity of employment scheduling. "Every weekday at 2 AM" reads
  like a night shift assignment.
- **Job control as labor management** -- Unix job control lets you
  suspend a job (Ctrl-Z), resume it in the foreground (`fg`) or
  background (`bg`), and check on running jobs (`jobs`). This is
  supervisory vocabulary: you suspend a worker, reassign them, check
  their status. The metaphor positions the user as a manager directing
  a workforce of processes.
- **Job queues** -- batch processing systems queue jobs and execute them
  in order, the way an employment office processes applications. "The
  job is in the queue" means "it is waiting its turn," importing the
  physical image of workers lined up waiting for assignment.

## Where It Breaks

- **Jobs have no volition; workers do** -- a human worker can quit,
  complain, negotiate, or work to rule. A cron job executes exactly what
  it is told or fails silently. The labor metaphor imports a social
  relationship (employer-employee) where there is only a mechanical one
  (scheduler-process). This anthropomorphism is mostly harmless, but it
  occasionally misleads: when a cron job "fails," people troubleshoot it
  as if it made a mistake, rather than recognizing that the specification
  was wrong.
- **Cron has no awareness of job dependencies** -- a real supervisor
  knows that Task B depends on Task A and adjusts the schedule
  accordingly. Cron is purely time-based: it fires jobs at specified
  times regardless of whether prerequisite jobs have completed. The labor
  metaphor suggests a competent manager who understands workflow; the
  reality is a clock that triggers commands. This mismatch has spawned
  entire categories of workflow orchestration tools (Airflow, Luigi,
  Temporal) to provide the dependency awareness that cron's "supervisor"
  lacks.
- **"Killing" a job escalates the metaphor disturbingly** -- `kill -9`
  sends SIGKILL to a process, terminating it immediately without
  cleanup. The labor metaphor starts at "employment" but the failure
  vocabulary escalates to violence. You do not fire a job; you kill it.
  The mixed metaphor (labor + violence) is so normalized in Unix culture
  that its strangeness is invisible, but it reveals a tension between
  the orderly employment frame and the raw power dynamics of process
  control.
- **Scheduled jobs lack the economic relationship** -- employment
  involves compensation: workers are paid for their labor. Cron jobs
  receive no compensation; they consume resources. If anything, jobs
  cost the employer (the system) rather than earning for the worker.
  The economic dimension of labor is entirely absent from the computing
  metaphor, leaving only the control dimension: submission, supervision,
  and termination.

## Expressions

- "Cron job" -- a task scheduled to run at specified times; the
  canonical Unix usage
- "Run the job" -- execute the scheduled task; "run" doubles as both
  labor and locomotion metaphor
- "Job queue" -- tasks waiting for execution; imports the physical
  image of a line of workers
- "Background job" -- a process running without occupying the terminal;
  "background" as the less visible work area
- "Kill the job" -- terminate a running process; the violent escalation
  from the employment frame
- "Job failed" -- the scheduled task did not complete successfully;
  treated as a performance issue rather than a mechanical failure
- "Submitted a batch job" -- sent work to the system for later
  processing; pure employment vocabulary

## Origin Story

The term "job" in computing predates Unix, originating in batch processing
systems of the 1950s and 1960s. IBM's Job Control Language (JCL) for
OS/360 formalized the concept: users submitted "jobs" consisting of "job
steps" to the system, which processed them in sequence. The labor metaphor
was deliberate -- early computing centers operated like factories, with
operators managing queues of submitted work.

Unix's `cron` was written by Ken Thompson for Version 7 Unix (1979). The
name references Chronos, but the "job" vocabulary came from the existing
batch processing tradition. The crontab file format -- a schedule of
commands -- formalized the shift-schedule metaphor. Paul Vixie's 1987
rewrite (Vixie cron) became the standard implementation and preserved the
metaphorical framework entirely. Modern systemd timers provide equivalent
functionality but use different vocabulary ("units" and "timers" instead
of "jobs" and "crontabs"), partially escaping the labor metaphor.

## References

- Thompson, K. "UNIX Implementation," Bell System Technical Journal,
  57(6), 1978
- Vixie, P. "cron -- daemon to execute scheduled commands," FreeBSD
  manual page
- Raymond, E.S. *The Art of Unix Programming*, Addison-Wesley, 2003
