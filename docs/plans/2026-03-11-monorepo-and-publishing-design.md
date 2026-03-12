# Monorepo and Publishing Design

Date: 2026-03-11

## Overview

Consolidate the agents repo (metaphorex/agents) into the content repo
(metaphorex/metaphorex) as a monorepo. Add a static website at metaphorex.org
and a Bun CLI tool. Establish versioning, workspace conventions, and new
commands for continuous improvement.

## 1. Repo Consolidation

### Why

The agents repo exists to operate on the content repo. Keeping them separate
creates friction: playbooks describe content extraction but live in a different
repo; issues and PRs split across two repos; the agents repo maintains a local
`content-repo/` checkout to function. One repo eliminates all of this.

### How

Merge the agents repo history into the monorepo using a plain merge (not
subtree — no metadata quirks):

```bash
git remote add agents git@github.com:metaphorex/agents.git
git fetch agents
git merge agents/main --allow-unrelated-histories --no-commit
# git mv files into their target locations
git commit -m "Merge agents repo history into monorepo"
git remote remove agents
```

Full commit history is preserved. `git log -- .claude/` works after the merge.

### Directory Layout (Post-Consolidation)

```
metaphorex/
├── catalog/                      # content: mappings, frames, categories
│   ├── mappings/
│   ├── frames/
│   └── categories/
├── playbooks/                    # extraction playbooks (from agents repo)
│   ├── design-patterns/
│   └── lakoff-johnson-mwlb/
├── site/                         # Astro static site
│   ├── src/
│   │   ├── content/ -> ../../catalog   # symlink to catalog
│   │   ├── layouts/
│   │   └── pages/
│   ├── astro.config.ts
│   └── package.json
├── cli/                          # Bun CLI (deferred)
│   ├── src/
│   └── package.json
├── scripts/                      # Python build/validation scripts
│   ├── validate.py
│   ├── stats.py
│   └── survey.py
├── .claude/                      # agents, commands, skills (dissolved plugin)
│   ├── agents/
│   ├── commands/
│   ├── skills/
│   └── settings.json
├── .github/
│   ├── workflows/
│   │   ├── validate.yml          # on PR — fast, Python
│   │   ├── deploy-site.yml       # nightly + manual dispatch
│   │   └── build-artifact.yml    # nightly + manual dispatch (deferred)
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE/
├── docs/plans/
├── AGENTS.md                     # vendor-neutral instructions
├── CLAUDE.md -> AGENTS.md        # symlink for Claude Code
├── CONTRIBUTING.md
├── LICENSE                       # CC BY-SA 4.0 (content default)
└── README.md
```

### License

- `catalog/`, `playbooks/`: CC BY-SA 4.0 (existing LICENSE at root)
- `site/`, `cli/`, `scripts/`, `.claude/`: MIT (per-directory LICENSE files)

### Post-Merge Cleanup

- Archive metaphorex/agents on GitHub (read-only, link to monorepo in README)
- Update any cross-repo references in agent prompts (content-repo/ paths, etc.)
- Remove the `content-repo/` local checkout hack from agent workflows

## 2. Static Site

### Stack

- **Astro** (static mode) — Content Collections with Zod schema validation,
  `reference()` for cross-refs, zero client JS
- **Pagefind** — post-build client-side search (~50KB index for current corpus)
- **GitHub Pages** — free hosting, custom domain metaphorex.org
- **llms.txt** — auto-generated at build time

### Content Collections

Astro Content Collections read from `site/src/content/` (symlinked to
`catalog/`). Zod schemas in `site/src/content.config.ts` mirror the existing
`validate.py` rules:

- Mappings: slug, name, kind (enum), source_frame (reference), target_frame
  (reference), categories (reference[]), author, contributors, related
- Frames: slug, name, broader (optional), related, roles
- Categories: slug, name, broader (optional), related

Cross-references validated at build time by Astro. The Python validator
remains the CI gate on PRs; Astro catches the same issues at site build.

### Pages

