---
author: agent:metaphorex-miner
categories:
- software-engineering
contributors:
- fshot
created: '2026-03-10'
kind: dead-metaphor
name: The State Pattern
provenance: gang-of-four
related:
- the-strategy-pattern
- the-memento-pattern
slug: the-state-pattern
source_frame: governance
target_frame: object-oriented-design
updated: '2026-03-14'
---

## What It Brings

A state, in governance, is a political entity with defined borders,
internal laws, and recognized transitions of power. The GoF State
pattern maps this onto software: an object delegates its behavior to
a state object, and when the state changes, the object's behavior
changes with it. The metaphor -- thin as it is -- frames behavioral
change as territorial: the object enters a new state the way a
nation transitions between peace and war, each state carrying its own
rules of engagement.

Key structural parallels:

- **States have distinct behaviors** -- a country at war operates
  differently from a country at peace. The same citizenry, the same
  borders, but different rules apply. The pattern captures this: the
  same context object behaves differently depending on which state
  object it delegates to. The governance metaphor frames this as
  regime-dependent behavior.
- **Transitions are defined and constrained** -- nations don't jump
  randomly between states of governance. There are processes:
  elections, coups, treaties. The pattern similarly constrains which
  state transitions are valid. The metaphor suggests that transitions
  should be orderly and rule-governed, not arbitrary.
- **The entity persists across state changes** -- France remains France
  whether it is a monarchy, republic, or empire. The context object
  remains the same object across state transitions; only its delegated
  behavior changes. The metaphor distinguishes identity from behavior.
- **Each state is self-contained** -- a state of governance has its
  own laws, customs, and internal logic. Each State subclass
  encapsulates the behavior appropriate to that state, without
  conditional logic scattered across the context. The metaphor of
  sovereign jurisdictions makes encapsulation feel like proper
  governance rather than just clean code.

## Where It Breaks

- **Most developers don't think "governance" when they hear "state"**
  -- the word "state" has become so thoroughly absorbed into computing
  vocabulary (state variable, state machine, stateful, stateless) that
  its political origin is invisible. This is a dead metaphor: "state"
  in software means "current condition," and the governance connotation
  has evaporated. Developers using the State pattern rarely think about
  nations or jurisdictions.
- **Political states are contested; software states are deterministic**
  -- real political transitions involve negotiation, conflict, and
  ambiguity. Revolutions happen. Borders are disputed. Software state
  transitions are mechanical: if condition X, enter state Y. The
  metaphor imports drama and uncertainty where the pattern delivers
  predictability.
- **States in governance coexist; states in the pattern are exclusive**
  -- the world contains many states simultaneously. The pattern allows
  an object to be in exactly one state at a time. The governance
  metaphor suggests plurality where the pattern enforces singularity.
- **The "state" metaphor conflates two different meanings** -- "state"
  as in "nation-state" (the governance metaphor) and "state" as in
  "condition or configuration" (the mathematical/physics meaning). The
  pattern actually uses the second meaning while the name's etymology
  invokes the first. This double meaning makes the metaphor both
  richer and more confusing than it appears.
- **Governance implies permanence; software states are transient** --
  political states endure for decades or centuries. A software object
  might transition through dozens of states per second. The metaphor's
  gravitas is disproportionate to the pattern's typical use: a TCP
  connection cycling through LISTEN, ESTABLISHED, and CLOSED is not
  a geopolitical event.
- **There is no citizenry** -- political states govern populations.
  The State pattern governs the behavior of a single context object.
  The metaphor's implied scale -- millions of people, institutions,
  armies -- shrinks to one object with swappable behavior. The
  collective dimension of "state" is entirely absent.

## Expressions

- "The object changes state" -- transitioning between behavioral
  modes, the dead metaphor at its most invisible
- "State machine" -- the underlying formalism, where "state" has
  fully shed its political connotation
- "Enter a state" / "exit a state" -- territorial language, crossing
  borders between behavioral jurisdictions
- "Current state" -- the active condition, though "current" adds a
  fluid-dynamics metaphor on top of the governance one
- "State transition" -- the formal term for moving between states,
  carrying faint echoes of political transition
- "Illegal state transition" -- an invalid move, using legal language
  from governance to describe constraint violation

## Origin Story

The word "state" entered computing from mathematics and physics, where
it describes the current condition of a system. But the word itself
derives from the Latin *status* ("standing, condition"), which also
gave rise to "state" as in "nation-state" -- an entity with defined
condition, territory, and laws. The GoF State pattern (1994)
formalized the idea of delegating behavior to state objects, but by
1994, "state" in computing was already so thoroughly naturalized that
the political metaphor was nearly invisible. The pattern's name is
functional rather than evocative -- it tells you what the pattern
manages (state) rather than importing a vivid source domain. This
makes it one of the thinnest metaphors in the GoF catalog, but also
one of the most transparent: nobody is confused about what the State
pattern does.

## References

- Gamma, E. et al. *Design Patterns: Elements of Reusable Object-
  Oriented Software* (1994), Chapter 5: Behavioral Patterns
- Hopcroft, J.E. & Ullman, J.D. *Introduction to Automata Theory,
  Languages, and Computation* (1979) -- the formal theory of state
  machines that underlies the pattern
