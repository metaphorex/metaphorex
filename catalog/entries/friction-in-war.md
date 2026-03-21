---
slug: friction-in-war
name: Friction in War
kind: metaphor
source_frame: war
applies_to:
- systems-thinking
- leadership-and-management
categories:
- decision-making
- organizational-behavior
author: agent:metaphorex-miner
contributors: []
related:
- fog-of-war
- death-by-a-thousand-cuts
- murphy-s-law
provenance: napoleons-military-maxims
created: '2026-03-20'
updated: '2026-03-20'
grounding: established
harness: Claude Code
transfers:
  - '[source] Friction between surfaces converts directed motion into heat and waste, importing the structure where purposeful effort degrades into overhead and delay at every interface between components'
  - '[source] Friction is proportional to the number of contact surfaces and the load being carried, importing the structure where organizational drag increases with both scale and ambition -- larger plans with more dependencies encounter more friction'
  - '[source] Friction cannot be eliminated from a mechanical system, only reduced through lubrication, importing the structure where operational drag is an irreducible feature of complex action, not a failure to be fixed but a force to be managed'
limits:
  - '[source] breaks because physical friction is predictable and measurable with known coefficients, while Clausewitzian friction is emergent and resists quantification -- you cannot calculate the friction coefficient of an exhausted supply clerk misrouting ammunition'
  - '[source] misleads by implying friction is always a negative force to minimize, when in mechanical systems friction is sometimes essential (brakes, traction, grip) -- analogously, some organizational "friction" (review processes, safety checks) prevents catastrophic failures'
  - '[source] obscures that Clausewitz''s friction is partly psychological -- fear, exhaustion, confusion, and moral uncertainty contribute as much as logistical snags, but the mechanical metaphor focuses attention on systemic rather than human sources of degradation'
---

## Transfers

Clausewitz devoted a chapter of *On War* (Book I, Chapter 7) to "friction,"
arguing that "everything in war is very simple, but the simplest thing is
difficult." The metaphor borrows from mechanics: physical friction is the
resistance that opposes motion at every point of contact between surfaces.
Clausewitz applies this to war to name the aggregate effect of countless
small impediments -- a misread map, a delayed courier, a rainstorm that
turns roads to mud, a nervous sentry who fires too early -- that together
transform elegant plans into chaotic reality.

Key structural parallels:

- **Proportional to complexity** -- in mechanics, friction multiplies with
  the number of moving parts and contact surfaces. In Clausewitz's model,
  friction scales with the number of units, supply chains, communication
  links, and decision points. A three-person patrol experiences minimal
  friction; a corps-level operation involving thousands of coordinated
  actions experiences enormous friction. This maps directly to software
  deployments (more microservices, more integration friction), corporate
  reorganizations (more departments, more coordination overhead), and
  any system where the number of interfaces grows faster than the number
  of components.
- **The gap between plan and execution** -- Clausewitz's central point is
  that friction makes the difference between what should happen on paper
  and what actually happens in practice. The plan assumes perfect
  communication, full compliance, ideal conditions. Reality delivers none
  of these. This is the structure behind "no plan survives contact with
  the enemy" (Moltke) and behind every project management methodology
  that builds in buffer time. Agile sprints, safety margins in
  engineering, and military rehearsals all exist as friction-management
  techniques.
- **Irreducibility** -- you cannot build a frictionless machine in the
  physical world, and Clausewitz argues you cannot run a frictionless
  military operation. Friction is not a bug to be patched; it is a
  fundamental property of systems where many independent agents must
  coordinate under uncertainty. This insight transfers to DevOps
  ("everything fails all the time"), to manufacturing (Toyota's
  recognition that defects are endemic, not exceptional), and to
  healthcare (checklists exist because human performance under pressure
  is inherently unreliable).
