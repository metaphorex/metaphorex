---
slug: compute-is-a-resource
name: "Compute Is a Resource"
kind: conceptual-metaphor
source_frame: economics
target_frame: artificial-intelligence
categories:
  - ai-discourse
  - systems-thinking
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - data-is-fuel
  - time-is-a-resource
  - labor-is-a-resource
---

## What It Brings

GPU hours, FLOPS, TPU pods -- computational capacity is treated as a
scarce natural resource to be extracted, stockpiled, traded, and allocated.
The metaphor maps the entire apparatus of resource economics onto
chip manufacturing and datacenter operations: nations compete for compute
the way they once competed for oil, companies hoard GPU capacity the way
they stockpile strategic reserves, and "compute governance" is debated
in the same breath as energy policy.

Key structural parallels:

- **Scarcity and allocation** -- compute is finite at any given moment.
  Training a large model requires specific quantities of GPU time, and
  that capacity cannot be in two places at once. The resource frame makes
  this constraint legible through economic vocabulary: budgets, allocation,
  quotas, rationing. Organizations "spend" compute on training runs and
  must decide how to "invest" their limited supply.
- **Extraction and supply chains** -- GPUs are manufactured from rare
  earth minerals through complex global supply chains. The resource
  metaphor maps cleanly onto this reality: TSMC fabs are the mines, chip
  designs are geological surveys, and export controls are resource
  embargoes. The "GPU arms race" directly imports geopolitical resource
  competition.
- **Stockpiling and reserves** -- companies pre-purchase GPU capacity,
  build massive datacenters, and accumulate compute reserves. The resource
  frame makes this legible as strategic stockpiling -- the computational
  equivalent of filling the Strategic Petroleum Reserve. The term "compute
  overhang" (accumulated but unused computational capacity) borrows
  directly from resource economics.
- **Markets and pricing** -- cloud GPU instances are priced per hour,
  traded on spot markets, and subject to supply-demand dynamics. The
  resource metaphor makes compute fungible and tradeable, enabling market
  mechanisms (auctions, futures, reservations) that treat computation as
  a commodity.
- **Scaling as resource consumption** -- larger models require more
  compute. The resource frame makes scaling decisions legible as resource
  allocation decisions: "We need 10x more compute for the next generation"
  sounds like an energy requirement, not a mathematical observation.

## Where It Breaks

- **Compute is manufactured, not extracted** -- oil exists in finite
  deposits formed over geological time. Compute is manufactured by humans
  and can be increased by building more fabs and datacenters. The resource
  metaphor imports a scarcity logic that applies to the short term (you
  cannot build a fab overnight) but not the long term (humanity can always
  build more chips). Treating compute as a fixed resource overstates the
  constraint and understates human agency in expanding supply.
- **Compute does not deplete** -- a GPU used for one training run is not
  consumed. It can immediately be used for the next. The resource metaphor
  imports depletion logic from oil and minerals, but compute is a flow
  resource (like electricity or labor), not a stock resource (like ore).
  The distinction matters: flow resources can be time-shared, parallelized,
  and recycled in ways that stock resources cannot.
- **The arms race frame escalates conflict** -- calling the competition for
  AI compute a "GPU arms race" imports Cold War dynamics onto what is
  fundamentally an industrial production challenge. Arms races involve
  mutually assured destruction, existential threat, and zero-sum logic.
  Compute competition is positive-sum in the long run: more global compute
  capacity benefits everyone. The arms race metaphor forecloses cooperative
  framings and escalates geopolitical tension.
- **Efficiency improvements change the equation** -- the resource frame
  emphasizes quantity (more GPUs, more FLOPS, more hours). But
  algorithmic efficiency improvements can reduce compute requirements by
  orders of magnitude. The resource metaphor systematically undervalues
  efficiency and overvalues brute accumulation, because the source domain
  (resource extraction) has no analogue for "making oil more efficient."
- **Fungibility is overstated** -- the resource metaphor treats all
  compute as interchangeable. But a GPU hour on an H100 is not equivalent
  to a GPU hour on an A100; TPUs and GPUs have different capabilities;
  and inference compute has different requirements than training compute.
  The commodity framing papers over qualitative differences that matter
  enormously in practice.

## Expressions

- "GPU arms race" -- geopolitical competition for compute framed as
  military escalation
- "Compute budget" -- allocating computational resources using financial
  planning vocabulary
- "We burned through our compute" -- consumption/depletion language for
  training runs
- "Compute overhang" -- stockpiled but unused capacity, from resource
  economics
- "Scaling laws" -- empirical regularities framed as natural laws
  governing compute requirements
- "FLOPS as currency" -- computational operations as the unit of exchange
  in the compute economy
- "Compute-optimal training" -- Chinchilla scaling, framed as optimal
  resource allocation
- "Democratizing compute" -- distributing a scarce resource more equitably

## Origin Story

The resource framing for computation predates AI. Operating systems have
always "allocated resources" (CPU time, memory, disk space), and cloud
computing introduced per-hour pricing that made compute explicitly
economic. But the framing intensified dramatically with large language
models. When GPT-3's training was estimated to cost millions of dollars
in compute, and when training runs began requiring thousands of GPUs for
months, the resource metaphor became the dominant lens for understanding
AI capability.

The geopolitical dimension emerged around 2022-2023 when US export
controls restricted advanced chip sales to China. Suddenly, compute was
not just an economic resource but a strategic one, and the full vocabulary
of resource geopolitics (embargoes, stockpiles, supply chain security)
became applicable. The "compute governance" discourse, promoted by think
tanks like GovAI and Epoch, explicitly treats computational capacity as
a governable resource analogous to nuclear material or spectrum allocation.

The metaphor shapes billions in real investment. When Sam Altman sought
$7 trillion for chip manufacturing in 2024, the resource frame made the
number legible: this was infrastructure investment in a strategic resource,
not a speculative bet on software.

## References

- Epoch AI, "Compute Trends Across Three Eras of Machine Learning"
  (2022) -- quantifies the exponential growth in training compute
- Sastry, G. et al. "Computing Power and the Governance of Artificial
  Intelligence" (2024) -- the foundational compute governance paper
- Hoffmann, J. et al. "Training Compute-Optimal Large Language Models"
  (Chinchilla, 2022) -- established compute-optimal scaling
- Maas, M. "AI is Like... A Literature Review of AI Metaphors" (2023)
