# Metaphorex

A collaboratively built knowledge graph of metaphors, mental models, and
conceptual mappings across all domains.

## What This Is

A catalog of **mappings** — structured analyses of how concepts from one
domain illuminate another. Each mapping documents what the metaphor brings
(the useful structural parallels), where it breaks (the limits and
misleading implications), and concrete expressions found in the wild.

This is not just software metaphors. It covers conceptual metaphors from
cognitive science, design patterns, archetypes, cross-field mappings, and
dead metaphors worth examining.

## Structure

```
catalog/
  mappings/    one markdown file per mapping (the main content)
  frames/      conceptual domains (source and target)
  categories/  taxonomy labels for cross-cutting classification
scripts/       validation and extraction tools
docs/          design documents and plans
```

Everything is plain markdown with YAML frontmatter. No static site generator.
Readable as-is on GitHub.

## Quick Start

Browse [catalog/mappings/](catalog/mappings/) to read entries. Each mapping has:

- **What It Brings** — the structural parallels that make it useful
- **Where It Breaks** — where the metaphor misleads
- **Expressions** — specific phrases and usages found in the wild

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The short version:

1. Create a mapping as a markdown file with the required frontmatter
2. Validate with `uv run scripts/validate.py validate`
3. Open a pull request

Contributions from both humans and agents are welcome.

## Validation

```bash
uv run scripts/validate.py validate           # check all content
uv run scripts/validate.py validate catalog/mappings/  # check specific directory
uv run scripts/validate.py extract             # emit structured JSON
```

## License

Content (`catalog/`, `playbooks/`) is licensed under
[CC BY-SA 4.0](LICENSE-CC-BY-SA-4.0). Code is licensed under
[MIT](LICENSE-MIT). See [LICENSE](LICENSE) for details.
