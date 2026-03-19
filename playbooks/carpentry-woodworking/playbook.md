---
project_issue: 1359
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Playbook: Carpentry and Woodworking

## Source Description

Carpentry and woodworking proverbs, terminology, and philosophical
frameworks that have migrated into figurative language across software
engineering, management, education, and everyday speech. Three distinct
layers:

1. **Workshop proverbs** -- "measure twice, cut once," "the best carpenters
   make the fewest chips," "let the tool do the work." Folk wisdom encoding
   asymmetric risk, economy of action, and preparation-over-force.

2. **David Pye's framework (1968)** -- *The Nature and Art of Workmanship*
   introduced the workmanship-of-risk vs. workmanship-of-certainty
   distinction. Not hand vs. machine, but whether the outcome is
   predetermined. Foundational for craft studies, design history, and the
   software craftsmanship movement.

3. **Joinery and material vocabulary** -- dovetail, mortise-and-tenon,
   shim, jig, veneer, grain, seasoning, knot. Many are dead metaphors in
   English (people say "dovetail" without knowing the joint). Others are
   alive in software (shim, scaffold, framework).

4. **Japanese woodworking philosophy** -- shokunin (artisan obligation),
   wabi-sabi (beauty in imperfection), Toshio Odate's writings. These
   concepts have been adopted by the software craftsmanship and lean
   movements.

## Access Method

### Primary Archives

**Wikipedia Glossary of Woodworking**
- URL: https://en.wikipedia.org/wiki/Glossary_of_woodworking
- Format: HTML alphabetical glossary with definitions
- Coverage: Comprehensive technical terminology (hundreds of terms)
- Usage: Reference for joint types, wood properties, tool names
- Note: Direct fetch returns 403; content accessed via WebSearch summaries

**First Round Review: Shims, Jigs, and Woodworking Concepts**
- URL: https://review.firstround.com/shims-jigs-and-other-woodworking-concepts-to-conquer-technical-debt/
- Format: Long-form article mapping woodworking to software
- Coverage: Shim, jig, knock-down joint, master carpenter
- Successfully fetched and parsed

**The Quote Garden: Woodworking Quotes**
- URL: https://www.quotegarden.com/woodworking.html
- Format: HTML list of attributed quotes
- Coverage: ~16 woodworking proverbs and aphorisms with dates
- Successfully fetched and parsed

**LumberJocks Forum: Woodworking Sayings and Proverbs**
- URL: https://www.lumberjocks.com/threads/woodworking-sayings-and-proverbs.47948/
- Format: Forum thread (JavaScript-rendered, not scrapable)
- Coverage: Community-sourced sayings
- Note: Content not extractable via fetch; used WebSearch summaries

**Japanese Tools Australia: Shokunin Kishitsu**
- URL: https://www.japanesetools.com.au/blogs/the-jta-blog/the-soul-of-the-tool-an-invitation-to-japanese-craftsmanship
- Format: Blog article
- Coverage: Shokunin concept and Japanese craft philosophy

**ESL Vault: Wood Idioms**
- URL: https://eslvault.com/wood-idioms/
- Format: HTML list of 31 wood-related idioms with explanations
- Coverage: Figurative expressions derived from wood and woodworking

### Secondary Sources (Consulted, Not Scraped)

- David Pye, *The Nature and Art of Workmanship* (1968) -- book, not
  available online. Key concepts extracted from secondary sources
  (Mortise & Tenon Magazine podcast, Lost Art Press blog, Medium summaries).
- Toshio Odate, *Japanese Woodworking Tools* -- book reference from the
  issue. Shokunin concept verified via web sources.
- Etymonline: etymology of "dovetail" (figurative use since 1650s)
- Shakespeare's *Coriolanus* (1607) -- first figurative use of
  "against the grain"

## Extraction Strategy

This is an **archive-type** project. The source material is finite: a
bounded set of woodworking terms, proverbs, and philosophical concepts
that have established figurative or metaphorical usage in other domains.

### Selection Criteria

A woodworking term qualifies as a candidate if it meets at least one of:

1. **Active figurative usage** -- the term is commonly used metaphorically
   in everyday English, business, or technical discourse (e.g., "dovetail,"
   "against the grain," "polished")

