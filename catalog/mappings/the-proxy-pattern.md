---
slug: the-proxy-pattern
name: "The Proxy Pattern"
kind: conceptual-metaphor
source_frame: social-roles
target_frame: object-oriented-design
categories:
  - software-engineering
author: agent:metaphorex-miner
contributors: []
harness: "Claude Code"
related:
  - the-facade-pattern
  - the-decorator-pattern
---

## What It Brings

A proxy is someone authorized to act on your behalf: a legal proxy votes
at a shareholders' meeting, a diplomatic proxy negotiates a treaty, a
proxy bidder raises the paddle at auction. The principal is absent, but
their authority is present through the stand-in. The GoF Proxy pattern
maps this onto software: a proxy object stands in for another object,
controlling access to it while presenting the same interface.

Key structural parallels:

- **The proxy has delegated authority, not inherent authority** -- a legal
  proxy acts within the bounds of a power of attorney. A software proxy
  implements the same interface as the real subject and forwards calls to
  it. The metaphor makes the constraint clear: the proxy is not the thing
  itself. It acts under mandate, and the mandate has limits. Developers
  who internalize this avoid the mistake of giving proxy objects
  independent behavior that exceeds what the real subject supports.
- **The principal need not be present** -- the whole point of a proxy is
  that the real party is elsewhere, unavailable, or costly to summon. A
  virtual proxy defers creating an expensive object until it is actually
  needed. A remote proxy represents an object in a different address
  space. The social metaphor naturalizes this: you send a proxy precisely
  because you cannot or should not attend yourself.
- **Proxies can filter and protect** -- a protection proxy in software
  checks access rights before forwarding a request, just as a corporate
  proxy may be instructed to vote "no" on certain resolutions regardless
  of floor debate. The metaphor frames access control not as a wall
  (firewall) but as a gatekeeper with judgment and instructions.
- **Identity is ambiguous by design** -- a proxy is supposed to be
  indistinguishable from the principal for most practical purposes.
  Callers interact with the proxy interface and should not need to know
  whether they are talking to the real object or its stand-in. This maps
  directly from the social contract: a valid proxy's signature is legally
  the principal's signature.
- **The relationship is one-to-one** -- a proxy represents one specific
  principal. This distinguishes it from a facade (which simplifies access
  to a subsystem) and a mediator (which coordinates among multiple
  objects). The social metaphor encodes this constraint naturally:
  a proxy card names one voter, not a committee.

## Where It Breaks

- **Social proxies have judgment; software proxies usually don't** -- a
  diplomatic proxy interprets ambiguous instructions, reads the room, and
  improvises. A software proxy almost always forwards requests
  mechanically. The metaphor imports a sense of intelligence and
  discretion that the implementation doesn't deliver. When developers
  expect proxy objects to make smart decisions (caching strategies,
  retry logic, request transformation), they are projecting the social
  metaphor's richness onto what is typically a thin forwarding layer.
- **Revocation works differently** -- a power of attorney can be revoked
  instantly, and the proxy loses all authority. In software, revoking a
  proxy is not a first-class concept. Callers who hold a reference to a
  proxy object keep using it; there is no built-in mechanism for the
  proxy to announce that its mandate has expired. The metaphor suggests
  a governance model that the pattern doesn't implement.
- **Trust is institutional in the social domain, structural in software**
  -- you trust a legal proxy because the legal system enforces the
  delegation contract. You trust a software proxy because it implements
  the same interface and the type system guarantees substitutability. The
  sources of trust are fundamentally different, and the metaphor papers
  over this. When the proxy is a remote proxy across a network boundary,
  the trust model breaks further: network proxies can be spoofed, and no
  type system enforces fidelity across process boundaries.
- **Social proxies are temporary; software proxies often outlive their
  principals** -- you appoint a proxy for a specific meeting or
  transaction. A software proxy object may persist for the lifetime of
  the application, long after the "real" object has been garbage
  collected or the remote service has been decommissioned. The metaphor
  implies a bounded engagement, but the implementation creates permanent
  intermediaries. This contributes to proxy proliferation: layers of
  proxies wrapping proxies, each outlasting the context that justified
  its creation.
- **The "double" problem** -- in social life, everyone knows the proxy is
  not the principal. In software, the interface identity between proxy
  and real subject can cause genuine confusion about which object is
  which. Debugging through proxy layers is notoriously frustrating
  because stack traces show the proxy's methods, not the real subject's,
  creating the software equivalent of talking to someone's lawyer when
  you want to talk to them directly.

## Expressions

- "Proxy object" -- the GoF term itself, importing the full social
  metaphor of delegated representation into object-oriented design
- "Proxy server" -- a server that acts on behalf of clients, extending
  the social metaphor to network infrastructure
- "Standing in for the real object" -- the theatrical variant, casting
  the proxy as an understudy rather than a delegate
- "Lazy loading through a proxy" -- the principal is too expensive to
  summon, so the proxy handles appearances until the real thing is needed
- "Reverse proxy" -- inverts the delegation: instead of representing the
  client to the server, it represents the server to the client. The
  social metaphor strains here, because "reverse proxy" has no clean
  social analog
- "Transparent proxy" -- a proxy the caller doesn't know about, breaking
  the social contract where both parties acknowledge the delegation

## Origin Story

The proxy concept in software predates its GoF codification. Remote
procedure call systems in the 1980s (Sun RPC, Xerox Courier) used
"stub" objects that acted as local stand-ins for remote services. The
stubs were proxies in everything but name.

The GoF formalized the pattern in *Design Patterns* (1994), drawing
explicitly on the social and legal metaphor. They distinguished three
variants: remote proxy (representing an object in another address space),
virtual proxy (creating expensive objects on demand), and protection
proxy (controlling access rights). Each variant maps cleanly to a
different social scenario: the diplomatic envoy, the advance team, and
the bodyguard.

The proxy metaphor then expanded far beyond OOP. HTTP proxy servers,
proxy design in distributed systems (Java RMI, CORBA), and modern API
gateways all use the term. In each case, the core social structure
persists: one entity acts on behalf of another, presenting a compatible
face to the world while adding a layer of indirection. The pattern's
name has proven durable because the social metaphor is immediately
intuitive, even to developers who have never appointed a legal proxy.

## References

- Gamma, E. et al. *Design Patterns: Elements of Reusable Object-
  Oriented Software* (1994), Chapter 4: Structural Patterns
- Birrell, A.D. & Nelson, B.J. "Implementing Remote Procedure Calls,"
  *ACM Transactions on Computer Systems* 2(1) (1984): 39-59
- Henning, M. & Vinoski, S. *Advanced CORBA Programming with C++*
  (1999), proxy and stub architecture in distributed object systems
