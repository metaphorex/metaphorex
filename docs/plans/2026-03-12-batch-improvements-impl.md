# Batch Improvements Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Ship five independent improvements: colophon page, category expansion, agents page, contributor backfill script, and graph exploration script.

**Architecture:** Each task is standalone — no dependencies between them. All site pages use the existing `Base.astro` layout. Scripts follow the PEP 723 inline-deps pattern established by `validate.py`. Categories and mappings follow the existing frontmatter schema.

**Tech Stack:** Astro (site pages), Python + PEP 723 (scripts), `gh` CLI (GitHub queries), networkx + matplotlib (graph)

---

### Task 1: Colophon Page

**Files:**
- Create: `site/src/pages/colophon.astro`
- Modify: `site/src/layouts/Base.astro:309-313`

**Step 1: Add nav link**

In `site/src/layouts/Base.astro`, add "Colophon" to the nav links span:

```astro
<span class="nav-links">
  <a href="/mappings/">Mappings</a>
  <a href="/frames/">Frames</a>
  <a href="/categories/">Categories</a>
  <a href="/colophon/">Colophon</a>
</span>
```

**Step 2: Create the colophon page**

Create `site/src/pages/colophon.astro`:

```astro
---
import Base from "@/layouts/Base.astro";
---

<Base title="Colophon" description="How Metaphorex is built, why it exists, and how to contribute">
  <article>
    <h1>Colophon</h1>

    <h2>What Metaphorex Is</h2>
    <p>
      Metaphorex is a knowledge graph of metaphors — conceptual metaphors,
      design patterns, archetypes, and cross-field mappings. Each entry maps
      a source domain onto a target domain, documents what the metaphor
      illuminates, where it breaks down, and how it surfaces in everyday
      language.
    </p>

    <h2>Goals</h2>
    <ul>
      <li>Catalog metaphors across all fields of human knowledge</li>
      <li>Make them searchable, linkable, and citable</li>
      <li>Surface where metaphors fail, not just where they work</li>
      <li>Remain open: no paywall, no login, CC BY-SA 4.0</li>
    </ul>

    <h2>Non-Goals</h2>
    <ul>
      <li>Not an encyclopedia — entries are concise, not exhaustive</li>
      <li>Not an academic journal — no peer review, no impact factor</li>
      <li>Not a dictionary — structure matters more than definitions</li>
    </ul>

    <h2>How It's Built</h2>
    <p>
      Every entry is a Markdown file with YAML frontmatter, stored in a
      <a href="https://github.com/metaphorex/metaphorex">GitHub repository</a>.
      GitHub is the CMS: pull requests are drafts, merged is published.
    </p>
    <p>
      A team of <a href="/agents/">AI agents</a> extracts and refines content
      from books, papers, and corpora. Humans direct the work, review every
      PR, and make editorial decisions. The <code>harness</code> field in
      frontmatter records which tool generated the prose; the
      <code>author</code> field records who directed the framing.
    </p>
    <p>
      The site is built with <a href="https://astro.build">Astro</a> and
      deployed to GitHub Pages. Search is powered by
      <a href="https://pagefind.app">Pagefind</a>.
    </p>

    <h2>Contributing</h2>
    <p>
      Contributions are welcome. The easiest way to start:
    </p>
    <ul>
      <li>
        <strong>Drop a metaphor</strong> — file a
        <a href="https://github.com/metaphorex/metaphorex/issues/new?template=nugget.yml">nugget issue</a>
        with a metaphor you noticed. Agents will expand it into a full entry.
      </li>
      <li>
        <strong>Propose a source</strong> — file an
        <a href="https://github.com/metaphorex/metaphorex/issues/new?template=import-project.yml">import project issue</a>
        to mine a book, paper, or corpus for metaphors.
      </li>
      <li>
        <strong>Edit an entry</strong> — open a PR. The "Where It Breaks" section
        always needs the most work.
      </li>
    </ul>
    <p>
      See <a href="https://github.com/metaphorex/metaphorex/blob/main/CONTRIBUTING.md">CONTRIBUTING.md</a>
      for full guidelines.
    </p>
  </article>
</Base>
```

**Step 3: Build and verify**

Run:
```bash
cd site && bun run build
```
Expected: Build succeeds. Verify by checking `site/dist/colophon/index.html` exists.

