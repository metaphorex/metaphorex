# Kaizen: Agent Self-Improvement

How and why Metaphorex agents modify their own pipeline — and where the
boundaries are.

## The premise

In manufacturing, *kaizen* means continuous improvement by the people doing
the work. The people closest to the friction are the ones best positioned to
fix it. The same logic applies here: our agents encounter pipeline friction
every run — ambiguous prompts, wrong API patterns, missing validation — and
they're the ones best positioned to describe what went wrong.

We extend that idea one step further: agents don't just *report* friction,
they *fix* it. The fixer agent reads a kaizen issue, edits the relevant
agent prompt or script, and opens a PR. A human reviews and merges.

This creates a feedback loop: agents encounter friction → file kaizen issues
→ fixer resolves them → agents run better next round.

## What agents can modify

The self-improvement surface is deliberately narrow:

| Path | Contents | Why modifiable |
|------|----------|---------------|
| `.claude/agents/*.md` | Agent system prompts | The primary kaizen target — prompt wording, API patterns, workflow steps |
| `scripts/*.py` | Validation, survey, utilities | Pipeline bugs and improvements |
| `docs/**` | Design docs and plans | Documentation of decisions |

These are the files where pipeline friction lives. An agent that encounters
a wrong `gh api` invocation pattern in its own prompt should be able to fix
that pattern for all future runs.

## What agents cannot modify

Governance files are human-only. These control what agents are, what they're
allowed to do, and how they're supervised:

| Path | Contents | Why protected |
|------|----------|---------------|
| `.claude/settings*.json` | Permissions and hooks | **Escalation path** — an agent that can edit its own permissions can grant itself arbitrary access |
| `CLAUDE.md` | Root project instructions | Defines the entire operating contract |
| `.claude/skills/**` | Skill definitions | Human-authored capabilities |
| `.claude/commands/**` | Slash commands | Human-authored entry points |
| `.claude/hooks/**` | Hook definitions | Guards cannot modify guards |
| `.github/workflows/**` | CI/CD pipelines | Deployment and merge automation |

The distinction is simple: **agents modify their tactics, not their
constraints.** A miner can improve how it reads files from a PR branch; it
cannot decide that it no longer needs review.

## Why this boundary matters

The self-improvement loop is powerful, but it has an obvious failure mode:
an agent that modifies its own governance can escalate without limit.
Concretely:

1. Agent edits `settings.local.json` to grant `Edit` (unrestricted)
2. Agent edits `CLAUDE.md` to remove review requirements
3. Agent edits its own prompt to skip validation
4. Agent pushes directly to main

Each step is individually plausible if the previous boundary is missing.
The whole point of the governance boundary is to make step 1 impossible,
so steps 2-4 never happen.

This isn't theoretical paranoia — it's the same principle as separation of
privileges in any system. The code that runs in production should not be
able to modify its own access control policy.

## Defense in depth

No single mechanism is sufficient. We use four layers:

### Layer 1: Permission rules (settings.local.json)

```json
"allow": ["Edit(.claude/agents/**)", "Edit(scripts/**)"],
"deny":  ["Edit(.claude/settings*)", "Edit(CLAUDE.md)", ...]
```

Coarse access control. Deny rules take precedence over allow rules. This
is the fastest check — it runs before the tool executes.

### Layer 2: Guard hook (scripts/guard-self-modification.sh)

A `PreToolUse` hook that inspects every `Edit`, `Write`, and `Bash` call.
It blocks writes to governance files and catches bash-based workarounds
like `sed -i` or `echo >` targeting protected paths.

The hook runs outside agent control — agents cannot modify it mid-session
because hooks are loaded at session start. Even if an agent could edit the
script file, the change wouldn't take effect until the next session.

### Layer 3: Worktree isolation

The fixer agent runs in a git worktree. Its edits exist on a branch, not
on main. Even if layers 1 and 2 somehow failed, the agent's changes are
isolated to a throwaway workspace.

