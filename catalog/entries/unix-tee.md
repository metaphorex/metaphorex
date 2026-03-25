---
applies_to:
- data-processing
author: agent:metaphorex-miner
categories:
- computer-science
contributors:
- fshot
created: '2026-03-17'
dead: true
harness: Claude Code
kind: metaphor
name: Unix Tee
summary: "A fitting that splits one data stream into two identical copies. Observation without alteration."
related:
- data-flow-is-fluid-flow
- unix-pipe
- unix-filter
slug: unix-tee
source_frame: fluid-dynamics
updated: '2026-03-17'
transfers:
  - "[source] a tee fitting splits a single flow into two paths without altering the fluid in either"
  - "[source] the T-shaped junction is passive -- it does not pump, redirect, or decide; it simply provides two outlets where there was one"
  - "[source] both output paths receive identical fluid at the same rate"
limits:
  - "[source] breaks because a physical tee divides flow volume between the two paths, whereas the mapped command duplicates the full stream to both destinations -- nothing is split, everything is copied"
  - "[source] misleads because physical tee orientation and pressure dynamics determine flow distribution, but the mapped command always sends identical complete output to both paths regardless of downstream conditions"
embodied_patterns:
  - flow
  - splitting
  - path
relation_types:
  - coordinate
  - transform
structure: pipeline
abstraction_level: specific
---

## Transfers

A T-shaped pipe fitting in a plumbing system: fluid flows in from one
end and exits from both branches of the T. The Unix `tee` command does
the same thing with data: it reads from standard input and writes
simultaneously to standard output and to one or more files. The name is
explicitly borrowed from plumbing -- one of the most transparently
metaphorical commands in Unix.

Key structural parallels:

- **Flow splitting** -- a plumbing tee takes a single stream and divides
  it into two. The `tee` command takes a single data stream and sends it
  two places: the terminal (or the next command in the pipeline) and a
  file. The structural mapping is exact: one input, two outputs, and the
  data continues flowing in both directions.
- **Inline operation** -- a plumbing tee is installed in the middle of a
  pipe run, not at the end. The `tee` command is used in the middle of a
  pipeline: `make 2>&1 | tee build.log | grep error`. It does not
  terminate the flow; it siphons off a copy while the main stream
  continues. This inline character is the whole point -- `tee` exists to
  observe the flow without interrupting it.
- **Passivity** -- a plumbing tee does not pump, heat, or filter the
  fluid. It merely provides a junction. The `tee` command does not
  transform the data. Every byte that enters exits unchanged through both
  paths. This passivity distinguishes `tee` from filters: filters
  transform, tees duplicate.
- **The name teaches the concept** -- unlike "grep" or "awk," which
  require explanation, "tee" is immediately comprehensible to anyone who
  knows plumbing terminology. The metaphor is not just naming; it is
  documentation. A programmer who understands T-fittings understands
  `tee` without reading the man page.

## Limits

- **Physical tees divide flow; `tee` duplicates it** -- this is the
  most significant break. When water hits a T-fitting, the volume splits:
  some goes left, some goes right, and the total flow is conserved. When
  data hits `tee`, every byte goes to both destinations in full. There
  is no division -- there is duplication. The plumbing metaphor implies
  conservation of volume; the digital reality is free copying. This
  difference is fundamental but invisible in the naming.
- **Physical tees are bidirectional; `tee` is not** -- a plumbing
  T-fitting can receive flow from any of its three openings and
  distribute to the others, depending on pressure gradients. The `tee`
  command has a fixed topology: one input (stdin), two outputs (stdout
  and file). You cannot send data backward through `tee` or use it to
  merge two streams. The plumbing fitting is more flexible than the
  software it inspired.
- **The metaphor does not scale** -- a plumber can install a four-way
  cross fitting, a manifold, or a header to split flow into many paths.
  The `tee` command writes to stdout plus one or more files, but it
  cannot split a pipeline into multiple parallel pipelines. For true
  multiway splitting, you need process substitution or named pipes --
  mechanisms that are outside the plumbing metaphor's vocabulary. The
  metaphor promises a fitting for every topology but delivers only the
  simplest T.
- **Pressure and backpressure disappear** -- in plumbing, a tee's
  behavior depends on downstream pressure. If one branch is blocked,
  flow goes to the other. If the `tee` command's file write blocks
  (full disk), the entire pipeline stalls. There is no automatic
  rerouting, no pressure equalization. The plumbing metaphor suggests
  a physical system that adapts to conditions; the digital
  implementation is rigid.

## Expressions

- "Tee it to a file" -- the standard idiom: `command | tee output.log`
- "Tee off the output" -- using `tee` to capture a copy of pipeline data
  for debugging or logging, borrowing from the plumbing sense of "tap off"
- "Pipe tee" -- describing the command by its plumbing equivalent,
  reinforcing the metaphor
- "tee /dev/null" -- a no-op tee that discards the copy, demonstrating
  the command's composability with Unix's other plumbing metaphors
- "tee -a" -- append mode, extending the metaphor: the file is a tank
  that accumulates rather than being refilled each time

## Origin Story

The `tee` command first appeared in Version 5 Unix (1974) at Bell Labs.
The name was chosen by the Unix developers explicitly because the command
does what a plumbing T-fitting does: splits a stream into two paths. It
is part of the systematic plumbing vocabulary that McIlroy, Thompson,
and Ritchie built into Unix -- pipes, filters, streams, sinks, drains,
and tees.

The command was a direct response to a practical problem: how do you
observe data flowing through a pipeline without disrupting it? Before
`tee`, you had to break the pipeline, write to a file, and then construct
a second pipeline to continue processing. `tee` solved this by making the
T-fitting available as a command, maintaining the fiction that a Unix
pipeline is a plumbing system you can tap into at any point.

The man page has always been terse -- `tee` is one of the simplest Unix
commands. Its power comes not from internal complexity but from its
position in the plumbing vocabulary: it fills the gap between linear pipes
and the need to observe or record intermediate data. It is the debugging
fitting in Unix's metaphorical plumbing system.

## References

- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM 17(7),
  1974
- Kernighan, B. & Pike, R. *The Unix Programming Environment*,
  Prentice-Hall, 1984
- McIlroy, M.D. "A Research UNIX Reader," Bell Labs, 1987
- tee(1) man page, man7.org -- https://man7.org/linux/man-pages/man1/tee.1.html
