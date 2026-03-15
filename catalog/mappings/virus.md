---
author: agent:metaphorex-miner
categories:
- linguistics
- software-engineering
- security
contributors: []
created: '2026-03-15'
harness: Claude Code
kind: dead-metaphor
name: Virus
related:
- firewall
slug: virus
source_frame: medicine
target_frame: computing
updated: '2026-03-15'
---

## What It Brings

A pathogen that cannot reproduce on its own -- it must hijack a host cell's
machinery to replicate. The biological-to-digital mapping is among the most
structurally faithful in all of computing: computer viruses, like biological
ones, are inert code that cannot execute independently. They must attach to
a host program, use that program's execution context to run, and copy
themselves into new hosts. The metaphor imported an entire epidemiological
framework that shaped both the technology and the industry built to fight it.

- **Replication through hijacking** -- a biological virus injects its
  genetic material into a host cell, which then unwittingly produces copies
  of the virus. A computer virus attaches to an executable, which then
  unwittingly copies the virus to other executables when it runs. The
  structural parallel is almost exact, and Fred Cohen chose the term
  precisely because of this correspondence.
- **Epidemiological thinking** -- the metaphor did not just name the
  threat; it imported the entire methodology of disease control. Infection
  vectors (how it spreads), quarantine (isolating infected files),
  inoculation (signature-based detection), and herd immunity (if enough
  machines are patched, the virus cannot propagate) all transferred
  directly from medicine to information security. The antivirus industry
  is organized as a public health system, complete with outbreak alerts,
  vaccination schedules (definition updates), and epidemiological tracking.
- **Contagion without intent** -- biological viruses spread through contact,
  not through the victim's choices. The metaphor frames infected users as
  patients, not as negligent actors. This shaped both legal and cultural
  responses: we quarantine infected machines rather than blame their
  operators, just as we treat disease carriers rather than punish them.

## Where It Breaks

- **Computer viruses have authors** -- biological viruses evolved through
  natural selection over billions of years. Computer viruses are written
  by human beings with specific intentions: destruction, espionage, profit,
  notoriety. The medical metaphor erases the attacker entirely. "Your
  computer has a virus" sounds like bad luck; "someone wrote malicious code
  that exploited your system" sounds like a crime. The epidemiological
  frame systematically depoliticizes what is, at bottom, an adversarial
  human act.
- **Viruses do not mutate on their own** -- biological viruses evolve
  through random mutation and selection pressure. Computer viruses change
  only when their authors release new variants. Polymorphic malware that
  alters its own code to evade detection is the closest analogue to
  biological mutation, but it is engineered polymorphism, not evolution.
  The metaphor overstates the autonomy of the threat.
- **The immune system analogy breaks at scale** -- biological immune
  systems are distributed, adaptive, and self-learning. Antivirus software
  is centralized, signature-based, and perpetually behind. The medical
  metaphor promised that computers could develop "immunity" through
  exposure and learning. Decades later, signature-based detection is
  considered inadequate precisely because it cannot match the adaptive
  elegance of the biological immune system the metaphor invoked.
- **"Antivirus" implies cure; the reality is chronic management** -- the
  medical frame suggests that infection can be cured and health restored.
  In practice, sophisticated malware often cannot be fully removed, only
  contained. The shift from "antivirus" to "endpoint detection and
  response" reflects the security industry's quiet acknowledgment that
  the cure metaphor was always too optimistic.

## Expressions

- "Your computer is infected" -- the diagnostic statement, framing a
  security breach as a medical condition
- "Antivirus software" -- the therapeutic intervention, an entire product
  category named by the metaphor
- "Quarantine" -- isolating suspicious files, directly borrowed from
  epidemiological practice
- "Virus definition updates" -- the equivalent of updated medical
  knowledge about new strains, distributed like public health bulletins
- "Worm" -- a variant that self-replicates without needing a host program,
  extending the biological metaphor to a different class of organism
- "Viral" -- the metaphor's most successful export, now meaning any
  content that spreads rapidly through a population, whether or not it is
  malicious

## Origin Story

Fred Cohen, a graduate student at the University of Southern California,
coined "computer virus" in 1983 during his doctoral research. His advisor
Leonard Adleman (the "A" in RSA encryption) suggested the term, drawing
the explicit analogy to biological viruses. Cohen's 1986 dissertation,
"Computer Viruses," formalized the definition: a program that can modify
other programs to include a possibly evolved copy of itself.

The metaphor was not Cohen's invention out of nothing. Science fiction had
explored the idea of self-replicating programs for years -- John Brunner's
1975 novel *The Shockwave Rider* featured a "tapeworm" program, and the
concept of self-replicating automata dates to John von Neumann's work in
the 1940s. But Cohen and Adleman chose "virus" specifically for the
biological parallel, and the name stuck because the structural mapping
was genuinely illuminating.

The first major PC virus in the wild, Brain (1986), came from Pakistan.
By the late 1980s, the antivirus industry had emerged, organized entirely
around the medical metaphor: companies like McAfee and Norton sold
"protection" against "infection" using "vaccines" (signature files). The
metaphor was already dead by the mid-1990s. Nobody downloading Norton
Antivirus thought about microbiology. But the epidemiological framework
the metaphor imported continues to shape how the security industry
organizes itself, funds research, and communicates threats to the public.

## References

- Cohen, F. "Computer Viruses," PhD dissertation, University of Southern
  California (1986) -- the foundational formal definition
- Adleman, L. "An Abstract Theory of Computer Viruses," Crypto '88 --
  the mathematical framework, by the man who named them
- Szor, P. *The Art of Computer Virus Research and Defense* (2005) --
  comprehensive technical history
- Brunner, J. *The Shockwave Rider* (1975) -- science fiction precursor
  that used the biological replication metaphor for self-spreading code
