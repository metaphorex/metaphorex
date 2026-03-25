---
applies_to:
- mathematical-modeling
- software-abstraction
author: agent:metaphorex-miner
categories:
- philosophy
- systems-thinking
contributors: []
created: '2026-03-19'
harness: Claude Code
kind: metaphor
limits:
- '[source] misleads because the 1:1 map fails from physical absurdity (it covers the territory), while real over-fitted models fail from computational cost and noise amplification -- different failure modes that the spatial parable conflates'
- '[source] implies fidelity is a single axis from sketch to perfect replica, but real models trade off along many independent dimensions (spatial resolution, temporal granularity, parameter count) that cannot be collapsed into a single "zoom level"'
- '[source] breaks when applied to simulations that must be high-fidelity to be safe -- nuclear reactor models or aircraft stress tests -- where "just simplify" is not an option and the Borges parable offers no guidance on where irreducible complexity begins'
name: Map-Territory Problem
summary: "A 1:1 map covers the territory it represents. The drive toward perfect model fidelity is itself a pathology."
related:
- the-map-is-not-the-territory
- incompleteness
slug: map-territory-problem
source_frame: cartography
transfers:
- '[source] maps cartographic scale onto model fidelity, establishing that a 1:1 map is physically useless because it replicates the territory rather than abstracting it, and therefore a model that captures everything captures nothing of analytical value'
- '[source] imports the spatial intuition that a map must be smaller than its territory to be portable, framing compression as a feature rather than a defect -- every useful model must discard information, and the question is which information'
- '[source] carries the image of cartographers laboring to extend the map until it obscures the empire it was meant to serve, mapping onto the organizational pattern where documentation, metrics, or process frameworks grow until they consume the capacity they were meant to measure'
updated: '2026-03-19'
embodied_patterns:
  - force
  - path
  - matching
relation_types:
  - cause
  - transform
structure: transformation
abstraction_level: generic
---

## Transfers

Borges's one-paragraph fiction "On Exactitude in Science" (1946) describes an
empire whose cartographers produce a map so detailed it achieves 1:1 scale
with the territory. The map is, of course, perfectly useless -- it covers the
land it was meant to represent, and subsequent generations leave it to rot in
the desert. The structural insight is not merely that all models simplify
(that is "The Map Is Not the Territory," the Korzybski formulation). Borges
adds a specific claim: that the drive toward perfect fidelity is itself a
pathology, and that a model which captures everything captures nothing of
analytical value.

Key structural parallels:

- **Compression is the point, not the cost** -- a road map that included
  every blade of grass would be neither a road map nor a field guide. It
  would be a second landscape. Borges makes the absurdity spatial and
  visceral: the map literally covers the territory. Applied to software,
  this maps onto the recurring pattern where comprehensive documentation,
  exhaustive test suites, or total-coverage metrics grow until they become
  as complex as the system they describe, consuming the same cognitive
  budget they were meant to save.

- **The pursuit of fidelity has diminishing returns that turn negative** --
  moving from a sketch map to a detailed one improves navigation. Moving
  from a detailed map to a 1:1 map makes navigation impossible. The
  relationship between fidelity and utility is not monotonic. In modeling,
  this corresponds to over-fitting: a statistical model trained to perfectly
  reproduce its training data captures noise along with signal and
  generalizes worse than a simpler model. The Borges parable gives this
  abstract statistical insight a memorable physical form.

- **The map becomes an institution that defends itself** -- Borges notes
  that the College of Cartographers had to grow to match the ambition of
  the map. The 1:1 map is not just useless; it is expensive to maintain
  and politically entrenched. This maps onto enterprise process frameworks,
  compliance regimes, and measurement systems that outlive their usefulness
  but resist simplification because institutional roles depend on their
  continued existence.

- **The ruins of the map outlast their purpose** -- Borges describes
  tattered fragments of the map surviving in the desert, sheltering animals.
  The image maps onto legacy systems, deprecated standards, and obsolete
  metrics that persist as infrastructure long after their original purpose
  has been forgotten. The metaphor frames technical debt not as neglect
  but as the natural decay of over-ambitious representation.

