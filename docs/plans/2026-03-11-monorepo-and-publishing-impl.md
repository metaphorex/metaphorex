# Monorepo and Publishing Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Consolidate agents into a monorepo and launch metaphorex.org with Astro + Pagefind + llms.txt today.

**Architecture:** Merge agents repo history via `--allow-unrelated-histories`, reorganize into target directory layout, scaffold Astro site with Content Collections reading from `catalog/` via symlink, deploy to GitHub Pages on a nightly + manual dispatch schedule.

**Tech Stack:** Astro 5, Pagefind, Bun, GitHub Pages, GitHub Actions

---

### Task 1: Merge Agents Repo History

**Files:**
- Modify: all files from agents repo (relocated)
- Create: `.claude/VERSION`

**Step 1: Ensure clean working tree on main**

```bash
cd /Users/fshot/code/fshot/metaphorex
git checkout main
git pull origin main
git status  # must be clean
```

Expected: clean working tree, up to date with origin/main.

**Step 2: Create a working branch**

```bash
git checkout -b chore/monorepo-consolidation
```

**Step 3: Add agents remote and fetch**

```bash
git remote add agents git@github.com:metaphorex/agents.git
git fetch agents
```

Expected: remote added, branches fetched.

**Step 4: Merge with --allow-unrelated-histories --no-commit**

```bash
git merge agents/main --allow-unrelated-histories --no-commit
```

Expected: files from agents repo appear at repo root alongside existing files. Merge paused (no commit yet). There should be no conflicts since the repos have no overlapping paths (agents has `agents/`, `commands/`, `skills/`, `scripts/survey.py`, `projects/`; content has `catalog/`, `scripts/validate.py`, `scripts/stats.py`, `docs/`).

If there are conflicts in `CONTRIBUTING.md`, `LICENSE`, or `README.md`, keep the content repo versions — these are more complete.

**Step 5: Relocate agents files to target directories**

```bash
# Agents, commands, skills -> .claude/
mkdir -p .claude/agents .claude/commands .claude/skills
git mv agents/*.md .claude/agents/
git mv commands/*.md .claude/commands/
git mv skills/metaphorex-schema .claude/skills/

# Playbooks
mkdir -p playbooks
git mv projects/design-patterns playbooks/

# Survey script joins other scripts
git mv scripts/survey.py scripts/survey.py  # already in scripts/ — handle collision
# If survey.py conflicts with scripts/ dir, move manually:
# mv survey.py scripts/survey.py && git add scripts/survey.py

# Remove agents-repo artifacts we don't need in monorepo
git rm -r content-repo 2>/dev/null || true
git rm -r .claude-plugin 2>/dev/null || true
git rm -r agents 2>/dev/null || true
git rm -r commands 2>/dev/null || true
git rm -r skills 2>/dev/null || true
git rm -r projects 2>/dev/null || true
git rm CODEOWNERS 2>/dev/null || true
```

Note: The agents repo has `scripts/survey.py` and the content repo has `scripts/validate.py` and `scripts/stats.py`. These should coexist in `scripts/` — no collision on filenames. If `git mv` complains because `scripts/` already exists, just `mv` the file and `git add` it.

**Step 6: Create agent suite version file**

Create `.claude/VERSION` with content:
```
0.1.0
```

**Step 7: Remove the agents-repo README/LICENSE/CONTRIBUTING (keep content-repo versions)**

```bash
# The merge brought in agents-repo versions — these are already staged
# If there are merge conflicts on these files, resolve by keeping content-repo versions
git checkout HEAD -- README.md LICENSE CONTRIBUTING.md 2>/dev/null || true
```

**Step 8: Commit the merge**

