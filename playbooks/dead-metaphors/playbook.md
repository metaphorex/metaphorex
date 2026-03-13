---
project_issue: 5
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Dead Metaphors Worth Resurrecting

## Source Description

Etymology dictionaries, historical linguistics research, and domain-specific
jargon catalogs documenting words and phrases that were once active metaphors
but have become literal through persistent use. This is a **vein** project:
dead metaphors are effectively infinite in number, so each batch focuses on
a coherent cluster.

**Batch 1** focuses on three clusters from the parent issue:

- **Software/tech dead metaphors** -- bug, patch, cookie, virus, spam, mouse,
  web, stream, cloud, daemon, kernel, shell, dashboard, troll, platform
- **Business dead metaphors** -- stakeholder, pipeline, silo, red tape, stock,
  brand, capital, bankrupt
- **Everyday dead metaphors with surprising origins** -- deadline, broadcast,
  salary, muscle, companion, window, running out of steam

## Access Method

### Primary Archives

1. **Wikipedia: List of computer term etymologies**
   https://en.wikipedia.org/wiki/List_of_computer_term_etymologies
   Structured table of 200+ computing terms with etymological origins.
   Primary source for identifying which tech terms have metaphorical roots.
   Scraped and filtered in `scripts/extract_dead_metaphors.py`.

