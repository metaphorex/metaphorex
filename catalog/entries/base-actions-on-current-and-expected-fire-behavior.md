---
slug: base-actions-on-current-and-expected-fire-behavior
name: Base Actions on Current and Expected Fire Behavior
kind: mental-model
source_frame: fire-safety
categories:
  - decision-making
  - risk-management
author: agent:metaphorex-miner
contributors: []
related:
  - size-up
  - lces
  - ooda-loop
created: '2026-03-21'
updated: '2026-03-21'
grounding: established
embodied_patterns:
  - path
  - flow
  - matching
relation_types:
  - cause
  - enable
  - select
structure: cycle
abstraction_level: specific
harness: Claude Code
transfers:
  - '[model] forces a separation between current state observation and trajectory prediction, requiring the decision-maker to answer "what IS the fire doing" and "what WILL it do" as distinct questions, which prevents the common error of assuming current conditions are stable'
  - '[model] mandates that action plans incorporate predicted future state rather than merely reacting to present symptoms, importing a forward-looking discipline that treats present conditions as a waypoint on a trajectory rather than a snapshot to be optimized against'
  - '[model] requires the operator to name the basis for their expectation -- weather forecast, fuel type, terrain -- making the prediction explicit and therefore auditable, which transfers to any domain where post-hoc accountability for decisions under uncertainty matters'
limits:
  - '[model] breaks because fire behavior prediction rests on well-understood physical laws (fuel moisture, wind speed, slope angle) that produce tractable forecasts within hours, while most organizational and software systems evolve through feedback loops, adversarial dynamics, or emergent behavior where "expected behavior" is not reliably derivable from current state'
  - '[model] misleads by implying that current and expected behavior are the only two inputs needed for a decision, omitting resource constraints, political context, stakeholder priorities, and other factors that legitimately shape action but have no analog in fire behavior'
---

## Transfers

Standard Fire Order #3 -- "Base all actions on current and expected fire
behavior" -- is one of the Ten Standard Fire Orders that govern US
wildland firefighting operations. It encodes a deceptively simple
discipline: do not act on what the fire was doing when you last checked,
and do not act on what you wish it were doing. Act on what it IS doing
right now and what it WILL do based on identifiable factors.

Key structural parallels:

- **Current vs. expected as distinct cognitive tasks** -- the order
  separates two questions that untrained decision-makers habitually merge.
  "Current behavior" requires direct observation: where is the fire, how
  fast is it moving, what is it consuming? "Expected behavior" requires
  prediction: given wind forecasts, terrain ahead, fuel type, and time of
  day, what will the fire do in the next hours? A fire that is currently
  creeping slowly through damp ground-level fuel may be 30 minutes away
  from reaching a dry slope where it will crown and run. A decision based
  only on current behavior deploys resources for a creeping fire; a
  decision based on expected behavior prepares for a running crown fire.
  In incident response, the parallel is distinguishing between current
  system symptoms and projected cascade effects.

- **Prediction must be grounded and named** -- firefighters do not
  predict fire behavior through intuition alone. They use specific inputs:
  the Haines Index (atmospheric stability), fuel moisture readings, wind
  speed and direction, slope percentage, time of day (diurnal wind
  patterns). The order requires that the prediction be based on identifiable,
  communicable factors. This makes the expectation auditable: after an
  incident, reviewers can ask "what factors did you base your expected
  behavior on?" and evaluate whether the prediction was reasonable. In
  software engineering, this maps to requiring that capacity planning
  decisions cite specific metrics (request rate trends, resource
  utilization curves) rather than vague appeals to "growth."

- **Action must track changing reality** -- the word "base" is critical.
  Actions are not decided once and then executed; they are continuously
  re-based on updated observation and prediction. If the wind shifts, the
  expected behavior changes, and actions must change with it. This creates
  a discipline of continuous recalibration that resists the sunk-cost
  trap: resources committed to a plan based on yesterday's fire behavior
  must be redeployed when today's behavior diverges. In project management,
  this maps to re-evaluating a roadmap when market conditions change rather
  than completing a plan because it was already approved.