```bash
git add -A
git commit -m "Merge agents repo into monorepo

Brings full commit history from metaphorex/agents. Files relocated:
- agents/, commands/, skills/ -> .claude/
- projects/ -> playbooks/
- scripts/survey.py -> scripts/
- Removed: content-repo/, .claude-plugin/, CODEOWNERS

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

**Step 9: Remove the temporary remote**

```bash
git remote remove agents
```

**Step 10: Verify history is preserved**

```bash
git log --oneline -- .claude/agents/miner.md | head -5
```

Expected: commits from the agents repo appear in the log.

**Human verification:** Run `git log --all --oneline | wc -l` — should show combined commit count from both repos. Run `ls .claude/agents/` — should show `prospector.md miner.md assayer.md smelter.md surveyor.md`. Run `ls playbooks/` — should show `design-patterns/`.

---

### Task 2: Update Agent Prompts for Monorepo Paths

**Files:**
- Modify: `.claude/agents/prospector.md`
- Modify: `.claude/agents/miner.md`
- Modify: `.claude/agents/assayer.md`
- Modify: `.claude/agents/smelter.md`
- Modify: `.claude/agents/surveyor.md`
- Modify: `.claude/commands/work.md`
- Modify: `.claude/commands/mine.md`
- Modify: `.claude/commands/prospect.md`
- Modify: `.claude/commands/assay.md`
- Modify: `.claude/commands/smelt.md`

**Step 1: Audit all agent/command files for cross-repo references**

Search for patterns that reference the old two-repo setup:
- `content-repo/` or `content_repo`
- `metaphorex/agents` (as a repo reference, not a directory)
- `metaphorex/metaphorex` (as a separate repo)
- Any `git clone` or `git remote` commands pointing to the agents repo
- References to `.claude-plugin/plugin.json`

```bash
grep -rn "content-repo\|content_repo\|metaphorex/agents\|metaphorex/metaphorex\|\.claude-plugin" .claude/
```

**Step 2: Update each file**

For each match found:
- Replace `content-repo/catalog/` with `catalog/`
- Replace references to "the content repo" or "metaphorex/metaphorex" with "this repo" or just remove the qualifier
- Replace `metaphorex/agents` repo references with "the `.claude/` directory"
- Update any `git clone` commands that set up the content-repo checkout — these are no longer needed
- Update playbook paths from `projects/` to `playbooks/`

**Step 3: Update survey.py if it has cross-repo paths**

```bash
grep -n "content.repo\|agents.*repo\|metaphorex/agents" scripts/survey.py
```

Fix any hardcoded paths.

**Step 4: Commit**

```bash
git add .claude/ scripts/survey.py
git commit -m "Update agent prompts and scripts for monorepo paths

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

**Human verification:** Read through `.claude/agents/miner.md` — it should not reference any external repo or `content-repo/` path.

---

### Task 3: Add AGENTS.md and Symlink

**Files:**
- Create: `AGENTS.md`
- Create: `CLAUDE.md` (symlink)

**Step 1: Write AGENTS.md**

Create `AGENTS.md` at repo root. Content should be a vendor-neutral project guide covering:
- What this repo is (one paragraph)
- How to build/test: `uv run scripts/validate.py validate`
- Directory structure (catalog/, playbooks/, site/, .claude/, scripts/)
- Content schema summary (mapping frontmatter fields, required body sections)
- How to contribute (link to CONTRIBUTING.md)
- Key conventions: slug-based filenames, zero warnings precedent, frames included in same PR

Keep it under 100 lines. This is for AI assistants, not humans — terse and structural.

**Step 2: Create CLAUDE.md symlink**

```bash
ln -s AGENTS.md CLAUDE.md
git add AGENTS.md CLAUDE.md
```

**Step 3: Commit**

```bash
git commit -m "Add AGENTS.md with CLAUDE.md symlink

Vendor-neutral project instructions for AI coding assistants.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

**Human verification:** `cat CLAUDE.md` should output the same content as `cat AGENTS.md`. `ls -la CLAUDE.md` should show it's a symlink.

---

### Task 4: Scaffold Astro Project

**Files:**
- Create: `site/package.json`
- Create: `site/astro.config.ts`
- Create: `site/tsconfig.json`
- Create: `site/src/content.config.ts`
- Create: `site/src/content` (symlink to `../../catalog`)

**Step 1: Initialize Astro project**

```bash
cd /Users/fshot/code/fshot/metaphorex
mkdir -p site
cd site
bun create astro@latest . -- --template minimal --no-install --no-git --typescript strict
bun install
```

If `bun create astro` doesn't support those flags exactly, create manually:

```bash
mkdir -p site/src/pages site/src/layouts site/public
```

Then create `site/package.json`:
```json
{
  "name": "metaphorex-site",
  "type": "module",
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  },
  "dependencies": {
    "astro": "^5"
  }
}
```

```bash
cd site && bun install
```

**Step 2: Create astro.config.ts**

```typescript
import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://metaphorex.org",
  output: "static",
});
```

**Step 3: Create tsconfig.json**

```json
{
  "extends": "astro/tsconfigs/strict",
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  }
}
```

**Step 4: Symlink content**

```bash
cd /Users/fshot/code/fshot/metaphorex/site/src
ln -s ../../catalog content
```

Verify: `ls -la site/src/content/mappings/` should list mapping files.

**Step 5: Create content.config.ts**

Create `site/src/content.config.ts`:

```typescript
import { defineCollection, z } from "astro:content";

