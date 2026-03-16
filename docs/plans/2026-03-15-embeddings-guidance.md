# Embeddings & vector search for Metaphorex
## Design document for Claude Code implementation

---

## Context and goal

Metaphorex is a catalog of load-bearing metaphors, patterns, archetypes, paradigms, and mental models. Each entry has structured fields including `transfers` (what relational structure carries over from the source domain) and `limits` (where the structure breaks).

The goal of the embedding layer is to make the catalog queryable by **structural similarity** rather than topic or keyword. A query like "items pile up until a worker becomes available" should return `queue`, `buffer`, and `pipeline` — not because those words appear in the query, but because the relational structure matches.

This is the foundation for a CLI tool and eventually an MCP server that an LLM agent can call to identify active metaphors in its reasoning, retrieve full mappings, and surface failure conditions before they cause problems.

---

## Why structural similarity requires per-proposition embeddings

The naive approach — embed each mapping as a single document — fails for metaphor work. PIPELINE and RIVER cluster together on topic. PIPELINE should cluster with ASSEMBLY LINE and DIGESTIVE SYSTEM, because they share the proposition "[source] blockage at any stage propagates upstream."

The fix: embed each `transfers` and `limits` proposition individually. A nearest-neighbor search on propositions finds the specific structural match, not the topically nearest entry. This also means search results tell you *which proposition matched* — which is more useful to an agent than knowing only which mapping matched.

---

## What gets embedded

Every embeddable unit gets its own record. For a mapping with 6 transfers, 3 limits, 4 expressions, and a title:

| section | text embedded | count |
|---------|--------------|-------|
| `title` | The mapping title, e.g. "Pipeline" | 1 |
| `transfer` | Each proposition from the `transfers` list | 6 |
| `limit` | Each proposition from the `limits` list | 3 |
| `expression` | Each phrase from the `expressions` list | 4 |
| `summary` | A generated 1–2 sentence synthesis of what the mapping is and does | 1 |

That example mapping produces 15 embedding records. The catalog at 400+ mappings with average ~10 propositions each is roughly 4,000–6,000 records. At 1536 dimensions (float32), that's ~35MB — trivially small for SQLite.

**Note:** `expressions` embeddings serve a different function from proposition embeddings. They catch cases where a metaphor is already active in someone's language before they've named it — e.g., "we need to pay down our tech debt" activates TECHNICAL DEBT before the agent has thought to look it up.

---

## Embedding record schema

```typescript
interface EmbeddingRecord {
  id: string;           // "{slug}::{section}::{index}" e.g. "pipeline::transfer::2"
  slug: string;         // mapping slug, joins to catalog
  kind: string;         // mapping kind: metaphor | pattern | archetype | paradigm | mental-model
  section: "title" | "transfer" | "limit" | "expression" | "summary";
  text: string;         // the exact sentence being embedded
  embedding: Float32Array; // stored as blob in sqlite-vec
  model: string;        // embedding model identifier
  model_version: string;
  created_at: string;   // ISO timestamp
}
```

The `meta` table tracks which model was used for the current index. Changing models requires a full re-embed — partial migrations produce silent wrong results and must be prevented.

```sql
CREATE TABLE meta (
  key TEXT PRIMARY KEY,
  value TEXT
);
-- e.g. INSERT INTO meta VALUES ('embedding_model', 'text-embedding-3-small');
--      INSERT INTO meta VALUES ('embedding_dimensions', '1536');
--      INSERT INTO meta VALUES ('catalog_version', '2026.03.13');
```

---

## Database setup: sqlite-vec

Use the `sqlite-vec` extension (by Alex Garcia). Pure C, no external dependencies, ships as a compiled binary per platform bundled in the npm package.

```typescript
// scripts/db.ts
import { Database } from "bun:sqlite";
import * as sqliteVec from "sqlite-vec";

export function openEmbeddingDb(path: string): Database {
  const db = new Database(path);
  sqliteVec.load(db);

  db.run(`
    CREATE TABLE IF NOT EXISTS meta (
      key TEXT PRIMARY KEY,
      value TEXT NOT NULL
    )
  `);

  db.run(`
    CREATE TABLE IF NOT EXISTS embedding_records (
      id TEXT PRIMARY KEY,
      slug TEXT NOT NULL,
      kind TEXT NOT NULL,
      section TEXT NOT NULL,
      text TEXT NOT NULL,
      model TEXT NOT NULL,
      model_version TEXT NOT NULL,
      created_at TEXT NOT NULL
    )
  `);

  db.run(`
    CREATE VIRTUAL TABLE IF NOT EXISTS embeddings USING vec0(
      id TEXT PRIMARY KEY,
      embedding FLOAT[1536]
    )
  `);

  db.run(`
    CREATE INDEX IF NOT EXISTS idx_records_slug ON embedding_records(slug)
  `);

  return db;
}
```

