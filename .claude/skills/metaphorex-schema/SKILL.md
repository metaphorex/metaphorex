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

|  | **Source active** | **Source dormant** |
|---|---|---|
| **Specific A→B** | `conceptual-metaphor` | `dead-metaphor` |
| **Generative/meta** | `archetype` | `paradigm` |

- `conceptual-metaphor` — specific A→B mapping where source domain is still active in people's minds (ARGUMENT IS WAR, CREATIVE PROCESS IS GARDENING)
- `dead-metaphor` — specific mapping where source domain is forgotten or invisible; the word has become pure jargon. Value is *reactivating* the buried image. (bottleneck, firewall, bug, daemon-process, technical-debt)
- `archetype` — generative structural pattern appearing across 3+ independent target domains. Not one A→B but a recurring motif. (The Trickster, The Commons, The Facade Pattern, The Observer Pattern)
- `paradigm` — meta-level foundational frame that shapes how entire fields think. Removing it would collapse a field's vocabulary. (survival of the fittest, data flow is fluid flow)

### Kind Decision Heuristics

**Don't default to `conceptual-metaphor`.** Work through these tests in order:

1. **Dead-metaphor test:** Would a newcomer need the source domain *explained*
   to them? If they use the term without picturing the source — if "bug" is
   just a word, not an insect — it's `dead-metaphor`. Most software jargon
   that originated as metaphor has died: bug, daemon, zombie process, race
   condition, code smell, spaghetti code, cargo cult, yak-shaving.

2. **Archetype test:** Does this structural pattern recur across 3+ unrelated
   target domains? GoF design patterns are almost all archetypes — the Facade
   principle (simplify a complex interface) appears in architecture, API
   design, organizational structure, and diplomacy. That's not one metaphor,
   it's a recurring structural motif.

3. **Paradigm test:** Would removing this metaphor collapse an entire field's
   vocabulary? If an industry would need to reinvent its language, it's a
   paradigm. "Data flow is fluid flow" is load-bearing for Unix philosophy,
   streaming architectures, and functional programming.

4. **If none of the above:** It's `conceptual-metaphor` — a specific,
   living A→B mapping where people still actively experience the source
   domain. ARGUMENT IS WAR qualifies because arguers genuinely feel
   combative tension.

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
