# Embeddings Pipeline Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a SQLite-backed vector search pipeline over the Metaphorex catalog, starting with plain text records and graduating to real OpenAI embeddings.

**Architecture:** TypeScript + Bun scripts read catalog markdown, extract per-proposition text units, store them in SQLite with sqlite-vec for nearest-neighbor search. The database is a generated artifact (gitignored), rebuilt from the catalog on demand.

**Tech Stack:** Bun 1.3+, bun:sqlite, sqlite-vec extension, gray-matter (YAML+markdown parsing), OpenAI text-embedding-3-small (Step 4+)

**Design doc:** `docs/plans/2026-03-16-embeddings-implementation-design.md`

---

### Task 1: Bun project scaffolding

**Files:**
- Create: `package.json`
- Create: `tsconfig.json`
- Modify: `.gitignore`

**Step 1: Create package.json**

```json
{
  "name": "metaphorex-scripts",
  "private": true,
  "type": "module",
  "scripts": {
    "build-db": "bun run scripts/build-db.ts",
    "search": "bun run scripts/search.ts"
  },
  "dependencies": {
    "gray-matter": "^4.0.3",
    "sqlite-vec": "^0.1.6"
  },
  "devDependencies": {
    "@types/bun": "latest"
  }
}
```

**Step 2: Create tsconfig.json**

```json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "types": ["bun-types"],
    "strict": true,
    "noEmit": true,
    "skipLibCheck": true
  },
  "include": ["scripts/**/*.ts"]
}
```

**Step 3: Add gitignore entries**

Add to `.gitignore`:

```
node_modules/
catalog/embeddings.db
```

**Step 4: Install dependencies**

Run: `bun install`
Expected: `bun.lock` created, `node_modules/` populated, no errors.

**Step 5: Verify sqlite-vec loads on macOS**

Create a throwaway test: `scripts/test-sqlite.ts`

```typescript
import { Database } from "bun:sqlite";
import * as sqliteVec from "sqlite-vec";

// macOS: Apple's system SQLite disables loadExtension().
// Point Bun at Homebrew's SQLite instead.
if (process.platform === "darwin") {
  const brewSqlite = "/opt/homebrew/opt/sqlite/lib/libsqlite3.dylib";
  const { existsSync } = await import("node:fs");
  if (!existsSync(brewSqlite)) {
    console.error(`Homebrew SQLite not found at ${brewSqlite}`);
    console.error("Install it: brew install sqlite");
    process.exit(1);
  }
  Database.setCustomSQLite(brewSqlite);
}

const db = new Database(":memory:");
sqliteVec.load(db);

const version = db.query("SELECT vec_version()").get() as any;
console.log("sqlite-vec loaded successfully, version:", Object.values(version)[0]);
db.close();
```

Run: `bun run scripts/test-sqlite.ts`
Expected: `sqlite-vec loaded successfully, version: v0.1.6` (or similar)

**Step 6: Commit**

```bash
git add package.json tsconfig.json bun.lock .gitignore scripts/test-sqlite.ts
git commit -m "feat: Bun project scaffolding with sqlite-vec"
```

**Verify:** `bun run scripts/test-sqlite.ts` prints the sqlite-vec version without errors or crashes.

---

### Task 2: Catalog parser

**Files:**
- Create: `scripts/lib/catalog.ts`

**Step 1: Write catalog parser**

