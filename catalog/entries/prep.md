---
slug: prep
name: Prep
kind: metaphor
source_frame: food-and-cooking
applies_to:
  - organizational-behavior
categories:
  - systems-thinking
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - mise-en-place
  - a-la-minute
  - all-day
dead: false
created: '2026-03-19'
updated: '2026-03-19'
grounding: folk
harness: Claude Code
transfers:
  - '[source] prep work is temporally separated from service -- chopping, measuring, and organizing happen hours before the first order arrives, encoding the principle that invisible upstream work determines the quality and speed of visible downstream execution'
  - '[source] prep is evaluated by its absence: when prep is done well, service is smooth and nobody notices; when it is done poorly, every subsequent step degrades, making it structurally analogous to infrastructure, build systems, and onboarding processes that are only visible when they fail'
  - '[source] the ratio of prep time to service time in a professional kitchen (typically 3:1 or higher) makes visible a proportion that most organizations systematically underestimate -- the setup work required to make execution look effortless'
limits:
  - '[source] breaks because kitchen prep has a fixed, knowable scope determined by the menu and the expected cover count, while most organizational prep work (infrastructure setup, sprint planning, onboarding) faces an open-ended scope where "how much prep is enough" has no objectively correct answer'
  - '[source] misleads by importing the kitchen''s sharp temporal boundary between prep and service into domains where the two overlap -- software teams cannot "finish all the prep" before beginning execution because requirements, tools, and environments change continuously during the work'
embodied_patterns:
  - path
  - part-whole
  - matching
relation_types:
  - enable
  - coordinate
structure: pipeline
abstraction_level: specific
---

## Transfers

In professional kitchens, "prep" is the hours of work that happen
before the restaurant opens: brunoise of vegetables, fabrication of
proteins, reduction of stocks, portioning of ingredients, organization
of stations. Prep is the invisible work that makes visible work
possible. A line cook who walks into service without prep is dead
before the first ticket prints.

Key structural parallels:

- **Invisible work enables visible performance** -- prep is
  definitionally upstream and invisible. No diner sees the cook
  julienning carrots at 2 PM. What they see is a dish that arrives
  in twelve minutes, perfectly composed. The structural insight is
  that execution speed and quality during service are determined
  hours earlier, during prep. This maps onto any domain where the
  quality of preparation determines the quality of performance:
  infrastructure provisioning before deployment, rehearsal before
  performance, sprint planning before execution, test suite
  construction before development.

- **Evaluated by absence** -- prep done well is invisible. Nobody
  notices that the station is organized, the ingredients are
  portioned, the sauces are ready. Prep done poorly is immediately
  and catastrophically visible: the cook reaches for diced onion
  and finds none, the service slows, tickets pile up, the kitchen
  enters the weeds. This negative-visibility property maps onto
  infrastructure, security, and platform engineering. Well-maintained
  CI/CD pipelines are invisible. Build systems that break are very
  visible. The structural parallel explains why prep work is
  chronically undervalued: its success is indistinguishable from
  nothing happening.

- **The 3:1 ratio** -- in a professional kitchen, a typical day
  involves three to four hours of prep for every hour of service.
  This ratio is known, accepted, and budgeted for. In most
  organizations, the equivalent ratio is neither measured nor
  acknowledged. Teams estimate the time for "the work" (service)
  without accounting for the prep: environment setup, tooling
  configuration, documentation, dependency management. The kitchen
  makes the ratio explicit and treats it as non-negotiable. The
  metaphor imports this discipline: if your prep-to-service ratio
  is wrong, your service will suffer, regardless of how skilled
  your team is during execution.

- **Prep is skilled labor** -- in the brigade system, prep is not
  relegated to unskilled workers. Fabricating proteins, making
  mother sauces, and tempering chocolate all require significant
  skill. The metaphor challenges the common organizational
  assumption that "setup work" is junior work. Infrastructure
  engineering, test architecture, and build system design are
  prep -- and they require senior expertise precisely because
  errors in prep cascade through every subsequent step.

