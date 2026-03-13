---
slug: neural-network-is-a-brain
name: "Neural Network Is a Brain"
kind: conceptual-metaphor
source_frame: biology
target_frame: artificial-intelligence
categories:
  - ai-discourse
  - cognitive-science
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - training-is-education
  - weights-are-knowledge
  - people-are-machines
---

## What It Brings

The foundational metaphor of artificial intelligence. McCulloch and Pitts
proposed the first mathematical model of a "neuron" in 1943, mapping
biological neural architecture onto logical threshold units. Eighty years
later, the vocabulary remains: we speak of neurons, layers, activation
functions, synaptic weights, and network architectures as if describing a
biological organ. The metaphor is so deeply embedded that most practitioners
do not experience it as metaphorical at all.

Key structural parallels:

- **Neurons as computational units** -- biological neurons receive
  electrochemical signals, integrate them, and fire when a threshold is
  reached. Artificial neurons receive numerical inputs, compute a weighted
  sum, and pass the result through an activation function. The mapping is
  clean enough to have generated an entire field, but the correspondence is
  structural, not mechanistic. Biological neurons are complex cells with
  thousands of synaptic connections, internal state, and temporal dynamics.
  Artificial neurons are single mathematical operations.
- **Layers as hierarchy** -- the brain processes information through
  layered regions (retina to V1 to V2 to inferotemporal cortex for vision).
  Deep neural networks stack layers of artificial neurons. The metaphor
  imports the idea that intelligence arises from hierarchical abstraction:
  early layers detect edges, later layers detect faces. This assumption
  shaped the deep learning revolution.
- **Activation as signal** -- biological neurons either fire or do not
  (approximately). Activation functions in neural networks threshold the
  output of each unit. The metaphor brings the intuition that computation
  happens through selective response -- not every unit contributes to every
  output, just as not every neuron fires for every stimulus.
- **Networks as emergent intelligence** -- the brain's intelligence arises
  not from individual neurons but from the pattern of connections between
  billions of them. The metaphor imports the hypothesis that intelligence
  is an emergent property of scale and connectivity, which directly
  motivates the "scaling laws" approach to AI: more parameters, more data,
  more capability.

## Where It Breaks

- **Biological neurons are not matrix multiplications** -- a real neuron
  has roughly 7,000 synaptic connections, processes signals with precise
  timing, releases dozens of different neurotransmitters, and modifies its
  own structure in response to activity. An artificial neuron multiplies a
  vector by a weight matrix and applies a nonlinear function. The gap
  between these two operations is not a matter of degree but of kind. The
  brain metaphor makes this gap invisible, encouraging the inference that
  artificial neural networks work "like brains do" when they work like
  linear algebra does.
- **Brains do not backpropagate** -- the core training algorithm for neural
  networks (backpropagation) has no known biological analogue. Real brains
  do not compute global error gradients and propagate them backward through
  synaptic connections. The metaphor quietly drops this fact: the most
  important thing about how artificial neural networks learn has nothing to
  do with how brains learn.
- **The anthropomorphism cascade** -- because the foundational metaphor
  says "this is a brain," every subsequent metaphor inherits the
  anthropomorphism. If the network is a brain, then its parameters are
  "knowledge," its outputs are "understanding," its errors are
  "hallucinations," and its constraints are "alignment." Each of these
  downstream metaphors derives its plausibility from the brain metaphor's
  initial claim. Questioning any one of them means questioning the
  foundation.
- **Brains are embodied; networks are not** -- a biological brain exists
  in a body, receives sensory input from a physical environment, and
  developed through millions of years of evolutionary pressure to keep
  that body alive. Neural networks have no body, no sensory apparatus, no
  evolutionary history, and no survival imperative. The brain metaphor
  strips away everything that makes brains brains and keeps only the
  connection topology.
- **Scale does not work the same way** -- the human brain has approximately
  86 billion neurons. GPT-4 is estimated to have around 1.8 trillion
  parameters. The metaphor suggests these are comparable quantities, but
  parameter count in a neural network does not map onto neuron count in a
  brain in any meaningful way. The comparison invites misleading headlines
  about AI "surpassing" human brain scale.

## Expressions

- "Neural network" -- the term itself is the metaphor, so ubiquitous it
  reads as literal
- "Deep learning" -- depth as hierarchical layers, importing the brain's
  layered processing structure
- "The model learned to recognize faces" -- learning and recognition
  borrowed directly from cognitive description
- "Artificial neurons fire when activated" -- activation borrowed from
  neuroscience
- "Convolutional neural networks are inspired by the visual cortex" --
  explicit source attribution to biology
- "It's basically how the brain works" -- the popular-press version,
  collapsing the analogy into identity

## Origin Story

Warren McCulloch and Walter Pitts published "A Logical Calculus of the
Ideas Immanent in Nervous Activity" in 1943, proposing that neurons could
be modeled as binary threshold logic units. Frank Rosenblatt built the
Perceptron in 1958, explicitly describing it as a model of biological
perception. The metaphor survived the AI winters, the connectionist-
symbolic debates, and the shift from hand-crafted features to end-to-end
learning. When deep learning exploded after 2012 (AlexNet), the brain
metaphor rode the wave -- every popular explanation of neural networks
began with a diagram of biological neurons.

Drew McDermott warned in 1976 about "wishful mnemonics" -- naming AI
components with cognitive terms that import unearned implications. The
brain metaphor is the original wishful mnemonic. Science (2025) documents
how this anthropomorphic framing continues to shape public understanding
and policy. The metaphor is not wrong -- it was genuinely productive in
suggesting architectural choices -- but it has long outlived its
explanatory usefulness and now primarily serves to mystify rather than
clarify.

## References

- McCulloch, W. & Pitts, W. "A Logical Calculus of the Ideas Immanent in
  Nervous Activity" (1943)
- Rosenblatt, F. "The Perceptron: A Probabilistic Model for Information
  Storage and Organization in the Brain" (1958)
- McDermott, D. "Artificial Intelligence Meets Natural Stupidity" (1976) --
  critique of wishful mnemonics
- Science, "The metaphors of artificial intelligence" (2025) -- documents
  ongoing anthropomorphic framing
- Maas, M. "AI is Like... A Literature Review of AI Metaphors" (2023)
