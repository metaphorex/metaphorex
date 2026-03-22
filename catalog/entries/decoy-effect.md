---
slug: decoy-effect
name: Decoy Effect
kind: mental-model
categories:
  - decision-making
  - psychology
  - economics-and-finance
author: agent:metaphorex-miner
contributors: []
related:
  - anchoring-effect
  - framing-effect
  - loss-aversion
created: '2026-03-21'
updated: '2026-03-22'
grounding: proven
harness: Claude Code
embodied_patterns:
  - attraction
  - scale
  - matching
relation_types:
  - cause/compel
  - transform/reframing
structure: competition
abstraction_level: generic
transfers:
  - '[law] introducing an asymmetrically dominated option shifts preference toward the option that dominates it, without being chosen itself'
  - '[law] the decoy works by creating a local comparison that makes the target option look decisively better along at least one dimension'
  - '[law] preferences between two options are not fixed properties but contextual -- they change when the choice set changes'
limits:
  - '[law] breaks when decision-makers are experienced or highly motivated to optimize, as expertise reduces susceptibility to context-dependent preference shifts'
  - '[law] misleads by implying that all third options function as decoys, when many genuinely expand the choice set rather than distorting it'
---

## Transfers

The decoy effect (also called the asymmetric dominance effect or the
attraction effect) describes how introducing a third option that is
clearly inferior to one of two existing options -- but not clearly
inferior to the other -- shifts preference toward the option that
dominates the decoy. The decoy is never chosen; its function is to
reframe the comparison.

Key structural parallels:

- **Asymmetric dominance** -- the decoy is worse than option A on all
  relevant dimensions (A dominates the decoy) but is only worse than
  option B on some dimensions. This asymmetry creates a local comparison
  that makes A look like a clear winner -- against the decoy. The
  decisiveness of that local victory bleeds into the overall evaluation.
  A feels like the "obviously better choice" even though the decoy was
  never a real contender.
- **Context-dependent preference** -- the effect demonstrates that
  preferences between A and B are not fixed. They change when the choice
  set changes. This violates the "independence of irrelevant alternatives"
  axiom in rational choice theory: a truly irrelevant option should not
  affect the ranking of relevant ones. The decoy effect shows that
  "irrelevant" options are structurally relevant as reference points.
- **The decoy as framing device** -- the decoy doesn't add information;
  it adds *structure*. It creates a dimension along which one option is
  unambiguously better, and humans preferentially evaluate along
  dimensions where comparison is easy. The decoy manufactures an easy
  comparison where none existed.
- **Pricing architecture** -- the most commercially important application.
  A $5 small coffee, a $6.50 large coffee, and a $6 medium-that's-almost-
  as-small-as-the-small: the medium is the decoy, making the large look
  like an obvious bargain. The three-tier pricing model used across SaaS,
  publishing, and retail is often designed with the middle tier as a decoy
  to push buyers toward the highest tier.

## Limits

- **Expertise reduces susceptibility** -- experienced decision-makers
  with clear criteria are less affected by decoys. A procurement officer
  with a scoring rubric evaluates options independently; the decoy adds
  a row to the spreadsheet but doesn't change the math. The effect is
  strongest when preferences are vague and comparison is difficult --
  precisely the conditions the decoy exploits.
- **Not all third options are decoys** -- the model can lead analysts
  to see manipulation where there is none. A company offering three
  genuinely differentiated products is not necessarily deploying a decoy.
  The model's analytical power comes with a paranoia risk: seeing every
  choice architecture as a trap.
- **The effect is fragile under scrutiny** -- when subjects are told about
  the decoy effect, it partially disappears. Awareness is a partial
  antidote. This limits the model's predictive power in contexts where
  decision-makers are sophisticated about behavioral economics.
- **Direction of the shift depends on decoy placement** -- small changes
  in how the decoy is positioned relative to the two main options can
  reverse the effect or create a "compromise effect" instead (preference
  for the middle option). The model is structurally precise but
  practically sensitive to implementation details.
- **Cultural and individual variation** -- the effect is well-replicated
  in Western laboratory settings with consumer goods. Its robustness
  across cultures, high-stakes decisions, and group decision-making
  contexts is less established. The model may describe a WEIRD-population
  regularity rather than a universal cognitive mechanism.

## Expressions

- "The decoy option" -- the dominated alternative introduced to shift
  preference
- "Asymmetric dominance" -- the technical term in behavioral economics
- "The attraction effect" -- alternative name emphasizing the pull toward
  the dominating option
- "The $6 medium" -- shorthand for a pricing tier designed to make the
  premium option look rational
- "Nobody buys the middle plan" -- product design folk wisdom, sometimes
  the explicit goal
- "Adding a third option to make the expensive one sell" -- the marketing
  application, stated plainly

## Origin Story

The decoy effect was first demonstrated by Joel Huber, John Payne, and
Christopher Puto in a 1982 paper presented at the Association for Consumer
Research conference (published in the Journal of Consumer Research in 1983).
They showed that adding an asymmetrically dominated alternative to a choice
set could increase the share of the dominating option -- a direct violation
of the regularity condition in rational choice theory, which holds that
adding an option can only decrease or maintain (never increase) the choice
share of existing options. The finding was initially controversial because
it challenged a foundational axiom of microeconomics. Subsequent
replications by Simonson (1989), Ariely (2008), and others established it
as one of the most robust context effects in decision-making research.

## References

- Huber, J., Payne, J.W. & Puto, C. "Adding Asymmetrically Dominated
  Alternatives: Violations of Regularity and the Similarity Hypothesis"
  (Journal of Consumer Research, 1982)
- Simonson, I. "Choice Based on Reasons: The Case of Attraction and
  Compromise Effects" (Journal of Consumer Research, 1989)
- Ariely, D. *Predictably Irrational* (2008) -- popular treatment with
  the magazine subscription example
