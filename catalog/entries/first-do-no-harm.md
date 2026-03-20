---
slug: first-do-no-harm
name: First Do No Harm
kind: metaphor
source_frame: medicine
applies_to:
- ethics-and-morality
- decision-making
categories:
- health-and-medicine
- ethics-and-morality
author: agent:metaphorex-miner
contributors: []
related:
- triage
- second-opinion
provenance: scheins-surgical-aphorisms
created: '2026-03-20'
updated: '2026-03-20'
grounding: established
harness: Claude Code
transfers:
  - '[source] the physician must evaluate whether a proposed treatment might leave the patient worse off than no treatment at all, importing a decision structure where the baseline is the current state and any intervention must clear the bar of net improvement over inaction'
  - '[source] medical training teaches that the body has self-healing capacities and that premature or excessive intervention can interfere with natural recovery, importing the structural insight that systems often have endogenous repair mechanisms that intervention can disrupt'
  - '[source] the asymmetry between action and inaction in medicine -- a surgeon who operates and causes harm is culpable in a way that a surgeon who declines to operate is not -- imports a moral weighting where the harms of commission are judged more severely than the harms of omission'
limits:
  - '[source] breaks because medical harm has observable, measurable consequences (infection, death, disability) with clear causal chains from intervention to outcome, while harm in policy, technology, and regulation is often diffuse, delayed, and contestable'
  - '[source] misleads by importing the physician''s one-to-one relationship with a single patient into domains where interventions affect millions of people simultaneously and where "doing no harm" to one group may require accepting harm to another'
  - '[source] can be weaponized as a bias toward inaction, because the harms of doing nothing are invisible (people who were never helped, problems that were never addressed) while the harms of intervention are visible and attributable'
---

## Transfers

"First do no harm" -- often rendered in Latin as *primum non nocere* --
is the most widely invoked principle in medical ethics and one of the
most thoroughly migrated medical concepts. It encodes a specific
priority ordering: before considering whether your intervention will
help, verify that it will not make things worse. The constraint is
asymmetric: it treats the prevention of iatrogenic harm (harm caused
by the healer) as lexicographically prior to the pursuit of therapeutic
benefit.

Key structural parallels:

- **The intervention-harm calculus** -- in medicine, every treatment
  carries risks. Surgery can cause infection. Antibiotics can cause
  allergic reactions. Chemotherapy destroys healthy cells alongside
  cancerous ones. The physician's first obligation is to weigh these
  risks against the disease's natural course and ensure the treatment
  is not worse than the condition. This imports directly into technology
  ethics (will this feature cause more harm than it prevents?), policy
  design (will this regulation's side effects exceed the problem it
  addresses?), and software deployment (will this hotfix introduce
  regressions worse than the bug it patches?). The structural transfer
  is the discipline of comparing intervention outcomes to baseline
  outcomes, not to ideal outcomes.
- **Endogenous healing versus exogenous intervention** -- a key medical
  insight underlying the principle is that the body heals itself in many
  cases. Unnecessary surgery, over-prescription, and premature
  intervention can interfere with natural recovery. This maps onto
  organizational life, where many problems resolve themselves through
  natural turnover, shifting priorities, or gradual adjustment. The
  manager who intervenes in every team conflict, the regulator who
  legislates every market imperfection, and the developer who refactors
  every code smell may all be violating the principle by disrupting
  endogenous repair processes.
- **Commission-omission asymmetry** -- the principle encodes a moral
  asymmetry: actively causing harm through intervention is worse than
  passively allowing harm through inaction. A surgeon who operates
  unnecessarily and causes a complication bears responsibility in a way
  that a surgeon who recommends watchful waiting does not, even if the
  patient deteriorates. This transfers into legal liability (malpractice
  attaches to action more easily than to inaction), technology ethics
  (companies that deploy a harmful AI model are judged more harshly than
  companies that fail to deploy a beneficial one), and policy (regulators
  who approve a dangerous drug bear more blame than regulators who delay
  a beneficial one).
- **Epistemic humility as a design constraint** -- the principle is
  strongest when uncertainty is high. When the physician is confident in
  the diagnosis and the treatment, the injunction is easily satisfied.
  When the diagnosis is uncertain and the treatment experimental, "first
  do no harm" becomes a powerful brake on overconfident intervention.
  This transfers to any domain where actors must decide under
  uncertainty: it argues for conservative action when you do not fully
  understand the system you are intervening in.

