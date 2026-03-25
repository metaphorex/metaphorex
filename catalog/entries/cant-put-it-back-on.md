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
name: You Can Always Take More Off, But You Can't Put It Back On
summary: "Removing too little is fixable; removing too much is fatal. Bias toward the recoverable error at every step."
provenance: carpentry-woodworking
related:
- shim
- jig
- scaffolding
slug: cant-put-it-back-on
source_frame: carpentry
updated: '2026-03-21'
transfers:
  - '[law] predicts that in any domain with irreversible subtraction, starting conservative and iterating toward the target produces better outcomes than starting aggressive and trying to correct overshoots'
  - '[law] predicts that the cost of undershoot (too much material left) is linear and recoverable, while the cost of overshoot (too much material removed) is discontinuous and often total -- the error function is asymmetric'
  - '[law] predicts that experienced practitioners will systematically bias toward leaving excess material at every stage, because they have internalized the asymmetric cost structure through repeated losses'
limits:
  - '[law] fails in domains where the cost of iteration exceeds the cost of aggressive first cuts -- in time-critical situations, conservative iteration is a luxury that the schedule cannot afford'
  - '[law] misleads when applied to additive processes (writing, painting, negotiation) where you can in fact "put it back on," making the asymmetry the proverb assumes simply absent'
---

## Transfers

The woodworking proverb "you can always take more off, but you can't put
it back on" encodes a fundamental insight about asymmetric reversibility.
When cutting wood, removing material is easy and irreversible. Adding
material back is either impossible or requires a patch that compromises
the piece. This asymmetry creates a rational strategy: always start with
more material than you need, and approach the final dimension through
successive, conservative removals.

Key structural parallels:

- **Asymmetric error costs** -- in woodworking, cutting too little leaves
  you with a workable piece that needs another pass. Cutting too much
  leaves you with scrap. The error in one direction is correctable; the
  error in the other direction is terminal. This asymmetry appears across
  many domains. In negotiation, opening with a higher ask (more material)
  lets you make concessions; opening too low leaves nothing to give. In
  editing text, writing too much gives you material to cut; writing too
  little forces you to generate new content under pressure. In pricing,
  launching high and discounting is easier than launching low and raising
  prices. The proverb identifies the structural asymmetry and prescribes
  the rational response: bias toward the recoverable error.
- **Iteration as the mechanism** -- the proverb does not say "get it right
  the first time." It says "take more off" -- iterate. The strategy is
  explicitly incremental: approach the target through multiple passes,
  each removing a small amount. In woodworking, the sequence is rough
  cut (bandsaw), dimension (jointer/planer), fine adjustment (hand plane),
  finish (sandpaper). Each tool removes less material with more precision.
  In software development, the MVP strategy follows the same logic: ship
  with more features than necessary (or more conservative behavior), then
  remove or simplify based on user feedback. The iteration is the skill,
  not the initial cut.
- **Conservative defaults as encoded wisdom** -- experienced woodworkers
  cut every piece slightly oversize and plane to final dimension. This is
  not caution; it is a production strategy that eliminates the most
  expensive failure mode (wasted material and time). In system design,
  conservative defaults (timeouts set high, permissions set restrictive,
  rate limits set low) follow the same logic: it is cheaper to relax a
  constraint than to tighten one after damage has occurred. The proverb
  is a policy prescription disguised as an observation.
- **The scrap pile as teacher** -- the proverb is always learned through
  loss. Every woodworker has a pile of boards ruined by cuts that went
  a fraction too far. The asymmetric cost structure is not theoretical;
  it is embodied in wasted material and wasted time. In business, the
  equivalent is the post-mortem of an irreversible decision: the product
  launch that went too early, the layoff that went too deep, the
  bridge that was burned. The proverb encodes the scar tissue.

## Limits

- **It assumes subtraction is the dominant operation** -- the proverb is
  perfectly calibrated for woodworking, where removing material is the
  primary operation. But many creative and professional domains are
  primarily additive. In writing, you can always add paragraphs back. In
  painting (at least in oils), you can paint over. In negotiation, you
  can make additional offers. In these domains, the asymmetry the proverb
  assumes does not hold, and its advice (start conservative) may be
  counterproductive -- it can produce timid first drafts, bland
  compositions, and weak opening positions.
- **Iteration costs may exceed the cost of the error** -- the proverb
  assumes that successive passes are cheap. In woodworking, this is
  roughly true: a few more strokes with a hand plane cost minutes. But
  in domains where each iteration is expensive (a rocket launch test, a
  clinical trial, a construction pour), the cost of conservative
  iteration can exceed the cost of an aggressive but well-calculated
  first attempt. Engineers with tight budgets sometimes must "cut to
  final dimension" on the first pass because there is no second pass.
- **It can rationalize perfectionism** -- "I'll just take a little more
  off" has no natural stopping point. In woodworking, you can sand and
  plane a piece past its useful dimension, chasing a fit that was already
  good enough. The proverb's iterative logic, taken too literally,
  becomes a license for infinite refinement. In software, this manifests
  as endless polishing of code that was already shippable, or endless
  simplification of a product that users found adequate.
- **Not all irreversibility is bad** -- the proverb frames irreversible
  action as inherently risky. But some domains reward decisive,
  irreversible commitment. In warfare, burning bridges prevents retreat
  and concentrates force. In business, public commitments create
  accountability that hedged positions do not. The proverb's bias toward
  reversibility is a specific strategic choice, not a universal truth.

## Expressions

- "You can always take more off, but you can't put it back on" -- the
  full proverb, universally known in woodworking shops
- "Measure twice, cut once" -- the companion proverb, addressing the
  planning stage of the same asymmetric-cost problem
- "Leave it fat" -- woodworking instruction to cut pieces oversize,
  planning to trim to final dimension
- "Sneak up on the line" -- making successive light cuts approaching
  the target mark, never crossing it in a single pass
- "Ship the MVP" -- software development expression encoding the same
  logic: launch with conservative scope, then iterate
- "You can't unring a bell" -- legal and diplomatic equivalent encoding
  the irreversibility of disclosure
- "Start conservative, dial it in" -- engineering expression for setting
  initial parameters with safety margin and adjusting through testing

## Origin Story

The proverb is a piece of workshop oral tradition with no traceable
first author. It appears in woodworking instruction manuals throughout
the 20th century and is one of the first principles taught to
apprentices. Its persistence owes to its perfect alignment with the
physics of the material: wood is a subtractive medium, and the Second
Law of Thermodynamics ensures that reassembly is harder than
disassembly. David Pye's *The Nature and Art of Workmanship* (1968)
formalized the underlying insight as the distinction between
"workmanship of risk" (where the result is determined by the worker's
judgment during execution) and "workmanship of certainty" (where it is
determined by the jig). The proverb is advice for the workmanship of
risk: when outcome depends on real-time judgment, bias conservative.

## References

- Pye, David. *The Nature and Art of Workmanship* (1968) -- workmanship
  of risk vs. certainty as the theoretical frame
- Taleb, Nassim Nicholas. *Antifragile* (2012) -- asymmetric downside
  as a general decision principle (the barbell strategy)
- Schwartz, Barry. *The Paradox of Choice* (2004) -- reversibility
  preferences in decision-making
