---
slug: everyone-goes-home
name: Everyone Goes Home
kind: mental-model
source_frame: fire-safety
categories:
  - organizational-behavior
  - risk-management
author: agent:metaphorex-miner
contributors: []
related:
  - good-luck-reinforces-bad-habits
  - lces
  - size-up
  - anchor-point
provenance: firefighting-maxims
created: '2026-03-21'
updated: '2026-03-21'
grounding: established
harness: Claude Code
transfers:
  - '[model] redefines mission success from the output achieved (fire suppressed, building saved) to the workforce preserved, forcing a recalculation where outcomes that destroy the team are coded as failures regardless of the objective accomplished'
  - '[model] encodes the structural insight that heroic cultures systematically undercount the cost of the hero by treating the survivor as the unit of analysis and the fatality as an acceptable exception, rather than treating both as draws from the same risk distribution'
limits:
  - '[model] breaks when the mission genuinely is more valuable than the individual -- military combat, pandemic response, and rescue of trapped civilians all involve situations where refusing to accept personnel risk means accepting certain death for others'
  - '[model] can degrade into a compliance framework where the phrase becomes a bureaucratic checkbox rather than a genuine risk calculus, creating the appearance of safety culture without the substance'
---

## Transfers

"Everyone Goes Home" is the central slogan of the National Fallen
Firefighters Foundation's cultural change initiative, launched in 2004
after decades of firefighter line-of-duty deaths that post-incident
analysis revealed were preventable. The program's premise: the fire
service's heroic identity -- the willingness to risk everything to save
lives and property -- had become a liability. Firefighters were dying
not because the risks were unavoidable but because the culture treated
risk-taking as a virtue rather than a cost.

Key structural parallels:

- **Redefining mission success** -- the fire service traditionally
  measured success by what was saved: the building, the occupants, the
  acreage. "Everyone Goes Home" redefines the metric to include the
  responders themselves. A fire that destroys a building but brings
  every firefighter home is a better outcome than a fire that saves the
  building but kills a crew member. This redefinition transfers to any
  domain where the workforce is treated as expendable in pursuit of the
  objective: software teams burning out to ship a product, medical
  residents working unsafe hours to maintain throughput, organizations
  sacrificing employee wellbeing for quarterly results. The model says:
  if your people do not survive the mission, the mission failed.

