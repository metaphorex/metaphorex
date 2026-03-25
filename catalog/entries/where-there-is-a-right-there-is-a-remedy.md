---
author: agent:metaphorex-miner
categories:
- law-and-governance
- philosophy
- ethics-and-morality
contributors: []
created: '2026-03-16'
harness: Claude Code
kind: mental-model
limits:
  - "[model] fails because some rights are deliberately created without remedies -- aspirational constitutional provisions, international human rights declarations, and unenforceable platform terms of service all assert rights while providing no mechanism for enforcement, and they still serve real functions as normative anchors"
  - "[model] misleads because it assumes a binary between remedied and unremedied rights, when in practice remedies exist on a spectrum from fully effective to purely symbolic, and the model cannot distinguish a toothless ombudsman from a court with enforcement power"
  - "[model] breaks in contexts where the remedy itself creates new harms -- mandatory minimum sentencing provides a remedy for crime but generates mass incarceration, and aggressive IP enforcement remedies infringement but chills legitimate fair use"
name: Where There Is a Right, There Is a Remedy
summary: "Legal maxim predicting that rights without enforcement mechanisms erode over time. Pairs every obligation with a feedback loop."
provenance: brooms-legal-maxims
related:
- let-the-master-answer
- responsibilities-are-possessions
slug: where-there-is-a-right-there-is-a-remedy
source_frame: governance
transfers:
  - "[model] predicts that any right declared without a corresponding enforcement mechanism will be eroded over time because rational actors discount unenforceable claims, making the right performative rather than substantive"
  - "[model] structures accountability design by requiring that every stated obligation be paired with a feedback loop -- a right without a remedy is a system without error correction"
  - "[model] distinguishes genuine commitments from virtue signaling by testing whether the declaring party has created or accepted a mechanism through which they can be held to account"
updated: '2026-03-16'
embodied_patterns:
  - balance
  - path
  - force
relation_types:
  - restore
  - enable
structure: equilibrium
abstraction_level: generic
---

## Transfers

Ubi jus ibi remedium: where there is a right, there is a remedy. The maxim
encodes a structural test for whether a right is real or merely declared. If
you assert a right but provide no mechanism through which a person can obtain
redress when that right is violated, you have created a promise that cannot
be kept -- and rational actors will treat it accordingly.

The cognitive move is diagnostic:

- **Rights without remedies are performative** -- a constitution that
  guarantees free speech but provides no court to hear speech cases has not
  actually guaranteed free speech. It has expressed a preference. The maxim
  forces the question: what happens when this right is violated? If the
  answer is "nothing," the right is decorative. This applies far beyond law.
  A company that promises employees "open-door access to leadership" but
  retaliates against those who use it has declared a right without a remedy.
- **The remedy is the proof of the right** -- you can reverse-engineer what
  a system actually values by looking at what it enforces. Organizations that
  invest heavily in compliance remedies for financial reporting but have no
  enforcement mechanism for ethical conduct have revealed their actual
  priorities, regardless of their stated values.
- **Every enforceable system pairs claims with recourse** -- software error
  handling follows this structure. An API that returns errors without error
  codes or retry mechanisms has created "rights" (the expectation of
  service) without "remedies" (a path to resolution). Well-designed systems
  pair every failure mode with a recovery path, just as well-designed legal
  systems pair every right with a remedy.
- **The maxim constrains rule-making** -- if you cannot design a workable
  remedy, you should question whether you should declare the right. This is
  a practical discipline: do not promise what you cannot enforce. It applies
  to parenting ("if you make a rule you won't enforce, you teach that rules
  are optional"), to management ("don't set policies you won't monitor"),
  and to international relations ("don't ratify treaties you won't comply
  with").

## Limits

- **Aspirational rights serve real functions without remedies** -- the
  Universal Declaration of Human Rights has no enforcement mechanism, yet
  it has shaped international norms, provided a vocabulary for dissent,
  and served as a benchmark against which state behavior is measured. The
  maxim's insistence that unremedied rights are empty underestimates the
  power of normative declarations to shift expectations over time, even
  without formal enforcement.
- **Remedies can be worse than the violation** -- the maxim assumes that
  providing a remedy is always an improvement. But remedies have costs.
  Mandatory minimum sentences provide a remedy for crime but generate mass
  incarceration. Aggressive intellectual property enforcement remedies
  infringement but chills legitimate fair use. The existence of a remedy
  does not guarantee that the remedy is proportionate or just.
- **The binary of right-with-remedy versus right-without-remedy is too
  clean** -- in practice, remedies exist on a spectrum. A complaint hotline
  that nobody answers is technically a remedy. A court system so expensive
  that only corporations can afford to use it is technically available. The
  maxim cannot distinguish between a robust enforcement mechanism and a
  nominal one. The real question is not "is there a remedy?" but "is the
  remedy accessible and effective?"
- **Some domains resist remediation by design** -- moral rights, aesthetic
  judgments, and relational expectations often have no appropriate remedy.
  If a friend betrays a confidence, what is the "remedy"? The maxim works
  well in formal systems (law, contract, policy) but poorly in domains
  where enforcement would destroy the very relationship the right is meant
  to protect.

## Expressions

- "Ubi jus ibi remedium" -- the Latin maxim, foundational in English common
  law since at least Ashby v. White (1703)
- "For every wrong, the law provides a remedy" -- Blackstone's paraphrase
  in *Commentaries on the Laws of England* (1765-1769)
- "A right without a remedy is no right at all" -- the compressed modern
  formulation used in legal education
- "What happens when this policy is violated?" -- the organizational
  design version, testing whether a stated commitment has teeth
- "If you can't enforce it, don't promise it" -- the management heuristic
  derived from the same structure
- "Error handling is the remedy for the right to reliable service" --
  software engineering parallel

## Origin Story

The maxim traces to Roman law (ubi jus ibi remedium) and entered English
common law through Bracton's *De Legibus et Consuetudinibus Angliae*
(c. 1235). Its most famous judicial statement came in Ashby v. White (1703),
where Chief Justice Holt declared that "if the plaintiff has a right, he
must of necessity have a means to vindicate and maintain it, and a remedy
if he is injured in the exercise or enjoyment of it." The maxim became a
cornerstone of equity jurisdiction -- courts of equity were created precisely
to provide remedies where common law courts could not.

Herbert Broom included it in *A Selection of Legal Maxims* (first edition
1845), where it appears among the foundational principles of English law.
The maxim remains active in constitutional law, where courts use it to
determine whether legislative or executive action has impermissibly stripped
citizens of remedies for constitutional rights.

## References

- Broom, H. *A Selection of Legal Maxims* (1845; 10th ed. 1939)
- Blackstone, W. *Commentaries on the Laws of England* (1765-1769), Vol. III
- Ashby v. White (1703) 2 Ld Raym 938 -- Holt CJ's foundational statement
- Marbury v. Madison, 5 U.S. 137 (1803) -- Marshall CJ applying the
  principle to constitutional law
