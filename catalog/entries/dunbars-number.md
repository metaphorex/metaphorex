---
slug: dunbars-number
name: "Dunbar's Number"
kind: mental-model
source_frame: biology
categories:
  - organizational-behavior
  - systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
  - peter-principle
created: '2026-03-21'
updated: '2026-03-21'
grounding: established
transfers:
  - '[model] The neocortex-to-group-size correlation in primates predicts a cognitive ceiling of roughly 150 stable relationships for humans, reframing organizational scaling problems as biological constraints rather than management failures'
  - '[model] Below the threshold, coordination is maintained through direct personal knowledge -- each member holds a mental model of every other member''s reliability, skills, and social position; above it, coordination requires formal structure (hierarchy, process, documentation) as a prosthetic for relationship memory'
  - '[model] The number appears across independent social formations (Neolithic villages, Roman military centuries, Hutterite communities, Gore-Tex factory units) suggesting a convergent solution to the same cognitive constraint'
limits:
  - '[model] The number 150 has wide confidence intervals (100-250 in Dunbar''s own work), yet is typically cited as a precise threshold, lending false precision to organizational design decisions'
  - '[model] Treats social cognition as a single bottleneck when modern communication tools (Slack, email, shared documents) externalize parts of relationship maintenance, potentially shifting the ceiling without removing it'
  - '[model] The primate correlation assumes that the same neocortical function that limits grooming-based bonding in primates limits language-based bonding in humans, but language is dramatically more efficient than grooming for relationship maintenance, complicating the direct extrapolation'
embodied_patterns:
  - container
  - link
  - scale
relation_types:
  - contain
  - coordinate
  - cause
structure: network
abstraction_level: generic
---

## Transfers

Robin Dunbar's 1992 observation that primate neocortex size correlates
with social group size, extrapolated to humans, predicts a cognitive
limit of roughly 150 stable social relationships. The number has become
one of the most influential cross-domain mappings from evolutionary
biology to organizational design.

Key structural parallels:

- **The cognitive container** -- each person maintains a mental model of
  their social world: who is reliable, who is skilled at what, who
  is allied with whom, who owes favors to whom. This model consumes
  cognitive resources proportional to the number of relationships
  tracked. At roughly 150, the container is full. Adding the 151st
  relationship either displaces an existing one or degrades the
  quality of all models. This is why people in large organizations
  report feeling "anonymous" -- they have exceeded the capacity of
  anyone's social-cognitive container.
- **The governance transition** -- below 150, groups can coordinate
  through mutual knowledge. Every member knows every other member
  well enough to predict behavior, enforce norms through reputation,
  and resolve conflicts through personal negotiation. Above 150,
  these mechanisms break down. The group must introduce formal
  governance: rules, roles, hierarchies, processes. This transition
  is not a management choice but a cognitive necessity. Organizations
  that resist formalization above 150 do not stay informal; they
  become chaotic.
- **Nested circles** -- Dunbar's later work refined the single number
  into a series of concentric circles with characteristic sizes:
  5 (intimate support group), 15 (close friends), 50 (good friends),
  150 (meaningful contacts), 500 (acquaintances), 1500 (faces you
  can name). Each circle represents a different depth of social
  knowledge and a different coordination mechanism. Software teams
  (5-7 people), departments (15-50), and divisions (150) map onto
  these circles with striking regularity, suggesting that
  organizational architecture converges on cognitive constraints
  regardless of industry.

## Limits

- **False precision** -- Dunbar's own research gives a range of
  100-250, not a precise 150. The number has been reified through
  repetition into an engineering constant when it is actually a
  statistical central tendency with wide variance across individuals
  and cultures. Using 150 as a hard threshold for organizational
  design decisions (splitting teams, capping company size) imports
  a specificity that the data does not support.
- **Communication technology as cognitive prosthetic** -- the
  original primate data is about grooming-based bonding, which
  requires co-presence and physical contact. Humans already
  transcended this constraint with language. Digital communication
  tools (social media profiles, CRM systems, shared documents)
  further externalize relationship maintenance, functioning as
  cognitive prosthetics that may shift the ceiling. LinkedIn users
  "maintain" hundreds of relationships that would have been
  impossible to sustain through face-to-face interaction alone.
  Whether these tool-mediated relationships are "real" in the sense
  Dunbar's model requires is an open question, but dismissing them
  entirely ignores the mechanism that distinguished humans from
  other primates in the first place.
- **The correlation is disputed** -- several replication attempts
  have questioned the neocortex-to-group-size correlation, and a
  2021 study by Lindenfors, Wartel, and Lind concluded that the
  confidence interval for the human prediction is so wide (2-520)
  as to be uninformative. Dunbar's Number may be a real phenomenon
  observed across human groups that happens to lack the neat
  neuroscientific explanation originally proposed for it.
- **Cultural variation** -- the converging evidence (Neolithic
  villages, military units, Hutterite communities) comes
  predominantly from Western and small-scale societies. Whether
  the same number applies to cultures with fundamentally different
  kinship structures, collectivist orientations, or social
  organization patterns is less established. The number may reflect
  a specific mode of relationship maintenance rather than a
  universal biological constant.

## Expressions

- "We've hit Dunbar's Number" -- used when an organization
  experiences coordination breakdown at roughly 150 people,
  diagnosing the problem as structural rather than managerial
- "Keep it under Dunbar" -- used in organizational design
  discussions to argue for capping team, department, or company
  size
- "The Dunbar layer" -- used to describe the social-cognitive
  tier at which a group transitions from informal to formal
  coordination
- "Two-pizza teams are Dunbar's inner circle" -- connecting
  Amazon's team-sizing heuristic to Dunbar's 5-person intimate
  support group

## Origin Story

Robin Dunbar, a British anthropologist and evolutionary
psychologist, published the foundational paper "Neocortex Size
as a Constraint on Group Size in Primates" in 1992. The paper
correlated neocortex ratio (neocortex volume relative to total
brain volume) with mean social group size across primate species,
then extrapolated the regression line to the human neocortex ratio,
yielding a predicted group size of roughly 150. Dunbar subsequently
found converging evidence in human social structures: Neolithic
farming villages (150-200 inhabitants), Roman military centuries
(80-160 soldiers), Hutterite community split threshold (150),
Gore-Tex factory unit cap (150), and Christmas card distribution
lists (mean 153.5 recipients). The number entered mainstream
discourse through Malcolm Gladwell's *The Tipping Point* (2000)
and has since become a standard reference in organizational design,
software team scaling, and social network analysis.

## References

- Dunbar, Robin I. M. "Neocortex Size as a Constraint on Group
  Size in Primates" (Journal of Human Evolution, 1992) -- the
  original paper
- Dunbar, Robin. *How Many Friends Does One Person Need?* (2010)
  -- popular-audience treatment of the number and its nested circles
- Gladwell, Malcolm. *The Tipping Point* (2000) -- popularization
  of Dunbar's Number for business audiences
- Lindenfors, Patrik, Andreas Wartel, and Johan Lind. "'Dunbar's
  Number' Deconstructed" (Biology Letters, 2021) -- critical
  reanalysis questioning the precision of the prediction
- Kerr, Dave. "Hacker Laws" -- https://github.com/dwmkerr/hacker-laws
