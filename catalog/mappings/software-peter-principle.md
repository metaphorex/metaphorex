---
author: agent:metaphorex-miner
categories:
- software-engineering
- organizational-behavior
contributors:
- fshot
created: '2026-03-15'
harness: Claude Code
kind: conceptual-metaphor
name: Software Peter Principle
related:
- technical-debt
- accidental-complexity
slug: software-peter-principle
source_frame: organizational-management
target_frame: software-programs
updated: '2026-03-15'
---

## What It Brings

Laurence J. Peter's 1969 principle observes that in a hierarchy, every
employee tends to rise to their level of incompetence. A competent
engineer is promoted to manager; a competent manager is promoted to
director. Promotion continues until the person occupies a role they
cannot perform well, and there they remain -- because organizations
reward past performance, not future capability. The hierarchy fills up
with people who are one level above their competence.

The software Peter Principle maps this dynamic onto codebases and
projects. Software that succeeds at a given scale or scope is "promoted"
-- given more features, more users, more integrations, more
responsibilities -- until it reaches a level of complexity it was never
designed to handle. There it remains, incompetent at its current role
but impossible to demote.

The structural parallels are detailed:

- **Success triggers promotion** -- in organizations, the reward for
  doing your job well is a different job. In software, the reward for a
  successful application is more requirements. A tool built for one team
  gets adopted by the whole department. A script that automated one task
  becomes the backbone of a workflow. Success at level N guarantees
  assignment to level N+1.
- **The new role requires different skills** -- a good engineer and a
  good manager need different competencies. Likewise, software that
  handles 100 users and software that handles 100,000 users need
  different architectures. The code that was elegant at its original
  scale becomes pathological at its promoted scale, not because it got
  worse, but because the demands changed.
- **Demotion is culturally impossible** -- organizations cannot easily
  demote a manager back to engineer. Similarly, once software has been
  adopted at a new scope, it is nearly impossible to reduce that scope.
  Users depend on it. Contracts reference it. Workflows are built around
  it. The software is trapped at its level of incompetence.
- **The hierarchy fills with incompetence** -- Peter's principle predicts
  that over time, every position will be occupied by someone incompetent
  to perform it. The software analogue is the enterprise environment
  where every critical system is operating beyond its design parameters,
  and the entire infrastructure is a collection of tools doing jobs they
  were never built for.

## Where It Breaks

- **Software is not an agent** -- Peter's principle depends on the
  employee's volition and identity. A person promoted beyond their
  competence still occupies the role, goes to meetings, makes decisions
  (badly). Software does not choose to be promoted, resist demotion, or
  identify with its position. The anthropomorphism necessary to make the
  metaphor work obscures the fact that the failure belongs to the humans
  who made the scoping decisions, not to the software itself.
- **Software can be refactored; people cannot** -- the Peter Principle
  describes a trap with no graceful exit: you cannot retrain a person
  into someone they are not. Software, in principle, can be rewritten,
  rearchitected, or replaced. The metaphor imports a sense of
  inevitability and permanence that does not apply. The fact that teams
  often choose not to rewrite does not mean they cannot.
- **The promotion is not a single event** -- in organizations, promotion
  is a discrete act: on Monday you are an engineer, on Tuesday you are a
  manager. In software, scope creep is continuous. There is no single
  moment when the system was "promoted" beyond its competence. The
  metaphor imposes a step-function narrative onto what is usually a
  gradual slide, which may cause teams to miss the transition because
  they are looking for a moment that never comes.
- **Competence in software is not intrinsic** -- a person has a
  relatively fixed set of capabilities. Software's "competence" depends
  entirely on its architecture, which is a human choice. The metaphor
  suggests that software has a natural ceiling, like a person's talent.
  In reality, the ceiling is set by design decisions that can be revised.
  This framing can lead to premature abandonment of systems that could
  be adapted.
- **The metaphor blames the tool for the organization's failure** -- the
  Peter Principle is a critique of hierarchical promotion systems, not of
  the individuals promoted. But the software version typically blames the
  software ("it can't handle this scale") rather than the organization
  that failed to invest in rearchitecting it. The metaphor displaces
  organizational accountability onto an inanimate system.

## Expressions

- "This project has been Peter Principled" -- the diagnosis that
  software has been promoted beyond its architectural competence
- "We've promoted this script into a platform" -- rueful acknowledgment
  that a small tool has been given responsibilities it was never
  designed for
- "It's at its level of incompetence" -- applying Peter's diagnostic
  directly, meaning the software cannot handle its current role but
  will not be replaced
- "Every successful internal tool eventually becomes a liability" -- the
  generalized principle, expressing the inevitability of promotion-
  beyond-competence in organizational software
- "It was great when it was just a spreadsheet" -- nostalgia for the
  tool's original, competent scope

## Origin Story

Laurence J. Peter and Raymond Hull published *The Peter Principle: Why
Things Always Go Wrong* in 1969. Framed as satire, the book described a
genuine organizational pathology with enough precision that it entered
management theory as a serious concept. The Peter Principle became one
of the most widely cited ideas in organizational behavior, alongside
Parkinson's Law and the Dilbert Principle.

The application to software emerged organically in developer culture,
without a single canonical articulation. The pattern was too visible to
need formal description: every developer has watched a successful small
tool get pressed into service as a mission-critical system. The phrase
"software Peter Principle" appears in blog posts and conference talks
from the mid-2000s onward, though its exact coinage is difficult to
trace.

The concept gained renewed currency with the rise of microservices
architecture in the 2010s. The microservices movement was, in part, a
response to monolithic applications that had been Peter Principled --
applications that started as simple services and were promoted into
doing everything, badly. Decomposing a monolith into services is, in
the Peter Principle frame, demoting the monolith back to a scope it
can handle.

## References

- Peter, L. & Hull, R. *The Peter Principle: Why Things Always Go
  Wrong* (1969) -- the original formulation of the organizational
  principle
- Fowler, M. "Monolith First" (2015) -- pragmatic advice about
  starting small, implicitly addressing the promotion-beyond-competence
  pattern
- Spolsky, J. "Things You Should Never Do, Part I" (2000) -- the
  rewrite debate, closely related to the question of what to do when
  software reaches its level of incompetence