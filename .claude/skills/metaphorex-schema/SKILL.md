---
name: metaphorex-schema
description: Use when creating, editing, or validating Metaphorex content — mappings, frames, or categories. Provides the canonical schema, frontmatter spec, body section conventions, and tone guide.
version: 1.0.0
---

# Metaphorex Content Schema

You are working with content for the Metaphorex project — a markdown-first
knowledge graph of metaphors at https://github.com/metaphorex/metaphorex.

## Terminology

- **Mapping** — the main content unit. A conceptual metaphor, archetype,
  dead metaphor, or paradigm linking a source and target domain.
- **Expression** — a specific instance of a mapping (e.g., "the server is
  choking" is an expression of PROGRAM FAILURE IS BODILY FAILURE).
- **Frame** — a conceptual domain with structural roles.
- **Category** — a SKOS-style taxonomy label.

## Mapping Frontmatter

```yaml
---
slug: kebab-case-name          # must match filename
name: "Human Readable Name"
kind: conceptual-metaphor       # see valid kinds below
source_frame: frame-slug        # must exist in catalog/frames/
target_frame: frame-slug        # must exist in catalog/frames/
categories:                     # at least one, must exist in catalog/categories/
  - category-slug
author: github-username          # or agent:<agent-name>
contributors: []                 # people/agents who made substantial edits
related: []                      # slugs of related mappings
---
```

### Valid Kinds (2x2 grid)

Four kinds along two axes — **specific vs generative** and **source active vs dormant**:

- `conceptual-metaphor` — specific A→B mapping where source domain is still active in people's minds (ARGUMENT IS WAR)
- `archetype` — generative pattern appearing across many A→B pairs (The Trickster, The Commons)
- `dead-metaphor` — specific mapping where source domain is forgotten; value is reactivating it (bottleneck, firewall)
- `paradigm` — meta-level foundational frame that shapes how entire fields think (survival of the fittest)

Previously `design-pattern` and `cross-field-mapping` existed but were removed:
design-pattern is just a conceptual-metaphor with provenance (the GoF book
named it; that doesn't change its graph structure), and cross-field-mapping
collapsed into conceptual-metaphor because the conscious/unconscious
distinction didn't hold in practice.

### No status field

PR workflow handles lifecycle: open PR = proposed, merged = published.
Only add `deprecated: true` when a mapping is superseded.

## Mapping Body Sections

Required (in this order):

### ## What It Brings
The structural parallels that make this mapping useful. Be specific about
what maps to what. Use bold bullet points for key parallels.

### ## Where It Breaks
**The most important section.** Where the metaphor misleads, what it hides,
where the structural analogy fails. This is not a formality — it's what
makes Metaphorex more than a list.

### ## Expressions
Specific phrases found in real usage. Format:
```markdown
- "expression here" — brief annotation explaining the mapping
```

Optional:

### ## Origin Story
Where this mapping comes from, who popularized it, how it evolved.

### ## References
Sources, citations, further reading. Use standard citation format.

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

If your mapping references frames or categories that don't exist, create
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
