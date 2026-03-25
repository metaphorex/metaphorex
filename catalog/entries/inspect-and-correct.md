---
slug: inspect-and-correct
name: "Inspect and Correct"
summary: "At the end of each work session, trace errors to their process causes and change the process, not the person, before the next session."
kind: mental-model
source_frame: food-and-cooking
categories:
  - organizational-behavior
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - coming-to-zero
  - mise-en-place
  - a-la-minute
provenance: culinary-mise-en-place
created: '2026-03-19'
updated: '2026-03-22'
grounding: folk
harness: Claude Code
transfers:
  - '[model] defines a daily practice of reviewing completed work for errors and their downstream consequences, distinguishing between the error itself (the burnt sauce) and the process failure that permitted it (the station was not checked before service)'
  - '[model] requires that the inspection be temporally close to the work -- end of shift, not end of quarter -- because the causal chain between error and consequence is still visible at short timescales but dissolves into noise at long ones'
  - '[model] frames correction as a change to the process rather than punishment of the person, separating the quality signal (this went wrong) from the attribution signal (you did this wrong)'
limits:
  - '[model] assumes errors are detectable at inspection time, but in knowledge work many errors only become visible weeks or months later when their consequences emerge -- the equivalent of a dish that tastes fine on service but was contaminated during prep'
  - '[model] breaks when the inspection overhead exceeds the cost of the errors it catches, which happens in high-throughput low-consequence environments where most errors are self-correcting'
embodied_patterns:
  - iteration
  - matching
  - path
relation_types:
  - transform/refinement
  - cause/propagate
  - select
structure: cycle
abstraction_level: generic
---

## Transfers

In Dan Charnas's *Work Clean* framework (derived from professional
kitchen practice), "Inspect and Correct" is the ninth principle of
mise en place: at the end of each work session, review what happened,
identify errors, trace them to their process causes, and adjust the
process for the next session. In a kitchen, this means examining the
night's tickets -- which orders were sent back, which dishes were
fired late, which stations ran out of prep -- and asking not "who
screwed up?" but "what in our system permitted this error?"

Key cognitive moves:

- **Error tracking as daily practice** -- the model insists that
  inspection is not an occasional audit or an annual review. It
  happens every day, at the end of every service. This frequency
  matters because it keeps the feedback loop short: the chef who
  burnt the sauce remembers the moment it happened, can identify the
  cause (the station was too hot because the burner was not adjusted
  after the previous dish), and can correct it for tomorrow. Weekly
  retrospectives lose this temporal resolution. Quarterly reviews
  lose it entirely.

- **Consequence tracing, not just error counting** -- the model
  distinguishes between an error and its consequences. A burnt sauce
  that was caught and remade is an error with no customer consequence
  but a significant waste consequence. A sauce that was served
  slightly off because the chef was unsure is an error with a
  quality consequence that may or may not generate a complaint. The
  model requires tracing the full chain: error, detection point,
  corrective action taken, customer impact, and waste generated.
  This discipline prevents the common failure of counting only the
  errors that customers notice.

- **Process correction, not personal blame** -- Charnas is explicit
  that inspect-and-correct targets the system, not the individual.
  "The onions were cut inconsistently" leads to "the knife was dull"
  or "the recipe card doesn't specify thickness" rather than "the
  prep cook was careless." This is structurally identical to the
  blameless postmortem in software engineering and to Deming's
  principle that 94% of problems are systemic. The kitchen context
  makes the principle concrete: you can see the dull knife, you can
  read the recipe card, you can measure the onion thickness.

- **The corrective must be testable tomorrow** -- because the
  cycle repeats daily, every correction gets tested within 24
  hours. "We'll sharpen the knives before prep" is tested at
  tomorrow's prep. "We'll add thickness to the recipe card" is
  tested when tomorrow's cook reads it. This rapid feedback
  distinguishes inspect-and-correct from corporate improvement
  processes where corrections are proposed in one quarter and
  evaluated in the next, by which time the context has changed.

## Limits

- **Knowledge work errors have long latency** -- in a kitchen, most
  errors are visible within minutes (the dish goes back, the timing
  is off, the ingredient runs out). In software, architecture
  decisions, hiring choices, and strategic commitments may not reveal
  their errors for months or years. Inspect-and-correct's daily
  cycle assumes that consequences are fast enough to inspect. When
  they are not, the model degenerates into inspecting what is
  measurable (lines of code, tickets closed) rather than what
  matters (design quality, team health).

- **Inspection overhead scales poorly** -- in a kitchen brigade of
  10 people producing 200 covers, the chef de cuisine can plausibly
  review every significant error from the evening. In a software
  organization of 500 engineers shipping thousands of changes per
  day, no individual can inspect the full output. The model must be
  distributed (each team inspects its own work), which introduces
  consistency problems: different teams define "error" differently,
  trace consequences to different depths, and correct with different
  rigor.

- **Not all errors warrant process changes** -- the model's bias is
  toward systematizing every correction. But some errors are
  genuinely one-off: a cook misreads a ticket because they were
  momentarily distracted; a developer introduces a typo that tests
  catch. Creating a process change for every one-off error produces
  bureaucratic accretion -- more checklists, more recipe cards, more
  review steps -- that eventually slows the work more than the
  errors cost. The model needs a threshold for when to systematize
  and when to let go, and it does not provide one.

- **The blameless frame can suppress accountability** -- "inspect the
  system, not the person" is a powerful corrective to blame culture.
  But taken to its extreme, it can make it impossible to address
  genuine individual performance problems. If every error is
  attributed to the system, there is no vocabulary for saying "this
  person is consistently underperforming and needs coaching or
  reassignment." The model's kitchen origins partially mitigate
  this -- a chef who consistently burns the sauce is moved off the
  station -- but the principle as stated does not include this
  escape valve.

## Expressions

- "What went wrong tonight, and what do we change tomorrow?" -- the
  daily inspect-and-correct question in kitchen form
- "Blameless postmortem" -- the software engineering equivalent,
  which shares the model's separation of error analysis from personal
  attribution
- "Fix the process, not the person" -- the core principle stated as
  an injunction
- "Short feedback loops" -- the structural property that makes daily
  inspection valuable, borrowed from control systems theory
- "Debrief" -- the military and aviation term for the same practice,
  emphasizing temporal proximity to the event

## Origin Story

The inspect-and-correct principle as Charnas presents it in *Work
Clean* (2016) draws on two traditions. The first is the professional
kitchen's daily rhythm of service followed by review: the
post-service debrief where the chef examines what went well and what
did not. The second is the quality management tradition from Deming
and the Toyota Production System, where continuous inspection and
correction (kaizen) is a foundational principle.

Charnas's contribution is making the kitchen version concrete and
personal. Rather than abstract process-improvement frameworks, he
describes a specific practice: at the end of each workday, look at
what you actually did, identify the errors and inefficiencies, trace
them to their causes, and make one concrete change for tomorrow.
The daily cadence and the individual scale distinguish it from
organizational retrospectives, which operate on longer cycles and
broader scope.

## References

- Charnas, D. *Work Clean: The Life-Changing Power of Mise-en-Place*
  (2016), Principle 9: "Inspect and Correct"
- Deming, W. E. *Out of the Crisis* (1986) -- the quality management
  tradition that underlies inspect-and-correct
- Ohno, T. *Toyota Production System* (1988) -- kaizen as continuous
  small improvements
- Allspaw, J. and Hammond, P. "10+ Deploys Per Day" (Velocity 2009)
  -- the software engineering equivalent, emphasizing short feedback
  loops and blameless postmortems