- `/` — homepage with corpus stats, recent additions, search
- `/mappings/` — browsable list, filterable by kind/category
- `/mappings/[slug]/` — single mapping with resolved frame links, related
  mappings, expressions
- `/frames/` — list of frames
- `/frames/[slug]/` — single frame with reverse lookup ("mappings using this
  frame")
- `/categories/` — list of categories
- `/categories/[slug]/` — single category with member mappings
- `/llms.txt` — structured index for LLM crawlers
- `/llms-full.txt` — full content inlined

### Search

Pagefind runs as a post-build step: `astro build && pagefind --site dist`.
Index includes mapping names, body text, and frontmatter metadata surfaced
via `data-pagefind-meta` attributes (kind, source_frame, target_frame).

### Deployment

GitHub Actions workflow (`deploy-site.yml`):

```yaml
on:
  schedule:
    - cron: "0 4 * * *"   # nightly at 4am UTC
  workflow_dispatch: {}     # manual trigger for demos
```

Steps: checkout -> install Bun -> `cd site && bun install && bun run build` ->
`pagefind --site dist` -> deploy to GitHub Pages.

Custom domain: CNAME record for `metaphorex.org` -> GitHub Pages.

### llms.txt

Generated as an Astro page (`site/src/pages/llms.txt.ts`) that iterates
all collections and outputs structured markdown:

```markdown
# Metaphorex

> A knowledge graph of metaphors — how we borrow structure from one domain
> to understand another.

## Mappings (132)

- [Argument Is War](https://metaphorex.org/mappings/argument-is-war):
  We structure arguments using war concepts — attacking positions, defending
  claims, winning debates.
...

## Frames (53)
...

## Categories (11)
...
```

`llms-full.txt` inlines the full body of each mapping. At current corpus
size (~200 files), this is well under 500KB — fits in any context window.

## 3. CLI (Deferred)

### Stack

- **Bun** runtime + `bun build --compile` for single-binary distribution
- **bun:sqlite** with sqlite-vec extension for FTS5 + vector search
- **Commander.js** for command structure
- **@modelcontextprotocol/sdk** for MCP server mode

### Commands (Planned)

```
m4x search "war argument"           # FTS query
m4x similar "argument-is-war"       # vector KNN
m4x get argument-is-war             # full entry as JSON
m4x list --kind conceptual-metaphor
m4x schema                          # describe available fields
m4x mcp                             # start as MCP server on stdio
```

JSON output by default (agents are the primary consumer). `--pretty` for humans.

### Artifact

Nightly GitHub Action builds `metaphorex.db` from `catalog/` source:
1. Parse markdown + YAML frontmatter
2. Insert into SQLite tables (mappings, frames, categories, expressions)
3. Enable FTS5 on text fields
4. Generate embeddings with `all-MiniLM-L6-v2` (via API at build time)
5. Store vectors in sqlite-vec `vec0` table
6. Upload to GitHub Release (`nightly` tag, overwritten each build)

Browsable via datasette-lite: `https://lite.datasette.io/?url=<release-url>`

## 4. Versioning

### Two Tracks

| Track | Scheme | What it versions | Where it's stamped |
|-------|--------|------------------|--------------------|
| **Corpus** | CalVer `YYYY.MM.DD` | The content archive | llms.txt header, site footer, SQLite metadata, CLI `--version`, GitHub Release tag |
| **Agent suite** | SemVer `0.x.y` | Agent prompts, commands, skills, pipeline logic | Stats blocks on issues/PRs, Co-Authored-By trailers, `.claude/VERSION` |

### Corpus CalVer

The date of the nightly build. No subjective major/minor decisions. Freshness
is immediately visible. Matches conventions in computational linguistics
corpus releases (WordNet, FrameNet).

When manual dispatch is used intra-day: `YYYY.MM.DD+N` (build number suffix).

### Agent Suite SemVer

- **Major**: pipeline redesign, breaking changes to agent contracts
- **Minor**: new agent, new command, significant prompt changes
- **Patch**: prompt tweaks, bugfixes, formatting changes

Single source of truth: `.claude/VERSION` file. Agents read it at startup
and include it in their stats blocks:

```markdown
## stats:miner/0.1.0:claude-opus-4
- tokens_in: 45000
- tokens_out: 12000
- runtime_s: 120
- usd: 0.85
```

Co-Authored-By trailers include version:
`Co-Authored-By: metaphorex-miner/0.1.0 <miner@metaphorex.org>`

## 5. Workspace Model

### Two Clones, Two Purposes

| Workspace | Location | Purpose | Who works here |
|-----------|----------|---------|----------------|
| **Workshop** | `~/code/fshot/metaphorex` | Design, brainstorm, write docs, tweak agent prompts, build site/CLI | Human (you) |
| **Factory** | `~/code/metaphorex-factory/metaphorex` | Run `/work`, `/mine`, `/prospect`. Agents create worktrees as needed. | Agents (you observe) |

Workshop stays on `main` or short-lived branches. Factory agents create
worktrees off `main` for each work unit, push branches, open PRs.

### Information Bridge: Factory -> Workshop

When you observe issues during Factory sessions:

1. **`/debrief`** command — extracts observations from the current Factory
   conversation, drafts a GitHub issue with context, examples, and proposed
   fixes. You review and file.
2. Issues become the unit of work that crosses the boundary.
3. Workshop picks up issues and implements fixes.

### Information Bridge: Workshop -> Factory

Agent prompt changes merged to main are picked up by Factory agents on their
next `git pull` (agents pull from main before starting work).

## 6. New Commands

### /debrief

**Purpose**: Extract observations from a Factory session into a GitHub issue.

**Behavior**: Analyzes conversation context, identifies friction points,
agent quality issues, and pipeline problems. Drafts a structured issue:

```markdown
## Observation
[What was noticed]

## Examples
[Specific PR/issue references]

## Suggested Fix
[Proposed change — agent prompt, pipeline logic, schema, etc.]

## Agent Version
miner/0.1.0
```

Labels auto-applied based on content: `kaizen:agent-prompt`,
`kaizen:pipeline`, `kaizen:schema`, `enhancement`, `bug`.

### /idea

**Purpose**: Lightweight feature request capture from Workshop sessions.

**Behavior**: Takes a one-liner, expands it minimally, files a GitHub issue
with appropriate labels. No conversation analysis — just fast capture.

```
/idea Add a "confidence" field to mapping frontmatter
```

### Kaizen Convention

Agents append a `## kaizen` block to their PR or issue comments when they
encounter friction:

```markdown
## kaizen
- **observed**: [what happened]
- **suggestion**: [proposed improvement]
- **severity**: minor | moderate | major
```

A periodic sweep (manual `/kaizen` command or scheduled Action) collects
these blocks, deduplicates, and creates consolidated kaizen issues.

## 7. Build Triggers

| Workflow | Trigger | Duration | Purpose |
|----------|---------|----------|---------|
| `validate.yml` | Every PR | ~10s | Python schema validation |
| `deploy-site.yml` | Nightly 4am UTC + `workflow_dispatch` | ~2 min | Astro + Pagefind -> GitHub Pages |
| `build-artifact.yml` | Nightly 4am UTC + `workflow_dispatch` (deferred) | ~3 min | SQLite + embeddings -> GitHub Release |

Content PRs are never more than 24 hours stale on the site. Manual dispatch
available for demos and sharing.

## 8. Implementation Order

1. **Repo consolidation** — merge agents history, reorganize directories
2. **Astro scaffold** — Content Collections, templates, Pagefind, llms.txt
3. **GitHub Pages deployment** — workflow, custom domain, CNAME
4. **New commands** — /debrief, /idea (can be built incrementally)
5. **Kaizen convention** — add to agent prompts
6. **CLI + SQLite artifact** — deferred to a later design session
7. **Factory workspace** — set up second clone after monorepo is stable
