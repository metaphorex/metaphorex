---
project_issue: 1227
repo: metaphorex/metaphorex
source_type: book
status: draft
---

# Playbook: Broom's Legal Maxims -- Load-Bearing Principles of Law

## Source Description

Herbert Broom, *A Selection of Legal Maxims, Classified and Illustrated*
(first published 1845, 10th edition available on Archive.org). The
definitive English-language compilation of legal maxims, organized into
chapters by domain: public policy, the crown, judicial administration,
logic, fundamental principles, property, contracts, evidence, etc.

Supplementary sources:
- Peter Halkerston, *A Collection of Latin Maxims & Rules* (1823;
  Project Gutenberg #72240)
- John N. Cotterell, *A Collection of Latin Maxims and Phrases* (1858;
  Project Gutenberg #68465)
- WritingLaw.com, "Top 235 Legal Maxims with Meaning" (modern web reference)

The combined archives contain 300+ maxims. The vast majority are
domain-specific legal rules with no metaphorical migration beyond law.
This project imports only the 25 maxims that encode structural reasoning
patterns applicable outside legal practice, or that have genuinely entered
non-legal discourse as conceptual metaphors.

## Access Method

### Primary Archives

1. **Broom full text (Archive.org):**
   https://archive.org/stream/aselectionlegal00cagngoog/aselectionlegal00cagngoog_djvu.txt

2. **Cotterell (Gutenberg #68465):**
   https://www.gutenberg.org/files/68465/68465-h/68465-h.htm

3. **Halkerston (Gutenberg #72240):**
   https://www.gutenberg.org/cache/epub/72240/pg72240-images.html

4. **WritingLaw.com (235 maxims):**
   https://www.writinglaw.com/important-legal-maxims-and-phrases/

### Archive Methodology

The Gutenberg HTML texts were fetched and parsed to extract the complete
maxim inventory. The scraping script at `scripts/extract_cotterell_maxims.py`
extracts Latin/English pairs from both Gutenberg sources.

The candidate selection was then performed by cross-referencing the full
archive against three filters:

1. **Cross-domain applicability:** Does this maxim encode a reasoning
   pattern that people apply outside of legal contexts? "Caveat emptor"
   passes (applied to hiring, technology adoption, information consumption).
   "Haereditas nunquam ascendit" fails (inheritance-specific).

2. **Linguistic migration:** Has the Latin phrase or its English equivalent
   entered everyday discourse? "Res ipsa loquitur" passes (people say "the
   thing speaks for itself"). "Qui prior est tempore potior est jure" fails
   (no common English equivalent in non-legal speech).

3. **Structural insight density:** Does the maxim encode a non-obvious
   structural principle that illuminates how rule-systems, authority, or
   fairness work? "Nemo judex in causa sua" passes (self-assessment is
   inherently unreliable). "Dies Dominicus non est juridicus" fails
   (calendar rule, no structural insight).

### Cross-Reference Sources

For maxims that have entered common usage, the following sources were
consulted for origin and migration history:

- Wikipedia articles on individual maxims (e.g., "Fruit of the poisonous
  tree," "Hard cases make bad law," "Possession is nine-tenths of the law")
- Merriam-Webster definitions for English equivalents
- Britannica "Legal maxim" entry
- Volokh, "The Mechanisms of the Slippery Slope," *Harvard Law Review*
  (2003) -- cited in the import issue

## Extraction Strategy

### For Miners

Each candidate in the manifest has:
- `slug`: the filename for `catalog/mappings/{slug}.md`
- `name`: the formal name (Latin where canonical, English where the
  English form is more widely known)
- `kind`: `conceptual-metaphor` or `dead-metaphor`
- `source_frame` and `target_frame`: which frames to use
- `broom_chapter`: which chapter of Broom (for origin context)
- `latin`: the Latin text (for maxims that have one)
- `description`: the structural insight and cross-domain application

**Miner workflow:**

1. Fetch the Broom full text from Archive.org to find the chapter
   discussion of each maxim. Broom provides extensive case law
   illustrations -- use these for the Origin Story section.
2. Research the maxim's migration into non-legal discourse. The mapping
   body should emphasize the structural reasoning pattern, not the legal
   technicalities.
3. For "What It Brings": focus on the reasoning pattern the maxim
   encodes and where it transfers productively to non-legal domains.
4. For "Where It Breaks": identify where the legal metaphor fails in
   its transferred context. Legal reasoning has specific structural
   properties (adversarial process, burden of proof, precedent) that
   do not always transfer. Flag where the metaphor imports false
   precision or false formality.
5. For "Expressions": list both the Latin phrase and its common English
   equivalents, plus examples of non-legal usage.

### Batching Recommendation

Process by reasoning-pattern cluster:

- **Batch 1 -- Fairness principles (5):** no-one-should-judge-their-own-case,
  hear-the-other-side, come-with-clean-hands, the-willing-suffer-no-injury,
  no-one-profits-from-their-own-wrong. These share a structural concern
  with procedural fairness.

- **Batch 2 -- Rule-system design (5):** the-law-does-not-concern-itself-with-trifles,
  hard-cases-make-bad-law, necessity-knows-no-law, the-law-is-harsh-but-it-is-the-law,
  no-one-is-bound-to-the-impossible. These encode principles about how
  rule-systems should work.

- **Batch 3 -- Responsibility and agency (4):** he-who-acts-through-another-acts-himself,
  let-the-master-answer, silence-gives-consent, use-your-own-so-as-not-to-harm-another.
  These address when and how responsibility attaches to actors.

- **Batch 4 -- Evidence and reasoning (4):** the-thing-speaks-for-itself,
  fruit-of-the-poisonous-tree, false-in-one-thing-false-in-all,
  the-exception-proves-the-rule. These encode principles about
  evaluating evidence and inference.

- **Batch 5 -- Rights and obligations (4):** ignorance-of-the-law-is-no-excuse,
  where-there-is-a-right-there-is-a-remedy, let-the-buyer-beware,
  no-one-gives-what-they-do-not-have. These address the structural
  relationship between rights, knowledge, and obligations.

- **Batch 6 -- Principles of justice (3):** let-justice-be-done-though-the-heavens-fall,
  letter-vs-spirit-of-the-law, possession-is-nine-tenths-of-the-law.
  These encode deep structural tensions in justice systems.

## Schema Mapping

### Kind Assignment

| Category | Kind | Count | Criteria |
|----------|------|-------|----------|
| Active metaphors | `conceptual-metaphor` | 23 | Latin maxims that actively structure reasoning in non-legal contexts |
| Dead metaphors | `dead-metaphor` | 2 | So embedded in everyday language that their legal origin is forgotten (possession is nine-tenths, the exception proves the rule) |

### Frame Inventory

**Existing frames (reusable):**
- `governance` -- primary source frame for most maxims (legal reasoning
  as a source domain)
- `economics` -- source frame for commercial maxims (caveat emptor,
  nemo dat)
- `ethics-and-morality` -- primary target frame for fairness/justice maxims
- `decision-making` -- target frame for procedural maxims
- `causal-reasoning` -- target frame for evidence/inference maxims
- `social-behavior` -- target frame for responsibility maxims
- `purity` -- source frame for clean hands doctrine
- `horticulture` -- source frame for fruit of the poisonous tree
- `language` -- source frame for letter vs. spirit

**No new frames needed.** The existing frame inventory covers all source
and target domains.

### Categories

All entries get `law-and-governance` as primary category. Additional:
- Fairness principles: `ethics-and-morality`
- Rule-system design: `systems-thinking` or `philosophy`
- Responsibility: `organizational-behavior`
- Evidence: (no additional)
- Justice principles: `philosophy`

### Author and Provenance

- `author: agent:metaphorex-miner`
- `provenance: brooms-legal-maxims`

## Gotchas

1. **Latin vs. English naming:** Some maxims are universally known by
   their Latin names (caveat emptor, res ipsa loquitur). Others are
   known only in English (hard cases make bad law, possession is
   nine-tenths). The manifest uses the more recognizable form as the
   `name`. Miners should include both forms in the body text.

2. **Legal precision vs. metaphorical usage:** Many of these maxims
   have precise legal meanings that differ from their popular usage.
   "The exception proves the rule" is the canonical example -- the
   legal meaning (the exception tests the rule) is opposite to the
   popular meaning (the exception confirms the rule). Miners should
   document this divergence in "Where It Breaks."

3. **Overlapping maxims:** Several candidates encode related principles.
   "Qui facit per alium" and "respondeat superior" both address
   vicarious liability. "Necessity knows no law" and "the law does not
   compel the impossible" both address the limits of rules. Miners
   should use `related:` links and distinguish the structural insight
   each one contributes.

4. **Not a Broom-only project:** Despite the name, this project draws
   from three Gutenberg texts plus modern references. "Fruit of the
   poisonous tree" is a 1939 American doctrine not in Broom at all.
   The project title reflects the most prominent source, but miners
   should cite the actual origin of each maxim.

5. **Some candidates are English, not Latin:** "Hard cases make bad
   law," "possession is nine-tenths," "clean hands," and "fruit of
   the poisonous tree" are English-language legal principles, not
   Latin maxims. They appear in Broom's tradition but not in the
   Latin maxim compilations.

6. **25 candidates is within the 100 sub-issue cap.** No overflow
   handling needed.
