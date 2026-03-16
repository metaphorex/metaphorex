# Metaphorex

Markdown-first knowledge graph of metaphors — conceptual metaphors, design
patterns, archetypes, and cross-field mappings. GitHub is the CMS: PRs are
drafts, merged = published. Licensed CC BY-SA 4.0 (content), MIT (code).

## Build & Validate

```bash
uv run scripts/validate.py validate   # zero-install, PEP 723 inline deps
```

Zero warnings, zero errors is the precedent. Fix all issues before merging.

## Directory Structure

```
catalog/           # Content: mappings/, frames/, categories/
playbooks/         # Import project playbooks, scripts, manifests
site/              # Astro site (metaphorex.org)
scripts/           # Validation, survey, utilities
.claude/           # Agent suite: agents/, commands/, skills/
docs/              # Design docs and plans
```

## Content Schema

Entries live in `catalog/mappings/<slug>.md` with YAML frontmatter:

```yaml
slug: argument-is-war          # kebab-case, matches filename
name: Argument Is War           # human-readable
kind: metaphor                  # metaphor | pattern | archetype | paradigm | mental-model
source_frame: war               # required for metaphor; optional for others
applies_to: [argumentation]     # optional; absent for mental-model
categories: [cognitive-linguistics]
author: lakoff-johnson
contributors: []
related: []
created: 2026-03-07             # ISO date, set on first creation
updated: 2026-03-10             # ISO date, updated on each edit
grounding: folk                  # proven | established | folk | contested (default: folk)
```

Required body sections: **Transfers**, **Limits**, **Expressions**.
Optional: Origin Story, References.

"Limits" is the most important section — never a throwaway.

Frames (`catalog/frames/`) have: slug, name, roles[], broader?, related[].
Categories (`catalog/categories/`) have: slug, name, broader?, related[].

## Architecture Principles

- **GitHub is the system of record.** All data (content, costs, pipeline status)
  is pulled from GitHub APIs or the catalog filesystem at query time. No local
  state files, no append-only logs, no loose JSON in the repo.
- **No external dependencies until unavoidable.** No databases, no SaaS dashboards,
  no third-party analytics. If GitHub can't answer the question, reconsider the
  question before reaching for a new dependency.

## Key Conventions

- Slug-based filenames: `catalog/mappings/argument-is-war.md`
- Flat directories (no subdirs until 200+ entries)
- Entries must include their frames in the same PR (validator enforces)
- Frames are cheap (create freely), categories are expensive (taxonomy decisions)
- New entries branch from main: `mine/<project>/<slug>` or `add/<slug>`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
