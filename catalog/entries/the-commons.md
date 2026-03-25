---
applies_to:
- shared-resources
author: fshot
categories:
- organizational-behavior
- systems-thinking
contributors: []
created: '2026-03-07'
kind: archetype
name: The Commons
summary: "Shared resource where individual rational use produces collective ruin. Hardin says tragedy is inevitable; Ostrom shows governance works."
related:
- survival-of-the-fittest
slug: the-commons
source_frame: animal-husbandry
updated: '2026-03-10'
transfers:
  - "[source] each herder's individually rational decision to add one more animal produces collectively irrational overgrazing"
  - "[source] the resource is rivalrous -- one herder's use directly diminishes what remains for others"
  - "[source] governance requires monitoring, graduated sanctions, and collective choice arrangements to prevent degradation"
limits:
  - "[source] breaks because grazing depletes the pasture, but information commons are non-rivalrous -- reading an article does not degrade it"
  - "[source] misleads because Ostrom's governance principles require members who know each other and can impose social sanctions, which fails at global scale with anonymous participants"
  - "[source] obscures that framing something as a commons preselects collective governance as the solution before analysis begins"
embodied_patterns:
  - container
  - balance
  - flow
relation_types:
  - compete
  - accumulate
structure: competition
abstraction_level: generic
---

## Transfers

A framework for shared resources and the tension between individual
incentive and collective benefit. The source mapping is vivid: a shared
grazing pasture where each herder benefits from adding one more cow, but
if every herder does this, the pasture is destroyed. Individual
rationality produces collective ruin. The pattern recurs everywhere:
open source projects, shared codebases, public APIs, fisheries, the
atmosphere, and this project. Any resource that is non-excludable (hard
to fence off) and rivalrous (my use diminishes yours) is a commons.

The archetype has two versions, and which one you carry determines what
you build:

- **Hardin's tragedy** — the commons inevitably degrades. Rational actors
  will always overexploit shared resources. The only solutions are
  privatization or top-down regulation. This framing dominated policy
  for decades.
- **Ostrom's governance** — communities routinely govern commons
  successfully, and have for centuries. Her eight design principles
  (clear boundaries, graduated sanctions, collective choice
  arrangements, monitoring, conflict resolution mechanisms) describe how
  real communities manage shared resources without privatizing them or
  handing control to the state. Ostrom won the Nobel Prize in Economics
  for this work. Hardin's essay is still cited more often.

## Limits

- **Tragedy assumes selfishness** — Hardin's version assumes purely
  self-interested rational actors. Ostrom showed this is empirically
  wrong: communities from Swiss alpine meadows to Japanese fishing
  villages to Maine lobster fisheries govern commons successfully. The
  "tragedy" framing is a thought experiment dressed as inevitability,
  biasing toward privatization.
- **Information isn't grass** — the grazing-land metaphor implies that
  use depletes the resource. This maps well to fisheries and forests but
  poorly to information commons. Reading a Wikipedia article doesn't
  degrade it. Software doesn't wear out when copied. The commons
  metaphor, applied to information, imports scarcity thinking where
  abundance applies.
- **Scale breaks governance** — Ostrom's principles work in communities
  where members know each other, can monitor behavior, and can impose
  social sanctions. A global open source project with anonymous
  contributors lacks these properties. The commons metaphor suggests
  that what works for a village fishery should work for npm, which is
  not obviously true.
- **Naming is a political act** — framing something as "a commons"
  implies shared ownership and collective governance. Calling the same
  resource "intellectual property" implies private ownership and market
  governance. The metaphor selects the solution before the analysis
  begins.

## Expressions

- "Tragedy of the commons" — Hardin's framing, now so pervasive that many
  people think it's a natural law rather than a contested thought experiment
- "Free rider problem" — the specific failure mode where someone benefits from
  the commons without contributing to its maintenance
- "Open source sustainability" — the contemporary version of the question:
  who maintains the pasture when everyone grazes for free?
- "Commons-based peer production" — Benkler's term for Wikipedia, Linux, and
  similar projects that produce value through collective voluntary effort
- "Public good" — the economics term for a non-excludable, non-rivalrous
  resource, which is what information commons actually are (not grazing land)

## Origin Story

The source domain is literal: common grazing land in medieval England,
where villagers had rights to graze livestock on shared pastures. These
were real legal arrangements governed by complex local rules, not the
unregulated free-for-all Hardin imagined.

Hardin's "The Tragedy of the Commons" (1968), published in *Science*,
turned this into a paradigm for resource depletion. His argument was
elegant, persuasive, and largely wrong about how actual commons worked.
He described a hypothetical open-access resource with no governance,
which is not what historical commons were.

Elinor Ostrom's *Governing the Commons* (1990) was the empirical corrective.
She studied real commons worldwide and identified eight design principles:
clearly defined boundaries, proportional equivalence between benefits and
costs, collective choice arrangements, monitoring, graduated sanctions,
fast and fair conflict resolution, local autonomy, and (for larger
systems) nested governance. She won the 2009 Nobel Memorial Prize in
Economic Sciences, the first woman to do so.

The pattern now structures debates about open source (who maintains the
commons?), platform economics (is Twitter/X a commons or a product?), AI
training data (who owns the commons of the internet?), and climate (the
atmosphere as global commons). In every case, whether you carry Hardin's
version or Ostrom's version determines whether you reach for privatization
or collective governance.

## References

- Hardin, G. "The Tragedy of the Commons," *Science* 162 (1968): 1243-1248
- Ostrom, E. *Governing the Commons* (1990) — the Nobel-winning rebuttal
- Benkler, Y. *The Wealth of Networks* (2006) — applies commons thinking to
  information production
- Hess, C. & Ostrom, E. *Understanding Knowledge as a Commons* (2007) —
  explicitly extends the framework to information and digital resources
