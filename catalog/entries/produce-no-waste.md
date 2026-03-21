---
author: agent:metaphorex-miner
categories:
- biology-and-ecology
- systems-thinking
contributors: []
created: '2026-03-20'
grounding: established
harness: Claude Code
kind: mental-model
limits:
- '[model] assumes every output has a latent use, but some by-products are genuinely toxic or entropic -- industrial slag, radioactive waste, and heat dissipation have no productive reuse without energy expenditure that exceeds the recovered value'
- '[model] treats waste as a design failure rather than a thermodynamic inevitability; the second law of thermodynamics guarantees that no closed transformation is perfectly efficient, so zero waste is an asymptote, not an achievable state'
- '[model] obscures the cost of integration: routing every output to a consumer requires coordination overhead that can exceed the value of the recovered material, especially in systems where the by-products are variable, low-volume, or unpredictable'
name: Produce No Waste
related:
- you-reap-what-you-sow
- make-hay-while-the-sun-shines
slug: produce-no-waste
source_frame: agriculture
transfers:
- '[model] every output of one process becomes an input to another -- chicken manure feeds compost, compost feeds soil, soil feeds crops -- so the cognitive move is to audit all outputs and ask what downstream process could consume each one'
- '[model] waste signals a design gap rather than an operational inevitability: if something leaves the system unused, the system boundary is drawn too narrowly or a connection is missing'
- '[model] the model reframes efficiency from "minimize inputs" to "maximize the number of useful transformations per unit of material," shifting attention from cost reduction to circulation design'
updated: '2026-03-20'
embodied_patterns:
  - flow
  - link
  - removal
relation_types:
  - transform
  - coordinate
structure: cycle
abstraction_level: generic
---

## Transfers

Holmgren's permaculture principle #6 observes that in mature ecosystems,
there is no waste: every output of one organism is an input to another. Leaf
litter becomes soil. Dead animals become nutrients. Exhaled carbon dioxide
becomes photosynthetic feedstock. The principle asks designers to replicate
this closure in human systems.

Key cognitive moves:

- **Audit all outputs** -- the first move is to notice what currently leaves
  the system unused. In agriculture, this means manure, crop residues, grey
  water, heat. In software, it means log data nobody reads, error messages
  nobody acts on, intermediate computations that are discarded. The model
  says: if it exits unused, you have not finished designing.
- **Connect outputs to inputs** -- the second move is to route each output
  to a process that can use it. Chicken manure goes to compost, compost goes
  to garden beds. In software engineering, this maps to using telemetry data
  to drive autoscaling, feeding error logs into automated alerting, or
  reusing test fixtures across suites. The structural insight is that waste
  is a missing connection, not an intrinsic property of the output.
- **Redesign boundaries** -- if an output has no consumer within the current
  system, the model asks whether the system boundary is drawn too narrowly.
  Perhaps the waste is valuable to an adjacent system. In permaculture, this
  means connecting the chicken run to the orchard (pest control) and the
  garden (fertilizer). In organizations, it means cross-team data sharing
  or exposing internal APIs that other teams can consume.

## Limits

- **Thermodynamic floor** -- the second law of thermodynamics guarantees
  that every energy transformation produces some unusable heat. Zero waste
  is physically impossible in any real system. The model is valuable as a
  design heuristic ("reduce waste by designing connections") but misleading
  as a literal goal ("eliminate all waste"). Confusing the heuristic with
  the goal leads to diminishing-returns investments in recapturing marginal
  outputs.
- **Coordination cost of closure** -- routing every output to a consumer
  requires someone to maintain the connection. In a permaculture garden,
  this is manageable because the gardener controls all processes. In a
  large organization, connecting every team's outputs to every other team's
  inputs creates an integration burden that can exceed the value of the
  recovered material. The model does not account for the cost of the
  connections it prescribes.
- **Toxic and entropic outputs** -- not all outputs are benign. Some
  by-products are genuinely harmful (chemical pollutants, security
  vulnerabilities in reused code, technical debt in shared libraries).
  The model's assumption that every output has a latent use obscures
  cases where the correct response is containment or destruction, not
  reuse.
- **Premature optimization of flows** -- applying the model too early
  in a system's life can lock in connections before the system's actual
  waste profile is understood. In software, this looks like building
  elaborate data pipelines for metrics that turn out to be useless. The
  model works best on mature systems whose waste streams are stable and
  well-characterized.

## Expressions

- "Waste is a resource in the wrong place" -- the principle's core reframe,
  common in circular economy discourse
- "Close the loop" -- the design directive derived from the principle,
  meaning connect outputs back to inputs
- "There is no 'away'" -- environmentalist shorthand for the insight that
  discarded material does not disappear but enters another system
- "One person's trash is another person's treasure" -- folk expression of
  the same structural insight, applied to markets
- "Eat your own dog food" -- software industry expression that applies the
  same logic to product development: consume your own output

## Origin Story

"Produce no waste" is Holmgren's sixth permaculture design principle,
published in *Permaculture: Principles and Pathways Beyond Sustainability*
(2002). Holmgren derived it from observation of mature ecosystems, where
nutrient cycling is nearly complete and outputs from one trophic level
reliably feed the next. The principle also draws on pre-industrial
agricultural practice, where farmers composted manure, saved seed, and
reused materials as a matter of economic necessity rather than ecological
ideology. The modern circular economy movement (McDonough and Braungart's
*Cradle to Cradle*, 2002; Ellen MacArthur Foundation, 2010s) formalizes
the same insight at industrial scale.

## References

- Holmgren, D. *Permaculture: Principles and Pathways Beyond
  Sustainability* (2002) -- principle #6
- McDonough, W. and Braungart, M. *Cradle to Cradle: Remaking the Way
  We Make Things* (2002) -- industrial application of zero-waste design
- Meadows, D. *Thinking in Systems* (2008) -- systems dynamics framework
  for understanding material flows and stocks
