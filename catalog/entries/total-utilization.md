---
slug: total-utilization
name: Total Utilization
kind: mental-model
source_frame: food-and-cooking
categories:
  - systems-thinking
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - mise-en-place
  - cleaning-as-you-go
  - a-la-minute
created: '2026-03-19'
updated: '2026-03-19'
grounding: folk
harness: Claude Code
transfers:
  - '[model] every scrap of material, motion, and time that does not contribute to the finished dish is waste to be eliminated, and the discipline of total utilization means designing workflows so that byproducts are inputs to other processes rather than trash'
  - '[model] wasted space on the station creates wasted motion in the body, which creates wasted time in the service, establishing a causal chain from spatial organization to temporal efficiency that applies to any workstation-based activity'
  - '[model] total utilization is achieved through systematic audit of the workflow -- watching where scraps accumulate, where hands travel empty, where time pools between tasks -- not through general exhortation to "be efficient"'
limits:
  - '[model] breaks when applied to creative or exploratory work, where "waste" (failed experiments, abandoned prototypes, tangential research) is the mechanism of discovery, and eliminating it eliminates the possibility of finding unexpected solutions'
  - '[model] assumes that the output is well-defined and repeatable (the same dish, made the same way, every service), but knowledge work often involves defining the output while producing it, making it impossible to identify waste until after the fact'
---

## Transfers

In professional kitchens, total utilization is the discipline of
extracting every possible use from every ingredient, every motion,
and every square inch of station space. Vegetable trimmings become
stock. Meat bones become demi-glace. Herb stems become bouquet garni.
The same principle extends to motion: a chef who reaches across the
station for salt wastes time and risks collisions. A chef whose salt
is at hand does not. Dan Charnas, in *Work Clean*, identifies total
utilization as Principle 10 of mise en place: "Use space to create
time."

Key structural parallels:

- **Waste is a design flaw, not an inevitability** -- the central
  claim of total utilization is that waste is evidence of poor
  workflow design, not a natural byproduct of production. When
  parsley stems go in the trash, the kitchen has failed to design
  a process that uses them. When a developer writes code that is
  never deployed, the team has failed to design a workflow that
  prevents unbuildable features from starting. The mental model
  reframes waste from "the cost of doing business" to "a signal
  that the system needs redesign."

- **Space, motion, and time are causally linked** -- Charnas captures
  this as "conserve space to conserve motion to conserve time." A
  cluttered workstation forces longer reaches, which slow each task,
  which cascade into missed timing across the entire service. The
  causal chain is spatial organization to physical efficiency to
  temporal performance. In knowledge work, the equivalent chain is:
  a cluttered file system forces longer searches, which slow each
  task, which cascade into missed deadlines. A cluttered codebase
  forces longer navigation, which slows each change, which cascades
  into slower delivery. The mental model insists that efficiency
  starts with the workspace, not with the worker's effort.

- **Byproducts are inputs** -- the highest form of total utilization
  is designing processes so that one task's waste becomes another
  task's raw material. Chicken carcasses become stock. Stock becomes
  sauce. Sauce trimmings season the next batch. In software, this
  maps onto the principle that logging output should feed monitoring,
  monitoring alerts should feed incident postmortems, postmortem
  findings should feed backlog prioritization. Each "byproduct" of
  operational work becomes input to a planning process. The model
  argues that a mature system has no terminal waste streams -- every
  output feeds something.

- **Utilization is measured by audit, not aspiration** -- a chef
  practicing total utilization does not simply resolve to waste less.
  She watches the trash can: what is going in? She watches her hands:
  where are they traveling empty? She watches the clock: where is
  time pooling between tasks? The mental model insists on empirical
  observation of actual waste, not abstract commitments to
  efficiency. In software teams, this maps onto value stream mapping:
  measuring the actual time code spends in each stage (writing,
  review, testing, deployment) and identifying where time accumulates
  without producing value.

## Limits