```typescript
// scripts/lib/catalog.ts
import matter from "gray-matter";
import { readFileSync, readdirSync } from "node:fs";
import { join, resolve } from "node:path";

const ROOT = resolve(import.meta.dirname, "../..");
const MAPPINGS_DIR = join(ROOT, "catalog/mappings");

export interface CatalogEntry {
  slug: string;
  name: string;
  kind: "metaphor" | "pattern" | "archetype" | "paradigm" | "mental-model";
  sourceFrame?: string;
  appliesTo?: string[];
  categories: string[];
  grounding: "proven" | "established" | "folk" | "contested";
  transfers: string[];
  limits: string[];
  expressions: string[];
}

/**
 * Parse markdown body into { heading: content } sections.
 * Mirrors validate.py's parse_sections().
 */
function parseSections(content: string): Record<string, string> {
  const sections: Record<string, string> = {};
  let currentHeading: string | null = null;
  let currentLines: string[] = [];

  for (const line of content.split("\n")) {
    const match = line.match(/^## (.+)$/);
    if (match) {
      if (currentHeading) {
        sections[currentHeading] = currentLines.join("\n").trim();
      }
      currentHeading = match[1].trim();
      currentLines = [];
    } else if (currentHeading !== null) {
      currentLines.push(line);
    }
  }
  if (currentHeading) {
    sections[currentHeading] = currentLines.join("\n").trim();
  }
  return sections;
}

/**
 * Extract bullet items from a markdown section.
 * Handles multi-line bullets (continuation lines indented with 2+ spaces).
 * Returns each bullet as a single joined string with whitespace normalized.
 */
function extractBullets(sectionContent: string): string[] {
  const bullets: string[] = [];
  let current: string | null = null;

  for (const line of sectionContent.split("\n")) {
    if (line.startsWith("- ")) {
      if (current !== null) bullets.push(current.trim());
      current = line.slice(2);
    } else if (current !== null && /^\s{2,}/.test(line)) {
      // Continuation line — append with a space
      current += " " + line.trim();
    } else if (current !== null && line.trim() === "") {
      // Blank line between bullets — keep accumulating
    } else if (current !== null) {
      // Non-continuation non-blank line — close current bullet
      bullets.push(current.trim());
      current = null;
    }
  }
  if (current !== null) bullets.push(current.trim());
  return bullets;
}

/**
 * Read all mappings from the catalog directory.
 * Returns structured entries with per-proposition arrays.
 */
export function readCatalog(): CatalogEntry[] {
  const files = readdirSync(MAPPINGS_DIR)
    .filter((f) => f.endsWith(".md"))
    .sort();

  return files.map((filename) => {
    const filepath = join(MAPPINGS_DIR, filename);
    const raw = readFileSync(filepath, "utf-8");
    const { data, content } = matter(raw);
    const sections = parseSections(content);

    return {
      slug: data.slug,
      name: data.name,
      kind: data.kind,
      sourceFrame: data.source_frame,
      appliesTo: data.applies_to,
      categories: data.categories ?? [],
      grounding: data.grounding ?? "folk",
      transfers: extractBullets(sections["Transfers"] ?? ""),
      limits: extractBullets(sections["Limits"] ?? ""),
      expressions: extractBullets(sections["Expressions"] ?? ""),
    };
  });
}

// Self-test when run directly
if (import.meta.main) {
  const catalog = readCatalog();
  console.log(`Loaded ${catalog.length} mappings\n`);

  // Show section counts
  let totalTransfers = 0, totalLimits = 0, totalExpressions = 0;
  for (const entry of catalog) {
    totalTransfers += entry.transfers.length;
    totalLimits += entry.limits.length;
    totalExpressions += entry.expressions.length;
  }
  console.log(`Total transfers:   ${totalTransfers}`);
  console.log(`Total limits:      ${totalLimits}`);
  console.log(`Total expressions: ${totalExpressions}`);
  console.log(`Total units:       ${catalog.length + totalTransfers + totalLimits + totalExpressions} (incl. titles)\n`);

  // Show a sample entry
  const sample = catalog.find((e) => e.slug === "argument-is-war") ?? catalog[0];
  console.log(`Sample: ${sample.slug}`);
  console.log(`  kind: ${sample.kind}`);
  console.log(`  transfers (${sample.transfers.length}):`);
  for (const t of sample.transfers.slice(0, 2))
    console.log(`    - ${t.slice(0, 80)}...`);
  console.log(`  limits (${sample.limits.length}):`);
  for (const l of sample.limits.slice(0, 2))
    console.log(`    - ${l.slice(0, 80)}...`);
  console.log(`  expressions (${sample.expressions.length}):`);
  for (const e of sample.expressions.slice(0, 2))
    console.log(`    - ${e.slice(0, 80)}...`);
}
```

