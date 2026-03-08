---
slug: the-commons
name: "The Commons"
kind: archetype
source_frame: animal-husbandry
target_frame: shared-resources
categories:
  - organizational-behavior
  - systems-thinking
author: metaphorex
contributors: []
related:
  - survival-of-the-fittest
  - the-trickster
---

## What It Brings

A framework for thinking about shared resources and the tension between
individual incentive and collective benefit. The source mapping is vivid:
a shared grazing pasture where each herder benefits from adding one more
cow, but if every herder does this, the pasture is destroyed. Individual
rationality produces collective ruin.

This is an archetype because the pattern recurs everywhere: open source
projects, shared codebases, public APIs, knowledge bases, Wikipedia, fisheries,
the atmosphere, and — yes — this project. Any resource that is non-excludable
(hard to fence off) and rivalrous (my use diminishes yours) is a commons.

But the archetype has two versions, and which one you carry determines what
you build:

**Hardin's version** (1968): the commons inevitably degrades. Rational actors
will always overexploit shared resources. The only solutions are privatization
or top-down regulation. This framing dominated policy for decades.

**Ostrom's version** (1990): communities routinely govern commons successfully,
and have for centuries. Her eight design principles — clear boundaries,
graduated sanctions, collective choice arrangements, monitoring, conflict
resolution mechanisms — describe how real communities actually manage shared
resources without either privatizing them or handing control to the state.

Ostrom won the Nobel Prize in Economics for this work. Hardin's essay is still
cited more often.

## Where It Breaks

Hardin's version assumes humans are purely self-interested rational actors.
Ostrom showed this is empirically wrong — communities ROUTINELY govern commons
successfully, from Swiss alpine meadows to Japanese fishing villages to Maine
lobster fisheries. The "tragedy" framing is itself a misleading metaphor that
biases toward privatization. It's a thought experiment dressed up as an
inevitability.

The grazing-land metaphor also implies that the resource is *depletable* — that
use consumes it. This maps well to fisheries and forests but poorly to
information commons. My reading of a Wikipedia article doesn't degrade it for
you. Software doesn't wear out when copied. The commons metaphor, applied to
information, can import scarcity thinking where abundance actually applies.
Open source is not a grazing pasture; code is not grass.

The archetype also struggles with *scale*. Ostrom's principles work because
they describe communities where members know each other, can monitor behavior,
and can impose social sanctions. A global open source project with anonymous
contributors doesn't have these properties. The commons metaphor suggests that
what works for a village fishery should work for npm, and this is not obviously
true.

Finally: framing something as "a commons" is itself a political act. It
implies shared ownership and collective governance. Calling the same resource
"intellectual property" implies private ownership and market governance. The
metaphor you choose selects the solution before the analysis begins.

## Expressions

- "Tragedy of the commons" — Hardin's framing, now so pervasive that many
  people think it's a natural law rather than a contested thought experiment
- "Free rider problem" — the specific failure mode where someone benefits from
  the commons without contributing to its maintenance
- "Open source sustainability" — the contemporary version of the question:
  who maintains the pasture when everyone grazes for free?
- "Commons-based peer production" — Benkler's term for Wikipedia, Linux, and
  similar projects that produce value through collective voluntary effort
- "Shared nothing architecture" — the anti-commons, a system design where
  components share no state, explicitly rejecting the commons pattern
- "Public good" — the economics term for a non-excludable, non-rivalrous
  resource, which is what information commons actually are (not grazing land)

## Origin Story

The source domain is literal: common grazing land in medieval England, where
multiple villagers had rights to graze livestock on shared pastures. These
were real legal arrangements governed by complex local rules — not the
unregulated free-for-all that Hardin imagined.

Hardin's "The Tragedy of the Commons" (1968), published in *Science*, turned
this into a paradigm for resource depletion. His argument was elegant,
persuasive, and largely wrong about how actual commons worked. He was
describing a hypothetical open-access resource with no governance, which is
not what historical commons were.

Elinor Ostrom's *Governing the Commons* (1990) was the empirical corrective.
She studied real commons around the world and identified eight design
principles that made them work: clearly defined boundaries, proportional
equivalence between benefits and costs, collective choice arrangements,
monitoring, graduated sanctions, fast and fair conflict resolution, local
autonomy, and (for larger systems) nested governance. She won the 2009 Nobel
Memorial Prize in Economic Sciences for this work — the first woman to do so.

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