**Step 4: Commit**

```bash
git add site/src/pages/colophon.astro site/src/layouts/Base.astro
git commit -m "Add colophon page with project overview and contributor welcome"
```

**Human verification:** Visit `/colophon/` in dev server. Nav shows five links. Page has five sections. All external links work.

---

### Task 2: Category Expansion — Create Category Files

**Files:**
- Create: 9 files in `catalog/categories/`

**Step 1: Create all 9 category files**

Each follows the same format as existing categories (see `catalog/categories/cognitive-science.md`). Create these files:

`catalog/categories/biology-and-ecology.md`:
```markdown
---
slug: biology-and-ecology
name: "Biology and Ecology"
related:
  - health-and-medicine
  - systems-thinking
---

Metaphors drawn from living systems — evolution, growth, ecosystems,
symbiosis, predation, and the life cycle.
```

`catalog/categories/economics-and-finance.md`:
```markdown
---
slug: economics-and-finance
name: "Economics and Finance"
related:
  - organizational-behavior
  - social-dynamics
---

Metaphors from markets, money, trade, debt, investment, and economic systems.
```

`catalog/categories/education-and-learning.md`:
```markdown
---
slug: education-and-learning
name: "Education and Learning"
related:
  - cognitive-science
  - psychology
---

Metaphors about how people learn, teach, discover, and transmit knowledge.
```

`catalog/categories/ethics-and-morality.md`:
```markdown
---
slug: ethics-and-morality
name: "Ethics and Morality"
related:
  - philosophy
  - social-dynamics
---

Metaphors structuring moral reasoning — purity, accounting, balance,
paths, and cleanliness.
```

`catalog/categories/health-and-medicine.md`:
```markdown
---
slug: health-and-medicine
name: "Health and Medicine"
related:
  - biology-and-ecology
  - psychology
---

Metaphors from medicine, disease, healing, diagnosis, and bodily health.
```

`catalog/categories/law-and-governance.md`:
```markdown
---
slug: law-and-governance
name: "Law and Governance"
related:
  - ethics-and-morality
  - organizational-behavior
---

Metaphors from legal systems, governance, regulation, justice, and
collective decision-making.
```

`catalog/categories/mathematics-and-logic.md`:
```markdown
---
slug: mathematics-and-logic
name: "Mathematics and Logic"
related:
  - philosophy
  - computer-science
---

Metaphors from formal reasoning, proof, measurement, geometric structure,
and mathematical abstraction.
```

`catalog/categories/mythology-and-religion.md`:
```markdown
---
slug: mythology-and-religion
name: "Mythology and Religion"
related:
  - arts-and-culture
  - psychology
---

Metaphors rooted in myth, archetype, ritual, sacred narrative, and
religious cosmology.
```

`catalog/categories/physics-and-engineering.md`:
```markdown
---
slug: physics-and-engineering
name: "Physics and Engineering"
related:
  - mathematics-and-logic
  - systems-thinking
---

Metaphors from physical forces, mechanics, thermodynamics, materials,
and engineered systems.
```

**Step 2: Run validator**

```bash
uv run scripts/validate.py validate catalog/categories/
```
Expected: "All content valid."

**Step 3: Commit**

```bash
git add catalog/categories/
git commit -m "Add 9 broad disciplinary categories (Dewey-inspired expansion)"
```

**Human verification:** `ls catalog/categories/ | wc -l` shows 20. Validator passes.

---

### Task 3: Category Expansion — Backfill Existing Mappings

**Files:**
- Modify: multiple files in `catalog/mappings/`

This task adds the new categories to existing mappings that belong in them. The assignments below are based on each mapping's source/target frames and subject matter. Only add a category when the mapping clearly belongs — when in doubt, leave it out.

**Step 1: Backfill category assignments**

For each mapping listed below, add the specified category to its `categories` list in frontmatter. Preserve existing categories; append the new one.

**biology-and-ecology:**
- `survival-of-the-fittest` (already has organizational-behavior, systems-thinking)
- `creative-process-is-gardening` (already has systems-thinking, arts-and-culture)
- `ideas-are-plants` (already has cognitive-science, linguistics)
- `people-are-plants` (pending in canon — skip if not yet in catalog)

