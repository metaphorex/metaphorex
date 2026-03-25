---
applies_to:
- security-analysis
author: agent:metaphorex-miner
categories:
- computer-science
- security
contributors: []
created: '2026-03-18'
harness: Claude Code
kind: paradigm
limits:
  - "[paradigm] assumes data flows in traceable paths like fluid through pipes, but in event-driven and asynchronous systems, data can appear at sinks through paths that no static analysis can enumerate"
  - "[paradigm] frames contamination as binary (tainted or clean), but real data undergoes partial sanitization, transformation, and re-combination that makes the clean/dirty boundary a spectrum rather than a line"
  - "[paradigm] implies that mapping all sources and sinks is a completable task, but in systems with dynamic code generation or plugin architectures the set of sinks is unbounded"
name: Source and Sink Analysis
summary: "Track untrusted data from entry points (sources) to dangerous operations (sinks). Security as fluid-dynamics: control endpoints, not the medium."
related:
- attack-surface
- lethal-trifecta
slug: source-and-sink-analysis
source_frame: fluid-dynamics
transfers:
  - "[paradigm] maps the physics of fluid flow -- contaminated input enters at sources, propagates through channels, and exits at sinks -- onto data security, making taint tracking a spatial exercise in tracing flow paths"
  - "[paradigm] imports the insight that contamination propagates downstream, so security analysis must follow data forward from entry points rather than backward from vulnerabilities, inverting the typical debugging mindset"
  - "[paradigm] carries the fluid-dynamics principle that you control flow by controlling endpoints, not the medium -- secure the sources and sinks rather than trying to purify data in transit"
updated: '2026-03-18'
embodied_patterns:
  - flow
  - container
  - balance
relation_types:
  - decompose
  - coordinate
structure: pipeline
abstraction_level: generic
---

## Transfers

Map untrusted inputs (sources) to dangerous outputs (sinks). The
paradigm borrows from fluid dynamics: contaminated fluid enters a
system at source points and must be tracked through every channel until
it reaches a sink where it could cause harm. In security, sources are
entry points for untrusted data (user input, API responses, file
uploads) and sinks are operations where that data could be dangerous
(SQL queries, system calls, HTML rendering).

Key structural parallels:

- **Flow as contamination propagation** -- in fluid dynamics, a
  contaminant introduced at a source spreads through connected
  channels. The paradigm maps this onto data: once untrusted input
  enters a system, it "flows" through variables, function calls, and
  data structures. Any operation that touches contaminated data becomes
  contaminated itself. This makes security analysis spatial -- you
  trace paths on a flow graph rather than inspecting individual
  operations.
- **Sources and sinks as the only points that matter** -- fluid
  engineers control contamination at endpoints, not by purifying
  every molecule in transit. The paradigm imports this economy: you
  do not need to audit every line of code, only the entry points
  (sources) and the dangerous operations (sinks). OpenGuard's advice
  crystallizes this: "If you have not drawn both maps, you do not
  know where your prompt-injection risk is."
- **Taint as persistent state** -- once fluid is contaminated, it
  remains contaminated unless explicitly treated. The paradigm maps
  this to taint tracking in static analysis: data from untrusted
  sources carries a "taint" flag that propagates through assignments
  and function calls until explicitly sanitized. The fluid metaphor
  makes this persistence intuitive -- you would not drink downstream
  from a pollution source just because the water passed through a
  long pipe.
- **Sanitization as filtration** -- water treatment plants sit between
  contaminated sources and consumption points. Input validation and
  output encoding sit between untrusted sources and dangerous sinks.
  The paradigm makes the placement of sanitization logical: it belongs
  at the boundary between contaminated and clean zones, not scattered
  arbitrarily through the codebase.

## Limits

- **Data does not flow like fluid** -- fluid follows physics: it moves
  downhill, fills containers, and does not spontaneously jump between
  disconnected pipes. Data in event-driven systems, message queues,
  and distributed architectures can appear at sinks through paths that
  no static flow analysis can predict. The fluid metaphor's physical
  constraints create false confidence in the traceability of data
  movement.
- **Binary taint is a simplification** -- fluid is either contaminated
  or it is not (at a given threshold). Data undergoes partial
  sanitization, encoding, transformation, and recombination. An HTML
  entity-encoded string is "clean" for HTML rendering but still
  "dirty" for SQL. The paradigm's binary clean/dirty framing obscures
  the context-dependence of safety.
- **The set of sinks may be unbounded** -- in a closed plumbing system,
  you can enumerate all outlets. In software with dynamic code
  generation, runtime code evaluation, plugin architectures, or
  reflection, new sinks can be created at runtime. The paradigm's
  implied completeness -- "draw both maps" -- may be impossible in
  sufficiently dynamic systems.
- **Sources are not always identifiable** -- the paradigm assumes you
  can enumerate entry points. In AI agent systems, "untrusted content"
  can arrive through any tool output, any retrieved document, any
  cached memory. The source is not a discrete pipe but the entire
  environment. The fluid-dynamics framing breaks when the contamination
  is ambient rather than channeled.

## Expressions

- "Source-to-sink analysis" -- the standard term in static analysis
  and security auditing
- "Taint analysis" / "taint tracking" -- the compiler technique that
  operationalizes the paradigm, tracking data provenance from source
  to sink
- "If you have not drawn both maps, you do not know where your
  prompt-injection risk is" -- OpenGuard's formulation for AI agents
- "Untrusted input reaches a dangerous sink" -- the canonical
  vulnerability description pattern in security advisories
- "Sanitize at the boundary" -- the design principle derived from
  the paradigm's flow logic

## Origin Story

Source-and-sink analysis emerged from compiler data-flow analysis in
the 1970s, where it was used to track the propagation of values through
program variables for optimization. The security application came later:
Perl's "taint mode" (1989) was among the first practical implementations,
automatically tracking data from external sources and preventing its use
in dangerous operations (system calls, file operations) without explicit
sanitization.

The terminology borrows directly from fluid dynamics and network theory,
where "source" and "sink" are standard terms for points where flow
originates and terminates. The security community adopted the terms
because the structural parallel is precise: untrusted data enters at
sources and causes harm at sinks, just as contaminated fluid enters a
system and causes damage at discharge points.

The paradigm has gained renewed attention in the AI agent security
context (2025-2026), where the sources (any content the agent processes)
and sinks (any action the agent can take) are both dramatically expanded
compared to traditional web applications.

## References

- OpenGuard. "Prompt Injections & Agent Security" (2026)
  https://openguard.sh/blog/prompt-injections/ -- applies source-sink
  analysis to AI agent threat modeling
- Wall, Larry. Perl 5 taint mode documentation (1994) -- early
  practical implementation of taint tracking
- Livshits, V. Benjamin & Lam, Monica S. "Finding Security
  Vulnerabilities in Java Applications with Static Analysis" *USENIX
  Security* (2005) -- foundational work on automated source-sink
  vulnerability detection