const mappings = defineCollection({
  type: "content",
  schema: z.object({
    slug: z.string(),
    name: z.string(),
    kind: z.enum([
      "conceptual-metaphor",
      "design-pattern",
      "archetype",
      "paradigm",
      "cross-field-mapping",
      "dead-metaphor",
    ]),
    source_frame: z.string(),
    target_frame: z.string(),
    categories: z.array(z.string()),
    author: z.string(),
    contributors: z.array(z.string()).default([]),
    related: z.array(z.string()).default([]),
    deprecated: z.boolean().optional(),
    harness: z.string().optional(),
  }),
});

const frames = defineCollection({
  type: "content",
  schema: z.object({
    slug: z.string(),
    name: z.string(),
    broader: z.string().optional(),
    related: z.array(z.string()).default([]),
    roles: z.array(z.string()),
  }),
});

const categories = defineCollection({
  type: "content",
  schema: z.object({
    slug: z.string(),
    name: z.string(),
    broader: z.string().optional(),
    related: z.array(z.string()).default([]),
  }),
});

export const collections = { mappings, frames, categories };
```

**Step 6: Verify build runs**

```bash
cd /Users/fshot/code/fshot/metaphorex/site
bun run build
```

Expected: Astro builds successfully with content collections loaded. May show warnings if any frontmatter doesn't match schema — fix those before continuing.

**Step 7: Commit**

```bash
cd /Users/fshot/code/fshot/metaphorex
git add site/
git commit -m "Scaffold Astro site with content collections

Symlinks site/src/content -> catalog/ so Astro reads mappings,
frames, and categories directly. Zod schemas validate frontmatter
at build time.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

**Human verification:** `cd site && bun run build` succeeds. `ls site/src/content/mappings/` lists mapping files.

---

### Task 5: Build Site Layout and Pages

**Files:**
- Create: `site/src/layouts/Base.astro`
- Create: `site/src/pages/index.astro`
- Create: `site/src/pages/mappings/index.astro`
- Create: `site/src/pages/mappings/[slug].astro`
- Create: `site/src/pages/frames/index.astro`
- Create: `site/src/pages/frames/[slug].astro`
- Create: `site/src/pages/categories/index.astro`
- Create: `site/src/pages/categories/[slug].astro`

**Step 1: Create Base layout**

Create `site/src/layouts/Base.astro`:

