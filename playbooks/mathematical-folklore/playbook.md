---
project_issue: 1356
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Mathematical Folklore -- Spherical Cows, Proof Strategies, and Named Paradoxes

## Source Description

**Mathematical folklore** is the oral and written tradition of named paradoxes,
proof strategies, aphorisms, and humorous heuristics that circulate among
mathematicians. Unlike formal mathematical results, folklore emphasizes
how mathematicians think, argue, and fail -- making it unusually rich in
metaphorical structure.

This project draws from four overlapping sub-sources:

1. **Named paradoxes** (Hilbert's Hotel, Banach-Tarski, Zeno's Paradox,
   Russell's Paradox, Simpson's Paradox, Birthday Paradox, Monty Hall)
2. **Informal proof strategies** (proof by intimidation, proof by handwaving,
   proof by exhaustion, reductio ad absurdum, proof by construction)
3. **Mathematical aphorisms** ("shut up and calculate," "consider a spherical
   cow," "a mathematician is a machine for turning coffee into theorems")
4. **Foundational impossibility results used as metaphors** (Goedel's
   Incompleteness, Arrow's Impossibility, the Halting Problem, No Free Lunch)

## Access Method

**Primary archive sources (scraped or referenced):**

- Illinois CS proof techniques archive:
  https://mfleck.cs.illinois.edu/proof.html
  Scraped by `scripts/extract_proof_techniques.py` -- yielded 33 named
  humorous proof techniques. Most are too thin individually but several
  (proof by intimidation, proof by handwaving, proof by exhaustion) have
  genuine cross-domain metaphorical depth.

- Northwestern CS proof techniques mirror:
  https://users.cs.northwestern.edu/~riesbeck/proofs.html
  Cross-referenced by the same script for additional techniques.

- Science Jokes proof methods archive:
  https://jcdverha.home.xs4all.nl/scijokes/9_7.html
  Additional humorous proof methods including Zemanian's collection.

- Wikipedia structured lists:
  - https://en.wikipedia.org/wiki/Mathematical_folklore
  - https://en.wikipedia.org/wiki/List_of_paradoxes
  - https://en.wikipedia.org/wiki/Spherical_cow
  - https://en.wikipedia.org/wiki/Proof_by_intimidation

- AMS Notices (Renteln & Dundes, 2005):
  https://www.ams.org/notices/200501/fea-dundes.pdf
  "Foolproof: A Sampling of Mathematical Folk Humor" -- comprehensive
  academic catalog of mathematical folklore. Referenced for completeness
  verification but not scraped (PDF, mostly jokes rather than entries).

- Krantz, Steven G. *Mathematical Apocrypha* (2002) and *Redux* (2005):
  Book-length collections. Referenced for completeness but not scraped.

**LLM gap-fill:** 11 of 28 candidates are LLM-sourced. These are
well-known mathematical concepts whose metaphorical use is broadly
documented but not enumerated in a single scrapable archive. The Surveyor
should verify these are real and not hallucinated (they are all standard
mathematical results with Wikipedia articles).

## Extraction Strategy

The archive source (Illinois CS proof techniques) provided 33 raw entries.
Of these, only 4 were selected as standalone candidates (proof by
intimidation, proof by handwaving, proof by exhaustion, proof by
construction). The remaining 29 are too thin -- they describe one-liner
joke techniques (proof by funding, proof by cosmology) that lack the
structural depth for a full Metaphorex entry with meaningful Transfers
and Limits sections.

Named paradoxes and foundational results were identified from the Wikipedia
List of Paradoxes and filtered by a strict criterion: **the concept must
have documented metaphorical use outside mathematics.** Purely internal
mathematical results (Cantor's diagonal argument, the axiom of choice)
were excluded unless they have a named folk form (Banach-Tarski, Hilbert's
Hotel) that circulates as a metaphor.

**Selection criteria:**

1. **Cross-domain portability**: Has the concept been used as a metaphor,
   mental model, or reasoning tool outside pure mathematics?
2. **Structural depth**: Can you write substantive Transfers AND Limits
   sections? A concept that is just "surprising fact" without structural
   mapping to other domains is too thin.
3. **Not already in catalog**: Entries for `occams-razor`, `hanlons-razor`,
   `bayesian-updating`, `regression-to-the-mean`, `the-commons` (frame),
   and `the-map-is-not-the-territory` already exist. These are excluded
   from this manifest.
4. **Named and recognizable**: The concept should have a standard name
   that practitioners in other fields would recognize.

## Schema Mapping

| Source field | Metaphorex field | Notes |
|-------------|-----------------|-------|
| Paradox/concept name | `name` | Use the common folk name |
| Slugified name | `slug` | kebab-case |
| Origin domain | `source_frame` | mathematical-proof, probability, set-theory, etc. |
| Application domain | `target_frame` | argumentation, decision-making, epistemology, etc. |
| -- | `kind` | metaphor, paradigm, or mental-model based on structure |
| -- | `categories` | Always includes `mathematics-and-logic` |
| -- | `author` | `agent:metaphorex-miner` |
| -- | `provenance` | `mathematical-folklore` |

**Kind assignment rules:**
- `metaphor`: Source-to-target structural mapping (spherical cow, butterfly
  effect, drunkard's walk, coffee-into-theorems)
- `paradigm`: Named reasoning structure or impossibility result that
  reframes how you think about a class of problems (reductio ad absurdum,
  Goedel's incompleteness, Arrow's impossibility, prisoner's dilemma)
- `mental-model`: Named cognitive tool for estimation or intuition
  calibration (birthday paradox, gambler's fallacy, ninety-ninety rule)

**Frame creation:** The Miner will need to create several new frames:
- `mathematical-proof` (roles: axioms, theorem, proof-strategy, rigor)
- `mathematical-modeling` (roles: model, assumptions, simplifications, predictions)
- `probability` (roles: sample-space, events, likelihood, independence)
- `set-theory` (roles: sets, elements, membership, cardinality)
- `game-theory` (roles: players, strategies, payoffs, equilibria)
- `computability-theory` (roles: programs, inputs, decidability, halting)
- `mathematical-logic` (roles: axioms, theorems, consistency, completeness)
- `dynamical-systems` (roles: state, trajectory, attractor, sensitivity)
- `mathematical-optimization` (roles: objective, constraints, search-space, optima)
- `mathematical-practice` (roles: conjecture, proof, collaboration, rigor)
- `mathematical-estimation` (roles: estimate, actual, error, bias)
- `mathematical-reasoning` (roles: premises, inference, conclusion, validity)
- `statistics` (roles: data, aggregation, confounders, correlation)

Some of these may already exist or overlap with existing frames. The Miner
should check and reuse existing frames where appropriate.

## Gotchas

1. **Overlap with existing entries.** `occams-razor`, `hanlons-razor`,
   `bayesian-updating`, `regression-to-the-mean`, and `the-map-is-not-the-territory`
   already exist in the catalog. The manifest excludes these. `tragedy-of-the-commons`
   is included as a candidate but `the-commons` already exists as a frame --
   the Miner should check whether a full entry already covers this ground.
   `borges-map` should explicitly link to `the-map-is-not-the-territory` and
   differentiate itself (model fidelity continuum vs. map/territory distinction).

2. **Proof technique granularity.** The archive yielded 33 humorous proof
   techniques. Only 4 are included as standalone entries. The rejected ones
   (proof by funding, proof by cosmology, proof by ghost reference, etc.)
   could be mentioned in the Expressions section of `proof-by-intimidation`
   or `proof-by-handwaving` as variants of the same folk tradition.

3. **"Shut up and calculate" attribution.** Often misattributed to Feynman.
   Actually coined by N. David Mermin in 1989 as a gloss on the Copenhagen
   interpretation. The Miner should get the attribution right.

4. **"Coffee into theorems" attribution.** Often misattributed to Paul
   Erdos. Actually Alfred Renyi. Erdos is credited with the corollary:
   "a comathematician is a machine for turning theorems into coffee."

5. **Goedel's Incompleteness is routinely misapplied.** The Limits section
   for this entry is critical. Popular invocations ("every system has blind
   spots") dramatically overextend the actual theorem, which applies only to
   formal systems powerful enough to express arithmetic. The Miner should
   resist the temptation to make the Transfers section too broad.

6. **Candidate count (28) is well under the 100 sub-issue cap.** No overflow
   handling needed.

7. **Mixed source reliability.** 17 candidates are archive-sourced (from
   scraped structured pages or Wikipedia), 11 are LLM-sourced. All LLM-sourced
   candidates are standard mathematical concepts with extensive documentation.
   The Surveyor should still verify them against Wikipedia or similar references.
