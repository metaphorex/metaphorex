---
author: agent:metaphorex-miner
categories:
- decision-making
- risk-management
contributors: []
created: '2026-03-20'
grounding: established
harness: Claude Code
kind: mental-model
limits:
  - '[model] breaks because the orders assume a single incident commander with clear authority, while organizational crises typically distribute decision rights across competing stakeholders with misaligned incentives'
  - '[model] misleads because the strict sequential ranking (know-before-act) presumes that information gathering can precede commitment, whereas many business and engineering crises require acting under irreducible uncertainty where waiting for full situational awareness is itself the greatest risk'
  - '[model] obscures the orders'' dependence on a shared physical environment where threats are visible (flame, smoke, terrain), importing a false sense that organizational dangers are equally legible if you simply "look up, look down, look around"'
name: Ten Standard Fire Orders
related:
- triage
- lces
slug: ten-standard-fire-orders
source_frame: fire-safety
transfers:
  - '[model] ranks situational awareness above action by placing "keep informed" and "know what your fire is doing" before any operational directive, encoding the principle that premature commitment kills more people than slow response'
  - '[model] encodes a withdrawal doctrine — orders 7-10 mandate escape routes, lookouts, and the authority to refuse engagement — establishing that disciplined retreat is a first-class decision, not a failure mode'
  - '[model] separates the decision to engage from the decision to persist by requiring continuous re-evaluation ("base all actions on current and expected fire behavior"), so that initial commitment does not become an escalation trap'
updated: '2026-03-20'
embodied_patterns:
  - part-whole
  - matching
  - path
relation_types:
  - prevent
  - coordinate
structure: hierarchy
abstraction_level: specific
---

## Transfers

The Ten Standard Fire Orders were codified in 1957 by a task force
investigating the deaths of firefighters who had ignored basic safety
principles. They are not advisory. They are a ranked, numbered checklist
that every wildland firefighter in the United States memorizes, and
violation of any single order is grounds for disengagement. Their
structure — not just their content — encodes a decision framework that
transfers to any domain where people must act under mortal uncertainty.

Key structural parallels:

- **Information precedes action.** The first three orders concern
  knowing: know what your fire is doing at all times, keep informed of
  fire weather conditions, base all actions on current and expected fire
  behavior. This is not a suggestion to gather data; it is a hard
  sequencing constraint. The framework insists that situational awareness
  is a precondition for every subsequent decision, not an optional
  enhancement. In software incident response, the equivalent is: read
  the dashboards before touching the code.

- **Escape routes are planned before engagement.** Orders 4 and 5 require
  identified escape routes and posted lookouts before any suppression
  activity begins. The structural insight is that retreat planning is
  not pessimism — it is a prerequisite for justified risk-taking. A team
  that cannot describe how it will disengage has no business engaging.
  This transfers directly to investment (stop-loss orders), military
  operations (extraction plans), and organizational change management
  (rollback procedures).

- **The authority to refuse.** Order 10 — "Fight fire aggressively,
  having provided for safety first" — places safety as a constraint on
  aggression, not the reverse. Combined with the broader NWCG culture
  that any firefighter can refuse an assignment they believe is unsafe,
  the framework encodes a principle that hierarchical authority does not
  override individual safety judgment. This is the structural equivalent
  of a "stop the line" protocol in manufacturing.

- **Continuous re-evaluation over plan commitment.** The orders do not
  describe a plan; they describe a cycle. "Base all actions on current
  and expected fire behavior" means the decision to engage must be
  re-justified at every moment. Initial commitment provides no inertia.
  This directly counters sunk-cost reasoning and plan-continuation bias.

## Limits

- **The orders assume legible threats.** Fire behavior, while complex,
  is physically observable — you can see the flame front, smell the
  smoke, feel the heat. Organizational and market threats are often
  invisible until they have already materialized. Applying the orders'
  "look before you leap" structure requires first solving the problem
  of making threats visible, which the framework takes for granted.

- **Sequential ranking breaks under time compression.** In a blowup
  scenario where conditions change in seconds, the ranked checklist
  collapses into a single imperative: run. The framework's value is in
  steady-state risk management, not in the extreme tail events where
  decisions must be reflexive. Transferring to business crises, the
  framework works well for strategic planning but poorly for the
  thirty-second window when systems are cascading.

- **The framework presumes a unified command.** The orders work because
  wildland fire operates under the Incident Command System with a single
  IC who has clear authority. Most organizational contexts distribute
  authority across multiple stakeholders with competing priorities. The
  order "ensure instructions are given and understood" presumes a
  communication topology that many organizations do not have.

- **Cultural enforcement is invisible in the text.** The orders on paper
  are a short list. What makes them effective is a culture that treats
  them as inviolable — backed by after-action reviews, fatality
  investigations, and professional norms. Copying the checklist without
  the enforcement culture produces a poster on the wall, not a decision
  framework.

## Expressions

- "Know what your fire is doing" — adapted in incident response to mean
  continuous monitoring of the evolving situation, not just the initial
  state
- "Have escape routes planned and known" — used in project management
  and investing to mean defining exit criteria before committing
  resources
- "Fight fire aggressively, having provided for safety first" — the
  canonical formulation of "bold action within safety constraints,"
  adapted in high-reliability organization literature
- "LCES" (Lookouts, Communications, Escape routes, Safety zones) — the
  mnemonic derivative used in organizational safety culture as a
  checklist for any high-risk operation
- "Risk a lot to save a lot, risk a little to save a little, risk
  nothing to save nothing" — the companion Brunacini doctrine, used in
  emergency management and beyond as a proportionality heuristic

## Origin Story

In 1956, the Inaja Fire in Cleveland National Forest killed eleven
firefighters. The subsequent investigation found that basic safety
principles had been violated — not because they were unknown, but
because they were not codified or enforced. A task force modeled their
response on the U.S. military's General Orders, producing ten numbered
directives that could be memorized and recited. The format was
deliberate: a ranked sequence, not a paragraph of guidance, because the
task force understood that under stress, people revert to what they have
rehearsed. The orders were originally codified by the U.S. Forest Service and
have been mandatory training content for every wildland firefighter in
the United States since 1957. The National Wildfire Coordinating Group
(NWCG), established in 1976, later became their institutional custodian
and continues to publish them in the Incident Response Pocket Guide. Despite periodic proposals
to update or expand them, the original ten remain largely unchanged —
a testament to the robustness of their structure.

## References

- National Wildfire Coordinating Group, *Incident Response Pocket Guide*
  (PMS 461), current edition
- Putnam, T. "The Collapse of Decision Making and Organizational
  Structure on Storm King Mountain," *Wildfire* 4(4), 1995
- Maclean, N. *Young Men and Fire* (1992) — the Mann Gulch disaster
  narrative that preceded the orders' codification
- Weick, K. "The Collapse of Sensemaking in Organizations: The Mann
  Gulch Disaster," *Administrative Science Quarterly* 38(4), 1993