## Limits

- **Fixed scope versus open-ended scope** -- kitchen prep has a
  knowable scope. The menu is fixed, the expected cover count is
  estimated, and the prep list can be written down completely
  before work begins. Most organizational prep work does not have
  this property. "Prep the infrastructure" is an open-ended task
  because the requirements are not fully known, the environment
  changes, and the scope creeps. The metaphor imports a bounded
  confidence ("prep is finishable") that may not be warranted.

- **Sharp temporal boundary** -- the kitchen has a hard line
  between prep and service. Prep ends when service begins.
  This boundary does not exist in most knowledge work. Software
  teams cannot "finish all the prep" and then "begin service"
  because requirements change, tools update, and new dependencies
  emerge during execution. The metaphor suggests a sequential
  process (prep then perform) that real work rarely follows.

- **Perishability** -- kitchen prep has a built-in freshness
  constraint. Prep done today is used today. Prep done too far
  in advance degrades -- cut herbs wilt, portioned fish dries,
  reduced sauces break. The metaphor does not map well onto
  domains where prep work has no natural expiration: an
  infrastructure script written last month is still valid if
  nothing changed. Conversely, in fast-moving domains, prep work
  can become obsolete faster than kitchen prep spoils --
  documentation written before a major refactor may be worse
  than no documentation.

- **The romance of hustle** -- kitchen culture romanticizes the
  intensity of service and sometimes treats prep as lesser work:
  the boring part before the exciting part. Importing this
  hierarchy into organizations reinforces the existing bias
  against preparation, planning, and maintenance in favor of
  visible, high-intensity execution. The metaphor's cultural
  baggage can undermine the very lesson it should teach.

## Expressions

- "Did you do your prep?" -- asking whether upstream work is
  complete before beginning execution
- "We need more prep time" -- requesting time for setup and
  planning before being expected to deliver
- "That's a prep task, not a service task" -- distinguishing
  upstream infrastructure work from downstream execution
- "No prep, no service" -- the kitchen maxim, applied to any
  domain where execution depends on prior preparation
- "We're prepping for launch" -- applying culinary terminology
  to product releases, event planning, or project kickoffs
- "The prep-to-service ratio is off" -- diagnosing an
  underinvestment in preparation relative to execution demands

## Origin Story

"Prep" as a distinct category of culinary labor is codified in
Auguste Escoffier's brigade system (*Le Guide Culinaire*, 1903),
which formalized the division of kitchen labor into stations and
phases. The separation of prep from service is a foundational
principle of professional kitchen organization, taught at every
culinary school and reinforced in every professional kitchen
worldwide.

The term migrated into general organizational language through
two channels. First, the lean and agile movements adopted kitchen
metaphors alongside manufacturing metaphors, recognizing that the
kitchen is a high-throughput, high-variability production
environment with lessons for knowledge work. Second, Anthony
Bourdain's *Kitchen Confidential* (2000) and subsequent media
presence made kitchen culture legible to a broad audience, and
terms like "prep," "mise en place," and "in the weeds" entered
the vocabulary of technology teams, project managers, and
productivity writers. Dan Charnas's *Work Clean* (2016) made the
transfer explicit, treating kitchen prep methodology as a
framework for knowledge work preparation.

## References

- Escoffier, A. *Le Guide Culinaire* (1903) -- codification of
  the brigade system and prep/service distinction
- Bourdain, A. *Kitchen Confidential: Adventures in the Culinary
  Underbelly* (2000) -- kitchen culture made legible to outsiders
- Charnas, D. *Work Clean: The Life-Changing Power of Mise-en-Place*
  (2016) -- prep methodology applied to knowledge work
- Ruhlman, M. *The Making of a Chef* (1997) -- culinary school
  pedagogy and the role of prep in professional training
