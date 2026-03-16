# Taxonomy stress test: what the import projects will yield
## Pre-flight analysis for the Miner agent

---

## TL;DR

The 5-kind taxonomy holds for all 12 import projects. No new kind is needed.
Three additions required: a recognized `mental-model` predictive subtype
(for named laws and effects), a `grounding` field with four values, and an
explicit discard filter in every import playbook.

---

## What each import project will actually yield

### Taxonomy-clean imports

**Glasgow Mapping Metaphor database (#1228)** — pure `metaphor` entries, bulk
importable. Already structured as source→target domain mappings. Grounding:
`folk` for most; some `established`.

**Nautical terms (#1226)** — `metaphor` + `dead: true`. The etymological
content is the value; `transfers` describes the original live mapping's
relational structure. "Three sheets to the wind" → "[source] excess of
uncontrolled surface area produces erratic, uncoordinated motion." Grounding:
`folk`.

**Ouroboros (#1132), Pied Piper (#1131)** — `archetype`. Clean.

### Mixed bags (classify per item, not per book)

**Hauser & Reich's Notes on Directing (#1232)**

One book, multiple kinds:

| Example | Kind | Notes |
|---------|------|-------|
| "Every scene is a chase scene" | `metaphor` | Drama mapped to pursuit |
| "The director creates conditions, not results" | `paradigm` | Position on creative leadership |
| "Acting is reacting" | `paradigm` | Position on performance technique |
| "Never show the audience your work" | `paradigm` | Opinion on craft and display |
| "If in doubt, cut it" | `mental-model` | Cross-domain decision rule under uncertainty |

The Miner classifies per item. Not every item in a book is the same kind.

**Andy Riley's comedy writers' room glossary (#1234)**

| Example | Kind | Action |
|---------|------|--------|
| "Lightning rod" (joke to absorb notes, protecting a better joke) | `metaphor` + `dead: true` | Import |
| "Gorilla" (moment so strong the audience talks about it afterward) | `metaphor` | Import |
| "Yes, and" | `mental-model` | Import — rich cross-domain usage |
| "Punching up / punching down" | `metaphor` | Import |
| "Table draft" (draft read at the table read) | Pure technical jargon | **Discard** |
| "Pickup" (line re-recorded after principal photography) | Pure technical jargon | **Discard** |
| "Producer note" | Pure technical jargon | **Discard** |

**Bannard's Aphorisms for Artists (#1231)**

Dense with paradigms and mental models; genuine metaphors are rarer.

- Evaluative principles ("bad art tries to look like good art") → `paradigm`
- Metaphorical craft observations → `metaphor` or `paradigm`
- Creative unblocking moves → `mental-model`

Don't force `metaphor` classification. Some aphorisms are too compressed to
generate `transfers` — discard them rather than padding.

### The stressed cases: named laws, effects, principles

**Hacker Laws (#1225) and TPS/Deming (#1233)**

Five structurally distinct things arrive under the label "law" or "principle":

---

#### Type 1: Named laws and effects

Conway's Law, Goodhart's Law, Gall's Law, Brooks's Law, Hofstadter's Law,
Amdahl's Law, Parkinson's Law, Murphy's Law, Dunning-Kruger Effect, Halo
Effect, Hawthorne Effect, Lindy Effect.

**What they are:** Empirical regularities asserted to have predictive power.
Descriptive, not prescriptive. Cross-domain. No inherent position.

**Kind:** `mental-model` — predictive subtype. `transfers` propositions use
"[law] predicts / implies / means that ..." form.

```yaml
kind: mental-model
title: Conway's Law
grounding: established
transfers:
  - "[law] predicts that system architecture will mirror the communication
    structure of the organization that built it"
  - "[law] implies that changing architecture requires changing the team
    structure that produces it"
  - "[law] means organizational silos produce architectural silos regardless
    of design intent"
limits:
  - "[law] is directional, not deterministic — strong leadership can
    temporarily override the effect"
  - "[law] says nothing about which communication structure is correct,
    only that systems reflect whichever one exists"
```

```yaml
kind: mental-model
title: Goodhart's Law
grounding: established
transfers:
  - "[law] predicts that when a measure becomes a target, it ceases to be
    a good measure"
  - "[law] implies that optimizing for a proxy metric degrades the system
    the metric was designed to represent"
limits:
  - "[law] applies to proxies — direct measurement of the actual goal is
    not subject to Goodhart effects"
```

Compare to a cognitive-move mental model:

```yaml
kind: mental-model
title: Inversion
# grounding omitted — defaults to folk
transfers:
  - "[model] reframes the question by asking what would guarantee failure
    rather than what would produce success"
  - "[model] finds constraints by working backward from the desired end state"
  - "[model] reveals hidden assumptions by asking what you would do if you
    wanted the opposite outcome"
limits:
  - "[model] can produce paralysis if failure modes are too numerous to rank"
  - "[model] assumes success and failure are symmetric — some failure modes
    have no instructive inverse"
```

Same kind, different proposition form. The embedding model captures the
distinction; the contributor writes accurate propositions.

---

#### Type 2: Razors

Occam's Razor, Hanlon's Razor, Hitchens's Razor, Sagan's Standard.

**What they are:** Decision rules for resolving underdetermination. When
multiple explanations fit the evidence, a razor prescribes which to prefer.
Cross-domain, no inherent position, prescribing a cognitive move.

**Kind:** `mental-model` — cognitive-move subtype.

```yaml
kind: mental-model
title: Hanlon's Razor
grounding: folk
transfers:
  - "[razor] instructs: prefer the explanation that requires less malicious
    intent when multiple explanations fit the evidence"
  - "[razor] reduces the cost of repairing relationships by defaulting to
    charitable interpretation"
  - "[razor] conserves investigative resources by eliminating low-probability
    explanations first"
limits:
  - "[razor] fails when malicious intent is demonstrably present or the
    simpler explanation"
  - "[razor] can be weaponized to excuse repeated harmful behavior as mere
    incompetence"
```

---

#### Type 3: Principles and operational rules

DRY, YAGNI, SOLID, Unix Philosophy, Deming's 14 Points, Hippocratic Oath.

**What they are:** Normative prescriptions. Tell you what you *should* do.
Domain-specific. Take a position. You can agree or disagree.

**Kind:** `paradigm` — fine-grained, with narrow `applies_to`.

Deming's 14 Points each get their own entry — they're separable and
independently applicable. "Drive out fear" and "eliminate numerical quotas"
are distinct paradigms.

```yaml
kind: paradigm
title: Don't Repeat Yourself (DRY)
applies_to: [software-engineering, documentation, system-design]
grounding: folk
transfers:
  - "[paradigm] every piece of knowledge must have a single authoritative
    representation in a system"
  - "[paradigm] duplication means changes must be made in multiple places,
    creating drift risk proportional to the number of copies"
  - "[paradigm] a change to one copy that isn't reflected in others is a
    defect waiting to be discovered"
limits:
  - "[paradigm] premature deduplication creates false abstractions harder
    to change than the original duplication"
  - "[paradigm] applies to knowledge, not necessarily to code — some code
    repetition reduces coupling at the cost of duplication"
```

---

#### Type 4: Theory-named-after-metaphor

Broken Windows Theory, Butterfly Effect.

**What they are:** Scientific or social theories named after their founding
metaphor. The metaphor and the theory are the same entry — `source_frame` is
the literal referent, `transfers` captures the relational structure, `grounding`
flags the epistemic status of the underlying claim.

```yaml
kind: metaphor
title: Broken Windows
source_frame: urban-disorder
applies_to: [community-management, software-maintenance, organizational-culture]
grounding: contested
transfers:
  - "[source] visible signs of neglect signal that norms are not enforced,
    inviting further norm violations"
  - "[source] disorder compounds: each unaddressed violation lowers the
    threshold for the next"
  - "[source] the first broken window is disproportionately costly because
    of what it signals about enforcement"
limits:
  - "[source] assumes visible disorder causes further disorder rather than
    both correlating with shared underlying causes — empirically contested"
  - "[source] prescriptive application tends to target visible poverty rather
    than root causes of disorder"
```

---

#### Type 5: Legal maxims

"Nemo dat quod non habet," "hard cases make bad law," "fruit of the poisonous
tree," "ignorance of the law is no excuse."

**Handling:** Where a live metaphorical source domain is present and
illuminating (`fruit of the poisonous tree`, `clean hands doctrine`), treat
as `metaphor` with `applies_to: [legal-reasoning]`. Where purely propositional
("ignorance of the law is no excuse"), treat as `paradigm`.

Most legal maxims that are tautological (nemo dat) get `grounding: proven` —
they're definitionally true within their system, not empirical claims.

---

## The `grounding` field

### Four values

| value | meaning |
|-------|---------|
| `proven` | Formally derived, mathematically necessary, or logically tautological. Not an empirical claim; cannot be overturned by a study. |
| `established` | Strong empirical grounding, well-replicated, accepted consensus in its domain. |
| `folk` | Practitioner tradition, widely believed and useful, limited or no formal testing. **The default — omit field to use.** |
| `contested` | Has real evidence or serious arguments on both sides. The debate is live and substantive. |

### Setting `grounding` — initial audit targets from import projects

| Entry | Grounding | Reason |
|-------|-----------|--------|
| Amdahl's Law | `proven` | Pure mathematics |
| CAP Theorem | `proven` | Formal proof |
| Nemo dat (legal maxim) | `proven` | Tautological within its system |
| Conway's Law | `established` | Well-studied across org types |
| Goodhart's Law | `established` | Well-observed across economics, policy, management |
| Loss Aversion | `established` | Hundreds of replications |
| Hawthorne Effect | `established` | Accepted even if magnitude debated |
| Gall's Law | `contested` | Compelling but essentially unfalsifiable |
| Broken Windows Theory | `contested` | Criminology data cuts both ways |
| Dunning-Kruger Effect | `contested` | Replicated but methodology disputed |
| The Lindy Effect | `contested` | Intuitively compelling, not rigorously tested |
| The Peter Principle | `contested` | Observed pattern, not experimentally established |
| Most aphorisms | (omit) | Default `folk` |
| Military maxims | (omit) | Default `folk` |
| Surgical aphorisms | (omit) | Default `folk` |

### Effect on tool layer

`get_mapping` includes `grounding` in its response. An agent retrieving
Broken Windows Theory to reason about code quality sees `contested` and can
hedge accordingly. An agent retrieving Amdahl's Law for capacity planning
sees `proven` and can cite it with confidence.

---

## The discard filter

Every import playbook must include this filter. An item is discarded if:

1. **No `transfers` possible:** Cannot generate at least 2 relational
   propositions that transfer beyond the origin domain. Pure domain vocabulary
   (table draft, producer note, NIMS codes) fails.

2. **No structural content:** A fact, a definition, or a proper noun with no
   relational structure. "Mise en place is a French culinary term" fails.
   "Mise en place encodes that preparation is itself the work" passes.

3. **Purely evaluative:** "This is good / bad" without a structural claim.
   Some aphorisms fail this test.

4. **Duplicate:** Direct expression of an entry already in the catalog.
   Check before adding.

Items that fail the filter are filed as `nugget` issues for later human
consideration — not silently dropped.

---

## Updated contributor decision table

| The item... | Kind | `grounding` |
|------------|------|-------------|
| Maps one domain onto another | `metaphor` | usually `folk` |
| Term whose origin is forgotten but structure is recoverable | `metaphor` + `dead: true` | usually `folk` |
| Narrative or character universal | `archetype` | usually `folk` |
| Structural solution to a recurring design problem | `pattern` | usually `folk` |
| Philosophy or position operating within domains | `paradigm` | usually `folk` |
| Operational rule or design principle | `paradigm` | `folk` or `established` |
| Legal maxim — propositional | `paradigm` | often `proven` |
| Legal maxim — with live metaphorical source | `metaphor` | usually `proven` or `folk` |
| Cross-domain cognitive move or technique | `mental-model` | usually `folk` |
| Named empirical regularity / predictive lens | `mental-model` (predictive) | `established` or `contested` |
| Razor (decision rule for underdetermination) | `mental-model` | `folk` |
| Named psychological or social effect | `mental-model` (predictive) | `established` or `contested` |
| Cannot generate 2+ `transfers` propositions | **Discard** — file as `nugget` | — |

---

## Summary of additions to schema kaizen

1. **`grounding` field** — `proven | established | folk | contested`.
   Default `folk` (field may be omitted). Add to schema spec, validator,
   CONTRIBUTING.md, and MCP tool response.

2. **Predictive mental-model subtype** — document in contributor guide with
   examples of Conway's Law, Goodhart's Law showing "[law] predicts..." form.

3. **Discard filter** — explicit criteria in every import playbook.
   Failed items → `nugget` issues, not the bin.

4. **Theory-named-after-metaphor pattern** — Broken Windows, Butterfly Effect:
   one entry, `source_frame` is the literal referent, `grounding` usually
   `contested` or `folk`.
