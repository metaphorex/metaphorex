---
author: agent:metaphorex-miner
categories:
- arts-and-culture
- software-engineering
contributors: []
created: '2026-03-21'
grounding: folk
embodied_patterns:
  - removal
  - iteration
  - scale
relation_types:
  - transform
  - select
  - cause
structure: pipeline
abstraction_level: generic
harness: Claude Code
kind: mental-model
limits:
- '[model] conflates economy of action with economy of waste -- a carpenter who makes few chips may have done so by planning precisely, or by cutting timidly and leaving excess material, so chip-count alone is ambiguous without knowing whether the target dimensions were achieved'
- '[model] fails in domains where exploration is the point -- a researcher who runs the fewest experiments is not the best researcher, because the goal is discovery rather than execution of a known plan, yet the proverb''s structure rewards convergence over divergence'
name: Best Carpenters Make the Fewest Chips
summary: "Waste volume is a visible proxy for the gap between intention and execution. Low chips means high planning quality."
provenance: carpentry-woodworking
related:
- let-the-tool-do-the-work
- good-art-carries-high-density-of-choice
slug: best-carpenters-fewest-chips
source_frame: carpentry
transfers:
- '[model] precise cuts remove exactly the planned material and nothing more, so waste volume is a visible proxy for the gap between intention and execution -- transferring the prediction that in any craft with irreversible material removal, low waste indicates high planning quality'
- '[model] each chip represents a corrective cut that a better plan would have avoided, encoding the principle that rework is a lagging indicator of upstream planning failure, which transfers to software (fewer bug-fix commits), writing (fewer revision passes), and surgery (fewer corrective procedures)'
- '[model] the proverb counts outputs (chips) rather than inputs (effort or time), providing a metric that is observable by third parties without access to the practitioner''s process, which is why it functions as a folk quality heuristic across trades'
updated: '2026-03-21'
---

## Transfers

The proverb dates to the English woodworking tradition, with variants
attested from the sixteenth century onward. "The best carpenter makes
the fewest chips" (sometimes "the best workman makes the fewest chips")
encodes a folk observation about the relationship between skill and
waste. A carpenter who must plane, trim, and re-cut produces a pile of
shavings and offcuts; a carpenter who measures precisely, cuts once, and
fits cleanly leaves little behind.

Key structural parallels:

- **Waste as inverse skill metric** -- the proverb's core structure.
  In carpentry, every chip is material that was attached to the
  workpiece and should not have been, or material that needed to be
  removed but was removed in multiple passes rather than one. The
  skilled carpenter marks once, saws to the line, and planes to
  final dimension in a few strokes. The unskilled carpenter overcuts,
  then trims, then adjusts, then patches -- each step producing waste.
  This transfers to software engineering, where the number of
  bug-fix commits, emergency patches, and refactoring PRs after a
  feature ships is the analogous chip pile. A well-planned
  implementation arrives close to final form on the first pass.

- **Planning quality over execution speed** -- the proverb does not
  say the best carpenter works fastest; it says they produce the
  least waste. The implication is that skill manifests primarily in
  the quality of upstream thinking -- measuring, visualizing the
  cut, reading the grain -- rather than in the speed of the saw.
  In writing, the analogous claim is that a well-outlined piece
  requires fewer drafts. In surgery, that a well-planned operation
  requires fewer corrective procedures. The metric (waste) is a
  lagging indicator of a leading quality (planning).

- **Observable proxy for invisible skill** -- chips are visible;
  planning is invisible. The proverb gives observers a way to
  evaluate skill without understanding the craft. You do not need
  to know joinery to see that one carpenter's floor is clean and
  another's is covered in shavings. This proxy structure transfers
  to any domain where process quality is hidden but its waste
  products are visible: in software, the commit log is the chip
  pile; in management, the number of emergency meetings is the
  chip pile; in cooking, the volume of trimmings in the compost
  bin tells you about the chef's knife skills.

