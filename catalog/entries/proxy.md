---
slug: proxy
name: Proxy
summary: "A stand-in that acts on another's behalf. The proxy's power comes from being mistaken for the real thing -- and its danger comes from the same source."
kind: pattern
source_frame: representation
applies_to:
  - software-engineering
  - organizational-behavior
  - epistemology
categories:
  - software-engineering
  - systems-thinking
author: agent:metaphorex-miner
harness: Claude Code
contributors: []
related:
  - facade
  - goodharts-law
  - the-map-is-not-the-territory
  - treat-the-patient-not-the-test
created: '2026-03-26'
updated: '2026-03-26'
grounding: established
transfers:
  - '[source] a legal proxy is authorized to act on behalf of another party, importing the principle that the stand-in must be treated as equivalent to the principal for all relevant purposes while remaining structurally distinct'
  - '[source] the proxy relationship requires that third parties cannot distinguish (or need not distinguish) the proxy from the principal, mapping the software pattern where a proxy object implements the same interface as the real object'
  - '[source] proxy authority is always bounded and revocable -- a legal proxy acts within a defined scope and can be dismissed -- importing the design principle that delegation is not abdication'
limits:
  - '[source] breaks because legal proxies exercise judgment in novel situations, while software proxies typically follow fixed rules and cannot adapt their behavior to unforeseen conditions without being reprogrammed'
  - '[source] misleads by implying equivalence between proxy and principal when the proxy necessarily introduces latency, indirection, and potential failure modes that the original does not have'
  - '[source] obscures the identity problem: in legal contexts the proxy is always known to be a proxy, while in software the entire point is often that clients cannot tell whether they are talking to a proxy or the real service'
embodied_patterns:
  - surface-depth
  - link
  - matching
relation_types:
  - translate
  - cause/constrain
  - enable
structure: boundary
abstraction_level: generic
---

## Transfers

A proxy is something that stands in for something else. The word comes from
the Latin *procuratio* -- managing on behalf of another. In law, a proxy
votes for an absent shareholder. In statistics, a proxy variable substitutes
for one that cannot be directly measured. In software, a proxy object
implements the same interface as the real object and intercepts calls to it.

The core structure across all these domains is the same: the proxy is treated
as equivalent to the thing it represents, for some defined set of purposes,
while remaining structurally distinct from it.

Key structural parallels:

- **Indistinguishability is the design goal** -- a proxy works precisely
  because third parties cannot tell (or need not care) that they are
  interacting with a stand-in rather than the real thing. The legal proxy
  votes as if they were the shareholder. The software proxy implements the
  same interface as the real service. The proxy variable correlates strongly
  enough with the target variable that statistical conclusions hold. When
  the proxy becomes distinguishable from the principal, it stops functioning
  as a proxy and becomes merely an intermediary.

- **Interception enables additional behavior** -- the proxy sits between the
  caller and the real thing, and that position lets it add capabilities: access
  control (protection proxy), caching (caching proxy), lazy initialization
  (virtual proxy), network transparency (remote proxy). The proxy pattern
  recognizes that interception is a feature, not a bug -- the intermediary
  position is the whole point.

- **Bounded authority** -- a legal proxy operates within a defined scope. A
  shareholder proxy can vote but cannot sell the shares. This maps to software
  proxies that expose the full interface but enforce policy on specific
  operations. The proxy's authority is always a subset of the principal's,
  even when the interface appears identical.

## Limits

- **Proxy metrics drift from what they measure** -- this is Goodhart's Law
  applied to the proxy concept. When a proxy variable (test scores, code
  coverage, GDP) becomes a target, people optimize the proxy rather than the
  underlying reality. The proxy diverges from the principal precisely because
  it was trusted as equivalent. The concept of "proxy" provides no built-in
  warning about this drift; it assumes the proxy-principal relationship is
  stable.

- **Software proxies introduce failure modes the principal does not have** --
  a network proxy can timeout, a caching proxy can serve stale data, a
  protection proxy can deny legitimate requests. The metaphor of "standing in"
  implies equivalence, but the proxy is always a degraded copy in some
  dimension. The degradation is the price of the additional behavior the
  proxy provides, but the metaphor does not make this tradeoff visible.

- **The identity confusion is not a bug, it is the design** -- in legal
  contexts, everyone knows the proxy is a proxy. In software, the entire
  point of the proxy pattern is that clients should not know. This deliberate
  opacity is powerful (it enables transparent caching, load balancing,
  security) but it creates debugging nightmares when the proxy's behavior
  diverges from the principal's. The system was designed to hide the
  distinction, so discovering the proxy is the source of a problem requires
  working against the architecture.

- **Proxies accumulate** -- one proxy is clean indirection. But systems
  evolve, and proxies attract more proxies: a caching proxy in front of a
  load-balancing proxy in front of a security proxy in front of the actual
  service. Each layer was justified individually, but the aggregate chain
  introduces latency, complexity, and failure modes that no single layer
  anticipated.

## Expressions

- "Proxy server" -- a server that intercepts requests between client and
  origin, the most common software usage
- "Proxy metric" -- a measurable quantity used as a stand-in for something
  that cannot be directly measured, carrying the inherent risk of
  metric-target divergence
- "Proxy war" -- a conflict where the actual combatants fight through
  substitutes, extending the metaphor to geopolitics
- "By proxy" -- acting through an intermediary rather than directly, the
  general English usage
- "Reverse proxy" -- a proxy that sits in front of servers rather than
  clients, inverting the original direction but preserving the
  interception structure

## Origin Story

The proxy concept in software was codified by the Gang of Four in *Design
Patterns* (1994), but the underlying idea is far older. Proxy voting dates
to medieval parliamentary practice. Proxy variables entered statistics in
the early 20th century. The software pattern recognized that the same
structural relationship -- a stand-in that is treated as equivalent to the
thing it represents -- appears across domains, and that the intermediary
position enables a family of useful behaviors (access control, caching,
remote access, lazy loading) that share a common architectural form.

## References

- Gamma, E. et al. *Design Patterns: Elements of Reusable Object-Oriented
  Software* (1994), pp. 207-217
- Goodhart, C.A.E. "Problems of Monetary Management: The U.K. Experience"
  (1975) -- the original observation about proxy metrics
- Fowler, M. *Patterns of Enterprise Application Architecture* (2002) --
  discusses remote proxy in the context of distributed systems
