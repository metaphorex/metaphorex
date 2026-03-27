---
project_issue: 1350
repo: metaphorex/metaphorex
source_type: book
status: draft
---

# Alexander's Pattern Language -- Import Playbook

## Source Description

Christopher Alexander, Sara Ishikawa, Murray Silverstein et al.
*A Pattern Language: Towns, Buildings, Construction* (Oxford University
Press, 1977). 253 numbered design patterns organized as a generative
grammar for built environments, descending from regional scale (#1
Independent Regions) to construction detail (#253 Things From Your Life).

Each pattern follows a structured format: name, confidence rating (0-2
stars), context (which larger patterns contain it), problem statement,
discussion with examples, solution statement, and references to smaller
patterns it contains. The patterns form a directed graph (a "language")
where each pattern connects to both higher-level and lower-level patterns.

This is the origin of "pattern language" as a concept. Kent Beck and Ward
Cunningham adapted the idea for software in 1987, leading to the Gang of
Four's *Design Patterns* (1994) and Ward Cunningham's invention of the wiki
(WikiWikiWeb) to collaboratively document software patterns.

## Access Method

**Primary archive**: [patternlanguage.cc](https://patternlanguage.cc/) --
a community site with the complete list of all 253 patterns, names, and
links to individual pattern pages.

**Secondary archives**:
- [Clayton Dorge's pattern list](https://claytondorge.com/patterns-list) --
  complete numbered list with brief descriptions
- [Wikipedia: A Pattern Language](https://en.wikipedia.org/wiki/A_Pattern_Language) --
  structured overview with section breakdown
- [patternlanguage.com](https://www.patternlanguage.com/) -- Alexander's
  own site (limited free content)
- [Pattern Language Index](https://www.patternlanguageindex.com/) --
  interactive pattern relationship mapping

**Scraping script**: `scripts/scrape_patterns.py` fetches the pattern list
from patternlanguage.cc. Falls back to a hardcoded canonical list of all
253 patterns if scraping fails (the site uses JavaScript rendering). The
canonical list was verified against patternlanguage.cc and Clayton Dorge's
list.

**Primary source**: The book itself (1171 pages). Pattern names, numbers,
and structural relationships are well-documented in the archives above.
Detailed content (problem statements, discussion, solution statements)
requires the book.

## Extraction Strategy

Not all 253 patterns are metaphorically interesting for Metaphorex. The
issue estimates ~30-50 mappings. After systematic review, the manifest
contains **62 new candidates** (plus 8 already in the catalog), for a total
of **70 patterns** that function as metaphors when applied beyond
architecture.

**Selection criteria for inclusion:**

1. The pattern name or concept has demonstrably migrated to software
   engineering, organizational design, UX design, or another field
2. The pattern encodes a structural insight that transfers across domains
   (not just a construction technique)
3. The architectural concept illuminates something about its target domain
   that would be harder to see without the metaphor

**Excluded patterns** (the remaining ~183):
- Pure construction technique with no metaphorical legs (e.g., #215 Ground
  Floor Slab, #216 Box Columns, #217 Perimeter Beams)
- Patterns too specific to residential architecture (e.g., #187 Marriage
  Bed, #143 Bed Cluster, #144 Bathing Room)
- Urban planning patterns with no clear cross-domain mapping (e.g., #2 The
  Distribution of Towns, #23 Parallel Roads, #50 T Junctions)
- Patterns whose metaphorical content is already captured by a more
  prominent pattern in the list

**Entry creation approach:**

Each entry should:
- Reference the specific pattern number and name from the book
- Source frame: `architecture-and-building`
- Explain the architectural insight first, then map it to the target domain
- Identify concrete expressions in software, organizations, or design
- The Limits section should address where the architectural metaphor breaks
  down or misleads in the target domain
- Kind: `pattern` (these are named design patterns)
- Include cross-references to related patterns (Alexander's patterns are a
  network; related entries should link to each other)

## Schema Mapping

| Alexander field | Metaphorex field |
|-----------------|-----------------|
| Pattern number | `pattern_number` in manifest (not in entry frontmatter) |
| Pattern name | `name` (title case) |
| -- | `slug` (kebab-case of name) |
| -- | `kind`: `pattern` |
| -- | `source_frame`: `architecture-and-building` |
| Context/domain of application | `applies_to` |
| Section of book (Towns/Buildings/Construction) | `categories` |
| Related patterns (graph edges) | `related` |
| Problem statement + discussion | Basis for **Transfers** section |
| Limitations of the architectural metaphor | **Limits** section |
| Common uses of the term outside architecture | **Expressions** section |

## Gotchas

1. **Book is the primary source, not freely available online.** The
   archives list pattern names and brief descriptions, but detailed content
   (problem statements, discussion, solution statements) requires the book.
   Miners should use the pattern name, number, and general knowledge of the
   concept. For well-known patterns (intimacy gradient, piecemeal growth),
   there is extensive secondary literature.

2. **Some patterns share names with unrelated concepts.** "Cascade"
   (#116 Cascade of Roofs) is unrelated to CSS cascading. "Interchange"
   (#34) is about transport, not data formats. Miners should be careful to
   trace the metaphor from Alexander's specific meaning, not a generic
   dictionary definition.

3. **Alexander patterns vs. Alexander philosophy.** Several important
   Alexander concepts (Quality Without a Name, piecemeal growth, generative
   process) come from *The Timeless Way of Building* (1979) or *The Oregon
   Experiment* (1975), not *A Pattern Language*. These are included in the
   manifest with `pattern_number: -1` and already exist in the catalog.

4. **The architecture-to-software migration is well-trodden ground.**
   Many Alexander patterns have been discussed in software contexts (Beck,
   Cunningham, Gabriel, Coplien). Entries should cite this migration history
   but go beyond "Alexander said X, software people do Y" to examine where
   the metaphor illuminates and where it misleads.

5. **Sub-issue cap.** With 62 new candidates, this project is under the
   GitHub sub-issue limit of 100. No overflow handling needed.

6. **8 entries already exist.** The manifest marks these with
   `existing_entry: true`. The Surveyor should skip these when creating
   sub-issues: a-place-to-wait, light-on-two-sides, intimacy-gradient,
   main-entrance, piecemeal-growth, the-quality-without-a-name,
   pattern-language-as-shared-vocabulary, software-habitability.
