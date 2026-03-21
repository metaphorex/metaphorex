---
applies_to:
- security-analysis
author: agent:metaphorex-miner
categories:
- security
- systems-thinking
contributors: []
created: '2026-03-18'
dead: true
grounding: folk
harness: Claude Code
kind: metaphor
limits:
- "[source] imports the assumption that damage attenuates with distance from the point of detonation, but in software systems a single compromised credential or service can propagate damage to arbitrarily distant components with no attenuation"
- "[source] frames damage as radiating outward from a single point of origin, but software failures often cascade through dependency chains and shared state in patterns that have no spatial analog"
- "[source] implies that blast radius is a fixed, measurable property of the weapon, while in software the scope of impact depends on runtime context, configuration, and the state of the system at the moment of failure"
name: Blast Radius
related:
- defense-in-depth
- supply-chain-attack
slug: blast-radius
source_frame: war
transfers:
- "[source] maps the physical zone of destruction surrounding an explosion onto the scope of systems, services, or data affected by a single security compromise or operational failure"
- "[source] imports the military practice of estimating damage zones before engagement, structuring security and operations thinking around pre-incident impact assessment and failure-domain sizing"
- "[source] carries the principle that containment (blast walls, distance, hardening) reduces the zone of destruction, mapping onto architectural practices like microservices, network segmentation, and least-privilege access that limit how far a failure can propagate"
updated: '2026-03-18'
embodied_patterns:
  - center-periphery
  - boundary
  - scale
relation_types:
  - cause
  - contain
  - prevent
structure: boundary
abstraction_level: generic
---

## Transfers

When a bomb detonates, the blast radius is the area within which
damage occurs. Damage is most severe at the center and attenuates with
distance. The metaphor maps this spatial damage model onto the scope
of impact from a security compromise or system failure.

- **Damage has scope** -- the core transfer. Before "blast radius"
  entered security and operations vocabulary, practitioners lacked a
  concise term for "how much breaks when this one thing fails." The
  metaphor provides it. The Clinejection attack's blast radius was not
  a single machine but an entire publication pipeline -- the compromise
  of one npm package propagated through dependency resolution to
  thousands of downstream systems. The spatial image makes impact
  assessment feel concrete and measurable even when the underlying
  system is abstract.
- **Containment is the response** -- in the physical domain, you
  contain blast radius through distance (separate things far apart),
  barriers (blast walls), and hardening (reinforced structures). The
  metaphor maps these directly onto software architecture:
  microservices (distance), network segmentation (barriers), and
  least-privilege access (hardening). Cloud architecture's obsession
  with "reducing blast radius" through availability zones, service
  isolation, and failure domain boundaries is this transfer in action.
- **Pre-incident estimation** -- military planning estimates blast
  radius before deploying ordnance. The metaphor imports this
  forward-looking analysis into security: before deploying a change,
  assess what would break if it goes wrong. Chaos engineering (Netflix's
  Chaos Monkey, for instance) is formalized blast radius estimation.

## Limits

- **Damage does not attenuate with distance** -- the most consequential
  failure. A physical blast weakens with the square of distance from the
  center. In software, a compromised root credential has equal impact on
  a service one hop away and one a hundred hops away. A leaked API key
  does not become less dangerous the further it travels. The spatial
  attenuation model fundamentally misleads about how software damage
  propagates. The actual pattern is often closer to a flood (binary:
  wet or dry) than an explosion (gradient: near or far).
- **There is no single point of origin** -- explosions have a
  detonation point. Software failures often have distributed causes:
  a race condition that depends on timing, a configuration drift that
  accumulated over weeks, a cascade of individually harmless events that
  combine into catastrophe. The metaphor's single-point-of-failure
  assumption makes it harder to reason about emergent failures.
- **Blast radius is not a fixed property** -- a bomb's blast radius is
  determined by its explosive yield and can be calculated in advance. A
  software failure's blast radius depends on what else is running, what
  state the system is in, what dependencies are loaded, and what
  compensating controls happen to be active. The same bug can have a
  blast radius of one request or one million depending on context. The
  metaphor imports false determinism.
- **The metaphor normalizes destruction** -- military language for damage
  assessment frames destruction as an expected, manageable outcome. This
  can lead to complacency: "the blast radius is acceptable" can become a
  way of not fixing the underlying vulnerability. The explosive metaphor
  makes controlled damage seem like good engineering rather than a sign
  of insufficient prevention.

## Expressions

- "What's the blast radius?" -- the standard question in incident
  response and change management, asking about the scope of potential
  impact
- "Reduce the blast radius" -- the design goal of microservices,
  failure domains, and service isolation: make it so that when something
  breaks, less stuff breaks with it
- "Blast radius of a deployment" -- used in DevOps for the scope of
  systems affected by a code change, particularly in canary and
  blue-green deployments
- "Failure domain" -- the demilitarized synonym for blast radius, used
  in cloud architecture when the explosive metaphor feels too dramatic
- "Limiting the blast radius to a single availability zone" -- standard
  cloud architecture language for geographic and logical isolation

## Origin Story

The term's precise entry into software vocabulary is difficult to date,
but it appears in security and operations discourse by the early 2010s.
It likely migrated from military and intelligence communities, where
blast radius is a literal engineering calculation for ordnance
deployment, through the cultural pipeline of security practitioners
with military or intelligence backgrounds.

The term's adoption accelerated with the rise of microservices
architecture (2012-2015), where "reducing blast radius" became a
primary justification for decomposing monoliths. Amazon Web Services
documentation uses "blast radius" extensively in its Well-Architected
Framework, treating the metaphor as standard technical vocabulary.
Netflix's chaos engineering practice, which deliberately introduces
failures to measure and reduce blast radius, further normalized the
term.

By 2020, "blast radius" was dead -- practitioners used it without any
awareness of its explosive origin. It had become a standard unit of
architectural reasoning: a dimensionless measure of how much breaks
when something breaks.

## References

- Grith.ai, "Clinejection: When Your AI Tool Installs Another" (2026)
  -- blast radius assessment of an npm supply chain attack
- AWS Well-Architected Framework, "Reliability Pillar" -- uses "blast
  radius" as standard vocabulary for failure domain sizing
- Rosenthal, C. *Chaos Engineering* (O'Reilly, 2020) -- formalized
  blast radius estimation through controlled failure injection
