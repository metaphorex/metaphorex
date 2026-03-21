---
slug: prompt-injection
name: Prompt Injection
kind: metaphor
source_frame: medicine
applies_to:
  - agent-security
categories:
  - security
  - ai-discourse
author: agent:metaphorex-miner
contributors: []
related:
  - ai-safety-is-containment
  - trojan-horse
  - computer-virus-is-biological-infection
  - firewall
dead: false
created: '2026-03-18'
updated: '2026-03-18'
grounding: established
harness: Claude Code
transfers:
  - "[source] a medical injection uses a needle to bypass the skin barrier and deliver a substance directly into the body's internal systems, exploiting the fact that the barrier distinguishes inside from outside"
  - "[source] the injected substance travels through the body's own circulatory system, using trusted internal pathways to reach its target rather than creating new ones"
  - "[source] injection works because the body cannot distinguish an externally introduced substance from one it produced itself once the substance is past the barrier"
limits:
  - "[source] breaks because medical injection requires a physical instrument (needle) that leaves evidence of penetration, while prompt injection leaves no trace of the boundary violation in the output"
  - "[source] misleads because the medical metaphor implies a passive patient, but prompt injection targets an active reasoning system whose own cognitive process becomes the attack vector"
embodied_patterns:
  - boundary
  - container
  - force
relation_types:
  - compete
  - transform
structure: boundary
abstraction_level: specific
---

## Transfers

The injection metaphor enters computing through SQL injection (first
documented by Jeff Forristal in 1998): an attacker inserts malicious code
into an input field, and the system treats it as trusted instructions
rather than untrusted data. The structural core is a boundary violation --
the system cannot distinguish between legitimate commands and injected ones
because they arrive through the same channel.

Prompt injection extends this pattern to language models. Simon Willison
named the attack in 2022, drawing the explicit parallel to SQL injection.
The medical source domain -- a syringe breaching the skin barrier to
deliver a foreign substance into the body's trusted interior -- provides
the deeper structural metaphor that organizes the entire family of
injection attacks.

Key structural parallels:

- **Boundary confusion** -- a medical injection works because the skin
  is a one-way trust boundary: what is inside is trusted, what is outside
  is not. The needle bypasses this boundary. In prompt injection, the
  trust boundary is between the system prompt (trusted instructions from
  the developer) and user input (untrusted data). The attack works when
  the model cannot distinguish developer instructions from user-supplied
  text -- both are "inside" the prompt. The medical metaphor makes this
  boundary failure viscerally legible.
- **The body's own systems distribute the payload** -- injected medicine
  travels through the bloodstream, using the body's own distribution
  network. Injected prompts are processed by the model's own reasoning
  capabilities, using its trusted execution to carry out the attacker's
  intent. The model does not execute foreign code; it follows instructions
  it believes are legitimate, just as the circulatory system does not
  reject properly dissolved substances.
- **The injection family** -- SQL injection, XSS (cross-site scripting),
  command injection, LDAP injection, and prompt injection all share the
  same structural pattern: untrusted input is interpreted as trusted
  instructions because the system conflates data and control channels.
  The medical metaphor unifies this entire family under a single image:
  something foreign getting past the barrier and being treated as self.
- **Dose determines effect** -- in medicine, the same substance can be
  therapeutic or lethal depending on dosage. In prompt injection, the
  same instruction-following capability that makes a model useful is
  what makes it vulnerable. The "dose" is the specificity and authority
  of the injected instruction. This parallel illuminates why prompt
  injection is so hard to fix: you cannot disable the vulnerability
  without disabling the functionality.

## Limits

- **No needle, no mark** -- medical injection requires a physical
  instrument and leaves physical evidence (puncture wound, injection
  site). Prompt injection is invisible: there is no syntactic marker
  distinguishing injected instructions from legitimate ones. The medical
  metaphor implies that detection should be straightforward (look for
  the puncture), but the defining challenge of prompt injection is that
  malicious instructions are indistinguishable from benign ones at the
  token level.
- **The patient is not reasoning** -- a human body receiving an
  injection is a passive biological system processing chemicals. A
  language model receiving a prompt injection is an active reasoning
  system being manipulated through its own cognition. The medical
  metaphor obscures this crucial difference: the model is not merely
  processing input but interpreting, reasoning about, and acting on it.
  The attack surface is the model's intelligence, not its input parsing.
- **Immunity does not transfer** -- biological systems develop antibodies
  after exposure. Language models do not develop resistance to prompt
  injections they have previously encountered. Each session is
  immunologically naive. The medical metaphor's strongest promise --
  that exposure leads to immunity -- does not hold.
- **The metaphor naturalizes a design flaw** -- calling it "injection"
  frames the attack as an intrusion from outside, like a pathogen.
  But prompt injection exploits a fundamental architectural decision:
  using the same channel for instructions and data. The medical metaphor
  obscures the fact that this is a design choice, not an inevitable
  vulnerability. Systems that separate instruction and data channels
  (like parameterized SQL queries) do not suffer injection attacks.

## Expressions

- "Prompt injection attack" -- the standard term for manipulating a
  language model through crafted input, already so established that the
  medical source domain is invisible
- "Inject instructions into the context window" -- practitioner language
  that preserves the medical metaphor's spatial structure (inside/outside)
- "Indirect prompt injection" -- instructions hidden in external content
  (web pages, emails) that the model retrieves and processes, extending
  the metaphor to contaminated surfaces rather than direct needle injection
- "The system prompt is the immune system" -- a common framing that
  extends the medical metaphor: the system prompt tries to protect the
  model from malicious input, but like an immune system, it can be
  overwhelmed or evaded
- "Injection-proof" -- the aspiration, borrowing from medical sterility
  language, that remains unrealized for language models

## Origin Story

Jeff Forristal (writing as "Rain Forest Puppy") published the first
documented SQL injection attack in Phrack Magazine in December 1998. The
term "injection" was already metaphorical -- it borrowed the medical image
of a foreign substance being introduced into a system through a boundary
violation. The metaphor proved so structurally apt that it spawned an
entire category: code injection, command injection, LDAP injection, XML
injection, header injection.

Simon Willison coined "prompt injection" in September 2022, explicitly
drawing the parallel to SQL injection. The naming was strategic: by
connecting the new AI vulnerability to a well-understood class of web
security flaws, Willison made the threat immediately legible to security
practitioners. OpenGuard's 2026 analysis calls it "the most critical
agent security threat," noting that as AI agents gain tool access, memory,
and network capabilities, the blast radius of a successful prompt
injection expands from information leakage to autonomous action on the
attacker's behalf.

The escalation follows a pattern: SQL injection was manageable because
databases do not reason. Prompt injection is harder because language models
do. The same metaphor covers both, but the target domain has changed in
a way that makes the source domain's implied defenses (input sanitization,
parameterized queries) insufficient.

## References

- Forristal, J. ("Rain Forest Puppy"). "NT Web Technology Vulnerabilities,"
  *Phrack Magazine* 54 (1998) -- first documented SQL injection
- Willison, S. "Prompt injection attacks against GPT-3" (2022) -- coined
  the term for language model attacks
- OpenGuard, "Prompt Injections & Agent Security" (2026) -- comprehensive
  agent security threat taxonomy
- OWASP. "Injection" -- Top 10 Web Application Security Risks, consistently
  ranked #1 or near the top since 2003
- Willison, S. "The Lethal Trifecta" (2025) -- combinatorial risk framework
  placing prompt injection in context
