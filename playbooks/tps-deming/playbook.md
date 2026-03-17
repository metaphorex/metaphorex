---
project_issue: 1233
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Playbook: Toyota Production System Glossary + Deming's 14 Points

## Source Description

Two tightly coupled sources from the quality management / lean manufacturing
tradition:

1. **Toyota Production System (TPS)** -- the manufacturing methodology
   developed at Toyota by Taiichi Ohno and Shigeo Shingo from the 1950s
   onward. TPS uses Japanese terminology that has migrated massively into
   software engineering, healthcare, government, and general management.

2. **W. Edwards Deming's 14 Points for Management** -- the philosophical
   foundation of quality management, first published in *Out of the Crisis*
   (1986). Deming taught statistical quality control to Japanese industry
   in the 1950s and directly influenced TPS. His work includes the PDCA
   cycle (originally Shewhart's), the System of Profound Knowledge, and
   numerous aphorisms that encode systems-thinking principles.

These sources are combined in one project because they share a common
intellectual lineage (Shewhart -> Deming -> Ohno/Shingo -> TPS) and their
concepts cross-reference heavily.

### Relationship to Issue #1354

Issue #1354 ("Import project: Deming's 14 Points + Shewhart cycle") covers
the same Deming material. This playbook consolidates both issues. Deming
concepts (PDCA, 14 Points, System of Profound Knowledge, key aphorisms)
are included here. Issue #1354 should be closed as a duplicate or marked
as subsumed by this project.

## Access Method

### Primary Archives

**Toyota UK Magazine TPS Glossary**
- URL: https://mag.toyota.co.uk/toyota-production-system-glossary/
- Format: HTML article with bold-tagged terms and inline definitions
- Coverage: 15 core TPS terms with descriptions
- Scraping script: `scripts/extract_tps_glossary.py` (BeautifulSoup)

**LeanProduction.com Lean Glossary**
- URL: https://www.leanproduction.com/lean-glossary/
- Format: HTML with H2 headings per term, paragraph definitions
- Coverage: 29 lean manufacturing terms with definitions
- Scraping script: `scripts/extract_tps_glossary.py` (BeautifulSoup)

**Lean Enterprise Institute Lexicon**
- URL: https://www.lean.org/explore-lean/lexicon-terms/
- Format: HTML directory listing with 169 linked terms
- Coverage: Most comprehensive enumeration; individual term pages at
  `https://www.lean.org/lexicon-terms/<term>/`
- Scraping script: `scripts/extract_tps_glossary.py` (BeautifulSoup)

**Deming Institute -- 14 Points**
- URL: https://deming.org/explore/fourteen-points/
- URL: https://deming.org/wp-content/uploads/2020/06/One-Pager-14Points.pdf
- Format: JavaScript-rendered page (not scrapable) and PDF
- Coverage: All 14 points with full text
- Note: The deming.org site is JS-rendered and resists scraping. The 14
  Points text was obtained from the web search results and cross-referenced
  with the ASQ summary at https://asq.org/quality-resources/tqm/deming-points

**Deming Institute -- PDSA Cycle**
- URL: https://deming.org/explore/pdsa/
- Coverage: PDCA/PDSA cycle description and history

### Secondary Sources (not scraped, used for cross-reference)

- Ohno, T. *Toyota Production System: Beyond Large-Scale Production* (1988)
- Deming, W.E. *Out of the Crisis* (1986)
- Deming, W.E. *The New Economics for Industry, Government, Education* (1993)
- Shingo, S. *A Study of the Toyota Production System* (1989)
- Rother, M. *Toyota Kata* (2009)
- Wikipedia: "Toyota Production System," "Deming's 14 Points," "PDCA"

### Extraction Script

`scripts/extract_tps_glossary.py` fetches from all three lean glossary
archives and produces merged JSON with deduplicated terms. The script
extracted 193 raw terms. The manifest curates these to 31 candidates that
encode transferable reasoning patterns (per the issue's selectivity guidance).

```bash
uv run playbooks/tps-deming/scripts/extract_tps_glossary.py
```

## Extraction Strategy

### Selectivity Criteria

The raw archives contain ~193 lean manufacturing terms. Most are pure
manufacturing vocabulary (e.g., "changeover," "cycle time," "finished
goods") that do not encode transferable reasoning patterns. The manifest
includes only terms that meet at least one of these criteria:

1. **Metaphorical depth** -- the term encodes a structural insight that
   transfers beyond manufacturing (e.g., "kanban" as pull-based flow,
   "poka-yoke" as error-proofing through design)
2. **Cross-domain migration** -- the concept has been adopted in software,
   healthcare, education, or management with structural parallels intact
3. **Philosophical weight** -- the term encodes a management philosophy
   or epistemological principle (e.g., "genchi genbutsu" as radical
   empiricism, "drive out fear" as prerequisite for quality)

Terms excluded as manufacturing-specific vocabulary: changeover, cycle time,
finished goods, raw materials, work-in-process, shipping stock, setup
reduction, line control, bottleneck analysis, OEE, TPM, SMED, KPIs, SMART
goals, six sigma, drum-buffer-rope, red tagging, and similar.

### For Miners

Each candidate in the manifest has:
- `slug`: filename for `catalog/entries/{slug}.md`
- `name`: the term as commonly written
- `kind`: `paradigm`, `mental-model`, or `metaphor`
- `source_frame` and `target_frame`: existing or needed frames
- `source`: `archive` (from scraping script) or `llm` (gap-fill)
- `description`: brief note on what makes this entry distinctive

**Miner workflow:**

1. For each candidate, fetch the LEI lexicon page at
   `https://www.lean.org/lexicon-terms/<slug>/` for the official definition
   and cross-references
2. Research the term's origin (which Toyota figure, what era, what problem
   it solved)
3. Identify migration paths: where has this concept been adopted outside
   manufacturing? (software, healthcare, management, education)
4. Write Transfers section emphasizing the structural insight, not just the
   manufacturing practice
5. Write Limits section: where does the manufacturing origin mislead when
   applied to other domains?
6. Set `related:` to link within this project's entries and to existing
   catalog entries (especially `activation-energy`, `fear-driven-development`)

### Batching Recommendation

Process in thematic clusters:

- **Batch 1 -- TPS Pillars (4):** jidoka, just-in-time, andon, poka-yoke.
  These form the structural core and should be mined first for calibration.
- **Batch 2 -- Flow and Waste (6):** kanban, heijunka, muda-mura-muri,
  continuous-flow, value-stream, takt-time. Flow concepts that share the
  fluid-dynamics metaphor.
- **Batch 3 -- Observation and Reflection (4):** gemba, genchi-genbutsu,
  hansei, obeya. Epistemological concepts about how organizations learn.
- **Batch 4 -- Improvement Methods (5):** kaizen, kaikaku, kata, five-whys,
  standardized-work, yokoten. How improvement happens and spreads.
- **Batch 5 -- Organization and Strategy (2):** hoshin-kanri, nemawashi.
  How decisions are made and deployed.
- **Batch 6 -- Deming Points (7):** pdca-cycle, constancy-of-purpose,
  drive-out-fear, cease-dependence-on-inspection, break-down-barriers,
  eliminate-slogans, eliminate-numerical-quotas, pride-of-workmanship.
- **Batch 7 -- Deming Philosophy (2):** system-of-profound-knowledge,
  a-bad-system-beats-a-good-person. LLM-sourced; verify against Deming texts.

## Schema Mapping

### Kind Assignment

| Category | Kind | Count | Criteria |
|----------|------|-------|----------|
| Systems/practices | `paradigm` | 10 | Complete methodology or practice system |
| Principles/insights | `mental-model` | 19 | Specific reasoning pattern or diagnostic |
| Structural metaphors | `metaphor` | 2 | Explicit source-target mapping (value-stream, continuous-flow) |

Most TPS concepts are `paradigm` (a complete practice system) or
`mental-model` (a specific reasoning pattern). Only `value-stream` and
`continuous-flow` are pure `metaphor` (they map fluid dynamics onto
organizational processes).

### Frame Inventory

**Existing reusable frames (in catalog):**
- `manufacturing` -- source frame for most TPS concepts
- `organizational-behavior` -- target frame for most entries
- `fluid-dynamics` -- source for value-stream, continuous-flow
- `architecture-and-building` -- source for break-down-barriers
- `horticulture` -- source for nemawashi (root preparation)
- `measurement` -- source for eliminate-numerical-quotas
- `psychology` -- secondary category for fear/motivation entries

**New frames potentially needed:**
- None. Existing frames cover all candidates.

### Categories

Primary categories by cluster:
- All TPS entries: `systems-thinking`
- Software-migrated concepts: `software-engineering` (secondary)
- Deming organizational points: `organizational-behavior`
- Psychological concepts: `psychology` (secondary)

## Gotchas

1. **Overlap with #1354.** Issue #1354 covers Deming's 14 Points as a
   separate project. This playbook consolidates both. The Surveyor should
   close #1354 as subsumed or link it as a companion issue.

2. **Japanese terminology.** Many terms are Japanese words (kaizen, kanban,
   gemba, etc.). Miners should include the literal Japanese meaning in the
   entry body (e.g., "kanban" = "signboard") as it often illuminates the
   metaphorical structure.

3. **Deming vs. Shewhart attribution.** The PDCA cycle was developed by
   Shewhart, popularized by Deming, and modified by Japanese engineers.
   Deming himself preferred PDSA (Plan-Do-Study-Act). Miners should
   document the attribution chain accurately.

4. **Not all 14 Points are individual entries.** Deming's 14 Points are
   numbered but some encode the same insight (e.g., Points 6, 13 on
   training/education). The manifest selects 7 of the 14 that encode
   distinct, transferable reasoning patterns. Points omitted as
   manufacturing-specific or redundant: 2 (adopt new philosophy), 4
   (end lowest-bidder purchasing), 5 (improve constantly -- subsumed by
   kaizen), 6 (institute training), 7 (institute leadership), 13
   (education program), 14 (transform the company).

5. **The TPS House metaphor.** TPS is commonly depicted as a house with
   two pillars (JIT and jidoka), a foundation (heijunka, standardized
   work, kaizen), and a roof (customer satisfaction). This is itself a
   rich architectural metaphor. Miners working on jidoka and just-in-time
   should reference the house structure.

6. **Gemba vs. genchi genbutsu.** These are closely related but distinct.
   Gemba is the place; genchi genbutsu is the practice of going there.
   Some sources conflate them. Miners should keep them separate and use
   `related:` links.

7. **LLM-sourced entries.** Two entries are LLM-sourced (system-of-profound-
   knowledge, a-bad-system-beats-a-good-person). These are well-established
   Deming concepts but were not found in the scraped glossary archives.
   The Surveyor should verify they meet the metaphorical depth threshold.

8. **31 candidates is well under the 100 sub-issue cap.** No overflow
   handling needed.