**Step 2: Run the parser**

Run: `bun run scripts/lib/catalog.ts`
Expected: `Loaded 445 mappings`, followed by section counts and a sample entry with bullet text.

**Step 3: Verify bullet parsing against a known entry**

Check that `argument-is-war` produces:
- 4 transfers (Opponents, Territory, Weapons, Victory and defeat)
- 4 limits
- 8 expressions

If counts are off, the multi-line bullet parsing needs adjustment. Debug by
inspecting the raw section content vs. extracted bullets.

**Step 4: Commit**

```bash
git add scripts/lib/catalog.ts
git commit -m "feat: catalog parser with per-proposition extraction"
```

**Verify:** Run `bun run scripts/lib/catalog.ts`, confirm 445 mappings loaded and sample bullets look correct.

---

### Task 3: SQLite database module

**Files:**
- Create: `scripts/lib/db.ts`

**Step 1: Write the database module**

```typescript
// scripts/lib/db.ts
import { Database } from "bun:sqlite";
import * as sqliteVec from "sqlite-vec";
import { existsSync } from "node:fs";

// macOS: Apple's system SQLite disables loadExtension().
if (process.platform === "darwin") {
  const brewSqlite = "/opt/homebrew/opt/sqlite/lib/libsqlite3.dylib";
  if (!existsSync(brewSqlite)) {
    console.error(`Homebrew SQLite not found at ${brewSqlite}`);
    console.error("Install it: brew install sqlite");
    process.exit(1);
  }
  Database.setCustomSQLite(brewSqlite);
}

export function openDb(path: string): Database {
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
      model TEXT,
      model_version TEXT,
      created_at TEXT NOT NULL
    )
  `);

  db.run(`CREATE INDEX IF NOT EXISTS idx_records_slug ON embedding_records(slug)`);
  db.run(`CREATE INDEX IF NOT EXISTS idx_records_section ON embedding_records(section)`);

  return db;
}
```

**Step 2: Quick smoke test**

Add to end of `db.ts`:

```typescript
if (import.meta.main) {
  const db = openDb(":memory:");
  const vecVersion = db.query("SELECT vec_version()").get() as any;
  console.log("DB module OK, sqlite-vec:", Object.values(vecVersion)[0]);
  db.close();
}
```

Run: `bun run scripts/lib/db.ts`
Expected: `DB module OK, sqlite-vec: v0.1.6` (or similar)

**Step 3: Commit**

```bash
git add scripts/lib/db.ts
git commit -m "feat: SQLite database module with sqlite-vec"
```

**Verify:** `bun run scripts/lib/db.ts` prints OK with the sqlite-vec version.

---

### Task 4: Build script — load text records into SQLite

**Files:**
- Create: `scripts/build-db.ts`

**Step 1: Write the build script**

```typescript
// scripts/build-db.ts
import { resolve } from "node:path";
import { unlinkSync, existsSync } from "node:fs";
import { readCatalog } from "./lib/catalog.ts";
import { openDb } from "./lib/db.ts";

const ROOT = resolve(import.meta.dirname, "..");
const DB_PATH = resolve(ROOT, "catalog/embeddings.db");

// Delete existing DB for a clean build
if (existsSync(DB_PATH)) {
  unlinkSync(DB_PATH);
  console.log("Removed existing embeddings.db");
}

const db = openDb(DB_PATH);
const catalog = readCatalog();
console.log(`Read ${catalog.length} mappings from catalog`);

// Collect all text units
interface TextUnit {
  id: string;
  slug: string;
  kind: string;
  section: string;
  text: string;
}

const units: TextUnit[] = [];

