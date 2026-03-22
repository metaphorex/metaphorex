// scripts/eval-structural.ts
// Usage: source .envrc && bun run scripts/eval-structural.ts
//
// Evaluates whether structural enrichment tags improve non-obvious metaphor
// retrieval. For each analogy triple (A, B_structural, C_topical):
//   - Baseline: embed A's transfers+limits text, compare cosine sim to B and C
//   - Enriched: prepend structural tags to text before embedding, compare again
//   - Success: B ranks above C (structural match beats topical trap)
//
// See: docs/plans/2026-03-20-structural-enrichment-vocabulary.md
//      docs/evals/structural-enrichment-eval-set.yaml

import { resolve } from "node:path";
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { parse as parseYaml } from "yaml";
import OpenAI from "openai";
import { readCatalog, type CatalogEntry } from "./lib/catalog.ts";

const ROOT = resolve(import.meta.dirname!, "..");
const EVALS_DIR = resolve(ROOT, "docs/evals");
const EVAL_SET_PATH = resolve(EVALS_DIR, "structural-enrichment-eval-set.yaml");

const MODEL = "openai/text-embedding-3-small";
const BATCH_SIZE = 50;

// ---------------------------------------------------------------------------
// Setup
// ---------------------------------------------------------------------------

if (!process.env.OPENROUTER_API_KEY) {
  console.error("OPENROUTER_API_KEY required. Run: source .envrc");
  process.exit(1);
}

const openai = new OpenAI({
  baseURL: "https://openrouter.ai/api/v1",
  apiKey: process.env.OPENROUTER_API_KEY,
});

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

interface EvalEntry {
  slug: string;
  kind: string;
  source_frame: string;
  embodied_patterns: string[];
  relation_types: string[];
  structure: string[];
  abstraction_level: string;
}

interface AnalogyTriple {
  id: string;
  description: string;
  A: string; // query slug
  B: string; // structural match (should rank higher)
  C: string; // topical trap (should rank lower)
  structural_bridge: string;
  note?: string;
}

interface TripleResult {
  id: string;
  description: string;
  A: string;
  B: string;
  C: string;
  structural_bridge: string;
  baseline: {
    simAB: number;
    simAC: number;
    pass: boolean; // B ranked above C?
  };
  enriched: {
    simAB: number;
    simAC: number;
    pass: boolean;
  };
  flipped: "improved" | "regressed" | "unchanged";
}

// ---------------------------------------------------------------------------
// Embedding helpers
// ---------------------------------------------------------------------------

async function embedTexts(texts: string[]): Promise<number[][]> {
  const vectors: number[][] = [];
  for (let i = 0; i < texts.length; i += BATCH_SIZE) {
    const batch = texts.slice(i, i + BATCH_SIZE);
    const response = await openai.embeddings.create({
      model: MODEL,
      input: batch,
    });
    vectors.push(...response.data.map((d) => d.embedding));
  }
  return vectors;
}

function cosineSim(a: number[], b: number[]): number {
  let dot = 0, normA = 0, normB = 0;
  for (let i = 0; i < a.length; i++) {
    dot += a[i] * b[i];
    normA += a[i] * a[i];
    normB += b[i] * b[i];
  }
  return dot / (Math.sqrt(normA) * Math.sqrt(normB));
}

// ---------------------------------------------------------------------------
// Faceted similarity (Jaccard on tag sets)
// ---------------------------------------------------------------------------

function jaccard(a: string[], b: string[]): number {
  const setA = new Set(a);
  const setB = new Set(b);
  let intersection = 0;
  for (const x of setA) if (setB.has(x)) intersection++;
  const union = setA.size + setB.size - intersection;
  return union === 0 ? 0 : intersection / union;
}

// IDF-style weights: common values get downweighted, rare values boosted
const RELATION_WEIGHTS: Record<string, number> = {
  cause: 0.3, transform: 0.3,           // overrepresented (50%+ of catalog)
  prevent: 0.8, enable: 0.8, contain: 0.8, // common but still useful
  coordinate: 1.0, compete: 1.0, select: 1.0, accumulate: 1.0,
  translate: 1.3, decompose: 1.3, restore: 1.3, // rare = high signal
};

const EP_WEIGHTS: Record<string, number> = {
  force: 0.5, path: 0.5, container: 0.6, // overrepresented
  boundary: 0.7, matching: 0.7, scale: 0.8,
  flow: 0.9, "part-whole": 0.9, link: 0.9, balance: 0.9,
  "surface-depth": 1.0, "near-far": 1.0, iteration: 1.0,
  blockage: 1.0, "center-periphery": 1.1,
  accretion: 1.2, removal: 1.1, splitting: 1.2,
  merging: 1.3, "self-organization": 1.3,
  superimposition: 1.3, attraction: 1.5,
};

