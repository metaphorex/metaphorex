---
slug: behind
name: Behind
kind: pattern
source_frame: food-and-cooking
applies_to:
  - communication
categories:
  - organizational-behavior
  - systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
  - the-line
  - a-la-minute
dead: false
created: '2026-03-19'
updated: '2026-03-19'
grounding: folk
harness: Claude Code
transfers:
  - '[source] the callout announces spatial presence before physical contact, converting potential collision into coordinated movement by making the invisible (who is behind you) audible'
  - '[source] the protocol is unilateral -- the approaching person calls out without waiting for acknowledgment, because in a high-tempo environment the cost of a missed call is a bump, while the cost of waiting for permission is a blocked path'
  - '[source] the vocabulary is compressed to a single word because the channel (shouting over kitchen noise) has low bandwidth, forcing maximum information into minimum signal'
limits:
  - '[source] breaks because kitchen callouts depend on shared physical space where position is unambiguous ("behind" means directly behind your body), while in distributed or asynchronous environments spatial metaphors lose their referent'
  - '[source] misleads by importing the assumption that all coordination failures are awareness failures, when many workplace collisions stem from conflicting priorities rather than insufficient spatial notice'
---

## Transfers

In professional kitchens, cooks shout "behind" when passing behind
another cook, "corner" when rounding a blind corner, "hot" when
carrying something that could burn, and "sharp" when carrying a blade.
These are not courtesies. They are safety protocols that prevent
collisions, burns, and lacerations in a space where people move fast
in close quarters with dangerous implements. The pattern is a
minimum-viable coordination protocol: announce your presence, your
vector, and your hazard level in a single word.

Key structural parallels:

- **Announce before impact** -- the core principle is that the person
  creating the hazard is responsible for the warning, not the person
  at risk. The cook carrying a hot pot says "hot behind" -- the
  stationary cook does not need to constantly check over their
  shoulder. This maps onto any system where the mover bears the
  communication burden: merge request notifications, deployment
  announcements, "I'm pushing to main," "heads up, I'm refactoring
  the auth module." The pattern allocates communication responsibility
  to the agent of change.

- **Compressed vocabulary for high-noise channels** -- kitchen callouts
  are single words because the environment is loud, hands are full, and
  attention is divided. The protocol survives noise by being short,
  loud, and unambiguous. This maps onto communication design for
  high-noise channels: alert fatigue in monitoring systems, commit
  message conventions, status codes. The pattern argues that
  coordination vocabulary should be as small as the channel demands.

- **No acknowledgment required** -- the cook shouts "behind" and keeps
  moving. They do not wait for "okay" or "heard." The protocol is
  fire-and-forget because requiring acknowledgment would create a
  blocking synchronization point in an asynchronous workflow. This maps
  onto notification systems (vs. request/response systems), UDP (vs.
  TCP), and broadcast announcements in Slack channels (vs. direct
  messages that expect replies).

- **The protocol is spatial, not hierarchical** -- it does not matter
  whether the chef or the dishwasher is the one passing behind. The
  callout is triggered by position, not rank. This is unusual in
  kitchen culture, which is otherwise rigidly hierarchical (the brigade
  system). The pattern shows that safety protocols can be orthogonal
  to organizational hierarchy -- a principle that maps onto anonymous
  bug reporting, blameless postmortems, and safety cultures that
  separate hazard identification from chain of command.

- **Failure is physical and immediate** -- if the protocol breaks down,
  someone gets burned, cut, or knocked into a stove. The consequences
  are instant and visceral, which is why the protocol is universally
  adopted in professional kitchens without formal enforcement. This
  maps onto the observation that coordination protocols are most
  reliably followed when the cost of failure is immediate and personal
  rather than deferred and distributed.

## Limits

- **Requires shared physical space** -- "behind" only works because
  everyone understands what "behind" means relative to their body and
  the kitchen layout. In distributed teams, virtual workspaces, or
  asynchronous workflows, there is no "behind." The spatial vocabulary
  has no referent. Attempts to replicate the protocol in chat
  ("heads up, I'm deploying") lose the physical immediacy that makes
  the original effective.

- **Works for spatial awareness, not priority conflicts** -- kitchen
  callouts prevent collisions caused by ignorance of position. They
  do not resolve conflicts caused by two cooks needing the same burner
  at the same time. Importing the pattern into domains where the
  coordination problem is prioritization rather than awareness produces
  a system that announces conflicts but cannot resolve them.

- **The protocol is ambient and interruptive** -- kitchen callouts are
  shouted, which means everyone hears them whether relevant or not.
  This works in a small kitchen with five cooks. It does not scale to
  a hundred-person engineering organization where "behind" announcements
  from every team would create alert fatigue. The pattern assumes a
  small group in close quarters.

- **Fire-and-forget assumes low consequence for missed signals** -- if
  a cook does not hear "behind," they might get bumped. It hurts but
  is rarely catastrophic. In systems where a missed notification can
  cause data loss, financial harm, or safety incidents, fire-and-forget
  is insufficient. The pattern works because the failure mode is a
  bruise, not a disaster.

## Expressions

- "Behind!" -- the canonical kitchen callout, announcing approach from
  the rear
- "Corner!" -- announcing movement around a blind turn
- "Hot behind!" -- combining hazard type with spatial position in two
  words
- "Sharp, coming through" -- knife-carry announcement, the most
  compressed risk communication possible
- "Heads up" -- the general-purpose English equivalent, used outside
  kitchens for the same function
- "I'm pushing to main" -- the software developer's "behind," warning
  collaborators of an incoming change that might affect their work

## Origin Story

Kitchen callouts are oral tradition, passed from cook to cook through
the apprenticeship system. They are not codified in Escoffier or any
formal culinary text; they are learned on the first day of work in any
professional kitchen. The Culinary Institute of America teaches them as
part of kitchen safety, and Anthony Bourdain popularized awareness of
them in *Kitchen Confidential* (2000), describing the kitchen as a
place where spatial awareness is a survival skill.

The pattern has analogs in military communication (call signs and
movement announcements), aviation (position reports in uncontrolled
airspace), and sailing (tacking calls). All share the same structure:
compressed vocabulary, unilateral announcement, spatial or vector
information, and the principle that the mover warns the stationary.
The culinary version is distinctive because it operates without any
formal training or certification -- it is pure oral tradition enforced
by the immediate physical consequences of its absence.

## References

- Bourdain, A. *Kitchen Confidential: Adventures in the Culinary
  Underbelly* (2000) -- popularized kitchen communication protocols
- Charnas, D. *Work Clean: The Life-Changing Power of Mise-en-Place*
  (2016) -- mise-en-place as a system for knowledge work
- The Culinary Institute of America. *The Professional Chef* (9th ed.,
  2011) -- kitchen safety and communication standards
