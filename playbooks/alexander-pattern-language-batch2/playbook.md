---
project_issue: 2189
parent_issue: 1350
repo: metaphorex/metaphorex
source_type: book
status: draft
---

# Alexander Pattern Language -- Batch 2

## Source Description

Christopher Alexander's **A Pattern Language** (1977) -- 253 named design
patterns organized as a generative grammar for built environments. This is
batch 2, an overflow from the parent project (#1350) which hit the GitHub
100 sub-issue cap.

Batch 2 covers 21 patterns from the interior/construction scale of the
book (patterns #168-#253), focused on room-level, material, and detail
patterns that carry strong metaphorical transfers to software engineering,
organizational design, and creative work.

The parent project (#1350) handles patterns at larger scales (town, building
complex, room arrangement). There is no overlap between batches -- each
candidate appears in exactly one batch.

## Access Method

### Primary archive: patternlanguage.cc

The site https://patternlanguage.cc/ hosts structured summaries of all 253
patterns with problem statements, solutions, and cross-references. Each
pattern has a stable URL of the form:

    https://patternlanguage.cc/Patterns/{Name}-({Number})

Example: https://patternlanguage.cc/Patterns/Alcoves-(179)

### Secondary archive: patternlanguage.com

Alexander's own site https://www.patternlanguage.com/ hosts sample pattern
pages with original text excerpts (e.g., pattern #221).

### Scraping script

`scripts/fetch_patterns.py` fetches all 21 batch 2 pattern pages from
patternlanguage.cc, extracts the problem statement / summary blockquote,
and outputs structured JSON. Run with:

```bash
uv run playbooks/alexander-pattern-language-batch2/scripts/fetch_patterns.py
```

Output goes to stdout (JSON array). The script is idempotent.

### Book reference

Alexander, C., Ishikawa, S. & Silverstein, M. *A Pattern Language: Towns,
Buildings, Construction* (Oxford University Press, 1977). The Miner should
use the pattern number, name, and summary from the archive, supplemented
by LLM knowledge of the full pattern text.

## Extraction Strategy

Each of the 21 patterns becomes one catalog entry. The Miner should:

1. **Read the pattern summary** from the archive (or the fetch script
   output) to understand the architectural problem and solution.

2. **Identify the metaphorical transfer.** The question is not "what is
   this pattern?" but "what does this pattern illuminate when applied to
   software, organizations, or creative work?" Most patterns carry a
   structural insight about boundaries, scale, visibility, or human
   comfort that transfers powerfully.

3. **Write Transfers** that articulate the structural parallels. Use the
   `[source]` prefix format for frontmatter transfer items. The body
   section should expand with specific examples from software engineering,
   organizational behavior, or creative process.

4. **Write Limits** that identify where the metaphor breaks. This is the
   highest-value section. Common break patterns for Alexander metaphors:
   - Physical constraints that don't exist in software (walls can't grow)
   - Sensory affordances that have no digital equivalent
   - Assumptions of stability that software's mutability undermines
   - Scale differences between rooms and codebases

5. **Write Expressions** -- actual phrases in developer/org discourse that
   invoke the pattern's logic, whether or not they cite Alexander.

6. **Set `provenance: alexander-pattern-language`** in the frontmatter to
   link back to this project.

### Prioritization

The 9 unmined patterns should be worked in order of metaphorical richness:

**High priority** (strongest cross-domain transfers):
- sitting-circle (#185) -- meeting design, team topologies
- ceiling-height-variety (#190) -- varying abstraction levels
- good-materials (#207) -- technology choice and technical debt
- filtered-light (#238) -- abstraction layers, curated views
- pools-of-light (#252) -- focused attention in interfaces
- things-from-your-life (#253) -- personalization, dotfiles

**Medium priority:**
- natural-doors-and-windows (#221) -- API surface design
- ornament (#249) -- code aesthetics, expressive programming
- different-chairs (#251) -- tool diversity, one-size-fits-none

### Already mined (12 of 21)

The following entries already exist in the catalog:
- connection-to-the-earth (#168)
- garden-growing-wild (#172)
- alcoves (#179)
- window-place (#180)
- workspace-enclosure (#183)
- windows-overlooking-life (#192)
- thick-walls (#197)
- secret-place (#204)
- structure-follows-social-spaces (#205)
- gradual-stiffening (#208)
- deep-reveals (#223)
- small-panes (#239)

## Schema Mapping

### Frames

All entries use `architecture-and-building` as the source frame. This frame
already exists in the catalog.

Target frames vary by entry but default to `software-abstraction`. Entries
with strong organizational mapping should also list `organizational-behavior`
in `applies_to`.

### Categories

Primary: `software-engineering`
Secondary (where applicable): `systems-thinking`, `organizational-behavior`

### Kind

Most entries are `pattern` (they describe a named problem/solution structure
that carries metaphorical weight). The `deep-reveals` entry uses `metaphor`
because the name itself is the metaphorical vehicle rather than the pattern
structure.

Use `pattern` as the default kind for batch 2 entries.

### Frontmatter template

```yaml
slug: <slug>
name: <Name>
kind: pattern
source_frame: architecture-and-building
applies_to:
  - software-abstraction
categories:
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related: []
provenance: alexander-pattern-language
created: '<today>'
updated: '<today>'
grounding: established
harness: Claude Code
transfers:
  - '[source] ...'
limits:
  - '[source] ...'
```

### Related entries

Cross-reference liberally within the Alexander set. Existing entries that
are good `related` targets:
- `a-place-to-wait` (pattern #150, batch 1)
- `intimacy-gradient` (pattern #127, batch 1)
- `entrance-transition` (pattern #112, batch 1)
- `zen-view` (pattern #134, batch 1)
- `a-room-of-ones-own` (pattern #141, batch 1)
- `the-facade-pattern` (from design-patterns project)
- Other batch 2 entries that have already been mined

## Gotchas

1. **This is batch 2 of a larger project.** The parent issue (#1350) has
   100 sub-issues covering the first batch. Do not duplicate work that
   belongs to batch 1. The 21 candidates here are the overflow set.

2. **12 entries already exist.** Only 9 remain to be mined. Check the
   catalog before starting work on any candidate. Close the sub-issue if
   the entry already exists with adequate Transfers and Limits sections.

3. **Pattern vs. metaphor confusion.** The entry is about the metaphorical
   structure of the pattern, not a tutorial on the pattern itself. The
   Miner should resist writing an architecture lesson. The question is
   always: what does this pattern reveal when applied outside architecture?

4. **Alexander's patterns are deeply interconnected.** Each pattern
   references others. The Miner should note these cross-references in the
   `related` field but should not feel obligated to create entries for
   referenced patterns that are not in the candidate list.

5. **Construction-scale patterns (#206-253) are more concrete.** Patterns
   like "Good Materials" and "Gradual Stiffening" deal with physical
   construction details. The metaphorical transfer to software is less
   obvious but often more interesting -- the Miner should look for the
   structural insight, not force a surface analogy.

6. **Sub-issues already exist.** All 21 sub-issues have been created under
   #2189. The Miner should work from the sub-issue list rather than
   creating new issues.
