# Kaizen: Schema overhaul for structural similarity + vector search
## Closes: #899 (mental models / frame-free entries)

---

## The core change in one sentence

Replace `target_frame` with `applies_to[]`, add `transfers` + `limits` + `grounding`, and consolidate to 5 kinds — so every entry is queryable by relational structure rather than topic.

---

## Why

Standard embedding search clusters PIPELINE with RIVER because they share a topic. It should cluster PIPELINE with ASSEMBLY LINE and DIGESTIVE SYSTEM — because those share relational structure (sequential stages, upstream blockage propagation, no memory of prior contents). The catalog needs to encode *why* a mapping works, not just *that* it exists.

The theoretical grounding is Gentner's Structure Mapping Engine (1983): analogical reasoning transfers *relational systems*, not surface attributes. `transfers` is a natural-language encoding of exactly what SME formalizes — we get the benefit without the formalism overhead. The embedding model already understands natural-language propositions; we just need to write them.

---

## Field changes

### `target_frame` → `applies_to: list[str]`

A list rather than a single value. In simple cases it's a list of one. For paradigms it may be several domains. For universally applicable entries (Inversion, Chesterton's Fence) it's omitted entirely — absence means universal applicability. For `mental-model` kind, `applies_to` is always absent by definition: a mental model that only applies to one domain is just a paradigm.

```yaml
# simple case — was: target_frame: software-architecture
applies_to: [software-architecture]

# paradigm with known domains
applies_to: [api-design, configuration-management, framework-design]

# universal entry — applies_to omitted entirely
```

### New fields: `transfers` and `limits`

Both are lists of natural-language propositions in `[source] ...` form. Both describe relational structure. `transfers` states what holds and carries over; `limits` states where the structure breaks. Symmetric names, identical format, embedded individually for vector search.

```yaml
# PIPELINE
transfers:
  - "[source] moves items in one direction only"
  - "[source] has discrete stages that transform items sequentially"
  - "[source] throughput is bounded by the slowest stage"
  - "[source] blockage at any stage propagates upstream"
  - "[source] items carry no memory of prior stages once passed"
  - "[source] individual stage capacity can be scaled independently"

limits:
  - "[source] assumes items are independent; feedback loops break the model"
  - "[source] assumes clear stage boundaries; fuzzy stages make capacity planning misleading"
  - "[source] misleads when applied to bidirectional or cyclical systems"
```

**What makes a good proposition:** Must be independently true of the source domain AND non-trivially false of topically-similar-but-structurally-different domains. For PIPELINE: "[source] involves flow" is useless — also true of RIVER. "[source] blockage propagates upstream" is good — false of rivers (rivers don't back up unless dammed; that's a different process), true of assembly lines, queues, bureaucratic approval chains.

**Proposition forms by kind:**

Metaphors, patterns, archetypes: `"[source] ..."`
Paradigms: `"[paradigm] ..."`
Mental models — cognitive move type: `"[model] reframes / instructs / approaches ..."`
Mental models — predictive type (named laws, effects): `"[law] predicts / implies / means that ..."`

The form signals the nature of the entry. The embedding model captures the semantic distinction.

### New field: `grounding`

Signals how much trust to place in the underlying claim before applying the entry as a reasoning tool.

| value | meaning | examples |
|-------|---------|---------|
| `proven` | Formally derived, mathematically necessary, or logically tautological. Cannot be empirically overturned because it's not an empirical claim. | Amdahl's Law (pure math), CAP theorem (formal proof), Nemo dat (tautological) |
| `established` | Strong empirical grounding, well-replicated, accepted consensus in its domain. A claim about the world with very strong support. | Conway's Law, loss aversion, Goodhart's Law |
| `folk` | Practitioner tradition, widely believed and useful, limited or no formal testing. **The default.** | Most aphorisms, most military maxims, Gall's Law, Parkinson's Law |
| `contested` | Has real evidence or serious arguments on both sides. The debate is live and substantive. | Broken Windows Theory, Dunning-Kruger Effect, the Lindy Effect |

**Default:** `folk`. The field may be omitted entirely; the validator assumes `folk`. Only `proven`, `established`, and `contested` require active editorial judgment to apply.

**Effect on tool layer:** The MCP `get_mapping` tool includes `grounding` in its response. An agent retrieving Broken Windows Theory to reason about code quality will see `contested` and can hedge accordingly.