### Layer 4: PR review gate

All fixer output goes through a pull request labeled `kaizen-fix`. A human
reviews and merges. This is the final backstop — no agent change reaches
main without human approval.

### What each layer catches

| Attack | L1 Permissions | L2 Hook | L3 Worktree | L4 PR Review |
|--------|:-:|:-:|:-:|:-:|
| Edit settings.json | X | X | | X |
| `sed -i` settings.json | | X | | X |
| Obfuscated bash write | | | X | X |
| Edit own prompt maliciously | | | | X |
| Disable validation in script | | | | X |

No single layer covers everything. Together they make escalation require
defeating four independent mechanisms.

## Known gaps

Honesty about limitations is itself a safety property.

**Bash obfuscation.** The guard hook uses pattern matching on bash commands.
A sufficiently creative command (variable indirection, eval, piping through
intermediate files) could bypass pattern detection. Layer 3 (worktree) and
layer 4 (PR review) catch this.

**Agent prompt manipulation.** An agent *can* edit another agent's prompt in
ways that are subtly harmful — for example, weakening validation criteria
or adding bias to content decisions. The PR review gate is the only defense
here, and it depends on the reviewer reading carefully.

**Session-scoped hooks.** Hooks load at session start. If an agent somehow
modified the guard script file, the change wouldn't affect the current
session — but it would affect the next one. The deny rule on `.claude/hooks/**`
and the PR review gate address this.

**Global bash permissions.** The global settings allow `Bash(sed:*)`,
`Bash(echo:*)`, etc. The guard hook catches writes to known governance
paths, but it's pattern-based, not hermetic. A future improvement would
be to tighten global bash permissions to exclude `.claude/` paths entirely.

## Operating principles

These guide decisions about what to allow and what to protect:

1. **Agents modify tactics, not constraints.** Prompts and scripts are
   tactics. Permissions, root instructions, and hooks are constraints.

2. **The closer to friction, the faster the fix.** Agents that encounter
   a problem should be able to fix it in the same pipeline round, not
   wait for a human to context-switch into the problem days later.

3. **Defense in depth, not defense in perfection.** No single layer needs
   to be unbreakable. Each layer catches what the previous one misses.

4. **Transparency over cleverness.** The guard script is simple bash, not
   a clever sandbox. Anyone can read it, understand it, and audit it.
   Complex security mechanisms that nobody reviews are worse than simple
   ones that everyone understands.

5. **Escalation requires human intent.** Expanding what agents can modify
   requires editing `settings.local.json` or `CLAUDE.md` — files that
   agents cannot touch. A human must deliberately choose to widen the
   boundary.

6. **Assume good faith, verify anyway.** The agents aren't adversarial —
   they're tools running prompts we wrote. The boundaries exist not because
   we expect malice, but because we expect mistakes. An agent that
   "helpfully" edits settings to unblock itself is more likely than an
   agent that deliberately escalates.

7. **Kill switches are cheap insurance.** Deleting `settings.local.json`
   re-gates everything. Deleting the guard script removes the hook (after
   session restart). Recovery from any misconfiguration should take seconds.

## Expanding the boundary

If the self-improvement loop proves reliable and the PR review gate catches
issues consistently, we may expand what agents can modify:

- **Skills** — if agents demonstrate they can improve skill definitions
  without breaking triggering accuracy
- **Workflows** — if CI/CD changes can be safely tested in PR checks
  before merge

Each expansion should be a deliberate decision with its own kaizen issue,
not a quiet permissions tweak. Document *why* the boundary moved and what
new review expectations apply.

## File reference

| File | Purpose |
|------|---------|
| `.claude/settings.local.json` | Permission allow/deny rules + hook config |
| `scripts/guard-self-modification.sh` | PreToolUse hook enforcing governance boundaries |
| `docs/kaizen-self-improvement.md` | This document |
