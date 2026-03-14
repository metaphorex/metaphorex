---
project_issue: 1226
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Nautical Terms -- Seafaring Metaphors in Everyday Language

## Source Description

The English language contains an extraordinary concentration of dead metaphors
from seafaring. The Age of Sail (16th-19th centuries) produced professional
vocabulary that migrated into everyday English as the metaphors' nautical
origins were forgotten. Terms like "loose cannon," "bitter end," "taken
aback," and "by and large" are now fully dead -- used daily by people who
have never been on a sailing vessel.

The primary structured source is the **Wikipedia Glossary of Nautical Terms**,
split across two pages (A-L and M-Z) with hundreds of entries. However, the
glossary contains mostly pure nautical vocabulary (starboard, halyard, cleat)
that never entered metaphorical use. The real value comes from cross-referencing
the glossary against curated lists of nautical terms that have migrated into
common usage.

**Primary references cited in the import issue:**

- Olivia Isil, *When a Loose Cannon Flogs a Dead Horse There's the Devil
  to Pay* (Ragged Mountain Press, 2003) -- book-length treatment of nautical
  terms in everyday English
- Beavis & McCloskey, *Salty Dog Talk: The Nautical Origins of Everyday
  Expressions* (Sheridan House, 1983) -- earlier systematic catalog

## Access Method

**Structured web archives used for extraction:**

1. **NOAA Nautical Terms** --
   https://oceanservice.noaa.gov/navigation/nautical-terms.html
   US government page listing common phrases with nautical origins.
   Well-structured, freely accessible.

2. **Royal Museums Greenwich** --
   https://www.rmg.co.uk/stories/maritime-history/nautical-origins-everyday-phrases
   Curated list from the UK's national maritime museum. Includes detailed
   etymologies and original nautical context. Highest-quality single source
   for etymological accuracy.

3. **Rubicon3 Sailor Sayings** --
   https://www.rubicon3adventure.com/50-sailor-sayings-you-wont-believe-are-part-of-your-daily-speech/
   50-item list with concise origins and modern meanings.

4. **Wikipedia Glossary of Nautical Terms** --
   https://en.wikipedia.org/wiki/Glossary_of_nautical_terms_(A%E2%80%93L)
   https://en.wikipedia.org/wiki/Glossary_of_nautical_terms_(M%E2%80%93Z)
   Comprehensive reference for verifying nautical origins and technical
   details. Not used as primary extraction source (too much non-metaphorical
   vocabulary) but essential for fact-checking.

**Extraction script:** `scripts/extract_nautical_metaphors.py` fetches the
NOAA and RMG pages and extracts term lists. The script is supplementary --
the actual candidate list was curated by cross-referencing all four web
archives plus the book references listed in the import issue.

```bash
uv run playbooks/nautical-terms/scripts/extract_nautical_metaphors.py
```

## Extraction Strategy

The Wikipedia glossary contains hundreds of entries. The import issue
estimates 20-35 mappings after heavy curation. The selection criteria:

**Include if:**

1. The term has genuinely migrated into non-nautical discourse -- people
   use it without knowing its seafaring origin
2. The term functions as a structural metaphor, not just an etymology
   curiosity -- it maps a source-domain relationship onto a target domain
3. There is a substantive "Where It Breaks" -- the nautical origin encodes
   assumptions that fail when applied to the modern usage
4. The term appears in at least two of the four web archive sources

**Exclude if:**

- Pure nautical vocabulary that never left the domain (starboard, halyard,
  bowsprit, jib)
- Terms where the nautical connection is disputed or folk etymology
  (e.g., "the whole nine yards" -- disputed origin, possibly not nautical)
- Terms that are essentially synonyms of already-included terms (e.g.,
  "smooth sailing" and "plain sailing" are the same metaphor)
- Terms too thin for a full mapping entry (e.g., "skipper" -- yes it's
  nautical, no there's nothing interesting to say about where it breaks)

**Result:** 35 candidates selected. All sourced from the web archives above.

**Frame assignment:** All candidates use `seafaring` as source_frame. This
is a new frame that needs to be created. Target frames vary by what the
metaphor illuminates in its modern usage.

## Schema Mapping

| Archive field | Metaphorex field | Notes |
|--------------|-----------------|-------|
| Term name | `name` | Title-cased |
| Term slug | `slug` | kebab-cased |
| Nautical origin | Feeds "What It Brings" | The original seafaring context |
| Modern meaning | Feeds "What It Brings" | The metaphorical migration |
| n/a | `kind` | Almost all `dead-metaphor` |
| n/a | `source_frame` | `seafaring` for all |
| n/a | `target_frame` | Varies by modern usage domain |

**Kind assignment:** Nearly all entries are `dead-metaphor` -- terms whose
nautical origins have been forgotten by most speakers. A few could be argued
as `conceptual-metaphor` if they are still used with awareness of the
nautical source (e.g., "sailing close to the wind" where the sailing image
is still somewhat active). The Miner should make the final call.

**Author:** All entries use `author: agent:metaphorex-miner`.

## Gotchas

1. **New frame required:** `seafaring` does not exist in `catalog/frames/`.
   The Miner must create it. Roles should include: vessel, crew, wind,
   rigging, cargo, harbor, course, weather, rank, armament.

2. **Category:** All candidates use `linguistics` as their primary category.
   This is appropriate since the project is about linguistic migration of
   terms, not about sailing per se.

3. **"Where It Breaks" is the key value-add.** The web archives provide
   the nautical origin and modern meaning. What they do NOT provide is
   analysis of where the metaphor fails -- the structural tensions between
   the nautical source and the modern usage. This is where the Miner adds
   genuine value. The import issue emphasizes this: "dead metaphors whose
   limits nobody thinks about are the most interesting."

4. **Disputed etymologies.** Some nautical origins are folk etymology.
   "The whole nine yards" is excluded because its nautical attribution is
   disputed. "Let the cat out of the bag" has competing nautical (cat-o'-
   nine-tails) and market (pig-in-a-poke) etymologies -- it is excluded.
   "Pipe down" and "toe the line" have both nautical and non-nautical
   proposed origins. Where included, the Miner should note the disputed
   etymology.

5. **Clusters by rigging, weather, punishment, and navigation.** The import
   issue notes that nautical metaphors come in clusters. The Miner should
   use the `related` field to link terms within clusters:
   - **Rigging terms:** know-the-ropes, jury-rigged, mainstay,
     three-sheets-to-the-wind
   - **Weather/wind terms:** in-the-doldrums, taken-aback,
     sailing-close-to-the-wind, take-wind-out-of-sails
   - **Punishment terms:** keelhauled, over-a-barrel
   - **Navigation terms:** even-keel, leeway, try-different-tack,
     plain-sailing
   - **Combat terms:** loose-cannon, shot-across-the-bow,
     showing-true-colors, first-rate

6. **Existing catalog entry:** `boat-anchor` already exists with
   source_frame `tool-use` and target_frame `software-programs`. It is a
   software-specific dead metaphor, not a general nautical term, so it is
   not duplicated here. The Miner should add `boat-anchor` to the `related`
   field of relevant entries.

7. **Candidate count (35) is well under the 100 sub-issue cap.** No
   overflow handling needed.
