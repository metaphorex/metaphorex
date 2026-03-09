---
slug: the-commons
name: "The Commons"
kind: archetype
source_frame: animal-husbandry
target_frame: shared-resources
categories:
  - organizational-behavior
  - systems-thinking
author: fshot
contributors: []
related:
  - survival-of-the-fittest
---

## What It Brings

A framework for shared resources and the tension between individual
incentive and collective benefit. The source mapping is vivid: a shared
grazing pasture where each herder benefits from adding one more cow, but
if every herder does this, the pasture is destroyed. Individual
rationality produces collective ruin.

The pattern recurs everywhere: open source projects, shared codebases,
public APIs, knowledge bases, Wikipedia, fisheries, the atmosphere, and
this project. Any resource that is non-excludable (hard to fence off)
and rivalrous (my use diminishes yours) is a commons.

But the archetype has two versions, and which one you carry determines what
you build:

**Hardin's version** (1968): the commons inevitably degrades. Rational actors
will always overexploit shared resources. The only solutions are privatization
or top-down regulation. This framing dominated policy for decades.

**Ostrom's version** (1990): communities routinely govern commons
successfully, and have for centuries. Her eight design principles (clear
boundaries, graduated sanctions, collective choice arrangements,
monitoring, conflict resolution mechanisms) describe how real communities
manage shared resources without privatizing them or handing control to
the state.

Ostrom won the Nobel Prize in Economics for this work. Hardin's essay is still
cited more often.

## Where It Breaks

Hardin's version assumes purely self-interested rational actors. Ostrom
showed this is empirically wrong. Communities routinely govern commons
successfully, from Swiss alpine meadows to Japanese fishing villages to
Maine lobster fisheries. The "tragedy" framing is a misleading metaphor
that biases toward privatization: a thought experiment dressed as
inevitability.

The grazing-land metaphor also implies that use depletes the resource.
This maps well to fisheries and forests but poorly to information commons.
Reading a Wikipedia article doesn't degrade it for you. Software doesn't
wear out when copied. The commons metaphor, applied to information,
imports scarcity thinking where abundance applies.
Open source is not a grazing pasture; code is not grass.

The archetype also struggles with *scale*. Ostrom's principles work in
communities where members know each other, can monitor behavior, and can
impose social sanctions. A global open source project with anonymous
contributors lacks these properties. The commons metaphor suggests that
what works for a village fishery should work for npm, which is not
obviously true.

Framing something as "a commons" is itself a political act. It implies
shared ownership and collective governance. Calling the same resource
"intellectual property" implies private ownership and market governance.
The metaphor selects the solution before the analysis begins.

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