for (const entry of catalog) {
  // Title
  units.push({
    id: `${entry.slug}::title::0`,
    slug: entry.slug,
    kind: entry.kind,
    section: "title",
    text: entry.name,
  });

  // Transfers
  for (const [i, t] of entry.transfers.entries()) {
    units.push({
      id: `${entry.slug}::transfer::${i}`,
      slug: entry.slug,
      kind: entry.kind,
      section: "transfer",
      text: t,
    });
  }

  // Limits
  for (const [i, l] of entry.limits.entries()) {
    units.push({
      id: `${entry.slug}::limit::${i}`,
      slug: entry.slug,
      kind: entry.kind,
      section: "limit",
      text: l,
    });
  }

  // Expressions
  for (const [i, e] of entry.expressions.entries()) {
    units.push({
      id: `${entry.slug}::expression::${i}`,
      slug: entry.slug,
      kind: entry.kind,
      section: "expression",
      text: e,
    });
  }
}

// Insert all records in a transaction
const insert = db.prepare(`
  INSERT INTO embedding_records (id, slug, kind, section, text, model, model_version, created_at)
  VALUES (?, ?, ?, ?, ?, NULL, NULL, ?)
`);

const now = new Date().toISOString();
db.transaction(() => {
  for (const unit of units) {
    insert.run(unit.id, unit.slug, unit.kind, unit.section, unit.text, now);
  }
})();

// Report
const counts = db.query(
  "SELECT section, COUNT(*) as count FROM embedding_records GROUP BY section ORDER BY section"
).all() as Array<{ section: string; count: number }>;

console.log(`\nInserted ${units.length} text units:`);
for (const { section, count } of counts) {
  console.log(`  ${section.padEnd(12)} ${count}`);
}

db.close();
console.log(`\nDatabase written to ${DB_PATH}`);
```

**Step 2: Run the build script**

Run: `bun run scripts/build-db.ts`
Expected output:

```
Read 445 mappings from catalog

Inserted NNNN text units:
  expression   NNNN
  limit        NNNN
  title        445
  transfer     NNNN

Database written to /Users/fshot/code/fshot/metaphorex/catalog/embeddings.db
```

**Step 3: Verify with sqlite3 CLI**

Run: `sqlite3 catalog/embeddings.db "SELECT section, COUNT(*) FROM embedding_records GROUP BY section"`
Expected: Same counts as the script output.

Run: `sqlite3 catalog/embeddings.db "SELECT id, text FROM embedding_records WHERE slug = 'argument-is-war' LIMIT 5"`
Expected: Title + first few transfers for argument-is-war.

**Step 4: Commit**

```bash
git add scripts/build-db.ts
git commit -m "feat: build script loads catalog text units into SQLite"
```

**Verify:** `bun run scripts/build-db.ts` runs clean. `sqlite3 catalog/embeddings.db "SELECT COUNT(*) FROM embedding_records"` returns a number in the thousands.

---

### Task 5: Add sqlite-vec virtual table with random vectors

**Files:**
- Modify: `scripts/lib/db.ts` — add vec0 virtual table creation
- Modify: `scripts/build-db.ts` — generate and insert random vectors

**Step 1: Add vec0 table to db.ts**

In `scripts/lib/db.ts`, after the `idx_records_section` index creation, add:

```typescript
  db.run(`
    CREATE VIRTUAL TABLE IF NOT EXISTS embeddings USING vec0(
      id TEXT PRIMARY KEY,
      embedding FLOAT[1536]
    )
  `);
```

**Step 2: Add random vector generation to build-db.ts**

After the text record insertion transaction, add:

```typescript
// Insert random vectors (placeholder until real embeddings)
console.log("\nGenerating random vectors (placeholder)...");

const DIMS = 1536;

const insertVec = db.prepare(
  "INSERT INTO embeddings (id, embedding) VALUES (?, ?)"
);

db.transaction(() => {
  for (const unit of units) {
    const vec = new Float32Array(DIMS);
    for (let d = 0; d < DIMS; d++) vec[d] = Math.random() - 0.5;
    insertVec.run(unit.id, vec);
  }
})();