- **Creative work requires waste** -- total utilization assumes that
  the output is known and the process is repeatable. A chef making
  the same consomme for the hundredth time can optimize every motion
  and ingredient. A research team exploring a new problem domain
  cannot, because they do not yet know what the "dish" is. Discarded
  prototypes, abandoned experiments, and tangential reading are not
  waste -- they are the search process by which the output is
  discovered. Applying total utilization to R&D suppresses
  exploration and produces only incremental improvements to known
  recipes.

- **Defining waste requires a stable definition of value** -- in a
  kitchen, value is clear: the finished dish, served to the guest,
  on time. Anything that does not contribute to that outcome is
  waste. In knowledge work, value is often ambiguous: is a team
  meeting waste or alignment? Is documentation waste or insurance?
  Is refactoring waste or investment? The mental model requires a
  clear value definition to function, and when that definition is
  contested, the model cannot distinguish waste from investment.

- **The model optimizes locally** -- total utilization on a single
  station can produce a globally suboptimal kitchen. If every chef
  hoards ingredients to minimize their personal waste, the kitchen
  as a whole may waste more because one station's surplus cannot
  flow to another station's deficit. In software teams, individual
  developers optimizing their personal workflow (minimizing context
  switches, batching code reviews) can create team-level bottlenecks
  (long review queues, blocked dependencies). The model must be
  applied at the system level, not the individual level, but the
  culinary source frames it as a personal discipline.

- **100% utilization is a system failure** -- queuing theory
  demonstrates that as utilization approaches 100%, wait times
  approach infinity. A kitchen running at total utilization with no
  slack cannot absorb a rush, a sick call, or a supply disruption.
  The mental model's name suggests that full utilization is the goal,
  but systems that maintain slack (deliberately underutilized
  capacity) are more resilient than systems that consume every
  resource. The model must be read as "eliminate waste" rather than
  "use everything at full capacity."

## Expressions

- "Use space to create time" -- Charnas's formulation of the
  space-motion-time causal chain
- "Zero waste" -- the aspirational target of total utilization,
  borrowed from environmental sustainability
- "Root-to-stem cooking" -- the culinary practice of using every
  part of a vegetable, the ingredient-level expression of total
  utilization
- "Value stream mapping" -- lean manufacturing technique for
  identifying waste in a production process
- "Dead code" -- software equivalent of unused scraps: code that
  exists but serves no purpose
- "YAGNI" (You Aren't Gonna Need It) -- the software principle
  that unneeded code is waste, closely aligned with total
  utilization's logic

## Origin Story

Total utilization as a culinary principle is as old as peasant
cooking, where economics demanded that nothing edible be discarded.
Classical French cuisine codified it: Escoffier's kitchen used
every part of every animal, and his *Le Guide Culinaire* (1903)
includes recipes for trimmings, offcuts, and bones precisely
because waste was professionally unacceptable.

Dan Charnas formalized total utilization as Principle 10 of mise
en place in *Work Clean: The Life-Changing Power of Mise-en-Place
to Organize Your Life, Work, and Mind* (2016), where he extended
it beyond ingredients to encompass space, motion, and time. Charnas
drew the explicit parallel to lean manufacturing's waste
elimination (Toyota's *muda*, *muri*, *mura*) and argued that the
kitchen's version was more intuitive because waste is physically
visible: you can see the overflowing trash can, feel the extra
steps, watch the clock tick during idle moments. The mental model
bridges culinary craft and knowledge work through the shared
principle that efficiency is achieved by designing waste out of
the system rather than working harder within a wasteful system.

## References

- Charnas, Dan. *Work Clean: The Life-Changing Power of Mise-en-
  Place to Organize Your Life, Work, and Mind* (2016) -- total
  utilization as Principle 10
- Escoffier, Auguste. *Le Guide Culinaire* (1903) -- classical
  codification of waste elimination in professional cooking
- Ohno, Taiichi. *Toyota Production System* (1988) -- the
  manufacturing parallel: identifying and eliminating seven types
  of waste
- Poppendieck, Mary & Tom. *Lean Software Development* (2003) --
  translating waste elimination from manufacturing to software
