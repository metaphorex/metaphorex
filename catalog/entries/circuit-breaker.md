---
slug: circuit-breaker
name: Circuit Breaker
kind: pattern
source_frame: electricity
applies_to:
- software-engineering
categories:
- software-engineering
- systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
- single-point-of-failure
- blast-radius
created: '2026-03-21'
updated: '2026-03-21'
grounding: established
harness: Claude Code
transfers:
  - '[source] A circuit breaker monitors current flow and trips open when the load exceeds a safe threshold, physically severing the circuit to prevent heat buildup from destroying the wiring or connected devices'
  - '[source] The breaker has three distinct states -- closed (current flows freely), open (current is blocked), and a reset mechanism that allows the circuit to be re-closed once the fault is cleared'
  - '[source] The protective cut happens automatically and instantly, without requiring a human operator to diagnose the overload, because the damage from delay would outweigh the cost of a false trip'
limits:
  - '[source] A physical circuit breaker protects against overcurrent on a single wire, but software circuit breakers are typically monitoring error rates across distributed calls, where "overload" is statistical, not physical'
  - '[source] The electrical metaphor implies the fault is downstream (the appliance is drawing too much), but in software the failure may be in the network, in the dependency, or in the circuit breaker''s own threshold configuration'
embodied_patterns:
  - boundary
  - blockage
  - flow
relation_types:
  - prevent
  - cause/propagate
  - restore
structure: boundary
abstraction_level: generic
---

## Transfers

In electrical engineering, a circuit breaker is a safety device that
automatically interrupts current flow when it detects an overload or short
circuit. The device protects the system by sacrificing availability (the
circuit goes dead) to prevent catastrophic damage (fire, melted wiring,
destroyed equipment). Michael Nygard imported this concept into software
architecture in *Release It!* (2007), recognizing that the same structural
trade-off applies to distributed systems: when a downstream service is
failing, it is better to stop calling it entirely than to let failures
cascade through the system.

Key structural parallels:

- **Threshold-triggered disconnection** -- the circuit breaker does not
  attempt to fix the problem. It detects that a threshold has been breached
  (too many failures in a time window) and severs the connection. This is
  structurally distinct from retry logic, which tries to push through the
  failure, and from load balancing, which routes around it. The breaker's
  strategy is deliberate disconnection: accept partial system failure to
  prevent total system failure.
- **Three-state lifecycle** -- the physical breaker has two states (closed
  and tripped). Nygard's software pattern adds a third: half-open, where the
  breaker tentatively allows a small number of requests through to test
  whether the downstream service has recovered. This closed-open-half-open
  cycle maps onto any system that must balance between aggressive protection
  and eventual recovery: immune responses that must eventually stand down,
  quarantines that must eventually lift, trade embargoes that must eventually
  be tested.
- **Fast failure over slow degradation** -- when the breaker is open,
  requests fail immediately with a known error rather than waiting for a
  timeout. This converts slow, unpredictable failure (hanging connections,
  thread pool exhaustion) into fast, predictable failure (instant rejection).
  The structural principle is that a system that fails quickly and loudly is
  safer than one that fails slowly and silently.
- **Cascading failure prevention** -- the deepest structural insight is that
  in interconnected systems, the failure of one component can propagate to
  others through shared resources (thread pools, connection pools, memory).
  The circuit breaker acts as a firebreak: it confines the failure to the
  component that caused it by preventing the caller from accumulating
  blocked resources.

## Limits

- **Threshold calibration is the real problem** -- the circuit breaker
  pattern is easy to describe but hard to tune. Set the failure threshold
  too low and the breaker trips on transient errors, causing unnecessary
  outages. Set it too high and the breaker fails to protect against
  genuine cascading failure. The electrical metaphor makes this look simple
  (wire gauge determines trip current), but software failure modes are
  far noisier: latency spikes, partial failures, and error rate fluctuations
  make threshold selection a continuous judgment call, not a one-time
  engineering calculation.
- **The breaker does not diagnose** -- a circuit breaker tells you that
  something is wrong but not what. It treats all failures the same way:
  trip and disconnect. This is appropriate for overload protection but
  inadequate for diagnosis. In organizations, the analogous failure is
  "we stopped working with that vendor because it was causing problems"
  without investigating whether the problems were temporary, fixable, or
  caused by the organization itself.
- **Half-open is the hardest state** -- the half-open state requires
  deciding how many probe requests to send, how long to wait for recovery,
  and what counts as "recovered." In practice, this state is where most
  circuit breaker implementations fail: they either recover too aggressively
  (slamming the recovering service with full load) or too conservatively
  (keeping the breaker open long after the downstream service has healed).
  The electrical metaphor provides no guidance here because physical breakers
  reset to fully closed immediately.
- **Only protects the caller** -- the circuit breaker protects the system
  that contains it, not the failing system downstream. If the downstream
  service is overloaded, the circuit breaker reduces its load (a side
  benefit), but the pattern's design intent is self-protection, not
  altruism. In organizational settings, "we stopped calling them" may
  protect your team's throughput while leaving the struggling team to
  collapse under other callers' load.

## Expressions

- "The circuit breaker tripped" -- describing a software system that has
  automatically stopped calling a failing dependency
- "We need a circuit breaker around that integration" -- advocating for
  failure isolation in distributed system design
- "Half-open state" -- the probing phase where a system tentatively tests
  whether a previously failing dependency has recovered
- "Fail fast" -- the principle that underlies the circuit breaker: return an
  error immediately rather than waiting for a timeout, common across
  resilience engineering discourse

## Origin Story

Physical circuit breakers were invented by Thomas Edison in 1879 as part of
his commercial power distribution system. The software pattern was named and
codified by Michael Nygard in *Release It! Design and Deploy Production-Ready
Software* (2007), drawing on his experience with cascading failures in
production systems. Nygard recognized that the electrical safety device's
structure -- automatic disconnection at a threshold, with a mechanism for
eventual reset -- mapped precisely onto the problem of dependent service
failure in distributed architectures. The pattern was further popularized by
Netflix's Hystrix library (2012), which made circuit breakers a standard
component of microservice architectures.

## References

- Nygard, Michael. *Release It! Design and Deploy Production-Ready Software*
  (2007) -- the canonical description of the software circuit breaker pattern
- Netflix Technology Blog. "Introducing Hystrix" (2012) -- the widely adopted
  open-source implementation
- Fowler, Martin. "CircuitBreaker" (2014) -- a concise pattern description at
  martinfowler.com
