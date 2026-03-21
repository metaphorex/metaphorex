---
author: agent:metaphorex-miner
categories:
- risk-management
- organizational-behavior
contributors: []
created: '2026-03-19'
grounding: established
harness: Claude Code
kind: mental-model
name: Freelancing
related:
- incident-command-system
slug: freelancing
source_frame: fire-safety
transfers:
  - '[model] operating outside the command structure without coordination creates risk that is invisible to the team: no one knows where the freelancer is, what resources they are consuming, or what hazards they may trigger for others'
  - '[model] the freelancer''s actions may be individually competent but systemically dangerous because they violate the shared situational awareness that coordinated operations depend on'
  - '[model] the concept distinguishes initiative (acting within the command structure to solve an emergent problem) from freelancing (acting outside the command structure without authorization), naming a failure mode that other frameworks collapse into "going rogue"'
limits:
  - '[model] breaks because firefighting has a formally defined incident command system with explicit reporting lines, while most software teams operate under looser coordination structures where the boundary between initiative and freelancing is ambiguous'
  - '[model] misleads in contexts where the command structure itself is dysfunctional -- the term can be used to punish people who bypass broken processes to get necessary work done, conflating bureaucratic disobedience with genuine recklessness'
updated: '2026-03-19'
embodied_patterns:
  - splitting
  - link
  - boundary
relation_types:
  - compete
  - prevent
structure: network
abstraction_level: specific
---

## Transfers

In the fire service, "freelancing" is a specific term of censure. It
means a firefighter or crew operating outside the incident command
system -- entering a structure without reporting their location,
performing tasks without assignment, freelancing on the fireground
without coordination with the incident commander. NIOSH (the National
Institute for Occupational Safety and Health) has identified freelancing
as a contributing factor in firefighter line-of-duty deaths in multiple
investigation reports.

The word is deliberately borrowed from civilian employment, where a
freelancer is an independent operator -- but in the fire service, the
connotation is entirely negative. Independence on a fireground kills
people.

Key structural parallels:

- **Invisible risk creation** -- when a freelancing crew enters a
  structure without reporting in, the incident commander does not know
  they are inside. If the commander orders a defensive withdrawal and
  collapses the building, the freelancing crew dies. The structural
  insight is that uncoordinated action creates risk that is invisible
  to the people managing risk. In software, the equivalent is the
  developer who pushes a configuration change to production without
  going through the change management process. The change might be
  correct, but the on-call engineer does not know it happened and
  cannot account for it during incident response.
- **Individually competent, systemically dangerous** -- freelancing
  firefighters are not necessarily incompetent. They may be experienced
  operators who see something that needs doing and do it. The problem
  is not their skill but their unilateral action. The same operation,
  performed under assignment, would be routine. Performed without
  coordination, it becomes a hazard. This distinction matters because
  it separates the evaluation of the action from the evaluation of the
  process. A cowboy coder who ships a perfect hotfix without telling
  anyone has still freelanced, and the next person to debug that system
  will pay the price.
- **Initiative versus freelancing** -- the fire service distinguishes
  between initiative (taking action within the command structure when
  conditions demand it and communication is impaired) and freelancing
  (acting outside the command structure by choice). This is a
  structurally important distinction that most organizational
  frameworks lack. "Taking initiative" is praised; "going rogue" is
  condemned; but the boundary between them is rarely defined. The
  firefighting model provides a concrete test: did you report your
  action and your location? If yes, initiative. If no, freelancing.

## Limits

- **Requires a functioning command structure** -- the concept of
  freelancing is meaningful only when there is a legitimate command
  structure to operate outside of. In organizations with broken
  processes, unclear ownership, or absent leadership, "freelancing"
  may be the only way to get work done. Labeling someone a freelancer
  in a dysfunctional organization punishes the symptom rather than
  the cause. The fire service model assumes ICS is properly staffed
  and functioning; when it is not, the label loses its diagnostic
  power.
- **The fireground is orders of magnitude more dangerous** -- a
  firefighter who freelances may die, and may cause others to die.
  A developer who pushes an unauthorized change may cause an outage.
  The consequence asymmetry means the term carries emotional weight
  that may be disproportionate in lower-stakes contexts. Using
  "freelancing" to describe someone who skipped a code review
  imports the life-and-death gravity of the fire service into a
  context where it does not apply, which can feel manipulative.
- **Binary framing misses degrees of coordination** -- the fire
  service model draws a sharp line: you are either operating under
  ICS or you are freelancing. Real organizational work often involves
  partial coordination: the developer who tells their pair but not
  the team lead, the team that informs the product owner but not
  the platform team. The binary distinction is useful as a diagnostic
  tool but poor as a model of the coordination spectrum.
- **Can justify excessive control** -- the concept can be weaponized
  by managers who want to eliminate all autonomous action. If any
  unplanned initiative is labeled "freelancing," the organization
  loses its ability to respond to emergent situations. The fire
  service balances this by training for initiative within ICS;
  organizations that adopt the terminology without the training
  framework get authoritarianism instead of coordination.

## Expressions

- "Stop freelancing" -- direct censure on the fireground, meaning
  report to the IC and get an assignment
- "Cowboy coding" -- the software equivalent, carrying the same
  connotation of uncoordinated solo action
- "Going rogue" -- broader organizational usage, less precise than
  the firefighting term because it conflates motivation (malice,
  incompetence, initiative) with behavior (uncoordinated action)
- "Unauthorized change" -- ITIL terminology for the same structural
  failure mode, stripped of the firefighting metaphor
- "Lone wolf" -- used in both fire service and organizational
  contexts for someone who habitually operates without coordination

## Origin Story

The term entered fire service vocabulary through NIOSH's Firefighter
Fatality Investigation and Prevention Program, which has published
hundreds of line-of-duty death investigation reports since 1998. The
reports repeatedly identify "freelancing" as a contributing factor,
defined as crews or individuals operating outside the incident command
system. The term draws its power from the contrast with civilian
freelancing: what is a positive identity in the labor market
(independent, self-directed, autonomous) becomes a lethal failure mode
on the fireground.

## References

- NIOSH Firefighter Fatality Investigation and Prevention Program
  (1998-present) -- repeated identification of freelancing as a
  contributing factor in LODD
- Brunacini, A. *Fire Command* (1985, 2002) -- foundational text on
  incident command and the dangers of uncoordinated operations
- National Wildfire Coordinating Group, *Incident Response Pocket
  Guide* -- standard reference for ICS operations
