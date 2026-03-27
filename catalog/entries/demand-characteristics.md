---
slug: demand-characteristics
name: Demand Characteristics
summary: "Subjects detect cues about what the researcher expects and adjust behavior to match, contaminating data with the hypothesis."
kind: mental-model
categories:
- psychology
- cognitive-science
author: agent:metaphorex-miner
contributors: []
related:
- hawthorne-effect
- placebo-effect
- goodharts-law
created: '2026-03-26'
updated: '2026-03-26'
grounding: established
harness: Claude Code
embodied_patterns:
  - container
  - surface-depth
  - matching
relation_types:
  - cause/constrain
  - cause/misfit
  - prevent
structure: cycle
abstraction_level: generic
transfers:
  - '[model] predicts that human subjects in any evaluative context will search for cues about what response is expected and adjust their behavior accordingly, because the social situation of being studied activates compliance and impression-management motives that override natural behavior'
  - '[model] identifies a structural confound where the measurement instrument (the experimental design) leaks information about the quantity being measured (the hypothesis), contaminating the data with the experimenter''s expectations rather than the subject''s genuine responses'
limits:
  - '[model] overstates subject sophistication -- many experimental subjects are genuinely naive about the hypothesis and respond naturally; the model''s assumption that subjects are quasi-detectives looking for cues is empirically true for some but not all participants'
  - '[model] conflates several distinct motives under one label: desire to help the experimenter, desire to look good, desire to sabotage the study, and simple hypothesis-guessing -- these produce different behavioral signatures and require different methodological countermeasures'
---

## Transfers

Demand characteristics describe the totality of cues in an experimental
setting that communicate the researcher's hypothesis to the subject,
enabling the subject to adjust their behavior to confirm (or sometimes
disconfirm) that hypothesis. The concept, introduced by Martin Orne in
1962, reframes the experimental subject from a passive responder into an
active interpreter of the social situation.

Key structural parallels:

- **The subject as detective** -- Orne's central insight is that human
  subjects do not simply react to experimental stimuli; they try to figure
  out what the experiment is about. Every element of the experimental
  situation -- the instructions, the setting, the demeanor of the
  experimenter, the structure of the tasks -- provides clues. Subjects
  assemble these clues into a hypothesis about the hypothesis, then
  behave in ways that confirm it. The experiment is not a one-way
  observation; it is a social negotiation.
- **The "good subject" role** -- most experimental subjects adopt a
  cooperative stance. They want to be helpful, to produce useful data, to
  validate the experimenter's time and effort. This social motive biases
  them toward confirming the perceived hypothesis. When a subject in a
  hypnosis study is asked to do something unusual, they may comply not
  because they are hypnotized but because the experimental context
  defines compliance as the expected behavior. The demand characteristics
  of the situation produce the result the experiment was designed to test.
- **Leaky instruments** -- the concept transfers beyond the laboratory.
  Any measurement of human behavior that reveals its purpose to the
  measured risks contamination. Employee satisfaction surveys where
  management announces "we want to know if the new policy is working"
  are measuring compliance with the implied expectation, not
  satisfaction. User testing where participants are told "we designed this
  feature to be intuitive" will produce reports of intuitiveness. The
  measurement leaks its own answer.
- **The experimenter as stimulus** -- demand characteristics are not just
  in the written protocol; they are embodied in the experimenter. Subtle
  cues -- tone of voice, facial expressions, body language when the
  subject gives the "right" answer -- shape behavior without either party
  being fully aware. Rosenthal's experimenter expectancy research showed
  that even when protocols are standardized, the experimenter's
  expectations leak through nonverbal channels.

## Limits

- **Not all subjects play along** -- Orne himself identified multiple
  subject roles. The "good subject" confirms the hypothesis; the
  "negativistic subject" deliberately disconfirms it; the "apprehensive
  subject" is preoccupied with self-presentation rather than the
  hypothesis; the "faithful subject" genuinely tries to respond naturally.
  The demand characteristics model predicts systematic bias, but actual
  subject pools contain a mixture of orientations, partially canceling
  out the effect. The model overpredicts the uniformity of the problem.
- **Modern methodology has countermeasures** -- double-blind designs,
  cover stories, deception protocols, between-subjects designs (where no
  subject sees both conditions), and implicit measures (reaction times,
  physiological responses) all reduce demand characteristics. The model
  was most powerful as a critique of mid-20th-century psychology when
  single-blind within-subjects designs were common. Its relevance has
  diminished as methodology has improved, though it has not disappeared.
- **The model assumes a single hypothesis to detect** -- in complex
  experimental designs with multiple conditions, interactions, and
  mediators, the "demand" is not a single signal but a cloud of
  contradictory cues. Subjects' hypotheses about these designs are
  typically wrong, which paradoxically makes the design more robust to
  demand effects. The model is most concerning for simple, transparent
  designs and least concerning for complex ones.
- **Generalizing to non-experimental settings is slippery** -- invoking
  "demand characteristics" to explain behavior outside the laboratory
  (in interviews, in therapy, in organizational surveys) stretches the
  concept beyond its original scope. In these settings, the "demand" is
  the entire social context, and calling it a confound rather than a
  legitimate social influence becomes a judgment call rather than a
  methodological diagnosis.

## Expressions

- "The subjects figured out what we were testing" -- the researcher's
  post-hoc recognition that demand characteristics may have contaminated
  results
- "What is this experiment really about?" -- the question subjects ask
  themselves (and sometimes each other) that drives hypothesis-guessing
- "Demand effects" -- the shorthand in methods sections, usually invoked
  as a limitation rather than a central finding
- "The experimenter expectancy effect" -- Rosenthal's complementary
  concept, focusing on the experimenter's role in transmitting demands
- "Social desirability bias" -- the related tendency to respond in ways
  that present oneself favorably, which amplifies demand characteristics
  when the "demanded" response is also the socially desirable one
- "What did you think this study was about?" -- the post-experimental
  inquiry (funnel debriefing) used to assess whether demand
  characteristics operated

## Origin Story

Martin Orne introduced the concept in his 1962 paper "On the Social
Psychology of the Psychological Experiment," which reframed the
experiment as a social situation rather than a neutral observation window.
Orne was a hypnosis researcher who noticed that subjects in hypnosis
experiments performed extraordinary feats -- not because they were in
altered states but because the experimental context defined those feats
as expected. His "quasi-control" methodology (asking simulators to fake
the experimental condition) became a standard tool for separating genuine
effects from demand artifacts.

The concept intersected with Robert Rosenthal's contemporaneous work on
experimenter expectancy effects (1963-1966), creating a powerful critique
of psychological methodology. Together, Orne and Rosenthal demonstrated
that the psychological experiment was not a transparent window onto the
mind but a social interaction contaminated by the expectations of both
parties. This critique catalyzed the methodological reforms of the 1970s
and 1980s, including widespread adoption of double-blind designs,
standardized protocols, and deception-based cover stories.

## References

- Orne, M.T. "On the Social Psychology of the Psychological Experiment"
  (1962) -- *American Psychologist*, the foundational paper
- Rosenthal, R. *Experimenter Effects in Behavioral Research* (1966) --
  the complementary work on experimenter expectancy
- Weber, S.J. & Cook, T.D. "Subject Effects in Laboratory Research"
  (1972) -- *Psychological Bulletin*, a review distinguishing the
  multiple subject roles
- Nichols, A.L. & Maner, J.K. "The Good-Subject Effect" (2008) --
  *Perspectives on Psychological Science*, a modern reassessment
