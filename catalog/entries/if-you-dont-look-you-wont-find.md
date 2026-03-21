---
slug: if-you-dont-look-you-wont-find
name: If You Don't Look, You Won't Find
kind: metaphor
source_frame: medicine
applies_to:
- decision-making
categories:
- health-and-medicine
- cognitive-science
author: agent:metaphorex-miner
contributors: []
related:
- triage
- the-retrospectoscope
- a-chance-to-cut-is-a-chance-to-cure
provenance: scheins-surgical-aphorisms
created: '2026-03-20'
updated: '2026-03-20'
grounding: established
harness: Claude Code
transfers:
  - '[source] A physical examination involves systematically palpating, percussing, and inspecting body regions that the patient has not complained about, importing the structure where discovery requires active search beyond the presenting complaint'
  - '[source] Pathology that is present but unexamined continues to progress silently -- an undiagnosed tumor grows, an undetected aneurysm expands -- importing the structure where the cost of not looking is not zero but cumulative and compounding'
  - '[source] The decision not to examine a body region is itself a clinical act with consequences, importing the structure where the absence of investigation is not neutral but constitutes an implicit bet that nothing is wrong'
limits:
  - '[source] In medicine the search space is bounded by anatomy -- there are a finite number of organ systems to examine -- but in domains like software or organizations the search space is effectively unbounded, and "looking everywhere" is not a viable strategy'
  - '[source] The aphorism assumes that finding pathology is always better than not finding it, but in medicine screening programs routinely produce overdiagnosis -- finding conditions that would never have caused harm -- and in other domains the cost of knowing can exceed the cost of ignorance'
  - '[source] Medical examination has well-validated protocols for what to look for and how to interpret findings, but the metaphor is often invoked in domains where there is no equivalent diagnostic framework, turning "look harder" into unfocused anxiety rather than systematic search'
embodied_patterns:
  - surface-depth
  - matching
  - path
relation_types:
  - enable
  - cause
structure: hierarchy
abstraction_level: generic
---

## Transfers

The aphorism belongs to the Oslerian tradition of clinical observation.
William Osler taught that the physician's primary instrument is
attentive examination, not theoretical knowledge: "The whole art of
medicine is in observation," he wrote, and variants of "if you don't
look, you won't find" circulate in surgical training as the operational
corollary. The principle is that pathology does not announce itself to
the incurious. A patient presenting with abdominal pain may also have
a melanoma on their back, an enlarged lymph node in their neck, or a
heart murmur that explains their fatigue -- but only if someone looks.

Key structural parallels:

- **Discovery requires active search, not passive reception.** The
  deepest structural transfer is epistemological: knowledge of a
  problem is not a property of the problem but a product of the
  investigation. An unexamined codebase does not have "no bugs"; it
  has undiscovered bugs. An unaudited financial system does not have
  "no fraud"; it has undetected fraud. The metaphor imports medicine's
  hard-won understanding that the absence of a finding is only
  meaningful if you have actually looked. This is not obvious. In
  everyday reasoning, "no news is good news" is the default. The
  medical frame inverts this: no news means no examination.

- **Omission of search is itself a consequential decision.** In
  clinical medicine, the decision not to order a test or examine a
  body region is documented and defensible -- or it is negligent. The
  metaphor imports this framing: choosing not to look is not the
  absence of a decision but a decision with its own risk profile. A
  manager who never conducts one-on-ones is not in a state of
  ignorance about their team's problems; they are in a state of
  chosen blindness. A company that does not audit its supply chain is
  not innocent of labor violations; it is choosing not to find them.
  The medical frame makes the omission visible as an act.

- **Undetected pathology compounds.** The medical urgency behind the
  aphorism is that diseases progress. An undiagnosed cancer at stage I
  is treatable; at stage IV it is terminal. The cost of not looking is
  not static but cumulative. This transfers to technical debt (small
  architectural problems that compound into systemic brittleness),
  organizational dysfunction (a small team conflict that metastasizes
  into department-wide toxicity), and regulatory compliance (a minor
  violation that, undetected, becomes a pattern that triggers
  catastrophic liability).

## Limits

- **Bounded anatomy vs. unbounded search spaces.** The physician's
  examination has natural scope: the human body has a finite number of
  organ systems, and clinical protocols define what to check for each
  presenting complaint. But in software, organizations, and markets,
  the space of things that could be wrong is effectively unbounded.
  "If you don't look, you won't find" is actionable advice when the
  search space is finite and the examination protocols are known. In
  domains without those constraints, the aphorism becomes an
  unfalsifiable demand to look harder without specifying where, which
  is indistinguishable from anxiety.

- **Overdiagnosis is a real cost of looking.** Medicine has learned,
  painfully, that finding things is not always better than not finding
  them. Prostate cancer screening detects slow-growing tumors that
  would never have caused symptoms, leading to unnecessary surgeries
  with serious side effects. Thyroid cancer screening in South Korea
  led to a fifteen-fold increase in diagnoses with no change in
  mortality. The metaphor's imperative to look assumes that discovery
  is always net positive, but in any domain where the cost of
  response exceeds the cost of the condition, looking creates harm.
  Security teams that scan for every possible vulnerability find
  thousands they cannot fix, creating alert fatigue that obscures the
  critical few.

- **The aphorism privileges the examiner's agency.** The frame
  assumes a competent examiner who knows what abnormal looks like.
  In medicine this is backed by years of training. When the metaphor
  migrates to domains where the looker lacks diagnostic competence,
  "looking" produces noise, not signal. A manager who conducts code
  reviews without understanding the codebase finds superficial style
  violations while structural defects pass unnoticed. The aphorism
  does not transfer the training, only the imperative.

## Expressions

- "If you don't look, you won't find" -- the standard clinical form,
  used in surgical and medical training to emphasize thorough
  examination
- "You see only what you look for, you recognize only what you know"
  -- Merrill Sosman's radiology maxim, extending the principle to
  include the role of prior knowledge in recognition
- "The most important thing in the physical examination is the
  physical examination" -- teaching aphorism emphasizing that the exam
  must actually be performed, not assumed
- "Listen to the patient; he is telling you the diagnosis" -- Osler's
  complementary principle, framing attentive observation as the
  primary diagnostic act
- "We find what we look for and we look for what we know" -- variant
  emphasizing the confirmation-bias risk embedded in directed search

## Origin Story

The aphorism is most closely associated with William Osler (1849-1919),
the Canadian physician who is widely regarded as the father of modern
clinical medicine. Osler's pedagogical revolution was to move medical
education from the lecture hall to the bedside, insisting that students
learn by examining patients rather than reading textbooks. His teaching
method -- "see the patient, examine the patient, think about the
patient" -- encoded the principle that observation is the foundation of
medical knowledge.

The specific phrasing "if you don't look, you won't find" circulates
in surgical training as folk wisdom without a single canonical source.
Moshe Schein includes it among the fundamental aphorisms of surgical
practice. The saying's power comes from its simplicity: it makes the
obvious non-obvious by framing the absence of examination as the
cause of the absence of findings, rather than framing the absence of
findings as evidence that nothing is wrong.

## References

- Osler, W. *Aequanimitas and Other Addresses* (1904) -- collected
  clinical teaching principles
- Schein, M. *Aphorisms & Quotations for the Surgeon* (tfm Publishing,
  2003) -- collector of the surgical aphorism tradition
- Sosman, M.C. "A Radiologist's Opinion of the Conventional Chest
  Film" -- source of "you see only what you look for" maxim
