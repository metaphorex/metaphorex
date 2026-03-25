---
slug: conways-law
name: Conway's Law
summary: "Your system architecture will mirror your organization's communication structure, whether you plan it that way or not."
kind: mental-model
categories:
  - software-engineering
  - organizational-behavior
  - systems-thinking
author: agent:metaphorex-miner
harness: Claude Code
contributors: []
related:
  - integrate-rather-than-segregate
  - bus-factor
created: '2026-03-21'
updated: '2026-03-21'
grounding: established
transfers:
  - '[law] predicts that the architecture of any system designed by an organization will be isomorphic to the communication structure of that organization, because the interfaces between components must be negotiated by the people building them, and people negotiate most easily along existing communication channels'
  - '[law] explains why a compiler built by four teams will have four passes regardless of the optimal design, because each team produces a component and the interfaces between components reflect team boundaries rather than technical requirements'
  - '[law] identifies that organizational restructuring is an architectural decision in disguise -- changing who talks to whom changes what the system looks like, even if no explicit technical mandate accompanies the reorg'
limits:
  - '[law] overpredicts isomorphism in organizations with strong architecture functions that deliberately resist the gravitational pull of org structure -- a sufficiently empowered architect or platform team can impose interfaces that cut across team boundaries, though this requires sustained political will'
  - '[law] misleads by implying that org structure determines architecture unidirectionally, when the relationship is bidirectional -- existing system architecture also constrains feasible organizational structures (the "reverse Conway maneuver" exploits this), creating a chicken-and-egg dynamic the law does not resolve'
embodied_patterns:
  - matching
  - link
  - boundary
relation_types:
  - cause/constrain
  - coordinate
  - cause/couple
structure: network
abstraction_level: generic
---

## Transfers

"Organizations which design systems are constrained to produce designs
which are copies of the communication structures of these organizations."
Melvin Conway stated this in 1967, and it has been empirically validated
in studies of software systems, hardware architectures, and product
designs across industries.

- **Communication channels become interfaces** -- the core structural
  insight. When two teams build components that must interact, the
  interface between those components is negotiated through the
  communication channel between the teams. If Team A and Team B talk
  weekly in a formal meeting, their interface will be formal and
  well-documented. If they sit next to each other and talk constantly,
  their interface will be informal and implicit. If they never talk,
  their components will not integrate. The system's architecture is a
  fossil record of the organization's communication patterns during
  the design period.

- **The four-team compiler** -- Conway's original example. A compiler
  produced by four groups will be a four-pass compiler, regardless of
  whether a four-pass design is optimal. Each group produces a pass,
  and the interfaces between passes map to the negotiation boundaries
  between groups. This is not laziness or incompetence -- it is a
  structural constraint. The cognitive load of coordinating across
  group boundaries is real, and teams minimize it by minimizing
  cross-boundary interfaces.

- **The inverse Conway maneuver** -- once you understand the law, you
  can use it intentionally. If you want a microservices architecture,
  organize into small, autonomous teams. If you want a monolithic
  architecture, organize into a single large team. ThoughtWorks and
  others have formalized this as a deliberate strategy: design the org
  chart to match the desired system architecture, and the architecture
  will follow. This is Conway's law weaponized -- using organizational
  design as an architectural tool.

- **Invisible organizational debt** -- Conway's law explains why
  rewrites and migrations often fail. The new system is designed by the
  same organization that built the old system, so it inherits the same
  communication-structure constraints. Teams attempting to replace a
  monolith with microservices without reorganizing will produce a
  "distributed monolith" -- microservices in name but coupled in
  practice, because the same cross-team coordination patterns persist.
  The architecture changes, but the forces shaping it do not.

## Limits

- **Strong architects can resist it** -- Conway's law describes a
  gravitational pull, not an absolute constraint. Organizations with
  empowered architecture roles, shared platform teams, or strong
  technical leadership can impose interface designs that cut across
  team boundaries. The law predicts the default outcome when no
  deliberate architectural force is applied. In practice, the question
  is how much organizational energy is required to maintain an
  architecture that contradicts the org chart, and whether that energy
  is sustainable over time. Most organizations tire and drift back
  toward Conway alignment.

- **Bidirectionality** -- the law as stated implies one-way causation:
  org structure determines system architecture. But the relationship
  is bidirectional. Existing system architecture constrains feasible
  organizational structures -- you cannot assign a team to a tightly
  coupled subsystem without also coupling that team to every other team
  whose subsystem is coupled to theirs. The "reverse Conway maneuver"
  exploits this, but the law itself does not account for the feedback
  loop. In practice, org and architecture co-evolve, each constraining
  the other's degrees of freedom.

- **Applies to design, not all systems** -- Conway's law applies to
  *designed* systems, where human communication is part of the
  production process. It does not apply to evolved systems (markets,
  ecosystems) or to systems built by a single person. A solo developer
  building a system is constrained by their own cognitive architecture,
  not by organizational communication. The law's domain of applicability
  is narrower than its frequent citation suggests.

- **Temporal mismatch** -- the law maps the organization's communication
  structure *at the time of design* onto the resulting architecture. But
  organizations change faster than architectures. The system you shipped
  in 2020 reflects the org chart of 2018-2019, not the org chart of
  today. This creates a temporal lag where the architecture is always
  a fossil of a previous organizational state, and current teams are
  constrained by decisions that a previous organizational configuration
  made. The law names the constraint but doesn't help manage this
  temporal drift.

## Expressions

- "The system looks like the org chart" -- the colloquial version, less
  precise but immediately intuitive
- "If you have four groups working on a compiler, you'll get a
  four-pass compiler" -- Conway's original example, still the most cited
- "Inverse Conway maneuver" -- deliberately structuring teams to match
  desired architecture, popularized by ThoughtWorks
- "Conway's law always wins" -- the resigned observation that
  architectural aspirations eventually conform to organizational reality
- "Distributed monolith" -- the failure mode predicted by Conway's law
  when teams adopt microservices without changing communication structure
- "Team Topologies" -- Skelton and Pais's framework, which is essentially
  Conway's law operationalized as an organizational design method

## Origin Story

Melvin Conway submitted his paper "How Do Committees Invent?" to the
*Harvard Business Review* in 1967. HBR rejected it. It was published
instead in *Datamation*, a trade magazine. Fred Brooks cited it in *The
Mythical Man-Month* (1975), calling it "Conway's law," and the name
stuck despite Conway never calling it a law himself.

The original paper is remarkably short and clearly argued. Conway
observed that the initial design of a system is also the initial
organization of the design team, because each part of the system must
have someone responsible for it. The interface between parts requires
communication between the responsible people. Therefore, the system's
decomposition mirrors the organization's decomposition.

The empirical validation came decades later. MacCormack, Rusnak, and
Baldwin (2012) studied open-source and commercial software products and
found strong correlations between organizational structure and
architectural modularity. The "mirroring hypothesis" (Colfer and
Baldwin 2016) extended the analysis across industries, confirming that
the correlation between organizational and technical architecture is
robust and bidirectional.

## References

- Conway, M. "How Do Committees Invent?" *Datamation* (1968) -- the
  original paper
- Brooks, F. *The Mythical Man-Month* (1975) -- named "Conway's law"
- MacCormack, A., Rusnak, J. & Baldwin, C. "Exploring the Duality
  between Product and Organizational Architectures." *Research Policy*
  41.8 (2012)
- Skelton, M. & Pais, M. *Team Topologies* (2019) -- Conway's law as
  organizational design methodology
