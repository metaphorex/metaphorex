---
slug: know-what-your-fire-is-doing
name: Know What Your Fire Is Doing
summary: "The possessive 'your' assigns personal observation duty. You own awareness of the specific threat you are engaging."
kind: mental-model
source_frame: fire-safety
categories:
- decision-making
- risk-management
author: agent:metaphorex-miner
contributors: []
related:
- ten-standard-fire-orders
- base-actions-on-current-and-expected-fire-behavior
- size-up
- ooda-loop
- lces
provenance: firefighting-maxims
created: '2026-03-26'
updated: '2026-03-26'
grounding: established
harness: Claude Code
embodied_patterns:
  - matching
  - flow
  - path
relation_types:
  - cause
  - enable
  - select
structure: cycle
abstraction_level: specific
transfers:
  - '[model] "know" demands continuous, active observation -- not a one-time briefing or an initial assessment -- importing the discipline that situational awareness is an ongoing process, not a state achieved once and retained'
  - '[model] "your fire" assigns personal ownership of observation to the operator engaging the specific threat, importing the principle that situational awareness cannot be fully delegated -- the person in contact with the hazard bears the primary duty to monitor it'
  - '[model] the order treats the fire as an agent with its own behavior ("what YOUR FIRE is doing"), importing the frame where the threat is an active, changing entity whose actions must be tracked like an adversary''s, not a static condition to be assessed once'
limits:
  - '[model] breaks because fire behavior is directly observable (visible flame, smoke, heat) while many organizational threats -- technical debt, market shifts, cultural erosion -- are invisible or legible only through lagging indicators, making "know what your fire is doing" aspirational rather than actionable in domains with low observability'
  - '[model] misleads by implying that the operator can know what the fire is doing through direct observation alone, when in complex systems the relevant "fire behavior" may be distributed across subsystems, time zones, or organizational boundaries that no single observer can monitor'
  - '[model] obscures the cognitive load problem: on an active fire line, continuous monitoring of fire behavior competes with the attentional demands of the work itself, and the order provides no guidance on how to allocate attention between doing the work and watching the threat -- a tension that transfers directly to incident response'
---

## Transfers

