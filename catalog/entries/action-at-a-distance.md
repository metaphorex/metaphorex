---
applies_to:
- software-programs
author: agent:metaphorex-miner
categories:
- software-engineering
- physics-and-engineering
contributors:
- fshot
created: '2026-03-17'
dead: false
embodied_patterns:
  - link
  - near-far
  - force
relation_types:
  - cause
  - enable
  - translate
structure: network
abstraction_level: generic
harness: Claude Code
kind: metaphor
name: Action at a Distance
summary: "You change something here and something over there breaks with no visible connection. The coupling exists but is not declared in the interface."
related:
- spaghetti-code
slug: action-at-a-distance
source_frame: physics
transfers:
  - "[source] a force acts on a body without any observable intermediary traversing the space between them"
  - "[source] the effect is instantaneous and non-local, violating the expectation that causes propagate through adjacent regions"
  - "[source] the mechanism of influence is hidden, making the causal chain untraceable by inspecting the immediate neighborhood of the affected body"
limits:
  - "[source] breaks because physical action at a distance is symmetric (both bodies experience force), whereas the mapped coupling is typically one-directional: the modifier does not feel the effect"
  - "[source] misleads because Einstein's objection was that it violated locality (no faster-than-light signaling), but in software the problem is not speed of propagation but invisibility of the coupling path"
updated: '2026-03-17'
---

## Transfers

Einstein called quantum entanglement "spooky action at a distance" --
the idea that measuring one particle instantly affects another, no matter
how far apart, with no visible mediating signal. In software, the phrase
names the same unsettling experience: you change something here, and
something over there breaks, with no apparent connection between the two
locations.

Key structural parallels:

- **Non-local causation** -- in physics, action at a distance means a force
  operates without a local intermediary. In code, it means modifying a
  variable, configuration value, or database row in one module produces
  effects in a distant module with no visible call chain connecting them.
  The developer at the point of breakage cannot trace the cause by reading
  nearby code.
- **Hidden coupling as the mechanism** -- quantum action at a distance
  troubled physicists because it implied a hidden variable or a violation
  of locality. Software action at a distance is similarly produced by
  hidden coupling: global state, shared mutable singletons, database
  triggers, event buses with implicit subscribers, or environment variables
  read by distant components. The coupling exists but is not declared in
  the interface.
- **Spookiness as a diagnostic signal** -- Einstein's word "spooky"
  captures the affective quality precisely. When a developer says "there's
  action at a distance happening here," they mean the system is behaving
  as if by magic -- effects appear without traceable causes. The metaphor
  converts a debugging intuition into a communicable concept.
- **Locality as a design principle** -- the physics metaphor implicitly
  advocates for locality: effects should propagate through adjacent,
  visible mechanisms. In software, this translates to explicit dependency
  injection, immutable values, and interfaces that declare their effects.
  The metaphor does rhetorical work by framing non-local coupling as
  physically unnatural.

## Limits

- **Physical action at a distance is symmetric; software coupling usually
  is not** -- in Newtonian gravity, both bodies experience force (Newton's
  third law). In software, the "action" is typically one-directional: the
  code that mutates global state is unaffected by the distant breakage it
  causes. The metaphor imports a symmetry that does not exist, potentially
  obscuring where the responsibility lies.
- **The metaphor implies the coupling is mysterious; often it is just
  undocumented** -- quantum entanglement is genuinely puzzling at a
  fundamental level. Software action at a distance is almost always
  explicable once you find the shared state or implicit dependency. The
  "spookiness" is a property of the developer's knowledge, not of the
  system's nature. Calling it action at a distance can romanticize what
  is really a documentation failure.
- **Not all non-local effects are pathological** -- event-driven
  architectures, reactive programming, and publish-subscribe systems are
  deliberately designed for non-local effects. The metaphor frames all
  action at a distance as a defect, but some systems are intentionally
  built so that changes in one place propagate to many distant consumers.
  The metaphor has no vocabulary for intentional non-locality.
- **The physics metaphor carries authority it hasn't earned** -- invoking
  Einstein and quantum mechanics lends the complaint an aura of scientific
  rigor. But the structural parallel is shallow: the physics concept
  concerns fundamental limits on information propagation, while the
  software concept concerns code organization. Dressing up a coupling
  complaint in physics language can make it sound more profound than it is.

## Expressions

- "There's action at a distance in this module" -- the diagnostic, meaning
  something external is affecting local behavior through hidden coupling
- "Spooky action at a distance" -- the full Einstein allusion, used when
  the coupling is particularly surprising or hard to trace
- "This global state is causing action at a distance everywhere" -- the
  explanation, identifying mutable shared state as the hidden mediator
- "We need to eliminate the action at a distance before we can refactor" --
  the prescription, treating non-local coupling as a prerequisite to fix
- "That's not a bug, that's action at a distance from the config change" --
  post-mortem diagnosis after an incident caused by distant coupling

## Origin Story

The physics concept dates to Newton's *Principia* (1687), where gravity
acts instantaneously across space with no visible medium. Newton himself
was uncomfortable with this ("I frame no hypotheses"). Einstein's 1935
EPR paper famously objected to quantum entanglement as "spooky action at
a distance" (*spukhafte Fernwirkung*), arguing it implied an incomplete
theory.

The phrase entered software engineering discourse informally, likely through
developers with physics backgrounds who recognized the structural parallel.
It appears in discussions of global state, side effects, and coupling at
least as early as the 1990s. Martin Fowler and others have used it in
refactoring contexts to name the code smell of hidden dependencies. The
term has remained relatively niche compared to "spaghetti code" or
"technical debt," but it fills a gap: it names a specific failure mode
(hidden non-local coupling) rather than a general condition (messiness).

## References

- Einstein, A., Podolsky, B., and Rosen, N. "Can Quantum-Mechanical
  Description of Physical Reality Be Considered Complete?" *Physical
  Review* 47 (1935) -- the EPR paper introducing "spooky action at a
  distance"
- Fowler, M. *Refactoring: Improving the Design of Existing Code* (1999)
  -- discusses hidden coupling and non-local effects as code smells
- Hunt, A. and Thomas, D. *The Pragmatic Programmer* (1999) -- advocates
  for minimizing "coupling between distant parts of the system"