- **Heroic identity as systemic risk** -- the fire service's culture
  valorizes the firefighter who takes extraordinary risks. "Everyone
  Goes Home" diagnoses this as a system-level pathology: the individual
  acts of heroism that the culture celebrates are the same behaviors
  that produce fatalities. The hero and the casualty are drawing from
  the same risk distribution; the hero is the survivor, not the
  counterexample. This transfers to startup culture ("move fast and
  break things"), surgical culture ("a chance to cut is a chance to
  cure"), and trading culture ("big risks, big rewards"). In each case,
  the celebrated risk-takers who succeed make the fatal risks taken by
  others invisible.

- **Structural prevention over individual courage** -- the program's 16
  Life Safety Initiatives shift responsibility from the individual
  firefighter's judgment to organizational systems: better training,
  mandatory fitness standards, improved apparatus design, and
  standardized incident management. The structural insight: a culture
  that depends on individual heroism to compensate for systemic failures
  will always produce casualties, because individual judgment is
  variable but systemic pressure is constant. This maps to the software
  engineering principle that safety should be a property of the system
  (type systems, automated testing, deployment safeguards) rather than
  a property of the developer (carefulness, expertise, heroic
  debugging).

- **The risk-benefit calculus made explicit** -- the program's companion
  principle, derived from Chief Alan Brunacini and NFPA 1500, states:
  "Risk a lot to save a lot. Risk a little to save a little. Risk
  nothing to save nothing." This makes the implicit calculus explicit
  and, critically, introduces a zero case: some situations warrant zero
  risk to personnel. A vacant building fully involved in fire is not
  worth a life. The transfer to business is the concept of acceptable
  loss: not every customer complaint warrants an all-hands response, not
  every competitive threat warrants a pivot, and some fights are not
  worth fighting at any price.

## Limits

- **Some missions are worth dying for** -- the model's power comes from
  its absolutism ("everyone"), but this absolutism breaks in domains
  where the mission genuinely outweighs individual survival. Military
  combat, pandemic response with limited protective equipment, and
  rescue of trapped civilians all involve situations where the ethical
  calculus requires accepting personnel risk. Importing "Everyone Goes
  Home" into these contexts without modification produces paralysis:
  if no one can be risked, no one can be saved.

- **Compliance capture** -- institutional adoption of the slogan can
  strip it of operational meaning. When "Everyone Goes Home" becomes a
  poster on the station wall rather than a decision framework on the
  fireground, it degrades into a liability shield. Organizations can
  display the slogan while maintaining the same risk-tolerant culture
  underneath. The model provides a goal but not a mechanism for
  detecting when the goal has been co-opted by the culture it was
  designed to change.

- **Survivor guilt and moral injury** -- when the model is internalized
  but the outcome is a fatality, "Everyone Goes Home" becomes an
  accusation rather than an aspiration. The surviving crew members
  experience the death not as a tragic risk inherent to the profession
  but as a failure of the system they were promised would protect them.
  The model's absolutist framing can amplify psychological harm when
  its promise cannot be kept.

- **The denominator problem** -- "Everyone" includes the people who were
  never at risk. A department can achieve "everyone goes home" by
  avoiding all high-risk incidents, which means the civilians who
  needed rescue did not go home. The model can incentivize
  organizational risk aversion that transfers the cost from the
  responders to the public. The fire service's version addresses this
  through the risk-benefit calculus ("risk a lot to save a lot"), but
  when the slogan is imported into other domains, the nuance is often
  lost.

## Expressions

- "Everyone goes home" -- the slogan itself, now used in fire service
  briefings, training, and organizational culture documents
- "Risk a lot to save a lot, risk a little to save a little, risk
  nothing to save nothing" -- the companion calculus attributed to
  Brunacini
- "No building is worth a life" -- the operational corollary for
  structural firefighting, encoding the zero-risk case
- "We don't trade lives for property" -- the blunt version used in
  fireground decision-making
- "Bring everyone back" -- variant used in military and expedition
  contexts with the same structural logic

## Origin Story

The National Fallen Firefighters Foundation launched the "Everyone Goes
Home" program in 2004, following a 2002 Firefighter Life Safety Summit
in Tampa, Florida. The summit brought together fire service leaders,
researchers, and safety advocates who documented a persistent pattern:
roughly 100 firefighters died on duty each year in the United States,
and a significant fraction of those deaths were preventable through
better training, fitness standards, vehicle safety, and incident
management. The summit produced 16 Firefighter Life Safety Initiatives
that became the program's operational framework. Chief Alan Brunacini of
the Phoenix Fire Department was a central intellectual force, having
articulated the risk-benefit calculus in his writings and NFPA 1500
advocacy since the 1980s. The program drew on NIOSH Fire Fighter
Fatality Investigation reports, which repeatedly identified the same
causal factors: inadequate size-up, failure to maintain accountability,
uncontrolled freelancing, and a culture that equated risk-taking with
professionalism.

## References

- National Fallen Firefighters Foundation. "Everyone Goes Home" program
  (everyonegoeshome.com) -- 16 Life Safety Initiatives
- Brunacini, A. *Fire Command* (1985, 2002) -- risk-benefit framework
- NFPA 1500: Standard on Fire Department Occupational Safety, Health,
  and Wellness Program
- NIOSH Fire Fighter Fatality Investigation and Prevention Program
  (cdc.gov/niosh/fire)
- Firefighter Life Safety Summit Report, Tampa, FL (2002)
