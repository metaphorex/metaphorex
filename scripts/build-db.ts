// scripts/build-db.ts
import { resolve } from "node:path";
import { unlinkSync, existsSync } from "node:fs";
import OpenAI from "openai";
import { readCatalog } from "./lib/catalog.ts";
import { openDb } from "./lib/db.ts";

const ROOT = resolve(import.meta.dirname!, "..");
const DB_PATH = resolve(ROOT, "catalog/embeddings.db");

const MODEL = "openai/text-embedding-3-small";
const DIMS = 1536;
const BATCH_SIZE = 100;

if (!process.env.OPENROUTER_API_KEY) {
  console.error("OPENROUTER_API_KEY environment variable is required");
  console.error("Run: source .envrc");
  process.exit(1);
}

const openai = new OpenAI({
  baseURL: "https://openrouter.ai/api/v1",
  apiKey: process.env.OPENROUTER_API_KEY,
});

// Delete existing DB for a clean build
if (existsSync(DB_PATH)) {
  unlinkSync(DB_PATH);
  console.log("Removed existing embeddings.db");
}

const db = openDb(DB_PATH);

// Model mismatch guard
const storedModel = db.query("SELECT value FROM meta WHERE key = 'embedding_model'").get() as { value: string } | null;
if (storedModel && storedModel.value !== MODEL) {
  console.error(`Model mismatch: DB has ${storedModel.value}, script uses ${MODEL}`);
  console.error("Delete catalog/embeddings.db and rebuild.");
  process.exit(1);
}
db.run("INSERT OR REPLACE INTO meta VALUES ('embedding_model', ?)", [MODEL]);
db.run("INSERT OR REPLACE INTO meta VALUES ('embedding_dimensions', ?)", [String(DIMS)]);

const catalog = await readCatalog();
console.log(`Read ${catalog.length} entries from catalog`);

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
  VALUES (?, ?, ?, ?, ?, ?, '1', ?)
`);

const now = new Date().toISOString();
db.transaction(() => {
  for (const unit of units) {
    insert.run(unit.id, unit.slug, unit.kind, unit.section, unit.text, MODEL, now);
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

// Embed in batches via OpenRouter
async function embedBatch(texts: string[]): Promise<number[][]> {
  const response = await openai.embeddings.create({
    model: MODEL,
    input: texts,
  });
  return response.data.map((d) => d.embedding);
}

console.log(`\nEmbedding ${units.length} units with ${MODEL}...`);
const insertVec = db.prepare("INSERT INTO embeddings (id, embedding) VALUES (?, ?)");

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

db.close();
console.log(`\nDatabase written to ${DB_PATH}`);
