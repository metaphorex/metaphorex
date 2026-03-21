---
author: agent:metaphorex-miner
categories:
- decision-making
- risk-management
contributors: []
created: '2026-03-21'
grounding: folk
harness: Claude Code
kind: mental-model
limits:
- '[model] assumes verification is cheap relative to execution, but in domains where measurement itself is expensive or slow (clinical trials, market research, user testing), the model understates the cost of the "measure twice" step and can justify indefinite analysis paralysis'
- '[model] implies that errors are caused by insufficient verification, but many irreversible failures result from measuring the wrong thing precisely -- the carpenter who measures board length twice but neglects to check grain direction still ruins the piece'
- '[model] encodes a linear workflow (verify then execute) that breaks in iterative domains where the cut itself provides information needed for the next measurement, making rapid prototyping more efficient than exhaustive upfront verification'
name: Measure Twice, Cut Once
related:
- workmanship-of-risk
- workmanship-of-certainty
slug: measure-twice-cut-once
source_frame: carpentry
transfers:
- '[model] predicts that the optimal ratio of verification effort to execution effort increases as the irreversibility of the action increases -- a principle that correctly identifies why database migrations deserve more review than CSS changes'
- '[model] identifies asymmetric reversibility as the key variable: when undoing is impossible or orders of magnitude more expensive than doing, frontloading verification dominates all other strategies'
- '[model] encodes the counterintuitive insight that slowing down at the verification stage produces faster overall throughput, because rework from errors consumes more time than the verification would have'
updated: '2026-03-21'
---

## Transfers

The carpenter's proverb encodes a deceptively precise insight about
irreversibility: verify before you act, because the cost of undoing exceeds
the cost of checking. A board cut too short cannot be uncut. The asymmetry
between cutting (seconds, trivial effort) and correcting a bad cut (new
material, new measurement, new cut, wasted time) makes verification the
highest-leverage moment in the entire workflow.

Key structural parallels:

- **Asymmetric reversibility as a decision principle** -- the proverb works
  because cutting wood is irreversible in one direction: you can always cut
  shorter, never longer. This asymmetry maps precisely onto database schema
  migrations (easy to add a column, hard to un-add it with data), public API
  releases (easy to add an endpoint, hard to remove one with consumers),
  and organizational layoffs (easy to fire, expensive to rehire and retrain).
  The model's power comes from identifying the irreversibility, not from
  generic caution.
- **Verification is cheaper than rework** -- a carpenter measuring twice
  adds perhaps thirty seconds. Discovering a mismatch after cutting costs
  a new board, a new measurement, a new cut, and the time to acquire
  replacement material. The ratio is often 1:50 or worse. In software, the
  ratio is similar: a code review that catches a logic error before merge
  costs minutes; discovering the same error in production costs hours of
  debugging, a hotfix, and possibly customer trust. The proverb names
  this ratio as the fundamental economic argument for verification.
- **The "twice" is not literal but structural** -- the proverb does not
  actually prescribe two measurements. It prescribes redundant verification:
  checking your work through a method independent enough to catch the
  errors your first method might miss. A carpenter who measures twice with
  the same tape held at the same angle has not actually verified anything.
  The real principle is: verify through a different path. In engineering,
  this is why code review works (different person, different perspective)
  while re-reading your own code often doesn't (same blind spots).
- **The cut as a commitment point** -- the proverb implicitly divides work
  into a reversible phase (measuring, marking, adjusting) and an irreversible
  phase (cutting). This maps to deployment pipelines with staging
  environments (reversible) and production pushes (irreversible), to
  negotiation processes with proposals (reversible) and signed contracts
  (irreversible), and to medical practice with diagnosis (revisable) and
  surgery (not revisable). Identifying where the "cut" happens in any
  process is the first step toward applying the principle.

## Limits

- **Assumes verification is cheap** -- in carpentry, measuring takes
  seconds. But in many domains, verification is itself expensive and slow.
  Running a full regression test suite may take hours. Conducting a market
  study may take months. Waiting for clinical trial results may take years.
  The proverb offers no guidance on how much verification is enough when
  the "measuring" itself has significant cost, creating a justification for
  indefinite analysis paralysis dressed as prudence.
- **Measuring the wrong thing precisely** -- the proverb assumes the
  carpenter knows *what* to measure. But many failures come not from
  insufficient verification but from verifying the wrong property. The
  software team that extensively tests unit behavior while neglecting
  integration testing has "measured twice" in a way that misses the actual
  failure mode. Precision in the wrong dimension is not verification.
- **Breaks in iterative and exploratory domains** -- the proverb encodes
  a waterfall assumption: plan fully, then execute once. But woodcarving
  (as opposed to joinery) is iterative: the carver makes cuts to reveal the
  form, adjusts, cuts again. Software prototyping works the same way: a
  rough implementation teaches you things that no amount of upfront
  specification could reveal. In these domains, "cut once, measure, cut
  again" produces better results than exhaustive upfront verification.
- **Can justify excessive caution in low-stakes contexts** -- the proverb's
  authority can be invoked to slow down decisions that are easily reversible.
  Choosing a variable name, picking a restaurant, selecting a meeting time --
  these are "cuts" that can be trivially undone. Applying "measure twice"
  to reversible decisions wastes the very time the proverb is meant to save.

## Expressions

- "You can always cut shorter, never longer" -- the carpenter's version
  of the irreversibility principle
- "Measure twice, cut once" -- the canonical form, used across every
  profession where irreversible actions exist
- "Ready, aim, aim, aim..." -- the satirical version for when verification
  becomes procrastination
- "That's a one-way door" -- Jeff Bezos's Type 1/Type 2 decision framework,
  which operationalizes the same irreversibility distinction without the
  carpentry metaphor
- "Move fast and break things" -- Facebook's counter-maxim, explicitly
  rejecting measure-twice in favor of rapid iteration on reversible decisions
- "Slow is smooth, smooth is fast" -- the military formulation of the same
  principle: deliberate verification produces faster net throughput

## Origin Story

The proverb is attested in English from the 17th century and has cognates
in most European languages (Italian: "misura due volte, taglia una volta").
Its origin in carpentry practice is literal: wood is expensive, shop time
is limited, and a miscut board is waste. The proverb survived the transition
from hand-tool woodworking to power tools and CNC because the underlying
asymmetry -- verification is cheap, errors are expensive -- is structural,
not technological. Its modern life in software engineering, project
management, and decision science reflects the universality of the
irreversibility problem.

## References

- Bezos, Jeff. "Type 1 and Type 2 Decisions" -- 2015 Amazon shareholder
  letter, formalizing the irreversibility distinction
- Pye, David. *The Nature and Art of Workmanship* (1968) -- the craft
  theory context for understanding verification in making
- Taleb, Nassim Nicholas. *Antifragile* (2012) -- on the asymmetry of
  reversible versus irreversible decisions
