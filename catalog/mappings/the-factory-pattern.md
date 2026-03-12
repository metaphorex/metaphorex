---
slug: the-factory-pattern
name: "The Factory Pattern"
kind: archetype
source_frame: manufacturing
target_frame: object-oriented-design
categories:
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - the-facade-pattern
  - data-flow-is-fluid-flow
---

## What It Brings

Call something a "factory" and you import the entire industrial worldview
into object creation. A factory takes raw materials, follows a
specification, and produces finished goods. The GoF Factory Method and
Abstract Factory patterns map this onto software: a factory method takes
parameters, follows a creation protocol, and returns finished objects.

Key structural parallels:

- **The caller is a customer, not a craftsman** -- you order a product;
  you don't build it yourself. This is the pattern's core insight:
  object creation is a concern that should be separated from object use.
  The manufacturing metaphor makes this separation feel natural, because
  nobody expects a customer to run the assembly line.
- **Factories produce to specification** -- an automotive factory builds
  cars from blueprints, not from scratch each time. A software factory
  returns objects conforming to an interface without the caller knowing
  which concrete class was instantiated. The metaphor captures
  substitutability: any product off the line meets the same spec.
- **Factories hide their internals** -- you see the loading dock, not
  the floor plan. Factory methods encapsulate the decision logic for
  which class to instantiate and how to configure it. The metaphor
  naturalizes information hiding in the specific context of creation.
- **Factories can retool** -- a physical factory can switch production
  runs. An Abstract Factory can be swapped to produce an entire family
  of related objects (e.g., switching from a Windows widget factory to
  a macOS widget factory). The metaphor makes this reconfigurability
  intuitive.
- **Quality control is built in** -- factories can validate, test, and
  reject products before shipping. Factory methods can enforce
  invariants, run validation, and return null or throw exceptions for
  invalid configurations. The metaphor frames this as expected behavior
  rather than defensive paranoia.

## Where It Breaks

- **Factories consume raw materials; software factories don't** -- a
  steel mill needs iron ore and coal. A software factory method needs
  parameters, but those parameters aren't "consumed" -- they're read,
  not destroyed. The manufacturing metaphor imports scarcity and
  resource depletion where none exists. Nobody worries about running
  out of constructor arguments.
- **Physical factories have throughput limits; software factories are
  essentially instant** -- a car factory takes hours per vehicle.
  `ButtonFactory.create()` takes microseconds. The metaphor can mislead
  developers into thinking factory methods are heavyweight operations
  that need pooling or caching, when most are trivially cheap. (Object
  pools exist, but not because creation is "manufacturing.")
- **The labor metaphor is entirely absent** -- real factories employ
  workers, who get tired, make mistakes, and unionize. Software
  factories have no workers. The GoF pattern evacuates the human element
  from the manufacturing metaphor and keeps only the mechanical parts.
  This makes "factory" feel clean and deterministic in ways that actual
  factories never are.
- **Factories produce identical goods; software objects have identity**
  -- two cars off the same line are fungible. Two objects from the same
  factory method share a class but have distinct identity, mutable
  state, and divergent life histories. The metaphor suggests uniformity
  where software actually produces distinct individuals.
- **"Factory" suggests physicality and permanence** -- a factory is a
  building with equipment bolted to the floor. A factory method is a
  function. Developers sometimes over-engineer factory classes --
  giving them state, lifecycle management, and configuration files --
  because the metaphor suggests a factory should be a substantial thing.
  The simplest factory is a three-line function, but that feels too
  flimsy for such an industrial name.
- **The environmental metaphor is missing** -- real factories produce
  waste, pollution, and externalities. Software factories produce
  objects that consume memory and eventually need garbage collection,
  but nobody calls that "industrial waste." The metaphor sanitizes
  creation's costs.

## Expressions

- "The factory produces widgets" -- treating object instantiation as
  manufacturing output
- "Factory method" -- the GoF pattern name itself, equating a function
  with an industrial facility
- "Abstract factory" -- a factory that produces factories; the
  meta-industrial recursion
- "Object creation" -- the baseline metaphor: making objects is
  creating things
- "The factory spits out instances" -- the production line at speed,
  implying mechanical repetition
- "Inject a different factory" -- retooling the production line for
  new output, dependency injection as factory swap
- "Factory pattern abuse" -- over-manufacturing, the sense that not
  everything needs an assembly line

## Origin Story

The Factory Method and Abstract Factory patterns were codified in
*Design Patterns* (1994) by Gamma, Helm, Johnson, and Vlissides. But
the manufacturing metaphor for object creation predates the GoF book.
Smalltalk programmers in the 1970s and 1980s already spoke of "factory
methods" -- class-side methods whose job was to produce properly
initialized instances. The term felt natural because Smalltalk's
object model (everything is an object, objects are created by sending
messages to classes) maps neatly onto the idea of placing an order
with a manufacturer.

The GoF formalized two variants: Factory Method (let subclasses decide
which class to instantiate) and Abstract Factory (produce families of
related objects). Both lean heavily on the manufacturing metaphor to
explain their intent, and both are among the most commonly used --
and most commonly over-applied -- patterns in the catalog. The phrase
"factory pattern" has become so ubiquitous in developer vocabulary
that many programmers use it without thinking about assembly lines
at all, edging it toward dead-metaphor territory.

## References

- Gamma, E. et al. *Design Patterns: Elements of Reusable Object-
  Oriented Software* (1994), Chapter 3: Creational Patterns
- Goldberg, A. & Robson, D. *Smalltalk-80: The Language and Its
  Implementation* (1983) -- early use of factory methods in Smalltalk
- Bloch, Joshua. *Effective Java*, Item 1: "Consider static factory
  methods instead of constructors" (2001/2008/2018) -- the pragmatic
  case for factories over direct construction
