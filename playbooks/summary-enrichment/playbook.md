---
project_issue: TBD
repo: metaphorex/metaphorex
source_type: corpus
status: active
---

# Summary Enrichment — One-sentence entry explainers

## Source Description

The source is the existing Metaphorex catalog (~1,241 entries). The goal is to
add a `summary` field to every entry's frontmatter: one punchy sentence (max
150 characters) that explains the metaphor to someone who doesn't recognize
the name.

## Access Method

The tiering and context extraction scripts produce the working data:

```bash
# Classify entries by difficulty
bun run scripts/tier-entries.ts > playbooks/summary-enrichment/tier-assignments.json

# Extract minimal context for generation
bun run scripts/extract-summary-context.ts \
  playbooks/summary-enrichment/tier-assignments.json \
  > playbooks/summary-enrichment/context.jsonl
```

## Tier Definitions

| Tier | Description | Model | Batch size | ~Count |
|------|-------------|-------|-----------|--------|
| 1 | Name is self-explanatory (bottleneck, trojan-horse, scapegoat) | Sonnet | 100 | ~400 |
| 2 | Name is suggestive but needs context (dead-zone, pendulation) | Opus | 50 | ~500 |
| 3 | Name is opaque or domain-specific (cognitive-defusion, lampshading) | Opus | 30 | ~300 |

## Style Guide

**Voice:** Clear and direct. Every sentence carries structural information.
The reader should think "oh, that's what that is."

**Constraints:**
- Max 150 characters
- No em dashes (U+2014). Use comma, period, or colon instead
- Not a dictionary definition
- Not a restatement of the first transfer proposition
- May use a second short sentence or phrase fragment
- Must stand alone without reading the rest of the entry

**Anti-patterns:**
- "This metaphor maps X to Y" (mechanical)
- "A concept from [domain] that..." (encyclopedic)
- Starting with "The idea that..." (passive)
- Restating the name as a sentence (circular)
- Smug kicker sentences ("Nobody asks who...", "The opacity was the point")
- Editorial gotchas that comment on the metaphor's irony instead of explaining it
- Punchlines that sacrifice information for cleverness

**Tone rule:** If the second sentence doesn't add structural information, cut
it. Be direct and earned, not performative. State the insight and stop.

## Golden Examples

These are injected as few-shot examples into every generation prompt.
Quality here sets the ceiling for the entire sweep.

### Tier 1 (self-explanatory names)

1. **Bottleneck**: "A system's throughput is limited by its narrowest point. Widening the neck is the only way to improve it."
2. **Bug**: "Defects are framed as creatures that invaded the code. The framing hides that they were authored in, not smuggled in."
3. **Bus Factor**: "How many people can vanish before the project dies. The number measures knowledge concentration, not headcount."
4. **Achilles Heel**: "One hidden weak point can negate all other strength. The more invulnerable the system, the more catastrophic the single failure."
5. **Bikeshedding**: "A committee approves a reactor in minutes and debates the bike shed for hours. Accessibility breeds opinions."

### Tier 2 (suggestive names)

1. **Triage**: "Sort by who can still be saved, not by who's loudest. Accept that some cases get deliberately abandoned."
2. **Dead Zone**: "A system degraded past the point where normal recovery works. Feedback loops that once healed now accelerate collapse."
3. **Facade**: "One clean interface hiding a mess of wiring behind it. The simplicity is real for the caller, fake for the maintainer."
4. **Lava Flow**: "Code nobody dares touch because nobody remembers why it's there. It hardened in place and now it's load-bearing."
5. **Containment**: "The therapist receives unbearable feelings without breaking. The container frame captures holding but understates the work of transformation."

### Tier 3 (opaque/domain-specific)

1. **Pendulation**: "Healing isn't linear. Swing between safety and distress until the amplitude dampens on its own."
2. **Lampshading**: "Call out the awkward thing before the audience does. Naming the flaw preempts the criticism."
3. **Cognitive Defusion**: "Your thoughts are weather, not climate. Observe them passing instead of obeying them."
4. **The Line**: "In a restaurant kitchen, the line is where raw becomes plated. Every station in sequence, no skipping."
5. **A Room of One's Own**: "Creative work requires material conditions. No space, no lock on the door, no art."

## Extraction Strategy

Use the `/enrich-summary` command. It reads `context.jsonl`, processes a batch
of entries for a given tier, generates summaries, inserts them into frontmatter,
validates, and opens a PR.

```bash
# Example: process next batch of Tier 1
/enrich-summary --tier 1

# Example: process specific slugs
/enrich-summary bottleneck trojan-horse scapegoat
```

## Git Workflow

- Branch: `enrich/summary-t{tier}-batch-{N}`
- Label: `needs-smelting`
- PR body includes 5 sample summaries for spot-checking
- Each PR closes its corresponding batch sub-issue (if using sub-issues)

## Progress

| Tier | Total | Done | Remaining |
|------|-------|------|-----------|
| 1 | TBD | 0 | TBD |
| 2 | TBD | 0 | TBD |
| 3 | TBD | 0 | TBD |

Update this table as batches merge.

## Quality Checks

Before opening a PR, verify:
- [ ] All summaries <= 150 characters
- [ ] No em dashes
- [ ] No "This metaphor..." or "A concept that..." openers
- [ ] Tone matches golden examples
- [ ] Summaries for non-obvious names are independently meaningful
- [ ] `uv run scripts/validate.py validate` passes clean
