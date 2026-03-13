---
slug: worse-is-better
name: "Worse Is Better"
kind: paradigm
source_frame: natural-selection
target_frame: software-engineering
categories:
  - software-engineering
  - systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
  - survival-of-the-fittest
---

## What It Brings

Gabriel's "Worse Is Better" paradigm (1989, published 1991) names a
counterintuitive pattern in software adoption: simpler, less correct
software consistently outcompetes more elegant, more complete alternatives.
The paradigm operates through explicitly evolutionary logic -- the "worse"
system is *fitter* in the Darwinian sense, not better by any engineering
metric.

Gabriel contrasts two design philosophies:

- **The MIT approach** (also called "the right thing"): interface
  simplicity and correctness come first. The implementation may be
  complex, but the user-facing abstraction must be clean. Completeness
  and consistency are non-negotiable. Common Lisp is the canonical
  example.
- **The New Jersey approach** (worse is better): implementation
  simplicity comes first. If the implementation would be too complex,
  sacrifice interface elegance or even correctness. "It is slightly
  better to be simple than correct." Unix and C are the canonical
  examples.

The paradigm's explanatory power comes from its evolutionary mechanism:

- **Portability as fitness** -- simple implementations run on limited
  hardware. C ran on PDP-11s where Lisp couldn't. The simpler system
  spreads to more environments.
- **Viral adoption** -- once portable, the simpler software gets adopted
  by more users, who grow accustomed to its quirks and limitations.
  They become a constituency that resists change.
- **Incremental improvement** -- the installed base creates pressure to
  improve the simple system rather than replace it. Unix acquired
  features over decades that Lisp had from birth, but by then Unix had
  won the ecological niche.

## Where It Breaks

- **The natural-selection frame smuggles in teleology** -- Gabriel uses
  evolutionary language ("virus," "spread," "survival"), but biological
  evolution has no goal. The worse-is-better paradigm implies that
  market adoption *should* determine software quality, collapsing the
  distinction between "what wins" and "what is good." Gabriel himself
  was ambivalent: he wrote the essay as a lament, not a celebration.
- **"Worse" is doing too much work** -- the label collapses several
  distinct properties (simplicity, incorrectness, incompleteness,
  inconsistency) into a single evaluative term. A system can be simple
  without being incorrect. The provocation of "worse" obscures the
  actual claim, which is about the primacy of implementation simplicity.
- **Survival-of-the-fittest is not the whole story** -- the paradigm
  inherits the same limitation as its parent metaphor. Cooperation,
  standards bodies, government funding, and network effects all shape
  software adoption. Unix didn't win purely through Darwinian fitness;
  AT&T's licensing decisions, DARPA funding, and the university
  ecosystem were as important as implementation simplicity. The
  natural-selection frame makes these institutional factors invisible.
- **The paradigm has a survivorship bias problem** -- we see the simple
  systems that won (Unix, C, HTTP) and the complex systems that lost
  (Lisp Machines, OSI model). We don't see the simple systems that
  also lost (dozens of forgotten microcomputer OSes) or the complex
  systems that won (the JVM, TCP/IP itself). The paradigm selects its
  own evidence.
- **The "New Jersey" label is parochial** -- Gabriel was writing from
  the MIT/Stanford Lisp world, and the essay reads as an insider's
  grudging admission. The frame makes sense only if you accept that the
  MIT approach is the default and needs explaining away. For most
  working programmers, "keep it simple" was never a paradox.

## Expressions

- "Worse is better" -- the phrase itself, now a standard term of art in
  software engineering discourse
- "The right thing" -- Gabriel's name for the MIT approach, used
  ironically by those who've internalized the paradigm
- "Good enough" -- the commercial expression: ship the minimum viable
  product and iterate
- "Viral adoption" -- software spreading through portability and
  simplicity rather than marketing
- "Worse is better is worse" -- Gabriel's own 1991 reversal, arguing
  against his earlier position (and then reversing again)
- "Embrace, extend, extinguish" -- Microsoft's strategy, which
  operationalizes worse-is-better at the corporate level: adopt the
  simple standard, add proprietary extensions, let the original die
- "Minimum viable product" -- the startup-era descendant: ship something
  simple, let the market tell you what to add

## Origin Story

Richard P. Gabriel drafted the essay in 1989 as part of a longer piece
on Lisp's competitive position. He was a Lisp partisan trying to
understand why Unix and C were winning despite what he saw as clear
technical inferiority. The essay circulated informally before appearing
in his 1991 collection "Lisp: Good News, Bad News, How to Win Big."

Gabriel's relationship to his own argument is famously unstable. He
wrote a companion essay, "Worse Is Better Is Worse," reversing his
position, then later reversed again. He has described the original essay
as a "virus" -- the idea itself demonstrating the pattern it describes,
spreading because it is provocative and simple rather than because it is
correct.

The essay resonated far beyond the Lisp community. It influenced
Raymond's "The Cathedral and the Bazaar" (1997), the Agile movement's
emphasis on shipping early, and the lean startup methodology's "minimum
viable product." The worse-is-better paradigm became one of the few
pieces of software philosophy that practicing engineers actually cite.

## References

- Gabriel, R. P. "The Rise of 'Worse Is Better'" (1989/1991),
  https://www.dreamsongs.com/RiseOfWorseIsBetter.html
- Gabriel, R. P. "Worse Is Better Is Worse" (1991),
  https://www.dreamsongs.com/Files/worse-is-worse.pdf
- Raymond, E. S. "The Cathedral and the Bazaar" (1997) -- directly
  influenced by Gabriel's evolutionary framing
- Ries, E. *The Lean Startup* (2011) -- the worse-is-better paradigm
  repackaged for entrepreneurs as MVP methodology
