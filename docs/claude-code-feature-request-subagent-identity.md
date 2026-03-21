# Feature Request: Subagent environment variable isolation for multi-identity workflows

## Summary

When running a multi-agent pipeline where different subagents need to authenticate as different GitHub bot accounts, there's no clean way to give each subagent its own `GH_TOKEN`. The Skill tool isn't available to subagents, environment variables can't be scoped per-agent, and `export` doesn't persist between Bash tool calls. The current workaround — repeating `GH_TOKEN="$VAR" gh ...` on every single command in every agent prompt — is fragile and verbose.

## Use case

We run a content pipeline ([metaphorex/metaphorex](https://github.com/metaphorex/metaphorex)) with 6 specialized subagents orchestrated by a "pitboss" in the main conversation:

| Agent | Role | Bot account | Token env var |
|-------|------|-------------|---------------|
| Miner | Creates content PRs | `m4x-miner` | `M4X_MINER_TOKEN` |
| Smelter | Mechanical PR cleanup | `m4x-miner` | `M4X_MINER_TOKEN` |
| Assayer | Reviews PRs for quality | `m4x-reviewer` | `M4X_REVIEWER_TOKEN` |
| Surveyor | Validates playbooks | `m4x-reviewer` | `M4X_REVIEWER_TOKEN` |
| Prospector | Researches new sources | `m4x-ops` | `M4X_OPS_TOKEN` |
| Fixer | Fixes pipeline bugs | `m4x-ops` | `M4X_OPS_TOKEN` |

Each agent needs to `gh pr create`, `gh issue edit`, `gh pr review`, etc. as its designated bot account. Without identity separation:
- All activity shows as the human operator, making audit trails useless
- Agents can approve their own PRs (miner creates, same identity reviews)
- GitHub's CODEOWNERS and branch protection rules can't distinguish agent roles

## Current problems

### 1. Subagents can't use Skills

We built an `agent-identity` skill that reads a crew config file and sets up the right token/git-identity per agent role. But subagents launched via the `Agent` tool don't have access to the `Skill` tool — they only get `Read, Write, Edit, Bash, Glob, Grep`. The skill was dead code from the agents' perspective, and all agents silently fell back to the operator's credentials.

### 2. No per-agent environment scoping

The `Agent` tool doesn't support passing environment variables to the subagent. We can't say "launch this agent with `GH_TOKEN=<value>`." The only way to get the right token is to have the agent inline `GH_TOKEN="$M4X_MINER_TOKEN"` on literally every `gh` CLI call, which requires:
- Repeating the instruction prominently in every agent prompt
- Repeating it again in every pitboss dispatch prompt (belt and suspenders)
- Hoping the model follows the instruction 100% of the time (it doesn't — we saw ~60% compliance before making the instructions extremely prominent)

### 3. `export` doesn't persist between Bash calls

Each `Bash` tool invocation is a fresh shell. `export GH_TOKEN=...` in one call has no effect on the next. This is documented behavior but it means there's no "set it once" pattern available — the inline prefix must appear on every single command.

## What would help

Any of these would significantly improve the multi-identity workflow:

### Option A: Agent-level environment variables (preferred)

Allow the `Agent` tool to accept an `env` parameter that sets environment variables for all Bash calls within that agent's session:

```json
{
  "subagent_type": "miner",
  "env": {
    "GH_TOKEN": "$M4X_MINER_TOKEN",
    "GIT_AUTHOR_NAME": "m4x-miner",
    "GIT_AUTHOR_EMAIL": "miner@metaphorex.org"
  }
}
```

This would be the cleanest solution — identity becomes a dispatch-time decision by the orchestrator, and the agent prompts don't need identity instructions at all.

### Option B: Persistent shell environment within a subagent

Allow `export` in one Bash call to persist to subsequent Bash calls within the same agent session. The agent could run a single setup command and all subsequent `gh` / `git` calls would inherit the right identity.

### Option C: Make Skills available to subagents

If subagents could invoke Skills, our original `agent-identity` skill would work. This would also unlock other reusable behaviors (schema validation, commit conventions, etc.) that we currently have to inline into every agent prompt.

### Option D: Agent-level git/gh config

A narrower solution: allow the `Agent` tool to accept `git_identity` and `gh_token` parameters that configure git and gh for the agent's session. Less general than Option A but covers the specific use case.

## Impact

This affects any pipeline that needs:
- **Audit trails** — knowing which agent did what
- **Separation of concerns** — preventing agents from approving their own work
- **Branch protection** — using GitHub's CODEOWNERS with bot accounts
- **Rate limiting** — distributing API calls across multiple tokens

We're currently running 6 agents across 3 bot accounts producing ~10-15 PRs per session. The inline-prefix workaround works but adds ~20 lines of identity boilerplate to every agent prompt and every dispatch call, and compliance is model-dependent.

## Environment

- Claude Code CLI
- macOS / fish shell
- Agents launched via `Agent` tool with `subagent_type`, `isolation: "worktree"`, `run_in_background: true`
- GitHub bot accounts with fine-grained PATs stored in env vars
