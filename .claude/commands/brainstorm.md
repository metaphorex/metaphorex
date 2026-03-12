---
name: brainstorm
description: Structure brainstorming for new Metaphorex import projects or pipeline features
---

You are running a structured brainstorm session for the Metaphorex project.
The user will describe an idea — your job is to explore it, stress-test it
against the taxonomy, and produce actionable output.

## Determine brainstorm type

Ask only if unclear. Two modes:

1. **Import project** (new catalog content) — default, higher priority
2. **Pipeline feature** (agent swarm, product, tooling)

For pipeline features, defer to the general `superpowers:brainstorming` skill
and add Metaphorex context. The rest of this command focuses on import projects.

## Import project brainstorm

### Phase 1 — Expand the idea

Start with what the user gave you. Then:

- **Research prior art.** Use WebSearch to find structured archives, academic
  catalogs, existing collections, blog posts, books, and conference talks
  related to the topic. Cite what you find.
- **Generate adjacent candidates.** What related metaphors, archetypes, or
  patterns does this topic surface? Cast a wide net.
- **Identify primary texts.** Who wrote about this first? What are the
  canonical references?

### Phase 2 — Triage into the taxonomy

For each candidate, determine:

| Field | Question |
|-------|----------|
| **Fits as mapping?** | Does it have a clear source→target structure? |
| **Kind** | Apply the 4-kind heuristics: dead-metaphor → archetype → paradigm → conceptual-metaphor |
| **Source frame** | What's the source domain? Does a frame already exist in `catalog/frames/`? |
| **Target frame** | What's the target domain? |
| **Category** | Which existing category fits? Need a new one? |
| **Already in catalog?** | Check `catalog/mappings/` for duplicates or related entries |
| **Belongs elsewhere?** | Is this not actually a metaphor? Is it a framework, a taxonomy, a literal description? |

Present this as a table. Be honest about what doesn't fit — not everything
is a mapping, and that's fine.

### Phase 3 — Scope the project

Based on the triage:

- **Project type**: archive (finite list) or vein (ongoing direction)?
- **Estimated scope**: how many mappings? How many new frames/categories?
- **Source methodology**: are there structured archives to scrape, or is this
  primarily LLM-sourced territory?
- **Priority assessment**: how time-sensitive is this? Is the discourse active
  and evolving? Does our catalog have a gap here?
- **Dependencies**: does this overlap with existing import projects? Would
  certain entries be better as nuggets?

### Phase 4 — Propose next steps

Output one of:

1. **Create an import-project issue** — provide the title, type (archive/vein),
   body text, and recommended labels (including `priority:high` if warranted).
   Ask the user if they want you to create it now.
2. **Create nugget issues** — if the idea breaks down into a few standalone
   entries rather than a project.
3. **Park it** — if the idea needs more research or doesn't fit the catalog
   well. Explain why and what would change your mind.

## Output format

Use tables and structured lists, not walls of text. The user should be able
to scan the output and make decisions quickly.
