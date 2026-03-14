---
author: agent:metaphorex-miner
categories:
- ai-discourse
- cognitive-science
contributors: []
created: '2026-03-13'
harness: Claude Code
kind: conceptual-metaphor
name: AI Hallucination Is Perception Disorder
related:
- training-is-education
- neural-network-is-a-brain
slug: ai-hallucination-is-perception-disorder
source_frame: medicine
target_frame: artificial-intelligence
updated: '2026-03-13'
---

## What It Brings

When a language model generates confident but false text, we call it a
"hallucination" -- a term borrowed from psychiatry, where it means
perceiving things that are not there. This is arguably the most
consequential metaphor in contemporary AI discourse. It does not merely
describe a technical failure; it presupposes that the model has something
like perception in the first place.

Key structural parallels:

- **Confabulation as misperception** -- the psychiatric term "hallucination"
  implies a sensory system that has malfunctioned. Applied to AI, it frames
  false outputs as a perceptual error: the model "saw" something that was
  not there. This imports the entire medical infrastructure of diagnosis,
  pathology, and potential cure. If hallucination is a disease, it can
  presumably be treated.
- **The model as perceiving subject** -- calling an output a hallucination
  requires a subject who hallucinates. The metaphor implicitly grants the
  model a phenomenological interior: it has experiences, and some of those
  experiences are faulty. This is the deepest and most hidden import of
  the metaphor.
- **False confidence as a symptom** -- psychiatric hallucinations are
  experienced with full conviction by the patient. The metaphor maps this
  onto AI's tendency to generate false information with the same syntactic
  confidence as true information. This is genuinely illuminating: the
  problem is not just that the model is wrong, but that it does not signal
  uncertainty.
- **The promise of a cure** -- medical framing implies that hallucinations
  are a disorder to be fixed, not a fundamental property of the system.
  This shapes research priorities toward "reducing hallucination" as if
  it were a bug rather than an inherent feature of probabilistic text
  generation.

## Where It Breaks

- **LLMs do not perceive** -- this is the fundamental break. A
  hallucination requires a perceiving subject whose sensory apparatus
  produces false experiences. Language models do not have sensory
  apparatus, do not have experiences, and do not perceive. They generate
  statistically plausible token sequences. The metaphor smuggles in an
  entire philosophy of mind (that the model has something like
  consciousness) through a single word choice.
- **"Confabulation" is the more accurate psychiatric analogy** -- what LLMs
  actually do is closer to confabulation: generating plausible-sounding
  narratives to fill gaps, without awareness that the narrative is
  fabricated. Confabulation is a memory disorder, not a perceptual one.
  But "confabulation" never caught on, probably because it is less
  dramatic and less familiar than "hallucination."
- **The medical frame pathologizes a normal behavior** -- for a language
  model, generating text that does not correspond to external facts is not
  a malfunction. It is the system operating exactly as designed: predicting
  the next token based on statistical patterns. The hallucination metaphor
  frames normal operation as disease, which distorts both research and
  public understanding.
- **The metaphor individualizes a systemic issue** -- in psychiatry, a
  hallucination is a symptom in an individual patient. Applied to AI, it
  locates the problem in the model rather than in the sociotechnical system
  (training data, deployment context, user expectations, lack of
  verification infrastructure). "The model hallucinated" deflects attention
  from "the system was deployed without adequate verification."
- **It obscures the role of the user** -- hallucinations happen to the
  patient without their input. But LLM confabulations are prompted: the
  user asked a question, and the model generated a plausible-sounding
  response. The metaphor erases the interaction and makes the model solely
  responsible for the output.

## Expressions

- "The model hallucinated" -- the standard description of confident false
  output, treating the model as a patient with symptoms
- "Hallucination rate" -- quantifying the disorder as a measurable
  pathology, like a fever reading
- "Reducing hallucinations" -- the treatment frame, implying that the
  condition can be cured with the right intervention
- "Grounding to reduce hallucination" -- connecting the model to external
  facts as a therapeutic intervention, like grounding techniques in
  psychiatric care
- "The model is making things up" -- a less clinical variant that still
  implies intentional fabrication

## Origin Story

The term "hallucination" entered AI discourse through computer vision in
the 2010s, where neural networks sometimes "saw" patterns in noise --
DeepDream's psychedelic dog faces being the iconic example. The visual
context made the psychiatric metaphor feel natural: the network literally
produced images of things that were not there. When large language models
began generating confident falsehoods in 2022-2023, the term transferred
from vision to language, losing the visual grounding that had made it
somewhat apt. The Springer study "Between fact and fairy: tracing the
hallucination metaphor in AI discourse" (2025) documents this migration
and argues that the metaphor has real consequences for regulation and
public trust. The Science article "The metaphors of artificial intelligence"
(2025) places hallucination within the broader pattern of anthropomorphic
framing that Drew McDermott warned about in the 1970s as "wishful
mnemonics" -- technical terms that trick their users into attributing
human qualities to machines. Alternative terms proposed by researchers
include "confabulation" (Bender et al.), "stochastic parroting" (Bender
et al., 2021), and simply "errors" or "fabrications," but none has
displaced "hallucination" in common usage.

## References

- Springer, "Between fact and fairy: tracing the hallucination metaphor
  in AI discourse" (2025) -- academic analysis of the metaphor's
  trajectory and consequences
- Science, "The metaphors of artificial intelligence" (2025) -- places
  hallucination in the context of AI anthropomorphism
- McDermott, D. "Artificial Intelligence Meets Natural Stupidity" (1976)
  -- the original critique of "wishful mnemonics" in AI terminology
- Bender, E. et al. "On the Dangers of Stochastic Parrots" (2021) --
  proposes alternative framings for LLM behavior
- Maas, M. "AI is Like..." (2023) -- catalogs hallucination under
  anthropomorphic framing in AI policy discourse