Standard Fire Order #2 -- "Know what your fire is doing at all times" --
establishes continuous situational awareness as the foundational
discipline of wildland firefighting. It is the second order, immediately
following "Keep informed on fire weather conditions and forecasts"
(Order #1), and together they establish the observation requirements
that must precede all operational action. The order is distinctive in
three ways: "know" (not "check" or "assess"), "your" (not "the"), and
"at all times" (not "periodically").

Key structural parallels:

- **Continuous, not periodic** -- "at all times" distinguishes this
  order from a check-in protocol or a scheduled assessment. The
  firefighter must maintain awareness of fire behavior as an ongoing
  cognitive process, not a task completed at intervals. On the fire
  line, this means looking up from the immediate work regularly,
  monitoring smoke column behavior, noting wind shifts, and tracking
  the fire's movement relative to escape routes. The order rejects
  the common failure mode of becoming absorbed in the task and losing
  awareness of the environment. In incident response, the parallel is
  maintaining a live dashboard or continuous monitoring feed -- not a
  status report produced every four hours.

- **Personal ownership through the possessive** -- "your fire" is not
  "the fire." The possessive assigns observation duty to the individual
  firefighter engaging a specific section of the fire. This matters
  because large fires involve multiple crews on different assignments.
  Each crew owns the observation duty for their portion. The order
  says you cannot rely entirely on the incident commander's overview,
  the lookout's report, or the weather service's forecast. The person
  in direct contact with the threat bears primary responsibility for
  monitoring it. In software operations, this transfers to the
  principle that the engineer deploying a change owns monitoring that
  deployment's behavior, not the SRE team in general.

- **The fire is an active agent** -- the phrasing "what your fire is
  doing" attributes agency to the fire. Fire is not a static hazard
  but a dynamic entity that moves, grows, changes direction, and
  responds to environmental inputs. This framing imports an adversarial
  awareness: you must track the fire the way you would track an
  opponent, anticipating its next move based on fuel, terrain, and
  weather. In security, this maps to treating the threat as an
  intelligent actor. In project management, it maps to treating a
  risk as an evolving condition rather than a fixed line item.

- **Knowledge as prerequisite for all other orders** -- the order's
  position (#2) makes it a prerequisite for all subsequent orders.
  You cannot "base actions on current and expected fire behavior"
  (Order #3) without first knowing what the fire is doing. You
  cannot "identify escape routes" (Order #4) without knowing where
  the fire is relative to your position. The order establishes
  observation as the foundation that supports every operational
  decision. In any operational domain, the equivalent principle is
  that you cannot act soundly on information you have not gathered.

## Limits

- **Observability does not transfer** -- wildfire is directly
  observable. Flame is visible. Smoke columns indicate intensity and
  direction. Heat can be felt. Sound changes as fire crowns or
  accelerates. The firefighter has multiple sensory channels providing
  real-time information about fire behavior. Most organizational
  "fires" -- system degradation, competitive threats, cultural
  dysfunction, technical debt -- are not directly observable. They
  manifest through lagging indicators, ambiguous signals, and metrics
  that are themselves imperfect proxies. The order's confident "know"
  assumes a level of observability that many domains do not provide.

- **Single-observer assumption** -- the order works because one
  firefighter can observe their section of fire. Large-scale
  organizational threats often cannot be comprehended by any single
  observer. A distributed systems incident involves behavior across
  dozens of services, databases, and network paths. No one engineer
  can "know what the fire is doing" in the way a wildland firefighter
  can know their section of fire. The order scales down, not up: it
  describes a local observation duty that does not aggregate cleanly
  into enterprise-wide situational awareness.

- **Attention competition** -- on the fire line, monitoring fire
  behavior competes with doing the work: cutting line, deploying hose,
  operating equipment. The order says "at all times," but the
  firefighter's attention is finite. This tension -- between working
  and watching -- is the central cognitive challenge on the fire line
  and the primary mechanism by which experienced crews are caught off
  guard: they were doing the work and stopped watching the fire. The
  order mandates awareness but provides no guidance on how to allocate
  attention between production and surveillance. This transfers
  directly to every operational domain where the people doing the work
  are also responsible for monitoring the environment.

- **It can produce hypervigilance** -- "at all times" taken literally
  demands continuous anxiety about the threat. On a long fire
  assignment, this is unsustainable. Firefighters must rest, eat, and
  manage fatigue. The practical implementation involves teams,
  lookouts, and rotations that allow individuals to reduce their
  monitoring burden without the fire going unwatched. The order's
  absolutist language does not describe actual practice but sets an
  aspirational standard that must be operationalized through systems
  rather than individual heroics.

## Expressions

- "Know what your fire is doing at all times" -- the full order, used
  in training and briefings
- "What's the fire doing?" -- the fundamental question, used as a
  verbal check on situational awareness during operations
- "Eyes on the fire" -- operational shorthand for maintaining
  observation discipline
- "We lost situational awareness" -- the after-action diagnosis when
  this order is violated, used in both fire and organizational
  incident reviews
- "Keep your head on a swivel" -- military and law enforcement
  equivalent, emphasizing continuous environmental scanning
- "What's this system doing right now?" -- the software engineering
  translation, applied during deployments and incident response

## Origin Story

The Ten Standard Fire Orders were established in 1957 by a US Forest
Service task force convened after the 1956 Inaja fire in California,
which killed 11 firefighters. The task force, studying military
general orders as a structural model, drafted ten orders designed to
prevent the specific failure modes identified in fatality
investigations. Order #2 addressed the recurring finding that crews
were caught by fire behavior they had not been monitoring.

The order's emphasis on personal ownership ("your fire") and
continuous awareness ("at all times") reflects the investigation
finding that in most fatality incidents, someone knew what the fire
was doing -- but that information had not reached the crew in contact
with the hazard. The order cuts through communication failures by
placing the observation duty on the person most at risk, rather than
relying on centralized information distribution.

The Yarnell Hill fire of 2013, which killed 19 members of the Granite
Mountain Hotshots, provided a devastating case study. The crew lost
contact with their lookout and moved into a drainage without current
knowledge of the fire's location or behavior. They were overrun by
fire that had changed direction due to thunderstorm outflow winds.
The investigation found that the fundamental failure was a loss of
situational awareness: they did not know what their fire was doing.

## References

- National Wildfire Coordinating Group, *Incident Response Pocket Guide*
  (PMS 461), current edition -- contains the Ten Standard Fire Orders
- "Report of Task Force on Study of Fatal and Near-Fatal Fires,"
  USDA Forest Service, 1957 -- origin document
- "Yarnell Hill Fire Serious Accident Investigation Report," Arizona
  State Forestry Division, 2013 -- case study of Order #2 failure
- Weick, K. E. "The Collapse of Sensemaking in Organizations: The
  Mann Gulch Disaster" (1993) -- organizational theory analysis of
  firefighting situational awareness failure
