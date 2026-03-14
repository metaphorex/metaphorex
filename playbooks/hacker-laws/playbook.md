---
project_issue: 1225
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Hacker Laws -- Software Engineering Principles and Named Laws

## Source Description

**dwmkerr/hacker-laws** is a curated, community-contributed GitHub repository
cataloging 60+ laws, theories, principles, and patterns relevant to software
engineering and technology. Maintained by Dave Kerr, it is one of the most
popular repositories of its kind (~25k stars). The content is structured as a
single large README.md with H3 headings for each entry, organized into "Laws"
and "Principles" sections.

The repository is openly licensed and well-structured Markdown, making it an
ideal archive source for deterministic extraction.

## Access Method

**Primary archive:** The canonical source is the repository's README.md,
fetchable via the GitHub raw content API:

- Repository: https://github.com/dwmkerr/hacker-laws
- Raw README: https://raw.githubusercontent.com/dwmkerr/hacker-laws/master/README.md

**Extraction script:** `scripts/extract_entries.py` parses all H3 headings
from the README, extracts the entry name, key quote (first blockquote),
reference URL, and body preview. It filters out structural headings
(Introduction, Reading List, etc.) and SOLID sub-principles.

The script can run against the live GitHub URL or a local copy:

```bash
python3 scripts/extract_entries.py                           # fetch from GitHub
python3 scripts/extract_entries.py --local /path/to/README.md  # local file
```

**Secondary sources consulted but not scraped:**

- Tom Van Vleck's "Software Engineering Proverbs" (multicians.org)
- Matthew Reinbold's "Technology Aphorisms"
- Wikipedia articles for individual laws (linked from each entry)

## Extraction Strategy

The archive contains 62 distinct entries after filtering structural headings
and SOLID sub-principles. Of these, 21 were selected as candidates based on
the selectivity criteria from the import issue:

**Selection criteria applied:**

