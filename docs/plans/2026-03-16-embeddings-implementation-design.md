# Embeddings implementation design

## Context

This is the implementation plan for the embeddings and vector search layer
described in `2026-03-15-embeddings-guidance.md`. That doc covers the *what*
and *why*; this doc covers the *how* and *in what order*.

Key decisions made during brainstorming:

- **Language:** TypeScript + Bun (not Python). Aligns with the Astro site,
  the future MCP server, and eventual client-side web search.
- **Embedding model:** OpenAI `text-embedding-3-small` (1536 dims, $0.02/MTok).
  Swappable later — full re-embed costs pennies at our scale.
- **Vector store:** SQLite + `sqlite-vec` extension. Generated artifact,
  gitignored, rebuilt on demand.
- **Build strategy:** SQLite-first with fake vectors, then swap in real
  embeddings once the pipeline is proven.

---

## Step 0 — Project scaffolding

**Goal:** Bun project at repo root with dependencies, macOS workaround documented.

**Files:**

```
package.json          # new — Bun project with deps
scripts/lib/          # new — shared TS modules
.gitignore            # edit — add embeddings.db, node_modules
```

**Dependencies:**

```json
{
  "dependencies": {
    "gray-matter": "^4.0.3",
    "sqlite-vec": "^0.1.6"
  },
  "devDependencies": {
    "@types/bun": "latest"
  }
}
```

**macOS workaround:** Apple's system SQLite disables `loadExtension()`.
Before creating any `Database` instance:

```typescript
import { Database } from "bun:sqlite";
Database.setCustomSQLite("/opt/homebrew/opt/sqlite/lib/libsqlite3.dylib");
```

This is a one-liner at the top of the db module. On Linux it's unnecessary
but harmless. If the path doesn't exist, Bun segfaults (not a clean error) —
so we should detect the platform and warn.

**Done when:** `bun install` succeeds and a trivial script can open a
`:memory:` SQLite database with sqlite-vec loaded.

---

## Step 1 — Catalog parser

**Goal:** Read all catalog markdown files, extract structured data with
per-proposition granularity.

**File:** `scripts/lib/catalog.ts`

**What it does:**

1. Glob `catalog/mappings/*.md`
2. Parse each file with `gray-matter` (YAML frontmatter + markdown body)
3. Split body into sections by `## Heading`
4. Extract bullet points from Transfers, Limits, Expressions as string arrays
5. Return typed array of `CatalogEntry` objects

**Types:**

```typescript
interface CatalogEntry {
  slug: string;
  name: string;
  kind: "metaphor" | "pattern" | "archetype" | "paradigm" | "mental-model";
  sourceFrame?: string;
  appliesTo?: string[];
  categories: string[];
  grounding: "proven" | "established" | "folk" | "contested";
  transfers: string[];   // individual propositions
  limits: string[];      // individual propositions
  expressions: string[]; // individual phrases
}
```

**Proposition extraction:** Each `- ` bullet under `## Transfers`, `## Limits`,
or `## Expressions` becomes one string. Multi-line bullets (continuation lines)
are joined. Bold lead-ins (e.g., `**Accumulation.**`) are preserved — they're
part of the proposition's meaning.

**Done when:** `bun run scripts/lib/catalog.ts` prints entry count and a
sample entry with its propositions. Validate against `validate.py`'s count
(445 mappings).

---

## Step 2 — SQLite database (no vectors)

**Goal:** Relational database with all text units, queryable with plain SQL.

**File:** `scripts/lib/db.ts`

**Schema:**

```sql
CREATE TABLE meta (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

CREATE TABLE embedding_records (
  id TEXT PRIMARY KEY,          -- "pipeline::transfer::2"
  slug TEXT NOT NULL,
  kind TEXT NOT NULL,
  section TEXT NOT NULL,        -- title | transfer | limit | expression
  text TEXT NOT NULL,
  model TEXT,                   -- NULL until real embeddings
  model_version TEXT,
  created_at TEXT NOT NULL
);

CREATE INDEX idx_records_slug ON embedding_records(slug);
CREATE INDEX idx_records_section ON embedding_records(section);
```

**ID format:** `{slug}::{section}::{index}` — e.g., `pipeline::transfer::2`.
Title always index 0. Propositions numbered by their order in the markdown.

**Loader script:** `scripts/build-db.ts`

1. Opens (or creates) `catalog/embeddings.db`
2. Creates tables if not present
3. Reads catalog via `scripts/lib/catalog.ts`
4. Inserts all text units into `embedding_records`
5. Reports: total records, breakdown by section type

