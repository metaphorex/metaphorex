# Metaphorex

A materials library of load-bearing metaphors and other useful abstractions.
Browse the catalog at [**metaphorex.org**](https://metaphorex.org).

## What This Is

A catalog of **mappings** — structured analyses of how concepts from one domain
illuminate another. Each mapping documents what the metaphor brings (the useful
structural parallels), where it breaks (the limits and misleading implications),
and concrete expressions found in the wild.

This covers conceptual metaphors from cognitive science, design patterns,
archetypes, paradigms, cross-field mappings, and dead metaphors worth examining.

## How It Works

Everything is plain markdown with YAML frontmatter. GitHub is the CMS: pull
requests are drafts, merged = published. A team of AI agents (Prospector,
Miner, Assayer, Smelter) extracts and refines content from books, papers, and
corpora.

## Project Structure

```
catalog/               Content
  mappings/            One markdown file per mapping (the main content)
  frames/              Conceptual domains (source and target)
  categories/          Taxonomy labels for cross-cutting classification
site/                  Astro site powering metaphorex.org
scripts/               Validation and extraction tools
playbooks/             Import project playbooks and scripts
docs/                  Design documents and plans
.claude/               Agent pipeline (Claude Code plugin)
```

## Quick Start

### Browse

Visit [metaphorex.org](https://metaphorex.org), or read entries directly on
GitHub in [catalog/mappings/](catalog/mappings/). Each mapping has:

- **What It Brings** — the structural parallels that make it useful
- **Where It Breaks** — where the metaphor misleads (the most important section)
- **Expressions** — specific phrases and usages found in the wild

### Validate Content

```bash
uv run scripts/validate.py validate
```

Zero warnings, zero errors is the standard. The validator uses PEP 723 inline
deps — no virtual environment or install step required.

### Run the Site Locally

```bash
cd site
bun install
bun run dev       # dev server at localhost:4321
bun run build     # production build (Astro + Pagefind search index)
bun run preview   # preview the production build
```

The site is built with [Astro](https://astro.build) and uses
[Pagefind](https://pagefind.app) for search. It deploys to GitHub Pages
nightly via CI, so new content merged to `main` goes live the next day.
You can also trigger a deploy manually from the Actions tab.

## Contributing

Contributions from both humans and agents are welcome. The easiest ways to
start:

- **Drop a metaphor** — file a [nugget issue](https://github.com/metaphorex/metaphorex/issues/new?template=nugget.yml)
  with a metaphor you noticed. Agents will expand it into a full entry.
- **Propose a source** — file an [import project issue](https://github.com/metaphorex/metaphorex/issues/new?template=import-project.yml)
  to mine a book, paper, or corpus for metaphors.
- **Edit an entry** — open a PR improving any catalog content with examples
  from your field, additional references, or sharper analysis.
- **Write a full entry** — create a mapping markdown file with the required
  frontmatter, validate, and open a PR.

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines, schema details,
editorial standards, and writing style.

## License

Content (`catalog/`, `playbooks/`) is licensed under
[CC BY-SA 4.0](LICENSE-CC-BY-SA-4.0). Code is licensed under
[MIT](LICENSE-MIT). See [LICENSE](LICENSE) for details.