## Limits

- **"Harm" is not self-defining** -- in medicine, harm is relatively
  (though not perfectly) clear: death, disability, pain, infection. In
  policy, technology, and ethics, harm is deeply contested. Does
  restricting speech cause harm? Does not restricting speech cause harm?
  Does economic disruption from regulation count as harm? The principle
  offers no guidance on how to define harm, and its apparent clarity
  conceals the fact that in most domains of application, the threshold
  question -- what counts as harm? -- is the real disagreement.
- **It privileges the status quo** -- "do no harm" takes the current
  state as the baseline. But the current state may itself be harmful.
  A physician treating a patient with a chronic condition cannot return
  to a pre-disease baseline; they can only choose among imperfect
  futures. In policy, "first do no harm" can be invoked to block
  regulation of an already-harmful industry, because any regulatory
  intervention introduces new costs and risks. The principle, taken
  literally, can become a conservative bias against necessary disruption.
- **It imports a one-to-one clinical frame into systemic contexts** --
  the physician has one patient. The principle asks: will this treatment
  harm this patient? But policymakers, platform operators, and
  organizational leaders affect thousands or millions of people
  simultaneously. Vaccination programs harm some individuals (adverse
  reactions) while benefiting populations. Content moderation harms
  some speakers while protecting others. The principle's one-patient
  structure provides no framework for these distributional trade-offs.
- **The omission bias it encodes can be its own harm** -- the principle's
  asymmetric treatment of action and inaction means that the harms of
  doing nothing are systematically underweighted. The regulator who
  delays approving a life-saving drug to avoid the risk of side effects
  causes invisible deaths -- people who would have been saved die
  without anyone noticing. The technology company that declines to
  deploy a beneficial tool because of potential misuse costs are real
  but never counted. "First do no harm" makes inaction feel safe, but
  inaction has its own body count.

## Expressions

- "First do no harm" -- the standard English formulation, used across
  medicine, technology ethics, policy, and regulation
- "*Primum non nocere*" -- the Latin rendering, sometimes attributed to
  Hippocrates but actually of uncertain medieval origin
- "Move fast and break things" -- Facebook's early motto, explicitly
  constructed as a rejection of the principle in favor of speed
- "The precautionary principle" -- the regulatory analog in
  environmental and public health policy, encoding a similar
  intervention-skepticism
- "Defensive medicine" -- the practice of ordering unnecessary tests
  to avoid liability, an over-application of the principle that
  generates its own harms
- "Above all, do no harm" -- variant phrasing common in technology
  ethics discussions and AI safety discourse
- "Hippocratic oath for engineers" -- periodic calls to formalize the
  principle for software and technology practitioners

## Origin Story

The phrase "first do no harm" is routinely attributed to the Hippocratic
Oath, but it does not appear there. The Oath says "I will abstain from
all intentional wrong-doing and harm" and "I will use treatment to help
the sick according to my ability and judgment, but never with a view to
injury and wrong-doing." The closest passage in the Hippocratic corpus
is from *Epidemics* (Book I, Section XI): "As to diseases, make a habit
of two things -- to help, or at least to do no harm." The Latin *primum
non nocere* appears in medical writing by the 17th century but its
exact origin is uncertain -- it is sometimes attributed to Thomas
Sydenham, sometimes to the Hippocratic tradition generally.

The phrase achieved its modern prominence through its adoption as a
shorthand for medical conservatism: the physician's first obligation is
to not make things worse. Its migration into technology ethics
accelerated in the 2010s as Silicon Valley's "move fast and break
things" ethos generated public backlash, and "first do no harm" became
the rallying principle for a more cautious approach to technology
deployment, AI development, and platform governance.

## References

- Hippocrates. *Epidemics*, Book I, Section XI -- the closest original
  source for the sentiment
- Smith, C.M. "Origin and Uses of Primum Non Nocere -- Above All, Do
  No Harm!" *Journal of Clinical Pharmacology* 45(4), 2005 -- traces
  the phrase's uncertain provenance
- Beauchamp, T. and Childress, J. *Principles of Biomedical Ethics*
  (1979, 8th ed. 2019) -- formalization of non-maleficence as one of
  four bioethical principles
- Jonas, H. *The Imperative of Responsibility* (1979) -- philosophical
  argument for precautionary ethics in technology
