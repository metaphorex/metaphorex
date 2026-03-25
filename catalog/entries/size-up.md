---
slug: size-up
name: Size-Up
summary: "Four questions before committing resources: What do I have? What is it doing? Where is it going? What do I need? State vs. trajectory."
kind: mental-model
source_frame: fire-safety
categories:
  - risk-management
  - decision-making
author: agent:metaphorex-miner
contributors: []
related:
  - lces
  - ooda-loop
created: '2026-03-19'
updated: '2026-03-19'
grounding: established
harness: Claude Code
transfers:
  - '[model] structures assessment around four sequential questions (What do I have? What is it doing? Where is it going? What do I need?) that force the observer to separate current state from trajectory from resource requirements, preventing the common error of jumping from observation to action without modeling change'
  - '[model] mandates assessment before resource commitment, building a temporal buffer between arrival and action that resists the urgency bias inherent in emergency situations'
limits:
  - '[model] breaks when the situation is adversarial rather than physical, because the four questions assume the threat has legible behavior governed by discoverable laws, while an adversary actively conceals state and changes trajectory in response to observation'
  - '[model] misleads by implying that a single size-up produces a stable picture, when in rapidly evolving situations the assessment is obsolete before the response plan derived from it can be executed'
embodied_patterns:
  - matching
  - path
  - boundary
relation_types:
  - prevent
  - transform
  - compete
structure: hierarchy
abstraction_level: generic
---

## Transfers

Size-up is the structured assessment protocol a fire officer performs
upon arrival at an incident, before committing any resources. It
follows a canonical sequence of questions: What do I have? What is it
doing? Where is it going? What do I need? The protocol converts the
chaos of arrival into an actionable mental model by forcing sequential
attention to distinct aspects of the situation.

Key structural parallels:

- **Four questions, four cognitive modes** -- the size-up sequence
  moves through distinct analytical tasks. "What do I have?" is
  identification -- classifying the type, scale, and nature of the
  incident. "What is it doing?" is observation of current dynamics.
  "Where is it going?" is prediction based on those dynamics. "What
  do I need?" is resource matching. Each question requires a different
  cognitive mode, and the sequence prevents a common failure: jumping
  from a partial observation ("it's a big fire") directly to resource
  requests without modeling the trajectory. In software incident
  response, the same sequence applies: What system is affected? What
  are the current symptoms? What will degrade next? What do we need
  to contain it?

- **Assessment before commitment** -- the size-up creates an
  intentional pause between arrival and action. Under stress, the
  natural impulse is to act immediately -- deploy resources, attack
  the fire, begin remediation. Size-up mandates a temporal buffer
  that resists this urgency. The structural insight is that minutes
  spent understanding the situation save hours spent on the wrong
  response. In medical triage, the parallel is the primary survey
  before intervention. In product management, it is the diagnostic
  phase before the roadmap.

- **Dynamic reassessment** -- size-up is not performed once. It is
  repeated as conditions change. The protocol creates a cognitive
  rhythm: act, reassess, adjust. This maps onto the OODA loop
  (Observe, Orient, Decide, Act) but with a more specific structure
  for the observation and orientation phases. In incident management,
  it corresponds to the practice of periodic status updates that
  re-answer the four questions rather than simply reporting actions
  taken.

- **Separation of state from trajectory** -- the distinction between
  "what is it doing?" and "where is it going?" is the model's most
  transferable insight. Current state and future trajectory are
  different questions requiring different evidence. A fire that is
  currently small but moving uphill toward dry fuel in rising wind
  is a different problem from a fire that is currently large but
  burning into wet ground with no wind. Teams that conflate present
  severity with future risk make systematically poor resource
  allocation decisions.

## Limits

- **Assumes legible behavior** -- size-up works because fire obeys
  physics. Fuel, weather, and topography produce predictable behavior
  that an experienced officer can read. In domains with adversarial
  agents (cybersecurity, competitive strategy, negotiation), the
  "what is it doing?" and "where is it going?" questions may have
  no stable answers because the threat is actively adapting to the
  observer's response. Size-up assumes a system that can be modeled;
  adversaries resist modeling.

- **Single-observer bottleneck** -- the canonical size-up is performed
  by the incident commander, a single decision-maker. This works for
  geographically bounded incidents visible from one vantage point.
  For distributed systems, organizational crises, or multi-front
  situations, no single observer can perform a meaningful size-up.
  The model needs to be parallelized and synthesized, which introduces
  coordination costs that the original protocol does not address.

- **Speed-accuracy tradeoff** -- the size-up mandates a deliberate
  pause, but some situations genuinely cannot wait. A structure
  fire with occupants trapped does not permit the same assessment
  time as a wildland fire on open ground. The model does not
  specify how to calibrate the depth of assessment to the urgency
  of the situation, and importing it wholesale into fast-moving
  domains can introduce dangerous delay.

- **Retrospective coherence bias** -- the four-question structure
  creates a narrative that feels complete: I know what I have, what
  it is doing, where it is going, and what I need. This sense of
  completeness can be illusory. The officer may have missed a
  critical factor (hidden fuel load, unreported chemical storage,
  a second fire front) that the four questions did not surface.
  The structured completeness of size-up can suppress the
  uncertainty that should trigger more investigation.

## Expressions

- "Give me a size-up" -- requesting a structured assessment before
  committing resources
- "What do we have?" -- the opening question, now used generically
  in incident response and crisis management
- "Where is this going?" -- the predictive question, applied to
  project risk, market dynamics, and organizational change
- "We need to size this up before we react" -- invoking the
  assessment-before-action principle
- "The size-up was wrong" -- acknowledging that initial assessment
  was based on incomplete information, used in after-action reviews

## Origin Story

Size-up as a formalized protocol dates to the professionalization of
urban firefighting in the mid-twentieth century, codified in materials
from the National Fire Academy and International Fire Service Training
Association (IFSTA). The four-question sequence (What do I have? What
is it doing? Where is it going? What do I need?) became standard
training content for fire officers and was later incorporated into
the Incident Command System (ICS).

The protocol's transfer to other domains accelerated through two
channels. First, emergency management professionals who trained in
ICS carried the size-up concept into disaster response, public
health, and law enforcement. Second, writers on organizational
decision-making -- particularly those influenced by Karl Weick's
work on sensemaking in high-reliability organizations -- recognized
the size-up as a canonical example of structured sensemaking under
time pressure. Todd Conklin and Sidney Dekker reference firefighting
protocols extensively in their work on safety culture and human
performance in complex systems.

## References

- International Fire Service Training Association (IFSTA),
  *Essentials of Fire Fighting*, current edition
- National Fire Academy, "Decision Making for Initial Company
  Operations" (course materials)
- Weick, K. "The Collapse of Sensemaking in Organizations: The
  Mann Gulch Disaster," *Administrative Science Quarterly* 38(4),
  1993
- Gasaway, R. *Size-Up, Assessment and Decision Making* (2014)
