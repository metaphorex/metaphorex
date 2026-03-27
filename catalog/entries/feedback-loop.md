---
slug: feedback-loop
name: Feedback Loop
summary: "Output routed back as input: a system that senses its own effects and adjusts accordingly. The loop, not the parts, explains the behavior."
kind: metaphor
source_frame: cybernetics
applies_to:
- systems-thinking
- organizational-behavior
categories:
- systems-thinking
- cognitive-science
author: agent:metaphorex-miner
contributors: []
related:
- feedback-loops
- homeostasis
- leverage-point
- strange-loop
- equilibration
- ooda-loop
created: '2026-03-26'
updated: '2026-03-26'
grounding: established
harness: Claude Code
transfers:
  - "[source] maps the engineering structure of output-routed-back-as-input onto any system where effects circle back to influence causes, making circular causation visible where linear thinking sees only chains"
  - "[source] imports the distinction between positive feedback (amplifying deviation) and negative feedback (correcting toward a set-point), providing a vocabulary for why some processes spiral and others stabilize"
  - "[source] carries the insight that delays in the loop produce oscillation and overshoot, explaining why well-intentioned corrections often worsen the problem they were meant to fix"
limits:
  - "[source] breaks because the engineering metaphor implies clean signal paths and measurable variables, while real social and organizational feedback involves ambiguous signals, contested measurements, and actors who game the sensors"
  - "[source] misleads by encouraging loop-seeing everywhere, including where causation is genuinely linear -- forcing every phenomenon into circular structure obscures cases where A simply causes B with no return path"
  - "[source] obscures agency by replacing actors with arrows and variables, turning human choices into mechanical responses and making 'the system produces this outcome' an excuse for individual inaction"
embodied_patterns:
  - iteration
  - flow
  - force
relation_types:
  - cause
  - restore
structure: cycle
abstraction_level: generic
---

## Transfers

In control engineering, a feedback loop exists when a system's output is
routed back to become its input. A thermostat measures room temperature
(output of the heating system), compares it to the set-point, and adjusts
the heater (input). The loop -- sense, compare, adjust -- is the unit of
analysis, not the individual components. When this structure is mapped onto
non-engineering domains, it fundamentally changes how we think about cause
and effect.

Key structural parallels:

- **Circular causation replaces root-cause thinking** -- in a feedback loop,
  the question "what caused X?" has no terminal answer because X partly caused
  itself through prior iterations. A manager sees declining morale, institutes
  surveillance, which further declines morale, which triggers more
  surveillance. The engineering metaphor teaches you to stop looking for the
  first cause and start tracing the circuit. The intervention point is the
  loop structure, not any single event in it.

- **Two species of loop** -- engineering distinguishes negative feedback
  (error-correcting, stabilizing) from positive feedback (deviation-amplifying,
  destabilizing). A budget review that detects overspending and triggers cuts
  is negative feedback. A viral post that attracts attention, which attracts
  more attention, is positive feedback. The metaphor's power is that it gives
  both phenomena the same structural name, revealing that a thermostat and a
  bank run are instances of the same abstract pattern.

