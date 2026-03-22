---
slug: fallacies-of-distributed-computing
name: Fallacies of Distributed Computing
kind: mental-model
source_frame: network-communication
categories:
  - software-engineering
  - systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
  - hyrums-law
  - law-of-leaky-abstractions
created: '2026-03-21'
updated: '2026-03-21'
grounding: established
transfers:
  - '[model] Each fallacy names a specific locality assumption that engineers unconsciously import from single-machine programming: the network will behave like a function call, the remote system will behave like a local object, the infrastructure will behave like a constant'
  - '[model] The eight fallacies form a progressive disillusionment sequence -- engineers typically discover them in order of increasing subtlety, from "the network is reliable" (week one) to "the network is homogeneous" (year three)'
  - '[model] The structural insight is that distribution does not add complexity linearly but categorically: each fallacy represents a qualitative difference between local and distributed reasoning, not a quantitative one'
limits:
  - '[model] The fallacies were codified in the early 1990s for enterprise networking; several (zero transport cost, infinite bandwidth) have become less practically urgent as infrastructure improved, risking false equivalence between 1994-era and modern network conditions'
  - '[model] Presents the fallacies as a flat list when they actually have dependency structure -- "the network is reliable" is foundational, while "there is one administrator" is organizational rather than technical, and mixing the two levels obscures what kind of reasoning each one corrects'
embodied_patterns:
  - boundary
  - link
  - surface-depth
relation_types:
  - prevent
  - translate
  - decompose
structure: network
abstraction_level: specific
---

## Transfers

In 1994, Peter Deutsch (building on work by Bill Joy and others at Sun
Microsystems) codified eight assumptions that programmers new to
distributed systems invariably make -- and that invariably prove false:

1. The network is reliable
2. Latency is zero
3. Bandwidth is infinite
4. The network is secure
5. Topology does not change
6. There is one administrator
7. Transport cost is zero
8. The network is homogeneous

The list's enduring value is not in the individual items (each is obvious
once stated) but in its structural claim: local reasoning fails
categorically, not incrementally, when applied to distributed systems.

Key structural parallels:

- **The locality illusion** -- when a programmer writes a function call,
  the call either succeeds or throws an exception. The function does not
  succeed partially, arrive out of order, or take 300 milliseconds
  sometimes and 3 seconds other times. Each fallacy names a specific
  property of local computation (deterministic completion, negligible
  latency, uniform environment) that programmers unconsciously import
  into their mental model of remote calls. The fallacies are not about
  networks being bad; they are about the mismatch between two
  fundamentally different computational models.
- **Progressive discovery** -- the fallacies are ordered roughly by how
  quickly engineers encounter them. "The network is reliable" fails on
  the first production deployment. "Latency is zero" fails under load
  testing. "The network is homogeneous" may not fail until the system
  spans cloud providers or regions years later. This ordering creates a
  pedagogical sequence: each fallacy prepares the ground for the next
  by eroding another layer of the locality assumption.
- **Categorical vs. quantitative complexity** -- the deepest structural
  insight is that distribution introduces qualitative differences, not
  just quantitative ones. A local system with twice the load needs
  twice the resources. A distributed system with one additional node
  introduces partial failure modes, consistency challenges, and
  coordination costs that have no local equivalent. The fallacies name
  the boundary between "harder" and "different."

## Limits

- **Historical specificity masquerading as timelessness** -- the
  fallacies were formulated when networks were genuinely unreliable,
  bandwidth genuinely scarce, and security genuinely absent. Modern
  cloud infrastructure has not eliminated these concerns but has
  changed their practical weight dramatically. "Bandwidth is infinite"
  was a serious trap in 1994; in 2024, it is approximately true for
  most application-layer traffic within a cloud region. Citing the
  fallacies without adjusting for infrastructure improvements can
  produce over-engineering as harmful as the naivete the fallacies warn
  against.
- **The list conflates technical and organizational fallacies** --
  fallacies 1-4 and 8 are properties of network physics (latency,
  reliability, bandwidth). Fallacies 5-7 are organizational and
  economic (topology changes because organizations change, there are
  multiple administrators because there are multiple organizations).
  Treating them as a single category obscures the different kinds of
  reasoning required to address each. The technical fallacies demand
  protocol design; the organizational fallacies demand governance
  design.
- **The fallacies do not tell you what to do** -- knowing that "the
  network is unreliable" does not tell you whether to use retries,
  circuit breakers, idempotency tokens, or saga patterns. The
  fallacies are diagnostic (they name the assumptions to question) but
  not prescriptive (they do not name the solutions). Engineers who
  memorize the list without learning the corresponding design patterns
  (timeouts, retries with backoff, eventual consistency) have only
  completed half the work.
- **Micro-service fetishism** -- the fallacies are sometimes invoked to
  argue against distributed architectures entirely ("distribution is
  hard, therefore monolith"). But the fallacies do not argue against
  distribution; they argue against naive distribution. The same
  fallacies apply whether you chose microservices deliberately or
  inherited a distributed system through organizational growth.

## Expressions

- "Fallacy number one: the network is reliable" -- the most frequently
  cited individual fallacy, invoked during post-mortems of outages
  caused by missing retry logic
- "You're assuming the network is free" -- shorthand for fallacy 7
  (zero transport cost), used when architects propose chatty protocols
  or fine-grained RPC calls across service boundaries
- "The eight fallacies" -- the list as a whole, cited as required
  reading for distributed systems engineers
- "Deutsch's fallacies" -- attributed form, distinguishing from the
  broader "fallacies" concept

## Origin Story

The list originated at Sun Microsystems in the late 1980s and early
1990s. Bill Joy and Tom Lyon identified the first four fallacies.
James Gosling contributed the fifth through seventh. Peter Deutsch
consolidated and published the list of seven in 1994. L. Peter
Deutsch (or possibly James Gosling) added the eighth ("the network
is homogeneous") shortly afterward. The fallacies became canonical in
distributed systems education through their inclusion in textbooks,
conference talks, and eventually the hacker-laws repository. They
remain the most widely cited checklist in distributed systems
engineering, appearing in virtually every introductory course on the
subject.

## References

- Deutsch, Peter. "The Eight Fallacies of Distributed Computing"
  (1994) -- the original codification
- Rotem-Gal-Oz, Arnon. "Fallacies of Distributed Computing Explained"
  (2006) -- the most widely read commentary
- Van Steen, Maarten and Andrew S. Tanenbaum. *Distributed Systems*
  (3rd edition, 2017) -- textbook treatment
- Kerr, Dave. "Hacker Laws" -- https://github.com/dwmkerr/hacker-laws
