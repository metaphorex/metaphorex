---
project_issue: 218
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Science Fiction as Conceptual Frame

## Source Description

Science fiction literature, film, and television -- fictional concepts that
have escaped their source material to become **load-bearing frames** for
understanding real technology, policy, and culture. This is a **vein**
project: the source is ongoing and effectively unbounded. Each prospecting
batch identifies a coherent set of candidates.

**Batch 1** focuses on the highest-impact SF concepts that have achieved
**cultural escape velocity** -- used as real-world metaphors by people who
may never have read or seen the source material. The inclusion test from the
parent issue requires at least 2 of 3: frame transfer, structural depth,
cultural escape velocity.

## Access Method

### Primary Archives

Structured catalogs and academic resources used to validate and source the
candidate list.

1. **The SF Encyclopedia (sf-encyclopedia.com) -- Theme Entries**
   https://sf-encyclopedia.com/category/theme
   949 theme entries covering the full taxonomy of SF concepts. The most
   comprehensive structured catalog of SF ideas, maintained by John Clute,
   David Langford, and contributors. Theme entries like "Dystopias,"
   "Robots," "Cyberspace," "Terraforming," and "Singularity" provided
   authoritative origin data and cross-references. The scraping script
   extracts the theme index to identify candidates with SFE coverage.

2. **Jeff Prucher, *Brave New Words: The Oxford Dictionary of Science
   Fiction* (2007)**
   https://global.oup.com/academic/product/brave-new-words-9780195305678
   The first historical dictionary of SF terminology. Organized by thematic
   category (Communications, Robots, Weapons, Space Drives, etc.) with
   earliest-known citations and etymology. The Library of Congress TOC at
   https://catdir.loc.gov/catdir/toc/ecip074/2006037280.html confirms
   coverage categories. Not directly scrapable (book), but the OUP blog
   post below provides a structured subset.

3. **OUP Blog -- "Nine words you might think came from science but are
   from science fiction" (Jeff Prucher, 2009)**
   https://blog.oup.com/2009/03/science-fiction/
   Structured list of 9 SF-originated terms (robotics, genetic engineering,
   zero-gravity, deep space, ion drive, pressure suit, computer virus,
   worm, gas giant) with etymology and first-citation data. The scraping
   script extracts these.

4. **SFRA Review -- "Is That From Science or Fiction?" (2021)**
   https://sfrareview.org/2021/07/20/is-that-from-science-or-fiction-otherworldly-etymologies-neosemes-and-neologisms-reveal-the-impact-of-science-fiction-on-the-english-lexicon/
   Academic survey of SF neologisms and neosemes (words given new meanings
   by SF) that entered common English. Categorizes terms as neologisms
   (robot, spacesuit, blaster) and neosemes (alien, hyperspace, lightspeed).
   Provides structured tables with dates and source works.

5. **Gizmodo -- "31 Essential Science Fiction Terms" (2014)**
   https://gizmodo.com/31-essential-science-fiction-terms-and-where-they-came-1594794250
   Structured list of 31 SF terms with origin works and dates. Includes:
   alien, android, ansible, beam, blaster, credit, cryostasis, cyberspace,
   death ray, dystopia, first contact, force field, generation ship, hive
   mind, homeworld, jack in, mad scientist, moon base, multiverse, parallel
   universe, posthuman, ray gun, robot, spaceship, superhero, telepathy,
   teleportation, terraforming, time travel, tractor beam, and science
   fiction itself.

6. **Springer -- "What can science fiction tell us about the future of AI
   policy?" (2021)**
   https://link.springer.com/article/10.1007/s00146-021-01273-2
   Academic analysis of how SF narratives frame AI policy discourse.
   Documents the Skynet/Terminator frame, Asimov's Laws frame, and the
   Frankenstein frame as dominant policy-shaping metaphors.

7. **ORF -- "Science Fiction as the Blueprint" (2024)**
   https://www.orfonline.org/research/science-fiction-as-the-blueprint-informing-policy-in-the-age-of-ai-and-emerging-tech
   Policy analysis of SF concepts used in technology governance discussions.

### Scraping Script

`scripts/extract_sf_metaphors.py` scrapes:
- The SFE theme index page to extract all 949 theme entries, then filters
  to ~35 themes most relevant to real-world metaphorical usage.
- The OUP blog post to extract the 9 SF-to-mainstream word entries.

The script outputs JSON to stdout and is idempotent.

### LLM Gap-Fill

14 of 40 candidates (35%) are LLM-sourced. These are SF concepts actively
used as real-world metaphors but not explicitly cataloged as "metaphors that
crossed over" in the archive sources above. The archives catalog SF
*terminology* (words coined by SF) and SF *themes* (narrative concepts), but
not specifically the metaphorical transfer from fiction to real-world framing.
This gap is inherent to the project: no single archive tracks "SF concepts
used metaphorically in policy/technology discourse."

