#!/bin/bash
# guard-self-modification.sh — PreToolUse hook that prevents agents from
# modifying their own governance files. This is the enforcement layer for
# the kaizen self-improvement boundary model (see docs/kaizen-self-improvement.md).
#
# ALLOWED (kaizen targets):
#   .claude/agents/*.md       — agent prompts (the whole point of kaizen)
#   scripts/*.py              — pipeline scripts
#   docs/**                   — documentation
#
# BLOCKED (governance / escalation paths):
#   .claude/settings*.json    — permission escalation
#   .claude/CLAUDE.md         — root instructions (not in this repo, but guard anyway)
#   CLAUDE.md                 — project-level root instructions
#   .claude/skills/**         — skill definitions (human-authored)
#   .claude/hooks/**          — hook definitions (guards guarding the guards)
#   hooks/hooks.json          — plugin hook config
#   .github/workflows/**      — CI/CD pipelines
#
# ALLOWED (co-authored with agents):
#   .claude/commands/**       — slash commands (pitboss updates dispatch logic)
#
# Install: add as PreToolUse hook matching "Write|Edit" in settings.json
# Kill switch: delete this script or remove the hook entry

set -euo pipefail

input=$(cat)
tool_name=$(echo "$input" | jq -r '.tool_name // empty')
file_path=""

if [ "$tool_name" = "Edit" ] || [ "$tool_name" = "Write" ]; then
  file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')
elif [ "$tool_name" = "Bash" ]; then
  # Check if bash command targets a guarded file via redirect or sed -i
  command=$(echo "$input" | jq -r '.tool_input.command // empty')
  # Only check commands that look like writes to guarded paths
  if echo "$command" | grep -qE '(settings.*\.json|CLAUDE\.md|\.claude/skills|\.claude/hooks|hooks\.json|\.github/workflows)'; then
    if echo "$command" | grep -qE '(>|>>|sed\s+-i|tee\s|cat\s.*>|echo\s.*>|mv\s|cp\s)'; then
      echo '{"hookSpecificOutput":{"permissionDecision":"deny"},"systemMessage":"BLOCKED by guard-self-modification.sh: bash command appears to write to a governance file. Agent prompts (.claude/agents/*.md) and scripts (scripts/) are the only self-modifiable paths. See docs/kaizen-self-improvement.md."}' >&2
      exit 2
    fi
  fi
  exit 0
fi

# No file path to check — allow
if [ -z "$file_path" ]; then
  exit 0
fi

# Normalize: strip leading ./ and resolve to relative path from project root
file_path="${file_path#./}"
# If absolute, strip project dir prefix
if [ -n "${CLAUDE_PROJECT_DIR:-}" ]; then
  file_path="${file_path#"$CLAUDE_PROJECT_DIR"/}"
fi

# --- BLOCKED paths ---
blocked=false
reason=""

case "$file_path" in
  .claude/settings*|*/settings.json|*/settings.local.json)
    blocked=true
    reason="settings files control permissions — human-only"
    ;;
  CLAUDE.md|.claude/CLAUDE.md|*/CLAUDE.md)
    blocked=true
    reason="root instruction files — human-only"
    ;;
  .claude/skills/*|.claude/skills/**)
    blocked=true
    reason="skill definitions — human-authored"
    ;;
  .claude/hooks/*|hooks/hooks.json)
    blocked=true
    reason="hook definitions — guards cannot modify guards"
    ;;
  .github/workflows/*|.github/workflows/**)
    blocked=true
    reason="CI/CD workflows — human-only"
    ;;
esac

if [ "$blocked" = true ]; then
  echo "{\"hookSpecificOutput\":{\"permissionDecision\":\"deny\"},\"systemMessage\":\"BLOCKED by guard-self-modification.sh: cannot modify $file_path ($reason). Only .claude/agents/*.md and scripts/ are self-modifiable. See docs/kaizen-self-improvement.md.\"}" >&2
  exit 2
fi

# All other paths — allow (normal permission rules still apply)
exit 0
