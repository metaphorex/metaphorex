---
author: agent:metaphorex-miner
harness: Claude Code
categories:
- organizational-behavior
- systems-thinking
contributors: []
created: '2026-03-18'
grounding: established
kind: mental-model
name: Eliminate Slogans
provenance: tps-deming
related:
- a-bad-system-beats-a-good-person
- eliminate-numerical-quotas
- pride-of-workmanship
slug: eliminate-slogans
updated: '2026-03-18'
embodied_patterns:
  - blockage
  - flow
  - force
relation_types:
  - prevent
  - cause
structure: hierarchy
abstraction_level: generic
transfers:
  - "[model] reveals that exhortations addressed to workers presuppose individual control over outcomes, while the bulk of quality variation originates in system design that only management can change"
  - "[model] predicts that slogans demanding zero defects will generate resentment rather than improvement, because the demand highlights the gap between aspiration and capacity without closing it"
  - "[model] distinguishes communication that changes the system (new tooling, revised process, removed bottleneck) from communication that merely restates the desired outcome in louder terms"
limits:
  - "[model] overstates the case against aspirational language -- some slogans function as coordination signals that align attention across large groups, which is a system-level intervention, not mere exhortation"
  - "[model] assumes a clear boundary between system-caused and worker-caused variation, but many real failures involve genuine skill gaps or attention failures that training and motivation can address"
---

## Transfers

Deming's Point 10 directs managers to eliminate slogans, exhortations, and
targets for the workforce. The reasoning is precise: the overwhelming
majority of quality problems -- Deming estimated 94% -- belong to the
system, not to the individual worker. When management posts banners reading
"Zero Defects" or "Do It Right the First Time," they are asking workers to
solve problems that workers do not have the authority or resources to solve.

Key structural parallels:

- **Slogans attribute system failures to individuals** -- a poster urging
  "commitment to quality" implicitly frames quality failures as failures of
  commitment. But a worker on an assembly line with worn tooling, inadequate
  training, and conflicting production quotas cannot commitment their way to
  zero defects. The slogan misdirects attention from the system to the
  person, ensuring the actual causes go unaddressed. This pattern recurs
  whenever leaders respond to systemic problems with motivational messaging:
  "work smarter, not harder" in organizations with broken processes, "move
  fast and break things" in codebases with no test infrastructure.
- **Exhortation creates adversarial relationships** -- Deming observed that
  slogans generate frustration and resentment among workers who already want
  to do good work but are prevented by the system. The worker reads "Zero
  Defects" and thinks: "I would if you'd fix the machine." Over time, the
  gap between slogan and reality erodes trust in management. The dynamic is
  not unique to manufacturing -- it appears whenever performance rhetoric
  outstrips systemic support.
- **The intervention hierarchy matters** -- Deming's point encodes a
  diagnostic ordering: before asking people to perform differently, ask
  whether the system permits different performance. Change the system first.
  If the system already enables quality and defects persist, then training
  or motivation might be relevant. But starting with slogans inverts this
  ordering and wastes the most accessible intervention (system redesign) in
  favor of the least effective one (exhortation).
- **Communication versus action** -- the model distinguishes two kinds of
  organizational communication: communication that changes the system (we
  are replacing this tool, revising this process, removing this bottleneck)
  and communication that restates the desired outcome (be more careful, try
  harder, commit to excellence). Only the first kind constitutes management.
  The second is abdication disguised as leadership.

## Limits

- **Not all slogans are empty exhortation** -- some organizational slogans
  function as coordination signals rather than performance demands. "Move
  fast and break things" at early Facebook was a genuine priority signal
  that authorized specific behavior (shipping without full QA). "Safety
  first" in high-reliability organizations encodes a decision rule (when
  production conflicts with safety, safety wins). Deming's model does not
  distinguish coordinating slogans from exhorting ones, and eliminating all
  slogans would remove a legitimate alignment tool.
- **The 94% attribution is an estimate, not a universal law** -- Deming's
  claim that 94% of variation is system-caused works well in manufacturing
  processes with strong statistical baselines. In knowledge work, creative
  work, or high-skill domains, the system-versus-individual attribution is
  murkier. A software team may have good tools and processes but still
  produce poor code because of genuine skill gaps. The model can become an
  excuse for never addressing individual performance.
- **Workers sometimes need direction, not just enablement** -- the model
  assumes workers already know what good work looks like and are simply
  prevented from achieving it. But in complex or novel domains, workers
  may genuinely not know the target. Clear articulation of goals -- which
  can look like "slogans" -- provides necessary direction. Deming's
  formulation conflates goal-setting with blame-shifting.
- **Cultural context matters** -- Deming developed these ideas primarily in
  American and Japanese manufacturing contexts. In organizations with weak
  management systems, aspirational messaging may be the only tool available
  while system improvements are underway. Eliminating slogans before
  building better systems leaves a vacuum.

## Expressions

- "Zero Defects" -- Philip Crosby's slogan, which Deming considered
  counterproductive when directed at workers rather than systems
- "Do It Right the First Time" -- a common quality slogan that Deming
  argued places blame on workers for system-caused failures
- "Work smarter, not harder" -- managerial exhortation that rarely
  comes with the system changes needed to make smarter work possible
- "We need to be more agile" -- modern variant: an organizational slogan
  substituting for the structural changes agility requires
- "Culture eats strategy for breakfast" -- ironically, itself a slogan
  about the inadequacy of slogans, sometimes used as a substitute for
  structural intervention
- "Move the needle" -- performance exhortation that assumes the
  performer controls the needle's position

## Origin Story

Point 10 of Deming's 14 Points for Management, published in *Out of the
Crisis* (1986), reads: "Eliminate slogans, exhortations, and targets for
the workforce asking for zero defects and new levels of productivity. Such
exhortations only create adversarial relationships, as the bulk of the
causes of low quality and low productivity belong to the system and thus
lie beyond the power of the workforce."

Deming's frustration with slogans was rooted in his statistical training.
He understood variation: if a process is in statistical control, the
outcomes are determined by the system, and no amount of exhortation will
move them outside the system's capability. Only management action on the
system can change the outcomes. He saw American management's addiction to
motivational posters and quality slogans as a symptom of statistical
illiteracy -- a failure to understand where variation comes from.

## References

- Deming, W. Edwards. *Out of the Crisis* (1986), pp. 65-66
- Deming, W. Edwards. *The New Economics for Industry, Government,
  Education* (1993), Chapter 2
- ASQ. "Deming's 14 Points for Total Quality Management."
  https://asq.org/quality-resources/tqm/deming-points
