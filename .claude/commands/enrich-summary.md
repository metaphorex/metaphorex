---
name: enrich-summary
description: Add summary field to catalog entries — tiered enrichment sweep
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent
model: sonnet
---

# Summary Enrichment Sweep

You are enriching Metaphorex catalog entries with a `summary` field: one
punchy sentence (max 150 characters) that explains the metaphor to someone
who doesn't recognize the name.

## Setup

1. Invoke the `agent-identity` skill before any git/gh commands
2. Read the playbook for style guide and golden examples:
   `playbooks/summary-enrichment/playbook.md`
3. Read the tier assignments and context:
   `playbooks/summary-enrichment/tier-assignments.json`
   `playbooks/summary-enrichment/context.jsonl`

## Batch Selection

$ARGUMENTS

If arguments specify a tier (`--tier 1`, `--tier 2`, `--tier 3`):
- Read the tier assignments JSON
- Find entries in that tier that don't yet have a `summary` field
- Pick the next batch (Tier 1: 100, Tier 2: 50, Tier 3: 30)

If arguments specify slugs, process those entries regardless of tier.

If no arguments, pick the next unenriched batch starting from Tier 1.

## Style Rules

**CRITICAL — read these before writing any summary:**

- Max 150 characters. Count them. If over, rewrite shorter.
- No em dashes (—). Use period, comma, or colon instead.
- Punchy and opinionated. Not encyclopedic.
- Not a restatement of the first transfer proposition.
- Not a dictionary definition ("X is a concept where...").
- Do NOT start with "This metaphor...", "A concept that...", "The idea that..."
- The reader should think "oh, that's what that is."
- May use a second short sentence or phrase fragment if needed.
- Match the voice of the golden examples in the playbook.

## Golden Examples (always reference these)

**Tier 1:**
- Bottleneck: "A system's throughput is limited by its narrowest point. Widening the neck is the only way to improve it."
- Sunk Cost: "Money already spent shouldn't influence what you do next. But it always does."
- Phoenix: "Total destruction is the prerequisite for rebirth. The fire is the feature, not the failure."

**Tier 2:**
- Triage: "Sort by who can still be saved, not by who's loudest. Accept that some cases get deliberately abandoned."
- Lava Flow: "Code nobody dares touch because nobody remembers why it's there. It hardened in place and now it's load-bearing."

**Tier 3:**
- Pendulation: "Healing isn't linear. Swing between safety and distress until the amplitude dampens on its own."
- Cognitive Defusion: "Your thoughts are weather, not climate. Observe them passing instead of obeying them."

## Enrichment Process

For each entry in the batch:

1. **Read context** from `context.jsonl` (filtered to current batch)
2. **Read the entry file** to understand the full picture
3. **Write the summary** following the style rules above
4. **Verify length**: must be <= 150 characters. If over, rewrite.
5. **Verify no em dash**: check for U+2014. If present, replace.
6. **Insert `summary:` into frontmatter** — place it after `name:`, before `kind:`.
   Use double-quoted YAML string. Example:
   ```yaml
   name: Bottleneck
   summary: "A system's throughput is limited by its narrowest point. Widening the neck is the only way to improve it."
   kind: metaphor
   ```
7. **Skip entries that already have a `summary` field**

### YAML Quoting

Always use double-quoted strings for summaries. If the summary contains
double quotes, escape them with backslash. If it contains apostrophes,
they're fine inside double quotes.

```yaml
summary: "Sort by who can still be saved, not by who's loudest."
```

## Validate

After enriching the batch:

```bash
uv run scripts/validate.py validate
```

Fix any errors. The validator checks summary length (<=150) and em dash.

## Commit and PR

Branch: `enrich/summary-t{tier}-batch-{N}`

```bash
git checkout -b enrich/summary-t{tier}-batch-{N}
git add catalog/entries/
git commit -m "Enrich: summary batch T{tier}.{N} (M entries)"
```

Open a PR labeled `needs-smelting`:

```bash
gh pr create \
  --title "Enrich: summary batch T{tier}.{N} (M entries)" \
  --label needs-smelting \
  --body "Adds summary field to M entries (Tier {tier}, batch {N}).

## Sample summaries

$(head -5 of the batch's summaries, formatted as a list)

Part of the summary enrichment sweep.
See: playbooks/summary-enrichment/playbook.md"
```

## Batch Size Guidance

- Tier 1 (self-explanatory): 100 entries per batch
- Tier 2 (needs context): 50 entries per batch
- Tier 3 (opaque/domain): 30 entries per batch

## Quality Checks

Before opening the PR, spot-check 5 entries from the batch:
- Is the summary independently meaningful without reading the entry?
- Does it match the tone of the golden examples?
- Is it <= 150 characters?
- Does it avoid the anti-patterns (mechanical, encyclopedic, circular)?
- For non-obvious names: would a newcomer understand what this entry is about?
