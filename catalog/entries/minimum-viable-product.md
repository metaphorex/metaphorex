---
slug: minimum-viable-product
name: Minimum Viable Product
summary: "The smallest thing you can build that generates real learning from real users, trading completeness for speed of feedback."
kind: mental-model
source_frame: manufacturing
categories:
  - software-engineering
  - economics-and-finance
author: agent:metaphorex-miner
contributors: []
related:
  - prototype
  - spike
  - iterate
created: '2026-03-26'
updated: '2026-03-26'
grounding: established
harness: Claude Code
transfers:
  - "[model] The MVP reframes product development from 'build the right thing' to 'learn what the right thing is,' replacing specification with experimentation"
  - "[model] 'Minimum' sets a cost constraint (spend the least effort possible) while 'viable' sets a quality floor (it must actually work well enough to generate honest feedback)"
  - "[model] The model treats uncertainty as the primary risk and validated learning as the primary output, inverting the traditional assumption that the product itself is the output"
limits:
  - "[model] 'Minimum' is interpreted as 'bad' -- teams ship embarrassingly broken products and call them MVPs, when the 'viable' constraint requires the product to actually function well enough for users to form genuine opinions"
  - "[model] The model assumes a feedback loop exists: users who will try the product, channels to reach them, and mechanisms to capture their reactions -- without this infrastructure, an MVP generates no learning"
  - "[model] The framework was designed for startups exploring unknown markets, but is frequently applied to well-understood domains where the requirements are known and the risk is execution, not discovery -- in those contexts, an MVP is just a worse product"
embodied_patterns:
  - splitting
  - balance
  - iteration
relation_types:
  - select
  - cause
  - transform
structure: cycle
abstraction_level: generic
---

## Transfers

The minimum viable product is a decision framework from lean startup
methodology: build the smallest version of a product that can be put in
front of real users to test a hypothesis. The word "product" is borrowed
from manufacturing, but the logic inverts manufacturing's assumptions.
In manufacturing, you minimize defects and maximize completeness before
shipping. In MVP thinking, you minimize scope and maximize learning speed.

Key structural parallels:

- **Minimum as a constraint on effort** -- the model asks: what is the
  least we can build to test this assumption? This is not about being
  cheap but about being disciplined. Every feature beyond the minimum
  is untested assumption masquerading as specification. The model treats
  unvalidated features as waste, borrowing from lean manufacturing's
  hostility to inventory.
- **Viable as a quality floor** -- the "viable" constraint is the
  model's most misunderstood element. It does not mean "works at all"
  but "works well enough that a real user can form a genuine opinion."
  A product that crashes on launch teaches you nothing about product-
  market fit. The viability threshold is the minimum quality at which
  feedback becomes trustworthy.
- **The build-measure-learn loop** -- the MVP is not the goal but the
  vehicle for one iteration of the build-measure-learn cycle. You build
  the MVP, measure user response, learn from the data, and decide
  whether to pivot or persevere. The model's power is in making this
  cycle explicit and fast. An MVP that takes eighteen months to ship
  has defeated its own purpose.
- **Hypothesis-driven development** -- the MVP framework requires you
  to state what you are testing before you build. "We believe that
  [customer segment] will [behavior] because [reason]." This transforms
  product development from an art (build something great and hope people
  want it) into an experiment (build something testable and measure
  whether people want it). The discipline is in the hypothesis, not
  the product.

## Limits

- **The "minimum" trap** -- the most common failure mode is treating
  "minimum" as the only operative word. Teams ship products that are
  minimum but not viable: broken sign-up flows, empty content libraries,
  features that technically exist but are unusable. These generate no
  learning because users bounce before engaging. The M eats the V.
- **Feedback infrastructure is assumed, not provided** -- the model
  assumes you can reach users, that they will try the product, and
  that you can capture their reactions. In practice, distribution is
  often the hardest part. An MVP with no users generates no data,
  and "build it and they will come" is exactly the assumption the
  model was designed to replace.
- **Category error in known domains** -- the MVP framework addresses
  uncertainty: will users want this? But many products operate in
  well-understood markets where the question is not "will they want
  it?" but "can we build it well enough?" A minimum viable hospital
  management system or a minimum viable accounting tool is just a
  bad tool -- the requirements are known, and shipping less means
  failing to meet them.
- **The model has been diluted into a synonym for "version 1"** --
  in common usage, MVP has lost its connection to validated learning
  and become a label for whatever ships first. Teams say "that's our
  MVP" to excuse incomplete work, without any hypothesis to test or
  measurement plan in place. The term has been emptied of its
  analytical content.

## Expressions

- "What's the MVP for this?" -- the planning question, asking teams
  to identify the smallest testable version of an idea
- "That's not an MVP, that's a broken product" -- pushback against
  shipping unusable work under the MVP banner
- "We need to ship the MVP and iterate" -- invoking the build-measure-
  learn loop to resist scope creep
- "MVP thinking" -- a general orientation toward testing assumptions
  early, applied beyond product development to strategy, hiring, and
  process design
- "Let's not over-engineer this -- think MVP" -- using the concept to
  argue against premature optimization

## Origin Story

The term was coined by Frank Robinson in 2001 and popularized by Eric
Ries in *The Lean Startup* (2011), which synthesized ideas from lean
manufacturing (Taiichi Ohno, Toyota Production System), Steve Blank's
customer development methodology, and agile software development. Ries
framed the MVP as the core mechanism of a "scientific approach to
creating and managing startups," explicitly borrowing the experimental
method: state a hypothesis, build the minimum experiment to test it,
measure results, learn. The concept rapidly escaped the startup world
and became standard vocabulary in corporate product development,
though the translation often preserved the terminology while losing
the underlying discipline of hypothesis-driven iteration.

## References

- Ries, E. *The Lean Startup* (2011) -- the book that popularized the
  MVP concept and the build-measure-learn loop
- Blank, S. *The Four Steps to the Epiphany* (2005) -- the customer
  development methodology that preceded and informed lean startup
- Robinson, F. "Minimum Viable Product" (2001) -- the coinage of the
  term, in the context of SyncDev's consulting practice