---

## Kind taxonomy: 7 → 5

| kind | source_frame | applies_to | transfers | limits |
|------|-------------|------------|-----------|--------|
| `metaphor` | required | optional (absent = universal) | min 3 | min 2 |
| `pattern` | optional | optional | min 3 | min 2 |
| `archetype` | optional | optional | min 3 | min 2 |
| `paradigm` | optional | optional | min 2 | min 2 |
| `mental-model` | optional | **absent** | min 2 | min 2 |

`mental-model` is the only kind where `applies_to` is structurally absent rather than optional. A mental model that only applies to one domain is just a paradigm.

### What each kind covers

**`metaphor`** — one domain illuminating another via structural transfer. Includes cross-field mappings (which are just metaphors with specific frame names) and dead metaphors (`dead: true` flag). The most common kind.

**`pattern`** — a structural solution to a recurring design problem. Source frame is often thin or vestigial (Observer, Factory); the value is in the structural solution, not the domain of origin.

**`archetype`** — narrative or character universals (Hero, Scapegoat, Trickster, Ouroboros). Applies across cultures and contexts; `applies_to` usually absent.

**`paradigm`** — a philosophy or worldview with a position, operating within one or more domains. Operational rules, design principles, legal maxims, aphoristic prescriptions. You can agree or disagree with a paradigm within its domain. Examples: DRY, Convention over Configuration, Worse is Better, Deming's 14 Points.

