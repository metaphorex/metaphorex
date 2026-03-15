---
project_issue: 1228
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Glasgow Mapping Metaphor — Prospecting Playbook

## Source Description

The **Mapping Metaphor** project at the University of Glasgow is an
AHRC-funded database (2012--2015) containing 14,000+ metaphorical
connections across 415 semantic categories, built on the Historical
Thesaurus of English (OUP, 2009). It analyzes approximately 4 million
word senses spanning 1,300 years of English, from Old English to the
present day.

The database organizes English vocabulary into three worlds:

- **External World** (1A--1Q): 257 categories, 5,257 connections
- **Mental World** (2A--2G): 83 categories, 1,540 connections
- **Social World** (3A--3M): 75 categories, 1,151 connections

Each connection links two semantic categories with:
- **Direction**: which domain provides the metaphor (>, <, or bidirectional <>)
- **Strength**: Strong or Weak (based on number of attesting word senses)
- **First date**: earliest attested period (e.g., "Old English", "1550-1599")
- **Sample lexemes**: specific words that instantiate the metaphorical transfer

## Access Method

### Primary: AJAX JSON API

The database exposes an undocumented AJAX API at:

```
https://mappingmetaphor.arts.gla.ac.uk/ajax/getJSON-table-drilldown.php
```

Parameters:
- `subCat`: subcategory code (e.g., `3C01` for "War and armed hostility")
- `strength`: `strong`, `weak`, or `both`

**Required headers** (API returns 403 without these):
- `Referer: https://mappingmetaphor.arts.gla.ac.uk/map-english/`
- `User-Agent: Mozilla/5.0 (compatible; Metaphorex/1.0; +https://metaphorex.org)`

Returns JSON array of connection objects:
```json
{
  "cat1": "3C01",
  "m1name": "War and armed hostility",
  "direction": ">",
  "cat2": "2B03",
  "m2name": "Answer and argument",
  "strength": "Strong",
  "firstdate": "1550-1599",
  "words": ["<i><a href='...'>assault</a></i>", ...],
  "type": "expanded"
}
```

### Secondary: Aggregated Category View

```
https://mappingmetaphor.arts.gla.ac.uk/ajax/getJSON-aggregated.php?mType=strong
```

Returns the 37 top-level categories with their import relationships
(which categories connect to which). Useful for understanding the
overall network topology.

### Scraping Script

`scripts/fetch_connections.py` — queries the AJAX API for a configurable
set of subcategories, deduplicates by category pair, strips HTML from
lexeme fields, and outputs structured JSON. Requires `requests`.

Run with:
```bash
uv run playbooks/glasgow-mapping-metaphor/scripts/fetch_connections.py > connections.json
```

### Archive URLs

- Homepage: https://mappingmetaphor.arts.gla.ac.uk/
- Interactive map: https://mappingmetaphor.arts.gla.ac.uk/map-english/
- About/stats: https://mappingmetaphor.arts.gla.ac.uk/about-the-project/stats-and-figures/
- User guide: https://mappingmetaphor.arts.gla.ac.uk/how-to-use/user-guide-text/

## Extraction Strategy

### Trial Slice Approach (per issue instructions)

The issue explicitly requests a **trial-slice approach** rather than
full extraction. This playbook follows that directive.

**Trial methodology:**
1. Queried 22 subcategories chosen for cross-domain richness (physical
   domains mapping to mental/social domains and vice versa)
2. Filtered to Strong connections only (these have multiple attesting
   word senses, indicating genuine productivity)
3. Selected 25 connections that meet all three criteria:
   - **Still alive**: metaphorical connection is productive in modern English
   - **Structural**: encodes a reasoning pattern, not just shared vocabulary
   - **Recognizable**: a non-specialist would recognize the expressions

### Trial Results

Of approximately 400+ strong connections reviewed across the sampled
subcategories, 25 passed the trial criteria. Most connections in the
database are:

- **Granular lexical observations**: e.g., "sword" appearing in both
  LIGHT and WAR categories. This is an individual word transfer, not a
  structural metaphor.
- **Historically attested but extinct**: connections from Middle English
  with no modern currency.
- **Within-world transfers**: e.g., FOOD -> DRINK, which are adjacent
  domain extensions rather than cross-domain metaphors.

### Recommendation: Cherry-Pick

**Recommended approach: extract the 25 trial-slice candidates as mappings,
then catalog the Glasgow database as a reference work.**

Rationale:
- The 25 candidates are genuinely strong Metaphorex entries
- Many overlap with Lakoff/Johnson canon (ARGUMENT IS WAR, TIME IS
  MOVEMENT, etc.) -- but Glasgow provides historical depth and lexical
  evidence that enriches the entries
- The remaining 13,975+ connections are academically valuable but do not
  meet Metaphorex's "load-bearing reasoning pattern" bar
- A full extraction would produce mostly dead-metaphor or granular entries
  that dilute catalog quality

### Deduplication Note

