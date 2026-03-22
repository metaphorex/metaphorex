---
slug: peter-principle
name: Peter Principle
kind: mental-model
source_frame: organizational-behavior
categories:
  - organizational-behavior
  - decision-making
author: agent:metaphorex-miner
contributors: []
related:
  - dunbars-number
created: '2026-03-21'
updated: '2026-03-21'
grounding: established
transfers:
  - '[law] Promotion in a hierarchy is driven by competence at the current level, but the skills required at each level are discontinuous, so the promotion mechanism systematically moves people away from the roles they perform well'
  - '[law] The end state of any sufficiently old hierarchy is that every position is occupied by someone unable to perform its duties, because competent performers are promoted out and incompetent performers are stuck'
  - '[law] The principle reframes individual "failure at a new role" as a systemic property of hierarchies that reward performance with role changes rather than with deepening of the current role'
limits:
  - '[law] Assumes promotion is the only reward mechanism, ignoring organizations that use dual-track ladders (technical vs. managerial), lateral moves, or compensation increases without title changes, all of which decouple reward from role change'
  - '[law] Treats competence at each level as fixed rather than developable, ignoring that many promoted individuals eventually become competent at the new level through learning, mentoring, or role adaptation -- the principle captures the steady-state without accounting for the transient'
  - '[law] The satire framing (Lawrence Peter presented it as a joke) obscures that the principle describes a real statistical tendency, not a deterministic law -- some promotions are genuinely well-suited, and some organizations do select for next-level potential rather than current-level performance'
embodied_patterns:
  - path
  - scale
  - blockage
relation_types:
  - cause
  - select
  - transform
structure: hierarchy
abstraction_level: generic
---

## Transfers

"In a hierarchy, every employee tends to rise to his level of
incompetence." Laurence J. Peter and Raymond Hull's 1969 formulation
was presented as satire, but the structural mechanism it describes is
real and has been empirically validated.

Key structural parallels:

- **The ladder-as-trap** -- a hierarchy functions like a ladder where
  each rung rewards you for standing well on the current rung by
  moving you to the next one. But the rungs are not uniform: the
  skills required to be an excellent engineer (deep technical focus,
  individual execution) are discontinuous from the skills required
  to be an excellent engineering manager (delegation, conflict
  resolution, strategic prioritization). The promotion mechanism
  treats the hierarchy as a single dimension when it is actually
  a sequence of qualitatively different roles.
- **Competence as a conveyor belt** -- the system is self-reinforcing.
  Competent performers at level N get promoted to level N+1. If they
  are competent at N+1, they get promoted to N+2. The conveyor belt
  stops only when they reach a level where they are no longer
  competent. The result: every position in the hierarchy accumulates
  people who have been promoted one step beyond their ability. The
  work gets done by those who have not yet reached their level of
  incompetence -- the still-rising.
- **The structural alternative the principle implies** -- the Peter
  Principle is most useful as an argument for its own negation. If
  hierarchies that promote based on current-level performance produce
  systematic incompetence, then competent hierarchies must promote
  based on predicted next-level performance (assessment centers,
  trial assignments) or must decouple reward from role change entirely
  (dual-track career ladders, pay bands that overlap across levels).
  The principle diagnoses the mechanism clearly enough to suggest the
  fix.

## Limits

- **Dual-track ladders as a structural refutation** -- organizations
  that offer parallel career tracks (individual contributor and
  management) directly address the mechanism the principle describes.
  A senior engineer can advance in compensation, status, and scope
  without being forced into management. When these tracks are genuine
  (not just ornamental), the Peter Principle's conveyor belt has an
  off-ramp. The principle's predictive power is inversely proportional
  to the quality of an organization's career architecture.
- **Competence is not static** -- the principle treats competence at
  each level as a fixed trait. In practice, many newly promoted
  managers are initially incompetent and become competent through
  experience, training, and mentoring. The principle captures a
  snapshot (the moment of promotion) and treats it as a permanent
  state. Organizations with strong onboarding, coaching, and
  feedback cultures can turn Peter Principle promotions into
  development opportunities rather than terminal placements.
- **The Dilbert Principle as counterpoint** -- Scott Adams proposed
  that organizations intentionally promote incompetent employees
  into management to get them out of productive roles. This is the
  cynical inversion of the Peter Principle: instead of competence
  accidentally producing incompetence, incompetence is deliberately
  rewarded. The two "principles" cannot both be true as general
  laws, which reveals that both are stylized descriptions of
  different organizational failure modes rather than universal
  mechanisms.
- **Cultural specificity** -- the principle assumes a meritocratic
  promotion system where performance at the current level drives
  advancement. In organizations where promotion is based on
  seniority, political connections, or demographic factors, the
  Peter Principle does not apply -- different dysfunctions operate
  instead. The principle is most descriptive of mid-20th-century
  Western corporate hierarchies and least descriptive of clan-based,
  seniority-based, or flat organizations.

## Expressions

- "He's been Peter Principled" -- used when someone is visibly
  struggling in a role they were promoted into based on success
  in a different role
- "Promoted to incompetence" -- the compressed version, used in
  organizational retrospectives
- "The best engineer does not make the best manager" -- the
  software-specific instantiation, now nearly proverbial in
  technology companies
- "Rising to the level of incompetence" -- the canonical
  formulation, used as a diagnostic label rather than an insult

## Origin Story

Laurence J. Peter, a Canadian educator, and Raymond Hull, a
playwright, published *The Peter Principle: Why Things Always Go
Wrong* in 1969. Peter had developed the idea while studying
hierarchies in education; Hull shaped it into readable satire. The
book was rejected by fourteen publishers before William Morrow & Co.
accepted it, after which it spent a year on the bestseller list. The
satirical framing was deliberate -- Peter believed the idea would be
dismissed if presented as serious sociology. Subsequent empirical
research (notably Benson, Li, and Shue's 2019 study of 53,035 sales
employees) confirmed the core mechanism: high-performing sales
workers promoted to management performed worse than peers who were
not promoted, and the effect was strongest for those whose sales
performance was most individual (least transferable to management).

## References

- Peter, Laurence J. and Raymond Hull. *The Peter Principle: Why
  Things Always Go Wrong* (1969) -- the original formulation
- Benson, Alan, Danielle Li, and Kelly Shue. "Promotions and the
  Peter Principle" (Quarterly Journal of Economics, 2019) -- empirical
  validation using sales-to-management promotion data
- Adams, Scott. "The Dilbert Principle" (1995) -- the cynical
  counterpoint
- Kerr, Dave. "Hacker Laws" -- https://github.com/dwmkerr/hacker-laws
