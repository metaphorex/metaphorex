---
slug: the-adapter-pattern
name: "The Adapter Pattern"
kind: archetype
source_frame: hardware-compatibility
target_frame: object-oriented-design
categories:
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - the-facade-pattern
---

## What It Brings

An electrical adapter lets you plug a device with one shape of prongs
into a socket with a different shape. The metaphor is about physical
fit -- two things that should work together but can't, because their
connection points have the wrong geometry. The GoF Adapter pattern maps
this onto software: a class that translates one interface into another
so that incompatible components can collaborate.

Key structural parallels:

- **Incompatibility is a shape problem** -- the adapter metaphor frames
  interface mismatches as geometric mismatches. Your three-prong plug
  doesn't fit the two-prong socket. Your client expects `draw()` but
  the library offers `render()`. The metaphor says: the functionality
  is there, the connection is wrong. This is a genuinely useful
  reframing. It separates the problem of capability (can the device do
  the work?) from the problem of compatibility (can it connect to
  this system?).
- **The adapter is small and dumb** -- a travel adapter doesn't boost
  voltage or change frequency. It just rearranges pins. A well-designed
  software adapter should be similarly thin: pure translation, no
  business logic. The metaphor sets the right expectation for scope.
  When developers build "adapters" that also transform data, cache
  results, and handle errors, the metaphor quietly protests.
- **Adapters are evidence of a standards failure** -- nobody wants to
  carry a bag of travel adapters. Their existence testifies that the
  world failed to agree on a universal standard. In software, the
  need for an adapter means two systems were designed without
  considering each other. The metaphor carries a trace of frustration:
  this shouldn't be necessary, but it is.

## Where It Breaks

- **Physical adapters are passive; software adapters are active** -- a
  plug adapter sits between socket and device doing nothing but
  providing geometry. A software adapter actively executes code on every
  call: it translates method signatures, converts data types, maps
  exceptions, and may need to maintain state. The passivity that the
  metaphor implies can mislead developers into thinking adapters are
  trivial to implement. They often are not.
- **Adapters don't compose in hardware the way they do in software** --
  stacking physical adapters is a fire hazard. In software, adapters
  can be chained, nested, and composed without physical consequence.
  Developers who internalize the physical metaphor may resist
  multi-layer adaptation that would be perfectly reasonable in code.
- **The metaphor hides the direction problem** -- a physical adapter
  has an obvious direction: plug goes in one end, socket on the other.
  Software adapters face a subtler question about who adapts to whom.
  The class adapter (using inheritance) and the object adapter (using
  composition) are fundamentally different strategies that the plug
  metaphor doesn't distinguish. You don't inherit from a travel adapter.
- **Voltage is invisible in the metaphor** -- a plug adapter handles
  shape but not power. A European device plugged into a US socket via a
  shape adapter may still fry because the voltage is wrong. Software
  adapters face the same risk: they can translate the interface while
  leaving semantic mismatches unaddressed. The method signatures match,
  but the behavioral contracts don't. The metaphor obscures this deeper
  incompatibility because it focuses attention on the visible shape
  of the connection.
- **No wear, no degradation** -- physical adapters develop loose
  connections over time. Software adapters don't degrade with use, but
  they do accumulate cruft as the interfaces they bridge evolve
  independently. The physical model of gradual loosening doesn't map,
  but the result -- a connection that becomes unreliable -- does.

## Expressions

- "Wrapping the legacy API" -- the adapter as a sheath around something
  old, making it fit something new
- "Plug-compatible" -- borrowed from hardware, meaning interfaces that
  can connect without modification, the state an adapter aims to achieve
- "Impedance mismatch" -- from electrical engineering, describing the
  friction between two systems that don't connect cleanly, most commonly
  applied to the object-relational mapping problem
- "Shim" -- a thin piece of material used to fill a gap, often used
  synonymously with adapter in practice but implying even less substance
- "Translation layer" -- the adapter stripped of its physical metaphor,
  reframed as language interpretation

## Origin Story

The Adapter pattern was codified in *Design Patterns: Elements of
Reusable Object-Oriented Software* (1994) by the Gang of Four. The
electrical adapter metaphor was already common in engineering discourse;
the GoF formalized it as a pattern with two variants (class adapter
using multiple inheritance, object adapter using composition).

The metaphor's appeal is its universality. Everyone who has traveled
internationally has encountered the adapter problem. The physical
experience of holding a plug that doesn't fit, then finding a small
device that solves the mismatch, maps directly onto the programming
experience of integrating an incompatible library. Few design pattern
names achieve this level of immediate physical recognition.

The term "impedance mismatch" -- now widespread in software discourse,
especially around ORMs -- extends the electrical metaphor further.
Where the adapter addresses shape, impedance mismatch addresses the
deeper incompatibility that shape adaptation alone cannot fix.

## References

- Gamma, E. et al. *Design Patterns: Elements of Reusable Object-
  Oriented Software* (1994), pp. 139-150
- The electrical adapter metaphor predates the GoF; it appears in
  hardware engineering literature from the 1960s onward
- "Impedance mismatch" as applied to object-relational mapping: see
  Neward, T. "The Vietnam of Computer Science" (2006)