**economics-and-finance:**
- `time-is-money` (already has cognitive-science, linguistics, philosophy)
- `ideas-are-commodities` (already has cognitive-science, linguistics)
- `ideas-are-money` (already has cognitive-science, linguistics)
- `inflation-is-an-entity` (already has cognitive-science, linguistics)
- `ideas-are-resources` (already has cognitive-science, linguistics, philosophy)
- `labor-is-a-resource` (already has cognitive-science, linguistics, organizational-behavior)
- `technical-debt` (already has software-engineering)

**ethics-and-morality:**
- `good-is-up` (already has cognitive-science, linguistics, philosophy)
- `virtue-is-up` (already has cognitive-science, linguistics, philosophy)

**health-and-medicine:**
- `health-is-up` (already has cognitive-science, linguistics)
- `love-is-a-patient` (already has cognitive-science, linguistics)

**physics-and-engineering:**
- `causes-are-forces` (already has cognitive-science, linguistics, philosophy)
- `a-force-is-a-moving-object` (already has cognitive-science, linguistics)
- `psychological-forces-are-physical-forces` (already has cognitive-science, linguistics, psychology)
- `obligations-are-forces` (already has cognitive-science, linguistics, philosophy)
- `love-is-a-physical-force` (already has cognitive-science, linguistics, psychology)

**mythology-and-religion:**
- `the-trickster` (already has cognitive-science, organizational-behavior, arts-and-culture)

**Step 2: Run validator**

```bash
uv run scripts/validate.py validate
```
Expected: "All content valid." Zero warnings, zero errors.

**Step 3: Commit**

```bash
git add catalog/mappings/
git commit -m "Backfill new categories onto existing mappings"
```

**Human verification:** Spot-check 3 mapping files. Each has its new category appended. Validator passes.

---

### Task 4: Agents Identity Page

**Files:**
- Create: `site/src/pages/agents.astro`
- Modify: `site/src/pages/mappings/[slug].astro:30-39`

**Step 1: Read agent definitions for reference**

Read these files to understand each agent's role:
- `.claude/agents/prospector.md` (identity, description)
- `.claude/agents/miner.md` (identity, description)
- `.claude/agents/assayer.md` (identity, description)
- `.claude/agents/smelter.md` (identity, description)

**Step 2: Create the agents page**

Create `site/src/pages/agents.astro`:

```astro
---
import Base from "@/layouts/Base.astro";
---

<Base title="Agents" description="The AI agents that build and maintain Metaphorex">
  <article>
    <h1>Agents</h1>
    <p>
      Metaphorex is built by a team of AI agents running as
      <a href="https://github.com/anthropics/claude-code">Claude Code</a>
      plugins. Each agent has a defined role, an identity used in frontmatter
      attribution, and a source definition on GitHub. Humans direct the work
      and review every pull request.
    </p>

    <h2 id="prospector">Prospector</h2>
    <p><code>agent:metaphorex-prospector</code></p>
    <p>
      Researches new import sources — books, papers, corpora — and builds
      extraction playbooks. The Prospector surveys a source, identifies
      candidate metaphors, writes parsing scripts, and creates GitHub
      sub-issues for each candidate. High-trust role: its code contributions
      go through CODEOWNERS review.
    </p>
    <p>
      <a href="https://github.com/metaphorex/metaphorex/blob/main/.claude/agents/prospector.md">
        Source definition on GitHub</a>
    </p>

    <h2 id="miner">Miner</h2>
    <p><code>agent:metaphorex-miner</code></p>
    <p>
      Follows approved playbooks to extract mappings from sources. The Miner
      reads a playbook, generates mapping markdown files with frontmatter
      and body sections, and opens pull requests. Most entries in the catalog
      were written by the Miner.
    </p>
    <p>
      <a href="https://github.com/metaphorex/metaphorex/blob/main/.claude/agents/miner.md">
        Source definition on GitHub</a>
    </p>

    <h2 id="assayer">Assayer</h2>
    <p><code>agent:metaphorex-assayer</code></p>
    <p>
      Reviews and refines Miner output. The Assayer checks mapping quality,
      validates that "Where It Breaks" sections are substantive, and suggests
      improvements before entries are merged.
    </p>
    <p>
      <a href="https://github.com/metaphorex/metaphorex/blob/main/.claude/agents/assayer.md">
        Source definition on GitHub</a>
    </p>

    <h2 id="smelter">Smelter</h2>
    <p><code>agent:metaphorex-smelter</code></p>
    <p>
      Runs mechanical cleanup on pull requests — validates frontmatter,
      normalizes formatting, fixes structural issues. The Smelter handles
      routine quality gates so human reviewers can focus on content.
    </p>
    <p>
      <a href="https://github.com/metaphorex/metaphorex/blob/main/.claude/agents/smelter.md">
        Source definition on GitHub</a>
    </p>
  </article>
</Base>
```

