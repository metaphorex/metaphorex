---
applies_to:
- causal-reasoning
author: agent:metaphorex-miner
categories:
- law-and-governance
- cognitive-science
contributors: []
created: '2026-03-16'
grounding: established
harness: Claude Code
kind: paradigm
name: False in One Thing, False in All
provenance: brooms-legal-maxims
related:
- the-exception-proves-the-rule
- use-your-own-so-as-not-to-harm-another
slug: false-in-one-thing-false-in-all
source_frame: governance
updated: '2026-03-16'
transfers:
  - "[paradigm] a single demonstrated falsehood licenses discounting the entire body of testimony from that source, converting a local credibility failure into a global one"
  - "[paradigm] the cost of detecting unreliability is shifted from the evaluator to the source -- one lie forces the liar to rehabilitate everything, not the listener to re-verify each claim"
  - "[paradigm] reliability is treated as a property of the speaker, not of individual statements, so that a failure of the container poisons all contents"
limits:
  - "[paradigm] breaks because local unreliability does not entail global unreliability -- a witness who misremembers a date may still accurately describe a face, and the maxim collapses this distinction"
  - "[paradigm] misleads because it provides cover for dismissing inconvenient testimony by finding any single error, incentivizing motivated search for flaws rather than honest evaluation"
---

## Transfers

*Falsus in uno, falsus in omnibus.* False in one thing, false in
everything. A legal instruction to juries that a witness caught lying
about one fact may be disbelieved on all facts. The maxim encodes a
powerful credibility heuristic: trustworthiness is indivisible.

Key structural parallels:

- **Credibility as a vessel** -- the maxim treats a witness's testimony
  as a single container. One crack and the whole vessel leaks. You do
  not need to test each claim individually; you test the source. This
  is enormously efficient: instead of verifying N statements, you verify
  one character.
- **Totalizing inference** -- a single demonstrated lie licenses
  discounting everything. The reasoning is not "this particular claim
  is false" but "this person is a liar." The maxim shifts the unit of
  evaluation from the proposition to the person, which is what makes
  it both powerful and dangerous.
- **Burden reversal** -- ordinarily, the evaluator bears the cost of
  checking each claim. The maxim reverses this: once caught, the source
  bears the cost of rehabilitating all prior testimony. This is the
  structural principle behind credit ratings, brand trust, and data
  provenance -- one failure forces comprehensive re-verification by the
  party that failed.
- **Signal amplification** -- in information theory terms, a single lie
  is a high-information signal about the source's reliability. The
  maxim says: treat that signal as definitive. Do not average it with
  prior good behavior. One defection in an iterated game reveals the
  strategy.

## Limits

- **Local unreliability is not global unreliability** -- a witness who
  lies about their whereabouts to hide an affair may nonetheless tell
  the truth about a car accident they observed. The maxim collapses the
  distinction between motivated lying (specific to a topic) and
  dispositional dishonesty (a general character trait). Most real-world
  unreliability is local.
- **The maxim rewards motivated reasoning** -- if you want to dismiss
  someone's testimony, the maxim gives you a recipe: find one error,
  then discard everything. This is the rhetorical structure behind
  "gotcha" journalism, ad hominem attacks, and the genetic fallacy. The
  maxim provides a rational-seeming framework for what is often
  confirmation bias.
- **It conflates error with deception** -- being wrong about a date is
  not the same as lying about a date. Memory is fallible, perception is
  unreliable, and honest mistakes are common. The maxim does not
  distinguish between incompetence and malice, which means it can
  punish honest witnesses for normal cognitive failures.
- **It ignores corroboration** -- even an unreliable witness can provide
  testimony that is independently corroborated. The maxim says to
  discard all testimony from a tainted source, but a responsible
  evaluator should check whether each claim has independent support
  rather than making a blanket judgment.
- **Data quality is not binary** -- in modern data systems, the maxim's
  logic would mean discarding an entire dataset because one row is
  corrupt. No serious data engineer does this. They clean the bad rows
  and keep the good ones. The maxim belongs to an era when evaluating
  each datum individually was impractical; in contexts where per-item
  verification is cheap, the totalizing approach is wasteful.

## Expressions

- "Falsus in uno, falsus in omnibus" -- the Latin maxim itself, still
  used in jury instructions in some U.S. jurisdictions
- "Once a liar, always a liar" -- the folk version, which drops the
  legal context but preserves the totalizing structure
- "Fool me once, shame on you; fool me twice, shame on me" -- a
  related proverb that encodes the one-strike credibility rule
- "If they'll lie about the small things, they'll lie about the big
  things" -- the scaling assumption embedded in the maxim
- "Trust is earned in drops and lost in buckets" -- a modern restatement
  of the asymmetry the maxim encodes
- "The boy who cried wolf" -- the narrative version: past false alarms
  destroy all future credibility

## Origin Story

The maxim *falsus in uno, falsus in omnibus* comes from Roman law and
was transmitted into English common law through the medieval legal
tradition. It was never a binding rule of law but rather a permissive
instruction: juries *may* (not must) disbelieve all testimony from a
witness shown to have lied about any part of it.

In American law, the maxim has had a complicated trajectory. It was
widely used in 19th-century jury instructions but has been criticized
and restricted in modern practice. Many jurisdictions now instruct
juries that a witness found to have testified falsely on one point
may be distrusted on other points but is not automatically discredited
on everything. The shift reflects a growing recognition that the
totalizing inference the maxim licenses is psychologically powerful
but epistemically crude.

Outside the courtroom, the maxim operates everywhere trust is at
stake. Brand management, scientific peer review, journalistic
credibility, and personal relationships all exhibit the same pattern:
a single demonstrated failure can destroy confidence in the whole,
even when the failure is narrow and the rest of the record is sound.

## References

- Broom, H. *A Selection of Legal Maxims* (1845) -- the standard
  Victorian compendium that codified the maxim for common-law practice
- Wigmore, J.H. *Evidence in Trials at Common Law* (1904), vol. 3A --
  critical analysis of the maxim's logical and evidential limitations
- New York Pattern Jury Instructions, PJI 1:22 -- modern formulation
  permitting but not requiring the totalizing inference
