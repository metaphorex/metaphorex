# Metaphorex Agents

A [Claude Code](https://claude.com/claude-code) plugin providing a multi-agent
pipeline for the Metaphorex content catalog.

## Pipeline

```
                    ┌─────────────────────────────────────────────────┐
                    │              PITBOSS (/work)                    │
                    │         Orchestrates all agents,                │
                    │       manages labels, merges PRs                │
                    └──────────┬──────────────────────────────────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         ▼                     ▼                      ▼
   ┌───────────┐        ┌───────────┐          ┌───────────┐
   │ PROSPECTOR│        │  SMELTER  │          │   MINER   │
   │           │        │           │          │           │
   │ Find      │        │ Validate  │          │ Extract   │
   │ archives, │        │ format,   │          │ mappings, │
   │ write     │        │ normalize │          │ open PRs  │
   │ scripts,  │        │ frontmatter│         │           │
   │ produce   │        └─────┬─────┘          └─────┬─────┘
   │ manifest  │              │                      │
   └─────┬─────┘              ▼                      │
         │              ┌───────────┐                │
         ▼              │  ASSAYER  │                │
   ┌───────────┐        │           │◄───────────────┘
   │ SURVEYOR  │        │ Review    │
   │           │        │ quality,  │
   │ Run       │        │ approve   │
   │ scripts,  │        │ or reject │
   │ verify    │        └─────┬─────┘
   │ manifest, │              │
   │ create    │              ▼
   │ issues    │        ┌───────────┐
   └───────────┘        │   MERGE   │
                        │ (pitboss) │
                        └───────────┘
```

### State diagram — import project lifecycle

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   CREATED    │────▶│  PROSPECTED  │────▶│   SURVEYED   │────▶│    MINED     │
│              │     │              │     │              │     │   (done)     │
│ import-      │     │ in-progress  │     │ in-progress  │     │ all issues   │
│ project      │     │              │     │ + surveyed   │     │ closed       │
│ label only   │     │ manifest.json│     │ sub-issues   │     │              │
└──────────────┘     │ + scripts    │     │ exist        │     └──────────────┘
                     └──────┬───────┘     └──────────────┘
                            │                    ▲
                            ▼                    │
                     ┌──────────────┐            │
                     │ NEEDS REWORK │────────────┘
                     │              │  re-prospect
                     │ needs-rework │
                     └──────────────┘
```

### State diagram — PR lifecycle

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   OPENED     │────▶│   SMELTED    │────▶│   ASSAYED    │────▶│   MERGED     │
│              │     │              │     │              │     │              │
│ needs-       │     │ needs-assay  │     │ approved     │     │ squash merge │
│ smelting     │     │              │     │              │     │ + auto-merge │
└──────────────┘     └──────────────┘     └──────┬───────┘     └──────────────┘
                                                 │
                                                 ▼
                                          ┌──────────────┐
                                          │  NEEDS FIX   │
                                          │              │──── miner fixes ──── back to
                                          │ needs-miner- │                     needs-assay
                                          │ fix          │
                                          └──────────────┘
```

## Agents

| Agent | Role | Model | Trigger |
|-------|------|-------|---------|
| **Prospector** | Find archives, write scripts, produce manifest | opus | `needs_prospecting` or `needs_rework` |
| **Surveyor** | Verify manifest, run scripts, create sub-issues | sonnet | `needs_survey` (prospected, not yet verified) |
| **Miner** | Extract mappings, open content PRs | opus | `unclaimed` issues (surveyed projects only) |
| **Smelter** | Validate formatting, normalize frontmatter | haiku | `needs-smelting` label on PRs |
| **Assayer** | Review mapping quality, approve or reject | sonnet | `needs-assay` label on PRs |

## Quick Start

Install as a Claude Code plugin, then:

```bash
# Run the full automated pipeline
/work

# Or run individual agents:
/prospect   # Research a new source
/mine       # Extract mappings from a surveyed project
/assay      # Review a mapping PR
/smelt      # Mechanical cleanup on a PR
```

## Key Design Principles

**Archive-first prospecting.** The Prospector's primary job is to find
existing structured archives (academic databases, HTML indexes, PDFs), not
to generate candidate lists from LLM knowledge. Scripts extract candidates
deterministically; LLM knowledge fills gaps only.

**Manifest before issues.** The Prospector produces a `manifest.json` — a
diffable, countable candidate list — but does NOT create GitHub sub-issues.
The Surveyor verifies the manifest by running scripts independently, then
creates issues only after approval. No side effects before verification.

**Deterministic label management.** Each agent is responsible for setting
the correct label on completion. The pitboss orchestrator trusts labels,
never interprets review text. If a label is wrong, that's an agent bug.

**Auto-merge after approval.** Approved PRs are merged automatically via
GitHub's auto-merge (squash). Branch protection requires the `validate` CI
check to pass.

## Project Structure

```
agents/              # Agent definitions (markdown + frontmatter)
commands/            # Slash commands (/work, /prospect, /mine, etc.)
skills/              # Shared skills (schema reference, etc.)
scripts/             # Pipeline tooling (survey.py, validate.py)
projects/
  <project-name>/
    playbook.md      # Extraction strategy (Prospector output)
    manifest.json    # Candidate list (Prospector output, Surveyor verified)
    scripts/         # Scraping/parsing scripts (Prospector output)
content-repo/        # Local checkout of metaphorex/metaphorex
```

## Agent Identity

Each agent identifies itself via `Co-Authored-By` in git commits:

```
Co-Authored-By: metaphorex-miner <miner@metaphorex.org>
```

Agents run under the contributor's own GitHub auth. No GitHub App setup
required.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Plugin code: [MIT](LICENSE). Playbooks: CC BY-SA 4.0.
