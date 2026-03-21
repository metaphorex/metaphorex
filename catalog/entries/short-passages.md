---
applies_to:
- software-abstraction
author: agent:metaphorex-miner
harness: "Claude Code"
categories:
- software-engineering
- systems-thinking
contributors: []
created: '2026-03-19'
kind: pattern
limits:
  - '[source] breaks because architectural corridors connect fixed rooms with known destinations, while software indirection connects abstractions whose implementations can change at runtime, making the "length" of a passage a property of execution rather than structure'
  - '[source] misleads by implying that all indirection is waste, when some indirection (interfaces, adapters, middleware) exists to absorb change and would be more costly to remove than to maintain'
  - '[source] assumes the traveler knows where they are going, while software developers often navigate unfamiliar codebases where the problem is not corridor length but the absence of signage -- short passages with no names are worse than long ones with clear labels'
name: Short Passages
related:
- unix-pipe
- chain-of-responsibility
- accidental-complexity
slug: short-passages
source_frame: architecture-and-building
transfers:
  - '[source] maps corridor length onto call-chain depth, framing excessive indirection as an architectural failure that forces traversal through spaces with no purpose of their own'
  - '[source] imports the principle that the path between intention and destination should contain only necessary transitions, making each intermediate step justify its existence'
  - '[source] treats long corridors as symptoms of a floor plan organized for the builder''s convenience rather than the inhabitant''s movement, paralleling code structured for the abstraction''s elegance rather than the reader''s comprehension'
updated: '2026-03-19'
embodied_patterns:
  - path
  - near-far
  - boundary
relation_types:
  - coordinate
  - enable
structure: network
abstraction_level: specific
---

## Transfers

Alexander's pattern #132 observes that long, featureless corridors make
buildings feel institutional and hostile. People avoid them, speed through
them, experience them as dead space between the places that matter. The
pattern prescribes: keep passages short, give them light, make them lead
somewhere specific. If a corridor is too long, the floor plan is wrong.

Applied to software, the mapping targets the call stack, the indirection
chain, and the abstraction layer count -- the corridors of code.

Key structural parallels:

- **Indirection as dead space** -- in a building, a corridor that exists
  only to connect two rooms is wasted square footage. In code, a method
  that exists only to call another method is wasted abstraction. Wrapper
  functions, pass-through classes, delegation chains that add no logic --
  these are the long corridors of software. Alexander's pattern asks: if
  this passage does nothing but connect, can you bring the rooms closer
  together instead?
- **Depth as disorientation** -- a visitor navigating five corridors and
  three stairwells to reach a meeting room will feel lost. A developer
  tracing a function call through five layers of indirection to find the
  actual logic will feel the same way. The pattern's insight is that the
  number of transitions matters independent of the total distance: each
  turn, each layer, each delegation is a cognitive checkpoint where the
  navigator must re-orient. Short passages minimize these checkpoints.
- **Symptoms of builder-centric design** -- Alexander argues that long
  corridors often result from organizing a building around its structural
  grid rather than its inhabitants' movement patterns. The software
  parallel is code organized around its type hierarchy or module boundaries
  rather than its readers' comprehension paths. When a developer must
  traverse three packages and four interfaces to understand a single
  business operation, the architecture is serving the architect, not
  the user.
- **Each passage must justify itself** -- the pattern does not demand zero
  corridors. It demands that each corridor be short and purposeful: a
  transition space with light, a view, a reason to exist. The software
  equivalent: each layer of indirection should perform a meaningful
  transformation, not merely relay. An adapter that translates between
  two protocols earns its existence. A base class that exists only so
  subclasses can exist does not.

## Limits

- **Software indirection has runtime value that corridors lack** -- an
  architectural corridor is geometrically fixed. A software interface can
  dispatch to different implementations at runtime. The "length" of the
  passage is a compile-time property; the "destination" is a runtime
  decision. This means some "long passages" in code exist precisely to
  enable flexibility that the architectural metaphor cannot represent.
  Removing them for brevity may sacrifice the ability to change the
  destination without rebuilding the floor plan.
- **Readability is not the same as traversal efficiency** -- Alexander
  cares about physical traversal: time, effort, disorientation. Software
  "traversal" happens in a developer's head, where the relevant metric
  is comprehensibility, not brevity. Sometimes a longer, more explicit
  chain of delegation is easier to understand than a short but dense
  direct call. The pattern's bias toward short can conflict with the
  principle of making implicit behavior explicit.
- **The pattern assumes known destinations** -- a corridor is bad when
  you know where you want to go and it makes you walk farther. But in
  unfamiliar codebases, the problem is often not knowing where to go at
  all. Short passages with no labels (terse function names, unnamed
  lambdas, anonymous inner classes) can be worse than long, well-signed
  corridors. The pattern does not address the signage problem.
- **Premature shortening creates coupling** -- removing a passage means
  connecting rooms directly. In buildings, this is a renovation. In
  software, this is tight coupling: the caller knows about the callee's
  internals, the UI knows about the database, the controller knows about
  the storage format. Alexander's pattern works because buildings have
  stable floor plans. Software that removes indirection for brevity may
  find itself unable to change anything without cascading modifications.

## Expressions

- "Too many layers of indirection" -- the direct software expression of
  Alexander's long-corridor complaint
- "Wrapper hell" -- the pathological extreme where every class wraps
  another class that wraps another class
- "Just show me the actual code" -- the developer's cry when navigating
  a deep delegation chain, Alexander's corridor complaint in software idiom
- "Call stack is too deep" -- both a runtime error and a design critique,
  literally measuring corridor length
- "Lasagna code" -- pejorative for code with too many layers (cf.
  spaghetti code for tangled flow), the architectural long-corridor
  applied to horizontal stacking
- "The shortest path to the metal" -- systems programming value of
  minimizing abstraction between intention and execution

## Origin Story

Christopher Alexander's pattern #132, "Short Passages," appears in *A
Pattern Language* (1977). Alexander observed that institutional buildings --
hospitals, government offices, schools -- routinely produced corridors that
were too long, too dark, and too uniform, because the floor plan was
designed around structural modules rather than human movement. The pattern
prescribes that no indoor passage should be longer than 50 feet without a
turn, a window, or a change of character.

The pattern's migration into software came through the broader adoption of
Alexander's pattern language by the software engineering community in the
1990s. While it was never codified as a named software pattern the way
"A Place to Wait" or "Light on Two Sides" were, its structural logic
underpins several software principles: the Law of Demeter (don't talk to
strangers through intermediaries), the Single Responsibility Principle
(each layer does one thing), and the general suspicion of deep inheritance
hierarchies. The metaphor of "too many layers" in software architecture
is Alexander's long corridor, whether or not the speaker knows it.

## References

- Alexander, Christopher. *A Pattern Language* (1977), Pattern #132:
  Short Passages
- Lieberherr, K. and Holland, I. "Assuring Good Style for
  Object-Oriented Programs," *IEEE Software* (1989) -- the Law of Demeter
- Martin, R.C. *Clean Code* (2008) -- on minimizing indirection and
  keeping call chains shallow
