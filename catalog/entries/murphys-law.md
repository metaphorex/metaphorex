---
slug: murphys-law
name: Murphy's Law
kind: mental-model
categories:
  - risk-management
  - systems-thinking
  - software-engineering
author: agent:metaphorex-miner
harness: Claude Code
contributors: []
related:
  - friction-in-war
  - defensive-programming
  - margin-of-safety
created: '2026-03-22'
updated: '2026-03-22'
grounding: folk
transfers:
  - '[law] predicts that any failure mode that is physically possible will eventually be exercised, because systems operate over enough trials, users, and environmental conditions that low-probability events become near-certainties given sufficient time'
  - '[law] reframes pessimism as a design principle: if a connector can be plugged in backwards, someone will plug it in backwards, so the correct response is not training or warnings but making the wrong configuration physically impossible'
  - '[model] identifies the asymmetry between failure and success -- success requires every component to work correctly, while failure requires only one component to fail, so the combinatorial space of failure vastly exceeds the combinatorial space of success'
limits:
  - '[model] is unfalsifiable as popularly stated -- if something goes wrong, it confirms the law; if nothing goes wrong, the law predicts it will eventually -- which makes it more of a heuristic attitude than a testable proposition'
  - '[model] conflates genuine engineering prudence (design for failure modes) with fatalistic folk wisdom ("things always go wrong"), and the fatalistic reading can justify under-investment in prevention by treating failure as inevitable rather than designable-against'
embodied_patterns:
  - force
  - path
  - blockage
relation_types:
  - cause/accumulate
  - prevent
  - cause/constrain
structure: competition
abstraction_level: generic
---

## Transfers

"Anything that can go wrong will go wrong." Popularly attributed to
Captain Edward Murphy, a US Air Force engineer, during rocket-sled
deceleration tests at Edwards Air Force Base in 1949. The insight that
matters is not the pessimistic truism but the engineering principle
underneath it: design systems that cannot be misassembled, not systems
that rely on correct assembly.

- **Design for the failure mode, not the success path** -- the
  operational core of Murphy's Law. Murphy's original complaint was
  about a strain gauge harness that could be wired in two ways, one
  of which was wrong. A technician wired it wrong. Murphy's response
  was not "we need better technicians" but "we need a connector that
  can only be plugged in one way." This is the distinction between
  a folk proverb and a design principle: the proverb says things go
  wrong; the principle says make the wrong thing impossible. Poka-yoke
  (error-proofing) in manufacturing, type systems in programming,
  and forcing functions in UX design are all implementations of this
  insight.

- **Combinatorial inevitability** -- a system with N components, each
  with a small probability of failure, has a near-certain probability
  of *some* failure as N grows. This is not pessimism but arithmetic.
  A system with 1,000 components each at 99.9% reliability has a
  63% chance of at least one failure. Murphy's Law is the folk
  articulation of the union bound in probability theory. The
  engineering response is redundancy, graceful degradation, and
  fail-safe design -- not optimism about individual component
  reliability.

- **The asymmetry of failure and success** -- success requires
  everything to work; failure requires only one thing to break. This
  creates a structural asymmetry that Murphy's Law names without
  quantifying. In complex systems (aircraft, surgery, software
  deployments), the number of failure modes vastly exceeds the
  number of success modes. The law's practical consequence: testing
  must focus disproportionately on failure paths, because the success
  path is a narrow corridor through a vast space of possible failures.

- **Temporal exhaustion** -- given enough time, every exercisable
  failure mode will be exercised. O-rings that work in warm weather
  will eventually encounter cold weather. Software that handles
  normal input will eventually receive adversarial input. Systems
  that survive ordinary load will eventually face extraordinary load.
  Murphy's Law is the argument for stress testing, chaos engineering,
  and pre-mortems: if the failure mode exists, time will find it, so
  you should find it first.

## Limits

- **Unfalsifiable as stated** -- the popular formulation ("anything
  that can go wrong will go wrong") is not a testable hypothesis.
  If failure occurs, the law is confirmed. If failure does not occur,
  the defender says "it hasn't happened *yet*." This makes the law
  epistemologically empty in its folk form. Its value is as a design
  heuristic (assume failure modes will be exercised), not as a
  predictive law (all failures will occur). The heuristic is
  productive; the law is not.

- **Fatalism vs. engineering** -- the folk reading ("things always
  go wrong, nothing you can do") is the opposite of the engineering
  reading ("things will go wrong, so design against it"). When
  Murphy's Law is invoked as resignation rather than as a call to
  defensive design, it becomes actively harmful: teams that believe
  failure is inevitable may invest less in prevention, monitoring,
  and recovery, creating a self-fulfilling prophecy. The law is
  useful precisely to the extent that it is *not* used fatalistically.

- **Selection bias in salience** -- we notice and remember when
  things go wrong. We do not notice or remember the vastly more
  numerous occasions when things go right. This availability bias
  makes Murphy's Law feel more true than it is. The bread does not
  always fall butter-side down; we just remember the times it did
  because the cleanup was annoying. Applied to engineering, this
  means Murphy's Law must be calibrated with actual failure-rate
  data rather than intuition, because intuition systematically
  overweights memorable failures.

- **Not all failure modes are equal** -- the law treats all possible
  failures as equally worth designing against, but in practice,
  resources are finite. A connector that can be plugged in backwards
  should be redesigned. A meteor strike on the server room should
  not. The engineering discipline of failure mode and effects analysis
  (FMEA) exists precisely because Murphy's Law provides no
  prioritization framework. Not everything that can go wrong
  *deserves* preventive investment.

## Expressions

- "Anything that can go wrong will go wrong" -- the canonical
  formulation, usually delivered after something has already gone
  wrong
- "If there's a wrong way to do it, someone will" -- the
  design-principle version, emphasizing user error as a design input
- "Murphy was an optimist" -- the escalation, implying that even
  things you thought couldn't go wrong, will
- "That's a Murphy-proof design" -- engineering compliment: the
  system cannot be misassembled or misused
- "This is why we have checklists" -- the operational response to
  Murphy's Law in aviation, medicine, and deployment engineering

## Origin Story

The story originates at Edwards Air Force Base in 1949, during US Air
Force Project MX981, a series of rocket-sled experiments testing human
tolerance for rapid deceleration. Captain Edward Murphy, an engineer,
designed a strain gauge harness with sensors that could be installed in
two orientations, one correct and one incorrect. A technician installed
every sensor incorrectly. Murphy reportedly said of the technician,
"If there's any way to do it wrong, he'll find it."

George Nichols, the project manager, compressed this into "Anything
that can go wrong will go wrong" and called it "Murphy's Law" in a
subsequent press conference. The phrase entered aerospace engineering
culture immediately and popular culture shortly after. John Stapp,
the Air Force physician who rode the rocket sled, helped popularize it
by crediting the project's excellent safety record to their policy of
taking Murphy's Law seriously: they designed every system assuming
that every possible error would eventually occur.

The law's persistence owes something to its dual nature: it functions
simultaneously as a joke (a resigned shrug at the universe's hostility)
and as a genuine engineering principle (design for the failure mode).
The joke keeps it in circulation; the principle keeps it useful.

## References

- Spark, N.T. *A History of Murphy's Law.* Periscope Film (2006) --
  the most thoroughly researched account of the origin story
- Reason, J. *Human Error.* Cambridge University Press (1990) --
  the systematic study of failure modes that Murphy's Law gestures at
- Shingo, S. *Zero Quality Control: Source Inspection and the
  Poka-Yoke System.* Productivity Press (1986) -- the manufacturing
  operationalization of Murphy's insight