console.log(`Inserted ${units.length} random vectors (${DIMS} dims each)`);
```

**Step 3: Run the updated build script**

Run: `bun run scripts/build-db.ts`
Expected: Previous output plus `Inserted NNNN random vectors (1536 dims each)`.

**Step 4: Verify vectors exist**

Run: `sqlite3 catalog/embeddings.db "SELECT COUNT(*) FROM embeddings"`
Expected: Same count as `embedding_records`.

**Step 5: Commit**

```bash
git add scripts/lib/db.ts scripts/build-db.ts
git commit -m "feat: sqlite-vec virtual table with random placeholder vectors"
```

**Verify:** `bun run scripts/build-db.ts` completes without errors. Vector count matches text record count.

---

### Task 6: Search script with nearest-neighbor queries

**Files:**
- Create: `scripts/search.ts`

**Step 1: Write the search script**

```typescript
// scripts/search.ts
// Usage: bun run scripts/search.ts <query>
// With random vectors this returns random results — proves plumbing works.

import { resolve } from "node:path";
import { openDb } from "./lib/db.ts";

const ROOT = resolve(import.meta.dirname, "..");
const DB_PATH = resolve(ROOT, "catalog/embeddings.db");
const DIMS = 1536;
const K = 10;

const query = process.argv.slice(2).join(" ");
if (!query) {
  console.error("Usage: bun run scripts/search.ts <query>");
  process.exit(1);
}

const db = openDb(DB_PATH);

// Generate a random query vector (placeholder until real embeddings)
const queryVec = new Float32Array(DIMS);
for (let d = 0; d < DIMS; d++) queryVec[d] = Math.random() - 0.5;

console.log(`Query: "${query}"`);
console.log(`(Using random vectors — results are meaningless placeholders)\n`);

// sqlite-vec nearest neighbor search
// vec0 returns rows ordered by distance; join to get metadata
const results = db.query(`
  SELECT
    r.slug,
    r.kind,
    r.section,
    r.text,
    e.distance
  FROM embeddings e
  JOIN embedding_records r ON r.id = e.id
  WHERE e.embedding MATCH ?
    AND k = ?
  ORDER BY e.distance
`).all(queryVec, K * 3) as Array<{
  slug: string;
  kind: string;
  section: string;
  text: string;
  distance: number;
}>;

// Deduplicate by slug — keep best (lowest distance) match per mapping
const bySlug = new Map<string, typeof results[0]>();
for (const row of results) {
  if (!bySlug.has(row.slug) || bySlug.get(row.slug)!.distance > row.distance) {
    bySlug.set(row.slug, row);
  }
}

// Sort by distance, take top K
const topResults = [...bySlug.values()]
  .sort((a, b) => a.distance - b.distance)
  .slice(0, K);

// Print results
for (const r of topResults) {
  const score = Math.max(0, 1 - r.distance).toFixed(2);
  const slug = r.slug.padEnd(30);
  const section = `[${r.section}]`.padEnd(14);
  const text = r.text.length > 60 ? r.text.slice(0, 57) + "..." : r.text;
  console.log(`${slug} ${section} ${score}  "${text}"`);
}

db.close();
```

**Step 2: Run the search**

Run: `bun run scripts/search.ts "items pile up until a processor becomes available"`
Expected: 10 results with slugs, sections, scores, and text snippets.
Results are random (garbage vectors), but the output format and pipeline work.

**Step 3: Run a second search to confirm results differ**

Run: `bun run scripts/search.ts "something breaks upstream"`
Expected: Different random results (proves it's generating new query vectors).

**Step 4: Commit**

```bash
git add scripts/search.ts
git commit -m "feat: search script with nearest-neighbor queries (random vectors)"
```

**Verify:** Two different search queries both return formatted results. Pipeline is proven end-to-end.

---

### Task 7: Real OpenAI embeddings

**Files:**
- Modify: `scripts/build-db.ts` — add OpenAI embedding calls
- Modify: `scripts/search.ts` — embed query with OpenAI
- Modify: `package.json` — add `openai` dependency

**Step 1: Add openai dependency**

Run: `bun add openai`

**Step 2: Add embedding function to build-db.ts**

Replace the random vector generation section with real OpenAI calls.
Key changes:

```typescript
import OpenAI from "openai";

