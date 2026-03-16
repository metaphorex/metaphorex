---
name: metaphorex-schema
description: Use when creating, editing, or validating Metaphorex content — entries, frames, or categories. Provides the canonical schema, frontmatter spec, body section conventions, and tone guide.
version: 1.0.0
---

# Metaphorex Content Schema

You are working with content for the Metaphorex project — a markdown-first
knowledge graph of metaphors at https://github.com/metaphorex/metaphorex.

## Terminology

- **Entry** — the main content unit. A conceptual metaphor, archetype,
  dead metaphor, or paradigm linking a source and target domain.
- **Expression** — a specific instance of an entry (e.g., "the server is
  choking" is an expression of PROGRAM FAILURE IS BODILY FAILURE).
- **Frame** — a conceptual domain with structural roles.
- **Category** — a SKOS-style taxonomy label.

## Entry Frontmatter

```yaml
---
slug: kebab-case-name          # must match filename
name: "Human Readable Name"
kind: metaphor                  # see valid kinds below
source_frame: frame-slug        # required for metaphor; optional for others
applies_to:                     # optional; absent for mental-model
  - frame-slug                  # must exist in catalog/frames/
categories:                     # at least one, must exist in catalog/categories/
  - category-slug
author: github-username          # or agent:<agent-name>
contributors: []
related: []
grounding: folk                  # proven | established | folk | contested (default: folk, may omit)
dead: true                       # optional, metaphor kind only
---
```

### Valid Kinds

- `metaphor` — specific A→B metaphor where the source domain illuminates the target. Includes dead metaphors (`dead: true`) where the source is forgotten but structurally recoverable. `source_frame` required.
- `pattern` — structural solution to recurring design problem. Source frame often thin/vestigial. `source_frame` optional.
- `archetype` — narrative or character universal across 3+ domains. `source_frame` optional.
- `paradigm` — philosophy or worldview with a position, operating within domains. You can agree or disagree. `source_frame` optional.
- `mental-model` — cross-domain cognitive move or predictive lens. No inherent domain, no inherent position. Two subtypes: cognitive moves (Inversion) and predictive laws (Conway's Law). `source_frame` optional. `applies_to` must be absent.

### Kind Decision Heuristics

| The item... | Kind |
|------------|------|
| Maps one domain onto another | `metaphor` |
| Term whose origin is forgotten but structure is recoverable | `metaphor` + `dead: true` |
| Narrative or character universal | `archetype` |
| Structural solution to a recurring design problem | `pattern` |
| Philosophy or position operating within domains | `paradigm` |
| Operational rule, design principle, legal maxim | `paradigm` |
| Cross-domain cognitive move or technique | `mental-model` |
| Named empirical regularity / predictive lens | `mental-model` |
| Razor (decision rule for underdetermination) | `mental-model` |
| Cannot generate 2+ structural propositions | **Discard** — file as nugget |

### Grounding

Signals epistemic status. Defaults to `folk` if omitted.

| Value | Meaning |
|-------|---------|
| `proven` | Formally derived, mathematically necessary, or tautological |
| `established` | Strong empirical grounding, well-replicated, accepted consensus |
| `folk` | Practitioner tradition, limited formal testing. **Default** |
| `contested` | Real evidence on both sides, live debate |

### No status field

PR workflow handles lifecycle: open PR = proposed, merged = published.
Only add `deprecated: true` when an entry is superseded.

## Entry Body Sections

Required (in this order):

### ## Transfers
The structural parallels that make this entry useful. Be specific about
what maps to what. Use bold bullet points for key parallels.

### ## Limits
**The most important section.** Where the metaphor misleads, what it hides,
where the structural analogy fails. This is not a formality — it's what
makes Metaphorex more than a list.

### ## Expressions
Specific phrases found in real usage. Format:
```markdown
- "expression here" — brief annotation explaining the metaphorical origin
```

Optional:

### ## Origin Story
Where this concept comes from, who popularized it, how it evolved.

### ## References
Sources, citations, further reading. Use standard citation format.

### Proposition Writing (for transfers and limits)

When creating entries, include `transfers` and `limits` in frontmatter as structured proposition lists. These are embedded individually for vector search.

**Form by kind:**

| Kind | Prefix | Example |
|------|--------|---------|
| `metaphor`, `pattern`, `archetype` | `[source]` | `[source] blockage propagates upstream` |
| `paradigm` | `[paradigm]` | `[paradigm] simplicity is preferred over correctness` |
| `mental-model` (cognitive) | `[model]` | `[model] reframes by asking what guarantees failure` |
| `mental-model` (predictive) | `[law]` | `[law] predicts systems mirror org structure` |

Each proposition must be:
- Independently true of the source domain
- Non-trivially false of 2+ topically-similar but structurally-different domains
- Relational, not attributive: "[source] connects X to Y via Z", not "[source] is large"

Minimum counts: 3 transfers for metaphor/pattern/archetype, 2 for paradigm/mental-model. 2 limits for all kinds.

## Frame Frontmatter

```yaml
---
slug: frame-slug
name: "Frame Name"
broader: parent-frame-slug      # optional, for hierarchy
related: []                      # optional
roles:                           # required — structural roles in this domain
  - role-name
---
```

Body: 2-4 sentences describing what makes this frame interesting as a
source or target domain.

## Category Frontmatter

```yaml
---
slug: category-slug
name: "Category Name"
broader: parent-category-slug    # optional
related: []                      # optional
---
```

Body: 1-2 sentence scope description.

## Frame & Category Upsert Rule

If your entry references frames or categories that don't exist, create
them in the same PR. Frames are cheap (create freely). Categories are
expensive (affect the whole taxonomy — think before adding).

## Tone Guide

Read the seed entries in the content repo for reference. The tone is:

- **Clear and direct** (Orwell) — no jargon for its own sake
- **Structurally rigorous** (Knuth) — precise about what maps and what doesn't
- **Generative** (Eno) — each entry should make you think of three more
- **Grounded in real use** (Steinbeck) — expressions from actual humans
- **Slightly irreverent** — serious about structure, not about propriety

## Validation

Run before submitting: `uv run scripts/validate.py validate`

Errors block merge. Warnings (dangling broader/related refs) should be
resolved — the seed set has zero warnings as precedent.
