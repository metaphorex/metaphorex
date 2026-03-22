---
slug: postels-law
name: "Postel's Law"
kind: mental-model
source_frame: diplomacy
categories:
- software-engineering
- systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
- hyrums-law
- law-of-leaky-abstractions
created: '2026-03-21'
updated: '2026-03-21'
grounding: established
transfers:
  - '[law] A system should be strict in what it produces and tolerant in what it accepts, absorbing the cost of others'' imperfection'
  - '[law] Asymmetric tolerance -- sending discipline paired with receiving generosity -- maximizes interoperability between imperfect parties'
  - '[law] Robustness comes from each party compensating for the other''s likely deviations from protocol'
limits:
  - '[law] Tolerance in what you accept creates implicit compatibility contracts: consumers begin to depend on the tolerated deviations, making them impossible to reject later (Hyrum''s Law)'
  - '[law] The asymmetry is unstable -- if receivers are liberal, senders have no incentive to be conservative, leading to a race to the bottom in protocol compliance'
embodied_patterns:
  - boundary
  - flow
  - balance
relation_types:
  - enable
  - contain
  - translate
structure: boundary
abstraction_level: generic
---

## Transfers

Be conservative in what you send, liberal in what you accept. Jon Postel's
1980 principle for TCP/IP implementations maps the logic of diplomatic
tolerance onto protocol design: each party absorbs the cost of the other
party's imperfection, and in return the system as a whole achieves
interoperability that strict enforcement would prevent.

Key structural parallels:

- **Diplomatic tolerance** -- in diplomacy, a rigid insistence that every
  communication follow exact protocol would make negotiation impossible.
  Skilled diplomats interpret generously, overlooking minor breaches of
  form to preserve substantive communication. Postel's Law applies the
  same principle to network protocols: a TCP implementation that rejects
  packets with minor formatting irregularities would fail to communicate
  with half the implementations on the network. Tolerance is the price of
  interoperability.
- **The asymmetry principle** -- the law is not "be liberal in
  everything." It prescribes asymmetric standards: strict for outbound
  (what you produce), liberal for inbound (what you consume). This maps
  the diplomatic distinction between self-discipline and other-tolerance.
  A diplomat speaks precisely but interprets charitably. A TCP
  implementation sends well-formed packets but accepts malformed ones
  when the intent is recoverable.
- **The interoperability tax** -- each party that practices Postel's Law
  pays a cost: the engineering effort to handle edge cases, malformed
  inputs, and ambiguous formats. This is a tax on the tolerant party,
  paid in exchange for the benefit of a functioning network. The
  diplomatic analogue: accommodating a difficult negotiating partner is
  costly, but the alternative (no agreement) is costlier.
- **The bootstrapping function** -- Postel formulated the law during the
  early internet, when implementations varied wildly and no single
  implementation could be authoritative. In this context, liberality was
  essential: without it, the network could not bootstrap. The law is most
  powerful in ecosystems with many independent implementers and no
  central authority -- exactly the conditions of both international
  diplomacy and early internet standards.

## Limits

- **Tolerance breeds dependency** -- the most significant structural
  limit. When a receiver accepts malformed input, senders who produce
  that malformed input have no incentive to fix it. Over time, the
  "liberal" behavior becomes load-bearing: removing it would break the
  senders who depend on it. This is the direct intersection with Hyrum's
  Law: tolerance creates implicit contracts. HTML's history is the
  canonical example -- browsers' liberal parsing of invalid HTML made the
  web possible, but also made it impossible to enforce valid HTML
  decades later.
- **The strictness-liberality asymmetry is unstable** -- if receivers
  are always liberal, senders face a moral hazard: they can cut corners
  on output quality because they know receivers will compensate. Over
  successive generations, the "conservative in what you send" half of
  the law erodes, leaving only "liberal in what you accept" -- which
  degrades the entire system. The IETF now debates whether Postel's Law
  was a net positive for the internet or whether it created a
  permissiveness debt that protocols are still paying off.
- **Security implications** -- liberal acceptance of input is a
  vulnerability surface. Accepting unexpected input formats is precisely
  how injection attacks, buffer overflows, and protocol confusion
  exploits work. Modern security practice (input validation, strict
  parsing, allowlists) is fundamentally anti-Postel. The law was
  formulated for a trusted academic network; applying it to adversarial
  environments inverts its intent.
- **The cultural context** -- Postel's Law assumes good-faith
  imperfection: the sender is trying to follow the protocol but failing
  due to implementation bugs. In adversarial contexts (spam, malware,
  protocol abuse), "liberal in what you accept" is not tolerance; it is
  a target. The diplomatic analogy breaks because diplomacy also assumes
  (at minimum) mutual recognition and good faith.

## Expressions

- "Be conservative in what you send, liberal in what you accept" -- the
  canonical formulation, sometimes called the Robustness Principle
- "Postel's Law" -- the shorthand, invoked in API design reviews and
  protocol discussions
- "The Robustness Principle" -- the RFC name (from RFC 761, later
  restated in RFC 1122)
- "Tolerant reader" -- the pattern name in message-oriented systems,
  where consumers ignore unexpected fields rather than rejecting messages
- "Liberal parsing" -- the implementation practice, especially in HTML
  and HTTP, of accepting deviations from the spec

## Origin Story

Jon Postel included the principle in RFC 761 (1980), the specification
for the Transmission Control Protocol: "TCP implementations should follow
a general principle of robustness: be conservative in what you do, be
liberal in what you accept from others." Postel was one of the founding
architects of the internet, serving as editor of the RFC series from its
inception until his death in 1998. The principle reflected both the
practical reality of early internet development (implementations varied
wildly, and intolerance would have fragmented the network) and Postel's
personal temperament, which colleagues described as generous and
accommodating. The law has since become one of the most debated
principles in protocol design, with proponents crediting it for the
internet's success and critics blaming it for the mess of HTML parsing,
the fragility of email standards, and the security vulnerabilities of
overly permissive input handling.

## References

- Postel, Jon. RFC 761: "DoD Standard Transmission Control Protocol"
  (1980) -- https://tools.ietf.org/html/rfc761
- Thomson, Martin. RFC 9413: "Maintaining Robust Protocols" (2023) --
  https://www.rfc-editor.org/rfc/rfc9413 (critiques and refines
  Postel's Law for modern contexts)
- Kerr, Dave. "Hacker Laws" -- https://github.com/dwmkerr/hacker-laws