**Step 3: Link agent authors from mapping pages**

In `site/src/pages/mappings/[slug].astro`, after the categories paragraph (line 45), add an author line that links `agent:*` authors to `/agents#<name>`:

```astro
<p class="muted">
  {entry.data.author.startsWith("agent:") ? (
    <>Author: <a href={`/agents#${entry.data.author.replace("agent:metaphorex-", "")}`}>{entry.data.author}</a></>
  ) : (
    <>Author: {entry.data.author}</>
  )}
</p>
```

**Step 4: Build and verify**

```bash
cd site && bun run build
```
Expected: Build succeeds.

**Step 5: Commit**

```bash
git add site/src/pages/agents.astro site/src/pages/mappings/\[slug\].astro
git commit -m "Add agents identity page and link agent authors from mappings"
```

**Human verification:** Visit `/agents/`. Four agents listed with anchor IDs. Visit any miner-authored mapping — author line links to `/agents#miner`.

---

### Task 5: Contributor Backfill Script

**Files:**
- Create: `scripts/backfill_contributors.py`

**Step 1: Write the script**

Create `scripts/backfill_contributors.py` with PEP 723 inline deps:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
"""Backfill contributors[] from GitHub activity.

For each mapping, finds:
  - The PR that introduced the file
  - Any issue linked in the PR
  - The issue filer's GitHub username
  - All PR authors who subsequently touched the file

Deduplicates against the author field and writes to contributors[].

Usage:
    uv run scripts/backfill_contributors.py             # dry run (print changes)
    uv run scripts/backfill_contributors.py --write      # write changes to files
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
MAPPINGS_DIR = ROOT / "catalog" / "mappings"


def gh(args: list[str]) -> str:
    """Run a gh CLI command and return stdout."""
    result = subprocess.run(
        ["gh"] + args,
        capture_output=True, text=True, check=True,
    )
    return result.stdout.strip()


def get_prs_for_file(filepath: str) -> list[dict]:
    """Find all merged PRs that touched a file."""
    # Use gh to search for PRs that modified this file
    output = gh([
        "pr", "list",
        "--state", "merged",
        "--search", f"'{filepath}'",
        "--json", "number,author,body",
        "--limit", "50",
    ])
    if not output:
        return []
    return json.loads(output)


def get_pr_for_commit(sha: str) -> dict | None:
    """Find the PR associated with a commit."""
    try:
        output = gh([
            "pr", "list",
            "--state", "merged",
            "--search", sha,
            "--json", "number,author,body",
            "--limit", "1",
        ])
        prs = json.loads(output) if output else []
        return prs[0] if prs else None
    except subprocess.CalledProcessError:
        return None


def get_introducing_commit(filepath: str) -> str | None:
    """Find the commit that first added a file."""
    result = subprocess.run(
        ["git", "log", "--diff-filter=A", "--format=%H", "--", filepath],
        capture_output=True, text=True, check=True,
        cwd=ROOT,
    )
    lines = result.stdout.strip().split("\n")
    return lines[-1] if lines and lines[-1] else None


def get_all_commit_authors(filepath: str) -> set[str]:
    """Get all GitHub usernames who committed changes to a file.

    Uses git log Co-Authored-By trailers and author emails.
    Returns GitHub usernames where identifiable.
    """
    result = subprocess.run(
        ["git", "log", "--format=%an%n%(trailers:key=Co-Authored-By)", "--", filepath],
        capture_output=True, text=True, check=True,
        cwd=ROOT,
    )
    # This gets commit authors but not necessarily GitHub usernames
    # For a more robust approach, we cross-reference with PR data
    return set()


def extract_issue_number(pr_body: str) -> int | None:
    """Extract linked issue number from PR body."""
    import re
    # Match patterns like "Closes #123", "Fixes #123", "Resolves #123"
    # Also match bare "#123" references
    patterns = [
        r"(?:closes|fixes|resolves)\s+#(\d+)",
        r"(?:close|fix|resolve)\s+#(\d+)",
        r"issue\s+#(\d+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, pr_body, re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None


def get_issue_author(issue_number: int) -> str | None:
    """Get the GitHub username of an issue's author."""
    try:
        output = gh([
            "issue", "view", str(issue_number),
            "--json", "author",
        ])
        data = json.loads(output)
        return data.get("author", {}).get("login")
    except subprocess.CalledProcessError:
        return None