LLM-sourced candidates: red-pill-is-awakening, skynet-is-ai-apocalypse,
newspeak-is-thought-control, the-borg-is-assimilation, pod-people-are-
conformist-replacement, spice-is-scarce-enabling-resource, mentat-is-
human-computer, the-jackpot-is-slow-apocalypse, paperclip-maximizer-is-
alignment-failure, holodeck-is-total-simulation, prime-directive-is-non-
interference, black-mirror-is-technology-dark-side, space-colonization-is-
business-expansion, psychohistory-is-predictive-social-science,
replicant-is-artificial-person.

All are verifiable in public discourse with straightforward web searches.

## Extraction Strategy

### What makes a good candidate

The parent issue defines the inclusion test (at least 2 of 3):
1. **Frame transfer**: People use the concept to reason about something real
2. **Structural depth**: The fictional concept has internal structure that
   maps non-trivially onto the real domain
3. **Cultural escape velocity**: The reference is understood by people who
   haven't consumed the source material

Additionally, candidates must be **genuine conceptual metaphors** -- not just
pop culture references or SF vocabulary. "Warp drive" is SF vocabulary.
"The singularity is near" is a conceptual metaphor that structures how
people think about technological change.

### Kind assignments

- `conceptual-metaphor` -- most candidates. The SF concept is actively used
  to frame real-world reasoning. (big-brother, cyberspace, matrix, etc.)
- `literary-frame` -- the SF concept provides a narrative structure for
  understanding real phenomena, but is more complex than a single source-to-
  target mapping. (brave-new-world, the-jackpot, black-mirror, spice, mentat)
- `cross-field-mapping` -- the SF concept named or enabled a real field of
  study or engineering practice. (terraforming, genetic-engineering, ansible,
  tricorder, dyson-sphere, cryonics)
- `dead-metaphor` -- SF-originated terms now so naturalized that the fiction
  origin is invisible. (robot, computer-virus, zero-gravity, grok, waldo,
  deep-space)

### Prioritization

- **Tier 1 (highest impact, do first):** big-brother, frankenstein,
  cyberspace, the-matrix, robot, skynet, metaverse, three-laws, singularity
- **Tier 2 (strong metaphors with structural depth):** brave-new-world,
  newspeak, the-borg, red-pill, dystopia, hive-mind, generation-ship,
  paperclip-maximizer, computer-virus, genetic-engineering, terraforming
- **Tier 3 (solid but narrower scope):** ansible, tricorder, spice, mentat,
  psychohistory, holodeck, prime-directive, pod-people, grok, waldo,
  black-mirror, replicant, the-jackpot, dyson-sphere, time-travel,
  uploading, deep-space, zero-gravity, cryonics, space-colonization

## Schema Mapping

### New frames needed

| Frame slug | Description |
|---|---|
| science-fiction | SF literature, film, TV as source of conceptual frames |
| dystopian-fiction | Cautionary narrative about social/technological futures |
| television-fiction | Episodic television as source of cultural frames |

### Existing frames that will be reused

- `surveillance` -- Big Brother
- `mythology` -- Frankenstein
- `spatial-location` -- cyberspace, metaverse, holodeck, deep-space
- `containers` -- the Matrix, uploading
- `medicine` -- red pill, computer virus, tricorder, cryonics
- `war` -- Skynet
- `social-roles` -- brave new world, robot
- `language` -- Newspeak
- `animal-behavior` -- Borg, hive mind
- `biology` -- pod people, genetic engineering
- `communication` -- ansible
- `physics` -- singularity, zero-gravity, Dyson sphere, psychohistory
- `rule-following` -- three laws, prime directive
- `horticulture` -- terraforming
- `travel` -- generation ship, space colonization
- `narrative` -- dystopia
- `gambling` -- the Jackpot
- `embodied-experience` -- grok, waldo
- `manufacturing` -- replicant, paperclip maximizer
- `economics` -- spice
- `mental-experience` -- mentat
- `vision` -- Black Mirror
- `architecture-and-building` -- Dyson sphere
- `journeys` -- time travel
- `governance` -- Big Brother, Newspeak, dystopia, generation ship, prime directive

### New categories needed

| Category slug | Description |
|---|---|
| science-fiction-discourse | SF concepts functioning as real-world frames for technology, policy, and culture |

### Existing categories that will be reused