---

## Embedding generation script

```typescript
// scripts/embed.ts
// Usage: bun run scripts/embed.ts [--force] [--slug pipeline]

import { Database } from "bun:sqlite";
import { openEmbeddingDb } from "./db";
import { readCatalog } from "./catalog";   // reads markdown + frontmatter
import { generateSummary } from "./summarize"; // small Opus call per entry

const MODEL = "text-embedding-3-small";
const DIMENSIONS = 1536;
const DB_PATH = "catalog/embeddings.db";
const BATCH_SIZE = 100;

async function embedText(texts: string[]): Promise<number[][]> {
  const response = await fetch("https://api.openai.com/v1/embeddings", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.OPENAI_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ model: MODEL, input: texts }),
  });
  const data = await response.json();
  return data.data.map((d: any) => d.embedding);
}

async function main() {
  const db = openEmbeddingDb(DB_PATH);

  // Guard against model mismatch
  const storedModel = db.query("SELECT value FROM meta WHERE key = 'embedding_model'").get() as any;
  if (storedModel && storedModel.value !== MODEL) {
    console.error(`Model mismatch: index built with ${storedModel.value}, script uses ${MODEL}`);
    console.error("Delete embeddings.db and re-run to rebuild from scratch.");
    process.exit(1);
  }

  db.run("INSERT OR IGNORE INTO meta VALUES ('embedding_model', ?)", [MODEL]);
  db.run("INSERT OR IGNORE INTO meta VALUES ('embedding_dimensions', ?)", [String(DIMENSIONS)]);

  const catalog = await readCatalog();
  const forceSlug = process.argv.includes("--slug")
    ? process.argv[process.argv.indexOf("--slug") + 1]
    : null;
  const force = process.argv.includes("--force");

  // Collect all units to embed
  const units: Array<{ id: string; slug: string; kind: string; section: string; text: string }> = [];

  for (const entry of catalog) {
    if (forceSlug && entry.slug !== forceSlug) continue;

    const makeId = (section: string, index: number) =>
      `${entry.slug}::${section}::${index}`;

    // Skip if already embedded and not forcing
    if (!force) {
      const existing = db.query(
        "SELECT id FROM embedding_records WHERE slug = ?", [entry.slug]
      ).all();
      if (existing.length > 0) continue;
    }

    // Title
    units.push({ id: makeId("title", 0), slug: entry.slug, kind: entry.kind, section: "title", text: entry.title });

    // Transfers
    for (const [i, t] of entry.transfers.entries())
      units.push({ id: makeId("transfer", i), slug: entry.slug, kind: entry.kind, section: "transfer", text: t });

    // Limits
    for (const [i, l] of entry.limits.entries())
      units.push({ id: makeId("limit", i), slug: entry.slug, kind: entry.kind, section: "limit", text: l });

    // Expressions
    for (const [i, e] of entry.expressions.entries())
      units.push({ id: makeId("expression", i), slug: entry.slug, kind: entry.kind, section: "expression", text: e });

    // Summary (generated if not cached)
    const summary = await generateSummary(entry);
    units.push({ id: makeId("summary", 0), slug: entry.slug, kind: entry.kind, section: "summary", text: summary });
  }

  console.log(`Embedding ${units.length} units...`);

  // Batch embed
  for (let i = 0; i < units.length; i += BATCH_SIZE) {
    const batch = units.slice(i, i + BATCH_SIZE);
    const texts = batch.map(u => u.text);
    const vectors = await embedText(texts);

    const insertRecord = db.prepare(`
      INSERT OR REPLACE INTO embedding_records
        (id, slug, kind, section, text, model, model_version, created_at)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    `);
    const insertVec = db.prepare(`
      INSERT OR REPLACE INTO embeddings (id, embedding) VALUES (?, ?)
    `);

    db.transaction(() => {
      for (const [j, unit] of batch.entries()) {
        insertRecord.run(unit.id, unit.slug, unit.kind, unit.section, unit.text,
          MODEL, "1", new Date().toISOString());
        insertVec.run(unit.id, new Float32Array(vectors[j]));
      }
    })();

    console.log(`  ${Math.min(i + BATCH_SIZE, units.length)} / ${units.length}`);
  }

  console.log("Done.");
}

main();
```