function parentOf(v: string): string {
  const idx = v.indexOf("/");
  return idx >= 0 ? v.slice(0, idx) : v;
}

function weightedJaccard(a: string[], b: string[], weights: Record<string, number>): number {
  const setA = new Set(a);
  const setB = new Set(b);
  let interWeight = 0;
  let unionWeight = 0;

  const bMatched = new Set<string>();
  const all = new Set([...setA, ...setB]);

  for (const v of all) {
    const w = weights[parentOf(v)] ?? 1.0;
    unionWeight += w;

    if (setA.has(v) && setB.has(v)) {
      // Exact match: full credit
      interWeight += w;
      bMatched.add(v);
    } else if (setA.has(v) && v.includes("/")) {
      // Check for parent-level match (cause/propagate ~ cause/compel → 0.3 credit)
      const parent = parentOf(v);
      let found = false;
      for (const bv of setB) {
        if (!bMatched.has(bv) && parentOf(bv) === parent && bv !== v) {
          interWeight += w * 0.3;
          bMatched.add(bv);
          found = true;
          break;
        }
      }
    }
  }
  return unionWeight === 0 ? 0 : interWeight / unionWeight;
}

/** Weighted faceted similarity across all structural tag fields */
function facetedSim(a: EvalEntry, b: EvalEntry): number {
  const epSim = weightedJaccard(a.embodied_patterns, b.embodied_patterns, EP_WEIGHTS);
  const rtSim = weightedJaccard(a.relation_types, b.relation_types, RELATION_WEIGHTS);
  const stSim = jaccard(a.structure, b.structure);
  const alSim = a.abstraction_level === b.abstraction_level ? 1.0 : 0.0;

  // Weights: embodied_patterns and relation_types are co-primary
  return epSim * 0.35 + rtSim * 0.35 + stSim * 0.20 + alSim * 0.10;
}

/** Blended score: faceted pre-filter + text similarity rerank */
function blendedSim(
  faceted: number,
  textSim: number,
  alpha: number, // weight on faceted (0-1)
): number {
  return alpha * faceted + (1 - alpha) * textSim;
}

// ---------------------------------------------------------------------------
// Text construction
// ---------------------------------------------------------------------------

function baselineText(entry: CatalogEntry): string {
  // Combine transfers + limits — the existing embedding strategy
  const parts: string[] = [];
  if (entry.transfers.length > 0) {
    parts.push(entry.transfers.join(" "));
  }
  if (entry.limits.length > 0) {
    parts.push(entry.limits.join(" "));
  }
  if (parts.length === 0) {
    // Fallback: use the entry name and expressions
    parts.push(entry.name);
    if (entry.expressions.length > 0) {
      parts.push(entry.expressions.join(" "));
    }
  }
  return parts.join(" ");
}