## Limits

- **The 1:1 map fails for physical reasons; real over-fitting fails for
  statistical reasons** -- Borges's map is useless because it physically
  covers the territory. A machine-learning model that memorizes its
  training data fails because it amplifies noise and cannot generalize.
  These are structurally different failure modes. The spatial parable
  makes over-fitting vivid but can obscure the actual mechanisms by which
  excess fidelity degrades performance. A reader who internalizes only the
  Borges image may not understand why adding parameters to a regression can
  make predictions worse.

- **Fidelity is not a single axis** -- the parable implies a linear
  progression from crude sketch to perfect replica. Real models trade off
  along multiple independent dimensions: spatial resolution, temporal
  granularity, parameter count, variable selection, causal structure. A
  model can be simultaneously too detailed in one dimension and too crude
  in another. The "zoom level" metaphor inherited from cartography
  collapses these dimensions into one, which is sometimes actively
  misleading for model selection.

- **Some domains require high fidelity** -- the parable counsels
  simplification, but nuclear reactor simulations, aircraft stress models,
  and pharmaceutical interaction databases need extreme fidelity in
  specific dimensions to be safe. The Borges framing can be misused to
  justify premature simplification in domains where the cost of abstraction
  is measured in lives. The parable offers no guidance on where irreducible
  complexity begins.

- **The metaphor does not address the map-making process** -- Borges
  describes the outcome (a useless map) but not the decision process that
  led there. Real modeling involves iterative decisions about what to
  include and exclude, often under uncertainty about which details matter.
  The parable is diagnostic (you have gone too far) but not prescriptive
  (how to decide when you have gone far enough).

## Expressions

- "A 1:1 map" -- shorthand for any model, specification, or documentation
  that has become as complex as the thing it describes
- "Borges's map" -- invoked in data science and machine learning to warn
  against over-fitting and excessive model complexity
- "The map that covered the empire" -- used in organizational contexts
  when process documentation or metrics frameworks have grown unwieldy
- "All models are wrong, but some are useful" (Box) -- the statistical
  restatement of the same insight, often paired with the Borges reference
- "You're building a 1:1 map" -- a code review or architecture critique
  meaning "your abstraction is not abstracting anything"

## Origin Story

Jorge Luis Borges published "Del rigor en la ciencia" ("On Exactitude in
Science") in 1946 as a single-paragraph fiction attributed to a fictitious
17th-century traveler. The story describes the College of Cartographers of
a great empire who produce a map at 1:1 scale that perfectly coincides with
the territory. Later generations, less devoted to cartography, abandon the
map to the elements. Borges credited the idea to Lewis Carroll's *Sylvie
and Bruno Concluded* (1893), in which a character describes a map "on the
scale of a mile to the mile" that was never unfolded because farmers
objected that it would block the sunlight.

The parable entered academic discourse through Jean Baudrillard's
*Simulacra and Simulation* (1981), which inverted it: in the postmodern
condition, the map precedes the territory, and reality is generated by the
model. Umberto Eco also engaged with it in "On the Impossibility of
Drawing a Map of the Empire on a Scale of 1 to 1" (1982). In data science,
the parable circulates as a folk warning against over-fitting, often
alongside George Box's aphorism.

## References

- Borges, Jorge Luis. "Del rigor en la ciencia," *Historia universal de
  la infamia* (1946)
- Carroll, Lewis. *Sylvie and Bruno Concluded* (1893), Chapter 11
- Baudrillard, Jean. *Simulacra and Simulation* (1981)
- Eco, Umberto. "On the Impossibility of Drawing a Map of the Empire on a
  Scale of 1 to 1," in *How to Travel with a Salmon* (1994)
- Box, George E.P. "Robustness in the Strategy of Scientific Model
  Building," in *Robustness in Statistics* (1979)