---

## Search implementation

```typescript
// scripts/search.ts

import { openEmbeddingDb } from "./db";

export interface SearchResult {
  slug: string;
  kind: string;
  matchedText: string;    // the specific proposition that matched
  section: string;        // which section it came from
  score: number;          // cosine similarity (0–1, higher = more similar)
}

export async function search(
  query: string,
  opts: {
    k?: number;
    sections?: Array<"transfer" | "limit" | "expression" | "title" | "summary">;
    kinds?: string[];
  } = {}
): Promise<SearchResult[]> {
  const db = openEmbeddingDb("catalog/embeddings.db");
  const { k = 10, sections, kinds } = opts;

  // Embed the query
  const queryVec = await embedText([query]).then(r => new Float32Array(r[0]));

  // Build filter conditions
  const conditions: string[] = [];
  if (sections?.length) {
    conditions.push(`r.section IN (${sections.map(() => "?").join(",")})`);
  }
  if (kinds?.length) {
    conditions.push(`r.kind IN (${kinds.map(() => "?").join(",")})`);
  }

  const whereClause = conditions.length
    ? `AND ${conditions.join(" AND ")}`
    : "";

  const filterParams = [
    ...(sections ?? []),
    ...(kinds ?? []),
  ];

  // sqlite-vec nearest neighbor query joined back to records
  const results = db.query(`
    SELECT
      r.slug,
      r.kind,
      r.text AS matched_text,
      r.section,
      e.distance
    FROM embeddings e
    JOIN embedding_records r ON r.id = e.id
    WHERE e.embedding MATCH ?
      AND k = ?
      ${whereClause}
    ORDER BY e.distance
  `, [queryVec, k * 3, ...filterParams]).all() as any[]; // over-fetch, then filter

  // Convert distance to similarity score, filter, dedupe by slug keeping best match
  const bySlug = new Map<string, SearchResult>();
  for (const row of results) {
    const score = 1 - row.distance; // L2 distance → approximate similarity
    if (!bySlug.has(row.slug) || bySlug.get(row.slug)!.score < score) {
      bySlug.set(row.slug, {
        slug: row.slug,
        kind: row.kind,
        matchedText: row.matched_text,
        section: row.section,
        score,
      });
    }
  }

  return [...bySlug.values()]
    .sort((a, b) => b.score - a.score)
    .slice(0, k);
}
```

---

## CLI interface

```
mx search <query>
  Search by natural language — finds nearest structural propositions

mx search "items pile up until a processor becomes available"
→ queue       [transfer] "[source] accumulates items until a processor claims them"  0.94
→ buffer      [transfer] "[source] absorbs bursts to smooth downstream flow"          0.88
→ pipeline    [transfer] "[source] throughput bounded by slowest stage"               0.71

mx search --section transfer "something breaks upstream when this fails"
  Search only transfer propositions — finds structural matches

mx search --section limit "fails when the boundaries between stages are unclear"
  Search only limit propositions — finds failure condition matches

mx search --kind paradigm "prefer doing less until you know more"
  Filter by entry kind

mx get <slug>
  Return full entry: frontmatter + all sections.
  Always includes grounding value so callers know the epistemic standing.

mx frames <text>
  Identify which metaphorical frames are active in a block of text.
  Embeds the input, searches expressions + titles, returns top matches.

mx match --transfer "[source] blockage propagates upstream"
  Exact structural proposition search — finds all entries where this holds

mx cluster <slug> [<slug>...]
  Given a set of slugs (e.g. from multiple mx frames calls on a system),
  analyze whether the active frames are coherent or contradictory.
  Returns: dominant frame, outlier frames, known incompatible pairs.
```

---

## MCP server tool signatures

These are the four tool primitives the MCP server exposes to an LLM agent. Each maps to a search operation against the embedding DB.

