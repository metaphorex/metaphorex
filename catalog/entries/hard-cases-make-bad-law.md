---
slug: hard-cases-make-bad-law
name: "Hard Cases Make Bad Law"
summary: "Rules designed around emotionally compelling edge cases produce worse outcomes for the typical case they were meant to govern."
kind: mental-model
source_frame: governance
categories:
  - law-and-governance
  - systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
  - letter-vs-spirit-of-the-law
provenance: brooms-legal-maxims
created: '2026-03-16'
updated: '2026-03-16'
embodied_patterns:
  - force
  - boundary
  - scale
relation_types:
  - cause
  - transform
structure:
  - boundary
abstraction_level: generic
harness: Claude Code
transfers:
  - "[law] predicts that rules designed around emotionally compelling edge cases will systematically produce worse outcomes for the typical case than rules designed around the baseline"
  - "[law] identifies the mechanism: extreme cases generate pressure to act, and that pressure overrides the careful balancing of competing interests that good general rules require"
limits:
  - "[law] breaks when the 'hard case' reveals a genuine structural flaw in existing rules rather than an emotional outlier -- some edge cases are not exceptions but evidence that the baseline rule was wrong all along"
  - "[law] misleads by implying that good law can be made without attending to hard cases at all, when in practice stress-testing rules against extreme scenarios is a standard and valuable part of policy design"
---

## Transfers

The maxim "hard cases make bad law" expresses a structural insight
about the relationship between extreme examples and general rules.
When a case is emotionally compelling -- a sympathetic victim, an
outrageous injustice, a dramatic set of facts -- it creates pressure
to decide in a way that feels right for that case but produces a
precedent that distorts the law for all future cases.

Key structural parallels:

- **Exception-driven policy is systematically worse** -- a rule
  designed for the typical case will produce occasionally harsh
  results at the margins. A rule designed for the extreme case will
  produce routinely inefficient results at the center. The model
  predicts that the political dynamics of hard cases (media
  attention, public outrage, sympathetic narratives) will push
  rule-makers toward the latter, systematically degrading rule
  quality. This maps onto software architecture (designing APIs
  around edge cases produces bloated interfaces for common use),
  organizational policy (creating processes to prevent rare abuses
  that burden everyone), and security design (imposing friction on
  all users to prevent the actions of the adversarial few).
- **Emotional salience distorts probability assessment** -- hard
  cases are memorable because they are extreme. This creates an
  availability bias: after encountering a hard case, decision-makers
  overestimate the frequency of similar situations and design rules
  accordingly. The model explains why a single dramatic failure
  can produce disproportionate regulatory responses: one airplane
  crash rewrites safety rules, one fraud case restructures an
  entire industry's compliance requirements, one security breach
  triggers organization-wide lockdowns.
- **The precedent outlives the case** -- in common law, a judicial
  decision becomes a rule for future cases. A decision driven by
  the emotional particulars of a hard case creates a precedent
  that applies to all subsequent cases, including the routine ones
  where the emotional pressure does not exist. The model explains
  why legal systems develop doctrines to cabin the influence of
  hard cases: narrow holdings, distinguishing on the facts,
  explicit statements that a ruling should not be read broadly.
- **The inverse is also true** -- "easy cases make invisible law."
  When cases are routine and uncontroversial, the rules they
  establish receive no scrutiny. The model highlights how
  attention asymmetry shapes rule quality: hard cases get too
  much attention and distort rules; easy cases get too little
  attention and may perpetuate unjust baselines.

## Limits

- **Some hard cases reveal real problems** -- the maxim assumes
  that the hard case is an outlier, not a symptom. But sometimes
  an emotionally compelling case exposes a genuine structural
  injustice that baseline-focused rule-making failed to address.
  The civil rights cases of the 1950s and 1960s were "hard cases"
  that made excellent law. Dismissing them as emotional outliers
  would have perpetuated segregation. The model provides no way
  to distinguish between a hard case that is a misleading outlier
  and one that is a window into systemic failure.
- **"Easy cases" can make bad law too** -- the maxim implies that
  rules made from routine cases are sound. But routine cases may
  reflect unexamined assumptions, entrenched biases, or systemic
  power imbalances. Law made from easy cases can be quietly unjust
  in ways that only become visible when a hard case forces scrutiny.
  The model's implicit baseline bias is itself a form of status quo
  bias.
- **The model can be weaponized as a silencing tactic** -- invoking
  "hard cases make bad law" is an effective way to shut down
  discussion of marginal cases, vulnerable populations, and
  systemic failures. If every emotionally compelling example can
  be dismissed as a "hard case" that should not influence policy,
  the maxim becomes a tool for protecting existing rules against
  legitimate challenge. The model does not distinguish between
  appropriate caution and inappropriate complacency.
- **It assumes rules can be cleanly separated from cases** -- the
  maxim presupposes that there is a "general rule" that exists
  independently of the cases it governs. But in common law, rules
  emerge from cases. There is no rule without cases, and the
  question of which cases are "hard" (and therefore
  distortion-prone) depends on what you think the rule should be.
  The model's clean distinction between rules and their
  exceptional applications is an idealization.

## Expressions

- "Hard cases make bad law" -- the full maxim, widely used in legal
  education, policy debates, and general discourse about rule-making
- "Legislating by anecdote" -- the policy equivalent: designing rules
  based on vivid stories rather than statistical baselines
- "Edge case driven development" -- software engineering expression
  for the anti-pattern of designing systems around unusual inputs
  rather than common ones
- "One bad apple spoils the barrel" -- related folk expression about
  how one extreme instance can contaminate the whole, though this
  encodes a different structural claim (contagion rather than
  distortion)
- "The plural of anecdote is not data" -- related heuristic about
  the danger of generalizing from vivid particular cases

## Origin Story

The maxim is attributed to Judge Robert Rolfe (later Baron Rolfe)
in *Winterbottom v. Wright* (1842), an English tort case about
whether a mail coach driver could sue the coach manufacturer for
injuries caused by a defective coach. Rolfe argued for a narrow
rule limiting liability to contractual parties, warning that
extending it to all affected parties would produce bad precedent
driven by sympathy for the injured plaintiff.

Ironically, the "bad law" Rolfe feared eventually came to pass:
product liability doctrines expanded throughout the 20th century to
allow exactly the kind of claims he sought to prevent, and most
legal scholars now regard the expansion as an improvement. The
history of the maxim itself illustrates one of its own limits:
sometimes the hard case is right and the existing rule is wrong.

The maxim was collected and popularized through Broom's *A Selection
of Legal Maxims* (1845) and has become one of the most frequently
cited principles in Anglo-American legal culture.

## References

- *Winterbottom v. Wright* (1842) 10 M&W 109 -- origin of the maxim
- Broom, H. *A Selection of Legal Maxims* (1845)
- Dworkin, R. "Hard Cases," *Harvard Law Review* 88 (1975) -- the
  most influential philosophical response, arguing that hard cases
  have right answers
- Sunstein, C. *Laws of Fear* (2005) -- on how emotionally salient
  cases distort risk regulation
