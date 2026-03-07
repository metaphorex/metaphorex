# Content Schema Design

Date: 2026-03-07

## Overview

Metaphorex is a markdown-first knowledge graph of metaphors, mental models,
and conceptual mappings. Content lives in plain markdown files with YAML
frontmatter, readable as-is on GitHub by humans and agents. No static site
generator required.

## Terminology

- **Mapping** — the main content unit. A conceptual metaphor, design pattern,
  archetype, or cross-field mapping between a source and target domain.
- **Expression** — a specific instance of a mapping, listed within the mapping's
  body. "The server is choking" is an expression of PROGRAM FAILURE IS BODILY
  FAILURE.
- **Frame** — a conceptual domain (e.g., "war", "bodily failure", "marine
  biology"). Frames have roles and structure independent of any single mapping.
- **Category** — a SKOS-style taxonomy label for cross-cutting classification.

## Directory Structure

```
catalog/
  mappings/         # flat, one .md per mapping
  frames/           # flat, one .md per frame
  categories/       # flat, one .md per category
scripts/
  validate.py       # frontmatter + body validation + JSON extraction
docs/
  plans/            # design docs
CONTRIBUTING.md
LICENSE
README.md
```

Mappings are flat (not grouped by domain). Categories are tags in frontmatter.
If the repo exceeds ~200 mappings, we can introduce category subdirectories
with a straightforward file move (git preserves history across renames).

## Mapping Schema

### Frontmatter

```yaml
---
slug: program-failure-is-bodily-failure
name: "Program Failure Is Bodily Failure"
kind: conceptual-metaphor
source_frame: bodily-failure
target_frame: software-programs
categories:
  - software-engineering
  - cognitive-science
author: fshot
contributors: []
related: []
---
```

Fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| slug | string | yes | URL-safe identifier, matches filename |
| name | string | yes | Human-readable title |
| kind | enum | yes | conceptual-metaphor, design-pattern, archetype, cross-field-mapping, dead-metaphor, paradigm |
| source_frame | string | yes | Slug of the source frame |
| target_frame | string | yes | Slug of the target frame |
| categories | string[] | yes | Category slugs (at least one) |
| author | string | yes | GitHub username or agent:<name> |
| contributors | string[] | no | Additional contributors |
| related | string[] | no | Slugs of related mappings |
| deprecated | boolean | no | Only present when true |

No `status` field. The PR workflow handles lifecycle:
open PR = proposed, draft PR = draft, merged = published.
`deprecated: true` is added when a mapping is superseded.

### Body Sections

```markdown
## What It Brings
The structural parallels that make this mapping useful.

## Where It Breaks
The limits — where the metaphor misleads or stops being useful.

## Expressions
- "expression here" — brief annotation

## Origin Story
Optional. Where this mapping comes from, who popularized it.

## References
Optional. Sources, citations, further reading.
```

Required sections: What It Brings, Where It Breaks, Expressions.
Optional sections: Origin Story, References.
Section order is conventional, enforced by validator.

## Frame Schema

### Frontmatter

```yaml
---
slug: bodily-failure
name: "Bodily Failure"
broader: embodied-experience
related: []
roles:
  - sufferer
  - symptom
  - cause
  - recovery
---
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| slug | string | yes | URL-safe identifier, matches filename |
| name | string | yes | Human-readable title |
| broader | string | no | Parent frame slug (hierarchy) |
| related | string[] | no | Related frame slugs |
| roles | string[] | yes | Structural roles within this frame |

### Body

Freeform markdown describing the frame — what it encompasses, key concepts,
why it's a useful source or target domain.

## Category Schema

### Frontmatter

```yaml
---
slug: cognitive-science
name: "Cognitive Science"
broader: science
related:
  - psychology
  - linguistics
---
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| slug | string | yes | URL-safe identifier, matches filename |
| name | string | yes | Human-readable label |
| broader | string | no | Parent category slug (SKOS broader) |
| related | string[] | no | Related category slugs |

### Body

Optional definition or scope description.

## Validator / Extractor

Single Python script (`scripts/validate.py`), runnable via:

```bash
uvx --with python-frontmatter --with mistune scripts/validate.py
```

Two modes:
- `validate` — checks frontmatter schema, required sections, cross-references
  (frame/category/related slugs resolve to real files). Exit 1 on failure.
- `extract` — emits structured JSON (one object per mapping with frontmatter +
  parsed body sections) to stdout. For downstream SQLite/pgvector importers.

## Attribution Model

- **License requirement**: credit "Metaphorex" with link to repo (project-level).
- **Per-entry**: `author` and `contributors` in frontmatter (encouraged norm,
  not a license obligation for downstream consumers).
- **Immutable record**: git history.

## Licensing

CC BY-SA 4.0. See LICENSE and CONTRIBUTING.md.