function enrichedText(entry: CatalogEntry, evalEntry: EvalEntry): string {
  // Prepend structural tags before the prose text
  const tags: string[] = [];
  tags.push(`[embodied_patterns: ${evalEntry.embodied_patterns.join(", ")}]`);
  tags.push(`[relation_types: ${evalEntry.relation_types.join(", ")}]`);
  tags.push(`[structure: ${evalEntry.structure.join(", ")}]`);
  tags.push(`[abstraction: ${evalEntry.abstraction_level}]`);
  tags.push(`[kind: ${evalEntry.kind}]`);

  return tags.join(" ") + " " + baselineText(entry);
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

console.log("Loading eval set...");
const evalSetRaw = readFileSync(EVAL_SET_PATH, "utf-8");
const evalSet = parseYaml(evalSetRaw) as {
  entries: EvalEntry[];
  analogy_triples: AnalogyTriple[];
};

console.log(`  ${evalSet.entries.length} tagged entries`);
console.log(`  ${evalSet.analogy_triples.length} analogy triples`);

// Build lookup maps
const evalEntryMap = new Map<string, EvalEntry>();
for (const e of evalSet.entries) {
  evalEntryMap.set(e.slug, e);
}

console.log("\nLoading catalog...");
const catalog = await readCatalog();
const catalogMap = new Map<string, CatalogEntry>();
for (const e of catalog) {
  catalogMap.set(e.slug, e);
}
console.log(`  ${catalog.length} total entries`);

// Collect all slugs needed for triples
const neededSlugs = new Set<string>();
for (const t of evalSet.analogy_triples) {
  neededSlugs.add(t.A);
  neededSlugs.add(t.B);
  neededSlugs.add(t.C);
}

// Verify all needed entries exist in both eval set and catalog
const missing: string[] = [];
for (const slug of neededSlugs) {
  if (!evalEntryMap.has(slug)) missing.push(`${slug} (not in eval set)`);
  if (!catalogMap.has(slug)) missing.push(`${slug} (not in catalog)`);
}
if (missing.length > 0) {
  console.error("\nMissing entries:");
  for (const m of missing) console.error(`  ${m}`);
  console.error("\nFix the eval set before running.");
  process.exit(1);
}

// Build baseline and enriched texts for all needed entries
console.log("\nBuilding text representations...");
const slugList = [...neededSlugs].sort();
const baselineTexts: string[] = [];
const enrichedTexts: string[] = [];

for (const slug of slugList) {
  const catEntry = catalogMap.get(slug)!;
  const evalEntry = evalEntryMap.get(slug)!;
  baselineTexts.push(baselineText(catEntry));
  enrichedTexts.push(enrichedText(catEntry, evalEntry));
}

// Embed both sets
console.log(`\nEmbedding ${slugList.length} entries (baseline)...`);
const baselineVecs = await embedTexts(baselineTexts);
console.log(`Embedding ${slugList.length} entries (enriched)...`);
const enrichedVecs = await embedTexts(enrichedTexts);

// Build slug -> vector maps
const baselineMap = new Map<string, number[]>();
const enrichedMap = new Map<string, number[]>();
for (let i = 0; i < slugList.length; i++) {
  baselineMap.set(slugList[i], baselineVecs[i]);
  enrichedMap.set(slugList[i], enrichedVecs[i]);
}

// ---------------------------------------------------------------------------
// Score all triples across multiple strategies
// ---------------------------------------------------------------------------

// Strategy configs: name, scoring function
const ALPHAS = [0.0, 0.3, 0.5, 0.7, 1.0];

interface StrategyResult {
  name: string;
  alpha: number; // -1 for text-only and tag-only
  passes: number;
  total: number;
  details: Array<{
    id: string;
    simAB: number;
    simAC: number;
    pass: boolean;
  }>;
}

function scoreTriple(
  t: AnalogyTriple,
  alpha: number,
): { simAB: number; simAC: number; pass: boolean } {
  const evalA = evalEntryMap.get(t.A)!;
  const evalB = evalEntryMap.get(t.B)!;
  const evalC = evalEntryMap.get(t.C)!;

  if (alpha === 0.0) {
    // Pure text baseline
    const simAB = cosineSim(baselineMap.get(t.A)!, baselineMap.get(t.B)!);
    const simAC = cosineSim(baselineMap.get(t.A)!, baselineMap.get(t.C)!);
    return { simAB, simAC, pass: simAB > simAC };
  }

  if (alpha === 1.0) {
    // Pure faceted (no text)
    const simAB = facetedSim(evalA, evalB);
    const simAC = facetedSim(evalA, evalC);
    return { simAB, simAC, pass: simAB > simAC };
  }

  // Blended
  const textAB = cosineSim(baselineMap.get(t.A)!, baselineMap.get(t.B)!);
  const textAC = cosineSim(baselineMap.get(t.A)!, baselineMap.get(t.C)!);
  const facAB = facetedSim(evalA, evalB);
  const facAC = facetedSim(evalA, evalC);
  const simAB = blendedSim(facAB, textAB, alpha);
  const simAC = blendedSim(facAC, textAC, alpha);
  return { simAB, simAC, pass: simAB > simAC };
}

console.log(`\nScoring ${evalSet.analogy_triples.length} triples across ${ALPHAS.length} strategies...\n`);

const strategyResults: StrategyResult[] = [];

for (const alpha of ALPHAS) {
  const name = alpha === 0.0 ? "text-only (baseline)"
    : alpha === 1.0 ? "faceted-only (tags)"
      : `blended (α=${alpha.toFixed(1)})`;

  const details: StrategyResult["details"] = [];
  let passes = 0;

  for (const t of evalSet.analogy_triples) {
    const result = scoreTriple(t, alpha);
    if (result.pass) passes++;
    details.push({ id: t.id, ...result });
  }

  strategyResults.push({
    name,
    alpha,
    passes,
    total: evalSet.analogy_triples.length,
    details,
  });
}

// Print comparison table
console.log("Strategy comparison:\n");
console.log("  Strategy                      Passes    Rate");
console.log("  " + "—".repeat(52));
for (const s of strategyResults) {
  const rate = (s.passes / s.total * 100).toFixed(0);
  const bar = "█".repeat(Math.round(s.passes / s.total * 30));
  console.log(`  ${s.name.padEnd(30)} ${String(s.passes).padStart(3)}/${s.total}   ${rate.padStart(3)}%  ${bar}`);
}

// Find best blended alpha
const bestStrategy = strategyResults.reduce((best, s) =>
  s.passes > best.passes ? s : best
);
console.log(`\n  Best: ${bestStrategy.name} (${bestStrategy.passes}/${bestStrategy.total})`);

// Detailed per-triple view for the best strategy vs baseline
const baseline = strategyResults.find((s) => s.alpha === 0.0)!;
const best = bestStrategy;

console.log(`\n\nPer-triple: baseline vs ${best.name}\n`);

let improved = 0, regressed = 0;
const results: TripleResult[] = [];

for (let i = 0; i < evalSet.analogy_triples.length; i++) {
  const t = evalSet.analogy_triples[i];
  const b = baseline.details[i];
  const e = best.details[i];

  const flipped = e.pass && !b.pass ? "improved"
    : !e.pass && b.pass ? "regressed"
      : "unchanged";

  if (flipped === "improved") improved++;
  if (flipped === "regressed") regressed++;

  const status = flipped === "improved" ? "FLIP +"
    : flipped === "regressed" ? "FLIP -"
      : e.pass ? "  ok  " : " miss ";

  console.log(
    `  ${status}  ${t.id} ${t.description.slice(0, 45).padEnd(47)}` +
    `base: ${b.simAB.toFixed(3)}/${b.simAC.toFixed(3)} ${b.pass ? "P" : "F"}  ` +
    `best: ${e.simAB.toFixed(3)}/${e.simAC.toFixed(3)} ${e.pass ? "P" : "F"}`
  );

  results.push({
    id: t.id,
    description: t.description,
    A: t.A,
    B: t.B,
    C: t.C,
    structural_bridge: t.structural_bridge,
    baseline: { simAB: b.simAB, simAC: b.simAC, pass: b.pass },
    enriched: { simAB: e.simAB, simAC: e.simAC, pass: e.pass },
    flipped,
  });
}

const baselinePasses = baseline.passes;
const enrichedPasses = best.passes;

// ---------------------------------------------------------------------------
// Summary
// ---------------------------------------------------------------------------

console.log(`\n${"=".repeat(70)}`);
console.log(`STRUCTURAL ENRICHMENT EVAL RESULTS`);
console.log(`${"=".repeat(70)}`);
console.log(`Total triples:      ${results.length}`);
console.log(`Baseline (text):    ${baselinePasses}/${results.length} (${(baselinePasses / results.length * 100).toFixed(0)}%)`);
console.log(`Best strategy:      ${best.name}`);
console.log(`Best passes:        ${enrichedPasses}/${results.length} (${(enrichedPasses / results.length * 100).toFixed(0)}%)`);
console.log(`Improved (flipped): ${improved}`);
console.log(`Regressed:          ${regressed}`);
console.log(`Net improvement:    ${improved - regressed > 0 ? "+" : ""}${improved - regressed}`);
console.log(`${"=".repeat(70)}`);

// Structural Surprise Rate: what fraction of best-strategy passes involve
// entries from different source frames?
const crossDomainPasses = results.filter((r) => {
  if (!r.enriched.pass) return false;
  const frameA = evalEntryMap.get(r.A)!.source_frame;
  const frameB = evalEntryMap.get(r.B)!.source_frame;
  return frameA !== frameB;
}).length;

console.log(`\nStructural Surprise Rate: ${crossDomainPasses}/${enrichedPasses} passes are cross-domain`);

// ---------------------------------------------------------------------------
// Report
// ---------------------------------------------------------------------------

let md = `# Structural Enrichment Eval Report\n\n`;
md += `**Date:** ${new Date().toISOString()}\n`;
md += `**Embedding model:** ${MODEL}\n`;
md += `**Entries tagged:** ${evalSet.entries.length}\n`;
md += `**Analogy triples:** ${results.length}\n\n`;

md += `## Strategy Comparison\n\n`;
md += `| Strategy | Passes | Rate |\n`;
md += `|----------|--------|------|\n`;
for (const s of strategyResults) {
  md += `| ${s.name} | ${s.passes}/${s.total} | ${(s.passes / s.total * 100).toFixed(0)}% |\n`;
}
md += `\n`;

md += `## Best Strategy vs Baseline\n\n`;
md += `| Metric | Baseline (text-only) | ${best.name} |\n`;
md += `|--------|---------------------|${"—".repeat(best.name.length + 2)}|\n`;
md += `| Passes | ${baselinePasses}/${results.length} (${(baselinePasses / results.length * 100).toFixed(0)}%) | ${enrichedPasses}/${results.length} (${(enrichedPasses / results.length * 100).toFixed(0)}%) |\n`;
md += `| Improved (flipped F→P) | — | ${improved} |\n`;
md += `| Regressed (flipped P→F) | — | ${regressed} |\n`;
md += `| Net improvement | — | ${improved - regressed > 0 ? "+" : ""}${improved - regressed} |\n`;
md += `| Cross-domain passes | — | ${crossDomainPasses}/${enrichedPasses} |\n\n`;

md += `## Detailed Results\n\n`;
md += `| ID | Description | A | B (structural) | C (topical) | Base A↔B | Base A↔C | Base | Enr A↔B | Enr A↔C | Enr | Flip |\n`;
md += `|----|-------------|---|----------------|-------------|----------|----------|------|---------|---------|-----|------|\n`;

for (const r of results) {
  md += `| ${r.id} | ${r.description.slice(0, 40)} | ${r.A} | ${r.B} | ${r.C} `;
  md += `| ${r.baseline.simAB.toFixed(3)} | ${r.baseline.simAC.toFixed(3)} | ${r.baseline.pass ? "P" : "F"} `;
  md += `| ${r.enriched.simAB.toFixed(3)} | ${r.enriched.simAC.toFixed(3)} | ${r.enriched.pass ? "P" : "F"} `;
  md += `| ${r.flipped === "improved" ? "+" : r.flipped === "regressed" ? "-" : "="} |\n`;
}

md += `\n## Improvements (baseline F → enriched P)\n\n`;
const improvements = results.filter((r) => r.flipped === "improved");
if (improvements.length === 0) {
  md += `None.\n\n`;
} else {
  for (const r of improvements) {
    md += `### ${r.id}: ${r.description}\n\n`;
    md += `- **A:** ${r.A}\n`;
    md += `- **B (correct):** ${r.B}\n`;
    md += `- **C (trap):** ${r.C}\n`;
    md += `- **Bridge:** ${r.structural_bridge}\n`;
    md += `- Baseline: A↔B ${r.baseline.simAB.toFixed(3)}, A↔C ${r.baseline.simAC.toFixed(3)} → FAIL (topical trap won)\n`;
    md += `- Enriched: A↔B ${r.enriched.simAB.toFixed(3)}, A↔C ${r.enriched.simAC.toFixed(3)} → PASS (structural match won)\n\n`;
  }
}

md += `## Regressions (baseline P → enriched F)\n\n`;
const regressions = results.filter((r) => r.flipped === "regressed");
if (regressions.length === 0) {
  md += `None.\n\n`;
} else {
  for (const r of regressions) {
    md += `### ${r.id}: ${r.description}\n\n`;
    md += `- **A:** ${r.A}\n`;
    md += `- **B (correct):** ${r.B}\n`;
    md += `- **C (trap):** ${r.C}\n`;
    md += `- Baseline: A↔B ${r.baseline.simAB.toFixed(3)}, A↔C ${r.baseline.simAC.toFixed(3)} → PASS\n`;
    md += `- Enriched: A↔B ${r.enriched.simAB.toFixed(3)}, A↔C ${r.enriched.simAC.toFixed(3)} → FAIL (regression)\n\n`;
  }
}

md += `## Methodology\n\n`;
md += `Each analogy triple contains:\n`;
md += `- **A** — query entry\n`;
md += `- **B** — structural match from a different source domain (should rank higher)\n`;
md += `- **C** — topical trap from the same/similar domain (should rank lower)\n\n`;
md += `**Strategies tested:**\n\n`;
md += `| Strategy | How it scores |\n`;
md += `|----------|---------------|\n`;
md += `| text-only (baseline) | cosine_sim of transfers+limits text embeddings |\n`;
md += `| faceted-only (tags) | Weighted Jaccard: 0.35×embodied_patterns + 0.35×relation_types + 0.20×structure + 0.10×abstraction_level |\n`;
md += `| blended (α=N) | α × faceted_sim + (1-α) × text_sim |\n\n`;
md += `A triple "passes" when sim(A, B) > sim(A, C).\n`;
md += `An "improvement" is a triple that fails baseline but passes the best strategy.\n`;
md += `The Structural Surprise Rate counts how many passes involve entries from different source frames.\n`;

mkdirSync(EVALS_DIR, { recursive: true });
const dateStr = new Date().toISOString().slice(0, 10);
const reportPath = resolve(EVALS_DIR, `${dateStr}-structural-enrichment-report.md`);
writeFileSync(reportPath, md);
console.log(`\nReport written to ${reportPath}`);
