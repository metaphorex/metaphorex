---
project_issue: 219
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Fantasy, Mythology, and Folklore as Conceptual Frame

## Source Description

Mythology, folklore, fantasy literature, and fairy tales -- ancient and modern
narratives whose concepts have become default frames for reasoning about power,
technology, organizations, and human nature. This is a **vein** project:
mythology-derived metaphors are effectively inexhaustible.

**Batch 1** focuses on metaphors that are actively used in modern discourse
across multiple domains (tech, business, politics, everyday life), organized
by tradition:

- **Greek/classical** (20 candidates): Achilles' heel, Pandora's box, Trojan
  horse, Sisyphean task, Midas touch, Siren song, Prometheus, Hydra, Labyrinth,
  Icarus, Phoenix, Nemesis, Herculean task, Odyssey, Cassandra, Narcissism,
  Chimera, Cornucopia, Aegis, Mentor
- **Additional classical** (15 candidates): Damocles' sword, Gordian knot,
  Pyrrhic victory, Procrustean bed, Augean stables, Cerberus, Elysium,
  Pandemonium, Scylla and Charybdis, Tantalus, Sphinx riddle, Trojan War,
  Faustian bargain, Pied Piper, Ouroboros
- **Norse/Germanic** (4 candidates): Ragnarok, Berserker, Valhalla, World tree
- **Arthurian** (3 candidates): Holy Grail, Excalibur, Round table
- **Cross-cultural folklore** (9 candidates): Golem, Emperor's new clothes,
  Sorcerer's apprentice, Rumpelstiltskin, Alchemy, Dragon hoard, Chosen One,
  Dark forest, Trickster, Shapeshifter
- **Eastern** (3 candidates): Karma, Yin and yang, Koan
- **Tolkien/modern fantasy** (5 candidates): One Ring, Palantir, Mordor,
  The Shire, Necromancy

## Access Method

### Primary Archives

1. **Wikipedia: Category "Words and phrases derived from Greek mythology"**
   https://en.wikipedia.org/wiki/Category:Words_and_phrases_derived_from_Greek_mythology
   Contains ~39 entries of English terms with Greek mythological origins.
   Wikipedia blocks automated scraping (403), so data was manually extracted
   and encoded as a static dataset in the extraction script.

2. **YourDictionary: 29 English Words With Origins in Greek Mythology**
   https://www.yourdictionary.com/articles/english-words-greek-mythology
   Curated list of mythology-derived English words with etymological context.

3. **Wikipedia: Individual mythology articles**
   Each candidate links to its Wikipedia article for the mythological source.
   URLs are cited per-entry in the extraction script and manifest.

4. **BeSpeaking: Idioms from Greek Mythology**
   https://www.bespeaking.com/idioms-from-greek-mythology/
   Five core Greek mythology idioms with usage examples.

5. **RelatedWords.io: Mythology (400+ words)**
   https://relatedwords.io/mythology
   Broad vocabulary list; used as discovery source, not primary archive.

### Methodology

Wikipedia's structured category pages and individual mythology articles serve
as the primary source for verifying that each candidate has genuine mythological
origins and documented modern metaphorical usage. Because no single archive
enumerates "mythology-as-metaphor" comprehensively, candidates were assembled
from multiple Wikipedia pages, cross-referenced with etymological sources.

The extraction script (`scripts/extract_mythology_metaphors.py`) encodes the
archive data as static datasets (since Wikipedia returns 403 on automated
scraping) and applies deterministic slug generation and frame classification.

## Extraction Strategy

1. **Source verification**: Each candidate must trace to a specific myth,
   folklore narrative, or fantasy source with a citable Wikipedia article.
2. **Modern usage test**: The candidate must be actively used as a metaphor
   in non-literary contexts (business, tech, politics, everyday speech).
   Per the issue's inclusion test, candidates must meet 2 of 3 criteria:
   active modern usage, structural depth, moral/causal encoding.
3. **Structural mapping**: The mythological concept must map onto real domains
   with multiple parallel elements, not just surface resemblance.
4. **Frame classification**: The script classifies target frames based on
   keyword analysis of modern meanings. Miners should refine these.

## Schema Mapping

| Manifest field | Mapping frontmatter field | Notes |
|---|---|---|
| slug | slug | Direct; kebab-case |
| name | name | Use the common English form (e.g., "Achilles' Heel") |
| kind | kind | Most are `conceptual-metaphor`; some dead metaphors (mentor, nemesis) may be `dead-metaphor` |
| source_frame | source_frame | Almost all use `mythology` frame; some may need tradition-specific frames |
| target_frame | target_frame | Script assigns heuristically; miners should verify |
| categories | categories | All include `mythology-and-religion`; miners add domain-specific categories |
| description | -- | Guides the Miner; not in frontmatter |
| tradition | -- | Informs the Origin Story section |
| archive_url | -- | Cite in References section |

### Miner Instructions

For each mapping, the Miner should:

1. **What It Brings**: Describe the mythological narrative structure and how
   it maps onto the target domain. Include the specific structural parallels
   (roles, sequences, consequences).
2. **Where It Breaks**: This is critical. Every mythological frame has limits.
   Where does the analogy mislead? What does the myth assume that does not
   hold in the target domain?
3. **Expressions**: Collect real-world usage examples. Prioritize non-obvious
   uses in tech, business, and policy discourse over literary references.
4. **Origin Story**: Brief retelling of the myth, focused on the elements
   that make it work as a metaphor.
5. **References**: Cite the Wikipedia article and any domain-specific usage.

### Special Considerations

- **Dead metaphors**: Some entries (mentor, nemesis, aegis, pandemonium) are
  so embedded in English that speakers do not realize they are mythological.
  For these, the Miner should consider `kind: dead-metaphor` and emphasize
  the hidden mythological structure.
- **Overlap with existing mappings**: `hydra-code` (slug: hydra-code) already
  exists for the software-specific application. The general `hydra` mapping
  should cover the broader metaphor across domains. `ai-is-an-oracle` exists;
  a general oracle/Delphi mapping would complement it.
- **Tolkien entries**: These are modern literary creations, not ancient myth.
  The Miner should acknowledge this in the Origin Story and explain why they
  function as mythological frames despite being authored by a known individual.

## Gotchas

- **Vein project**: This batch covers 60 candidates. Future batches should
  explore: gaming metaphors (level up, boss fight, respawn), additional
  fairy tale frames, African/Polynesian/Indigenous mythologies,
  Mesopotamian/Sumerian frames, and Hindu epic metaphors.
- **Kind ambiguity**: Some candidates straddle `conceptual-metaphor` and
  `dead-metaphor`. The Miner should make the judgment call per entry.
- **Frame creation**: Miners will likely need to create new frames for some
  target domains. The `mythology` source frame already exists.
- **Tradition-specific frames**: Future batches may need `norse-mythology`,
  `arthurian-legend`, `eastern-philosophy` as source frames if the general
  `mythology` frame becomes too broad.
- **Sub-issue cap**: 60 candidates is within the GitHub 100-sub-issue limit.
  No overflow handling needed for batch 1.