def get_pr_authors_for_file(filepath: str) -> set[str]:
    """Get all PR authors who touched a file via git log + gh."""
    # Get all commit SHAs that touched this file
    result = subprocess.run(
        ["git", "log", "--format=%H", "--", filepath],
        capture_output=True, text=True, check=True,
        cwd=ROOT,
    )
    shas = [s for s in result.stdout.strip().split("\n") if s]

    authors = set()
    seen_prs = set()
    for sha in shas:
        pr = get_pr_for_commit(sha)
        if pr and pr["number"] not in seen_prs:
            seen_prs.add(pr["number"])
            login = pr.get("author", {}).get("login")
            if login:
                authors.add(login)
    return authors


def process_mapping(path: Path, write: bool) -> dict | None:
    """Process a single mapping file. Returns change info or None."""
    post = frontmatter.load(path)
    meta = post.metadata
    author = meta.get("author", "")
    existing = set(meta.get("contributors", []))

    filepath = f"catalog/mappings/{path.name}"
    new_contributors = set()

    # Find the introducing commit and its PR
    intro_sha = get_introducing_commit(filepath)
    if intro_sha:
        pr = get_pr_for_commit(intro_sha)
        if pr:
            # Check for linked issue
            body = pr.get("body", "") or ""
            issue_num = extract_issue_number(body)
            if issue_num:
                issue_author = get_issue_author(issue_num)
                if issue_author:
                    new_contributors.add(issue_author)

    # Find all PR authors who touched the file
    pr_authors = get_pr_authors_for_file(filepath)
    new_contributors.update(pr_authors)

    # Remove the author (don't list them as contributor too)
    # For agent authors, strip the agent: prefix for comparison
    if author.startswith("agent:"):
        # Agent authors don't have GitHub usernames to filter
        pass
    else:
        new_contributors.discard(author)

    # Remove bot accounts
    new_contributors -= {"metaphorex-miner", "metaphorex-prospector",
                         "metaphorex-assayer", "metaphorex-smelter"}

    # Merge with existing
    combined = sorted(existing | new_contributors)

    if set(combined) == existing:
        return None  # No change

    if write:
        post.metadata["contributors"] = combined
        path.write_text(frontmatter.dumps(post) + "\n")

    return {
        "file": path.name,
        "added": sorted(new_contributors - existing),
        "total": combined,
    }


def main() -> None:
    write = "--write" in sys.argv

    changes = []
    mapping_files = sorted(MAPPINGS_DIR.glob("*.md"))
    total = len(mapping_files)

    for i, path in enumerate(mapping_files, 1):
        print(f"\r[{i}/{total}] {path.name}", end="", flush=True, file=sys.stderr)
        change = process_mapping(path, write=write)
        if change:
            changes.append(change)

    print(file=sys.stderr)

    if changes:
        print(f"\n{len(changes)} mapping(s) updated:\n")
        for c in changes:
            added = ", ".join(c["added"]) if c["added"] else "(no new)"
            print(f"  {c['file']}: +{added}")
    else:
        print("\nNo changes needed.")

    if not write and changes:
        print(f"\nDry run. Use --write to apply {len(changes)} change(s).")


if __name__ == "__main__":
    main()
