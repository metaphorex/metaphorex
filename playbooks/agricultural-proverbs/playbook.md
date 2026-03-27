---
project_issue: 1358
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Playbook: Agricultural Proverbs -- Ancient Farming Wisdom in Modern Language

## Source Description

Agricultural proverbs and farming wisdom that have migrated from literal
farming contexts into metaphorical use across business, politics, personal
development, and systems thinking. The source spans three distinct layers:

1. **Classical proverbs** -- ancient farming sayings (Biblical, Greek, Roman,
   Celtic, and cross-cultural folk wisdom) that have become idiomatic in
   English. These are the oldest metaphorical transfers in the language, some
   dating to Sumerian tablets.

2. **Permaculture principles** -- David Holmgren's 12 design principles and
   Bill Mollison's complementary principles from the permaculture movement
   (1970s-present). These are modern, deliberately articulated principles
   that use agricultural observation as a source domain for systems thinking.

3. **Regenerative agriculture concepts** -- contemporary farming philosophy
   (feed the soil not the plant, terroir, monoculture risk) that maps
   directly to organizational and creative domains.

### Relationship to Existing Catalog

The catalog already contains 9 entries with agricultural source frames:

- `creation-is-cultivation`, `creative-process-is-gardening` (horticulture)
- `ideas-are-plants`, `people-are-plants`, `prosperity-is-plant-growth`
- `beauty-is-a-flower`, `harm-is-a-thorn` (plant metaphors)
- `cornucopia` (harvest abundance archetype)
- `silo` (agricultural storage structure)

These are excluded from this project's manifest. The existing `agriculture`
and `horticulture` frames will be reused.

## Access Method

### Primary Archives

**Glossophilia: "On and Off the Farm"**
- URL: https://glossophilia.org/2021/01/on-and-off-the-farm-some-phrases-straight-out-of-the-barnyard/
- Format: HTML article with bold-tagged phrase names and inline definitions
- Coverage: 38 farm-origin phrases and idioms in English
- Scraping: `scripts/extract_agricultural_candidates.py` (BeautifulSoup)

**Proverbicals.com: Farming Proverbs**
- URL: https://proverbicals.com/farming
- Format: HTML list of 35 cross-cultural farming proverbs
- Coverage: Chinese, Irish, Estonian, Polish, Finnish, Ethiopian proverbs
- Used for manual review (structured enough for direct reading)

**Permaculture Principles (Holmgren)**
- URL: https://permacultureprinciples.com/permaculture-principles/
- Format: HTML page with 12 numbered principles + associated proverbs
- Coverage: All 12 Holmgren principles with canonical names
- Scraping: Hardcoded in extraction script (canonical list is stable)

**World Permaculture Association (Mollison)**
- URL: https://worldpermacultureassociation.com/mollison-principles/
- Format: HTML article listing Mollison's design principles
- Coverage: Mollison's principles including "the problem is the solution"

**EnchantedLearning: Farm Adages**
- URL: https://www.enchantedlearning.com/english/adages/farm.shtml
- Format: HTML list of farm adages with meanings
- Note: Content behind paywall; used WebFetch for initial read only

### Secondary Sources (Manual Research)

- Wendell Berry: *Bringing It to the Table*, *The Unsettling of America*
  (Goodreads quotes pages used for reference, not scraped)
- Pliny the Elder: *Natural History* -- "The master's eye is the best
  fertilizer" (cited in issue)
- Biblical Proverbs: agricultural subset (Galatians 6:7, Matthew 3:12,
  Matthew 7:6)

## Extraction Strategy

### Archive-sourced candidates (24 of 35)

The scraping script extracts raw phrases from Glossophilia and cross-
references with the Proverbicals.com list. Each raw phrase is evaluated for:

1. **Metaphorical productivity** -- does it map to domains beyond farming?
2. **Structural depth** -- does the mapping have enough complexity for a
   full Transfers + Limits + Expressions entry?
3. **Non-duplication** -- is it distinct from existing catalog entries?

Many barnyard animal idioms (e.g., "happy as a pig in mud," "hog-wild,"
"pig's ear") are colorful but lack structural metaphorical depth. These are
excluded from the manifest in favor of idioms with genuine cross-domain
mapping potential.

### LLM-sourced candidates (11 of 35)

The following candidates were identified from knowledge of the agricultural
tradition and are flagged as `"source": "llm"` in the manifest:

- `fallow-period` -- agricultural practice with no single canonical proverb
- `the-masters-eye-is-the-best-fertilizer` -- Pliny, cited in issue
- `feed-the-soil-not-the-plant` -- regenerative agriculture, cited in issue
- `deep-roots-are-not-reached-by-frost` -- proverb, not in scraped archives
- `terroir` -- viticultural concept, no proverb archive source
- `monoculture-risk` -- agricultural systems concept
- `pruning-for-growth` -- horticultural practice
- `grafting` -- horticultural practice
- `composting` -- agricultural process

These require additional verification by the Surveyor.

### Permaculture principle selection

Not all 12 Holmgren principles are included as separate candidates. Several
are too generic to be specifically agricultural (e.g., #4 "Apply Self-
Regulation and Accept Feedback" is a cybernetics principle, not distinctly
agricultural). The 7 included permaculture principles were selected because
their agricultural grounding is central to their metaphorical power.

## Schema Mapping

| Field | Mapping |
|-------|---------|
| `slug` | kebab-case of the proverb/concept name |
| `name` | Title case of the canonical form |
| `kind` | `metaphor` for proverbs with clear source/target domains; `mental-model` for permaculture principles and regenerative concepts; `pattern` for design patterns like stacking functions |
| `source_frame` | `agriculture` (most); `horticulture` for pruning, grafting |
| `target_frame` | Varies: `moral-accounting`, `time-and-temporality`, `systems-thinking`, `organizational-behavior`, etc. |
| `categories` | `folk-wisdom` for classical proverbs; `systems-thinking` for permaculture; both where applicable |
| `author` | Varies: omit for folk proverbs, specific for permaculture (holmgren, mollison) |
| `provenance` | `agricultural-proverbs` (this project) |

### Frames needed

New frames that may need creation:
- `evaluation-and-judgment` -- for wheat/chaff, pearls/swine, praise the ripe field
- `search-and-discovery` -- for needle in a haystack
- `social-identity` -- for black sheep
- `difficulty-and-effort` -- for hard row to hoe
- `human-development` -- for sow wild oats
- `resilience` -- for deep roots
- `action-and-agency` -- for plow a field by turning it over

Check existing frames before creating -- some may already exist under
different names.

## Gotchas

- **Barnyard animal idioms vs. agricultural metaphors**: Many farm-origin
  idioms involve animals (bull in a china shop, get my goat, beat a dead
  horse) but their metaphorical structure is about the animal behavior, not
  about agriculture as a practice. The manifest excludes pure animal-behavior
  idioms in favor of idioms whose agricultural process is the metaphorical
  engine.

- **Overlapping proverbs**: Some proverbs appear in multiple cultures with
  slight variation. The Miner should use the most widely known English form
  as the canonical name and note variants in the Expressions section.

- **Permaculture principles as mental models**: Holmgren's principles are
  explicitly designed as design thinking tools, not folk proverbs. They
  should be `kind: mental-model` with `author: holmgren` and should
  reference the permaculture tradition in their Origin Story section.

- **Biblical vs. folk attribution**: Several proverbs have both Biblical
  citations and pre-Biblical folk origins (reap what you sow, wheat from
  chaff). The Miner should note both without claiming definitive origin.

- **Candidate count (35)**: Well within the 100-sub-issue GitHub cap.
  No overflow handling needed.