```astro
---
interface Props {
  title: string;
  description?: string;
}

const { title, description = "A knowledge graph of metaphors" } = Astro.props;
const corpusVersion = new Date().toISOString().split("T")[0].replace(/-/g, ".");
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content={description} />
    <title>{title} | Metaphorex</title>
    <style>
      :root {
        --max-width: 48rem;
        --font-mono: "SF Mono", "Fira Code", monospace;
        --font-sans: system-ui, -apple-system, sans-serif;
        --bg: #fafaf9;
        --fg: #1c1917;
        --muted: #78716c;
        --border: #e7e5e4;
        --accent: #2563eb;
      }
      * { margin: 0; padding: 0; box-sizing: border-box; }
      body {
        font-family: var(--font-sans);
        color: var(--fg);
        background: var(--bg);
        line-height: 1.6;
        max-width: var(--max-width);
        margin: 0 auto;
        padding: 2rem 1rem;
      }
      a { color: var(--accent); text-decoration: none; }
      a:hover { text-decoration: underline; }
      nav { margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 1px solid var(--border); }
      nav a { margin-right: 1.5rem; }
      footer { margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--border); color: var(--muted); font-size: 0.875rem; }
      h1 { font-size: 1.5rem; margin-bottom: 0.5rem; }
      h2 { font-size: 1.25rem; margin: 1.5rem 0 0.5rem; }
      h3 { font-size: 1.1rem; margin: 1rem 0 0.25rem; }
      .tag { display: inline-block; font-size: 0.75rem; padding: 0.125rem 0.5rem; background: var(--border); border-radius: 0.25rem; margin: 0.125rem; }
      .muted { color: var(--muted); }
      .entry-list { list-style: none; }
      .entry-list li { padding: 0.5rem 0; border-bottom: 1px solid var(--border); }
      .entry-list li:last-child { border-bottom: none; }
      article { line-height: 1.7; }
      article h2 { margin-top: 2rem; }
      article ul, article ol { margin-left: 1.5rem; margin-bottom: 1rem; }
      article p { margin-bottom: 1rem; }
    </style>
  </head>
  <body>
    <nav>
      <a href="/"><strong>Metaphorex</strong></a>
      <a href="/mappings/">Mappings</a>
      <a href="/frames/">Frames</a>
      <a href="/categories/">Categories</a>
    </nav>
    <slot />
    <footer>
      Metaphorex {corpusVersion} &middot;
      <a href="https://github.com/metaphorex/metaphorex">GitHub</a> &middot;
      CC BY-SA 4.0
    </footer>
  </body>
</html>
```

**Step 2: Create homepage**

Create `site/src/pages/index.astro`:

```astro
---
import Base from "@/layouts/Base.astro";
import { getCollection } from "astro:content";

const mappings = await getCollection("mappings");
const frames = await getCollection("frames");
const categories = await getCollection("categories");

const recent = mappings
  .sort((a, b) => a.data.name.localeCompare(b.data.name))
  .slice(0, 10);
---

<Base title="Home">
  <h1>Metaphorex</h1>
  <p>A knowledge graph of metaphors — how we borrow structure from one domain to understand another.</p>

  <h2>Corpus</h2>
  <p>
    <strong>{mappings.length}</strong> mappings &middot;
    <strong>{frames.length}</strong> frames &middot;
    <strong>{categories.length}</strong> categories
  </p>

  <h2>Browse</h2>
  <ul>
    <li><a href="/mappings/">All mappings</a> — conceptual metaphors, design patterns, archetypes</li>
    <li><a href="/frames/">All frames</a> — source and target domains</li>
    <li><a href="/categories/">All categories</a> — cross-cutting taxonomy</li>
  </ul>

  <h2>Sample Mappings</h2>
  <ul class="entry-list">
    {recent.map((m) => (
      <li>
        <a href={`/mappings/${m.data.slug}/`}>{m.data.name}</a>
        <span class="muted"> — {m.data.kind}</span>
      </li>
    ))}
  </ul>
</Base>
```

**Step 3: Create mappings list page**

Create `site/src/pages/mappings/index.astro`:

```astro
---
import Base from "@/layouts/Base.astro";
import { getCollection } from "astro:content";

const mappings = await getCollection("mappings");
const sorted = mappings.sort((a, b) => a.data.name.localeCompare(b.data.name));
---

<Base title="Mappings">
  <h1>Mappings ({mappings.length})</h1>
  <div id="search"></div>
  <ul class="entry-list" data-pagefind-body>
    {sorted.map((m) => (
      <li>
        <a href={`/mappings/${m.data.slug}/`}>{m.data.name}</a>
        <span class="tag">{m.data.kind}</span>
        <br />
        <span class="muted">
          {m.data.source_frame} &rarr; {m.data.target_frame}
        </span>
      </li>
    ))}
  </ul>
</Base>
```

**Step 4: Create single mapping page**

Create `site/src/pages/mappings/[slug].astro`:

