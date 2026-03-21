---
applies_to:
- network-security
author: agent:metaphorex-miner
categories:
- security
- software-engineering
contributors: []
created: '2026-03-21'
harness: Claude Code
kind: metaphor
name: Security Violations Are Trespassing
related:
- ai-safety-is-containment
slug: security-violations-are-trespassing
source_frame: physical-security
updated: '2026-03-21'
embodied_patterns:
  - container
  - boundary
  - force
relation_types:
  - prevent
  - contain
  - compete
structure: boundary
abstraction_level: generic
transfers:
  - '[source] a trespasser crosses a physical boundary that separates authorized interior from unauthorized exterior, mapping digital access control onto the embodied experience of walls and doors'
  - '[source] trespassing law distinguishes degrees of violation by the intruder''s intent and the owner''s signage, importing a graduated severity model where unauthorized access is worse with malicious intent and despite clear warnings'
  - '[source] physical trespass leaves forensic traces -- footprints, broken locks, disturbed objects -- framing intrusion detection as crime scene investigation where every access leaves a trail'
limits:
  - '[source] breaks because digital boundaries are not continuous surfaces -- a network perimeter has no physical topology, and an attacker need not traverse intermediate space to reach an interior resource'
  - '[source] misleads by implying that unauthorized access requires physical proximity or effort, when credential theft can grant instant interior access from any location without crossing any boundary'
---

## Transfers

Someone broke in. The perimeter was breached. The intruder gained access
to the inner sanctum. Security discourse is saturated with spatial
metaphors of trespass, and for good reason: the human body has spent
millions of years learning to distinguish inside from outside, safe
territory from hostile territory. This is not just a convenient
analogy -- it is the conceptual infrastructure on which the entire
field of information security is built.

Key structural parallels:

- **The perimeter as property line** -- physical security begins with
  a boundary: a fence, a wall, a locked door. Network security
  inherits this structure wholesale. Firewalls are walls. DMZs are
  demilitarized zones between the network's territory and the wild
  internet. The metaphor is so deeply embedded that the concept of
  "perimeter security" is treated as an architectural category rather
  than a metaphorical choice.
- **Intrusion as illegal entry** -- the word "intrusion" itself is a
  trespassing term. Intrusion detection systems (IDS) are modeled on
  burglar alarms: sensors at the boundary that trigger when something
  crosses uninvited. The attacker is a burglar. The defender is a
  guard. The vocabulary is entirely spatial.
- **Breach as structural failure** -- a "breach" is a hole in a wall.
  A data breach is a hole in the perimeter through which data escapes.
  The metaphor imports the physics of fortification: breaches happen at
  the weakest point, they can be patched or reinforced, and once the
  wall is broken the interior is exposed.
- **Zones of trust** -- physical security uses concentric zones (public
  sidewalk, lobby, office floor, server room, vault) with increasing
  restrictions. Network security mirrors this with network segments,
  VLANs, and zero-trust zones. The spatial metaphor makes "defense in
  depth" -- multiple concentric barriers -- feel like common sense
  rather than one design choice among many.

## Limits

- **Digital boundaries are not continuous** -- a physical wall is a
  continuous surface; you must go through it or over it. A network
  "perimeter" is a set of rules applied to packets at specific
  checkpoints. There is no wall between checkpoints. The metaphor
  creates false confidence in perimeter completeness.
- **Credentials are not keys** -- a physical key is a unique object
  that cannot be in two places at once. A digital credential can be
  copied, shared, stolen, and used simultaneously from multiple
  locations. The trespassing metaphor obscures this fundamental
  difference: digital "keys" do not behave like physical keys.
- **The attacker is already inside** -- trespassing assumes an outside
  attacker trying to get in. The majority of security incidents
  involve insiders or compromised credentials that grant legitimate-
  looking access. The spatial metaphor's emphasis on perimeter defense
  systematically underestimates insider threats.
- **Zero-trust architecture abandons the metaphor** -- the move to
  zero-trust networking is fundamentally a rejection of the
  trespassing frame. There is no "inside" to trespass into. Every
  request is verified regardless of origin. The fact that this
  architectural shift required naming ("zero trust") shows how deeply
  the trespassing metaphor had embedded the assumption that interior
  space is inherently trustworthy.

## Expressions

- "Perimeter defense" -- the most literal spatial term, treating the
  network as a fenced property
- "Intrusion detection" -- monitoring for trespassers crossing the
  boundary
- "Data breach" -- a hole in the wall through which assets escape
- "The attacker gained access" -- spatial entry language applied to
  authentication
- "Defense in depth" -- concentric fortification rings
- "DMZ" -- demilitarized zone, borrowed from military spatial control
- "Firewall" -- a literal wall against the spread of fire, the
  foundational metaphor of network boundary security