```

**Step 2: Test dry run**

```bash
uv run scripts/backfill_contributors.py
```
Expected: Lists mappings that would be updated, shows which contributors would be added. No files modified.

**Step 3: Run with write flag and validate**

```bash
uv run scripts/backfill_contributors.py --write
uv run scripts/validate.py validate
```
Expected: Files updated. Validator still passes.

**Step 4: Commit**

```bash
git add scripts/backfill_contributors.py
git commit -m "Add contributor backfill script (GitHub activity → frontmatter)"
```

Then commit the backfilled data separately:

```bash
git add catalog/mappings/
git commit -m "Backfill contributors from GitHub activity (issue filers, PR authors)"
```

**Human verification:** Check 3 mapping files that had nugget issues filed. The issue filer's username appears in `contributors[]`. The `author` field is not duplicated in contributors.

---

### Task 6: Graph Exploration Script

**Files:**
- Create: `scripts/graph_explore.py`

**Step 1: Write the script**

Create `scripts/graph_explore.py` with PEP 723 inline deps:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
#     "networkx>=3.2",
#     "matplotlib>=3.8",
# ]
# ///
"""Explore the Metaphorex frame-to-frame graph.

Builds a directed graph where nodes are frames and edges are mappings.
Outputs statistics and a visualization to help decide whether graph
features are worth pursuing.

Usage:
    uv run scripts/graph_explore.py                    # print stats + save PNG
    uv run scripts/graph_explore.py --output graph.svg # save as SVG
"""

from __future__ import annotations

import sys
from pathlib import Path

import frontmatter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx

ROOT = Path(__file__).resolve().parent.parent
MAPPINGS_DIR = ROOT / "catalog" / "mappings"
FRAMES_DIR = ROOT / "catalog" / "frames"


def load_graph() -> tuple[nx.DiGraph, dict[str, str]]:
    """Build directed graph from catalog. Returns (graph, frame_slug_to_name)."""
    G = nx.DiGraph()

    # Load frame names
    frame_names = {}
    for f in FRAMES_DIR.glob("*.md"):
        post = frontmatter.load(f)
        slug = post.metadata.get("slug", f.stem)
        name = post.metadata.get("name", slug)
        frame_names[slug] = name
        G.add_node(slug, name=name)

    # Add edges from mappings
    for f in MAPPINGS_DIR.glob("*.md"):
        post = frontmatter.load(f)
        meta = post.metadata
        src = meta.get("source_frame")
        tgt = meta.get("target_frame")
        if src and tgt:
            if G.has_edge(src, tgt):
                G[src][tgt]["weight"] += 1
                G[src][tgt]["mappings"].append(meta.get("slug", f.stem))
            else:
                G.add_edge(src, tgt, weight=1, mappings=[meta.get("slug", f.stem)])

    return G, frame_names


def print_stats(G: nx.DiGraph, frame_names: dict[str, str]) -> None:
    """Print graph statistics."""
    print(f"Nodes (frames): {G.number_of_nodes()}")
    print(f"Edges (unique frame pairs): {G.number_of_edges()}")
    print(f"Total mappings as edges: {sum(d['weight'] for _, _, d in G.edges(data=True))}")

    # Degree analysis (treat as undirected for connectivity)
    U = G.to_undirected()

    print(f"\n--- Components ---")
    components = list(nx.connected_components(U))
    print(f"Connected components: {len(components)}")
    sizes = sorted([len(c) for c in components], reverse=True)
    print(f"Component sizes: {sizes}")

    if len(components) == 1 or sizes[0] > 1:
        largest = max(components, key=len)
        subgraph = U.subgraph(largest)
        try:
            diameter = nx.diameter(subgraph)
            print(f"Diameter of largest component: {diameter}")
        except nx.NetworkXError:
            print("Diameter: could not compute")

    print(f"\n--- Hub Frames (top 15 by degree) ---")
    degree_sorted = sorted(U.degree(), key=lambda x: x[1], reverse=True)[:15]
    for slug, deg in degree_sorted:
        name = frame_names.get(slug, slug)
        print(f"  {name} ({slug}): {deg} connections")

    print(f"\n--- Bridges ---")
    bridges = list(nx.bridges(U))
    if bridges:
        print(f"{len(bridges)} bridge edge(s) (removing them disconnects the graph):")
        for u, v in bridges[:10]:
            print(f"  {frame_names.get(u, u)} <-> {frame_names.get(v, v)}")
    else:
        print("No bridges (graph is 2-edge-connected)")

    # Find some interesting multi-hop paths
    print(f"\n--- Multi-Hop Paths (sample) ---")
    nodes = list(largest if len(components) > 0 else G.nodes())
    if len(nodes) >= 2:
        # Find the pair with the longest shortest path
        try:
            all_pairs = dict(nx.all_pairs_shortest_path_length(subgraph))
            max_dist = 0
            max_pair = (None, None)
            for src, dists in all_pairs.items():
                for tgt, dist in dists.items():
                    if dist > max_dist:
                        max_dist = dist
                        max_pair = (src, tgt)

            if max_pair[0]:
                path = nx.shortest_path(U, max_pair[0], max_pair[1])
                path_names = [frame_names.get(n, n) for n in path]
                print(f"  Longest shortest path ({max_dist} hops):")
                print(f"    {' → '.join(path_names)}")

            # A few more interesting paths between distant domains
            interesting_pairs = [
                ("war", "love-and-relationships"),
                ("fluid-dynamics", "economics"),
                ("horticulture", "software-abstraction"),
                ("gambling", "philosophy"),
                ("medicine", "software-programs"),
            ]
            for src, tgt in interesting_pairs:
                if src in U and tgt in U and nx.has_path(U, src, tgt):
                    path = nx.shortest_path(U, src, tgt)
                    path_names = [frame_names.get(n, n) for n in path]
                    print(f"  {frame_names.get(src, src)} → {frame_names.get(tgt, tgt)} ({len(path)-1} hops):")
                    print(f"    {' → '.join(path_names)}")
        except Exception as e:
            print(f"  Path analysis failed: {e}")


def draw_graph(G: nx.DiGraph, frame_names: dict[str, str], output: str) -> None:
    """Draw the graph and save to file."""
    U = G.to_undirected()

    fig, ax = plt.subplots(1, 1, figsize=(20, 16))

    # Node sizes by degree
    degrees = dict(U.degree())
    node_sizes = [max(degrees.get(n, 1) * 120, 80) for n in U.nodes()]

    # Layout
    pos = nx.spring_layout(U, k=2.5, iterations=80, seed=42)

    # Edge widths by weight
    edge_weights = [U[u][v].get("weight", 1) * 0.5 for u, v in U.edges()]

    nx.draw_networkx_edges(U, pos, alpha=0.2, width=edge_weights, ax=ax)
    nx.draw_networkx_nodes(U, pos, node_size=node_sizes, node_color="#36c",
                           alpha=0.7, ax=ax)

    # Labels for high-degree nodes only
    labels = {n: frame_names.get(n, n) for n in U.nodes() if degrees.get(n, 0) >= 3}
    nx.draw_networkx_labels(U, pos, labels, font_size=7, font_family="sans-serif", ax=ax)

    ax.set_title(f"Metaphorex Frame Graph — {U.number_of_nodes()} frames, {U.number_of_edges()} edges",
                 fontsize=14)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"\nGraph saved to {output}")


def main() -> None:
    output = "graph.png"
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output = sys.argv[idx + 1]

    G, frame_names = load_graph()
    print_stats(G, frame_names)
    draw_graph(G, frame_names, output)


if __name__ == "__main__":
    main()
```