```astro
---
import Base from "@/layouts/Base.astro";
import { getCollection, render } from "astro:content";

export async function getStaticPaths() {
  const mappings = await getCollection("mappings");
  return mappings.map((entry) => ({
    params: { slug: entry.data.slug },
    props: { entry },
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);

const allFrames = await getCollection("frames");
const sourceFrame = allFrames.find((f) => f.data.slug === entry.data.source_frame);
const targetFrame = allFrames.find((f) => f.data.slug === entry.data.target_frame);

const allMappings = await getCollection("mappings");
const related = entry.data.related
  .map((slug: string) => allMappings.find((m) => m.data.slug === slug))
  .filter(Boolean);
---

<Base title={entry.data.name} description={`${entry.data.name}: ${entry.data.source_frame} → ${entry.data.target_frame}`}>
  <article data-pagefind-body>
    <h1
      data-pagefind-meta={`kind:${entry.data.kind}`}
      data-pagefind-meta={`source_frame:${entry.data.source_frame}`}
      data-pagefind-meta={`target_frame:${entry.data.target_frame}`}
    >
      {entry.data.name}
    </h1>

    <p class="muted">
      <span class="tag">{entry.data.kind}</span>
      {sourceFrame
        ? <a href={`/frames/${sourceFrame.data.slug}/`}>{sourceFrame.data.name}</a>
        : entry.data.source_frame}
      &rarr;
      {targetFrame
        ? <a href={`/frames/${targetFrame.data.slug}/`}>{targetFrame.data.name}</a>
        : entry.data.target_frame}
    </p>

    <p class="muted">
      Categories: {entry.data.categories.map((c: string) => (
        <a href={`/categories/${c}/`} class="tag">{c}</a>
      ))}
    </p>

    <Content />

    {related.length > 0 && (
      <>
        <h2>Related Mappings</h2>
        <ul>
          {related.map((r: any) => (
            <li><a href={`/mappings/${r.data.slug}/`}>{r.data.name}</a></li>
          ))}
        </ul>
      </>
    )}
  </article>
</Base>
```

**Step 5: Create frames list page**

Create `site/src/pages/frames/index.astro`:

```astro
---
import Base from "@/layouts/Base.astro";
import { getCollection } from "astro:content";

const frames = await getCollection("frames");
const sorted = frames.sort((a, b) => a.data.name.localeCompare(b.data.name));
---

<Base title="Frames">
  <h1>Frames ({frames.length})</h1>
  <ul class="entry-list">
    {sorted.map((f) => (
      <li>
        <a href={`/frames/${f.data.slug}/`}>{f.data.name}</a>
        {f.data.broader && <span class="muted"> &larr; {f.data.broader}</span>}
      </li>
    ))}
  </ul>
</Base>
```

**Step 6: Create single frame page with reverse lookups**

Create `site/src/pages/frames/[slug].astro`:

```astro
---
import Base from "@/layouts/Base.astro";
import { getCollection, render } from "astro:content";

export async function getStaticPaths() {
  const frames = await getCollection("frames");
  return frames.map((entry) => ({
    params: { slug: entry.data.slug },
    props: { entry },
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);

const allMappings = await getCollection("mappings");
const asSource = allMappings.filter((m) => m.data.source_frame === entry.data.slug);
const asTarget = allMappings.filter((m) => m.data.target_frame === entry.data.slug);
---

<Base title={entry.data.name}>
  <article>
    <h1>{entry.data.name}</h1>

    {entry.data.broader && <p class="muted">Broader: {entry.data.broader}</p>}

    <p><strong>Roles:</strong> {entry.data.roles.join(", ")}</p>

    <Content />

    {asSource.length > 0 && (
      <>
        <h2>As Source Frame ({asSource.length})</h2>
        <ul>
          {asSource.map((m) => (
            <li><a href={`/mappings/${m.data.slug}/`}>{m.data.name}</a> &rarr; {m.data.target_frame}</li>
          ))}
        </ul>
      </>
    )}

    {asTarget.length > 0 && (
      <>
        <h2>As Target Frame ({asTarget.length})</h2>
        <ul>
          {asTarget.map((m) => (
            <li>{m.data.source_frame} &rarr; <a href={`/mappings/${m.data.slug}/`}>{m.data.name}</a></li>
          ))}
        </ul>
      </>
    )}
  </article>
</Base>
```

**Step 7: Create categories list page**

Create `site/src/pages/categories/index.astro`:

