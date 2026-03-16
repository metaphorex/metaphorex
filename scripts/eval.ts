// scripts/eval.ts
// Usage: bun run scripts/eval.ts --suite a|b|c|all

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
// Suite B — m4x vs raw Claude
// ---------------------------------------------------------------------------

import OpenAI from "openai";

function getOpenRouterClient(): OpenAI {
  return new OpenAI({
    baseURL: "https://openrouter.ai/api/v1",
    apiKey: process.env.OPENROUTER_API_KEY!,
  });
}

async function chatCompletion(
  model: string,
  systemPrompt: string,
  userPrompt: string,
): Promise<string> {
  const client = getOpenRouterClient();
  const response = await client.chat.completions.create({
    model,
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: userPrompt },
    ],
    max_tokens: 1500,
    temperature: 0,
  });
  return response.choices[0]?.message?.content ?? "";
}

interface SuiteBTestCase {
  name: string;
  scenario: string;
  searchQueries: string[];
}

const SUITE_B_TESTS: SuiteBTestCase[] = [
  {
    name: "microservices-design",
    scenario: "A queue-based microservices architecture where services communicate via message brokers, with circuit breakers for failure isolation and a shared database for state.",
    searchQueries: [
      "message queue processing pipeline",
      "circuit breaker failure isolation",
      "shared state coordination",
    ],
  },
  {
    name: "fast-growing-team",
    scenario: "A startup engineering team that grew from 5 to 50 in a year. The original founders still make most technical decisions. New hires feel they can't influence architecture. Knowledge lives in people's heads, not documentation.",
    searchQueries: [
      "knowledge hoarded by few people",
      "authority concentrated in founders",
      "oral tradition versus written documentation",
    ],
  },
  {
    name: "permissions-system",
    scenario: "We're designing a permissions system. Users have 'roles' that 'grant' them 'access' to 'resources'. Admins can 'delegate' permissions. There's an 'audit trail' of who 'gave' what access to whom.",
    searchQueries: [
      "roles as containers for capabilities",
      "granting access as giving possession",
      "hierarchical authority delegation",
    ],
  },
  {
    name: "ml-model-opacity",
    scenario: "A machine learning model has been retrained on production data so many times that nobody understands why it makes specific decisions. The team calls it 'the black box' and treats its outputs as 'predictions' that need 'confidence scores'.",
    searchQueries: [
      "black box opacity understanding",
      "prediction as oracle or prophecy",
      "confidence and certainty as measurable quantities",
    ],
  },
  {
    name: "code-review-as-war",
    scenario: "A team's code review process has become adversarial. Reviewers 'attack' PRs, authors 'defend' their decisions, people 'pick their battles' about which comments to address. Senior engineers use reviews to 'assert dominance'. New hires are afraid to submit PRs.",
    searchQueries: [
      "collaboration framed as combat",
      "critique as attack",
      "dominance hierarchy in technical evaluation",
    ],
  },
];

const SYSTEM_PROMPT_RAW = `You are analyzing which conceptual metaphors are active in a given scenario. For each metaphor you identify:
1. Name it (e.g., "ARGUMENT IS WAR")
2. Explain what structural assumptions it carries
3. Identify where it might mislead — what does the metaphor make hard to see?

Be specific. Focus on non-obvious metaphors, not just the surface-level ones. List at least 5 metaphors.`;

const SYSTEM_PROMPT_WITH_M4X = `You are analyzing which conceptual metaphors are active in a given scenario. You have access to results from a metaphor catalog search. Use these results as a starting point, but also identify metaphors the search may have missed.

For each metaphor you identify:
1. Name it (e.g., "ARGUMENT IS WAR") and note if it came from the catalog search
2. Explain what structural assumptions it carries
3. Identify where it might mislead — what does the metaphor make hard to see?

Be specific. Focus on non-obvious metaphors, not just the surface-level ones. List at least 5 metaphors.`;

const CLAUDE_MODEL = "anthropic/claude-sonnet-4";

interface SuiteBResult {
  name: string;
  scenario: string;
  searchResultsSummary: string;
  rawResponse: string;
  m4xResponse: string;
}

