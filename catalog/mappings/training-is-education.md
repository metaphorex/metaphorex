---
author: agent:metaphorex-miner
categories:
- ai-discourse
- cognitive-science
contributors: []
created: '2026-03-13'
harness: Claude Code
kind: conceptual-metaphor
name: Training Is Education
related:
- ai-hallucination-is-perception-disorder
- neural-network-is-a-brain
slug: training-is-education
source_frame: education
target_frame: artificial-intelligence
updated: '2026-03-13'
---

## What It Brings

Machine learning "trains" models. Models "learn" from data. There are
"teacher" networks and "student" networks. The training process follows a
"curriculum." These are not innocent word choices. The education metaphor
frames statistical optimization as pedagogy, importing an entire social
institution -- with its assumptions about understanding, intention, and
growth -- into a domain of gradient descent and loss minimization.

Key structural parallels:

- **Optimization as learning** -- adjusting model parameters to minimize a
  loss function is described as the model "learning." This maps the
  student's process of building understanding onto a numerical optimization
  procedure. The metaphor makes it natural to ask whether the model "really
  understands" the material, a question that only makes sense if you accept
  the educational frame.
- **Data as curriculum** -- training data is structured, sequenced, and
  curated, just as a curriculum is designed by educators. "Curriculum
  learning" is an actual ML technique that deliberately orders training
  examples from easy to hard, making the educational metaphor literal.
  The frame implies that data selection is a pedagogical act.
- **Teacher-student hierarchy** -- "teacher forcing" (providing ground-truth
  outputs during training) and "knowledge distillation" (transferring
  knowledge from a large model to a small one) map the teacher-student
  relationship onto model interactions. The metaphor imports authority,
  expertise, and the assumption that the teacher possesses genuine knowledge
  to transmit.
- **Epochs as semesters** -- multiple passes through training data are
  called "epochs," suggesting cycles of study. The frame implies that
  repeated exposure deepens understanding, when what actually happens is
  that repeated gradient updates refine parameter values.
- **Overfitting as rote memorization** -- a model that memorizes training
  data rather than generalizing is described as having "memorized" rather
  than "learned." The metaphor imports the educational distinction between
  surface learning and deep understanding, which is genuinely useful as
  an intuition pump even though the underlying mechanisms are different.

## Where It Breaks

- **Models do not understand** -- this is the central break. Education
  aims at comprehension: the student should be able to explain, apply,
  transfer, and critique what they have learned. A neural network
  minimizes a loss function. The education metaphor hides this difference
  by making it feel natural to attribute understanding to a system that
  has none. Drew McDermott identified this in 1976 as "wishful mnemonics":
  naming your program UNDERSTAND does not give it understanding.
- **There is no teacher** -- in supervised learning, labeled data provides
  signal, but nobody is teaching. There is no pedagogical intention, no
  adaptation to the student's confusion, no Socratic dialogue. "Teacher
  forcing" names a technique, not a relationship. The metaphor imports a
  social bond that does not exist.
- **Training does not follow a developmental arc** -- education assumes
  cognitive development: the student matures, builds on prior knowledge,
  and eventually achieves independent mastery. ML training is iterative
  parameter adjustment. There is no developmental stage theory for neural
  networks, despite the metaphor's invitation to look for one.
- **The metaphor obscures the role of architecture** -- in education, the
  same curriculum can produce different outcomes depending on the student's
  aptitude. In ML, the architecture (transformer, CNN, RNN) determines
  what the model can learn as much as the data does. The education
  metaphor foregrounds data and backgrounds architecture, because in
  classrooms, curriculum matters more than classroom design.
- **"Lifelong learning" is not lifelong learning** -- the ML concept of
  continual learning borrows the aspirational language of human education,
  but the challenges are entirely different. Human lifelong learning
  involves motivation, identity, and social context. ML continual learning
  is about catastrophic forgetting of parameter values.

## Expressions

- "The model was trained on..." -- the foundational expression, framing
  optimization as education
- "The model learned to..." -- attributing learning outcomes to a
  statistical process
- "Teacher forcing" -- providing correct answers during training, mapping
  the teacher's role onto ground-truth labels
- "Knowledge distillation" -- transferring a large model's capabilities to
  a smaller one, as a teacher transmits knowledge to a student
- "Curriculum learning" -- ordering training data from easy to hard,
  making the pedagogical metaphor explicit
- "The model has seen millions of examples" -- framing data exposure as
  study, with a visual perception overlay
- "Pre-training and fine-tuning" -- mapping the general-education-then-
  specialization arc onto the two-phase training paradigm

## Origin Story

The educational vocabulary of machine learning dates to the field's
earliest years. Arthur Samuel's 1959 paper on machine checkers used
"learning" to describe parameter adjustment, establishing the metaphor
before the field had a name. "Neural network" already imported biological
learning; the education metaphor layered social learning on top.
"Teacher forcing" was introduced by Williams and Zipser (1989) for
recurrent network training. "Curriculum learning" was formalized by Bengio
et al. (2009), making the metaphor architecturally literal. The Science
article "The metaphors of artificial intelligence" (2025) identifies the
education frame as one of the most pervasive and consequential
anthropomorphisms in AI, noting that Drew McDermott's 1970s critique of
"wishful mnemonics" was specifically aimed at this family of terms. The
metaphor persists because it is genuinely useful as an intuition pump --
"overfitting is like memorizing the textbook" conveys a real insight --
but its cost is the persistent confusion about whether AI systems
understand anything at all.

## References

- Science, "The metaphors of artificial intelligence" (2025) -- documents
  the education metaphor as anthropomorphic framing
- McDermott, D. "Artificial Intelligence Meets Natural Stupidity" (1976)
  -- the original critique of wishful mnemonics in AI
- Bengio, Y. et al. "Curriculum Learning" (2009) -- formalizes the
  pedagogical metaphor as an ML technique
- Williams, R. & Zipser, D. "A Learning Algorithm for Continually Running
  Fully Recurrent Neural Networks" (1989) -- introduces teacher forcing
- Samuel, A. "Some Studies in Machine Learning Using the Game of Checkers"
  (1959) -- early use of "learning" for parameter adjustment