- `philosophy` -- Matrix, singularity, dystopia, uploading, replicant
- `cognitive-science` -- cyberspace, robot, grok, hive mind, time travel
- `linguistics` -- robot, grok, zero-gravity, deep-space, Newspeak
- `ai-discourse` -- Skynet, three laws, singularity, mentat, paperclip, replicant, uploading
- `ethics-and-morality` -- Frankenstein, genetic engineering, prime directive, Black Mirror
- `social-dynamics` -- brave new world, Borg, pod people, hive mind, dystopia, space colonization
- `computer-science` -- cyberspace, metaverse, ansible, computer virus, holodeck
- `law-and-governance` -- Big Brother, prime directive
- `systems-thinking` -- terraforming, generation ship, Dyson sphere, spice, the Jackpot
- `security` -- computer virus
- `software-engineering` -- ansible
- `health-and-medicine` -- tricorder, cryonics
- `biology-and-ecology` -- terraforming, genetic engineering, the Jackpot
- `economics-and-finance` -- spice, space colonization
- `physics-and-engineering` -- zero-gravity, Dyson sphere, waldo
- `arts-and-culture` -- holodeck
- `organizational-behavior` -- Borg, generation ship
- `psychology` -- pod people
- `mathematics-and-logic` -- psychohistory

### Target frames

Most candidates target real-world domains, not a single shared frame:
- `governance` -- Big Brother, Newspeak, dystopia, prime directive, psychohistory
- `artificial-intelligence` -- Skynet, three laws, singularity, mentat, paperclip, replicant, uploading
- `computing` -- cyberspace, metaverse, holodeck, computer virus, ansible
- `ethics-and-morality` -- Frankenstein, brave new world
- `social-dynamics` -- Borg, pod people, hive mind, space colonization
- `ecology` -- terraforming, the Jackpot
- `tool-use` -- tricorder, waldo
- `philosophy` -- the Matrix, red pill, cryonics

## Gotchas

1. **This is a vein, not an archive.** The candidate list is a batch, not
   an exhaustive enumeration. The parent issue identifies potentially 50-100+
   mappings. Batch 1 covers 40 candidates; future batches should cover
   additional SF works and themes.

2. **No single "SF metaphors in real life" archive exists.** The SF
   Encyclopedia catalogs SF themes (fiction-internal taxonomy). Brave New
   Words catalogs SF terminology (etymology). But no structured archive
   specifically tracks the metaphorical transfer from SF to real-world
   discourse. This project sits at the intersection. The 35% LLM-sourced
   rate reflects this gap.

3. **Kind ambiguity.** Some candidates straddle `conceptual-metaphor`,
   `literary-frame`, and `cross-field-mapping`. The distinction: conceptual
   metaphors structure thinking (Big Brother), literary frames provide
   narrative structure (the Jackpot), and cross-field mappings named real
   things (ansible, waldo). The Miner should use judgment and document
   borderline cases.

4. **Overlap with active-ai-metaphors project.** Several candidates overlap
   with the AI metaphors vein (Skynet, three laws, singularity, paperclip
   maximizer, replicant, uploading, mentat). The SF project focuses on the
   *fictional origin* and *narrative structure* of the metaphor; the AI
   project focuses on *current AI discourse usage*. Miners should cross-link
   using `related:` but not duplicate entries. If an entry already exists
   from the AI project, the SF project should add related context, not
   create a duplicate.

5. **Dead metaphors are worth documenting.** Robot, computer virus, zero-g,
   grok, waldo, and deep space are now naturalized English. The interesting
   analysis is what hidden assumptions the original SF frame still carries.
   The "Where It Breaks" section should address the ghost of the metaphor.

6. **The Frankenstein problem.** Some candidates (Frankenstein, Big Brother,
   the Matrix) are so culturally pervasive that the "metaphor" is actually
   a cluster of related framings. The Miner should identify the *dominant*
   structural mapping rather than trying to cover every usage.

7. **40 candidates in batch 1.** Well within GitHub's 100 sub-issue limit.

## Future Batches

### Batch 2: Banks, Egan, and post-scarcity SF

Candidates to research from the parent issue:
- Banks's Culture (post-scarcity society as frame for UBI/abundance discourse)
- Banks's Minds (superintelligent AI governance)
- Banks's knife missiles (autonomous weapons)
- Egan's Permutation City cellular automata (recursive simulation)
- Egan's Diaspora orphanogenesis (mind-children without biological parents)
- Stephenson's Diamond Age Primer (adaptive AI tutor)
- Stephenson's Anathem concentric monasteries (layered isolation)

### Batch 3: Games, internet folklore, and collaborative mythology

Candidates to research:
- Battle royale / Hunger Games (competition framing)
- SCP Foundation (collaborative classification mythology)
- Backrooms (liminal digital spaces)
- Mirror life (synthetic biology risk)
- Gibson's black ice (lethal defensive security)

### Batch 4: Additional film/TV concepts

Candidates to research:
- Alien's chestbursters (parasitic emergence)
- Soylent Green (resource deception)
- Blade Runner's tears in rain (impermanence of artificial memory)
- Westworld's hosts (AI consciousness awakening)
- Ex Machina's Ava (gendered AI deception)
