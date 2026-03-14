# Batch Improvements Design

Date: 2026-03-12

## Overview

Five improvements to the Metaphorex site and catalog, designed as a batch.
Each is independent and can ship in any order.

1. Colophon page
2. Category expansion
3. Agents identity page
4. Mechanical contributor attribution
5. Graph exploration script

Two topics surfaced during brainstorming but remain open questions, recorded
at the end.

## 1. Colophon Page

### What

A single `/colophon` page on the Astro site covering project motivation,
goals and non-goals, how Metaphorex is assembled, and a welcome to
contributors.

### Why

The site has zero meta-pages. All context about the project lives in GitHub
README/CONTRIBUTING files that site visitors never see. A colophon bridges
that gap.

### How

Add `site/src/pages/colophon.astro`. Hand-write the content directly in the
template (no content collection — it's one page). Add "Colophon" to the nav
in `Base.astro`.

Sections:
- **What Metaphorex Is** — a knowledge graph of metaphors across all domains
- **Goals** — catalog conceptual metaphors, design patterns, archetypes, and
  cross-field mappings; make them searchable, linkable, citable
- **Non-Goals** — not an encyclopedia, not a dictionary, not an academic
  journal; no paywalls, no login
- **How It's Built** — markdown files with YAML frontmatter, GitHub as CMS,
  agents extract and refine content, humans review and merge
- **Contributing** — link to CONTRIBUTING.md, explain the nugget and
  import-project issue templates, mention that agents do the heavy lifting
  but humans direct the work

### Dependencies

None. Ships standalone.

## 2. Category Expansion

### What

Expand categories from 11 to ~20, using broad disciplinary buckets inspired
(loosely) by the Dewey Decimal system. Categories should cover fields of
human knowledge, not narrow topics.

### Why

The current 11 categories cluster around cognitive-science, linguistics,
software-engineering, and philosophy. Entries touching economics, medicine,
biology, morality, and mythology lack proper homes. The pending
cognitive-linguistics-canon issues (156 entries) and open veins (AI moment,
Jungian archetypes, fantasy/mythology, sci-fi) will make this worse.

### Proposed New Categories

| Slug | Name | Rationale |
|------|------|-----------|
| biology-and-ecology | Biology and Ecology | survival-of-the-fittest, gardening metaphors, people-are-plants |
| economics-and-finance | Economics and Finance | time-is-money, ideas-are-commodities, money-is-a-liquid cluster in pending |
| education-and-learning | Education and Learning | understanding-is-seeing, knowing-is-grasping, many pending entries |
| ethics-and-morality | Ethics and Morality | morality-is-accounting, morality-is-purity — large cluster in pending canon |
| health-and-medicine | Health and Medicine | treating-illness-is-fighting-a-war, love-is-a-patient, health-is-up |
| law-and-governance | Law and Governance | the-commons, social-accounting, obligations-are-forces |
| mathematics-and-logic | Mathematics and Logic | logic-is-gravity, linear-scales-are-paths |
| mythology-and-religion | Mythology and Religion | the-trickster, Jungian archetypes vein, great-chain-of-being |
| physics-and-engineering | Physics and Engineering | causes-are-forces, a-force-is-a-moving-object, physical-force frames |

### How

1. Create 9 new category files in `catalog/categories/`
2. Backfill existing mappings that belong in new categories (mechanical —
   smelter agent or script)
3. Run validator to confirm zero warnings

Existing categories remain unchanged. No hierarchy (`broader` field) yet —
revisit when the catalog outgrows flat buckets.

### Dependencies

Backfill touches many mapping files. Best done as one PR per new category
or one large batch PR.

## 3. Agents Identity Page

### What

A hand-written `/agents` page on the site listing each agent (Prospector,
Miner, Assayer, Smelter) with a description, the `author` string it uses in
frontmatter, and a link to its definition on GitHub.

### Why

140 of 153 mappings are authored by `agent:metaphorex-miner`. That string
appears on every mapping detail page with no explanation and no link. Visitors
deserve to know what the miner is, how it works, and where its code lives.

### How

Add `site/src/pages/agents.astro`. Hand-write the content. For each agent:
- Name and one-paragraph role description
- The `author` string it uses (e.g., `agent:metaphorex-miner`)
- Link to `.claude/agents/<name>.md` on GitHub

Update the mapping detail page (`site/src/pages/mappings/[slug].astro`) to
render any `author` value starting with `agent:` as a link to `/agents#<name>`.

### Dependencies

None. Ships standalone. The link rendering is a small template change.

## 4. Mechanical Contributor Attribution

### What

A script (integrated into the smelter pipeline) that populates the
`contributors[]` frontmatter field from GitHub activity.

### Why

Metaphorex should be generous in recognizing everyone who contributed:
issue filers who suggested a metaphor, operators who ran agents, editors
who improved prose. Currently `contributors: []` on nearly every entry.

### Attribution Sources

For each mapping file, the script:

1. Finds the PR that introduced it (from git history)
2. Finds any issue linked in the PR body or branch name
3. Extracts the **issue filer's** GitHub username (the person who said
   "you should add this metaphor")
4. Extracts all **PR authors** who touched the file (from subsequent PRs)
5. Deduplicates against the `author` field
6. Writes the result to `contributors[]`

### How

A Python script (`scripts/backfill_contributors.py`, PEP 723 inline deps)
that uses the `gh` CLI to query GitHub. Can run standalone for the initial
backfill, then integrate as a smelter step for ongoing maintenance.

The script opens a single PR with all changes. A smelter-class agent (small
model) can run this periodically.

### Schema Impact

No schema change. `contributors[]` already exists in the frontmatter spec
and Astro content schema. The validator already accepts it.

### Dependencies

Requires `gh` CLI authenticated. Touches many files — best as its own PR.

## 5. Graph Exploration Script

### What

A one-off Python script that builds a frame-to-frame directed graph from
the catalog and outputs visual and statistical analysis.

### Why

The catalog is a graph: mappings connect source frames to target frames.
Before investing in graph visualization features for the site, we need to
know whether the graph reveals interesting structure — multi-hop paths
connecting distant domains, hub frames, isolated clusters — or is just a
novelty.

### How

Add `scripts/graph_explore.py` (PEP 723 inline deps: networkx, matplotlib,
pyyaml). Reads all mapping frontmatter, builds a directed graph where nodes
are frames and edges are mappings.

Outputs:
- **PNG/SVG** of the full graph (force-directed layout, nodes sized by degree)
- **Hub analysis** — frames with the most connections (highest degree)
- **Diameter** — longest shortest path in the graph
- **Components** — is it one connected blob or separate islands?
- **Example paths** — a few multi-hop paths between distant frames

No site integration. No build step. Run it, look at the output, decide
whether to pursue graph features.

### Dependencies

None. Standalone script.

## Open Questions

### Pipeline Architecture

The validator (`scripts/validate.py`) is currently a linter. There is
appetite to evolve it toward a build pipeline that:

1. Validates (current behavior)
2. Extracts structured data (all frontmatter → JSON or SQLite)
3. Derives computed artifacts (graph data, contributor rolls, stats)

This extracted DB could feed the Astro site, graph tools, and search
indexing (similar to Pagefind's approach). Decision deferred until a
concrete consumer beyond "peek at the graph" materializes.

### Issue Templates

The project has two issue templates (nugget, import-project) but lacks
templates for feature/site suggestions and editorial feedback. Design
deferred — the need is real but the shape is unclear.
