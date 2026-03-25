/**
 * Classify catalog entries into tiers for summary enrichment.
 *
 * Tier 1: Name is self-explanatory → Sonnet, batches of 100
 * Tier 2: Name is suggestive but needs context → Opus, batches of 50
 * Tier 3: Name is opaque or domain-specific → Opus, batches of 30
 *
 * Usage: bun run scripts/tier-entries.ts > playbooks/summary-enrichment/tier-assignments.json
 *
 * /// <reference types="bun-types" />
 */

import { readCatalog, type CatalogEntry } from "./lib/catalog.ts";

// ---------------------------------------------------------------------------
// Frame concreteness classifications
// ---------------------------------------------------------------------------

const CONCRETE_FRAMES = new Set([
  "architecture-and-building",
  "containers",
  "war",
  "food-and-cooking",
  "carpentry",
  "agriculture",
  "fire-safety",
  "horticulture",
  "fluid-dynamics",
  "journeys",
  "seafaring",
  "vision",
  "animal-behavior",
  "textiles",
  "mining",
  "games",
  "sports",
  "weather",
  "terrain",
  "hunting",
  "fishing",
  "theater",
  "music",
]);

const ABSTRACT_FRAMES = new Set([
  "psychotherapy",
  "philosophy",
  "phenomenology",
  "hermeneutics",
  "epistemology",
  "semiotics",
  "linguistics",
  "quantum-physics",
  "category-theory",
]);

// ---------------------------------------------------------------------------
// Scoring heuristics
// ---------------------------------------------------------------------------

const IS_PATTERN = /\bIs\b/; // "X Is Y" names
const POSSESSIVE_PROPER = /[A-Z][a-z]+'s\b/; // "Hofstadter's", "Conway's"
const NON_ASCII = /[àáâãäåæçèéêëìíîïñòóôõöùúûüýÿ]/i;

function tierScore(entry: CatalogEntry): number {
  let score = 0;

  // Name patterns
  if (IS_PATTERN.test(entry.name)) score += 2;
  if (entry.dead && entry.name.split(/\s+/).length <= 2) score += 2;
  if (entry.name.split(/\s+/).length === 1) score += 1;
  if (POSSESSIVE_PROPER.test(entry.name)) score -= 1;
  if (NON_ASCII.test(entry.name)) score -= 2;

  // Source frame concreteness
  if (entry.sourceFrame && CONCRETE_FRAMES.has(entry.sourceFrame)) score += 1;
  if (entry.sourceFrame && ABSTRACT_FRAMES.has(entry.sourceFrame)) score -= 1;

  // Abstraction level
  if (entry.abstractionLevel === "primitive") score += 1;
  if (entry.abstractionLevel === "specific") score -= 1;

  // Mental models with long names are often opaque
  if (entry.kind === "mental-model" && entry.name.split(/\s+/).length > 3)
    score -= 1;

  return score;
}

function assignTier(score: number): 1 | 2 | 3 {
  if (score >= 2) return 1;
  if (score >= 0) return 2;
  return 3;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

const entries = await readCatalog();

// Skip entries that already have a summary
const todo = entries.filter((e) => !e.summary);

const tiers: Record<1 | 2 | 3, { slug: string; name: string; score: number }[]> = {
  1: [],
  2: [],
  3: [],
};

for (const entry of todo) {
  const score = tierScore(entry);
  const tier = assignTier(score);
  tiers[tier].push({ slug: entry.slug, name: entry.name, score });
}

// Sort each tier by slug for deterministic output
for (const t of [1, 2, 3] as const) {
  tiers[t].sort((a, b) => a.slug.localeCompare(b.slug));
}

// Output JSON to stdout
const output = {
  generated: new Date().toISOString().split("T")[0],
  total: todo.length,
  skipped: entries.length - todo.length,
  counts: {
    tier1: tiers[1].length,
    tier2: tiers[2].length,
    tier3: tiers[3].length,
  },
  tier1: tiers[1].map((e) => e.slug),
  tier2: tiers[2].map((e) => e.slug),
  tier3: tiers[3].map((e) => e.slug),
};

console.log(JSON.stringify(output, null, 2));

// Summary to stderr
const sample = (arr: typeof tiers[1], n: number) =>
  arr
    .slice(0, n)
    .map((e) => `  ${e.slug} (score: ${e.score})`)
    .join("\n");

console.error(`\n=== Tier Assignments ===`);
console.error(`Total: ${todo.length} entries (${entries.length - todo.length} already have summary)`);
console.error(`Tier 1 (self-explanatory): ${tiers[1].length}`);
console.error(sample(tiers[1], 5));
console.error(`Tier 2 (needs context):    ${tiers[2].length}`);
console.error(sample(tiers[2], 5));
console.error(`Tier 3 (opaque/domain):    ${tiers[3].length}`);
console.error(sample(tiers[3], 5));
