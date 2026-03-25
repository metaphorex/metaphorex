---
slug: jevons-paradox
name: "Jevons Paradox"
summary: "Efficiency gains can increase total consumption by lowering the effective price and stimulating new demand."
kind: mental-model
source_frame: economics
categories:
- systems-thinking
- economics-and-finance
author: agent:metaphorex-miner
contributors: []
related: []
created: '2026-03-21'
updated: '2026-03-21'
grounding: established
transfers:
  - '[law] Making a resource cheaper to use per unit increases total consumption rather than decreasing it'
  - '[law] Efficiency gains create surplus that gets reinvested in more of the same activity, not saved'
  - '[law] The demand curve for a resource is more elastic than efficiency-focused planners assume'
limits:
  - '[law] Applies only when demand for the resource is elastic -- if nobody wants more of the thing, efficiency gains do reduce total consumption'
  - '[law] Conflates the rebound effect (partial offset) with full paradox (total consumption exceeds pre-efficiency baseline), when most measured cases show partial rebound, not full paradox'
embodied_patterns:
  - flow
  - scale
  - balance
relation_types:
  - cause
  - enable
structure: cycle
abstraction_level: generic
---

## Transfers

Efficiency improvements increase total resource consumption, not decrease
it. William Stanley Jevons observed in 1865 that improvements in the
efficiency of coal-burning steam engines had increased total coal
consumption rather than conserving coal. The paradox maps the economic
logic of price elasticity onto resource planning: when each unit of
resource produces more output, the effective price per unit of output
drops, stimulating demand that overwhelms the per-unit savings.

Key structural parallels:

- **The efficiency-demand feedback loop** -- making something cheaper to
  use per unit makes it more attractive to use in total. Jevons observed
  that James Watt's more efficient steam engine did not reduce Britain's
  coal consumption; it made steam power economically viable for factories,
  ships, and railways that previously could not afford it. Each efficiency
  improvement opened new use cases, expanding total demand. The same loop
  operates in computing: more efficient CPUs did not reduce electricity
  consumption; they made computation cheap enough to embed in
  thermostats, doorbells, and toothbrushes.
- **The conservation fallacy** -- efficiency advocates often assume that
  saving X% per unit translates to X% less total consumption. This
  assumes demand is fixed, which it almost never is. The paradox names
  the gap between engineering efficiency (output per unit of input) and
  systemic efficiency (total input consumed). A car that gets twice the
  mileage does not halve fuel consumption if people respond by driving
  twice as far, buying bigger vehicles, or commuting from farther away.
- **The surplus reinvestment mechanism** -- when efficiency creates
  savings, those savings do not disappear. They become available for
  reinvestment. If a factory cuts energy costs by 30%, that 30% becomes
  budget for expansion, additional shifts, or new product lines -- all
  of which consume energy. The paradox is a special case of the general
  principle that freed resources find new uses.
- **The technology adoption ratchet** -- efficiency improvements often
  enable entirely new categories of use that did not exist before, making
  reversal impossible. Before efficient LEDs, decorative lighting at the
  current scale was unthinkable. Before efficient compression, streaming
  video was impossible. The new uses are not substitutions for old ones;
  they are net additions to total consumption.

## Limits

- **Demand elasticity is not infinite** -- the paradox requires that
  demand for the resource (or the output it enables) be highly elastic.
  For resources with truly saturated demand, efficiency gains do reduce
  consumption. If a household already heats to a comfortable temperature,
  a more efficient furnace may genuinely reduce gas consumption because
  there is no latent demand for a warmer house. The paradox is strongest
  for resources that serve as inputs to open-ended activities (computing,
  transportation, communication) and weakest for those serving bounded
  needs (heating to a set point, lighting a room).
- **Rebound versus paradox** -- economists distinguish between the
  "rebound effect" (efficiency gains are partially offset by increased
  use) and the full "Jevons Paradox" (increased use exceeds the
  efficiency gain, leading to higher total consumption). Most measured
  cases show rebound effects of 10-60%, not full paradox. Invoking
  "Jevons Paradox" for any rebound effect overstates the finding and
  can be used to argue (incorrectly) that efficiency improvements are
  pointless.
- **Confuses micro and macro** -- the paradox operates at the system
  level, not the individual level. An individual who buys a more
  efficient car and does not change driving habits does consume less
  fuel. The paradox emerges from aggregate behavior: the average person
  does change habits, and new users enter the market. Applying the
  paradox to individual decisions inverts its scale.
- **Policy interventions can constrain the loop** -- the paradox assumes
  unconstrained demand. Carbon taxes, emissions caps, and usage quotas
  can break the feedback loop by ensuring that efficiency-freed resources
  are not automatically reinvested in more consumption. The paradox is
  a description of what happens without intervention, not a law of nature
  that cannot be overridden.

## Expressions

- "Jevons Paradox in action" -- diagnosis used when an efficiency
  improvement has led to increased total consumption
- "The rebound effect" -- the milder version, acknowledging that some
  (but not all) efficiency gains are offset by increased use
- "Making it cheaper just means we'll use more of it" -- the informal
  formulation, common in sustainability and technology discussions
- "Efficiency is not conservation" -- the policy implication, used to
  argue that efficiency alone cannot solve resource depletion

## Origin Story

William Stanley Jevons published *The Coal Question* in 1865, arguing
that Britain's industrial prosperity depended on coal and that efficiency
improvements in steam engines would not conserve it. His central
observation: "It is wholly a confusion of ideas to suppose that the
economical use of fuel is equivalent to a diminished consumption. The
very contrary is the truth." Jevons was arguing against the optimistic
view that technology would solve the coal depletion problem. The book
influenced British policy debates and established Jevons as one of the
founders of mathematical economics. The paradox was rediscovered in the
1980s and 1990s during debates about energy policy and has become a
standard reference in discussions of sustainability, computing
infrastructure, and AI resource consumption.

## References

- Jevons, William Stanley. *The Coal Question* (1865) -- London:
  Macmillan and Co.
- Alcott, Blake. "Jevons' Paradox" (2005) -- *Ecological Economics*,
  54(1), 9-21
- Kerr, Dave. "Hacker Laws" -- https://github.com/dwmkerr/hacker-laws