2. **Named framework** -- the term is part of a published intellectual
   framework that has been adopted beyond woodworking (e.g., Pye's
   workmanship of risk, shokunin)

3. **Software/tech adoption** -- the term has been explicitly borrowed
   by software engineering or tech culture (e.g., shim, jig, scaffolding,
   framework)

4. **Proverb with cross-domain applicability** -- a woodworking saying
   that encodes a general principle used in other fields (e.g., "measure
   twice, cut once")

### Exclusions

- Pure technical terms with no figurative life (e.g., "rabbet," "dado,"
  "spokeshave") unless they have documented metaphorical usage
- General construction terms that are not specifically woodworking
  (e.g., "foundation," "blueprint" -- these belong to architecture)
- Tools that are only known by name, not by metaphorical function

### No Scraping Script

Unlike projects with clean HTML glossaries, the woodworking archives are
a mix of forum threads (JavaScript-rendered), Wikipedia (403 on fetch),
and long-form articles. The candidate list was assembled by:

1. Searching and fetching multiple structured sources (Quote Garden,
   First Round Review, Wikipedia via search, ESL Vault)
2. Cross-referencing terms that appear across multiple sources
3. Verifying figurative usage via etymology (Etymonline) and idiom
   databases
4. Gap-filling with LLM knowledge for terms with obvious metaphorical
   life but no single canonical archive entry (flagged as source: "llm")

## Schema Mapping

| Woodworking concept | kind | source_frame | target_frame |
|---|---|---|---|
| Workshop proverbs | mental-model | carpentry | planning-and-preparation |
| Pye's framework concepts | paradigm | carpentry | quality-and-craftsmanship |
| Joint types (figurative) | metaphor | carpentry | abstract-organization |
| Material properties (figurative) | metaphor | carpentry | materials / social-dynamics |
| Software-adopted terms | metaphor | carpentry | software-programs |
| Japanese craft philosophy | paradigm | carpentry | quality-and-craftsmanship |
| Dead metaphors (idioms) | metaphor | carpentry | varies |

### Frame Requirements

The following frames will need to be created if they do not already exist:

- **carpentry** -- the source frame for all entries (does not exist yet)
- **quality-and-craftsmanship** -- target for Pye's framework, seasoning,
  polished (does not exist yet)
- **planning-and-preparation** -- target for proverbs about verification
  and setup (does not exist yet)

Existing frames that will be reused:
- materials, abstract-organization, social-dynamics, tool-use, aesthetics,
  causal-reasoning, software-programs, education-and-learning

### Category Usage

All entries use existing categories. No new categories needed:
- cognitive-linguistics, folk-wisdom, software-engineering, philosophy,
  arts-and-culture, social-dynamics, organizational-behavior

## Gotchas

1. **Many terms are dead metaphors.** "Dovetail," "against the grain,"
   "veneer," "polished," "nail it," "framework" -- speakers do not
   consciously connect these to woodworking. The Miner should foreground
   the etymological connection and what is lost/gained by the death of
   the metaphor.

2. **Overlap with architecture/construction.** Terms like "scaffolding"
   and "framework" sit at the boundary of carpentry and general
   construction. The entries should acknowledge the woodworking origin
   specifically (timber framing, not steel scaffolding).

3. **Pye's framework is subtle.** The workmanship-of-risk vs.
   workmanship-of-certainty distinction is NOT hand vs. machine. A hand
   tool with a jig is workmanship of certainty. A machine operated
   freehand is workmanship of risk. The Miner must get this right.

4. **Japanese terms need careful handling.** Shokunin and wabi-sabi are
   from Japanese culture broadly, not only woodworking. The entries
   should scope to the woodworking manifestation and note the broader
   cultural context without claiming woodworking as the sole origin.

5. **The candidate list is 27 entries.** Well within the 100 sub-issue
   GitHub cap.

6. **LLM-sourced candidates (7 of 27).** The following candidates are
   flagged as LLM-sourced because no single archive page provided them
   as metaphorical terms, though their figurative usage is well-attested:
   read-the-grain, cant-put-it-back-on, plane-it-smooth, framework,
   nail-it, heartwood-and-sapwood, tooling-up. The Surveyor should
   verify these are worth extracting.
