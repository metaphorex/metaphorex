// scripts/eval.ts
// Usage: bun run scripts/eval.ts --suite a

import { resolve } from "node:path";
import { writeFileSync, mkdirSync } from "node:fs";
import { search, type SearchResult } from "./lib/search.ts";

const ROOT = resolve(import.meta.dirname!, "..");
const EVALS_DIR = resolve(ROOT, "docs/evals");

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

interface StructuralTestCase {
  name: string;
  query: string;
  section?: string;
  kind?: string;
  expectedSlugs: string[];
}

interface TestResult {
  name: string;
  query: string;
  pass: boolean;
  expectedSlugs: string[];
  foundSlugs: string[];
  missingSlugs: string[];
  topResults: Array<{ slug: string; score: number; section: string }>;
}

// ---------------------------------------------------------------------------
// Suite A — Structural search quality
// ---------------------------------------------------------------------------

const STRUCTURAL_TESTS: StructuralTestCase[] = [
  {
    name: "blockage-cascade",
    query: "blockage at one point causes problems everywhere downstream",
    expectedSlugs: ["bottleneck", "the-pipeline-pattern", "data-flow-is-fluid-flow", "yak-shaving"],
  },
  {
    name: "accumulated-cost",
    query: "accumulated cost of past shortcuts compounds over time",
    expectedSlugs: ["technical-debt", "compounding", "mental-accounting", "moral-accounting"],
  },
  {
    name: "container-boundary",
    query: "boundaries that protect also isolate and trap",
    expectedSlugs: ["relationships-are-enclosures", "firewall", "ai-safety-is-containment", "activities-are-containers", "categories-are-containers"],
  },
  {
    name: "threshold-trigger",
    query: "a small input crosses a threshold and triggers a disproportionately large response",
    expectedSlugs: ["activation-energy", "nonlinearity", "tipping-point"],
  },
  {
    name: "map-territory-reification",
    query: "the model becomes confused with the thing it models",
    expectedSlugs: ["the-map-is-not-the-territory"],
  },
  {
    name: "transfer-only-debt",
    query: "interest compounds on deferred work",
    section: "transfer",
    expectedSlugs: ["technical-debt", "compounding"],
  },
  {
    name: "limit-only-debt",
    query: "the metaphor makes it hard to quantify or prioritize",
    section: "limit",
    expectedSlugs: ["technical-debt"],
  },
  {
    name: "expression-detection",
    query: "we need to pay down our tech debt before the pipeline gets clogged",
    section: "expression",
    expectedSlugs: ["technical-debt", "the-pipeline-pattern"],
  },
  {
    name: "cross-domain-structure",
    query: "removing one part causes the whole system to collapse",
    expectedSlugs: ["redundancy", "jenga"],
  },
  {
    name: "adversarial-framing",
    query: "framing a collaborative activity as a competition with winners and losers",
    expectedSlugs: ["argument-is-war", "competition-is-competition-for-desired-objects"],
  },
];

// ---------------------------------------------------------------------------
// Runner
// ---------------------------------------------------------------------------

async function runStructuralTest(tc: StructuralTestCase): Promise<TestResult> {
  const results = await search(tc.query, {
    k: 5,
    section: tc.section,
    kind: tc.kind,
  });

  const topSlugs = results.map((r) => r.slug);
  const foundSlugs = tc.expectedSlugs.filter((s) => topSlugs.includes(s));
  const missingSlugs = tc.expectedSlugs.filter((s) => !topSlugs.includes(s));
  const pass = missingSlugs.length === 0;

  return {
    name: tc.name,
    query: tc.query,
    pass,
    expectedSlugs: tc.expectedSlugs,
    foundSlugs,
    missingSlugs,
    topResults: results.map((r) => ({
      slug: r.slug,
      score: parseFloat(r.score.toFixed(4)),
      section: r.section,
    })),
  };
}

async function runSuiteA(): Promise<TestResult[]> {
  const results: TestResult[] = [];
  for (const tc of STRUCTURAL_TESTS) {
    process.stdout.write(`  ${tc.name} ... `);
    const result = await runStructuralTest(tc);
    console.log(result.pass ? "PASS" : "FAIL");
    if (!result.pass) {
      console.log(`    missing: ${result.missingSlugs.join(", ")}`);
      console.log(`    got:     ${result.topResults.map((r) => r.slug).join(", ")}`);
    }
    results.push(result);
  }
  return results;
}

// ---------------------------------------------------------------------------
// Report generation
// ---------------------------------------------------------------------------

function generateReport(suite: string, results: TestResult[]): string {
  const passed = results.filter((r) => r.pass).length;
  const total = results.length;
  const now = new Date().toISOString();

  let md = `# Eval Report: Suite ${suite.toUpperCase()}\n\n`;
  md += `**Date:** ${now}\n`;
  md += `**Results:** ${passed}/${total} passed\n\n`;
  md += `## Summary\n\n`;
  md += `| Test | Result | Found | Missing |\n`;
  md += `|------|--------|-------|---------|\n`;

  for (const r of results) {
    const status = r.pass ? "PASS" : "FAIL";
    const found = r.foundSlugs.join(", ") || "-";
    const missing = r.missingSlugs.join(", ") || "-";
    md += `| ${r.name} | ${status} | ${found} | ${missing} |\n`;
  }

  md += `\n## Details\n\n`;

  for (const r of results) {
    md += `### ${r.name} ${r.pass ? "PASS" : "FAIL"}\n\n`;
    md += `**Query:** "${r.query}"\n\n`;
    md += `**Expected:** ${r.expectedSlugs.join(", ")}\n\n`;
    md += `Top 5 results:\n\n`;
    md += `| # | Slug | Section | Score |\n`;
    md += `|---|------|---------|-------|\n`;
    for (let i = 0; i < r.topResults.length; i++) {
      const tr = r.topResults[i];
      md += `| ${i + 1} | ${tr.slug} | ${tr.section} | ${tr.score} |\n`;
    }
    md += `\n`;
  }

  return md;
}

// ---------------------------------------------------------------------------
// CLI
// ---------------------------------------------------------------------------

const args = process.argv.slice(2);
let suite = "a";

for (let i = 0; i < args.length; i++) {
  if (args[i] === "--suite" && i + 1 < args.length) {
    suite = args[++i].toLowerCase();
  }
}

console.log(`Running eval suite ${suite.toUpperCase()}...\n`);

let results: TestResult[];

switch (suite) {
  case "a":
    results = await runSuiteA();
    break;
  default:
    console.error(`Unknown suite: ${suite}`);
    process.exit(1);
}

const passed = results.filter((r) => r.pass).length;
const total = results.length;
console.log(`\n${passed}/${total} passed`);

// Write report
mkdirSync(EVALS_DIR, { recursive: true });
const dateStr = new Date().toISOString().slice(0, 10);
const reportPath = resolve(EVALS_DIR, `${dateStr}-eval-report.md`);
const report = generateReport(suite, results);
writeFileSync(reportPath, report);
console.log(`Report written to ${reportPath}`);
