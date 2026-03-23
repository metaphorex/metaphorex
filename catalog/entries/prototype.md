---
slug: prototype
name: Prototype
kind: mental-model
source_frame: manufacturing
categories:
- cognitive-science
- software-engineering
author: agent:metaphorex-miner
contributors: []
related:
- the-prototype-pattern
- spike
- proof-by-construction
- minimum-viable-product
created: '2026-03-23'
updated: '2026-03-23'
grounding: established
harness: Claude Code
transfers:
  - '[model] frames early attempts as disposable learning instruments rather than failed products, importing the manufacturing practice of building a preliminary model specifically to reveal what the final design should be'
  - '[model] separates the cost of learning from the cost of production -- the prototype absorbs uncertainty so that the production run does not have to'
  - '[model] implies that fidelity should be deliberately limited: a prototype that is too polished discourages the revisions it was built to invite'
limits:
  - '[model] can become a rationalization for shipping unfinished work -- labeling something a "prototype" lowers quality expectations even when the artifact will never be replaced by a production version'
  - '[model] assumes a clean handoff from exploration to production, but in practice prototypes accumulate users, dependencies, and political defenders that prevent their retirement, making the "disposable" framing dishonest'
  - '[model] imports a manufacturing timeline (prototype then production) that obscures iterative development, where the distinction between prototype and product is continuously renegotiated rather than resolved at a single threshold'
embodied_patterns:
  - matching
  - iteration
  - path
relation_types:
  - enable
  - transform/refinement
  - cause/misfit
structure: pipeline
abstraction_level: generic
---

## Transfers

A prototype is a preliminary version of an artifact built to test
assumptions before committing to full-scale production. The word comes
from Greek *prototypon* (first impression), and the manufacturing
practice is ancient: build a rough version, learn from its failures,
then build the real thing. The mental model transfers this sequence --
cheap test, then expensive commitment -- into any domain where
uncertainty is high and production is costly.

Key cognitive moves:

- **Disposability as a feature** -- the prototype's defining property is
  that it is meant to be thrown away. This is counterintuitive: most
  effort aims to produce lasting artifacts. The mental model reframes
  early work as an investment in learning rather than a down payment on
  the final product. Fred Brooks's dictum "plan to throw one away; you
  will anyhow" captures this: the first attempt's purpose is to reveal
  what you did not know, not to survive into production.

- **Fidelity as a design variable** -- a prototype need not (and often
  should not) replicate every property of the final artifact. A paper
  mockup tests layout without testing materials. A software spike tests
  architecture without testing edge cases. The mental model teaches that
  choosing *what to leave out* of the prototype is itself a design
  decision -- it forces the builder to identify which assumptions carry
  the most risk and need testing first.

- **Cost separation** -- manufacturing prototypes separate the cost of
  learning from the cost of production. Tooling for mass production is
  enormously expensive; a hand-built prototype is cheap by comparison.
  The mental model transfers this cost asymmetry: in any domain, the
  prototype should cost a fraction of the full implementation, because
  its purpose is to reduce the risk that the full implementation will
  be wasted. When the prototype costs as much as the production version,
  the model has been misapplied.

- **Revelation of unknown unknowns** -- the prototype's deepest value is
  not in confirming what the builder already suspects but in revealing
  problems that were invisible on paper. A structural prototype reveals
  load-bearing weaknesses. A user interface prototype reveals workflow
  assumptions. The mental model teaches that the prototype is an
  instrument for discovering the questions you did not know to ask.

## Limits

- **The prototype that refuses to die** -- Brooks's advice assumed that
  builders would actually throw away the first version. In practice,
  prototypes accumulate users, integrations, and institutional defenders.
  "We already have something that works" becomes the argument against
  rebuilding properly. The prototype, designed for learning, becomes the
  production system by default. The mental model has no resources for
  this transition because it frames the prototype as disposable -- it
  cannot name the political and economic forces that keep provisional
  artifacts alive.

- **Quality laundering** -- labeling an artifact a "prototype" can
  function as permission to skip quality controls (testing, documentation,
  accessibility, security) that would otherwise be required. When the
  prototype ships to real users without being replaced, the label has
  laundered substandard work. The model assumes the prototype phase has
  a clear endpoint, but in iterative development the boundary between
  prototype and product is often never formally crossed.

- **Premature convergence** -- a prototype makes one set of assumptions
  concrete, which anchors subsequent thinking around those assumptions.
  Teams that build a prototype early may fail to consider architecturally
  different approaches because the prototype has made one path tangible
  and all others abstract. The model teaches "build to learn" but does
  not address the anchoring effect of having built anything at all.

- **Manufacturing linearity does not always transfer** -- the prototype
  → production pipeline assumes a linear sequence: explore, then commit.
  Many domains (software, writing, organizational design) are better
  served by continuous iteration where every version is simultaneously a
  prototype for the next and a production artifact for the present. The
  binary distinction (prototype vs. product) can be more constraining
  than clarifying.

## Expressions

- "Plan to throw one away; you will anyhow" -- Brooks's *The Mythical
  Man-Month* (1975), the canonical statement of deliberate disposability
- "It's just a prototype" -- the quality-lowering hedge, simultaneously
  useful (reduces premature polish) and dangerous (excuses permanent
  shoddiness)
- "The prototype is the spec" -- inversion of the model, where the
  preliminary artifact becomes the definitive reference, common in
  hardware startups and game development
- "Rapid prototyping" -- the practice of compressing the
  prototype-learn-rebuild cycle, imported from manufacturing into
  software, design, and organizational strategy
- "Paper prototype" -- a deliberately low-fidelity version that tests
  concepts without any implementation, emphasizing that the prototype's
  purpose is learning, not demonstration
- "Spike" -- Extreme Programming's term for a targeted prototype that
  tests a single technical assumption

## Origin Story

The word "prototype" enters English from French *prototype*, itself from
Greek *prototypon* ("first impression, original form"), combining
*protos* (first) and *typos* (impression, model). In manufacturing, the
practice of building a preliminary model before committing to production
tooling is ancient -- potters made test firings, architects built scale
models, and shipwrights carved hull models before laying keels. The
formalization of prototyping as a named engineering practice accelerated
in the 20th century with the rise of mass production, where the cost gap
between a hand-built prototype and production tooling made the
explore-then-commit sequence economically rational.

In software, Brooks articulated the disposable prototype in *The
Mythical Man-Month* (1975). The concept was further refined by the rapid
prototyping movement of the 1980s-90s, Extreme Programming's "spike"
concept, and the lean startup movement's "minimum viable product" --
each a variation on the same mental model, differing primarily in what
kind of learning the prototype is designed to produce.

## References

- Brooks, F. P. *The Mythical Man-Month* (1975) -- "plan to throw one
  away" as engineering wisdom
- Schrage, M. *Serious Play: How the World's Best Companies Simulate to
  Innovate* (2000) -- prototyping as organizational learning
- Gamma, E. et al. *Design Patterns* (1994) -- the Prototype pattern as
  a software-specific application
- Buchenau, M. and Suri, J.F. "Experience Prototyping," *DIS '00*
  (2000) -- extending prototyping beyond artifacts to experiences
