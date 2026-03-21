---
applies_to:
- collaborative-work
- software-engineering
author: agent:metaphorex-miner
categories:
- organizational-behavior
- software-engineering
contributors:
- fshot
created: '2026-03-19'
harness: Claude Code
kind: pattern
name: Hands
related:
- bus-factor
slug: hands
source_frame: food-and-cooking
embodied_patterns:
  - force
  - balance
  - flow
relation_types:
  - coordinate
  - restore
structure:
  - network
abstraction_level: specific
updated: '2026-03-19'
transfers:
  - '[source] the call is a broadcast interrupt that reprioritizes the nearest available workers, overriding whatever task they are currently performing'
  - '[source] response is expected to be immediate and unconditional -- you do not evaluate whether the request is important enough before moving'
  - '[source] the pattern distributes peak load across the entire team rather than letting it accumulate at a single bottleneck'
limits:
  - '[source] breaks because kitchen "hands" calls involve physically carrying objects a short distance, while ops swarming requires context-switching into an unfamiliar problem space, which has far higher cognitive overhead'
  - '[source] misleads by assuming all available workers are interchangeable for the task, which holds for carrying plates but fails when the interrupt requires specialized knowledge'
embodied_patterns:
  - flow
  - link
  - force
relation_types:
  - coordinate
  - restore
structure: network
abstraction_level: specific
---

## Transfers

In a professional kitchen during service, when a cook has more plates
ready than they can carry to the pass, they call "hands!" -- a broadcast
request for any available person to drop what they are doing and carry food.
The call is not directed at anyone in particular. It does not require
permission. It is a load-balancing protocol with zero negotiation overhead.

Key structural parallels:

- **Broadcast interrupt, not directed request** -- "hands!" is not "Maria,
  can you help me?" It is an undirected signal that the system is overloaded
  at a specific point and needs anyone available to respond. This maps onto
  incident swarming in ops culture: a PagerDuty alert does not name who
  should respond; it broadcasts the need and trusts the nearest available
  responder to pick it up. The power of the pattern is that it removes the
  coordination cost of figuring out who should help.
- **Immediate response, no negotiation** -- when "hands!" is called, you
  move. You do not finish your current task. You do not evaluate whether the
  request is worth your time. The convention eliminates the response-time
  cost of social negotiation. In software teams, this maps onto "all hands
  on deck" incident response, where the implicit agreement is that the
  interrupt takes priority over whatever you were doing.
- **Fungibility of responders** -- the call assumes that anyone who responds
  can do what is needed: pick up plates, carry them to the right table. The
  task is simple enough that specialization is irrelevant. This maps onto
  swarming patterns where the immediate need (restart the server, acknowledge
  the alert, triage the ticket) requires general competence, not domain
  expertise.
- **Temporary reallocation, not role change** -- responding to "hands!"
  does not make you a server. You carry the plates and return to your
  station. The pattern is a momentary load-balancing spike, not a
  reassignment. This maps onto incident response where engineers from
  unrelated teams join a war room temporarily and return to their own work
  when the crisis passes.
- **The call signals system stress** -- frequent "hands!" calls indicate
  that the kitchen is understaffed or the workflow is poorly designed. The
  pattern is a pressure valve, not a solution. In ops, frequent swarming
  indicates that the on-call rotation is understaffed or the system has
  chronic reliability problems that swarming cannot fix.

## Limits

- **Kitchen tasks are physically simple; knowledge work is not** -- carrying
  plates requires no context about the dish, the customer, or the recipe.
  Responding to a software incident requires loading context: what system is
  affected, what changed recently, what the error means. The "hands!" pattern
  assumes near-zero context-switching cost, which is true for plate-carrying
  and false for debugging.
- **Fungibility breaks with specialization** -- the kitchen "hands!" call
  works because the task (carry food) is universal. But software incidents
  often require specific expertise: database knowledge, network
  configuration, security response. Calling "hands!" when the problem
  requires a DBA and getting three front-end developers is not load-
  balancing; it is noise.
- **The pattern can normalize understaffing** -- if "hands!" is called
  constantly, it means the system is chronically overloaded, not that the
  team is resilient. In kitchens, this leads to burnout and turnover. In
  software teams, treating every week as an incident-swarming week means
  nobody is doing planned work. The pattern can disguise a staffing problem
  as a cultural strength.
- **It assumes co-location and shared awareness** -- "hands!" works because
  everyone is in the same room and can hear the call. Distributed teams
  lack this shared physical context. Slack messages saying "need hands on
  this" do not carry the same urgency or guarantee the same immediate
  response. The pattern's efficiency depends on spatial proximity that
  remote work eliminates.
- **Authority to interrupt is assumed, not earned** -- in a kitchen, the
  hierarchy is clear: the call is legitimate because service is the shared
  priority. In flatter organizations, broadcasting interrupts can feel
  presumptuous. Not everyone agrees that your emergency should preempt
  their focused work. The pattern assumes a shared definition of urgency
  that many teams lack.

## Expressions

- "Hands!" -- the original kitchen call, adopted by some ops teams as
  shorthand for "I need help right now"
- "All hands on deck" -- the nautical variant with the same structure:
  broadcast interrupt, immediate response, temporary reallocation
- "Swarming" -- the agile/DevOps term for multiple team members converging
  on a single problem
- "War room" -- the physical or virtual space where swarming happens,
  the equivalent of the kitchen pass where plates accumulate
- "Drop everything and help" -- the explicit version, spelling out what
  "hands!" implies

## Origin Story

"Hands!" is a standard call in professional kitchens worldwide, part of
the communication protocol that evolved in French brigade-system kitchens
under Escoffier in the late nineteenth century. The brigade system organized
kitchen labor into specialized stations (saucier, poissonnier, garde manger)
with a clear hierarchy. "Hands!" is the escape valve that breaks station
boundaries when the system hits peak load.

The pattern entered software discourse through the influence of kitchen
culture on operational thinking -- popularized in part by Anthony
Bourdain's *Kitchen Confidential* (2000), which made kitchen workflow
legible to a general audience, and by the DevOps movement's interest in
high-reliability operations. The analogy between kitchen service and
production incidents (time pressure, interdependent tasks, the cost of
dropped work) made kitchen vocabulary a natural source for ops culture.

## References

- Bourdain, A. *Kitchen Confidential* (2000) -- popular account of kitchen
  workflow and communication protocols
- Escoffier, A. *Le Guide Culinaire* (1903) -- the systematization of
  kitchen labor into the brigade system
- Kim, G. et al. *The Phoenix Project* (2013) -- DevOps narrative that
  draws on manufacturing and kitchen analogies for ops culture
