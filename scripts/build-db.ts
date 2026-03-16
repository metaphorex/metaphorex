// scripts/build-db.ts
import { resolve } from "node:path";
import { unlinkSync, existsSync } from "node:fs";
import { readCatalog } from "./lib/catalog.ts";
import { openDb } from "./lib/db.ts";

const ROOT = resolve(import.meta.dirname!, "..");
const DB_PATH = resolve(ROOT, "catalog/embeddings.db");

// Delete existing DB for a clean build
if (existsSync(DB_PATH)) {
  unlinkSync(DB_PATH);
  console.log("Removed existing embeddings.db");
}

const db = openDb(DB_PATH);
const catalog = await readCatalog();
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

db.close();
console.log(`\nDatabase written to ${DB_PATH}`);
