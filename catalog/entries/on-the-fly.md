---
slug: on-the-fly
name: On the Fly
kind: metaphor
source_frame: food-and-cooking
applies_to:
  - organizational-behavior
categories:
  - systems-thinking
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - a-la-minute
  - mise-en-place
  - in-the-weeds
  - the-rush
dead: true
created: '2026-03-21'
updated: '2026-03-21'
grounding: folk
harness: Claude Code
provenance: culinary-mise-en-place
transfers:
  - '[source] an on-the-fly order in a kitchen is caused by an upstream failure -- a wrong dish sent, a forgotten modification, a mistimed fire -- so the phrase encodes reactive correction rather than adaptive flexibility'
  - '[source] the on-the-fly order jumps the queue, displacing planned work and forcing the cook to break sequence, which makes visible the hidden cost of unplanned work on throughput in any ordered production system'
  - '[source] the urgency of an on-the-fly order is non-negotiable because a guest is waiting with no food, creating a hard real-time deadline that cannot be batched, deferred, or deprioritized without visible failure'
limits:
  - '[source] breaks because kitchen on-the-fly orders are always small, scoped, and completable in minutes, while organizational "on the fly" work often has unbounded scope and uncertain completion time -- the metaphor imports a false confidence that reactive work is quick work'
  - '[source] misleads by framing reactive work as a kitchen emergency (rare, caused by error), when in many organizations unplanned work is the dominant mode rather than the exception, and calling it "on the fly" preserves the fiction that planned work is the norm'
---

## Transfers

In professional kitchen argot, "on the fly" is a command shouted when a
dish is needed immediately -- usually because the original was sent back,
dropped, or never fired. It is not a request; it is an emergency. An
on-the-fly order overrides the carefully sequenced ticket rail and forces
a cook to interrupt their planned work to produce a single dish under
maximum time pressure. The phrase has migrated so completely into general
English that most speakers have forgotten its culinary origin, making it
a dead metaphor that still encodes culinary logic about reactive work.

Key structural parallels:

- **Reactive correction, not flexible adaptation** -- the crucial insight
  is that "on the fly" in the kitchen is never a positive event. It means
  something went wrong upstream: a server entered the wrong order, the
  expediter mistimed the fire, a dish was plated incorrectly. The phrase
  encodes failure recovery, not agility. When software teams say "we'll
  handle it on the fly," they are importing this structure -- the change
  is unplanned, reactive, and caused by an earlier failure in
  specification, planning, or communication. The culinary origin makes
  visible what the dead metaphor conceals: on-the-fly work is a symptom
  of upstream dysfunction, not a demonstration of adaptability.

- **Queue disruption** -- an on-the-fly order does not add itself politely
  to the end of the ticket rail. It inserts at the front, displacing
  whatever the cook was building. The cook must set down the plate they
  were composing, switch contexts to the emergency dish, and then return
  to find their prior work degraded -- proteins overcooked, sauces
  cooled, garnishes wilted. This maps precisely onto the cost of
  interrupt-driven work in any production system: the on-the-fly task
  is not free, because the work it displaced suffers delay and quality
  degradation.

- **Hard real-time deadline** -- an on-the-fly order has a constraint
  that most kitchen orders lack: a guest is sitting at a table with no
  food while their companions eat. The deadline is not "as soon as
  possible" but "before the social situation becomes unacceptable."
  This creates the kitchen equivalent of a hard real-time system, where
  missing the deadline is a categorical failure, not a graduated
  degradation. The metaphor transfers to incident response, customer
  escalations, and any context where a visible gap must be closed
  before it compounds into reputational damage.

- **The cost is borne by the cook, not the cause** -- whoever made the
  mistake that triggered the on-the-fly order is rarely the person who
  must fix it. The line cook absorbs the disruption, the stress, and
  the quality risk, while the server who entered the wrong table number
  has already moved on. This structural unfairness maps onto
  organizations where downstream producers absorb the cost of upstream
  errors: developers fixing last-minute requirement changes, operations
  teams handling deployment failures caused by untested code.

## Limits

- **Kitchen on-the-fly is small and scoped** -- an on-the-fly order is
  one dish. It takes minutes. The cook knows exactly what to produce
  because it is on the menu. In organizations, "doing it on the fly"
  often means improvising a solution to an unbounded problem --
  redesigning a feature during a demo, rewriting a proposal during a
  meeting, debugging a production issue with no runbook. The metaphor
  imports the kitchen's implicit promise that the emergency is small
  and completable, which is often false in knowledge work.

- **The metaphor normalizes reactive work** -- in a well-run kitchen,
  on-the-fly orders are rare and treated as failures worth investigating.
  In many organizations, the majority of work arrives "on the fly" --
  unplanned, interrupt-driven, and urgent. Using the phrase casually
  ("we'll just do it on the fly") normalizes this condition by framing
  it as a manageable exception rather than a systemic planning failure.
  The culinary origin suggests the opposite: a kitchen that lives in
  on-the-fly mode is a kitchen that is failing.

- **Dead metaphor hides the kitchen's judgment** -- most speakers of
  English use "on the fly" to mean "quickly, without preparation,"
  losing the kitchen's specific meaning of "emergency replacement for
  a failed order." The dead metaphor thus strips out the causal
  structure (something went wrong) and retains only the temporal
  quality (it needs to happen fast), which is the less useful half of
  the original meaning.

## Expressions

- "Fire it on the fly" -- kitchen command to produce a dish immediately,
  outside the normal ticket sequence
- "We'll figure it out on the fly" -- organizational usage, meaning to
  improvise rather than plan, usually obscuring the fact that this is
  failure recovery
- "On-the-fly changes" -- software usage for last-minute modifications,
  preserving the urgency but losing the connotation of upstream failure
- "Another on-the-fly from the front of house" -- kitchen complaint,
  attributing the emergency to a service-side error
- "Hot-patching on the fly" -- systems administration term for applying
  fixes to running production systems, preserving the culinary sense
  of repair under time pressure

## Origin Story

"On the fly" entered culinary vocabulary through the American restaurant
industry, where the phrase became standard shorthand for an emergency
refire. Anthony Bourdain documented the term's emotional charge in
*Kitchen Confidential* (2000), describing on-the-fly orders as among the
most stressful events in a cook's service. The phrase migrated into
general English usage at least by the mid-twentieth century, losing its
specific culinary meaning and retaining only the sense of speed and
improvisation. Dan Charnas's *Work Clean* (2016) treats on-the-fly work
as the antithesis of mise en place -- the unplanned disruption that
preparation is designed to minimize but never fully eliminate.

## References

- Bourdain, A. *Kitchen Confidential: Adventures in the Culinary
  Underbelly* (2000) -- on-the-fly as kitchen stress event
- Charnas, D. *Work Clean: The Life-Changing Power of Mise-en-Place*
  (2016) -- on-the-fly as the failure mode that mise en place resists