```typescript
// Tool 1: identify which frames are active in language
identify_frames({
  text: string,      // the agent's reasoning, code comment, doc excerpt, etc.
  k?: number,        // default 5
}): Array<{
  slug: string,
  kind: string,
  score: number,
  grounding: string,                // proven | established | folk | contested
  matched_expression: string,       // the specific expression that fired
}>

// Tool 2: get a full mapping with all sections
get_mapping({
  slug: string,
}): {
  title: string,
  kind: string,             // metaphor | pattern | archetype | paradigm | mental-model
  source_frame?: string,
  applies_to?: string[],    // absent for mental-model and universal entries
  transfers: string[],
  limits: string[],
  expressions: string[],
  grounding: string,        // proven | established | folk | contested
  related: string[],
}

// Tool 3: find entries by structural property
match_structure({
  proposition: string,     // "[source] blockage propagates upstream"
  valence: "transfer" | "limit" | "either",
  k?: number,
}): Array<{
  slug: string,
  kind: string,
  matched_text: string,
  score: number,
}>

// Tool 4: name something using a frame's vocabulary
name_from_frame({
  slug: string,            // the active frame
  role: string,            // "the thing that detects anomalies"
  behavior: string,        // "pattern-matches against known bad states, escalates unknowns"
}): Array<{
  name: string,
  implied_by: string,      // which transfer proposition suggests this name
  connotations: string[],  // what the name implies beyond the role
}>
```

---

## Embedding model choice

**Recommended: `text-embedding-3-small` (OpenAI)**

- 1536 dimensions, excellent quality for semantic + structural similarity
- Cost: ~$0.02 per 1M tokens; the full catalog re-embed costs cents
- Available via any OpenAI-compatible endpoint (LiteLLM, local proxies)

**Alternative: `nomic-embed-text` (local via Ollama)**

- Use if offline capability is required or cost is a constraint
- Quality is good but slightly lower on structural reasoning tasks
- Requires Ollama running locally; CLI needs a config flag to switch

**Critical: store model identifier in DB `meta` table.** Changing models requires a full re-embed. Mixed-model indexes produce silently wrong nearest-neighbor results. The embed script must detect and reject model mismatches (see implementation above).

---

## Build artifact strategy

The embedding DB is a generated artifact, not source-controlled content.

```
catalog/
  mappings/          # source of truth — markdown + YAML
  embeddings.db      # generated — gitignored

scripts/
  embed.ts           # generates embeddings.db from catalog
  search.ts          # query interface used by CLI and MCP server
```

`embeddings.db` is rebuilt:
- On first run of the CLI (if absent)
- On `mx reindex` (explicit rebuild)
- In CI after any merge to main that touches `catalog/mappings/`

The nightly deploy to GitHub Pages already rebuilds the site — add `bun run scripts/embed.ts` to that workflow so the shipped CLI always has a current index.

---

## Phased implementation order

**Phase 1 — Data layer (do first, blocks everything)**
- `scripts/db.ts`: sqlite-vec setup, table creation, meta table
- `scripts/embed.ts`: read catalog, generate + store embeddings
- Validate on 20 entries before running full catalog

**Phase 2 — Search layer**
- `scripts/search.ts`: nearest-neighbor query with section + kind filters
- Dedupe by slug, return matched text + score
- Test: known structural queries should return expected slugs in top 3

**Phase 3 — CLI**
- `mx search`, `mx get`, `mx frames`, `mx match`, `mx cluster`
- `mx reindex` for explicit rebuild
- Structured output option (`--json`) for piping to other tools

**Phase 4 — MCP server**
- Wrap the four tool primitives in an MCP-compliant server
- Validate tool schemas match the signatures above
- Document which embedding model the caller must use for `nearest_frames` if passing pre-computed vectors

---

## Notes for the implementation session

**Don't embed propositions as a concatenated blob.** Each proposition is a separate record. The granularity is the entire point — a query matches a *specific* structural fact, not a vague average of the whole entry.

**The `expressions` section serves a distinct function.** Proposition embeddings find structural matches. Expression embeddings catch implicit/dead metaphors already active in someone's language. Both are needed. Keep them in separate records so they can be searched independently.

**`mx cluster` is the highest-value tool for system analysis.** When an agent calls `identify_frames` multiple times across a codebase or design doc, the accumulated frame set can be analyzed for coherence. Contradictory metaphor clusters (ORGANISM vs. MACHINE for the same system) are where design confusion lives. This tool is additive — implement it after the basic search layer works.

**The MCP `identify_frames` tool is the entry point for agent use.** An agent that calls this on its own reasoning at key decision points will surface implicit metaphors before they mislead. The others are follow-up tools. Design the agent prompt to call `identify_frames` first, then `get_mapping` on the top hits to check `limits` before proceeding.
