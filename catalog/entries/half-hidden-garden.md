---
slug: half-hidden-garden
name: Half-Hidden Garden
kind: pattern
source_frame: architecture-and-building
applies_to:
  - software-abstraction
categories:
  - software-engineering
  - systems-thinking
author: agent:metaphorex-miner
contributors:
  - fshot
related:
  - the-facade-pattern
  - filtered-light
  - positive-outdoor-space
dead: false
created: '2026-03-21'
updated: '2026-03-21'
grounding: folk
harness: Claude Code
provenance: alexander-pattern-language
transfers:
  - '[source] imports the principle that a space which reveals part of itself while concealing the rest creates an invitation to enter, framing API discoverability as a design of progressive revelation rather than exhaustive documentation'
  - '[source] carries the structural insight that full exposure kills intimacy while full concealment kills curiosity, establishing the calibration problem: encapsulation must be porous enough to signal what lies within but opaque enough to protect internal complexity'
  - '[source] establishes that the boundary between public and private is not a wall but a gradient, importing the observation that the most usable interfaces are those that hint at deeper capability without demanding the user comprehend it upfront'
limits:
  - '[source] breaks because physical gardens reveal themselves through sensory leakage -- fragrance drifts over walls, birdsong carries, colors glimpsed through gaps -- while software interfaces can only disclose through explicit design choices, meaning the "half-hidden" quality requires deliberate construction rather than emerging from natural properties of the medium'
  - '[source] misleads by implying that the hidden portion is desirable and will reward exploration, when in software the hidden internals behind an interface may be technical debt, legacy complexity, or implementation details that the user should never need to encounter'
  - '[source] assumes a single viewer approaching from a public path, but software interfaces serve multiple audiences simultaneously -- what should be half-hidden from an end user should be fully visible to a debugging engineer, creating conflicting visibility requirements the garden metaphor does not address'
embodied_patterns:
  - boundary
  - surface-depth
  - container
relation_types:
  - contain
  - enable
  - translate
structure:
  - boundary
abstraction_level: specific
---

## Transfers

Alexander's pattern #111, "Half-Hidden Garden," observes that a garden
which is completely hidden behind a high wall feels secretive and
unwelcoming from the street. A garden completely exposed to the street
loses its sense of enclosure and privacy. The solution is a garden that
is partly visible -- through a gate with gaps, over a low wall, past a
screen of planting -- so that passersby can sense its existence and
character without being fully inside it. The half-visibility creates
an invitation: there is something here worth entering, and entering it
will feel like arriving somewhere distinct from the street.

Key structural parallels:

- **API surface as low wall** -- a well-designed API reveals enough of the
  system's capability to attract the right users without exposing internal
  complexity. The method signatures, type hints, and brief documentation
  visible in an IDE's autocomplete are the glimpse over the garden wall.
  They signal what the system can do without requiring the caller to
  understand how it does it. An API that exposes every internal function
  (no wall) overwhelms; one that provides only opaque handles with no
  documentation (high wall) repels.

- **Progressive disclosure as garden path** -- Alexander's half-hidden
  garden creates a sequence: glimpse from the street, entry through a
  gate, arrival in the full space. In interface design, progressive
  disclosure follows the same structure: a summary view hints at deeper
  content, a click reveals more detail, a drill-down exposes the full
  dataset. Each step reveals more of the garden. The pattern frames
  information architecture as spatial choreography.

- **Encapsulation with discoverability** -- the object-oriented concept
  of encapsulation (hiding internals behind a public interface) achieves
  the wall but often neglects the "half-hidden" quality. A class whose
  public methods give no hint of what capabilities are available behind
  them is a high-walled garden. Good encapsulation, in Alexander's
  framing, is a low wall: the internals are protected but their general
  character is perceptible from outside.

- **The invitation to explore** -- Alexander notes that the half-visibility
  creates desire: seeing part of a garden makes you want to see the rest.
  In software, this maps to the "getting started" experience. A CLI tool
  whose `--help` output reveals a thoughtfully organized command structure
  creates the same invitation. A library whose README shows a compelling
  three-line example makes you want to explore its full API. The pattern
  argues that partial revelation is a stronger motivator than complete
  documentation.

- **Boundary as gradient, not edge** -- the garden is not divided into
  "public" and "private" by a single line. There is a transition zone:
  the street, the low wall, the entrance planting, the path, the inner
  garden. In software, the most usable systems create similar gradients:
  public API, internal API, protected helpers, private implementation.
  The pattern reframes access control as a spatial gradient rather than
  a binary classification.

## Limits

- **Software "half-hiding" must be designed, not emergent** -- a physical
  garden behind a low wall naturally emits sensory signals: color, scent,
  sound. These are properties of the garden that leak across the boundary
  without effort. Software has no such natural leakage. An API behind an
  abstraction is completely invisible unless someone deliberately writes
  documentation, type annotations, or examples. The "half-hidden" quality
  in software requires explicit investment in revelation, making it an
  active design choice rather than a natural property of the medium.

- **The hidden interior may not reward exploration** -- Alexander's
  pattern assumes the garden is desirable: entering it will be a positive
  experience. In software, what lies behind the interface may be legacy
  code, poorly documented internals, or accidental complexity that the
  abstraction was specifically designed to hide. The half-hidden metaphor
  implies that exploration is always rewarding, but in many software
  systems the abstraction is a mercy, not a tease.

- **Multiple audiences need different visibility** -- a garden on a street
  serves one audience (passersby who might become visitors). A software
  interface serves many: end users who should see only the curated surface,
  integrators who need to see more of the internals, and maintainers who
  need to see everything. Alexander's single-gradient model does not
  accommodate these layered visibility requirements, which demand multiple
  "walls" at different heights for different viewers.

- **Half-hidden implies stability of the interior** -- Alexander's garden
  is a stable physical space. What you glimpse over the wall today is
  what you will find when you enter tomorrow. Software internals change
  rapidly, and what was glimpsed through the API surface yesterday may be
  refactored, deprecated, or removed tomorrow. The half-hidden metaphor
  does not account for the instability of the concealed space.

## Expressions

- "Progressive disclosure" -- the interaction design principle that
  reveals complexity gradually, the user's path from street to garden
- "Encapsulation" -- the object-oriented principle of hiding internals,
  the garden wall -- though often implemented as total concealment rather
  than Alexander's half-hiding
- "API surface area" -- the visible portion of a system's capability,
  the view over the garden wall
- "Leaky abstraction" -- Joel Spolsky's term for when internals become
  visible unintentionally, the garden wall that has crumbled rather than
  been deliberately lowered
- "Getting started guide" -- the curated first glimpse of a system's
  capabilities, the view through the garden gate

## Origin Story

Pattern #111 in *A Pattern Language* (1977) addresses the relationship
between private gardens and public streets. Alexander observed that
suburban developments with high fences created dead, hostile streetscapes,
while gardens without boundaries felt exposed and were underused. The
half-hidden garden solves both problems by creating a boundary that
signals rather than blocks. The pattern's concern with calibrated
visibility found natural application in software interface design, where
the tension between encapsulation (hiding complexity) and discoverability
(revealing capability) is a central design challenge.

## References

- Alexander, Christopher. *A Pattern Language* (1977), Pattern #111:
  Half-Hidden Garden
- Spolsky, Joel. "The Law of Leaky Abstractions" (2002) -- on the
  failure mode of boundaries that reveal too much
- Nielsen, Jakob. "Progressive Disclosure" (2006) -- the interaction
  design principle as systematic half-hiding