**Step 2: Run the script**

```bash
uv run scripts/graph_explore.py --output graph.png
```
Expected: Prints statistics (components, hubs, diameter, paths). Saves `graph.png`.

**Step 3: Review output**

Open `graph.png` and review the statistics. Key questions to answer:
- Is the graph one connected component or fragmented?
- Are there multi-hop paths longer than 3?
- Which frames are the biggest hubs?
- Are there surprising connections between distant domains?

**Step 4: Commit the script (not the output)**

```bash
git add scripts/graph_explore.py
git commit -m "Add graph exploration script (frame-to-frame network analysis)"
```

Add `graph.png` to `.gitignore` if not already ignored:
```bash
echo "graph.png" >> .gitignore
git add .gitignore
git commit -m "Ignore graph exploration output files"
```

**Human verification:** Run the script. Look at the PNG. Read the stats. Decide if graph features are worth pursuing.

---

### Task 7: Final Validation and Site Build

**Step 1: Run full validator**

```bash
uv run scripts/validate.py validate
```
Expected: "All content valid." Zero warnings, zero errors.

**Step 2: Build the site**

```bash
cd site && bun run build
```
Expected: Build succeeds. No errors.

**Step 3: Verify new pages exist**

```bash
ls site/dist/colophon/index.html site/dist/agents/index.html
```
Expected: Both files exist.

**Human verification:** Run `cd site && bun run dev`, visit all new pages, click through links. Nav has 5 items. Colophon links work. Agent links from mappings work. New categories appear on the categories index.
