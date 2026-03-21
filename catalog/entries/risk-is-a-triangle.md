---
applies_to:
- combinatorial-risk
author: agent:metaphorex-miner
categories:
- systems-thinking
- security
contributors: []
created: '2026-03-18'
harness: Claude Code
kind: paradigm
limits:
  - "[paradigm] assumes exactly three necessary conditions, but many real hazards have more -- the fire triangle itself was extended to a tetrahedron when chemical chain reactions were recognized as a fourth factor"
  - "[paradigm] implies the conditions are independent and equally weighted, obscuring cases where one condition dominates or where conditions interact non-linearly"
  - "[paradigm] suggests mitigation is simple subtraction (remove one side), but in practice a condition may be impossible to fully eliminate rather than merely reduced"
name: Risk Is a Triangle
related:
- lethal-trifecta
slug: risk-is-a-triangle
source_frame: fire-safety
transfers:
  - "[paradigm] structures risk as the combination of N independent necessary conditions, each individually manageable but dangerous in concert, making hazard assessment a matter of identifying and enumerating preconditions"
  - "[paradigm] imports the subtraction principle from fire suppression -- remove any one side and the triangle collapses -- giving practitioners a clear mitigation strategy: find the easiest condition to eliminate"
  - "[paradigm] makes combinatorial risk visually legible by mapping abstract preconditions onto geometric shapes, enabling pedagogy and rapid communication of risk structure"
updated: '2026-03-18'
embodied_patterns:
  - matching
  - path
  - boundary
relation_types:
  - cause
  - transform
structure: hierarchy
abstraction_level: generic
---

## Transfers

The fire triangle -- heat, fuel, oxygen -- is the canonical model: three
conditions, each necessary, none sufficient, dangerous only in
combination. Remove any one and fire cannot sustain. This structure has
been independently discovered across multiple domains, always with the
same insight: danger is combinatorial, and mitigation is subtraction.

Key structural parallels:

- **Necessary conditions, not sufficient ones** -- each vertex of the
  triangle is harmless alone. Heat without fuel is just warmth. Fuel
  without oxygen is inert storage. The paradigm teaches practitioners to
  look not for a single cause but for the combination that enables harm.
  This is the core transfer: stop asking "what caused this?" and start
  asking "which conditions converged?"
- **Mitigation by subtraction** -- fire suppression works by removing
  one element: water removes heat, a blanket removes oxygen, clearing
  brush removes fuel. The triangle paradigm imports this into every
  domain it touches. The fraud triangle (pressure, opportunity,
  rationalization) suggests removing opportunity through controls. The
  epidemiological triad (host, agent, environment) suggests modifying
  the environment. The strategy is always the same: find the cheapest
  side to eliminate.
- **Visual pedagogy** -- the geometric shape makes abstract risk
  concrete. Fire safety instructors draw a triangle on a whiteboard.
  Fraud auditors draw a triangle. The shape itself becomes a thinking
  tool -- a way to check completeness ("have I identified all three
  sides?") and a communication device ("which side are we attacking?").
- **Cross-domain isomorphism** -- the fire triangle, fraud triangle
  (Albrecht/Cressey), epidemiological triad, and lethal trifecta
  (Willison) are structurally identical. Each maps three necessary
  conditions onto the same geometric shape. The paradigm is not
  metaphorical in the usual sense -- it is a recurring structural
  pattern discovered independently in fire science, criminology,
  epidemiology, and information security.

## Limits

- **The number three is a pedagogical convenience, not a natural law** --
  real systems often have more than three necessary conditions. The fire
  triangle became the fire tetrahedron when fire science recognized
  chemical chain reactions as a fourth element. The fraud triangle has
  been challenged by models with four or five factors. The geometric
  simplicity that makes the paradigm teachable also makes it
  reductive. Practitioners who internalize "three sides" may stop
  looking after they find the third condition.
- **Equal weighting is an illusion** -- the triangle's symmetry implies
  each condition contributes equally. In practice, conditions are
  rarely equal. In the fraud triangle, opportunity is far more
  controllable than pressure or rationalization. In the fire triangle,
  you cannot remove oxygen from an open environment. The geometric
  equality can mislead practitioners into treating all three sides as
  equally viable mitigation targets.
- **Subtraction assumes elimination is possible** -- "remove one side"
  sounds decisive but may be infeasible. You cannot remove all
  untrusted content from an AI agent's environment. You cannot
  eliminate all financial pressure from employees. The paradigm's
  clean mitigation logic can create false confidence about the
  completeness of controls.
- **Static structure, dynamic reality** -- the triangle is a snapshot.
  Real risk evolves: conditions strengthen, weaken, and interact over
  time. A condition that was absent can emerge. A condition that was
  controlled can escape controls. The paradigm's fixed geometry does
  not naturally accommodate temporal dynamics or feedback loops.

## Expressions

- "The fire triangle" -- the original and most widely taught instance,
  standard in fire safety education worldwide
- "The fraud triangle" -- Cressey/Albrecht's criminological application:
  pressure, opportunity, rationalization
- "The epidemiological triad" -- host, agent, environment in disease
  transmission
- "Remove one side of the triangle" -- the standard mitigation advice,
  used across all domains where the paradigm appears
- "Which leg are we cutting?" -- practitioner shorthand for choosing a
  mitigation strategy

## Origin Story

The fire triangle emerged from fire safety pedagogy, likely in the early
20th century, as a teaching tool for firefighters and safety engineers.
It has no single inventor -- it codified what chemists already knew about
combustion into a visual mnemonic. The triangle was extended to a
tetrahedron in the 1960s when fire scientists added the chemical chain
reaction as a fourth element, but the triangle remains the dominant
pedagogical form.

Donald Cressey's fraud triangle (1953) applied the same structure to
white-collar crime, though the direct influence of the fire triangle is
unclear -- the structural isomorphism may be convergent rather than
borrowed. The epidemiological triad predates both, tracing to the germ
theory era. Simon Willison's "lethal trifecta" (2025) is the most
recent instance, explicitly named after the fire triangle analogy and
applied to AI agent security.

## References

- Cressey, Donald. *Other People's Money* (1953) -- the fraud triangle
- Albrecht, W. Steve et al. *Fraud Examination* (2011) -- systematized
  fraud triangle for auditing practice
- Willison, Simon. "The Lethal Trifecta" (2025) -- AI agent security
  application, explicitly citing the fire triangle
- National Fire Protection Association -- fire triangle pedagogy
