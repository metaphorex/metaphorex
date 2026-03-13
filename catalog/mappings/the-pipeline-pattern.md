---
author: agent:metaphorex-miner
categories:
- software-engineering
- systems-thinking
contributors:
- fshot
harness: Claude Code
kind: archetype
name: The Pipeline Pattern
related:
- data-flow-is-fluid-flow
- bottleneck
slug: the-pipeline-pattern
source_frame: fluid-dynamics
target_frame: data-processing
---

## What It Brings

An oil pipeline carries crude from wellhead to refinery through connected
segments. Water pipelines carry supply from reservoir to tap. The
Pipeline pattern maps this onto data processing: data flows through a
sequence of stages, each stage transforming the input and passing the
result to the next. Unix pipes (`cmd1 | cmd2 | cmd3`) are the canonical
software instantiation, but the metaphor reaches far beyond shell
scripting -- ETL pipelines, CI/CD pipelines, machine learning pipelines,
and data engineering pipelines all inherit the same fluid image.

Key structural parallels:

- **Flow is unidirectional** -- oil doesn't flow backward through a
  pipeline. Data enters at one end and exits at the other, transformed
  at each stage. The metaphor makes sequential processing feel like
  physics: the direction is obvious and natural, governed by something
  like gravity or pressure.
- **Stages are independent and composable** -- a pipeline segment
  doesn't know what comes before or after it. It receives input,
  processes it, and outputs the result. Unix pipes enforce this: each
  program reads stdin and writes stdout. The fluid metaphor naturalizes
  this composability -- you connect pipe segments, and the fluid flows.
- **The pipeline has throughput, not just correctness** -- physical
  pipelines are measured in barrels per day. Software pipelines are
  measured in records per second. The metaphor imports the language of
  flow rate, capacity, and throughput into data processing, shifting
  the conversation from "does it work" to "how fast does it flow."
- **Backpressure is a natural concept** -- if a downstream pipe
  segment is narrower, pressure builds up. In reactive streams and
  message queues, slow consumers create backpressure that must be
  managed. The fluid metaphor makes this failure mode immediately
  intuitive: of course a pipe can be overwhelmed.
- **Filters remove impurities** -- water treatment pipelines include
  filtration stages. Data pipelines include validation and filtering
  stages. The metaphor frames data quality as purification -- dirty
  data goes in, clean data comes out.

## Where It Breaks

- **Data is not a fluid** -- fluids are continuous; data is discrete.
  Fluids mix; data items maintain identity. A barrel of oil in the
  middle of a pipeline has lost its individuality. A record in a data
  pipeline retains its schema, its primary key, its lineage. The fluid
  metaphor obscures the discrete, addressable nature of data and can
  lead developers to treat data pipelines as undifferentiated streams
  when individual records matter.
- **Real pipelines don't branch easily; software pipelines do** --
  splitting a physical pipeline requires expensive infrastructure. A
  software pipeline can fan out to multiple consumers with a `tee` or
  a pub/sub topic. The metaphor's linearity underrepresents the
  directed acyclic graphs that most real data pipelines become. By
  the time a "pipeline" has branches, joins, and conditional routing,
  it's a network, not a pipe.
- **The pipeline metaphor hides state** -- a physical pipeline is
  stateless; the pipe doesn't remember previous fluid. But many
  software pipeline stages are stateful: aggregations, windowed
  computations, deduplication. The stateless purity of the pipe
  metaphor can mislead architects into underestimating the complexity
  of stages that must remember what they've seen.
- **Pipelines suggest continuous flow; most software pipelines are
  batched** -- despite the fluid imagery, most ETL pipelines run on
  schedules: nightly batch jobs, hourly syncs. The metaphor of
  continuous flow creates expectations of real-time processing that
  the implementation doesn't deliver. "Pipeline" promises a stream
  but often delivers a bucket brigade.
- **Failure in a physical pipeline is catastrophic and visible** --
  a burst pipe floods the landscape. A failed pipeline stage often
  fails silently, dropping records or producing corrupt output that
  isn't discovered until downstream. The dramatic, visible nature of
  physical pipe failures is the opposite of software pipeline failures,
  which are typically quiet and insidious.
- **"Pipeline" has become a dead metaphor in CI/CD** -- when
  developers say "the pipeline is broken," they mean their GitHub
  Actions workflow failed. The fluid origin is completely absent.
  This semantic drift means "pipeline" now carries two distinct
  meanings in software: data-processing-as-fluid-flow (alive) and
  CI/CD-as-workflow (dead metaphor wearing a pipeline costume).

## Expressions

- "Data flows through the pipeline" -- the core metaphor, data as
  fluid moving through connected segments
- "The pipeline is clogged" -- a stage is slow or blocked, impeding
  throughput
- "Backpressure" -- downstream slowness pushing resistance upstream,
  directly from fluid dynamics
- "Filter stage" -- removing unwanted data, purification of the stream
- "Pipeline orchestration" -- managing the flow, the pipeline
  operator's control room
- "Pipe and filter architecture" -- the formal architectural style,
  combining the plumbing and purification metaphors
- "The build pipeline" -- CI/CD usage, where "pipeline" means
  sequential workflow
- "Streaming pipeline" -- emphasizing continuous flow over batch
  processing

## Origin Story

The pipeline metaphor in computing dates to Doug McIlroy's Unix pipes,
implemented by Ken Thompson in 1973. McIlroy's memo proposing pipes
used explicitly plumbing language: programs should be connected "like
garden hoses -- screw in another segment when it becomes necessary."
The metaphor was so productive that it shaped Unix's fundamental design
philosophy: small programs that do one thing, connected by pipes.

The fluid metaphor then migrated upward. ETL (Extract, Transform, Load)
pipelines in data warehousing borrowed the image in the 1990s. CI/CD
pipelines adopted it in the 2010s. Machine learning pipelines
(scikit-learn's `Pipeline` class) extended it to model training. Each
adoption stretched the metaphor further from its fluid-dynamics origin,
but the core image -- data flowing through connected stages -- proved
remarkably durable.

## References

- McIlroy, M.D. "Summary -- Unimplemented Commands" (1964) -- the
  original memo proposing pipes
- Ritchie, D.M. & Thompson, K. "The UNIX Time-Sharing System" (1974)
  -- pipes as a fundamental Unix mechanism
- Hohpe, G. & Woolf, B. *Enterprise Integration Patterns* (2003),
  Chapter 3: Pipes and Filters
- Kleppmann, Martin. *Designing Data-Intensive Applications* (2017),
  Chapter 10: Batch Processing -- modern pipeline architectures
