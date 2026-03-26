---
name: agent-identity
description: >
  Use before any gh or git commands in an agent context.
  Reads operator crew config to set GH_TOKEN and git identity.
  Falls back gracefully when no config exists.
---

# Agent Identity

Set up GitHub and git identity for the current agent.

## Step 1: Read crew config

Read `.claude/metaphorex-agents.local.md`. If the file does not exist,
skip to the Fallback section below.

## Step 2: Find your role

Parse the YAML frontmatter. Find the role whose `agents` array contains
your agent name (from your own frontmatter `identity` field, minus the
`metaphorex-` prefix. For example `metaphorex-miner` matches `miner`).

If no matching role is found, skip to the Fallback section.

## Step 3: Check token

Check if the env var named in `gh_token_var` is set:

```bash
echo "${<gh_token_var>:-(not set)}"
```

If the variable is not set or empty, log this warning and skip to Fallback:

> Identity config found but token `<gh_token_var>` is not in the environment.
> Falling back to default auth.
> See CONTRIBUTING.md#agent-setup for bot account setup.

## Step 4: Apply identity

IMPORTANT: Each Bash tool call is a fresh shell. Environment variables like
`export GH_TOKEN` do NOT persist between tool calls. You must inline the
token on every single `gh` command.

**For ALL `gh` commands**, prefix with the token inline:

```bash
GH_TOKEN="$<gh_token_var>" gh pr create ...
GH_TOKEN="$<gh_token_var>" gh issue comment ...
```

This is not optional. Every `gh` call without the prefix will use the
wrong identity. There are no shortcuts — no aliases, no exports, no
shell functions that persist. Inline prefix on every call.

**For ALL `git commit` commands**, use `-c` flags:

```bash
git -c user.name="<git_name>" -c user.email="<git_email>" commit ...
```

**Co-Authored-By trailer** on all commits:

```
Co-Authored-By: <git_name> <<git_email>>
```

**Summary — remember these two prefixes for your entire run:**

```
gh prefix:  GH_TOKEN="$<gh_token_var>"
git prefix: git -c user.name="<git_name>" -c user.email="<git_email>"
```

## Fallback

No crew config or no token. This is normal for contributors without bot
accounts. Use whatever `gh` auth and git config is already active.

Use the Co-Authored-By trailer from your own agent frontmatter:

```
Co-Authored-By: <your identity> <<your email>>
```

Log once at the start of your run:

> No crew config at `.claude/metaphorex-agents.local.md`. Using default
> auth. See CONTRIBUTING.md#agent-setup for bot account setup.