const MODEL = "text-embedding-3-small";
const DIMS = 1536;
const BATCH_SIZE = 100;

// Check for API key
if (!process.env.OPENAI_API_KEY) {
  console.error("OPENAI_API_KEY environment variable is required");
  process.exit(1);
}

const openai = new OpenAI();

// Model mismatch guard
const storedModel = db.query(
  "SELECT value FROM meta WHERE key = 'embedding_model'"
).get() as { value: string } | null;

if (storedModel && storedModel.value !== MODEL) {
  console.error(`Model mismatch: DB has ${storedModel.value}, script uses ${MODEL}`);
  console.error("Delete catalog/embeddings.db and rebuild.");
  process.exit(1);
}

db.run("INSERT OR REPLACE INTO meta VALUES ('embedding_model', ?)", [MODEL]);
db.run("INSERT OR REPLACE INTO meta VALUES ('embedding_dimensions', ?)", [String(DIMS)]);

// Batch embed
async function embedBatch(texts: string[]): Promise<number[][]> {
  const response = await openai.embeddings.create({
    model: MODEL,
    input: texts,
  });
  return response.data.map((d) => d.embedding);
}

console.log(`\nEmbedding ${units.length} units with ${MODEL}...`);

const insertVec = db.prepare(
  "INSERT INTO embeddings (id, embedding) VALUES (?, ?)"
);

for (let i = 0; i < units.length; i += BATCH_SIZE) {
  const batch = units.slice(i, i + BATCH_SIZE);
  const texts = batch.map((u) => u.text);
  const vectors = await embedBatch(texts);

  db.transaction(() => {
    for (const [j, unit] of batch.entries()) {
      insertVec.run(unit.id, new Float32Array(vectors[j]));
    }
  })();

  const done = Math.min(i + BATCH_SIZE, units.length);
  console.log(`  ${done} / ${units.length}`);
}
```

**Step 3: Update search.ts to embed the query**

Replace the random query vector generation with:

```typescript
import OpenAI from "openai";

const MODEL = "text-embedding-3-small";

if (!process.env.OPENAI_API_KEY) {
  console.error("OPENAI_API_KEY environment variable is required");
  process.exit(1);
}

const openai = new OpenAI();

// Check model matches what was used to build the DB
const storedModel = db.query(
  "SELECT value FROM meta WHERE key = 'embedding_model'"
).get() as { value: string } | null;

if (!storedModel) {
  console.error("No embedding model in DB. Run build-db.ts first with real embeddings.");
  process.exit(1);
}
if (storedModel.value !== MODEL) {
  console.error(`Model mismatch: DB has ${storedModel.value}, search uses ${MODEL}`);
  process.exit(1);
}

// Embed the query
const response = await openai.embeddings.create({
  model: MODEL,
  input: [query],
});
const queryVec = new Float32Array(response.data[0].embedding);
```

Remove the "(Using random vectors)" disclaimer from the output.

**Step 4: Rebuild the database with real embeddings**

Run: `bun run scripts/build-db.ts`
Expected: Progress output showing batches of 100, completing in under a minute.
Total cost: ~$0.01.

**Step 5: Test with a structural query**

Run: `bun run scripts/search.ts "items pile up until a processor becomes available"`
Expected: Results should include mappings with queue/buffer/pipeline-like structural propositions. The matched text should be a specific transfer proposition, not just a title.

Run: `bun run scripts/search.ts "something breaks when boundaries are unclear"`
Expected: Different, structurally relevant results.

**Step 6: Commit**

```bash
git add package.json bun.lock scripts/build-db.ts scripts/search.ts
git commit -m "feat: real OpenAI embeddings for catalog search"
```

**Verify:** Two different structural queries return semantically relevant results. The matched propositions make sense as structural matches, not just topic matches.

---

### Task 8: CLI search with filters

**Files:**
- Modify: `scripts/search.ts` — add --section, --kind, --json flags

**Step 1: Add argument parsing**

Parse CLI args before the query:

```typescript
const args = process.argv.slice(2);
let sectionFilter: string | null = null;
let kindFilter: string | null = null;
let jsonOutput = false;
const queryParts: string[] = [];

