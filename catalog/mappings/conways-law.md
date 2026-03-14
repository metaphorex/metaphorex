---
slug: conways-law
name: "Conway's Law"
kind: conceptual-metaphor
source_frame: organizational-behavior
target_frame: software-architecture
categories:
  - software-engineering
  - organizational-behavior
author: agent:metaphorex-miner
contributors: []
related:
  - brookss-law
---

## What It Brings

Organizations design systems that mirror their own communication
structures. Melvin Conway's 1968 observation maps the topology of human
communication onto the topology of technical artifacts: if four groups
build a compiler, you get a four-pass compiler. The mapping runs deeper
than mere analogy -- it identifies a structural isomorphism between two
systems that are nominally independent.

- **Communication channels become module boundaries** -- the most
  productive mapping. Teams that don't talk to each other produce
  components that don't integrate well. Teams that share a hallway produce
  tightly coupled subsystems. The organizational boundary and the software
  interface are not merely similar; they are causally linked. The org chart
  is a blueprint the system reads whether anyone intends it or not.
- **Hierarchy maps to layering** -- a deep reporting structure produces
  deeply layered software. A flat organization with cross-functional teams
  produces flatter, more modular architectures. The correspondence is
  strong enough that Eric Raymond reformulated it as: "If you have four
  groups working on a compiler, you'll get a four-pass compiler."
- **The inverse Conway maneuver** -- once the mapping is understood, it
  becomes prescriptive. Teams at ThoughtWorks, Spotify, and Amazon have
  deliberately restructured organizations to produce desired system
  architectures. If you want microservices, create small autonomous teams.
  The law becomes a lever: reshape the organization, and the system
  follows. This reflexive use -- using a descriptive law as a design
  tool -- is rare among named laws.

## Where It Breaks

- **The mapping assumes stable teams** -- Conway's Law presupposes that
  the organization is relatively fixed while the system is being designed.
  In practice, reorganizations, attrition, and contractor rotations mean
  the organizational topology is shifting underneath the system as it is
  built. The system preserves the fossilized communication structure of
  a team that no longer exists. This is why legacy systems often have
  architectural boundaries that no one can explain -- they are the ghosts
  of departed org charts.
- **Open-source falsifies the communication assumption** -- the Linux
  kernel is built by thousands of contributors with no shared org chart,
  no hallways, and no reporting lines. Yet it has a coherent architecture.
  Conway's Law assumes bounded organizations with identifiable
  communication channels. Open-source development replaces org structure
  with governance processes, mailing lists, and maintainer hierarchies
  that are structurally different from corporate communication. The law
  still applies, but the "communication structure" must be redefined so
  broadly that it risks becoming tautological.
- **Causation runs both ways, but the law claims one direction** --
  Conway says the organization shapes the system. But systems also shape
  organizations: a monolithic codebase forces teams into coordination
  patterns they would not otherwise adopt. Database teams exist because
  databases exist, not the other way around. The bidirectional causation
  makes the law less predictive than it appears -- you cannot change just
  the org chart and expect the system to follow if the existing system is
  actively constraining how teams work.
- **Small teams can produce arbitrarily complex systems** -- a single
  developer can write a system with dozens of modules, none of which
  correspond to organizational boundaries (because there is only one
  person). Conway's Law has nothing to say about the internal architecture
  produced by a single mind. The law requires organizational plurality
  to generate its predictions.

## Expressions

- "If you have four groups working on a compiler, you'll get a four-pass
  compiler" -- Eric Raymond's restatement, crisper than the original
- "The inverse Conway maneuver" -- deliberately restructuring teams to
  produce a desired architecture, coined by ThoughtWorks consultants
- "Ship your org chart" -- sardonic shorthand for the law's prediction,
  common in DevOps and platform engineering discussions
- "Conway's Law is not optional" -- a frequent admonition in architecture
  discussions, emphasizing that the isomorphism holds whether you
  acknowledge it or not
- "Two-pizza teams" -- Amazon's organizational heuristic, designed in
  explicit awareness of Conway's Law to produce small, decoupled services

## Origin Story

Melvin Conway submitted his paper "How Do Committees Invent?" to the
Harvard Business Review in 1967; it was rejected on the grounds that the
thesis had not been proved. He published it in Datamation in April 1968.
Fred Brooks cited it in The Mythical Man-Month (1975), giving it the name
"Conway's Law" and bringing it to a much wider audience.

The law gained renewed currency in the 2010s as microservices architecture
became popular. The "inverse Conway maneuver" -- restructuring teams to
achieve architectural goals -- was named by Jonny LeRoy and Matt Simons
at ThoughtWorks. James Lewis and Martin Fowler cited Conway's Law as a
foundational principle in their influential 2014 article defining
microservices. Today the law is one of the most cited principles in
software architecture, far more famous than its author.

## References

- Conway, M. "How Do Committees Invent?" *Datamation* 14(5), April
  1968 -- the original paper
- Brooks, F. *The Mythical Man-Month*, Addison-Wesley, 1975 -- where
  the observation acquired the name "Conway's Law"
- Lewis, J. & Fowler, M. "Microservices," martinfowler.com, March
  2014 -- Conway's Law as foundational principle for microservices
- Skelton, M. & Pais, M. *Team Topologies*, IT Revolution Press,
  2019 -- the inverse Conway maneuver as organizational design method
