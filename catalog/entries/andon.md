---
slug: andon
name: Andon
summary: "Any worker can stop the line. Stopping is reframed as value creation, not cost, but it requires a culture where pulling the cord is safe."
kind: paradigm
source_frame: manufacturing
applies_to:
  - organizational-behavior
categories:
  - systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
  - poka-yoke
  - kanban
  - muda-mura-muri
  - heijunka
created: '2026-03-18'
updated: '2026-03-18'
grounding: established
embodied_patterns:
  - blockage
  - flow
  - link
relation_types:
  - prevent
  - enable
  - coordinate
structure: pipeline
abstraction_level: specific
harness: Claude Code
transfers:
  - "[paradigm] distributes quality authority to the lowest-level operator, making the person closest to the defect the one empowered to stop the entire line rather than routing the signal through management hierarchy"
  - "[paradigm] treats stopping production as a value-creating act rather than a cost, inverting the default assumption that throughput and quality compete"
  - "[paradigm] forces immediate collective response to problems by making them impossible to ignore -- the signal is visual, audible, and halts flow, preventing the accumulation of downstream defects"
limits:
  - "[paradigm] breaks in domains where stopping the line is irreversible or catastrophic -- a surgeon cannot halt a procedure the way a factory worker halts an assembly line, and emergency services cannot pause response while diagnosing a process failure"
  - "[paradigm] assumes that the person who detects the problem can also localize it, but in complex software systems the operator who sees the symptom (a failed test, an alert) is often distant from the root cause, making the 'stop and fix' response less effective than 'stop, investigate, and escalate'"
---

## Transfers

Andon (Japanese: lantern, lamp) is the visual signal system in the Toyota
Production System where any worker on the assembly line can pull a cord or
press a button to signal a problem, slowing or halting the line until the
issue is resolved. The andon board -- a lit display above the production
floor -- shows which station triggered the alert, making the problem visible
to everyone simultaneously.

Key structural parallels:

- **Authority at the point of detection** -- in traditional manufacturing
  hierarchies, line workers report problems upward and wait for permission
  to act. Andon inverts this: the worker who sees the defect has unilateral
  authority to stop the entire line. This distributes quality authority to
  the person with the most information, not the person with the most rank.
  In software, this maps to any-engineer-can-revert-a-deploy policies, CI
  systems that block merges on test failure, and on-call rotations where the
  responder has authority to roll back without waiting for approval.

- **Stopping is productive** -- andon reframes halting production from a
  cost to an investment. Every minute the line is stopped costs throughput,
  but every defect that passes downstream costs exponentially more to fix.
  The paradigm asserts that the cheapest time to fix a problem is right now,
  at the point of detection. In software, this is the principle behind
  failing builds loudly and immediately rather than allowing broken code to
  propagate through staging environments.

- **Visibility as a forcing function** -- the andon signal is not a private
  message. It is a public, ambient, impossible-to-ignore display. This
  prevents the organizational pathology of known-but-unacknowledged problems.
  When the light is on, everyone sees it, and social pressure ensures
  response. In software teams, this maps to build radiators, Slack channel
  alerts, and dashboard monitors that broadcast system health to the entire
  team rather than burying it in logs.

- **Structured escalation, not chaos** -- pulling the andon cord does not
  mean panic. It triggers a defined response protocol: the team leader
  arrives, the problem is diagnosed, and a decision is made to fix in place
  or escalate further. The system transforms ad hoc firefighting into a
  repeatable process. In incident management, this maps to runbooks,
  severity levels, and incident commander roles.

## Limits

- **Not all systems can be stopped** -- andon works because a factory line
  can be halted and restarted without catastrophic consequences. In domains
  where stopping is irreversible or dangerous (surgery, air traffic control,
  live financial trading), the paradigm must be adapted to "signal and
  mitigate" rather than "signal and stop." Applying andon logic literally
  to a running production system can cause more damage than the defect it
  was meant to catch.

- **Signal fatigue degrades the system** -- if the andon cord is pulled too
  frequently for minor issues, responders learn to treat every signal as
  noise. The paradigm works only when the signal threshold is calibrated
  correctly. In software, this is the alert fatigue problem: teams that
  receive hundreds of non-actionable alerts per day stop responding to any
  of them, and the andon system becomes decoration.

- **Detection and diagnosis are separate skills** -- andon assumes the
  worker who detects the problem can describe it well enough for rapid
  resolution. In complex systems (distributed software, organizational
  dysfunction), the person who sees the symptom may be far from the root
  cause. Stopping the line surfaces the symptom but does not automatically
  locate the disease. Without a diagnostic capability paired to the
  signaling system, andon becomes a way to stop work without fixing
  anything.

- **Cultural prerequisites are invisible** -- andon requires a culture where
  stopping the line is genuinely safe. If workers fear punishment for halting
  production, the cord exists but is never pulled. Toyota spent decades
  building the psychological safety that makes andon functional. Importing
  the mechanism without the culture produces a system where problems are
  still hidden, just through different channels.

## Expressions

- "Pull the andon cord" -- call attention to a problem and demand immediate
  response; used in software and management to mean escalating visibly
  rather than suffering silently
- "The build is red" -- CI/CD equivalent of the andon light; the visual
  signal that something is broken and no further changes should merge
- "Stop the line" -- used in agile and DevOps contexts to mean prioritizing
  a quality issue over feature velocity
- "Andon board" -- any real-time status display showing system health,
  from factory floor displays to engineering team dashboards
- "Anyone can pull the cord" -- shorthand for distributed authority over
  quality, emphasizing that seniority is not required to raise an alarm

## Origin Story

Andon originated at Toyota in the 1950s under Taiichi Ohno as part of the
jidoka (autonomation) pillar of the Toyota Production System. The word
"andon" literally means "lantern" in Japanese, referring to the paper-
covered lamps used in traditional Japanese architecture. At Toyota, it
became the name for the illuminated boards hung above the production line
that displayed station status.

The practice was revolutionary because it contradicted the prevailing
manufacturing wisdom that maximizing line uptime was the highest priority.
Ohno argued that a line running at full speed while producing defects was
worse than a line that stopped to fix problems. This required a fundamental
shift in how Toyota measured performance: not by output volume, but by
output quality.

Andon migrated into software engineering through the lean software movement
of the 2000s, particularly via Mary and Tom Poppendieck's *Lean Software
Development* (2003) and the DevOps movement of the 2010s. The concept
underlies continuous integration practices, where a failing test halts the
pipeline, and incident management frameworks, where any engineer can
declare an incident.

## References

- Ohno, T. *Toyota Production System: Beyond Large-Scale Production* (1988)
- Liker, J. *The Toyota Way* (2004) -- Principle 5: "Build a culture of
  stopping to fix problems"
- Poppendieck, M. and Poppendieck, T. *Lean Software Development* (2003)
- Kim, G. et al. *The Phoenix Project* (2013) -- andon cord as DevOps
  practice