**`mental-model`** — a cross-domain cognitive move or predictive lens with no inherent domain and no inherent position. Two subtypes, same kind:
- *Cognitive move* (Inversion, Second-Order Thinking, Hanlon's Razor): a technique for thinking differently
- *Predictive* (Conway's Law, Goodhart's Law, Dunning-Kruger Effect): an empirical regularity used as a forecasting tool

### Eliminations and folds

`cross-field-mapping` → `metaphor`. Identical schema and search behavior; specificity of frame names is sufficient distinction.

`dead-metaphor` → `metaphor` + `dead: true`. Dead metaphors have structural properties — the original live mapping's relational structure is what made the term stick. "Three sheets to the wind": "[source] excess of uncontrolled surface area produces erratic, uncoordinated motion." That proposition explains the etymology AND transfers to new domains. Dead entries with `transfers` are analytical tools; without them they're footnotes. Require `transfers` for all dead metaphors.

`mental-model` kept distinct from `paradigm`. A paradigm has a position (Convention over Configuration is an opinion about API design — you can disagree). A mental model is a technique or lens (Inversion has no domain and no opinion — it just instructs you to think backward). This distinction matters for how an agent uses the entry: paradigms are applied or rejected, mental models are performed.

### Decision criteria for contributors

- One domain illuminating another via structural transfer → `metaphor`
- Term whose origin is forgotten but structure is recoverable → `metaphor` + `dead: true`
- Narrative or character universal → `archetype`
- Structural solution to a recurring design problem → `pattern`
- Philosophy or worldview with a position, operating within domains → `paradigm`
- Operational rule, design principle, legal maxim → `paradigm`
- Cross-domain cognitive move or technique (performs a thinking operation) → `mental-model`
- Named empirical regularity used as a predictive lens → `mental-model` (predictive)
- Razor (decision rule for resolving underdetermination) → `mental-model`
- Cannot generate 2+ `transfers` propositions → **Discard**, file as `nugget`

---

## Full schema

```yaml
# Required for all kinds
title: string
kind: metaphor | pattern | archetype | paradigm | mental-model
transfers: list[str]      # min 3 for metaphor/pattern/archetype; min 2 for paradigm/mental-model
limits: list[str]         # min 2 for all kinds
expressions: list[str]    # specific phrases found in the wild

# Required for metaphor; optional for pattern, archetype, paradigm; absent for mental-model
source_frame: string

# Optional for metaphor, pattern, archetype, paradigm; absent for mental-model
# Omit entirely for universal entries
applies_to: list[str]

# Optional — defaults to folk if omitted
grounding: proven | established | folk | contested

# Optional
dead: bool                # metaphor kind only
categories: list[str]     # existing taxonomy, unchanged
related: list[str]        # slugs of related entries
```

---

## Implementation tasks

### Task 1: Validator + schema spec

Update CONTRIBUTING.md:
- Full schema spec with new fields and 5-kind taxonomy
- Decision criteria table (above)
- Proposition-writing guidelines with examples of all proposition forms
- `grounding` value definitions with examples

Update `scripts/validate.py`:
- Accept `applies_to` (list), reject `target_frame`
- Accept `transfers` (list), reject `structural_properties`
- Accept `limits` (list), reject `failure_conditions`
- Accept `grounding` enum: `proven | established | folk | contested`; default `folk` if absent
- Remove `cross-field-mapping` and `dead-metaphor` from allowed kinds
- Add `mental-model` to allowed kinds with `applies_to` forbidden (error if present)
- Enforce min proposition counts per kind per table above
- `dead: bool` optional field for `metaphor` kind only (error if present on other kinds)
- Lint warning when `dead: true` but `transfers` has fewer than 2 items

### Task 2: Migration script

One-shot migration across all catalog entries:

- `target_frame: x` → `applies_to: [x]`
- `structural_properties:` → `transfers:`
- `failure_conditions:` → `limits:`
- `kind: cross-field-mapping` → `kind: metaphor`
- `kind: dead-metaphor` → `kind: metaphor` + `dead: true`
- `kind: mental-model` → keep as `kind: mental-model` (now a first-class kind)
- Remove any `applies_to` from `mental-model` entries (structurally absent)
- Set `grounding:` to nothing (omit field; validator defaults to `folk`)

Run validator after migration. Zero errors is the target before proceeding.

### Task 3: Opus content pass

One Opus pass per entry generating `transfers` and `limits`. Run on 20 entries first; review before scaling.

**Generation prompt:**
```
You are building a structured metaphor knowledge base optimized for
structural similarity search.

ENTRY:
{full_entry_text}

Generate two lists:

transfers: 4-8 propositions in "[source] ..." form (or "[paradigm]",
"[model]", "[law]" as appropriate to the kind).

Each proposition must be:
- Independently true of the source domain
- Non-trivially false of at least two topically-similar but
  structurally-different domains (name those domains in a comment
  after the proposition to show your work)
- Relational, not attributive: "[source] connects X to Y via Z",
  not "[source] is large"

limits: 2-5 propositions in "[source] breaks when ..." or
"[source] misleads when ..." form.

Flag low confidence with a # low-confidence comment.
Output YAML only.
```

**Quality gate (second pass):** For each generated `transfers` proposition, ask: "Is this also true of three topically similar but structurally different domains?" If yes, the proposition is not discriminating enough — flag for revision. Run this critique on the first 20 entries before scaling.

### Task 4: Audit existing paradigm and mental-model entries

For each current `kind: paradigm` entry:
- Evaluate whether `source_frame` is genuine or was forced in by the old validator
- If forced/artificial: remove it; `transfers` carries the semantic weight
- If genuine (survival-of-the-fittest has a real evolutionary biology source): keep it, add `transfers`

For each entry that should be `mental-model`:
- Confirm `applies_to` is absent
- Confirm `transfers` uses appropriate predictive or procedural proposition form

### Task 5: Set `grounding` on entries that need it

Entries with non-`folk` grounding need explicit editorial judgment. Initial audit targets:

| Entry | Likely grounding |
|-------|-----------------|
| Amdahl's Law | `proven` |
| CAP Theorem | `proven` |
| Conway's Law | `established` |
| Goodhart's Law | `established` |
| Loss Aversion | `established` |
| Broken Windows Theory | `contested` |
| Dunning-Kruger Effect | `contested` |
| The Lindy Effect | `contested` |
| Gall's Law | `contested` |
| Most aphorisms | (omit — defaults to `folk`) |

---

## What not to do

**Don't formalize propositions into predicates.** `has_property(pipeline, upstream_blocking)` loses the semantic richness that makes embedding useful. The model understands "blockage propagates upstream" across dozens of domains — you ride that for free.

**Don't enumerate `applies_to` exhaustively for broad paradigms.** If scope is genuinely unclear, omit the field. Chasing completeness produces noise.

**Don't skip the quality gate on the Opus pass.** Bad `transfers` propositions produce confident wrong results in vector search. Twenty entries reviewed before scaling saves significant rework.

**Don't add `applies_to` to `mental-model` entries.** The validator will reject it. A mental model that needs `applies_to` is a paradigm.