```astro
---
import Base from "@/layouts/Base.astro";
import { getCollection } from "astro:content";

const categories = await getCollection("categories");
const sorted = categories.sort((a, b) => a.data.name.localeCompare(b.data.name));
---

<Base title="Categories">
  <h1>Categories ({categories.length})</h1>
  <ul class="entry-list">
    {sorted.map((c) => (
      <li>
        <a href={`/categories/${c.data.slug}/`}>{c.data.name}</a>
        {c.data.broader && <span class="muted"> &larr; {c.data.broader}</span>}
      </li>
    ))}
  </ul>
</Base>
```

**Step 8: Create single category page**

Create `site/src/pages/categories/[slug].astro`:

```astro
---
import Base from "@/layouts/Base.astro";
import { getCollection, render } from "astro:content";

export async function getStaticPaths() {
  const categories = await getCollection("categories");
  return categories.map((entry) => ({
    params: { slug: entry.data.slug },
    props: { entry },
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);

const allMappings = await getCollection("mappings");
const members = allMappings
  .filter((m) => m.data.categories.includes(entry.data.slug))
  .sort((a, b) => a.data.name.localeCompare(b.data.name));
---

<Base title={entry.data.name}>
  <article>
    <h1>{entry.data.name}</h1>

    {entry.data.broader && <p class="muted">Broader: {entry.data.broader}</p>}

    <Content />

    <h2>Mappings ({members.length})</h2>
    <ul>
      {members.map((m) => (
        <li>
          <a href={`/mappings/${m.data.slug}/`}>{m.data.name}</a>
          <span class="tag">{m.data.kind}</span>
        </li>
      ))}
    </ul>
  </article>
</Base>
```

**Step 9: Test local build and dev server**

```bash
cd /Users/fshot/code/fshot/metaphorex/site
bun run build
```

Expected: Astro builds all pages successfully. Check output for page count — should be ~200 pages (132 mappings + 53 frames + 11 categories + index pages).

```bash
bun run dev
```

Visit `http://localhost:4321/` — verify homepage shows corpus stats. Click through to a mapping, frame, and category. Verify cross-reference links work.

**Step 10: Commit**

```bash
cd /Users/fshot/code/fshot/metaphorex
git add site/
git commit -m "Add site layouts and pages for all content types

Homepage, list pages, and detail pages for mappings, frames,
and categories. Cross-reference links resolve between entries.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

**Human verification:** `cd site && bun run dev` — browse `http://localhost:4321/mappings/argument-is-war/` and verify it shows the mapping content with links to the war and argumentation frames.

---

### Task 6: Add Pagefind Search

**Files:**
- Modify: `site/package.json` (add pagefind dep + build script)
- Modify: `site/src/layouts/Base.astro` (add search widget)

**Step 1: Install Pagefind**

```bash
cd /Users/fshot/code/fshot/metaphorex/site
bun add -D pagefind
```

**Step 2: Update build script in package.json**

Update the `build` script in `site/package.json`:

```json
"build": "astro build && pagefind --site dist"
```

**Step 3: Add Pagefind UI to the Base layout**

In `site/src/layouts/Base.astro`, add after the `<nav>` element and before `<slot />`:

```html
<link href="/_pagefind/pagefind-ui.css" rel="stylesheet" />
<script src="/_pagefind/pagefind-ui.js" is:inline></script>
<div id="search"></div>
<script is:inline>
  new PagefindUI({ element: "#search", showSubResults: true });
</script>
```

Add CSS for the search widget:

```css
#search { margin-bottom: 1.5rem; }
```

Note: The Pagefind assets only exist after build, so `bun run dev` won't show search. That's fine — search works in production and `bun run preview`.

**Step 4: Build and test**

```bash
cd /Users/fshot/code/fshot/metaphorex/site
bun run build
bun run preview
```

Visit `http://localhost:4321/`, type "argument" in search — should show Argument Is War and related mappings.

**Step 5: Commit**

