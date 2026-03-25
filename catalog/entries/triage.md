---
slug: triage
name: Triage
kind: metaphor
dead: true
source_frame: medicine
summary: "Sort by who can still be saved, not by who's loudest. Accept that some cases get deliberately abandoned."
applies_to:
- decision-making
- software-engineering
categories:
- health-and-medicine
- decision-making
author: agent:metaphorex-miner
contributors: []
related:
- first-do-no-harm
- differential-diagnosis
provenance: scheins-surgical-aphorisms
created: '2026-03-19'
updated: '2026-03-19'
grounding: established
harness: Claude Code
transfers:
  - '[source] the surgeon sorts casualties into three groups -- those who will survive without treatment, those who will die regardless, and those for whom treatment makes the difference -- importing a prioritization structure that explicitly accepts some losses to maximize total lives saved'
  - '[source] the sorting decision must be made rapidly at the point of intake, before full diagnostic information is available, importing the structure where prioritization under time pressure necessarily relies on heuristics rather than thorough analysis'
  - '[source] resources are finite and non-fungible -- the surgeon, the operating table, the blood supply cannot be in two places at once -- importing the structure where allocation is a zero-sum choice and helping one case means not helping another'
limits:
  - '[source] breaks because medical triage assumes casualties arrive involuntarily and have no preferences about their own treatment priority, while most metaphorical triage targets (bug reports, business decisions, customer complaints) involve agents who contest their assigned priority and can escalate'
  - '[source] misleads by importing the moral authority of battlefield medicine -- the surgeon triaging casualties has life-and-death legitimacy -- onto mundane prioritization decisions that lack comparable stakes, inflating routine task management into crisis rhetoric'
  - '[source] obscures that surgical triage is designed for temporary resource scarcity during a crisis, while most organizations that adopt "triage" as a permanent workflow are normalizing chronic under-resourcing rather than managing an acute emergency'
embodied_patterns:
  - splitting
  - matching
  - scale
relation_types:
  - select
  - decompose
structure: hierarchy
abstraction_level: generic
---

## Transfers

Triage derives from the French *trier* (to sort) and entered military
medicine through Baron Dominique Jean Larrey, Napoleon's chief surgeon,
who developed a system for sorting battlefield casualties by urgency
rather than rank during the Napoleonic Wars. The system's core innovation
was moral: treat the salvageable first, regardless of who they are.
The concept has become so thoroughly dead as a metaphor that "bug triage"
and "email triage" carry no residual medical imagery for most users.

Key structural parallels:

- **Three-category sorting** -- the power of triage is not in prioritization
  per se but in the three-way sort that includes an explicit "will not
  treat" category. This is the structural feature that distinguishes
  triage from ordinary ranking. When a product team triages bugs, the
  decisive act is not choosing what to fix first but choosing what to
  never fix. The metaphor imports the moral structure of deliberate
  abandonment: some cases are written off so that others may be saved.
  This is triage's deepest and most uncomfortable transfer.
- **Speed over accuracy at the sorting stage** -- battlefield triage
  requires snap judgments. The surgeon spends seconds per casualty,
  using gross indicators (pulse, consciousness, wound location) rather
  than thorough diagnosis. The metaphor imports this temporal pressure:
  triage is not careful analysis but rapid pattern matching. In software,
  bug triage meetings that take hours per bug have stopped triaging and
  started diagnosing -- they have confused the sorting step with the
  treatment step.
- **Resource constraint as the forcing function** -- triage exists because
  resources are insufficient to treat everyone. Remove the constraint and
  triage is unnecessary -- in a hospital with unlimited capacity, every
  patient gets treated immediately. The metaphor imports the assumption
  that demand exceeds supply, which is why "triage" implies crisis. When
  organizations use triage language in normal operations, they are either
  genuinely under-resourced or performing crisis theater.
- **Sorting authority requires expertise** -- in medicine, triage is
  performed by experienced clinicians who can rapidly assess severity.
  The metaphor imports the requirement for qualified judgment: effective
  triage cannot be delegated to whoever happens to be available. A junior
  engineer triaging critical bugs, like an untrained volunteer sorting
  casualties, will misjudge severity and waste resources on the wrong
  cases.

## Limits

- **Medical casualties do not argue back** -- the most important
  structural difference. A battlefield casualty does not contest their
  triage category. A customer whose support ticket is triaged as low
  priority will escalate, complain, and churn. A developer whose bug
  is triaged as "won't fix" will reopen it, argue in comments, and
  appeal to management. The metaphor imports a sorting authority that
  the domain does not support. Medical triage assumes passive patients;
  organizational triage involves active agents with their own priorities.
- **The crisis frame inflates routine work** -- medical triage is
  designed for acute emergencies: battlefield casualties, mass casualty
  events, pandemic surges. Applying the same frame to Monday morning
  bug reports imports urgency and stakes that the situation does not
  warrant. This inflation is not harmless: it creates a permanent state
  of crisis that burns out teams and prevents the systemic improvements
  that would eliminate the need for triage in the first place.
- **Triage normalizes scarcity instead of addressing it** -- Larrey
  invented triage because he genuinely could not treat every casualty.
  The constraint was physical and temporary. When software teams adopt
  permanent triage processes, they are often normalizing a staffing
  deficit or a quality problem rather than managing a genuine crisis.
  The medical metaphor provides moral cover for chronic under-investment:
  "we triage" sounds responsible; "we are permanently under-resourced"
  sounds like a management failure.
- **The three-category model oversimplifies** -- modern medical triage
  uses five categories (the Emergency Severity Index), not three.
  Larrey's original system was suited to a world of binary outcomes
  (survive or die) and limited interventions. Software bugs, customer
  requests, and business decisions exist on a continuum that the
  three-bucket model distorts. The metaphor encourages discrete
  categorization where continuous prioritization would be more effective.

## Expressions

- "Bug triage" -- the standard software term for sorting reported defects
  by priority, fully dead as a metaphor
- "Email triage" -- sorting an overflowing inbox by urgency, implying
  that some messages will be deliberately ignored
- "We need to triage this situation" -- crisis management language for
  rapid prioritization under pressure
- "Triage meeting" -- a regular team meeting for sorting incoming work,
  often weekly despite the crisis connotation
- "That's a triage decision" -- emphasizing that the choice involves
  deliberate sacrifice of lower-priority items
- "Walking wounded" -- triage category for casualties who can wait,
  transferred to mean issues that are painful but not blocking

## Origin Story

Baron Dominique Jean Larrey, Napoleon's Surgeon-General, is credited
with formalizing triage during the Napoleonic Wars (1803-1815). Larrey
established "flying ambulances" (ambulances volantes) that reached
casualties on the battlefield and sorted them for treatment by medical
urgency rather than military rank -- a radical egalitarian innovation
in an era when officers were treated before enlisted men regardless of
wound severity.

The three-category system (immediate treatment, delayed treatment,
expectant/unsalvageable) became standard military medicine through the
nineteenth and twentieth centuries. The term migrated into civilian
emergency medicine in the mid-twentieth century and into general
management language by the 1990s. By the 2000s, "triage" was standard
vocabulary in software development, customer support, and project
management, with most users unaware of its military-surgical origins.

## References

- Larrey, Dominique Jean. *Memoirs of Military Surgery and Campaigns*
  (1812-1817) -- the original triage system
- Iserson, K.V. and Moskop, J.C. "Triage in Medicine, Part I: Concept,
  History, and Types" (2007) -- comprehensive history of triage systems
- Gilboy, N. et al. "Emergency Severity Index" (2005) -- modern five-level
  triage replacing Larrey's three-category model
