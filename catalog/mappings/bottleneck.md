---
slug: bottleneck
name: "Bottleneck"
kind: dead-metaphor
source_frame: containers
target_frame: systems-performance
categories:
  - systems-thinking
  - software-engineering
author: metaphorex
contributors: []
related:
  - firewall
  - data-flow-is-fluid-flow
---

## What It Brings

The intuition that system throughput is limited by its narrowest point. You
can widen everything else — bigger pipes, faster processors, more staff — but
if you don't widen the neck, nothing changes. The flow rate of the entire
system is the flow rate of its most constrained point.

This is Goldratt's Theory of Constraints compressed into a single word. The
physical mapping carries real structural insight: a bottle has a wide body
(excess capacity) narrowing to a single restriction (the constraint). Pour
faster and all you get is spillage, not throughput. The metaphor tells you
*where to look* and *what not to bother optimizing* — which is more than
most metaphors manage.

The metaphor is so dead that "bottleneck analysis" is a formal methodology
in operations research, taught in business schools without anyone pausing to
note they're extending a figure of speech about glass containers. Profilers
identify bottlenecks. Capacity planners eliminate bottlenecks. The word has
become a technical term that happens to also be a metaphor, which is exactly
what dead metaphors do.

## Where It Breaks

Bottles have ONE neck. Real systems often have shifting, multiple, or
cascading bottlenecks. Widen one neck and you reveal the next — the
constraint migrates downstream. Goldratt knew this (his whole methodology
is a cycle: identify, exploit, subordinate, elevate, repeat), but the
bottleneck metaphor doesn't encode the cycle. It implies a single, findable,
fixable restriction. Many performance engineers have optimized exactly one
bottleneck and declared victory, only to discover they'd merely relocated
the constraint.

A bottleneck is fixed geometry. It doesn't adapt, hide, or move. Real
performance constraints do all three. A database that's fine at 100 QPS
becomes the bottleneck at 10,000 QPS, then stops being the bottleneck when
you add read replicas and the network becomes the constraint instead. The
physical metaphor suggests permanence; real constraints are dynamic.

The metaphor also implies that flow is *good* — that the goal is always to
maximize throughput. But sometimes the bottleneck is doing useful work.
A code review process that slows down deployments is a "bottleneck," but
removing it might increase throughput of bugs along with features. Not every
narrow neck is a problem. Some are filters.

## Expressions

- "The bottleneck is the database" — the canonical engineering usage, often
  correct, always said with weary resignation
- "We're bottlenecked on review" — organizational variant, where the
  constraint is human attention rather than compute
- "Widening the bottleneck" — fixing the constraint, using the physical
  metaphor of reshaping the glass
- "Remove the constraint" — Goldratt's language, which has largely displaced
  the bottle imagery in operations management
- "Throughput limited" — the abstract version, where the metaphor has been
  fully drained of its physical origin

## Origin Story

The word "bottleneck" has been used metaphorically since at least the 1890s,
originally for traffic congestion and logistics — any point where a wide flow
narrows. It was a natural metaphor; everyone had handled bottles.

Goldratt's *The Goal* (1984) formalized the concept into operations
management theory, complete with methodology, without most readers noticing
they were extending a metaphor about glassware into manufacturing science.
The book is written as a novel — a factory manager discovers the Theory of
Constraints through Socratic dialogue with a physicist — and never once
acknowledges that "bottleneck" is figurative. It doesn't need to. The
metaphor was already dead by 1984.

In computing, the term became standard in performance analysis by the 1970s.
Amdahl's Law (1967) is essentially a mathematical formalization of the
bottleneck metaphor: the speedup of a program is limited by the fraction
that cannot be parallelized — the neck of the bottle.

## References

- Goldratt, E. & Cox, J. *The Goal* (1984) — the foundational text for
  constraint theory, built entirely on a dead metaphor
- Amdahl, G. "Validity of the Single Processor Approach to Achieving
  Large Scale Computing Capabilities," AFIPS (1967) — the bottleneck
  metaphor as mathematics