- **The order is a decision filter, not a decision rule** -- it tells
  you what to base your decision on, not what decision to make. Two
  commanders observing the same fire behavior may make different tactical
  choices depending on available resources, crew fatigue, and values at
  risk. The order constrains the input, not the output. This transfers
  to any domain where decision frameworks need to standardize the evidence
  basis without prescribing the conclusion.

## Limits

- **Prediction tractability does not transfer** -- fire behavior is
  governed by physics. Given fuel type, moisture content, wind speed,
  slope angle, and atmospheric stability, an experienced firefighter can
  predict fire movement with useful accuracy over a span of hours. This
  tractability is a feature of the physical domain, not of the mental
  model. In organizational contexts, "expected behavior" of a market, a
  competitor, or a complex software system is not derivable from a small
  set of observable inputs. Importing the fire order's confidence in
  prediction leads to overconfident forecasting in domains where the
  equivalent physics do not exist.

- **Two inputs are not enough** -- the fire order works because in
  wildland fire, the decision-relevant factors genuinely reduce to fire
  behavior. Other factors (crew morale, resource availability, political
  pressure) are handled by other orders and protocols. In most
  organizational decisions, current state and predicted trajectory are
  necessary but radically insufficient inputs. Strategy must also weigh
  resource constraints, stakeholder alignment, regulatory environment,
  and opportunity costs that have no analog in fire behavior analysis.

- **Temporal horizon mismatch** -- fire behavior prediction is useful
  over hours to a day. The order's rhythm of "observe, predict, act,
  re-observe" maps onto fast tactical decisions. Many organizational
  decisions require prediction over months or years, where the
  compounding of uncertainty makes "expected behavior" more aspiration
  than forecast. Applying the fire order's confident predictive stance
  to long-horizon decisions imports a false precision.

- **The order assumes observable current state** -- firefighters can see
  the fire. They have direct sensory access to current behavior. In many
  organizational contexts, "current state" is itself uncertain: the team
  does not know how many users are affected, how much revenue is at risk,
  or what the competitor is actually doing. The order's clean separation
  of current and expected behavior assumes that current behavior is known,
  which is often the harder problem in non-fire domains.

## Expressions

- "What is the fire doing? What will it do?" -- the canonical two-question
  formulation, used in fire briefings
- "Base your actions on current and expected behavior" -- the full order,
  invoked in training and after-action reviews
- "The fire doesn't care about your plan" -- the folk corollary,
  emphasizing that plans must yield to observed reality
- "Are we planning for the fire we have or the fire we'll have in an
  hour?" -- the predictive challenge, applied in incident management
- "What's the expected behavior of this system under load?" -- software
  engineering transfer of the two-question discipline

## Origin Story

The Ten Standard Fire Orders were established in 1957 by a task force
convened after the Inaja fire in California, which killed 11 firefighters.
The task force, led by the US Forest Service, studied military general
orders as a structural model and drafted ten orders intended to prevent
the specific failure modes identified in fatality investigations. Order
#3 -- "Base all actions on current and expected fire behavior" -- addressed
the recurring finding that crews had acted on outdated or wishful
assessments of fire conditions.

The orders were refined after subsequent tragedies, including the 1994
South Canyon fire (14 fatalities) and the 2013 Yarnell Hill fire (19
fatalities). In both cases, investigations found that crews had failed to
update their assessment of fire behavior as conditions changed -- acting
on the fire they had briefed, not the fire they faced. The order's
emphasis on "current AND expected" -- not one or the other -- reflects
this hard-won lesson about the gap between briefed conditions and actual
conditions.

## References

- National Wildfire Coordinating Group, *Incident Response Pocket Guide*
  (PMS 461), current edition -- contains the Ten Standard Fire Orders
- "Report of Task Force on Study of Fatal and Near-Fatal Fires,"
  USDA Forest Service, 1957 -- origin of the Ten Standard Fire Orders
- Maclean, N. *Young Men and Fire* (1992) -- Mann Gulch disaster,
  foundational text on fire decision-making
- Marsh, R. "Yarnell Hill Fire Serious Accident Investigation Report,"
  Arizona State Forestry Division, 2013 -- case study of failure to
  re-assess expected fire behavior
