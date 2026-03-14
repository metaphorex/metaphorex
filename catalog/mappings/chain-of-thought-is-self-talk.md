---
author: agent:metaphorex-miner
categories:
- ai-discourse
- cognitive-science
contributors: []
created: '2026-03-13'
harness: Claude Code
kind: conceptual-metaphor
name: Chain of Thought Is Self-Talk
related:
- ai-hallucination-is-perception-disorder
- neural-network-is-a-brain
- training-is-education
- ralph-wiggum-loop
slug: chain-of-thought-is-self-talk
source_frame: mental-experience
target_frame: artificial-intelligence
updated: '2026-03-13'
---

## What It Brings

Chain-of-thought prompting and the ReAct paradigm frame AI reasoning as
inner monologue made visible. The model "thinks out loud," "shows its
work," and "reasons step by step" -- language borrowed directly from
developmental psychology, where Vygotsky described children learning to
internalize speech as a tool for thought. The metaphor maps the structure
of human self-directed speech onto token generation, making a statistical
process feel like cognition.

Key structural parallels:

- **Showing work improves performance** -- the core empirical finding.
  When humans talk themselves through a problem, they perform better than
  when they try to jump to the answer. When LLMs generate intermediate
  reasoning tokens before a final answer, they also perform better. The
  metaphor makes this finding intuitive: of course showing your work
  helps, just like it helped in math class. The structural parallel is
  real enough to be useful, even if the mechanisms are completely
  different.
- **Internal monologue as reasoning substrate** -- human self-talk is not
  merely narration of pre-existing thoughts; the speech itself structures
  the thinking. Vygotsky argued that inner speech is a cognitive tool,
  not a byproduct. The metaphor imports this claim onto LLMs: the
  intermediate tokens are not decorative narration but the mechanism
  through which the model "arrives" at better answers. This framing
  shapes how researchers think about why chain-of-thought works.
- **Step-by-step decomposition** -- self-talk naturally decomposes complex
  problems into sequential steps. "First I need to... then I can..."
  is how humans narrate problem-solving to themselves. Chain-of-thought
  prompting instructs the model to do the same: break the problem into
  steps and address each one. The metaphor makes decomposition feel like
  a natural cognitive strategy rather than an engineering technique.
- **Scratchpad as working memory** -- some implementations give the model
  a "scratchpad" for intermediate calculations, borrowing the metaphor
  of physical note-taking as an external memory aid. This maps onto the
  psychological concept of working memory augmentation: writing things
  down frees up mental capacity for the next step. The scratchpad frame
  makes the model's context window feel like a cognitive resource.
- **Thinking tokens as hidden reasoning** -- models with "extended
  thinking" generate tokens the user does not see, framed as the model
  thinking privately before speaking. This directly maps the human
  experience of internal deliberation: we think before we speak, and
  the thinking is private. The metaphor makes hidden token generation
  feel like a familiar cognitive process.

## Where It Breaks

- **LLMs do not have inner experience** -- human self-talk is
  phenomenologically rich. It involves intention, attention, emotional
  coloring, metacognition ("am I on the right track?"), and the felt
  sense of understanding. Chain-of-thought tokens have none of this.
  They are statistically generated sequences that happen to resemble
  the surface form of human reasoning narration. The metaphor maps the
  output format while importing the assumption of an experiential
  interior that does not exist.
- **Self-talk is causal; CoT tokens may not be** -- when a human says
  "let me think about this step by step," the subsequent reasoning
  actually follows from the deliberate decomposition. Whether chain-of-
  thought tokens are causally effective in the same way is an open
  research question. The model might generate the right answer for
  statistical reasons that have nothing to do with the "reasoning" in
  the intermediate tokens. The self-talk metaphor assumes causal
  efficacy that has not been established.
- **Human self-talk serves emotional regulation** -- a large function of
  inner speech is managing anxiety, maintaining motivation, and
  processing emotions. "I can do this. Calm down. Focus." Chain-of-
  thought prompting has no emotional dimension. The metaphor maps only
  the cognitive-instrumental aspect of self-talk while ignoring its
  affective core, which in humans may be inseparable from its cognitive
  function.
- **The "thinking" can be fabricated** -- human self-talk, while
  sometimes self-deceptive, generally reflects actual cognitive
  processes. An LLM's chain-of-thought can be entirely confabulated:
  the model may generate plausible-looking reasoning steps that do not
  correspond to its actual computational path from input to output.
  The self-talk metaphor hides the possibility that the "reasoning"
  is post-hoc rationalization generated to satisfy the prompt format.
- **Vygotsky's theory is about development; LLMs do not develop** --
  internalized speech in humans emerges through a developmental process:
  children first talk aloud, then whisper, then internalize. Chain-of-
  thought prompting skips this trajectory entirely. The developmental
  framing imports expectations about learning and maturation that do
  not apply to a system whose "reasoning" was established during
  training, not through ongoing cognitive development.

## Expressions

- "Let's think step by step" -- the canonical chain-of-thought prompt,
  borrowing the language of self-directed reasoning instruction
- "Show your work" -- from mathematics pedagogy, framing token
  generation as demonstrating a reasoning process
- "The model is reasoning" -- attributing cognitive processes to token
  generation
- "Extended thinking" -- hidden token generation framed as private
  deliberation
- "Scratchpad" -- intermediate computation space, from physical
  note-taking
- "Inner monologue" -- chain-of-thought generation described as
  internalized speech
- "Think before you answer" -- prompt instruction that imports the
  human sequence of deliberation followed by utterance
- "Reasoning tokens" -- tokens whose function is framed as cognitive
  processing rather than text generation

## Origin Story

Chain-of-thought prompting was formalized by Wei et al. in "Chain-of-
Thought Prompting Elicits Reasoning in Large Language Models" (2022).
The paper demonstrated that asking a model to show intermediate reasoning
steps dramatically improved performance on math and logic tasks. The
finding was immediately interpreted through the self-talk lens: the model
"reasons better when it thinks out loud."

The ReAct paradigm (Yao et al., 2023) extended this by interleaving
reasoning and action: the model narrates its thinking, takes an action,
observes the result, and reasons again. The explicit framing as
"reasoning" and "thinking" cemented the self-talk metaphor.

The psychological parallel has deep roots. Vygotsky's zone of proximal
development (1934) and his theory of internalized speech describe how
children learn to use language as a cognitive tool. The chain-of-thought
metaphor maps this developmental theory onto LLM behavior, suggesting
that language-as-thinking-tool is a universal structure that applies to
both biological and artificial systems. Whether this structural parallel
is coincidence, convergent design, or deep truth about the relationship
between language and reasoning is among the most contested questions in
AI philosophy.

The metaphor intensified in 2024-2025 with "reasoning models" that
generate hidden thinking tokens. The term "extended thinking" frames
hidden computation as private deliberation, completing the mapping from
inner speech to token generation.

## References

- Wei, J. et al. "Chain-of-Thought Prompting Elicits Reasoning in
  Large Language Models" (2022) -- the foundational paper establishing
  the technique and its implicit self-talk framing
- Yao, S. et al. "ReAct: Synergizing Reasoning and Acting in Language
  Models" (2023) -- interleaved reasoning and action as inner monologue
  plus behavior
- Vygotsky, L. "Thought and Language" (1934) -- the developmental
  psychology theory of internalized speech that the metaphor draws from
- Science, "The metaphors of artificial intelligence" (2025) -- places
  "reasoning" language within the broader pattern of AI anthropomorphism