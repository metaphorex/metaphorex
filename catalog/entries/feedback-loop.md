---
slug: feedback-loop
name: Feedback Loop
kind: mental-model
source_frame: systems-thinking
categories:
  - systems-thinking
  - decision-making
author: agent:metaphorex-miner
harness: Claude Code
contributors: []
related:
  - feedback-loops
  - equilibration
  - thermostat-model
grounding: established
created: '2026-03-21'
updated: '2026-03-21'
embodied_patterns:
  - iteration
  - flow
  - force
relation_types:
  - cause/propagate
  - restore
structure: cycle
abstraction_level: generic
transfers:
  - '[model] A system''s output becomes its own input, so the consequence of an action alters the conditions for the next action -- making cause and effect circular rather than linear'
  - '[model] Positive loops amplify deviation from an initial state while negative loops dampen it, and correctly classifying which type is operating determines whether intervention should brake or steer'
  - '[model] Delays between output and re-input create oscillation and overshoot, explaining why corrections that respond to past states reliably worsen present conditions'
limits:
  - '[model] The loop abstraction presupposes that the system has a stable enough structure to route outputs back as inputs -- in systems undergoing structural change, the "loop" itself is being rewritten, and the model cannot represent its own dissolution'
  - '[model] Identifying a feedback loop requires choosing system boundaries, and different boundary choices yield different loops from the same phenomena -- the model suggests loops are discovered rather than constructed'
---

## Transfers

A feedback loop is the minimal unit of circular causation: output from a
process re-enters as input, modifying the process's next iteration. The
concept originates in control engineering (Watt's governor, Wiener's
cybernetics) and transfers to any domain where consequences feed back into
causes.

The structural mechanism that transfers:

- **Circular causation replaces linear causation** -- in a feedback loop,
  asking "what caused X?" has no terminal answer because X partly caused
  itself through prior iterations. The cognitive move is to stop looking for
  a root cause and start tracing the circuit. This restructures problem-solving:
  instead of fixing a cause, you modify the loop. A thermostat does not fix
  temperature; it modifies the heating loop.

- **Amplification vs. stabilization** -- positive feedback amplifies any
  deviation from the current state (compound interest, viral growth, panic
  selling). Negative feedback dampens deviation and restores a reference state
  (a thermostat, blood sugar regulation, editorial review cycles). The
  cognitive tool is classification: when you see a runaway process, ask
  whether a positive loop is operating. When you see stubborn stasis, ask
  what negative loop is holding it in place.

- **Delay is the source of instability** -- when feedback is instantaneous,
  negative loops stabilize perfectly and positive loops accelerate smoothly.
  Real systems have delays: the economy responds to interest rate changes
  months later; a new hire's impact on team velocity takes quarters to
  manifest. Delayed feedback causes overshoot and oscillation because
  corrective action responds to past states, not current ones. The practical
  implication: the longer the delay, the gentler the correction should be.

- **Loop dominance determines system behavior** -- most real systems contain
  multiple feedback loops operating simultaneously. Which loop dominates at a
  given moment determines what the system does. A startup's growth loop
  (more users, more revenue, more development) may dominate early, then yield
  to a quality loop (more users, more bugs, worse experience, fewer users).
  The analytical task is identifying which loop currently dominates and what
  could shift dominance.

## Limits

- **Not all causation is circular** -- the feedback loop model encourages
  seeing loops everywhere, but some causal chains are genuinely one-directional.
  An asteroid impact causes an extinction event without a feedback mechanism
  linking extinction back to asteroid frequency. Forcing linear causation into
  a loop framework adds complexity without insight.

- **Boundary dependence** -- drawing a feedback loop requires deciding what
  is inside the system and what is external. Different boundary choices produce
  different loops from the same data. Two analysts can look at the same market
  and draw contradictory loop diagrams, each internally consistent. The model
  implies that feedback loops are properties of the system being observed, but
  they are equally properties of the observer's framing choices.

- **The "positive = good" confusion** -- in everyday language, "positive
  feedback" means praise. In systems thinking, it means amplification -- which
  includes bank runs, arms races, and ecological collapse. This terminological
  collision causes consistent misapplication in organizational settings where
  "positive feedback loop" is reflexively treated as a desirable state.

- **Agency dissolves into arrows** -- loop diagrams represent human decisions
  as variables influencing other variables. The person disappears, replaced
  by a node in the circuit. This is analytically useful when structural forces
  genuinely override individual choice, but it can also serve as an
  accountability shield: "the system produces this outcome" substitutes for
  "these people made these choices."

## Expressions

- "Vicious cycle" / "virtuous cycle" -- colloquial names for positive
  feedback loops with undesirable and desirable outcomes respectively
- "Flywheel effect" -- Jim Collins's business metaphor for a positive loop
  that builds momentum through successive iterations
- "Death spiral" -- a positive feedback loop running toward system collapse,
  common in insurance and organizational contexts
- "Self-correcting mechanism" -- negative feedback in institutional settings,
  as in "checks and balances"
- "Doom loop" -- organizational negative spiral where failed strategies
  trigger panic pivots that fail in turn
- "Runaway effect" -- positive feedback without a natural governor or check

## Origin Story

The concept traces to James Watt's centrifugal governor (1788), a mechanical
device that used steam engine output speed to regulate steam input, creating a
physical negative feedback loop. Norbert Wiener formalized the concept in
*Cybernetics* (1948), extending it from mechanical to biological and social
systems. Jay Forrester applied feedback analysis to industrial and urban
systems at MIT in the 1960s, and Peter Senge popularized it for management
audiences in *The Fifth Discipline* (1990). The feedback loop has since become
arguably the most widely exported concept from engineering to the social
sciences.

## References

- Wiener, N. *Cybernetics: or Control and Communication in the Animal and
  the Machine* (1948)
- Forrester, J. *Industrial Dynamics* (1961)
- Meadows, D. *Thinking in Systems: A Primer* (2008)
- Senge, P. *The Fifth Discipline: The Art and Practice of the Learning
  Organization* (1990)
