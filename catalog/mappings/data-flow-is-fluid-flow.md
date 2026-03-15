---
author: fshot
categories:
- software-engineering
- systems-thinking
contributors: []
created: '2026-03-07'
kind: paradigm
name: Data Flow Is Fluid Flow
provenance: mcilroy-pipes-memo
related:
- program-failure-is-bodily-failure
- bottleneck
slug: data-flow-is-fluid-flow
source_frame: fluid-dynamics
target_frame: data-processing
updated: '2026-03-11'
---

## What It Brings

The metaphor that became infrastructure. When Doug McIlroy proposed Unix
pipes in 1964, he imported the entire compositional logic of plumbing
into software design. Data "flows" through "pipes," gets "filtered,"
arrives at "sinks." Because the metaphor was so structurally apt,
engineers built systems that *actually work this way*.

Key structural parallels:

- **Composability** — plumbing connects with standardized joints. Unix
  pipes connect with a standardized interface (text streams). You can
  rearrange the pipes without redesigning the system. `grep | sort | uniq`
  works because each segment doesn't care what's upstream or downstream.
- **Directionality** — fluids flow downhill (or under pressure). Data
  flows from source to sink. The metaphor gives engineers an immediate
  intuition about system topology.
- **Flow rate and capacity** — a pipe has throughput limits. A buffer
  can overflow. These aren't just metaphors: "backpressure" in
  Reactive Streams is a formal protocol concept, borrowed wholesale from
  fluid dynamics.
- **Leaks and blockages** — data can be "lost" (leaked) or processing
  can "stall" (blocked pipe). The diagnostic intuition transfers: if
  nothing is coming out, check for a blockage upstream.

The metaphor's deepest gift is *composability as a default assumption*.
Fluids don't care about the shape of the pipe they just left. This
insight (that processing stages should be independent) is the
foundation of Unix philosophy, streaming architectures, and functional
data pipelines.

## Where It Breaks

- **Fluids are continuous; data is discrete** — water doesn't arrive in
  packets. It doesn't have headers, delimiters, or encoding. The
  metaphor obscures the fundamental challenge of data processing:
  parsing, framing, and schema evolution.
- **Fluids obey physics; data obeys logic** — water can't flow uphill
  without a pump. Data can be copied, broadcast, and sent in any
  direction at near-zero cost. The metaphor imports scarcity intuitions
  that don't apply. Data isn't "used up" when it flows through a filter.
- **"Backpressure" imports useful structure and misleading baggage** —
  the concept is genuinely useful: a slow consumer should signal the
  producer to slow down. But fluids also have viscosity, turbulence,
  and laminar vs. turbulent flow. None of these map. Engineers
  occasionally try to extend the metaphor into these regions and
  produce nonsense.
- **"Data lake" is where the metaphor drowns** — a lake is where
  water *stops flowing*. Calling a massive unstructured data store a
  "lake" is accidentally honest: it's where data goes to sit,
  stratify, and resist extraction.
  The metaphor warns you, if you listen.
- **Fluids mix; data shouldn't** — when two streams of water merge, you
  get water. When two data streams merge, you get a schema conflict.
  The metaphor makes data integration look easier than it is.

## Expressions

- "Pipe the output to grep" — the original Unix expression, now so
  literal it barely registers as metaphor
- "Streaming architecture" — continuous flow as system topology
- "Data pipeline" — sequential processing stages connected by flow
- "Filter" — a stage that removes unwanted elements (borrowed from
  fluid filtration)
- "Tap" — an observation point that diverts a copy of the flow
  (plumbing fixture)
- "Source" — where data originates, as a spring or wellhead
- "Sink" — the terminal destination of a flow (drain)
- "Buffer overflow" — the container's capacity exceeded, with
  catastrophic spillage
- "Backpressure" — downstream resistance propagating upstream
- "Data lake" — a reservoir of unprocessed data (see "Where It Breaks")
- "Drain the queue" — consume pending messages as emptying a vessel

## Origin Story

Doug McIlroy's 1964 memo at Bell Labs proposed connecting programs "like
garden hoses — screw in another segment when it becomes necessary to
massage data in another way." Ken Thompson implemented pipes in Unix in
1973, reportedly in one night. The metaphor was so natural that it
became the shell operator `|`, one of the most productive keystrokes in
computing history.

The lineage runs through ETL pipelines, Java's `InputStream`/
`OutputStream`, Node.js streams, Reactive Extensions, Apache Kafka, and
every system that treats data processing as flow through connected
stages. McIlroy's garden hose became civilization-scale plumbing.

## References

- McIlroy, M.D. Internal Bell Labs memo (1964), quoted in Mahoney,
  M.S. "The Unix Oral History Project"
- Ritchie, D.M. & Thompson, K. "The UNIX Time-Sharing System,"
  *Communications of the ACM* 17:7 (1974)
- Marz, N. & Warren, J. *Big Data: Principles and Best Practices of
  Scalable Real-Time Data Systems* (2015) — Lambda architecture as
  extended plumbing metaphor