- **Economy as aesthetic** -- the proverb connects efficiency to
  quality to beauty. A joint that fits without adjustment is not
  only more efficient to produce; it is tighter, stronger, and
  more elegant. Waste reduction and quality improvement are the
  same action, not competing goals. This transfers to code (fewer
  lines is often better code), to prose (tight writing is better
  writing), and to design (minimalism as the aesthetic consequence
  of precise decision-making).

## Limits

- **Economy is not always the goal** -- in exploratory work, waste
  is the point. A sculptor roughing out a form from a block of
  marble produces enormous amounts of waste by design. A researcher
  running experiments is "making chips" deliberately -- most
  hypotheses will fail, and that failure is informative. The
  proverb's structure rewards convergence toward a known target,
  not divergent exploration. Applying it to research, art, or
  early-stage design penalizes the necessary mess of creative
  search.

- **Confuses economy of material with economy of time** -- a
  carpenter who makes few chips may have spent hours measuring and
  re-measuring before cutting. The waste pile is small, but the
  time cost is high. The proverb says nothing about time efficiency;
  it measures only material waste. In software, the developer who
  writes the fewest bug-fix commits may have spent weeks in design
  review. Whether that tradeoff is worthwhile depends on context
  the proverb does not address.

- **Survivorship bias** -- we see the clean workshop; we do not see
  the practice pieces. Every expert carpenter once made enormous
  messes. The proverb describes the endpoint of a skill development
  curve but can be misread as a description of how the best
  carpenters always worked. Applied prescriptively to beginners
  ("make fewer chips"), it produces paralysis: the novice who is
  afraid to cut wastes more material through hesitation and
  half-cuts than one who commits to a bold, slightly-off cut.

- **Chips are not always waste** -- in some woodworking traditions,
  shavings and offcuts are themselves valuable: tinder, packing
  material, animal bedding, kindling. The proverb assumes chips
  have zero value, but byproducts can be resources. In software,
  the "chips" of a project -- abandoned prototypes, exploratory
  branches, failed approaches -- sometimes contain reusable code,
  transferable insights, or documentation of what does not work.

## Expressions

- "The best carpenter makes the fewest chips" -- the English proverb,
  attested from the 1500s in various forms

- "Measure twice, cut once" -- the most widely known variant, which
  shifts focus from the waste metric to the planning behavior that
  reduces it

- "A clean shop is a sign of a good craftsman" -- the workshop variant,
  extending from waste volume to overall workspace discipline

- "First-time quality" -- the manufacturing and lean-production term
  for the same principle: getting the output right on the first pass,
  eliminating rework

- "Do it right the first time" -- the generic management version,
  which preserves the planning-over-correction structure but loses
  the specific material insight about waste as a skill metric

- "Code smell" -- the software engineering adaptation (Fowler, 1999):
  visible symptoms in the codebase that indicate upstream planning
  or design failures, analogous to the chip pile on the workshop floor

## Origin Story

The proverb belongs to the English proverbial tradition and appears in
various forms from the sixteenth century onward. It circulated among
the craft guilds where apprenticeship was the primary mode of skill
transmission. The workshop floor was a daily, visible record of each
worker's skill level, and waste volume was a natural metric because
timber was expensive and offcuts were largely useless for fine joinery.

The proverb's longevity reflects the universality of its structure:
any domain with irreversible material transformation and visible waste
products generates the same folk observation. Butchers, tailors,
stonemasons, and leather workers all have variants of the same
principle. The carpentry version persists because wood is the most
commonly worked material and "chips" is the most vivid image of waste.

## References

- Proverb attested in English proverbial collections from the 16th
  century onward; see Tilley, M.P. *A Dictionary of the Proverbs
  in England in the Sixteenth and Seventeenth Centuries*. University
  of Michigan Press, 1950
- Fowler, M. *Refactoring: Improving the Design of Existing Code*.
  Addison-Wesley, 1999 -- "code smells" as the software equivalent
  of workshop waste
- Womack, J. & Jones, D. *Lean Thinking*. Simon & Schuster, 1996 --
  waste elimination as the organizing principle of manufacturing
  quality