**No `summary` section yet.** Summaries require an LLM call. We skip them
until Step 4 (or later — they're the lowest-priority embedding type).

**Done when:** `bun run scripts/build-db.ts` creates `embeddings.db` and you
can query it:

```bash
sqlite3 catalog/embeddings.db "SELECT section, COUNT(*) FROM embedding_records GROUP BY section"
```

---

## Step 3 — sqlite-vec with random vectors

**Goal:** Prove the vector plumbing works end-to-end with fake data.

**Changes:**

1. Add `embeddings` virtual table to `db.ts`:

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS embeddings USING vec0(
  id TEXT PRIMARY KEY,
  embedding FLOAT[1536]
);
```

2. In `build-db.ts`, after inserting text records, generate a random
   `Float32Array(1536)` for each record and insert into `embeddings`.

3. Write `scripts/search.ts`:
   - Takes a query string (ignored for now — just generates a random vector)
   - Runs nearest-neighbor search against `embeddings`
   - Joins back to `embedding_records` to get slug, section, text
   - Deduplicates by slug (keeps best match per mapping)
   - Prints results with scores

**Done when:** `bun run scripts/search.ts "anything"` returns 10 random-but-valid
results with slugs, matched text, and distances. Results are garbage (random
vectors), but the pipeline is proven.

---

## Step 4 — Real embeddings

**Goal:** Replace random vectors with OpenAI embeddings. First time the
results mean something.

**Changes to `build-db.ts`:**

1. Add `embedText()` function calling OpenAI's embeddings API via the
   `openai` npm package
2. Batch texts in groups of 100 (API limit is higher, but 100 keeps
   progress output useful)
3. Store model identifier in `meta` table
4. Add model-mismatch guard: if `meta.embedding_model` differs from the
   script's configured model, refuse to run (user must delete DB and rebuild)
5. Add `--force` flag to re-embed everything, `--slug X` to embed one entry

**New dependency:** `openai` npm package.

**Environment:** Requires `OPENAI_API_KEY` env var. Script exits with a
clear message if missing.

**Cost estimate:** 445 mappings × ~15 units × ~50 tokens avg = ~330K tokens.
At $0.02/MTok = **less than $0.01** for the full catalog.

**Changes to `search.ts`:**

1. Embed the query string using the same model
2. Use the real query vector for nearest-neighbor search
3. Results should now be semantically meaningful

**Done when:** `bun run scripts/search.ts "items pile up until a processor
becomes available"` returns queue, buffer, pipeline (or similar structural
matches) in the top results.

---

## Step 5 — CLI search

**Goal:** Usable search interface with filtering options.

**File:** `scripts/search.ts` (enhanced)

**Usage:**

```
bun run scripts/search.ts <query>
bun run scripts/search.ts --section transfer <query>
bun run scripts/search.ts --section limit <query>
bun run scripts/search.ts --kind metaphor <query>
bun run scripts/search.ts --json <query>
```

**Output format (default):**

```
queue       [transfer] "accumulates items until a processor claims them"  0.94
buffer      [transfer] "absorbs bursts to smooth downstream flow"         0.88
pipeline    [transfer] "throughput bounded by slowest stage"              0.71
```

**Output format (--json):**

```json
[
  {
    "slug": "queue",
    "kind": "pattern",
    "section": "transfer",
    "matchedText": "accumulates items until a processor claims them",
    "score": 0.94
  }
]
```

**Done when:** Search works with all filter combinations and both output
formats. Manual testing with 5–10 known queries confirms results are
structurally reasonable.

---

## What's NOT in this plan

These are future work, not blocked by this implementation:

- **`mx` CLI wrapper** — a proper CLI with subcommands (`mx search`,
  `mx get`, `mx frames`, `mx cluster`). Build after the search layer proves
  out.
- **MCP server** — wraps the search layer for agent use. Phase 4 of the
  guidance doc.
- **Summary embeddings** — requires an LLM call per entry to generate a
  1–2 sentence synthesis. Add when the basic pipeline is working.
- **CI integration** — rebuild `embeddings.db` on merge to main. Add once
  the scripts are stable.
- **Validator migration to TypeScript** — the existing Python validator
  stays as-is for now.

---

## File inventory

New files this plan creates:

```
package.json                  # Step 0
scripts/lib/catalog.ts        # Step 1
scripts/lib/db.ts             # Step 2
scripts/build-db.ts           # Step 2 (enhanced in 3, 4)
scripts/search.ts             # Step 3 (enhanced in 4, 5)
```

Modified files:

```
.gitignore                    # Step 0 — add embeddings.db, node_modules
```

Generated artifacts (gitignored):

```
catalog/embeddings.db         # Generated by build-db.ts
node_modules/                 # Bun dependencies
bun.lock                      # Bun lockfile (commit this)
```