```bash
cd /Users/fshot/code/fshot/metaphorex
git add site/
git commit -m "Add Pagefind search to site

Post-build indexing with client-side search UI. Index includes
mapping names, body text, and frontmatter metadata.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

**Human verification:** `cd site && bun run build && bun run preview` — search for "war" and verify results appear.

---

### Task 7: Add llms.txt and llms-full.txt

**Files:**
- Create: `site/src/pages/llms.txt.ts`
- Create: `site/src/pages/llms-full.txt.ts`

**Step 1: Create llms.txt endpoint**

Create `site/src/pages/llms.txt.ts`:

```typescript
import { getCollection } from "astro:content";

export async function GET() {
  const mappings = await getCollection("mappings");
  const frames = await getCollection("frames");
  const categories = await getCollection("categories");

  const sortedMappings = mappings.sort((a, b) =>
    a.data.name.localeCompare(b.data.name)
  );
  const sortedFrames = frames.sort((a, b) =>
    a.data.name.localeCompare(b.data.name)
  );
  const sortedCategories = categories.sort((a, b) =>
    a.data.name.localeCompare(b.data.name)
  );

  const version = new Date().toISOString().split("T")[0].replace(/-/g, ".");

  const lines = [
    "# Metaphorex",
    "",
    `> A knowledge graph of metaphors. Version ${version}. ${mappings.length} mappings, ${frames.length} frames, ${categories.length} categories.`,
    "",
    "Metaphorex catalogs conceptual metaphors, design patterns, archetypes, and cross-field mappings. Each mapping connects a source frame to a target frame and documents what the metaphor brings and where it breaks.",
    "",
    `## Mappings (${mappings.length})`,
    "",
    ...sortedMappings.map(
      (m) =>
        `- [${m.data.name}](https://metaphorex.org/mappings/${m.data.slug}/): ${m.data.source_frame} -> ${m.data.target_frame} (${m.data.kind})`
    ),
    "",
    `## Frames (${frames.length})`,
    "",
    ...sortedFrames.map(
      (f) =>
        `- [${f.data.name}](https://metaphorex.org/frames/${f.data.slug}/): roles: ${f.data.roles.join(", ")}`
    ),
    "",
    `## Categories (${categories.length})`,
    "",
    ...sortedCategories.map(
      (c) =>
        `- [${c.data.name}](https://metaphorex.org/categories/${c.data.slug}/)`
    ),
  ];

  return new Response(lines.join("\n"), {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
}
```

**Step 2: Create llms-full.txt endpoint**

Create `site/src/pages/llms-full.txt.ts`:

```typescript
import { getCollection } from "astro:content";

export async function GET() {
  const mappings = await getCollection("mappings");
  const frames = await getCollection("frames");
  const categories = await getCollection("categories");

  const sortedMappings = mappings.sort((a, b) =>
    a.data.name.localeCompare(b.data.name)
  );

  const version = new Date().toISOString().split("T")[0].replace(/-/g, ".");

  const sections: string[] = [
    "# Metaphorex (Full)",
    "",
    `> Version ${version}. ${mappings.length} mappings, ${frames.length} frames, ${categories.length} categories.`,
    "",
  ];

  for (const m of sortedMappings) {
    sections.push(`## ${m.data.name}`);
    sections.push("");
    sections.push(
      `**Kind:** ${m.data.kind} | **Source:** ${m.data.source_frame} | **Target:** ${m.data.target_frame} | **Categories:** ${m.data.categories.join(", ")}`
    );
    sections.push("");
    sections.push(m.body || "");
    sections.push("");
    sections.push("---");
    sections.push("");
  }

  return new Response(sections.join("\n"), {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
}
```

**Step 3: Build and verify**

```bash
cd /Users/fshot/code/fshot/metaphorex/site
bun run build
cat dist/llms.txt | head -30
cat dist/llms-full.txt | wc -l
```

Expected: `llms.txt` shows structured index with all entries. `llms-full.txt` is larger with full body content.

**Step 4: Commit**

```bash
cd /Users/fshot/code/fshot/metaphorex
git add site/src/pages/llms.txt.ts site/src/pages/llms-full.txt.ts
git commit -m "Add llms.txt and llms-full.txt endpoints

Structured index and full content dump for LLM crawlers.
Auto-generated from content collections at build time.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

**Human verification:** `curl http://localhost:4321/llms.txt | head -20` shows the structured index starting with `# Metaphorex`.

---

### Task 8: GitHub Pages Deployment Workflow

**Files:**
- Create: `.github/workflows/deploy-site.yml`
- Create: `site/public/CNAME`

**Step 1: Create CNAME file**

Create `site/public/CNAME`:

```
metaphorex.org
```

**Step 2: Create deployment workflow**

Create `.github/workflows/deploy-site.yml`:

```yaml
name: Deploy site

on:
  schedule:
    - cron: "0 4 * * *"
  workflow_dispatch: {}

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: oven-sh/setup-bun@v2

      - name: Install dependencies
        working-directory: site
        run: bun install --frozen-lockfile

      - name: Build site
        working-directory: site
        run: bun run build

      - uses: actions/upload-pages-artifact@v3
        with:
          path: site/dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

**Step 3: Add .gitignore for site build artifacts**

Create `site/.gitignore`:

```
node_modules/
dist/
.astro/
```

**Step 4: Commit**

```bash
cd /Users/fshot/code/fshot/metaphorex
git add .github/workflows/deploy-site.yml site/public/CNAME site/.gitignore
git commit -m "Add GitHub Pages deployment workflow

Nightly at 4am UTC + manual dispatch. Builds Astro + Pagefind,
deploys to GitHub Pages with custom domain metaphorex.org.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

**Step 5: Configure GitHub Pages (manual steps)**

After merging to main:
1. Go to GitHub repo Settings > Pages
2. Set Source to "GitHub Actions"
3. Add custom domain `metaphorex.org`
4. Configure DNS: CNAME record `metaphorex.org` -> `metaphorex.github.io`
   (or A records for apex domain — GitHub docs specify the IPs)
5. Trigger the workflow manually: Actions > Deploy site > Run workflow

**Human verification:** After first deploy, visit `https://metaphorex.org/` — should show the homepage. Visit `/llms.txt` — should show the structured index.

---

### Task 9: Push and Create PR

**Step 1: Push the branch**

```bash
git push -u origin chore/monorepo-consolidation
```

**Step 2: Create PR**

```bash
gh pr create --title "Consolidate agents repo + launch metaphorex.org" --body "$(cat <<'EOF'
## Summary

- Merge agents repo history into monorepo (full commit history preserved)
- Relocate agents/commands/skills to `.claude/`, playbooks to `playbooks/`
- Add AGENTS.md with CLAUDE.md symlink
- Scaffold Astro site with Content Collections reading from `catalog/`
- Add Pagefind search, llms.txt, and llms-full.txt
- Add GitHub Pages deployment workflow (nightly + manual dispatch)
- Add agent suite versioning (`.claude/VERSION`)

## Test plan

- [ ] `cd site && bun run build` succeeds
- [ ] `bun run preview` — homepage shows corpus stats
- [ ] Search for "war" returns results
- [ ] `/mappings/argument-is-war/` shows content with frame links
- [ ] `/llms.txt` returns structured index
- [ ] `.claude/agents/miner.md` has no cross-repo references
- [ ] `git log -- .claude/agents/miner.md` shows agents repo history
- [ ] Manually trigger deploy workflow after merge

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

**Human verification:** PR shows combined diff of agents merge + site scaffold. CI validation passes (existing `validate.yml` should still work — site files don't affect it).

---

### Task 10: Post-Merge DNS and First Deploy

This task is manual — performed after the PR is merged.

**Step 1: Configure DNS for metaphorex.org**

Add DNS records (at your registrar or Cloudflare):
- If using apex domain: A records pointing to GitHub Pages IPs (185.199.108-111.153)
- If using www subdomain: CNAME `www.metaphorex.org` -> `metaphorex.github.io`

**Step 2: Enable GitHub Pages**

1. Repo Settings > Pages > Source: GitHub Actions
2. Custom domain: `metaphorex.org`
3. Enforce HTTPS: checked

**Step 3: Trigger first deploy**

Actions > Deploy site > Run workflow > Run

**Step 4: Verify**

- `https://metaphorex.org/` loads
- `https://metaphorex.org/llms.txt` returns structured index
- `https://metaphorex.org/mappings/argument-is-war/` shows content
- Search works

**Human verification:** All four URLs above return expected content with HTTPS.