2. **Etymonline (Douglas Harper's Online Etymology Dictionary)**
   https://www.etymonline.com/
   The standard reference for English word origins. Individual entries
   consulted for each candidate. Not bulk-scrapeable (no structured index
   of metaphorical terms), but individual URLs are stable and citeable.

3. **Examples.com: 99+ Dead Metaphor Examples**
   https://www.examples.com/english/dead-metaphors.html
   Enumerated list of 100 dead metaphors. Useful as a candidate discovery
   source, though most entries are idiomatic expressions rather than
   single-word dead metaphors with rich structural mappings.

4. **Gizmodo: The Mysterious Origins of 21 Tech Terms**
   https://gizmodo.com/the-mysterious-origins-of-21-tech-terms-1678246145
   Journalist-researched etymologies of tech terms. Provided the Engelbart
   mouse/CAT story and the Monty Python spam connection.

5. **Mapping Metaphor with the Historical Thesaurus (University of Glasgow)**
   https://mappingmetaphor.arts.gla.ac.uk/
   Academic resource mapping 14,000+ metaphorical connections in English
   across all recorded history. Interactive web tool, no bulk download
   available. Useful for validating whether a metaphor is attested
   historically, but not directly scrapeable for candidate lists.
   The Glasgow project covers ALL metaphorical connections (not just dead
   ones), so filtering is manual.

### Scraping Script

`scripts/extract_dead_metaphors.py` encodes structured data from the
Wikipedia and Etymonline archives as static datasets (Wikipedia returns
403 on programmatic access, Etymonline has no bulk API). The script
combines three curated source datasets:

- **Wikipedia computer term etymologies** (15 entries): filtered to terms
  with metaphorical origins from non-computing domains
- **Everyday dead metaphors** (14 entries): terms with surprising
  etymological origins, sourced from Etymonline and Examples.com
- **Business dead metaphors** (5 entries): organizational/financial terms
  with hidden physical origins

The script outputs JSON to stdout and is idempotent.

### LLM Gap-Fill

0 of 30 candidates are LLM-sourced. All candidates trace to archive sources
(Wikipedia computer term etymologies, Etymonline, Examples.com, Gizmodo).
The descriptions synthesize information from multiple archive sources but
do not introduce candidates that lack archival attestation.

## Extraction Strategy

### What makes a good candidate for this project

A dead metaphor worth resurrecting must satisfy three criteria:

1. **The metaphor is genuinely dead** -- most speakers use the term without
   awareness of its metaphorical origin. "Bottleneck" qualifies; "heart of
   the matter" does not (most people still sense the body metaphor).

2. **The original mapping has structural richness** -- knowing the origin
   changes how you think about the modern term. "Deadline" (prison kill line)
   transforms a mundane work term into something with real weight. "Cyber"
   (Greek for steering) does not add much insight.

3. **The structural parallels or divergences are interesting** -- the
   original metaphor either maps surprisingly well onto the modern meaning
   (virus, cookie) or reveals hidden assumptions the modern usage smuggles
   in (dashboard, silo, brand).

### What to avoid

- **Idioms without structural depth** -- "kick the bucket," "break a leg,"
  "piece of cake." These are dead metaphors but they don't carry structural
  mappings worth analyzing. They're just expressions.
- **Terms where etymology is well-known** -- if most educated speakers know
  the origin, the metaphor isn't dead enough to be interesting to resurrect.
- **Terms already in the catalog** -- 38 dead-metaphor entries already exist
  (mostly from the sw-eng-vernacular and unix-c-metaphors projects). Check
  `catalog/mappings/` before adding candidates.

### Prioritization (Batch 1)

- **Tier 1 (richest structural mappings):** virus, deadline, brand, cloud,
  daemon, kernel-shell (as a pair), stakeholder, silo
- **Tier 2 (solid with good breaks):** bug, patch, cookie, web, broadcast,
  dashboard, pipeline, capital, bankrupt
- **Tier 3 (thinner but worth documenting):** spam, mouse, stream, troll,
  salary, muscle, companion, window, stock, platform, red-tape,
  running-out-of-steam

### Kind assignments

All candidates are `dead-metaphor`. This project does not produce
`conceptual-metaphor` entries (those go to other import projects like
cognitive-linguistics-canon). The distinction: a dead-metaphor entry focuses
on etymology, the original live mapping, and what was lost/preserved when
the metaphor died. A conceptual-metaphor entry focuses on the active
structural mapping in current cognition.

### Distinguishing from existing entries

38 dead-metaphor entries already exist in the catalog, primarily from the
sw-eng-vernacular and unix-c-metaphors projects. These cover:
- Software engineering vernacular: spaghetti-code, technical-debt, code-smell, etc.
- Unix/C metaphors: unix-pipe, filesystem-tree, stdin-stdout-stderr, etc.
- Recently added: firewall, bottleneck, jailbreaking, guardrails

This batch focuses on terms NOT yet covered and emphasizes the etymological
resurrection angle rather than the software engineering usage angle.

Also check `leverage` (exists as `kind: paradigm`) -- excluded from this
batch to avoid overlap.

## Schema Mapping

### New frames needed

None. All source frames for this batch already exist in `catalog/frames/`.

### Existing frames that will be reused

- `organism` -- bug (creatures infesting systems)
- `food-and-cooking` -- cookie, spam, companion
- `medicine` -- virus
- `animal-behavior` -- mouse, muscle, web
- `fluid-dynamics` -- stream, pipeline
- `natural-phenomena` -- cloud
- `mythology` -- daemon, troll
- `horticulture` -- kernel, shell, broadcast, silo
- `war` -- deadline
- `travel` -- dashboard
- `embodied-experience` -- window, running-out-of-steam
- `architecture-and-building` -- platform, bankrupt, window
- `animal-husbandry` -- brand, capital
- `gambling` -- stakeholder
- `materials` -- stock, red-tape, salary (Latin sal = salt, a physical commodity)
- `physics` -- running-out-of-steam
- `textiles` -- patch

### Target frames that will be reused

- `software-programs` -- bug, patch
- `computing` -- cookie, virus, spam, mouse, web, stream, cloud, daemon,
  kernel, shell, dashboard, troll, platform
- `time-and-temporality` -- deadline
- `communication` -- broadcast
- `economics` -- salary, bankrupt, capital, stock, brand
- `governance` -- stakeholder, silo, red-tape
- `systems-performance` -- pipeline
- `social-behavior` -- companion
- `embodied-experience` -- muscle, running-out-of-steam
- `architecture-and-building` -- window

### New categories needed

None. The existing `linguistics` category covers etymology-focused entries.

### Existing categories that will be reused

- `linguistics` -- all entries (etymological focus)
- `software-engineering` -- tech dead metaphors
- `organizational-behavior` -- business dead metaphors
- `security` -- virus
- `systems-thinking` -- cloud, platform
- `cognitive-science` -- muscle
- `social-dynamics` -- companion, troll

## Gotchas

1. **This is a vein, not an archive.** Dead metaphors are effectively
   infinite. Batch 1 covers the most structurally interesting candidates
   across the three clusters defined in the issue. Future batches should
   cover: medical dead metaphors (diagnosis, symptom, patient), legal dead
   metaphors (court, verdict, attorney), nautical dead metaphors (navigate,
   fathom, leeway), and body-part dead metaphors (head of department,
   arm of the law, foot of the mountain).

2. **No single canonical archive of dead metaphors exists.** Unlike the
   Lakoff/Johnson project (which has the Osaka and Berkeley archives), dead
   metaphor cataloging is distributed across etymology dictionaries, blog
   posts, and linguistics papers. The Glasgow Mapping Metaphor project is
   the most comprehensive academic resource but covers all metaphors (not
   just dead ones) and lacks a bulk-download dataset.

3. **The "Where It Breaks" section is unusual for dead metaphors.** For
   active metaphors, "breaks" means structural limits of the mapping. For
   dead metaphors, "breaks" should focus on: (a) what was lost when the
   metaphor died, (b) what hidden assumptions the dead metaphor still
   smuggles into modern thinking, and (c) what happens when you resurrect
   the original mapping and take it seriously.

4. **Origin Story section is mandatory for dead metaphors.** Unlike other
   mapping kinds where Origin Story is optional, dead-metaphor entries MUST
   have a detailed Origin Story section documenting the etymological chain.
   This is the core value of the entry.

5. **Kernel and shell are a complementary pair.** The Miner should create
   both entries and link them with `related:`. The botanical metaphor system
   (kernel = seed, shell = covering) is internally consistent and should be
   documented as such.

6. **Salary etymology is contested.** The "Romans paid in salt" story is
   widely repeated but lacks strong attestation in ancient sources. The Miner
   should note the controversy rather than repeating the folk etymology
   uncritically. Cite the Kiwi Hellenist blog post debunking the literal
   salt-payment interpretation.

7. **30 candidates in batch 1.** Well within GitHub's 100 sub-issue limit.

## Future Batches

### Batch 2: Nautical and navigation dead metaphors

Candidates to research:
- Navigate (Latin navis + agere -- to drive a ship)
- Fathom (Old English faethm -- outstretched arms, a depth measurement)
- Leeway (slack distance a ship drifts downwind)
- Overwhelm (Middle English -- to capsize, turn upside down)
- Aloof (Dutch te loef -- to windward, keeping distance from shore)
- By and large (sailing terms: by the wind and on a large tack)
- Flagship (admiral's ship, now a company's premier product)
- In the offing (visible from shore but not yet arrived)

### Batch 3: Medical and legal dead metaphors

Candidates to research:
- Diagnosis (Greek -- to know apart, to distinguish)
- Symptom (Greek -- to fall together, coincidence)
- Verdict (Latin vere dictum -- truly spoken)
- Attorney (Old French atorner -- to appoint, turn toward)
- Mortgage (Old French mort + gage -- death pledge)
- Quarantine (Italian quarantina -- forty days of isolation for ships)

### Batch 4: Body-part dead metaphors

Candidates to research:
- Head (of department, of state, of table)
- Arm (of the law, of a chair, of a river)
- Foot (of a mountain, of a page, of a bed)
- Bottleneck expansion: neck (of the woods, of a guitar)
- Eye (of a storm, of a needle, of a potato)
- Mouth (of a river, of a cave)