async function runSuiteB(): Promise<SuiteBResult[]> {
  const results: SuiteBResult[] = [];

  for (const test of SUITE_B_TESTS) {
    console.log(`  ${test.name}...`);

    // Run m4x searches
    const allSearchResults: SearchResult[] = [];
    for (const q of test.searchQueries) {
      const hits = await search(q, { k: 5 });
      allSearchResults.push(...hits);
    }

    // Dedupe by slug
    const seen = new Set<string>();
    const uniqueResults = allSearchResults.filter((r) => {
      if (seen.has(r.slug)) return false;
      seen.add(r.slug);
      return true;
    }).slice(0, 15);

    const searchContext = uniqueResults.map((r) =>
      `- **${r.slug}** [${r.section}] (score: ${r.score.toFixed(2)}): ${r.matchedText.slice(0, 120)}`
    ).join("\n");

    // (A) Raw Claude
    process.stdout.write(`    raw... `);
    const rawResponse = await chatCompletion(
      CLAUDE_MODEL, SYSTEM_PROMPT_RAW,
      `Scenario: ${test.scenario}`
    );
    console.log("done");

    // (B) Claude + m4x
    process.stdout.write(`    +m4x... `);
    const m4xResponse = await chatCompletion(
      CLAUDE_MODEL, SYSTEM_PROMPT_WITH_M4X,
      `Scenario: ${test.scenario}\n\n## Catalog search results:\n\n${searchContext}`
    );
    console.log("done");

    results.push({
      name: test.name,
      scenario: test.scenario,
      searchResultsSummary: searchContext,
      rawResponse,
      m4xResponse,
    });
  }

  return results;
}

// ---------------------------------------------------------------------------
// Suite C — Catalog coverage analysis
// ---------------------------------------------------------------------------

interface CoverageTestCase {
  name: string;
  query: string;
  domain: string;
}

const COVERAGE_TESTS: CoverageTestCase[] = [
  { name: "feedback-loop", query: "output feeds back as input, amplifying or dampening over time", domain: "systems" },
  { name: "erosion", query: "gradual degradation that is invisible until sudden failure", domain: "materials" },
  { name: "immune-response", query: "system detects foreign elements and mounts a defense that can itself cause damage", domain: "biology" },
  { name: "debt-servicing", query: "ongoing payments consume resources that could be used productively", domain: "economics" },
  { name: "scaffolding", query: "temporary structure that enables building but must be removed", domain: "construction" },
  { name: "fermentation", query: "controlled decay that produces something valuable", domain: "biology" },
  { name: "triage", query: "rapid sorting under resource scarcity to maximize outcomes", domain: "medicine" },
  { name: "terraforming", query: "reshaping an environment to support a different kind of life", domain: "science-fiction" },
  { name: "composting", query: "breaking down old material to nourish new growth", domain: "agriculture" },
  { name: "signal-noise", query: "separating meaningful information from random interference", domain: "engineering" },
  { name: "vaccination", query: "controlled exposure to a weakened threat builds resistance", domain: "medicine" },
  { name: "pruning", query: "removing parts to strengthen the whole", domain: "agriculture" },
  { name: "migration", query: "moving from one habitat to another when conditions change", domain: "ecology" },
  { name: "crystallization", query: "gradual solidification from fluid to rigid structure", domain: "chemistry" },
  { name: "phase-transition", query: "sudden qualitative change when a quantitative threshold is crossed", domain: "physics" },
  { name: "keystone-species", query: "one component whose removal causes ecosystem collapse", domain: "ecology" },
  { name: "sedimentation", query: "layers accumulate over time, earlier layers become inaccessible", domain: "geology" },
  { name: "pollination", query: "cross-fertilization between separate entities produces novel offspring", domain: "biology" },
  { name: "pressure-valve", query: "controlled release mechanism that prevents catastrophic failure", domain: "engineering" },
  { name: "succession", query: "one type of growth prepares the conditions for the next type", domain: "ecology" },
];

interface CoverageResult {
  name: string;
  query: string;
  domain: string;
  isHit: boolean;
  topScore: number;
  topResults: Array<{ slug: string; score: number; section: string; matchedText: string }>;
}

