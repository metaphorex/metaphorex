---
slug: scattered-work
name: "Scattered Work"
summary: "Alexander's pattern: distributing workplaces throughout a community rather than concentrating them in single-purpose districts"
kind: pattern
source_frame: architecture-and-building
applies_to:
  - organizational-structure
categories:
  - systems-thinking
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - flexible-office-space
  - small-work-groups
  - work-community
created: '2026-03-19'
updated: '2026-03-19'
grounding: established
harness: Claude Code
transfers:
  - '[source] concentrating all workplaces in a single district forces long commutes that consume time and energy, while distributing work throughout the community embeds productive activity in the fabric of daily life'
  - '[source] a separated work district becomes socially dead outside business hours, while scattered workplaces keep neighborhoods alive throughout the day because workers and residents share the same streets, shops, and public spaces'
  - '[source] scattering work creates natural redundancy -- if one location becomes unusable, others continue functioning -- because the system has no single point of spatial failure'
limits:
  - '[source] breaks because physical scattering requires that each location be self-sufficient in infrastructure (power, plumbing, transit access), and the cost of duplicating infrastructure across many small sites can exceed the cost of one large campus'
  - '[source] assumes that all work can be performed in small, distributed units, but some activities (heavy manufacturing, large-scale research facilities, hospital complexes) have minimum viable scales that prevent meaningful distribution'
  - '[source] romanticizes the pre-industrial mixed-use neighborhood without accounting for the zoning and environmental reasons work was separated from residence -- noise, pollution, truck traffic -- which remain valid for many industries'
embodied_patterns:
  - part-whole
  - boundary
  - container
relation_types:
  - cause
  - transform
structure: hierarchy
abstraction_level: specific
---

## Transfers

Alexander's pattern #9 argues that the modern practice of concentrating
workplaces in office parks, industrial districts, and central business
districts is destructive to community life. When all work happens in one
place and all living happens in another, the result is commuter traffic,
dead neighborhoods during business hours, and dead office districts at
night. The remedy is to scatter workplaces throughout the community so
that work and life are physically interleaved.

Key structural parallels:

- **Concentration creates dead zones** -- a business district that empties
  at 6 PM and a residential suburb that empties at 8 AM are both failures
  of the same kind: single-purpose zones that are alive for part of the
  day and dead for the rest. Alexander's insight is that temporal deadness
  is a symptom of spatial monoculture. Applied to software, a monolithic
  codebase that concentrates all business logic in one module creates the
  same problem: a module that is overwhelmingly active during feature
  work and completely ignored during infrastructure work. Applied to
  organizations, a centralized team that owns all decisions creates
  bottleneck periods and idle periods rather than steady flow.

- **Scattering embeds work in context** -- when a workshop sits between
  a bakery and an apartment building, the workers eat at the bakery, the
  baker repairs her oven at the workshop, the apartment residents know
  their neighbors' trades. Work is embedded in a social fabric rather
  than extracted from it. In software architecture, this maps onto the
  principle that business logic should live close to the data it operates
  on, not extracted into a separate "logic layer" that is disconnected
  from its context. In organizations, it maps onto embedding specialists
  in product teams rather than concentrating them in functional
  departments.

- **The commute is the tax on concentration** -- Alexander frames the
  daily commute as evidence of a spatial design failure. The time spent
  traveling between separated zones is pure waste, analogous to the
  overhead of context-switching between separated systems. When a
  developer must leave the codebase to consult a wiki, leave the wiki
  to file a ticket, and leave the ticket system to update a dashboard,
  each transition is a commute. Scattering the relevant information
  closer to the work eliminates these transitions.

- **Scattering creates resilience through redundancy** -- a city with
  one business district is fragile; a disaster there halts the economy.
  A city with work scattered across twenty neighborhoods can absorb the
  loss of any one. This maps directly onto distributed systems
  architecture: scattering replicas across availability zones, scattering
  team knowledge across multiple people (reducing bus factor), scattering
  deployment targets across regions. The pattern's structural claim is
  that spatial distribution is inherently more resilient than spatial
  concentration.

