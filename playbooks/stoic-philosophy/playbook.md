---
project_issue: 2390
repo: metaphorex/metaphorex
source_type: corpus
status: draft
---

# Playbook: Stoic Philosophy -- Marcus Aurelius and the Stoics

## Source Description

The Stoic philosophical tradition (c. 300 BCE -- 180 CE), focusing on
the three principal Roman-era Stoics whose works survive intact:

- **Epictetus** (c. 50--135 CE) -- *Discourses* (4 surviving books of 8),
  *Enchiridion* (handbook). Former slave, professional teacher. Most
  systematic use of metaphor as pedagogical tool.
- **Seneca** (c. 4 BCE -- 65 CE) -- *Epistulae Morales* (124 letters),
  *De Ira*, *De Brevitate Vitae*, *De Tranquillitate Animi*, other
  dialogues. Roman senator, rhetorician. Most literary, most extended
  metaphors.
- **Marcus Aurelius** (121--180 CE) -- *Meditations* (12 books). Roman
  emperor, private journal. Most compressed, most imagistic. Not
  intended for publication.

Earlier Stoics (Zeno, Cleanthes, Chrysippus) survive only in fragments
and doxography; their metaphors are included where reliably attributed.

### Why this matters for the catalog

Stoic philosophy is one of the richest surviving sources of load-bearing
metaphors and mental models in Western thought. The Stoics did not use
metaphors as decoration -- they used them as *spiritual exercises*
(Hadot's term), cognitive tools for restructuring judgment. Many Stoic
metaphors have entered modern discourse (CBT, ACT, resilience training,
productivity culture) with their structural depth stripped out. The
catalog should recover the structural content.

This is a **vein** project. The Stoic corpus is finite but the tradition
of commentary and interpretation is ongoing. This batch covers the
primary metaphors, mental models, and paradigms from the surviving
texts. Future batches could target: Stoic physics metaphors, Stoic logic
metaphors, specific Senecan letter clusters, or modern Stoic adaptations.

### Estimated yield: 15 candidates (this batch)

## Access Method

### Archive Assessment

**No single structured archive exists for Stoic metaphors.** Unlike the
cognitive linguistics canon (which has the Osaka archive and Master
Metaphor List), Stoic metaphorical imagery has not been exhaustively
cataloged in a machine-readable format.

### Reference Sources Used

1. **Jan Garrett, "Metaphorical Structure of Epictetus' Encheiridion"**
   URL: https://people.wku.edu/jan.garrett/stoa/metepict.htm
   Academic analysis identifying 5+ systematic metaphors in the
   Enchiridion. Used to verify Epictetus metaphor candidates.

2. **Donald Robertson, "Stoicism as a Ball Game"**
   URL: https://donaldrobertson.name/2019/10/29/stoicism-as-a-ball-game/
   Identifies the Chrysippean ball game metaphor and its extensions in
   Epictetus and Seneca. Used to verify the ball-game candidate.

3. **Daily Stoic Glossary**
   URL: https://dailystoic.com/glossary/
   64 Stoic technical terms with explanations. Used to identify
   concept-candidates and distinguish metaphors from bare concepts.

4. **Stanford Encyclopedia of Philosophy: Marcus Aurelius**
   URL: https://plato.stanford.edu/entries/marcus-aurelius/
   Academic overview with discussion of Aurelius' use of imagery.

5. **Pierre Hadot, *The Inner Citadel* (1998)**
   Book-length analysis of Marcus Aurelius' Meditations as spiritual
   exercises. Identifies the three disciplines (desire, action, judgment)
   and maps Marcus' imagery onto them.

6. **Primary texts** (public domain):
   - Epictetus, *Enchiridion*: https://classics.mit.edu/Epictetus/epicench.html
   - Marcus Aurelius, *Meditations* (various translations available)
   - Seneca, *Dialogues*: https://standardebooks.org/ebooks/seneca/dialogues/aubrey-stewart

### Methodology

This candidate list is **LLM-sourced with academic reference
verification**. No scraping script was written because no structured
archive exists to scrape. Each candidate was cross-referenced against
at least one of the reference sources above and/or the primary texts.

## Extraction Strategy

### Candidate Selection Criteria

Each candidate must satisfy ALL of:

1. **Has a source frame** -- a concrete domain (wrestling, theater,
   fortification, navigation, medicine, fire, etc.) that maps
   structurally onto a philosophical target
2. **Transfers structurally** -- the mapping is not just an illustration
   but carries inferential structure: if you reason about the source
   domain, you learn something about the target
3. **Has limits** -- the mapping breaks somewhere interesting, and the
   Stoics either noticed or should have
4. **Appears in primary texts** -- not a modern invention attributed to
   the Stoics

### What was excluded

- **Bare concepts without metaphorical structure** -- *apatheia*,
  *eudaimonia*, *arete* are important Stoic concepts but they are not
  metaphors. They lack a source frame.
- **Single-use literary comparisons** -- Marcus Aurelius uses hundreds
  of brief similes. Only those that carry structural weight (multiple
  entailments, reusable framing) are included.
- **Modern reinterpretations** -- Ryan Holiday's formulations are
  included only when they preserve or illuminate the original structure.

## Schema Mapping

| Stoic source | Catalog field | Notes |
|---|---|---|
| Metaphor name (English) | `name` | Capitalized English form |
| Kebab-case slug | `slug` | Derived from English name |
| metaphor / mental-model / paradigm | `kind` | See per-candidate notes |
| Concrete source domain | `source_frame` | Wrestling, theater, navigation, etc. |
| Target domain | `applies_to` | Philosophy, ethics, psychology, etc. |
| `philosophy` | `categories` | All entries get `philosophy` |
| Primary text citation | Origin Story section | Book/letter/chapter reference |
| `folk` or `established` | `grounding` | Most get `established` -- these are canonical |

### Frame requirements

New frames likely needed:
- `athletics-and-combat` (for wrestling, pankration metaphors)
- `banqueting` (for the feast/banquet metaphor)
- `dice-and-games` (for the dice game metaphor)
- `archery` (for the archer metaphor)

Existing frames that apply:
- `animal-husbandry` (dog-tied-to-cart -- already used)
- `theater-and-performance` (life-is-a-play -- already used)
- `fortification` (mind-is-a-citadel -- already used)
- `philosophy` (paradigm entries)
- `navigation` (helmsman/voyage metaphors)
- `medicine-and-healing` (philosophy-as-medicine)

## Gotchas

1. **Overlapping entries** -- Several Stoic metaphors cluster around the
   same insight (amor fati, obstacle-is-the-way, dog-tied-to-cart all
   address acceptance of fate). The Miner must articulate what makes each
   structurally distinct, not just thematically related.

2. **Attribution uncertainty** -- Many metaphors are attributed to early
   Stoics (Zeno, Cleanthes, Chrysippus) but survive only through later
   authors. The Miner should cite the surviving text, not the attributed
   originator, as the primary reference.

3. **Kind classification** -- The line between `metaphor` (has source
   frame) and `mental-model` (framework for thinking) is blurry for some
   Stoic concepts. Rule of thumb: if the entry's power comes from its
   *imagery* (the wrestling ring, the citadel, the dog and cart), it is a
   metaphor. If its power comes from its *framework* (dichotomy of
   control, negative visualization), it is a mental-model.

4. **10 entries already exist** -- See the "Already Mined" section in the
   manifest for the complete list. The Miner must not duplicate these.

5. **Candidate count (15) is well under the 100 sub-issue cap** -- no
   overflow handling needed.
