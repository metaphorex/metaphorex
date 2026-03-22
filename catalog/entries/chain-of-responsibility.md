---
slug: chain-of-responsibility
name: Chain of Responsibility
kind: pattern
source_frame: software-architecture
applies_to:
- organizational-behavior
- decision-making
categories:
- software-engineering
- organizational-behavior
author: agent:metaphorex-miner
contributors: []
related:
- pipeline
- bottleneck
created: '2026-03-21'
updated: '2026-03-21'
grounding: established
harness: Claude Code
transfers:
  - '[source] A request enters a sequence of handlers, each of which inspects the request and either processes it or passes it to the next handler, so that the sender never needs to know which handler ultimately acts'
  - '[source] Each handler in the chain decides independently whether to handle or forward, meaning responsibility is distributed across the chain rather than concentrated in a single dispatcher'
  - '[source] The chain can be reconfigured at runtime by adding, removing, or reordering handlers without altering the request sender, decoupling the act of requesting from the act of fulfilling'
limits:
  - '[source] If no handler in the chain accepts the request, it falls off the end silently unless a catch-all is explicitly installed -- the pattern has no built-in guarantee of fulfillment'
  - '[source] The linear sequencing means that handler order determines priority, but this ordering is implicit and often invisible to the person reading the code, creating a hidden dependency on configuration'
  - '[source] Each handler must share the same interface, which means the pattern works poorly when different handlers need fundamentally different information to make their decisions'
embodied_patterns:
  - path
  - link
  - blockage
relation_types:
  - select
  - cause/propagate
  - coordinate
structure: pipeline
abstraction_level: generic
---

## Transfers

The Chain of Responsibility pattern, codified by the Gang of Four in 1994,
decouples a request's sender from its receiver by threading the request through
a sequence of potential handlers. Each handler inspects the request, decides
whether to process it, and if not, forwards it along the chain. The structural
insight is that responsibility can be distributed across a sequence of
autonomous decision-makers without any central authority knowing in advance who
will act.

Key structural parallels:

- **Decoupled dispatch** -- the sender issues a request and does not know (or
  care) which handler fulfills it. This is structurally identical to how a
  customer complaint moves through an escalation hierarchy: the front-line
  agent either resolves it or passes it to a supervisor, who either resolves
  it or passes it further. The customer does not choose who helps them; the
  chain decides.
- **Sequential autonomy** -- each handler has full authority to accept or
  decline. No handler consults the others; each makes its decision in
  isolation based on its own criteria. This distinguishes the pattern from a
  central dispatcher (which inspects the request once and routes it) and gives
  it the property of graceful extensibility: adding a new handler requires no
  changes to existing ones.
- **Implicit priority through ordering** -- the first handler in the chain
  gets first refusal. This means that chain configuration is a form of policy:
  placing a security-check handler before a business-logic handler ensures
  that unauthorized requests never reach the business layer. The ordering
  encodes organizational priorities without making them explicit in code.
- **Request as a traveling object** -- the request itself is passed unchanged
  (or enriched) from handler to handler, accumulating context as it moves.
  This mirrors how a document circulates through an approval chain, gathering
  signatures, or how a piece of mail is forwarded through sorting facilities
  until it reaches the right destination.

## Limits

- **Silent failure at the chain's end** -- if no handler accepts the request,
  the default behavior in most implementations is to do nothing. Unlike a
  central dispatcher, which would throw an explicit "unhandled" error, the
  chain's distributive structure means that unhandled requests can silently
  disappear. This makes the pattern dangerous in contexts where every request
  must be addressed, such as emergency triage or payment processing.
- **Ordering as hidden policy** -- the chain's behavior depends critically on
  the order of its handlers, but this order is typically set in configuration,
  not in the handlers themselves. When debugging a chain, you must reconstruct
  the runtime ordering to understand why a particular handler did or did not
  fire. In organizations, this manifests as escalation paths that exist on
  paper but whose actual behavior depends on who happens to be staffing each
  level.
- **Uniform interface constraint** -- all handlers must accept the same request
  type, which means the pattern works best when the decision can be made from
  the same information at every level. In practice, different handlers often
  need different context: a spam filter needs message headers, a content
  moderator needs the body, a fraud detector needs payment history. Forcing
  these into a single interface either bloats the request object or starves
  some handlers of information.
- **Performance cost of traversal** -- every request potentially traverses the
  entire chain, even if only the last handler can process it. In long chains
  with expensive evaluation at each node, this traversal cost can dominate.
  The pattern trades dispatch efficiency for configurability.

## Expressions

- "Pass it up the chain" -- escalation in customer service and organizational
  hierarchies, where each level either resolves or forwards
- "Middleware stack" -- web frameworks like Express.js implement request
  handling as a chain of middleware functions, each calling `next()` to
  forward to the next handler
- "Event bubbling" -- in DOM event handling, an event propagates up through
  parent elements until one handles it or it reaches the document root
- "Chain of command" -- military and organizational usage where authority
  flows through a sequence of ranked positions

## Origin Story

The Chain of Responsibility was formalized as a behavioral design pattern in
the Gang of Four's *Design Patterns: Elements of Reusable Object-Oriented
Software* (1994). The pattern's structural ancestor is the exception handling
mechanism in programming languages, where an exception propagates up through
nested handlers until one catches it. The GoF recognized this as a general
strategy for decoupling senders from receivers and abstracted it into a
reusable design. The pattern gained renewed prominence with the rise of web
middleware architectures in the 2000s and 2010s, where HTTP request processing
is almost universally implemented as a handler chain.

## References

- Gamma, Erich, et al. *Design Patterns: Elements of Reusable Object-Oriented
  Software* (1994) -- pp. 223-232, the canonical description
- Fowler, Martin. *Patterns of Enterprise Application Architecture* (2002) --
  discusses the pattern in the context of enterprise middleware
