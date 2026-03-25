---
applies_to:
- decision-making
author: agent:metaphorex-miner
categories:
- organizational-behavior
- software-engineering
contributors: []
created: '2026-03-21'
harness: Claude Code
kind: metaphor
name: Technical Decisions Are Territory
summary: "Maps land ownership onto code ownership: teams claim sovereignty over services, enforce borders via code review, and fight turf wars."
related:
- influence-is-physical-force
slug: technical-decisions-are-territory
source_frame: governance
updated: '2026-03-21'
embodied_patterns:
  - container
  - boundary
  - center-periphery
relation_types:
  - contain
  - compete
  - prevent
structure: competition
abstraction_level: generic
transfers:
  - '[source] territory has borders that define where one jurisdiction ends and another begins, mapping decision authority onto bounded spatial regions where teams have sovereignty'
  - '[source] territorial disputes arise when two parties claim the same land, importing the structural dynamic of cross-team conflicts over shared technical concerns'
  - '[source] sovereignty means the right to govern without external interference, framing team ownership as political autonomy where the owning team has veto power over changes within their domain'
limits:
  - '[source] breaks because territorial borders are stable once drawn, whereas technical boundaries shift constantly as systems evolve -- an API that was clearly one team''s territory becomes contested when a new service depends on it'
  - '[source] misleads by importing the zero-sum logic of land ownership, when technical decisions can often be shared or composed rather than exclusively controlled'
---

## Transfers

This is our codebase. That is your codebase. Don't push changes to our
repo without talking to us first. The territorial metaphor for technical
decision-making is so pervasive that engineers rarely notice they are
using it. But it structures organizational behavior in powerful ways:
it determines who gets consulted, who gets to veto, and whose opinion
counts as authoritative.

Key structural parallels:

- **Ownership as sovereignty** -- a team "owns" a service the way a
  nation-state owns its territory. Ownership confers the right to make
  unilateral decisions about what happens within the boundary. Code
  review norms enforce this: changes to someone else's service require
  their approval, just as territorial sovereignty requires consent for
  foreign intervention. The CODEOWNERS file is literally a territorial
  map.
- **Scope as jurisdiction** -- a team's technical authority extends to
  the edge of their service boundary and no further. "That's not our
  problem" is a jurisdictional claim: the issue falls outside the
  team's territory. Cross-cutting concerns (security, performance,
  observability) become analogous to international law -- norms that
  apply across jurisdictions but lack enforcement mechanisms within any
  single territory.
- **Border disputes as cross-team conflicts** -- when two services
  need to share a database, when an API contract needs to change, when
  a platform team wants to impose a standard -- these are border
  disputes. The territorial metaphor provides a ready-made vocabulary:
  "encroachment," "overreach," "stepping on toes." It also imports a
  ready-made conflict resolution framework: negotiation, escalation to
  a higher authority, or simply building a wall (API boundary).
- **Colonization as platform mandates** -- when a platform team imposes
  a standard across all services, teams experience it as a loss of
  sovereignty. "They're taking over our deployment pipeline" carries
  genuine emotional weight because the territorial metaphor makes it
  feel like a seizure of self-governance, not merely a tooling change.

## Limits

- **Technical territory is not scarce** -- physical territory is
  zero-sum: if you control this land, I cannot. Technical decisions are
  not inherently zero-sum. Two teams can independently choose their own
  frameworks, databases, and deployment strategies without diminishing
  each other's options. The territorial metaphor imports scarcity
  where none exists, escalating routine coordination into conflict.
- **Borders are artificial and mutable** -- physical borders are
  expensive to move (wars, treaties). Service boundaries can be
  refactored in a sprint. The metaphor makes architectural decisions
  feel permanent and politically charged, discouraging the routine
  restructuring that healthy codebases require.
- **Sovereignty hides interdependence** -- real systems have shared
  databases, common libraries, and transitive dependencies. The
  territorial metaphor's emphasis on autonomy obscures these
  structural couplings. A team that believes it is sovereign over its
  service may not realize that its choices constrain every downstream
  consumer.
- **The metaphor privileges defense over collaboration** -- territorial
  thinking defaults to protecting boundaries. "Don't touch my code"
  is a defensive posture that the metaphor makes feel natural and
  righteous. But healthy engineering cultures require the opposite:
  willingness to accept outside contributions, to cede control when
  appropriate, and to share ownership of cross-cutting concerns.

## Expressions

- "Code ownership" -- the foundational territorial claim
- "That's not in our scope" -- jurisdictional boundary assertion
- "They're stepping on our toes" -- territorial encroachment complaint
- "CODEOWNERS" -- the literal map of territorial sovereignty in a Git
  repository
- "Don't touch my code" -- the territorial defensive reflex
- "Land grab" -- a team expanding its technical authority into
  unclaimed or contested territory
- "Turf war" -- two teams fighting over decision authority on a shared
  concern
