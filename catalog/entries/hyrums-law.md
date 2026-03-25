---
slug: hyrums-law
name: "Hyrum's Law"
summary: "With enough users of an API, every observable behavior becomes a binding contract regardless of what the documentation promises."
kind: mental-model
source_frame: contracts-and-law
categories:
- software-engineering
- systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
- law-of-leaky-abstractions
- chestertons-fence
created: '2026-03-21'
updated: '2026-03-21'
grounding: established
transfers:
  - '[law] With enough users, every observable behavior becomes a binding obligation regardless of documentation'
  - '[law] The gap between documented and actual interface shrinks to zero under sufficient usage pressure'
  - '[law] Changing any observable behavior constitutes a breach of implicit contract, even if no explicit promise was made'
limits:
  - '[law] Implies all observed behaviors are equally depended upon, when in practice dependency follows a power-law distribution'
  - '[law] Treats user count as the sole driver of implicit contracts, ignoring that internal organizational boundaries and versioning practices can maintain the documented-actual gap indefinitely'
embodied_patterns:
  - boundary
  - force
  - accretion
relation_types:
  - accumulate
  - contain
  - cause
structure: growth
abstraction_level: generic
---

## Transfers

With a sufficient number of users of an API, it does not matter what you
promise in the contract: all observable behaviors of your system will be
depended on by somebody. Hyrum Wright's observation at Google maps the
legal distinction between written and implied terms onto software
interfaces.

Key structural parallels:

- **Written vs. implied terms** -- contract law recognizes that a signed
  document does not exhaust the agreement. Courts enforce "implied terms"
  that reasonable parties would have expected. Hyrum's Law says the same
  thing about APIs: the documentation is the written contract, but the
  actual behavior -- response times, error message formats, ordering of
  unordered results -- constitutes a body of implied terms that users
  treat as binding.
- **Usage pressure as case law** -- in common law, precedent accumulates
  through cases. Each user who depends on an undocumented behavior is
  another "case" that solidifies the implied contract. The more cases,
  the harder it is to change the behavior without "overturning precedent."
  This explains why large APIs ossify: they accumulate so much implied
  contract that the documented interface becomes a fiction.
- **Breach and damages** -- when a provider changes an observable
  behavior, users experience it as a breach of contract, regardless of
  what the documentation said. The "damages" are broken builds, failed
  integrations, production incidents. The fact that the provider never
  promised the behavior is legally irrelevant in the court of
  operational reality.
- **The impossibility of a complete contract** -- contract theory
  recognizes that no written agreement can anticipate every contingency.
  Hyrum's Law makes the same claim about API documentation: you cannot
  document every observable behavior, so some implied terms are
  inevitable. The only question is how many users will discover them.

## Limits

- **Not all observers are equal** -- the law implies uniform dependency
  across all observable behaviors, but in practice the distribution is
  heavily skewed. A handful of behaviors (response format, status codes)
  attract most dependencies. The long tail of obscure behaviors (thread
  scheduling artifacts, memory allocation patterns) may never be observed
  at all. The law is more useful as a warning about the fat head than as
  a literal claim about the full distribution.
- **Versioning as a pressure valve** -- the legal metaphor breaks because
  software contracts can be versioned in ways that legal contracts
  cannot. Semantic versioning, deprecation policies, and migration
  windows create mechanisms for renegotiating implied terms that have no
  legal equivalent. Organizations that version aggressively can maintain
  a gap between documented and actual interface indefinitely.
- **Internal vs. external users** -- the law was formulated at Google,
  where the "users" of an internal API are other teams within the same
  organization. The dynamics are different for external APIs, where users
  have less access to implementation details and therefore observe fewer
  behaviors. The law is strongest in monorepo environments where any team
  can grep the source code.
- **Conflation with Postel's Law** -- Hyrum's Law is sometimes cited as
  an argument against Postel's Law (be liberal in what you accept). But
  they address different failure modes: Postel's Law concerns input
  handling, while Hyrum's Law concerns output observation. Being strict
  in output does not prevent users from depending on the specific form of
  your strictness.

## Expressions

- "Hyrum's Law guarantees someone is depending on that behavior" -- the
  standard invocation during discussions about whether a change is
  "safe"
- "We can't change that, Hyrum's Law" -- the resignation, used when a
  team discovers that an undocumented behavior has become load-bearing
- "The implicit API surface" -- the broader concept that Hyrum's Law
  names: the gap between what you intend to expose and what you actually
  expose

## Origin Story

Hyrum Wright, a software engineer at Google, articulated the law based on
his experience maintaining large-scale internal libraries used by
thousands of teams. The law emerged from the practical observation that
any change to a widely-used library, no matter how minor or
"implementation-internal," would break someone. Wright formalized this as:
"With a sufficient number of users of an API, it does not matter what you
promise in the contract: all observable behaviors of your system will be
depended on by somebody." The law gained wide circulation through the
hacker-laws repository and through Google's internal engineering culture,
where it became a standard reference in API design reviews.

## References

- Wright, Hyrum. "Hyrum's Law" -- https://www.hyrumslaw.com/
- Winters, Titus, Tom Manshreck, and Hyrum Wright. *Software Engineering
  at Google* (2020) -- discusses the law in the context of large-scale
  software maintenance
- Kerr, Dave. "Hacker Laws" -- https://github.com/dwmkerr/hacker-laws