- **Experience as lubrication** -- Clausewitz notes that experienced
  troops and seasoned officers generate less friction, not because they
  eliminate it, but because they have internalized workarounds. The
  veteran knows which roads flood, which subordinates need close
  supervision, which orders need to be repeated. This maps to
  organizational learning: experienced teams ship faster not because
  their processes are better on paper, but because they have
  unconsciously mapped the friction points and route around them.

## Limits

- **Physical friction is measurable; Clausewitzian friction is not** --
  an engineer can calculate friction coefficients and predict energy loss
  with precision. Clausewitz's friction resists quantification because
  it emerges from the interaction of human psychology, organizational
  structure, environmental conditions, and enemy action. Treating
  organizational friction as an engineering problem to be measured and
  optimized imports false precision. The metaphor invites dashboards and
  metrics where judgment and experience are what actually reduce friction.
- **Not all friction is wasteful** -- in mechanics, friction enables
  braking, traction, and grip. A frictionless surface is not useful; it
  is dangerous. Organizational friction includes code review,
  regulatory compliance, safety checklists, and approval chains. The
  Clausewitz metaphor, used carelessly, frames all impediments to speed
  as enemies of effectiveness. "Move fast and break things" is an
  anti-friction ideology that ignores the load-bearing function of
  certain kinds of organizational resistance.
- **The metaphor is mechanical, but the reality is psychological** --
  Clausewitz understood that much of friction is human: fear, fatigue,
  confusion, conflicting loyalties. The mechanical metaphor tends to
  focus attention on process and logistics (fixable, engineerable) at
  the expense of morale and cognition (harder, more fundamental). A
  team experiencing friction because of interpersonal conflict or
  burnout cannot be "lubricated" with better tooling.
- **Friction implies a single direction of desired motion** -- physical
  friction opposes movement along a defined path. But organizational
  friction often arises because there is no agreed-upon direction: teams
  pull in different directions, priorities conflict, strategy is unclear.
  The metaphor assumes the plan is sound and friction is what prevents
  execution, but often the "friction" is a signal that the plan itself
  is wrong.

## Expressions

- "Friction of war" / "Clausewitzian friction" -- the canonical
  military-strategic usage, denoting the cumulative drag of small
  impediments
- "Organizational friction" -- business usage for process overhead,
  coordination costs, and bureaucratic drag
- "Friction log" -- UX research term for a diary of every point where
  a user encounters unnecessary difficulty in a product flow
- "Reduce friction" -- product design and sales language for removing
  obstacles from a conversion or onboarding path
- "Frictionless" -- Silicon Valley ideal (frictionless payments,
  frictionless sharing), implicitly positioning all impediments as waste
- "The simplest thing is difficult" -- Clausewitz's summary of friction,
  often quoted in project management contexts

## Origin Story

Clausewitz introduced the concept in Book I, Chapter 7 of *Vom Kriege*
(1832), titled "Friction in War." He explicitly borrowed from mechanics:
"Friction is the only concept that more or less corresponds to the
factors that distinguish real war from war on paper." The metaphor was
not casual -- Clausewitz chose it precisely because friction in mechanics
was well understood as an irreducible, pervasive force that degraded
ideal performance.

The concept gained renewed currency in the twentieth century as military
theorists (particularly the U.S. Marine Corps doctrine *Warfighting*,
1989) adopted Clausewitz as foundational reading. Barry Watts's 1996
monograph *Clausewitzian Friction and Future War* provided the most
sustained modern analysis. In business, the concept migrated through
management consulting and MBA curricula that draw on military strategy.

## References

- Clausewitz, Carl von. *On War*, Book I, Chapter 7: "Friction in War"
  (1832) -- the foundational text
- United States Marine Corps. *Warfighting* (MCDP 1, 1989) -- doctrine
  manual that popularized Clausewitz for a generation of officers
- Watts, Barry D. *Clausewitzian Friction and Future War* (1996) --
  monograph examining friction's relevance to modern warfare
- Perrow, Charles. *Normal Accidents* (1984) -- systems theory parallel:
  "normal accidents" as friction's catastrophic endpoint