async function runSuiteC(): Promise<CoverageResult[]> {
  const results: CoverageResult[] = [];

  for (const test of COVERAGE_TESTS) {
    process.stdout.write(`  ${test.name}... `);
    const hits = await search(test.query, { k: 5 });

    const topScore = hits[0]?.score ?? 0;
    const isHit = topScore > 0.40;

    console.log(isHit
      ? `HIT (${topScore.toFixed(2)}) → ${hits[0].slug}`
      : `GAP (${topScore.toFixed(2)})`
    );

    results.push({
      name: test.name,
      query: test.query,
      domain: test.domain,
      isHit,
      topScore,
      topResults: hits.slice(0, 3).map((r) => ({
        slug: r.slug,
        score: r.score,
        section: r.section,
        matchedText: r.matchedText,
      })),
    });
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

function generateSuiteBReport(results: SuiteBResult[]): string {
  let md = `# Eval Report: Suite B — m4x vs Raw Claude\n\n`;
  md += `**Date:** ${new Date().toISOString()}\n`;
  md += `**Model:** ${CLAUDE_MODEL}\n`;
  md += `**Scenarios:** ${results.length}\n\n`;

  for (const r of results) {
    md += `## ${r.name}\n\n`;
    md += `**Scenario:** ${r.scenario}\n\n`;
    md += `### Search results injected\n\n${r.searchResultsSummary}\n\n`;
    md += `### Raw Claude (no tools)\n\n${r.rawResponse}\n\n`;
    md += `### Claude + m4x search\n\n${r.m4xResponse}\n\n`;
    md += `---\n\n`;
  }

  return md;
}

function generateSuiteCReport(results: CoverageResult[]): string {
  const hits = results.filter((r) => r.isHit);
  const gaps = results.filter((r) => !r.isHit);

  let md = `# Eval Report: Suite C — Catalog Coverage\n\n`;
  md += `**Date:** ${new Date().toISOString()}\n`;
  md += `**Coverage:** ${hits.length}/${results.length} (${(hits.length / results.length * 100).toFixed(0)}%)\n\n`;

  md += `## Summary\n\n`;
  md += `| Probe | Domain | Result | Top Score | Best Match |\n`;
  md += `|-------|--------|--------|-----------|------------|\n`;
  for (const r of results) {
    const status = r.isHit ? "HIT" : "GAP";
    const bestMatch = r.topResults[0]?.slug ?? "-";
    md += `| ${r.name} | ${r.domain} | ${status} | ${r.topScore.toFixed(2)} | ${bestMatch} |\n`;
  }

  md += `\n## Gaps (candidates for new content)\n\n`;
  for (const r of gaps) {
    md += `### ${r.name} (${r.domain})\n\n`;
    md += `**Query:** "${r.query}"\n\n`;
    md += `Closest matches:\n\n`;
    for (const [i, tr] of r.topResults.entries()) {
      md += `${i + 1}. **${tr.slug}** [${tr.section}] (${tr.score.toFixed(2)}): ${tr.matchedText.slice(0, 80)}...\n`;
    }
    md += `\n`;
  }

  md += `## Hits\n\n`;
  for (const r of hits) {
    md += `- **${r.name}** → ${r.topResults[0]?.slug} (${r.topScore.toFixed(2)})\n`;
  }
  md += `\n`;

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

if (!["a", "b", "c", "all"].includes(suite)) {
  console.error(`Unknown suite: ${suite}. Use --suite a|b|c|all`);
  process.exit(1);
}

mkdirSync(EVALS_DIR, { recursive: true });
const dateStr = new Date().toISOString().slice(0, 10);
const reports: string[] = [];

// Suite A
if (suite === "a" || suite === "all") {
  console.log(`Running eval suite A...\n`);
  const suiteAResults = await runSuiteA();
  const passed = suiteAResults.filter((r) => r.pass).length;
  console.log(`\n${passed}/${suiteAResults.length} passed`);
  const reportA = generateReport("a", suiteAResults);
  reports.push(reportA);
  if (suite === "a") {
    const path = resolve(EVALS_DIR, `${dateStr}-suite-a-report.md`);
    writeFileSync(path, reportA);
    console.log(`Report written to ${path}`);
  }
}

// Suite B
if (suite === "b" || suite === "all") {
  console.log(`Running eval suite B...\n`);
  const suiteBResults = await runSuiteB();
  console.log(`\n${suiteBResults.length} scenarios completed`);
  const reportB = generateSuiteBReport(suiteBResults);
  reports.push(reportB);
  if (suite === "b") {
    const path = resolve(EVALS_DIR, `${dateStr}-suite-b-report.md`);
    writeFileSync(path, reportB);
    console.log(`Report written to ${path}`);
  }
}

// Suite C
if (suite === "c" || suite === "all") {
  console.log(`Running eval suite C...\n`);
  const suiteCResults = await runSuiteC();
  const hits = suiteCResults.filter((r) => r.isHit).length;
  console.log(`\nCoverage: ${hits}/${suiteCResults.length} (${(hits / suiteCResults.length * 100).toFixed(0)}%)`);
  const reportC = generateSuiteCReport(suiteCResults);
  reports.push(reportC);
  if (suite === "c") {
    const path = resolve(EVALS_DIR, `${dateStr}-suite-c-report.md`);
    writeFileSync(path, reportC);
    console.log(`Report written to ${path}`);
  }
}

// Combined report for --suite all
if (suite === "all") {
  const combined = reports.join("\n\n---\n\n");
  const path = resolve(EVALS_DIR, `${dateStr}-eval-report.md`);
  writeFileSync(path, combined);
  console.log(`Combined report written to ${path}`);
}
