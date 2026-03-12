---
project_issue: 2
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Software Engineering Vernacular Metaphors

## Source Description

Informal developer culture: the metaphorical language that software
engineers use daily in Slack channels, blog posts, conference talks,
Stack Overflow answers, Reddit threads, and Hacker News comments. These
are not formal design patterns (covered by project #3) but living
vernacular -- expressions like "technical debt," "code smell," "yak
shaving," and "zombie process" that carry hidden conceptual structure.

This is a **vein** project: the source is ongoing and effectively
unbounded. Each batch focuses on a coherent set of candidates. Batch 1
covers the most well-known and structurally rich vernacular metaphors.

## Access Method

### Primary Archives (Batch 1)

Four structured online archives were used to build the initial candidate
list:

1. **Coding Horror: New Programming Jargon** (2012)
   https://blog.codinghorror.com/new-programming-jargon/
   Top 30+ entries from a Stack Overflow community wiki question on
   programming jargon. Curated by Jeff Atwood with community voting.
   Script: `scripts/extract_codinghorror.py`

2. **Dev.to: Wikipedia Coding Slang** (2021)
   https://dev.to/thormeier/i-plowed-through-coding-slang-wikipedia-articles-so-you-dont-have-to-25-terms-you-probably-didnt-know-3lkf
   25 terms systematically extracted from Wikipedia's computer jargon
   and anti-pattern articles.
   Script: `scripts/extract_devto_wikipedia.py`

3. **GitHub: software-engineering-terminology** (saqemlas)
   https://github.com/saqemlas/software-engineering-terminology
   Curated list of SE terminology, idioms, and concepts with descriptions.
   Script: `scripts/extract_github_terminology.py`

4. **Wikipedia: Anti-pattern & Computer Jargon categories**
   https://en.wikipedia.org/wiki/Anti-pattern
   https://en.wikipedia.org/wiki/Category:Computer_jargon
   Used for cross-referencing and verifying candidates. Direct scraping
   was blocked by Wikipedia's bot policy; entries were verified manually.

### Secondary Sources (not scraped, used for verification)

- **The Jargon File** (catb.org) -- the canonical hacker lexicon.
  TLS certificate issues prevented automated fetching, but the Jargon
  File was used as a reference for verifying etymology and usage of
  terms like "deep magic," "heisenbug," and "boat anchor."
  http://www.catb.org/jargon/html/

- **Nipun Arora: Software Engineering Idioms**
  https://www.blog.nipunarora.net/terminologies-used-in-tech/

### LLM Gap-Fill

11 of 41 candidates (27%) are LLM-sourced. These are well-known
metaphors that appear in developer discourse but were not present in
the scraped archives. They include foundational terms like "garbage
collection," "sandbox," "race condition," and "silver bullet" that any
developer would recognize. The Surveyor should verify these are genuine
vernacular metaphors worth cataloging.

### Future Batches

Batch 2+ should explore:
- The Jargon File entries (when TLS issues are resolved or via a mirror)
- Wikipedia's full "List of computer term etymologies" article
- Stack Overflow's community wiki on programming jargon (350+ answers)
- Reddit r/programming and r/ExperiencedDevs for emerging metaphors
- Conference talk transcripts (Strange Loop, PyCon, etc.)
- Martin Fowler's bliki for methodology metaphors
- DevOps/SRE culture for infrastructure metaphors (pets vs cattle, etc.)

## Extraction Strategy

Each candidate becomes one mapping entry. The extraction approach:

1. **Identify the source domain** of the expression. "Technical debt"
   borrows from finance. "Code smell" borrows from olfactory perception.
   "Yak shaving" borrows from animal husbandry (via a Ren & Stimpy
   episode, allegedly).

2. **Map the structural parallels** -- what features of the source domain
   carry over to software engineering, and what makes the mapping apt?
   The best vernacular metaphors have deep structural correspondence:
   technical debt has principal, interest, compound interest, bankruptcy,
   refinancing -- each maps to a specific software engineering situation.

3. **Find the breaks** -- where does the metaphor mislead? "Technical
   debt" implies you can always pay it back, but some tech debt
   compounds beyond recovery. "Code smell" implies subjectivity, but
   some smells are objectively measurable.

4. **Collect expressions** -- real phrases developers use that extend or
   rely on the metaphor. For "technical debt": "we need to pay down our
   debt," "the interest is killing us," "we're technically bankrupt."

5. **Trace the origin** -- many vernacular metaphors have documented
   origin stories. Ward Cunningham coined "technical debt" in 1992.
   Kent Beck and Martin Fowler popularized "code smell." The origin
   story matters because it reveals the original intent of the mapping.

### Prioritization

Candidates are ordered by metaphorical richness:
- **Tier 1 (do first):** Rich structural metaphors with multiple
  parallel mappings, active community usage, and interesting breaks.
  Examples: technical-debt, code-smell, spaghetti-code, cargo-cult-programming.
- **Tier 2:** Solid metaphors with clear source domains but thinner
  structural mapping. Examples: bus-factor, dogfooding, bikeshedding.
- **Tier 3:** Dead metaphors or thin metaphors still worth documenting.
  Examples: sandbox, garbage-collection, race-condition.

### Distinguishing from Project #3 (Design Patterns)

Project #3 covers formal design patterns (GoF, Fowler, Alexander) where
the pattern name is the metaphor. This project covers informal developer
vernacular. The boundary:

- "The Factory Pattern" = project #3 (formal pattern, named metaphor)
- "Spaghetti code" = project #2 (informal vernacular, organic metaphor)
- "Technical debt" = project #2 (informal vernacular, coined metaphor)

Some overlap may exist in frames (e.g., both use `manufacturing`,
`social-roles`). That is fine -- frames are shared vocabulary.

## Schema Mapping

### Frames needed (create if missing)

Several source frames may need to be created by the Miner:

| Frame slug | Description |
|---|---|
| economics | Financial systems, debt, interest, investment, bankruptcy |
| detective-fiction | Clues, red herrings, investigations, trails |
| natural-phenomena | Volcanic, oceanic, weather, geological processes |
| risk-assessment | Probability, exposure, vulnerability, mitigation |
| organizational-behavior | Management, hierarchy, promotion, dysfunction |

Existing frames that will be heavily reused:
- `embodied-experience` -- for bodily/sensory metaphors (smell, rot, etc.)
- `food-and-cooking` -- spaghetti, baklava, chunky salsa
- `mythology` -- cargo cult, hydra, voodoo, silver bullet, deep magic
- `social-behavior` -- rubber ducking, drinking the kool-aid
- `animal-husbandry` -- yak shaving, dogfooding, monkey patching
- `military-command` -- skunkworks
- `competition` -- race condition, jenga
- `manufacturing` -- golden hammer
- `social-roles` -- orphan process

### Target frames

Most candidates target `software-programs` (the metaphor describes
something about code or running software). Some target:
- `collaborative-work` -- bikeshedding, bus-factor, skunkworks, fear-driven-development
- `software-programs` -- most others

### Categories

Primary: `software-engineering` (all candidates)
Secondary: `cognitive-science`, `organizational-behavior`,
`systems-thinking`, `philosophy`, `security` (where applicable)

### Kind assignments

Valid kinds: `conceptual-metaphor`, `archetype`, `dead-metaphor`, `paradigm`.

- Most entries: `conceptual-metaphor` (the source domain is still active
  in the developer's mind when using the term)
- Dead metaphors: `dead-metaphor` for terms so embedded that the source
  domain is forgotten -- `garbage-collection`, `sandbox`, `race-condition`,
  `magic-number`, `duck-typing`
- No `archetype` or `paradigm` entries in this batch

## Gotchas

1. **Overlap with project #3.** Design patterns are formal; vernacular
   metaphors are informal. If a term appears in both, the vernacular
   entry should focus on how developers *actually use* the metaphor in
   conversation, not on the formal pattern definition.

2. **Existing catalog entries.** `data-flow-is-fluid-flow`,
   `program-failure-is-bodily-failure`, `bottleneck`, and `firewall`
   already exist in the catalog. This batch does NOT include these.
   Related entries should link to them via `related:`.

3. **Cultural sensitivity.** "Drinking the Kool-Aid" references a mass
   death event. "Voodoo programming" appropriates a religious practice.
   The Miner should note these origin stories honestly without sanitizing
   them. The metaphor's power often comes from its darkness.

4. **Dead metaphor detection.** The line between conceptual-metaphor and
   dead-metaphor is judgment. A good test: if you told a junior developer
   "that's a metaphor from [source domain]," would they be surprised?
   If yes, it is a dead metaphor.

5. **Food metaphor family.** Spaghetti, baklava, lasagna, and ravioli
   code form a coherent family. The Miner should use `related:` links
   to connect them and reference the family in each entry.

6. **Physics-bug family.** Heisenbug, Bohrbug, Mandelbug, Schrodinbug
   form a family. Only Heisenbug is in this batch (the others are
   rare in actual usage). The Miner should mention the family in the
   Heisenbug entry.

7. **Frame reuse.** Many candidates share frames. Check what exists
   before creating new ones. In particular, `embodied-experience` already
   covers a lot of the sensory/bodily metaphors.

8. **Vernacular, not academic.** The tone of these entries should reflect
   developer culture. Quote actual usage from Stack Overflow, Hacker News,
   etc. These metaphors live in conversation, not in textbooks.