Several trial-slice candidates overlap with existing catalog entries or
with candidates from other import projects (e.g., lakoff-johnson-mwlb).
The manifest marks these. The Miner should:
- Skip candidates already in the catalog (e.g., ARGUMENT IS WAR)
- For candidates in other projects, check which project has richer source
  material and extract from the better source
- When Glasgow provides historical depth that other sources lack, note
  Glasgow as a secondary reference in the mapping's References section

## Schema Mapping

### Glasgow Category -> Metaphorex Frame

| Glasgow Category | Metaphorex Frame | Notes |
|-----------------|-----------------|-------|
| 1A28 Atmosphere and weather | weather | New frame |
| 1B01 Life | life-course | Existing frame |
| 1C01 Health / 1C02 Ill-health | medicine | Existing frame |
| 1E01 Animals | animal-behavior | Existing frame |
| 1F01 Plants | horticulture | Existing frame (covers plant growth) |
| 1G01 Food and eating | food-and-cooking | Existing frame |
| 1I07 Sight | vision | Existing frame |
| 1I12 Perception and cognition | intellectual-inquiry | Existing frame |
| 1J03 Weight, heat and cold | heat / weight | New frames |
| 1J08 Strength | physical-strength | New frame |
| 1M01 Time | time-and-temporality | Existing frame |
| 1N01 Movement | movement | New frame |
| 2A01 Mind | mental-experience | Existing frame |
| 2A07 Perception and cognition | intellectual-inquiry | Existing frame |
| 2A10 Cleverness | intelligence | New frame |
| 2B03 Answer and argument | argumentation | Existing frame |
| 2D01 Emotion | emotion | New frame |
| 2D08 Love and friendship | love-and-relationships | Existing frame |
| 2D17 Courage | courage | New frame |
| 2E05 Decision-making | decision-making | Existing frame |
| 3A10 Social conflict | social-behavior | Existing frame |
| 3C01 War and armed hostility | war | Existing frame |
| 3D01 Rule and government | authority-and-mentorship | Existing frame |
| 3F01 Morality | ethics-and-morality | Existing frame |
| 3J01 Travel and travelling | travel | Existing frame |
| 3L01 Trade and commerce | economics | Existing frame |
| 3M07 Performance arts | performance | New frame |

### Glasgow Fields -> Metaphorex Fields

| Glasgow Field | Metaphorex Field | Notes |
|--------------|-----------------|-------|
| (constructed) | slug | Kebab-case from metaphor name |
| (constructed) | name | "SOURCE IS TARGET" format |
| (inferred) | kind | Usually `conceptual-metaphor` |
| cat1/m1name | source_frame | Map via table above |
| cat2/m2name | target_frame | Map via table above |
| direction | (body text) | Note in Origin Story |
| strength | (body text) | Note in Origin Story |
| firstdate | (body text) | Historical depth for Origin Story |
| words | Expressions | Sample expressions to expand |

### Body Section Guidance for Miner

- **What It Brings**: Use the Glasgow connection data as a starting point
  but expand well beyond it. Glasgow provides the lexical evidence; the
  Miner should articulate the structural mappings (what roles, relations,
  and inferences transfer).
- **Where It Breaks**: Glasgow data says nothing about where metaphors
  break. This section must come from the Miner's analysis.
- **Expressions**: Glasgow's `words` field provides a seed list of
  individual words. Expand these into full expressions with contextual
  sentences.
- **Origin Story**: Cite Glasgow's historical dating and lexical evidence.
  Include the first attestation period and note how the connection
  evolved over time.
- **References**: Always cite the Glasgow Mapping Metaphor project.

## Gotchas

1. **The Glasgow API is undocumented and requires browser-like headers.**
   It returns 403 without `Referer` and `User-Agent` headers. The scraping
   script includes these headers. If the API changes, save raw JSON responses
   as a fallback.

2. **Glasgow connections are bidirectional observations, not named metaphors.**
   "3C01 > 2B03" (War -> Argument) is the raw data; "ARGUMENT IS WAR" is
   the Metaphorex interpretation. The Miner must construct the metaphor
   name and determine which direction is conceptually primary.

3. **Many candidates overlap with Lakoff/Johnson canon.** At least 8 of
   the 25 trial candidates are well-known conceptual metaphors. Glasgow
   adds historical depth but the Miner should check for existing catalog
   entries and cross-reference with the lakoff-johnson-mwlb project.

4. **Word lists contain HTML.** The scraping script strips HTML tags, but
   the Miner should verify cleaned output. Some words include etymological
   notation (e.g., "world < woruld") that should be preserved in Origin
   Story sections.

5. **Strength is relative to the Glasgow methodology.** "Strong" means
   multiple word senses attest the connection, not that the metaphor is
   cognitively important. Some "Weak" Glasgow connections may be stronger
   conceptual metaphors than some "Strong" ones.

6. **No sub-issue overflow.** The cherry-pick approach yields 25 candidates,
   well under GitHub's 100 sub-issue limit.