- **The grain of scattering matters** -- Alexander does not argue for
  uniform distribution. He argues that each neighborhood should contain
  a mix of work types appropriate to its character. The scattering is
  deliberate, not random. In software, this is the difference between
  a well-designed microservices architecture (each service contains the
  work appropriate to its bounded context) and a randomly decomposed
  system (services split along arbitrary lines with no coherent
  responsibility). The pattern succeeds when each scattered unit is
  locally coherent.

## Limits

- **Infrastructure duplication is expensive** -- a single office campus
  shares reception, IT support, conference rooms, cafeterias, and
  maintenance staff across hundreds of workers. Scattering work into
  twenty small sites requires twenty receptions, twenty IT setups,
  twenty maintenance contracts. The pattern romanticizes the village
  workshop without accounting for the economies of scale that drove
  concentration in the first place. In software, this appears as the
  microservices overhead problem: each service needs its own deployment
  pipeline, monitoring, and on-call rotation, and the aggregate cost
  of these duplicated systems can exceed the cost of maintaining a
  monolith.

- **Some work requires minimum viable scale** -- a hospital needs
  operating theaters, imaging equipment, and specialized staff that
  cannot be scattered into neighborhood clinics. A semiconductor fab
  requires clean rooms that cannot be miniaturized. Alexander
  acknowledges this implicitly by focusing on small workshops and
  offices, but the pattern's rhetoric suggests a universality that its
  applicability does not support. In software, some computations
  require co-located data and processing that cannot be distributed
  without unacceptable latency.

- **Separation was sometimes a solution, not a mistake** -- zoning laws
  that separated heavy industry from residential areas emerged because
  living next to a tannery or a foundry was genuinely harmful. The
  pattern treats all concentration as a failure of imagination, but
  some work produces noise, pollution, traffic, or hazard that makes
  proximity to residences a bad idea. In organizations, separating
  security review from feature development is not a failure of
  "scattering" -- it is an intentional firewall that prevents conflicts
  of interest.

- **Coordination costs scale with distribution** -- scattered units
  must communicate to remain coherent, and communication costs grow
  with distance and the number of nodes. Alexander's pattern assumes
  that scattered workshops are largely autonomous, which works for
  artisans but fails for interdependent teams. A distributed
  engineering organization that scatters across time zones pays a
  coordination tax in meetings, handoffs, and misunderstandings that
  a co-located team avoids.

## Expressions

- "Distributed teams" -- the organizational equivalent of scattered
  work, now standard in remote-first companies
- "Embed the specialist" -- placing a designer or SRE inside a product
  team rather than in a centralized department
- "Co-location of code and data" -- the software architecture principle
  that logic should live near the data it operates on
- "Mixed-use development" -- urban planning term for buildings or zones
  that combine residential, commercial, and office space
- "Bus factor" -- the risk metric that measures how concentrated
  knowledge is; scattering knowledge reduces the bus factor
- "Edge computing" -- processing data near its source rather than
  sending it to a centralized data center

## Origin Story

Christopher Alexander's pattern #9, "Scattered Work," appears in
*A Pattern Language* (1977). Alexander observed that industrial-era
zoning had created cities with separated residential, commercial, and
industrial districts, producing commuter culture and socially dead
neighborhoods. His remedy was to reverse the separation: scatter
workplaces into residential areas so that communities contain both
work and life.

The pattern anticipated the remote work movement by four decades.
When COVID-19 forced millions of knowledge workers to work from home
in 2020, the result was precisely what Alexander described: work
scattered into residential neighborhoods, local cafes becoming
impromptu offices, and commuter districts emptying. The pattern
also maps onto the distributed systems movement in software
engineering, where the arguments for and against scattering
(resilience vs. coordination cost, autonomy vs. consistency) replay
Alexander's urban planning debates in a different medium.

## References

- Alexander, Christopher. *A Pattern Language* (1977), Pattern #9:
  Scattered Work
- Alexander, Christopher. *The Timeless Way of Building* (1979) --
  the theoretical foundation for the pattern language approach
- Newman, Sam. *Building Microservices* (2015) -- the software
  architecture parallel, arguing for distributed service ownership
