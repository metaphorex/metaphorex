# Agents Plugin Design

Date: 2026-03-07
Repo: metaphorex/agents

## Overview

A Claude Code plugin providing three agents that operate the Metaphorex
content pipeline: researching sources, extracting mappings, and reviewing
quality. Agents run under the contributor's own GitHub auth and identify
themselves via git Co-Authored-By trailers and structured issue comments.

## Agent Roles

### Prospector (high trust)

Researches a source identified by an import-project issue. Produces:
- A playbook (extraction strategy, access method, parsing approach, gotchas)
- Extraction scripts (deterministic parsers for the source)
- Sub-issues on the parent issue (one per mapping candidate)
- PR into metaphorex/agents with playbook + scripts

Invoked via: `/prospect <issue-url>`

### Miner (standard trust)

Follows an approved playbook to extract mappings. For each sub-issue:
- Reads playbook + approved scripts
- Generates mapping/frame/category markdown files
- Runs the content validator
- Opens a PR into metaphorex/metaphorex
- Links PR to the sub-issue
- Posts a run summary comment on the parent issue

Invoked via: `/mine <project-name>`

### Assayer (standard trust)

Reviews Miner output for quality, accuracy, and completeness. On each PR:
- Checks frontmatter correctness and cross-references
- Evaluates "What It Brings" / "Where It Breaks" for depth and rigor
- Verifies expressions are grounded in real usage
- Posts review (approve, request changes, or comment)
- Pushes fixup commits for mechanical issues
- Does NOT modify Prospector scripts (read-only consumer)

Invoked via: `/assay <pr-url>`

## Trust Model

- Prospector writes code → PRs into agents repo → CODEOWNERS requires
  human review on `projects/*/scripts/**`
- Miner writes content → PRs into content repo → standard review
- Assayer reviews + refines → pushes fixups to existing PRs → lightweight
- Agents NEVER commit directly to main in either repo

## Agent Identity

Each agent declares its identity in frontmatter:

```yaml
---
name: miner
identity: metaphorex-miner
email: miner@metaphorex.org
model: inherit
color: green
---
```

- `identity` — unique name used in Co-Authored-By trailers and run comments
- `email` — used in the Co-Authored-By trailer

Contributors who fork an agent MUST create a distinct identity:
```yaml
identity: acme-miner
email: miner@acme-labs.dev
```

### Auth Model

Agents run under the contributor's own GitHub auth (gh CLI token). No
GitHub App setup required. The contributor's permissions are the boundary:
if they can only PR, the agent can only PR. The human is accountable for
what runs under their auth.

Co-Authored-By trailer identifies the agent in git history:
```
Co-Authored-By: metaphorex-miner <miner@metaphorex.org>
```

## Cost Tracking

After each run, the agent posts a structured comment on the parent
import-project issue:

```markdown
### Run: metaphorex-miner • 2026-03-07 14:30 UTC

| Metric | Value |
|--------|-------|
| Agent | [metaphorex-miner@`a1b2c3d`](https://github.com/metaphorex/agents/blob/a1b2c3d/agents/miner.md) |
| Harness | Claude Code |
| Model | claude-sonnet-4-6 |
| Entries | 5 |
| PRs | #12, #13, #14, #15, #16 |
| Tokens | ~24,000 |
| Est. cost | $0.08 |

<details><summary>Per-entry breakdown</summary>

| Entry | Tokens | PR |
|-------|--------|----|
| argument-is-war | 4,200 | #12 |
| time-is-money | 3,800 | #13 |

</details>
```

Three independent version axes in each run comment:
- **What ran the agent** → runtime name (Harness: Claude Code, Codex, etc.)
- **What the agent knew** → commit hash in the Agent permalink
- **What did the thinking** → Model name

The Agent link is a GitHub permalink to the agent file at the exact commit
hash — canonical source + version in one URL.

No generated log files are committed. The issue comment IS the run log.

## Repo Structure

```
metaphorex-agents/
├── .claude-plugin/
│   └── plugin.json
├── agents/
│   ├── prospector.md
│   ├── miner.md
│   └── assayer.md
├── commands/
│   ├── prospect.md
│   ├── mine.md
│   └── assay.md
├── skills/
│   └── metaphorex-schema/
│       └── SKILL.md          # shared schema knowledge
├── scripts/
│   └── post-run-comment.sh   # posts structured run comment to issue
├── projects/                  # accumulated extraction knowledge
│   └── <project-name>/
│       ├── playbook.md        # Prospector output
│       └── scripts/           # Prospector-written extraction code
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── CODEOWNERS
```

## Playbook Format

```yaml
---
project_issue: 1
repo: metaphorex/metaphorex
source_type: book             # book | web | corpus | api | oral-tradition
status: active                # draft | active | completed | stale
---
```

Body sections:
- `## Source Description` — what it is, where to find it
- `## Access Method` — how the agent accesses the content
- `## Extraction Strategy` — what to look for, how to identify mappings
- `## Schema Mapping` — how source concepts map to metaphorex frontmatter
- `## Gotchas` — accumulated knowledge from failed attempts

## Pipeline Flow

```
Human creates import-project issue in metaphorex/metaphorex
        │
        ▼
   /prospect <issue-url>
        │
   Prospector researches source
   ├── Writes playbook.md + extraction scripts
   ├── Creates sub-issues (one per mapping candidate)
   └── Opens PR into metaphorex/agents
        │
        ▼
   Human reviews + merges playbook PR (CODEOWNERS gate on scripts/)
        │
        ▼
   /mine <project-name>
        │
   Miner works each sub-issue
   ├── Reads playbook + approved scripts
   ├── Generates mapping + frame + category files
   ├── Runs validator (uv run scripts/validate.py validate)
   ├── Opens PR into metaphorex/metaphorex
   ├── Links PR to sub-issue
   └── Posts run comment on parent issue
        │
        ▼
   /assay <pr-url>
        │
   Assayer reviews each PR
   ├── Structural review (schema, cross-refs, sections)
   ├── Quality review (depth, rigor, grounded expressions)
   ├── Pushes fixup commits for mechanical issues
   └── Posts GitHub review (approve / request changes)
        │
        ▼
   Human spot-checks, merges
```

## Content Schema Skill

Both Prospector and Miner need to know the metaphorex content schema.
Rather than duplicating this in each agent's system prompt, a shared
skill (`skills/metaphorex-schema/SKILL.md`) contains:

- Mapping frontmatter spec (all fields, valid kinds, constraints)
- Required body sections and conventions
- Frame and category schema
- Validator rules
- Tone guide (reference the seed entries in metaphorex/metaphorex)

The skill instructs agents to fetch the current seed entries from the
content repo as style references.

## Frame & Category Upsert Process

When an agent creates mappings that reference frames or categories that
don't exist:

- The agent creates the frame/category files in the same PR
- Frames are cheap (contributors should feel free to create them)
- Categories are expensive (taxonomy decisions affect the whole graph)
- The Prospector should identify needed frames during playbook creation
- The validator enforces that source_frame and target_frame resolve

## Licensing

- Plugin code: MIT
- Playbooks: CC BY-SA 4.0 (extraction knowledge is content)
