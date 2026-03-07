# Contributing to Metaphorex Agents

## Forking Agents

You're encouraged to fork and remix these agents. When you do:

1. **Create a distinct identity.** Change the `identity` and `email` fields
   in the agent's frontmatter:

   ```yaml
   identity: your-org-miner
   email: miner@your-org.dev
   ```

   This ensures your agent's commits and run comments are distinguishable
   from the canonical agents.

2. **Keep the schema skill.** The `metaphorex-schema` skill is the shared
   contract between agents and the content repo. Your forked agents should
   still use it (or your own updated version).

3. **Test against the validator.** Before submitting PRs from your forked
   agents, run `uv run scripts/validate.py validate` in the content repo.

## Improving Agents

PRs to improve agent prompts, add extraction scripts, or enhance the schema
skill are welcome.

### Agent changes

- Changes to agent system prompts should be tested against real extraction
  tasks before submitting.
- Include before/after examples in your PR description.

### Playbooks and scripts

- Playbooks are extraction knowledge — treat them as content (CC BY-SA 4.0).
- Scripts in `projects/*/scripts/` require CODEOWNERS review. They must be:
  - Safe: read input, write to stdout, no side effects
  - Deterministic: same input → same output
  - Documented: a comment at the top explaining what it does

## Run Comments

When your agent completes a run, post a structured comment on the parent
import-project issue. Include:

- Agent permalink (link to your agent.md at the specific commit hash)
- Harness (Claude Code version — the runtime driving the agent)
- Model used
- Token counts and estimated cost
- Per-entry breakdown with PR links

This is how we track agent activity and costs without generating log file PRs.

## License

By contributing, you agree that:
- Plugin code (agents, commands, skills, scripts) is licensed under MIT
- Playbook content is licensed under CC BY-SA 4.0
