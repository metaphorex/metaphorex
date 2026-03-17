---
applies_to:
- software-engineering
author: agent:metaphorex-miner
categories:
- software-engineering
- philosophy
contributors: []
created: '2026-03-17'
kind: paradigm
name: Worse Is Better
provenance: gabriel-worse-is-better
related:
- survival-of-the-fittest
- software-development-is-a-bazaar
- software-development-is-cathedral-building
slug: worse-is-better
source_frame: natural-selection
updated: '2026-03-17'
transfers:
  - "[paradigm] simpler organisms colonize more environments because they need fewer resources to survive, so implementation simplicity is a fitness advantage that compounds through distribution"
  - "[paradigm] the organism that ships (gets born, arrives in a new habitat) first occupies the niche, and incumbency creates switching costs that later, more correct competitors cannot overcome"
  - "[paradigm] incremental adaptation to environmental pressure produces designs that no architect would have planned, yet which outcompete planned designs in practice"
limits:
  - "[paradigm] breaks because biological evolution has no user who suffers from incorrect behavior -- a virus that crashes its host is just another selection outcome -- while software incorrectness imposes real costs on people who depend on the system"
  - "[paradigm] misleads because it implies a universal law (simpler always wins), but the history of software includes many cases where the more correct system prevailed (TCP/IP over simpler alternatives, SQL over navigational databases, Unicode over code pages)"
---

## Transfers

Richard P. Gabriel coined "worse is better" in his 1991 essay "The Rise
of 'Worse Is Better'" to name a design philosophy he initially observed
with dismay and eventually came to respect. The core claim: software that
prioritizes implementation simplicity over interface correctness will
spread more widely, get adopted more broadly, and ultimately improve
more than software designed for correctness from the start.

Gabriel explicitly framed this as an evolutionary argument. The "New
Jersey approach" (Unix, C) produces software that is simple to
implement, portable, and small enough to run on limited hardware. Like
a hardy weed, it colonizes environments that more refined software
cannot reach. Once established, it improves incrementally under user
pressure. The "MIT approach" (Lisp machines, Multics) produces software
that is correct and complete but too complex to port, too large to run
everywhere, and too slow to ship. Like a hothouse orchid, it thrives
only in controlled conditions.

Key structural parallels:

- **Implementation simplicity as fitness** -- the New Jersey approach
  says "it is slightly better to be simple than correct." In evolutionary
  terms, this is the cockroach strategy: sacrifice elegance for
  survivability. Unix ran on cheap hardware. C compiled on everything.
  The PDP-11 was not the best machine, but C ran on it, and then on
  everything else. Simplicity is what makes a design portable, and
  portability is what makes it dominant.
- **Viral spread through adequacy** -- Gabriel's most striking claim is
  that "worse" software spreads like a virus. It is good enough to be
  adopted. Once adopted, users become conditioned to accept its
  limitations. Once conditioned, they resist switching to "better"
  alternatives. The virus metaphor is deliberate: adoption is
  contagion, not rational choice.
- **Incremental improvement as adaptation** -- once the worse-is-better
  software has colonized its niche, it improves under selection pressure
  from users. Features are added, bugs are fixed, interfaces are
  cleaned up. The result is not the system an architect would have
  designed, but it is the system that survived. And it works well
  enough.
- **Correctness as a luxury** -- the MIT approach insists on getting
  the interface right before shipping. Gabriel argues this is a
  reproductive disadvantage: while the correct system is being
  perfected, the simple system is being adopted. By the time the
  correct system ships, the market has moved on.
- **The 50%-solution that ships** -- "the right thing" delivers 90% of
  the desired functionality with 100% correctness. Worse-is-better
  delivers 50% of the functionality with 50% correctness -- but it
  ships. And 50% of something, delivered, beats 90% of something,
  under development.

## Limits

- **"Worse" is tendentious** -- Gabriel chose the name for rhetorical
  shock, but it obscures a real distinction. The New Jersey approach is
  not worse in every dimension; it makes a deliberate tradeoff (simplicity
  over correctness). Calling it "worse" imports a value judgment that the
  essay itself argues against. The name has become a thought-terminating
  cliche: people invoke "worse is better" to justify shipping broken
  software, which is not what Gabriel meant.
