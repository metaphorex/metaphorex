---
name: configure
description: Set up operator-level crew config for Metaphorex agents
allowed-tools: ["Read", "Write", "AskUserQuestion", "Bash"]
---

# Configure Metaphorex Agent Crew

Set up `.claude/metaphorex-agents.local.md` with operator-level identity
config for the agent pipeline.

## Step 1: Check for existing config

Read `.claude/metaphorex-agents.local.md`. If it exists, show the current
config and ask: "Update this config, or start fresh? [update/fresh]"

## Step 2: Ask about bot accounts

Ask the user:

> Do you have dedicated GitHub bot accounts for Metaphorex agents?
>
> If yes, I'll configure each agent role with its bot account token.
> If no, agents will use your default `gh` auth. No config file needed.
>
> **[y/N]**

If no: say "No crew config needed. Agents will use your default gh auth
and git identity. You're all set." and stop.

## Step 3: Configure each role

For each of the three roles, ask (with defaults pre-filled):

### Miner role (Miner, Smelter agents)

> Token env var name? **[M4X_MINER_TOKEN]**
> Git username? **[m4x-miner]**
> Git email? **[miner@metaphorex.org]**

### Reviewer role (Assayer, Surveyor agents)

> Token env var name? **[M4X_REVIEWER_TOKEN]**
> Git username? **[m4x-reviewer]**
> Git email? **[reviewer@metaphorex.org]**

### Ops role (Prospector, Fixer agents)

> Token env var name? **[M4X_OPS_TOKEN]**
> Git username? **[m4x-ops]**
> Git email? **[ops@metaphorex.org]**

## Step 4: Write config file

Write `.claude/metaphorex-agents.local.md` with the collected values:

```yaml
---
roles:
  miner:
    agents: [miner, smelter]
    gh_token_var: <collected>
    git_name: <collected>
    git_email: <collected>

  reviewer:
    agents: [assayer, surveyor]
    gh_token_var: <collected>
    git_name: <collected>
    git_email: <collected>

  ops:
    agents: [prospector, fixer]
    gh_token_var: <collected>
    git_name: <collected>
    git_email: <collected>
---

# Agent Crew Configuration

Operator-level identity config for Metaphorex agents.
Run `/configure` to regenerate.
```

## Step 5: Verify tokens are available

For each role, check if the token env var is set:

```bash
echo "${M4X_MINER_TOKEN:-(not set)}"
```

Report which tokens are available and which are missing. For missing
tokens, remind the operator:

> Token `M4X_MINER_TOKEN` is not set. Run `gh-pat-rotate m4x-miner`
> and `source ~/.secrets/gh-pats.sh` to load it.

## Step 6: Done

> Crew config saved to `.claude/metaphorex-agents.local.md`.
> Restart Claude Code for agents to pick it up.
