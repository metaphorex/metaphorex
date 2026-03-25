---
slug: kiss
name: KISS (Keep It Simple, Stupid)
summary: "Design principle: complexity is a bug unless forced by the problem itself; simplicity requires deliberate effort, not default."
kind: mental-model
categories:
  - software-engineering
  - physics-and-engineering
  - decision-making
author: agent:metaphorex-miner
harness: Claude Code
contributors: []
related:
  - kernighans-law
  - accidental-complexity
  - occams-razor
created: '2026-03-22'
updated: '2026-03-22'
grounding: established
transfers:
  - '[model] predicts that systems designed with fewer components, interactions, and special cases will be more reliable, maintainable, and diagnosable than functionally equivalent systems with more complexity, because each additional element is a potential failure point and each interaction between elements multiplies the space of possible failure modes'
  - '[model] identifies that the primary threat to a system''s longevity is not insufficient capability but unnecessary complexity -- systems fail not because they cannot do enough but because they do too much, and each unused capability still contributes to the maintenance burden and failure surface'
  - '[model] predicts that the impulse to add features, options, and contingencies feels like improvement to the designer but degrades the system for the user, because designers experience complexity as expressiveness while users experience it as cognitive load'
limits:
  - '[model] provides no method for determining what counts as "simple" in a given context -- simplicity is relative to the problem, the user, and the operating environment, and the principle offers no decision procedure for distinguishing essential complexity (which cannot be removed without losing required capability) from accidental complexity (which can)'
  - '[model] can be weaponized to dismiss necessary complexity as over-engineering, shutting down legitimate architectural discussions with an appeal to a slogan -- the most damaging misuse occurs when someone invokes KISS to reject a design that handles real edge cases, producing a system that is simple only until it encounters reality'
embodied_patterns:
  - removal
  - part-whole
  - force
relation_types:
  - prevent
  - decompose
  - transform/refinement
structure: hierarchy
abstraction_level: generic
---

## Transfers

The design principle that simplicity should be a key goal and unnecessary
complexity should be avoided. Attributed to Kelly Johnson, lead engineer
at Lockheed's Skunk Works, who reportedly told his team that their jet
aircraft designs must be repairable by an average mechanic in field
conditions with only standard tools.

- **Field-repairability as design constraint** -- Johnson's original
  framing was not abstract aesthetic preference but concrete operational
  requirement. A jet engine is inherently complex, but a *repairable*
  jet engine constrains that complexity: standard fasteners instead of
  custom ones, accessible components instead of buried ones, clear
  diagnostic paths instead of ambiguous symptoms. The principle's force
  comes from specifying *who* must understand the system and *under what
  conditions*. "Simple" without a context is meaningless; "simple enough
  for a field mechanic with a standard toolkit" is a design specification.

- **Complexity as failure surface** -- each component added to a system
  is a potential failure point. Each interaction between components
  multiplies the space of possible failure modes combinatorially. A
  system with 10 components has 45 pairwise interactions; a system with
  20 has 190. KISS encodes the insight that reliability tracks inversely
  with the number of things that can go wrong, and that the number of
  things that can go wrong grows faster than the number of things that
  can go right.

- **The designer's bias** -- KISS implicitly identifies a cognitive
  asymmetry: designers experience complexity as capability and
  expressiveness, while users experience it as friction and confusion.
  The designer who adds a configuration option feels empowered; the user
  who encounters 47 configuration options feels overwhelmed. This maps
  to Brooks's distinction between essential and accidental complexity,
  and to the Unix philosophy of tools that do one thing well.

- **Negative design** -- the principle's deepest structural insight is
  that good design is often about what you *remove* rather than what you
  add. Antoine de Saint-Exupery captured this: "Perfection is achieved,
  not when there is nothing more to add, but when there is nothing left
  to take away." KISS operationalizes this by making the burden of proof
  fall on addition: every new element must justify its existence against
  the baseline cost of existing at all.

## Limits