- **Not all simple software wins** -- the paradigm is an observation
  about historical tendencies, not a law. Plenty of simple-but-incorrect
  software died, and plenty of complex-but-correct software thrived.
  TCP/IP was more complex than some alternatives and won anyway. SQL
  was more complex than navigational databases and won anyway. The
  paradigm overgeneralizes from Unix's success story.
- **Correctness costs are real** -- Gabriel's paradigm treats
  incorrectness as a temporary condition that gets fixed through
  incremental improvement. But some incorrectness is catastrophic and
  irreversible. Security vulnerabilities in C's memory model, inherited
  from the worse-is-better era, have cost the industry billions and
  killed people. The paradigm has no vocabulary for incorrectness that
  compounds rather than dissipates.
- **The paradigm can be self-fulfilling** -- if engineers believe that
  simple-and-wrong beats correct-and-complex, they will consistently
  choose simple-and-wrong. This creates a selection environment where
  only simple-and-wrong software gets built, which then confirms the
  paradigm. The paradigm may describe a historical contingency (Unix won)
  rather than a structural necessity (simple always wins).
- **Gabriel himself was ambivalent** -- the essay's tone is ironic and
  self-contradictory. Gabriel later wrote a companion essay ("Worse Is
  Better Is Worse") arguing the opposite position, and then a third
  essay acknowledging his own confusion. The paradigm's originator was
  never sure it was true. Treating it as settled wisdom ignores the
  productive uncertainty at its core.

## Expressions

- "Worse is better" -- the paradigm name itself, now used as shorthand
  for the design philosophy
- "Ship it" -- the imperative form: stop perfecting and release
- "Perfect is the enemy of good" -- the Voltaire aphorism that worse-is-
  better operationalizes for software
- "The New Jersey approach" -- Gabriel's term for the worse-is-better
  philosophy, contrasted with "the MIT approach"
- "Good enough" -- the evaluative standard that worse-is-better
  substitutes for correctness
- "The right thing" -- Gabriel's ironic term for the MIT approach,
  implying that being right is not enough
- "Minimum viable product" -- the startup-era descendant of worse-is-
  better, though stripped of Gabriel's evolutionary framing
- "Done is better than perfect" -- Facebook's version, which drops the
  irony entirely

## Origin Story

Richard P. Gabriel, a Lisp programmer and entrepreneur, wrote "The Rise
of 'Worse Is Better'" in 1991 as a section of a longer essay on Lisp's
decline. The essay contrasted two design philosophies: the MIT approach
(exemplified by Lisp, Multics, and ITS) and the New Jersey approach
(exemplified by C, Unix, and early Internet protocols). Gabriel's test
case was how Unix and the MIT system handled a specific operating-system
problem (the PC loser-ing problem in system calls interrupted by
signals). Unix's solution was simpler but incorrect; the MIT solution
was correct but complex. Unix won.

Gabriel published the essay at a time when the Lisp machine market was
collapsing and Unix was conquering the world. The essay was partly
elegy, partly provocation. It circulated widely in the early Internet
and became one of the most discussed essays in software engineering.
Gabriel's ambivalence -- he admired the MIT approach but could not deny
Unix's success -- gave the essay a productive tension that flat
advocacy would lack.

The worse-is-better paradigm was later absorbed into the broader
discourse around agile development, lean startup methodology, and the
open-source movement, though these later movements typically dropped
Gabriel's evolutionary framing and his discomfort with his own
conclusion.

## References

- Gabriel, R. P. "The Rise of 'Worse Is Better'" (1991), originally in
  *Lisp: Good News, Bad News, How to Win Big*
- Gabriel, R. P. "Worse Is Better Is Worse" and "Is Worse Really Better?"
  -- companion essays exploring the opposite position
- Raymond, E. S. "The Cathedral and the Bazaar" (1997) -- the bazaar
  model as a worse-is-better development process
- Brooks, F. P. "No Silver Bullet" (1986) -- the complexity argument
  from the other side
- Hickey, R. "Simple Made Easy" (2011) -- a modern argument for the MIT
  approach, distinguishing simple from easy