1. **Genuine structural metaphor**: Does the law encode a source-to-target
   mapping that transfers insight across domains? Mathematical formulas
   (Amdahl's Law), empirical trends (Moore's Law, Koomey's Law), and UI
   ergonomic rules (Fitts' Law) do not qualify.

2. **Cross-domain portability**: Has the law migrated beyond its origin
   domain? Goodhart's Law (economics to management to education to policy)
   passes. Wadler's Law (Haskell language design) does not.

3. **"Where It Breaks" depth**: Can you write a substantive "Where It Breaks"
   section? If the law is a one-liner observation with no structural tension,
   it is too thin. Murphy's Law and Wheaton's Law fail this test.

4. **Not already covered**: Bikeshedding (Law of Triviality) and Golden
   Hammer (Law of the Instrument) already exist in the catalog. The
   `sw-eng-vernacular` project covers software-specific jargon metaphors
   (technical debt, code smell, etc.) -- this project covers named laws and
   principles that are structurally distinct from those.

**Entries rejected (41 of 62):**

| Entry | Reason |
|-------|--------|
| 90-9-1 Principle | Statistical observation, no metaphorical structure |
| 90-90 Rule | Wry restatement of Pareto, too thin |
| Amdahl's Law | Mathematical formula, not a metaphor |
| CAP Theorem | Formal constraint triangle, no metaphor |
| Clarke's Laws | Aphorisms without structural mapping |
| Cunningham's Law | Social observation, no source-target transfer |
| Fitts' Law | Ergonomic formula |
| Hutber's Law | Observation without metaphorical structure |
| IPO Model | Architectural pattern, too generic |
| Koomey's Law | Empirical trend |
| Linus's Law | Observation about crowdsourcing |
| Metcalfe's Law | Mathematical relationship |
| Moore's Law | Empirical trend |
| Murphy's Law | Folk wisdom, "Where It Breaks" would be trivial |
| Occam's Razor | Well-known philosophical principle, very thin as mapping |
| Premature Optimization | Knuth quote, design principle not metaphor |
| Putt's Law | Observation about hierarchies, thin |
| Reed's Law | Mathematical relationship |
| Bitter Lesson | Empirical AI observation |
| Ringelmann Effect | Social psychology finding without metaphorical depth |
| Law of Demeter | Coding guideline, thin metaphor |
| Law of the Instrument | Already covered by `golden-hammer` |
| Law of Triviality | Already covered by `bikeshedding` |
| Scout Rule | Thin camping metaphor |
| Spotify Model | Organizational pattern, not metaphor |
| Two Pizza Rule | Thin heuristic |
| Twyman's Law | Statistical observation |
| Wadler's Law | Domain-specific variant of Law of Triviality |
| Wheaton's Law | Ethical principle, no structure |
| All Models Are Wrong | Epistemological observation, thin |
| Kerckhoffs's Principle | Security principle, no metaphor |
| Dilbert Principle | Cynical variant of Peter Principle (included) |
| Pareto Principle | Statistical pattern, not a metaphor |
| Stochastic Parrot | AI-specific, thin as standalone mapping |
| SOLID (all 5) | Design principles, not metaphors |
| DRY | Design principle |
| KISS | Design principle |
| YAGNI | Design principle |
| Principle of Least Astonishment | Design principle |
| Hick's Law | Ergonomic formula |
| Robustness Principle | Included as Postel's Law (different slug) |

## Schema Mapping

Each hacker-laws entry maps to the Metaphorex schema as follows:

| Hacker-Laws field | Metaphorex field | Notes |
|-------------------|-----------------|-------|
| H3 heading | `name` | Cleaned of Markdown links |
| Heading slug | `slug` | kebab-cased, e.g. `conways-law` |
| First blockquote | Feeds "What It Brings" | The canonical statement |
| Body text | Feeds "What It Brings" | Context and examples |
| Wikipedia/ref link | `related` / References | External context |
| See Also links | `related` field | Cross-references within catalog |

**Kind assignment:**
- Laws that map structure between two distinct domains: `cross-field-mapping`
- Laws that use one domain's logic to illuminate another: `conceptual-metaphor`

**Frame assignment:**
- `source_frame`: The domain the law originates from (economics, physics,
  biology, organizational behavior)
- `target_frame`: The domain the law illuminates when applied (software,
  organizations, decision-making)

**Author:** All entries use `author: agent:metaphorex-miner` since the
Miner agent will write the actual mapping content.

## Gotchas

1. **Overlap with `sw-eng-vernacular` project (issue #2):** That project
   covers software engineering *jargon metaphors* (technical debt, code smell,
   spaghetti code). This project covers *named laws and principles*. The
   distinction is clear but the Peter Principle appears in both -- this
   manifest uses `peter-principle` (the general form), while sw-eng-vernacular
   has `software-peter-principle` (the software-specific variant). The Miner
   should note the relationship in the `related` field.

2. **Existing catalog entries:** `bikeshedding` and `golden-hammer` already
   exist and cover the same ground as Law of Triviality and Law of the
   Instrument. These are excluded from this manifest.

3. **Source frames vary widely:** These laws come from economics, physics,
   biology, psychology, military history, and organizational theory. Each
   mapping needs its source frame researched independently. The hacker-laws
   descriptions are software-centric summaries, but the Miner should trace
   each law back to its original domain.

4. **Candidate count (21) is well under the 100 sub-issue cap.** No overflow
   handling needed.

5. **Some laws are pairs or families:** Hyrum's Law and Leaky Abstractions
   are closely related (both about interface/abstraction failures). Peter
   Principle and Dilbert Principle are related (only Peter Principle is
   included). Amara's Law and the Hype Cycle are combined into one entry.
   The Miner should use the `related` field to link these.

6. **Postel's Law tension with Hyrum's Law:** These two laws are in direct
   tension -- Postel says be liberal in what you accept, Hyrum says every
   observable behavior becomes a contract. The Miner should cross-reference
   them and note the tension in "Where It Breaks."
