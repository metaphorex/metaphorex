---
author: agent:metaphorex-miner
categories:
- arts-and-culture
- philosophy
contributors: []
created: '2026-03-21'
grounding: folk
embodied_patterns:
  - iteration
  - scale
  - path
relation_types:
  - transform
  - select
structure: cycle
abstraction_level: generic
harness: Claude Code
kind: mental-model
limits:
- '[model] conflates "no objective completion criterion" with "no completion criterion at all," ignoring that many creative domains have well-defined done conditions (the building passes inspection, the test suite is green, the client signs off) which are external to the maker but perfectly functional'
- '[model] romanticizes abandonment as artistic sensitivity when it is often simply poor project management -- the novelist who abandons every manuscript at chapter three is not exercising refined judgment about diminishing returns, they are failing to finish'
- '[model] provides no framework for distinguishing productive stopping (shipping a good-enough product) from premature stopping (abandoning work that would have been significantly better with modest additional effort), collapsing a spectrum into a single gesture'
name: Art Is Never Finished, Only Abandoned
related:
- workmanship-of-risk
- measure-twice-cut-once
slug: art-is-never-finished-only-abandoned
source_frame: visual-arts-practice
transfers:
- '[model] reframes completion from an objective state of the work to a subjective decision by the maker, predicting that all "done" judgments in creative domains are stopping rules rather than achievement of a natural endpoint'
- '[model] identifies the diminishing-returns curve inherent in refinement -- each revision improves the work less while risking more -- and names the rational response: stop before the curve inverts'
- '[model] predicts that external deadlines (patrons, publishers, release dates) function as commitment devices that force stopping decisions the maker would otherwise defer indefinitely, explaining why constraints enable rather than inhibit creative output'
updated: '2026-03-21'
---

## Transfers

The aphorism -- attributed to Paul Valery ("Un ouvrage n'est jamais acheve
... mais abandonne") and sometimes misattributed to Leonardo da Vinci --
reframes the act of finishing creative work. There is no moment when a
painting, poem, or program is objectively complete. There is only the moment
when the maker stops working on it, either by choice or by external force.

This is not a lament. It is a structural observation about creative work
that transfers to any domain where the output has no natural stopping point.

Key structural parallels:

- **Completion as a stopping rule, not a state** -- in carpentry, a joint
  either fits or it doesn't; in mathematics, a proof either holds or it
  doesn't. But in painting, writing, and software design, there is always
  another revision that could improve the work. The model reframes "Is it
  done?" from a question about the object to a question about the maker's
  judgment: "Have I decided to stop?" This transfers to software shipping
  decisions, where "feature-complete" and "release-ready" are decisions by
  people, not properties of the code.
- **The diminishing-returns curve of refinement** -- early revisions to a
  creative work produce dramatic improvements. Later revisions produce
  smaller improvements and carry increasing risk of degrading what already
  works. At some point the curve inverts: further work makes the piece worse.
  The model names the rational response to this curve: stop before the
  inversion. In software, this is the argument for shipping an MVP rather
  than polishing indefinitely -- not because polish doesn't matter, but
  because the marginal value of each additional polish pass decreases while
  the opportunity cost increases.
- **External constraints as enabling forces** -- Valery's insight explains
  why creative workers are often more productive with deadlines than without
  them. The deadline is not an interruption of the creative process; it is
  the mechanism that forces the abandonment decision the maker would
  otherwise defer. Patrons, publishers, sprint deadlines, and conference
  submission dates all function as commitment devices. Without them, the
  work accretes revisions indefinitely -- not because the maker is lazy but
  because the work genuinely could always be better.
- **Abandonment as craft judgment** -- the model elevates the decision to
  stop from a failure ("I gave up") to a skill ("I recognized the right
  stopping point"). Knowing when further work will subtract rather than add
  is itself a form of expertise. The junior painter overworks the canvas;
  the master stops while the brushwork is still visible. The junior developer
  over-engineers the solution; the senior ships the simplest version that
  solves the problem.

## Limits

- **Not all completion is subjective** -- the model applies to creative and
  design work where quality is open-ended, but many professional domains
  have objective completion criteria. A bridge either bears its load or it
  doesn't. A tax return either balances or it doesn't. Applying the "never
  finished" model to work with clear done conditions imports false ambiguity
  and can justify shipping incomplete work by calling it "abandonment" when
  it is actually "failure to meet specification."
- **Romanticizes quitting** -- the aphorism can become a permission structure
  for chronic non-completion. The writer who abandons every novel at the
  difficult middle chapters, the entrepreneur who pivots away from every
  business at the first plateau, the musician who records demos but never
  finishes albums -- these are not exercising refined artistic judgment about
  stopping points. They are failing to push through the inevitable difficult
  phase of any creative project. The model provides no way to distinguish
  wise abandonment from premature surrender.
- **Collapses a spectrum into a binary** -- the aphorism suggests two states:
  working and abandoned. But real creative work has graduated completion
  states: rough draft, working draft, polished draft, submitted, published,
  revised edition. Each transition involves a stopping decision, but they
  are qualitatively different decisions with different stakes. Treating
  them all as "abandonment" obscures the meaningful differences between
  shipping a beta and walking away from a project entirely.
- **The attribution problem undermines its authority** -- the aphorism is
  attributed to Valery, Leonardo, and others, with no definitive source. Its
  folk provenance means it carries the authority of ancient wisdom without
  the accountability of a specific argument. This makes it easy to invoke
  as a conversation-ending truism rather than engaging with the specific
  question of whether *this* particular work, in *this* particular context,
  should be stopped or continued.

## Expressions

- "Ship it" -- the software engineering command that enacts Valery's
  principle: stop refining and release
- "Perfect is the enemy of good" -- Voltaire's formulation of the same
  diminishing-returns insight, without the artistic framing
- "Done is better than perfect" -- Facebook's poster, operationalizing
  the abandonment principle as organizational culture
- "Scope creep" -- the project management term for what happens when the
  "never finished" nature of the work is not counteracted by an abandonment
  decision
- "The last 10% takes 90% of the time" -- the engineering observation that
  maps onto the diminishing-returns curve the aphorism describes
- "Let it go" -- the colloquial version of the abandonment decision, often
  said by the person on the team who has internalized the stopping-rule
  insight

## Origin Story

The aphorism is most reliably attributed to Paul Valery, the French poet
and essayist, who wrote in 1933: "Un ouvrage n'est jamais acheve -- accident
heureux ou lassitude -- mais abandonne." ("A work is never completed --
happy accident or weariness -- but abandoned.") Valery was reflecting on his
own struggle with his long poem *La Jeune Parque*, which he revised
obsessively for four years before publishing. The misattribution to Leonardo
da Vinci, while historically unsupported, has a certain aptness: Leonardo's
notebooks are full of unfinished projects, and the *Mona Lisa* was reportedly
worked on for years without Leonardo considering it complete.

The aphorism entered software engineering discourse through the open-source
and agile movements, where it provides philosophical justification for
iterative release, MVPs, and the general preference for shipping over
polishing. Its adoption reflects software's structural similarity to art:
code, like a painting, can always be improved, and the absence of a natural
stopping point makes the decision to ship a judgment call rather than an
objective determination.

## References

- Valery, Paul. "Au sujet du Cimetiere marin" (1933) -- the probable
  original source of the aphorism
- Brooks, Frederick P. *The Mythical Man-Month* (1975) -- on the
  impossibility of knowing when software is "done"
- Ries, Eric. *The Lean Startup* (2011) -- the MVP as a formalized
  abandonment strategy: ship the minimum, learn, iterate