- **Delays as the source of dysfunction** -- in engineering, a feedback loop
  with a time delay produces oscillation. The thermostat with a slow sensor
  overshoots the target temperature, then overcorrects, producing cycles. The
  metaphor maps this onto economic cycles (farmers plant for last year's
  prices), hiring decisions (recruiting for last quarter's demand), and policy
  (regulating for yesterday's crisis). The insight is specific: the problem is
  not that the feedback exists but that the delay between action and
  measurement causes the system to correct for conditions that no longer hold.

- **Loop dominance** -- complex systems contain many feedback loops operating
  simultaneously. Which loop dominates at any moment determines the system's
  behavior. A startup has a positive growth loop (users attract developers
  attract users) and a negative quality loop (users generate bugs, bugs repel
  users). The engineering metaphor directs attention to the question of
  dominance: not "which loops exist?" but "which loop is winning right now,
  and what could shift it?"

## Limits

- **Social feedback is not engineering feedback** -- in a thermostat, the
  sensor is objective, the signal path is clean, and the actuator responds
  deterministically. In organizations, the "sensor" is a manager's
  perception, the "signal" is filtered through politics and self-interest,
  and the "actuator" is a person who may resist, reinterpret, or game the
  response. The engineering metaphor imports a precision and reliability
  that social feedback systems do not possess. Treating organizational
  feedback as if it were thermostat-like encourages designing systems
  that assume clean signals, then being surprised when they fail.

- **Not everything is a loop** -- the metaphor's greatest danger is
  overapplication. Some causal chains are genuinely linear: an asteroid
  strikes, a species goes extinct. There is no feedback path from the
  extinction back to the asteroid. Forcing every phenomenon into loop
  structure -- "but isn't there always feedback?" -- is a form of
  theoretical imperialism that obscures simple causation. The question to
  ask is whether the putative return path actually carries a signal strong
  enough to influence the original cause.

- **"Positive" does not mean "good"** -- the engineering terminology is
  actively misleading in everyday language. "Positive feedback" sounds
  affirming; in engineering it means amplifying, which includes arms
  races, addiction spirals, and financial bubbles. The terminological
  confusion is not trivial -- it leads to consistent misuse in business
  contexts where "positive feedback loop" is treated as synonym for
  "virtuous cycle," obscuring the fact that many positive feedback
  processes are destructive.

- **Agency dissolves in the diagram** -- feedback loop diagrams show
  variables connected by arrows. People disappear, replaced by "stocks"
  and "flows." This is analytically powerful -- it reveals structure
  independent of personality -- but it also dehumanizes. When a system
  dynamics diagram shows "employee dissatisfaction" flowing into
  "turnover" flowing into "workload" flowing back into "dissatisfaction,"
  the employees have become fluid in a pipe. The metaphor makes it easy
  to say "the system produces this outcome" without asking who benefits
  from the system staying the way it is.

## Expressions

- "There's a feedback loop here" -- identifying circular causation in a
  business or social situation
- "Positive feedback loop" / "negative feedback loop" -- distinguishing
  amplifying from stabilizing dynamics, often with the positive/negative
  confusion described above
- "Closing the loop" -- establishing a return signal path where none
  existed, common in product development and management discourse
- "Breaking the loop" -- intervening to disrupt a self-reinforcing cycle,
  especially a destructive one
- "Tightening the feedback loop" -- reducing delay between action and
  signal, a core principle of agile development and lean manufacturing
- "Feedback-driven" -- organizational self-description emphasizing
  responsiveness to signals from customers, employees, or markets

## Origin Story

The concept of mechanical feedback dates to James Watt's centrifugal
governor (1788), which regulated steam engine speed by feeding rotational
output back to a throttle valve. The mathematical theory was formalized by
James Clerk Maxwell in "On Governors" (1868). Norbert Wiener coined
"cybernetics" in 1948, generalizing feedback from machines to biological
and social systems. The metaphor entered management through Jay Forrester's
system dynamics work at MIT in the 1960s and was popularized for business
audiences by Peter Senge's *The Fifth Discipline* (1990). Today "feedback
loop" is so thoroughly absorbed into general discourse that most users
employ it without awareness of its engineering origin -- a dead metaphor
that still structures how millions of people think about cause and effect.

## References

- Wiener, N. *Cybernetics: Or Control and Communication in the Animal
  and the Machine* (1948)
- Maxwell, J.C. "On Governors" (1868) -- foundational mathematical
  treatment
- Forrester, J. *Industrial Dynamics* (1961) -- feedback applied to
  business systems
- Senge, P. *The Fifth Discipline* (1990) -- popularized for management
- Meadows, D. *Thinking in Systems* (2008) -- accessible modern treatment