- **"Simple" is not self-defining** -- the principle's greatest weakness
  is that it provides no method for determining what counts as simple.
  A microservices architecture is simpler than a monolith in deployment
  independence; a monolith is simpler in operational overhead. A
  dynamic type system is simpler in syntax; a static type system is
  simpler in debugging. Simplicity is always relative to a perspective,
  a use case, and a timescale. KISS as a slogan sidesteps exactly the
  hard analysis it should motivate.

- **Essential complexity exists** -- some problems are inherently
  complex. Tax law, protein folding, air traffic control -- these
  cannot be simplified below a certain threshold without losing
  necessary functionality. KISS applied naively to such domains
  produces systems that are simple and wrong. Fred Brooks's distinction
  between essential and accidental complexity (1986) is the necessary
  complement: KISS is a powerful tool for eliminating accidental
  complexity, but it is silent on essential complexity, and mistaking
  one for the other is dangerous.

- **Rhetorical weapon** -- "KISS" is frequently invoked not as a design
  principle but as a conversation-stopper. "Let's just keep it simple"
  can dismiss legitimate architectural discussions, reject necessary
  error handling, or shut down consideration of edge cases. The
  principle's slogan form ("stupid" reinforces the dismissal) makes it
  easy to weaponize against careful engineering. The most damaging
  systems are often those that were "kept simple" past the point where
  simplicity served the problem.

- **Simplicity debt** -- a system that is kept simple early may
  accumulate complexity debt later. A prototype with no error handling
  is simple; a production system with no error handling is negligent.
  KISS does not distinguish between simplicity as a stage (appropriate
  now, to be elaborated later) and simplicity as a permanent design
  value. Teams that internalize "keep it simple" without "...for now"
  sometimes resist necessary evolution, producing systems that are
  simple, brittle, and obsolete.

## Expressions

- "Keep it simple, stupid" -- the full phrase, with the pejorative
  directed at the designer, not the design
- "KISS principle" -- the acronym, used in engineering education and
  software development as a shorthand maxim
- "Simplicity is the ultimate sophistication" -- attributed (probably
  incorrectly) to Leonardo da Vinci, expressing the same principle
  with more elegance
- "Do the simplest thing that could possibly work" -- the Extreme
  Programming variant (Kent Beck), which adds a testability criterion
- "Less is more" -- Mies van der Rohe's architectural version, which
  applies KISS to aesthetics
- "Worse is better" -- Richard Gabriel's provocative reformulation,
  arguing that simpler, less correct systems win because they ship

## Origin Story

The phrase is attributed to Kelly Johnson (1910-1990), who led Lockheed
Martin's Advanced Development Programs, known as the Skunk Works. Johnson
designed some of the most advanced aircraft of the 20th century,
including the U-2, the SR-71 Blackbird, and the F-104 Starfighter. The
story goes that Johnson handed his design team a set of standard tools
and told them that the jet aircraft they were designing must be
repairable by an average mechanic in field combat conditions using only
those tools. If the design was too complex for that constraint, it was
too complex.

The exact phrasing and origin are disputed -- some sources render it as
"Keep It Short and Simple" or attribute it to different contexts. But
the Skunk Works provenance is significant: it grounds the principle not
in abstract philosophy but in operational reality. Simplicity was not
an aesthetic preference but a survival requirement. Aircraft that
couldn't be repaired in the field were aircraft that couldn't fly.

The principle was adopted into software engineering in the 1960s-1970s,
where it aligned with the emerging Unix philosophy and the growing
recognition that software complexity was the primary cause of project
failure. Brooks's "No Silver Bullet" (1986) and the Agile Manifesto
(2001) both echo KISS's core claim that complexity is the enemy.

## References

- Johnson, C.L. "Kelly" -- Lockheed Skunk Works, various oral histories
- Brooks, F. "No Silver Bullet -- Essence and Accident in Software
  Engineering." *IEEE Computer* 20.4 (1987)
- Gabriel, R. "Worse Is Better." *Lisp: Good News, Bad News, How to Win
  Big* (1991)
- Raymond, E.S. *The Art of Unix Programming* (2003) -- codifies the
  simplicity principle in Unix tradition