for (let i = 0; i < args.length; i++) {
  if (args[i] === "--section" && i + 1 < args.length) {
    sectionFilter = args[++i];
  } else if (args[i] === "--kind" && i + 1 < args.length) {
    kindFilter = args[++i];
  } else if (args[i] === "--json") {
    jsonOutput = true;
  } else {
    queryParts.push(args[i]);
  }
}

const query = queryParts.join(" ");
if (!query) {
  console.error("Usage: bun run scripts/search.ts [--section transfer|limit|expression|title] [--kind metaphor|pattern|...] [--json] <query>");
  process.exit(1);
}
```

**Step 2: Add post-query filtering**

After the nearest-neighbor search, filter results:

```typescript
let filtered = results;
if (sectionFilter) {
  filtered = filtered.filter((r) => r.section === sectionFilter);
}
if (kindFilter) {
  filtered = filtered.filter((r) => r.kind === kindFilter);
}
```

Apply deduplication and top-K on the filtered set.

**Step 3: Add JSON output mode**

```typescript
if (jsonOutput) {
  const output = topResults.map((r) => ({
    slug: r.slug,
    kind: r.kind,
    section: r.section,
    matchedText: r.text,
    score: Math.max(0, 1 - r.distance),
  }));
  console.log(JSON.stringify(output, null, 2));
} else {
  // existing formatted output
}
```

**Step 4: Test all filter combinations**

Run: `bun run scripts/search.ts --section transfer "blockage propagates"`
Expected: Only transfer propositions in results.

Run: `bun run scripts/search.ts --section limit "fails when boundaries unclear"`
Expected: Only limit propositions in results.

Run: `bun run scripts/search.ts --kind metaphor "strength and power"`
Expected: Only metaphor-kind entries in results.

Run: `bun run scripts/search.ts --json "items accumulate"`
Expected: JSON array output.

**Step 5: Commit**

```bash
git add scripts/search.ts
git commit -m "feat: search CLI with section, kind, and JSON output filters"
```

**Verify:** Each filter combination returns correctly filtered results. JSON output parses cleanly with `bun run scripts/search.ts --json "test" | python -m json.tool`.

---

### Task 9: Clean up test file, final verification

**Files:**
- Delete: `scripts/test-sqlite.ts` (no longer needed, functionality covered by db.ts)

**Step 1: Remove the scaffolding test file**

```bash
git rm scripts/test-sqlite.ts
```

**Step 2: Full pipeline verification**

Run these in sequence:

```bash
# 1. Clean build
rm -f catalog/embeddings.db
bun run scripts/build-db.ts

# 2. Structural similarity search
bun run scripts/search.ts "items pile up until a processor becomes available"

# 3. Transfer-only search
bun run scripts/search.ts --section transfer "blockage propagates upstream"

# 4. Limit-only search
bun run scripts/search.ts --section limit "fails when boundaries are unclear"

# 5. JSON output
bun run scripts/search.ts --json "accumulated cost of shortcuts"

# 6. Validator still passes (Python scripts unaffected)
uv run scripts/validate.py validate
```

All commands should succeed. Search results should be structurally meaningful.

**Step 3: Commit**

```bash
git add -A
git commit -m "chore: remove scaffolding test, verify full pipeline"
```

**Verify:** All 6 commands above run successfully. The validator passes (no regressions to existing Python tooling).
