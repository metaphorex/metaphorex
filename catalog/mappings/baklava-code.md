---
author: agent:metaphorex-miner
categories:
- software-engineering
contributors:
- fshot
harness: Claude Code
kind: conceptual-metaphor
name: Baklava Code
related:
- spaghetti-code
slug: baklava-code
source_frame: food-and-cooking
target_frame: software-programs
---

## What It Brings

Baklava is built from dozens of tissue-thin phyllo sheets stacked with
thin smears of filling between them. The pastry's defining quality is
that the layers are individually insubstantial -- each one too thin to
stand on its own, meaningful only in aggregate. This maps onto code that
suffers from excessive abstraction layering: too many interfaces,
wrappers, adapters, and indirection layers, each adding almost nothing,
collectively burying the business logic under a geological stratum of
ceremony.

Key structural parallels:

- **Thin layers as empty abstraction** -- each phyllo sheet is nearly
  transparent. Each code layer is nearly contentless: a service that
  calls a manager that calls a handler that calls a repository that
  calls a mapper. The individual layer does not justify its existence.
  You can see through it, but you still have to traverse it.
- **The filling gets lost** -- in baklava, the nut filling is a thin
  line between sheets. In baklava code, the actual business logic is a
  few lines buried inside dozens of pass-through classes. The thing the
  code exists to *do* becomes the thinnest layer in the stack. A
  developer tracing a request through the system finds more phyllo than
  pistachio.
- **Structural rigidity from lamination** -- stacked phyllo, once baked,
  becomes rigid and brittle. Similarly, deeply layered code becomes
  resistant to change: modifying behavior requires touching every layer
  in the stack. The layers that were supposed to provide flexibility
  through separation of concerns instead provide rigidity through
  coupling. Every layer depends on the layer below it, and every layer
  above depends on it.
- **Part of the food-metaphor family** -- baklava code sits alongside
  spaghetti code (tangled), lasagna code (too many thick layers), and
  ravioli code (well-encapsulated units). Together they form a
  taxonomy of structural pathologies mapped through cuisine. Baklava
  occupies a specific niche: the problem is not tangling or thickness
  but *thinness multiplied*. The anti-pattern is not complexity but
  vacuous decomposition.

## Where It Breaks

- **Baklava layers are identical; code layers are not** -- phyllo sheets
  are interchangeable. Code layers have different responsibilities:
  controllers, services, repositories, DTOs. The metaphor suggests
  homogeneous redundancy, but real baklava code has heterogeneous
  redundancy -- each layer does something slightly different, which is
  what makes it hard to remove any one of them. The problem is not
  identical layers but *nearly-identical-but-not-quite* layers.
- **Baklava is delicious; baklava code is not** -- the pastry is a
  celebrated achievement of culinary engineering. The code is a failure
  of software engineering. The metaphor borrows the structure but inverts
  the valence: what is virtue in the kitchen (painstaking layering) is
  vice in the codebase (pointless indirection). A developer who says
  "this is baklava code" means something quite different from a baker
  who says "this is baklava."
- **The metaphor implies deliberate craft** -- baklava requires patient,
  skilled layering. But baklava code is usually produced not by deliberate
  over-engineering but by cargo-culting "clean architecture" templates.
  Nobody *intends* to create empty layers; they follow a framework that
  generates them. The metaphor credits the programmer with artisanal
  effort when the reality is often mechanical compliance with a project
  template.
- **Layer count is not the real problem** -- the metaphor focuses on
  quantity of layers, but some well-designed systems have many layers
  that each carry genuine responsibility. The actual pathology is layers
  that do nothing but delegate. Counting layers is a proxy metric; the
  metaphor encourages measuring the wrong thing.

## Expressions

- "This is pure baklava" -- developer shorthand for code with too many
  abstraction layers, often encountered in enterprise Java codebases
- "Baklava architecture" -- extending from code to system design, where
  microservices add delegation layers without adding value
- "More phyllo than filling" -- the ratio complaint: the infrastructure
  code vastly outweighs the business logic
- "Unwrapping the baklava" -- refactoring by collapsing unnecessary
  layers, the inverse of the lasagna problem
- "Enterprise baklava" -- a pointed variant associating the anti-pattern
  with enterprise software culture, particularly Spring and Java EE
  projects with mandatory layers

## Origin Story

The term emerged in developer blog posts and Stack Overflow discussions
in the 2010s as part of the broader food-metaphor family for code
structure. Where "spaghetti code" dates to the 1970s structured
programming debates, "baklava code" is a product of the enterprise
Java era, when frameworks like Spring encouraged (and sometimes enforced)
multi-layer architectures with controllers, services, repositories,
DTOs, mappers, and validators -- each a thin sheet of phyllo between the
HTTP request and the database query.

The metaphor gained traction as a counterpoint to "lasagna code" (too
many *thick* layers). Baklava code is the more specific diagnosis: the
layers are not just numerous but *individually empty*. The term is most
commonly used in communities critical of over-engineered enterprise
patterns, often alongside the observation that the same logic could be
expressed in a fraction of the code without the ceremonial layering.

## References

- Atwood, J. "New Programming Jargon," Coding Horror (2012) -- includes
  baklava code among community-sourced programming slang
- Stack Overflow community wiki, "New programming jargon" -- the
  crowd-sourced list where baklava code appeared alongside other food
  metaphors for code structure
