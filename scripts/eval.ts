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
  maxTokens: number = 2000,
): Promise<string> {
  const client = getOpenRouterClient();
  const response = await client.chat.completions.create({
    model,
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: userPrompt },
    ],
    max_tokens: maxTokens,
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

const SYSTEM_PROMPT_RAW = `You are an expert in conceptual metaphor theory (Lakoff & Johnson). You understand that metaphors are not just linguistic decoration — they are cognitive structures that shape how we reason about abstract concepts by mapping them onto concrete source domains.

When analyzing a scenario, look for:
- The source domains being invoked (war, journey, container, machine, organism, etc.)
- Structural mappings: what relations from the source domain are being projected onto the target
- Entailments: what the metaphor makes you expect that may not be true
- Hidden assumptions: what alternative framings are being crowded out
- Dead metaphors: terms so conventional that their metaphorical origin is invisible

For each metaphor you identify:
1. Name it in CONCEPTUAL METAPHOR format (e.g., "ARGUMENT IS WAR")
2. Explain what structural assumptions it carries — what does the source domain make you expect?
3. Identify where it misleads — what does the metaphor make hard to see or think?

Be merciless. Focus on non-obvious metaphors, not surface-level ones. Identify at least 7 metaphors, including at least 2 that most people would miss.`;

const SYSTEM_PROMPT_WITH_M4X = `You are an expert in conceptual metaphor theory (Lakoff & Johnson). You understand that metaphors are not just linguistic decoration — they are cognitive structures that shape how we reason about abstract concepts by mapping them onto concrete source domains.

You have access to results from a curated metaphor catalog search. Use these results as a starting point — they may surface metaphors you wouldn't think of on your own. But also identify metaphors the search may have missed.

When analyzing a scenario, look for:
- The source domains being invoked (war, journey, container, machine, organism, etc.)
- Structural mappings: what relations from the source domain are being projected onto the target
- Entailments: what the metaphor makes you expect that may not be true
- Hidden assumptions: what alternative framings are being crowded out
- Dead metaphors: terms so conventional that their metaphorical origin is invisible

For each metaphor you identify:
1. Name it in CONCEPTUAL METAPHOR format (e.g., "ARGUMENT IS WAR") and note if it came from the catalog search
2. Explain what structural assumptions it carries — what does the source domain make you expect?
3. Identify where it misleads — what does the metaphor make hard to see or think?

Be merciless. Focus on non-obvious metaphors, not surface-level ones. Identify at least 7 metaphors, including at least 2 that most people would miss.`;

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
// Suite D — LLM-as-judge (Opus reviews Suite B results)
// ---------------------------------------------------------------------------

const JUDGE_MODEL = "anthropic/claude-opus-4";

const JUDGE_SYSTEM_PROMPT = `You are a rigorous evaluator comparing two approaches to conceptual metaphor identification: a raw LLM approach (no tools) vs an LLM augmented with catalog search results (m4x).

For each scenario, you will see:
- The scenario description
- The catalog search results that were injected
- The raw LLM response
- The m4x-augmented LLM response

Evaluate BOTH responses on these dimensions (score each 1-5):

1. **Breadth** — How many distinct, genuinely relevant metaphors were identified? (Not just count — quality of coverage across different source domains)
2. **Depth** — How insightful are the "where it misleads" analyses? Are they specific and actionable, or generic platitudes?
3. **Novelty** — Did the response surface non-obvious metaphors that most analysts would miss? Dead metaphors? Competing frames?
4. **Precision** — Are the metaphors well-named and clearly articulated, or vague and overlapping?

Then provide:
- **Winner**: raw | m4x | tie
- **Key differentiator**: One sentence on what made the difference (or why it was a tie)
- **Novel metaphors not in catalog**: List EVERY metaphor identified by EITHER response that appears to be a genuinely useful conceptual metaphor NOT already captured in the catalog search results. For each, provide:
  - A suggested slug (kebab-case)
  - The source domain
  - A one-sentence description of what it maps
  - Which response generated it (raw, m4x, or both)

Format your response as structured markdown with clear headers.`;

interface JudgeResult {
  scenario: string;
  judgment: string;  // full Opus response
}

async function runSuiteD(suiteBResults: SuiteBResult[]): Promise<JudgeResult[]> {
  const results: JudgeResult[] = [];

  for (const b of suiteBResults) {
    process.stdout.write(`  judging ${b.name}... `);

    const userPrompt = `## Scenario: ${b.name}

**Description:** ${b.scenario}

### Catalog search results injected into m4x response:

${b.searchResultsSummary}

### Raw Claude response (no tools):

${b.rawResponse}

### Claude + m4x response (with catalog search):

${b.m4xResponse}`;

    const judgment = await chatCompletion(JUDGE_MODEL, JUDGE_SYSTEM_PROMPT, userPrompt);
    console.log("done");

    results.push({ scenario: b.name, judgment });
  }

  return results;
}

function generateSuiteDReport(results: JudgeResult[]): string {
  let md = `# Eval Report: Suite D — LLM Judge (Opus)\n\n`;
  md += `**Date:** ${new Date().toISOString()}\n`;
  md += `**Judge model:** ${JUDGE_MODEL}\n`;
  md += `**Subject model:** ${CLAUDE_MODEL}\n`;
  md += `**Scenarios judged:** ${results.length}\n\n`;

  for (const r of results) {
    md += `## ${r.scenario}\n\n`;
    md += r.judgment;
    md += `\n\n---\n\n`;
  }

  return md;
}

/** Extract novel metaphor candidates from judge responses for import ticket.
 *
 * Instead of fragile regex on the judge's markdown, we ask a second LLM call
 * to consolidate all novel candidates into a clean structured list.
 */
async function extractNovelCandidates(judgeResults: JudgeResult[]): Promise<string> {
  const allJudgments = judgeResults.map((r) =>
    `## ${r.scenario}\n\n${r.judgment}`
  ).join("\n\n---\n\n");

  const consolidationPrompt = `Below are Opus judge evaluations of 5 metaphor-analysis scenarios. Each evaluation includes a "Novel Metaphors Not in Catalog" section listing metaphors that were identified during analysis but don't exist in the Metaphorex catalog yet.

Your job: extract ALL novel metaphor candidates across ALL scenarios into a single consolidated list. For each candidate:
1. **slug** (kebab-case, suitable for a filename)
2. **name** (human-readable, "Source Is Target" format)
3. **source domain**
4. **one-sentence description** of what structural mapping it encodes
5. **scenario** where it was identified
6. **generated by** (raw, m4x, or both)

Deduplicate: if the same metaphor appears in multiple scenarios, merge into one entry noting all scenarios.

Exclude metaphors that are too generic (e.g., "understanding-is-vision" is already well-known in cognitive linguistics and likely in the catalog). Focus on metaphors specific enough to be genuinely useful catalog entries.

Format as a markdown checklist so the human curator can check/uncheck candidates.

## Judge evaluations:

${allJudgments}`;

  const consolidated = await chatCompletion(
    JUDGE_MODEL,
    "You are a meticulous editor consolidating evaluation results into a clean import list for a metaphor catalog.",
    consolidationPrompt,
    4000, // needs room for ~20-30 candidates with descriptions
  );

  const dateStr = new Date().toISOString().slice(0, 10);
  let body = `## Eval-driven curation: novel metaphor candidates\n\n`;
  body += `**Source:** Suite D judge analysis (${dateStr})\n`;
  body += `**Judge model:** ${JUDGE_MODEL}\n`;
  body += `**Subject model:** ${CLAUDE_MODEL}\n`;
  body += `**Scenarios analyzed:** ${judgeResults.length}\n\n`;
  body += `These metaphors were identified by Claude during scenario analysis but are not yet in the catalog. `;
  body += `Each was flagged by an Opus judge as genuinely useful. Human curation decides which to add.\n\n`;
  body += `---\n\n`;
  body += consolidated;
  body += `\n\n---\n\n`;
  body += `### Process\n\n`;
  body += `Auto-generated by \`bun run scripts/eval.ts --suite d --create-issue\`.\n\n`;
  body += `The eval-driven curation cycle:\n`;
  body += `1. Eval scenarios prompt Claude to identify metaphors\n`;
  body += `2. Opus judge flags candidates not in catalog\n`;
  body += `3. Consolidation pass deduplicates and filters\n`;
  body += `4. Human curator checks off candidates worth adding\n`;
  body += `5. Checked candidates become nugget issues for the Miner\n`;

  return body;
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
let createIssue = false;

for (let i = 0; i < args.length; i++) {
  if (args[i] === "--suite" && i + 1 < args.length) {
    suite = args[++i].toLowerCase();
  } else if (args[i] === "--create-issue") {
    createIssue = true;
  }
}

if (!["a", "b", "c", "d", "all"].includes(suite)) {
  console.error(`Unknown suite: ${suite}. Use --suite a|b|c|d|all`);
  console.error(`  --create-issue  Create GitHub issue with novel metaphor candidates (Suite D)`);
  process.exit(1);
}

mkdirSync(EVALS_DIR, { recursive: true });
const dateStr = new Date().toISOString().slice(0, 10);
const reports: string[] = [];

// Shared state — Suite D needs Suite B results
let storedSuiteBResults: SuiteBResult[] | null = null;

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
if (suite === "b" || suite === "d" || suite === "all") {
  console.log(`Running eval suite B...\n`);
  storedSuiteBResults = await runSuiteB();
  console.log(`\n${storedSuiteBResults.length} scenarios completed`);
  const reportB = generateSuiteBReport(storedSuiteBResults);
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

// Suite D — LLM judge (uses Suite B results)
if (suite === "d" || suite === "all") {
  console.log(`\nRunning eval suite D (Opus judge)...\n`);
  const suiteDResults = await runSuiteD(storedSuiteBResults!);
  console.log(`\n${suiteDResults.length} scenarios judged`);

  const reportD = generateSuiteDReport(suiteDResults);
  reports.push(reportD);

  const path = resolve(EVALS_DIR, `${dateStr}-suite-d-report.md`);
  writeFileSync(path, reportD);
  console.log(`Report written to ${path}`);

  // Create GitHub issue with novel metaphor candidates
  if (createIssue) {
    console.log(`\nConsolidating novel candidates (Opus call)...`);
    const issueBody = await extractNovelCandidates(suiteDResults);
    const title = `Eval-driven curation: novel metaphor candidates (${dateStr})`;

    console.log(`\nCreating GitHub issue...`);
    const proc = Bun.spawn(
      ["gh", "issue", "create",
        "--repo", "metaphorex/metaphorex",
        "--title", title,
        "--body", issueBody,
        "--label", "import-project",
        "--label", "eval-driven-curation",
      ],
      { stdout: "pipe", stderr: "pipe" }
    );
    const stdout = await new Response(proc.stdout).text();
    const stderr = await new Response(proc.stderr).text();
    await proc.exited;

    if (proc.exitCode === 0) {
      console.log(`Issue created: ${stdout.trim()}`);
    } else {
      console.error(`Failed to create issue: ${stderr}`);
    }
  }
}

// Combined report for --suite all
if (suite === "all") {
  const combined = reports.join("\n\n---\n\n");
  const path = resolve(EVALS_DIR, `${dateStr}-eval-report.md`);
  writeFileSync(path, combined);
  console.log(`Combined report written to ${path}`);
}
