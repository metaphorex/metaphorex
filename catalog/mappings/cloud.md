---
author: agent:metaphorex-miner
categories:
- linguistics
- software-engineering
- systems-thinking
contributors: []
created: '2026-03-15'
harness: Claude Code
kind: dead-metaphor
name: Cloud
related:
- firewall
slug: cloud
source_frame: natural-phenomena
target_frame: computing
updated: '2026-03-15'
---

## What It Brings

A cloud is overhead, amorphous, and pervasive. You cannot see its internal
structure from below, and you do not need to. Network engineers drew clouds
on diagrams long before "cloud computing" became a product category, and
the original drawing convention encoded a precise architectural statement:
this part of the network is someone else's problem.

- **Opacity from below** -- you look up at a cloud and see a uniform white
  surface. You do not see the turbulent convection cells, the ice crystals
  at different altitudes, or the precise geography of the water droplets.
  Cloud computing imports this opacity as a feature: the consumer sees a
  uniform API surface and does not see the load balancers, the data center
  topology, or the specific machines running their workload. Abstraction
  is rendered as atmospheric distance.
- **Ubiquity** -- clouds are everywhere overhead. Cloud services are
  everywhere on the network. "The cloud" suggests a resource that is not
  in any specific place but is accessible from any place, the way rain can
  fall on any point beneath a cloud layer. This maps cleanly to the
  geographic distribution of cloud data centers and the promise of
  location-independent access.
- **Elasticity** -- clouds grow and shrink, merge and dissipate. Cloud
  computing's elasticity (scale up, scale down, pay for what you use) maps
  onto this atmospheric behavior. The metaphor makes auto-scaling feel
  natural rather than engineered.
- **Someone else's problem** -- the original network diagram cloud meant
  "traffic enters here, emerges there, and what happens in between is
  not your concern." This is the deepest structural contribution of the
  metaphor: it gave engineers permission to stop thinking about
  infrastructure they did not own.

## Where It Breaks

- **Clouds have no owners; data centers do** -- the most consequential
  failure of the metaphor. A real cloud belongs to nobody. AWS belongs to
  Amazon. When you put your data "in the cloud," you are putting it on
  specific machines in specific buildings owned by a specific corporation
  subject to specific jurisdictions. The metaphor's atmospheric
  vagueness actively obscures questions of ownership, sovereignty, and
  vendor lock-in that are critical to any serious infrastructure decision.
- **Clouds are ephemeral; data centers are not** -- a cloud dissipates.
  A data center is a concrete building with a 20-year lease, diesel
  generators, and water cooling systems. The environmental footprint of
  "the cloud" is massive and material: electricity, water, rare earth
  minerals, electronic waste. The metaphor's ethereal connotation makes
  it psychologically easier to ignore the physical reality. "Storing
  files in the cloud" sounds clean; "storing files in a warehouse in
  Virginia" does not.
- **Clouds are unreliable; the metaphor promises reliability** -- real
  clouds bring storms, block sunlight unpredictably, and dump rain on
  picnics. Yet "the cloud" in computing connotes reliable, always-on
  infrastructure. The metaphor has been selectively mapped: the ubiquity
  and softness of clouds are imported, but the unreliability and
  destructiveness are quietly dropped. When AWS us-east-1 goes down and
  takes half the internet with it, the atmospheric metaphor provides no
  framework for understanding the failure.
- **The plural matters** -- there is no single cloud in nature or in
  computing. Multi-cloud strategies, cloud-to-cloud data transfer, and
  cloud egress costs all reveal that "the cloud" is actually many clouds
  operated by competing providers with incompatible APIs. The metaphor's
  singular form ("the cloud") hides the fragmented, competitive reality.

## Expressions

- "In the cloud" -- stored or running on remote infrastructure, the
  canonical expression of the metaphor
- "Cloud-native" -- designed to exploit cloud properties from the ground
  up, as though the cloud were an environment one could be native to
- "Move to the cloud" -- migrate infrastructure from on-premises to
  remote hosting, a spatial metaphor (upward, outward) for what is
  actually a vendor relationship
- "Cloud burst" -- a spike in demand exceeding cloud capacity, borrowing
  the meteorological term for sudden heavy rain
- "Above the cloud line" -- management or strategy layers that interact
  with cloud services only through abstractions, extending the
  atmospheric altitude metaphor
- "There is no cloud, just other people's computers" -- the counter-slogan
  that attempts to resurrect the dead metaphor by exposing what it hides

## Origin Story

The cloud symbol in network diagrams dates to the early 1970s. ARPANET
documentation used cloud shapes to represent networks whose internal
topology was irrelevant to the diagram's purpose. The convention was
practical: if you are diagramming your local network's connection to a
wide-area network, the WAN's internal routing is not your problem. You
draw a cloud, label it, and move on.

The term "cloud computing" as a product category emerged in the mid-2000s.
Google's Eric Schmidt used it at a Search Engine Strategies conference in
2006, and Amazon Web Services launched its Elastic Compute Cloud (EC2) the
same year. The naming was deliberate: "Elastic Compute Cloud" fused the
atmospheric metaphor with the promise of on-demand scalability.

The metaphor succeeded commercially because it solved a marketing problem.
"Remote server rental" sounds like a commodity. "The cloud" sounds like a
paradigm shift. The ethereal, omnipresent connotation helped sell what was
fundamentally a real estate business (renting rack space and compute
cycles) as something transformative and inevitable. By 2010, "cloud" had
completed its transition from diagram convention to dead metaphor: nobody
drawing an architecture diagram thinks about weather when they draw a
cloud shape, and nobody saying "deploy to the cloud" pictures cumulus
formations.

## References

- Regalado, A. "Who Coined 'Cloud Computing'?" MIT Technology Review
  (2011) -- traces the term's origin and early commercial usage
- Etymonline, "cloud" -- Old English *clud*, originally meaning "rock,
  hill" (clouds as sky-rocks), itself a dead metaphor
- Hu, M. "The Big Data of Cloud Computing," Legislation and Policy Brief
  (2015) -- analysis of how the cloud metaphor obscures data sovereignty
- Vaidhyanathan, S. *Anti-Social Media* (2018) -- discusses how cloud
  metaphors depoliticize infrastructure decisions
