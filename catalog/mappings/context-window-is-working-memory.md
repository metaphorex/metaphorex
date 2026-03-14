---
author: agent:metaphorex-miner
categories:
- ai-discourse
- cognitive-science
contributors: []
created: '2026-03-13'
harness: Claude Code
kind: conceptual-metaphor
name: Context Window Is Working Memory
related:
- ai-hallucination-is-perception-disorder
- neural-network-is-a-brain
- training-is-education
- chain-of-thought-is-self-talk
slug: context-window-is-working-memory
source_frame: mental-experience
target_frame: artificial-intelligence
updated: '2026-03-13'
---

## What It Brings

The "context window" -- the maximum number of tokens a language model can
process in a single interaction -- is routinely described as the model's
"working memory." The metaphor maps the well-studied cognitive constraint
of human short-term memory onto the mechanical token limit of a transformer
architecture. It makes an engineering parameter feel like a psychological
limitation, importing rich intuitions about forgetting, cognitive load,
and the struggle to hold complex ideas in mind.

Key structural parallels:

- **Finite capacity** -- human working memory holds roughly 7 plus or
  minus 2 chunks of information (Miller, 1956). A model's context window
  holds a fixed number of tokens. The metaphor maps this shared finitude:
  both systems can only "attend to" so much at once, and exceeding the
  limit means something gets lost.
- **Recency dominance** -- in human working memory, recent items are
  easier to recall (the recency effect). In transformer attention,
  recent tokens often receive higher attention weights, especially in
  long contexts. The metaphor makes this architectural bias feel natural:
  of course the model remembers what you just said better than what you
  said ten thousand tokens ago.
- **Context loss as forgetting** -- when a conversation exceeds the
  context window and earlier tokens are dropped, we say the model "forgot"
  the beginning. This maps human memory failure onto mechanical truncation,
  making it feel like a cognitive limitation rather than a buffer overflow.
- **Chunking and compression** -- humans extend working memory through
  chunking: grouping individual items into meaningful units. Techniques
  like summarizing earlier conversation to fit within the context window
  are described as analogous strategies. The metaphor makes engineering
  workarounds feel like cognitive strategies.
- **The "malloc/free problem"** -- Geoffrey Huntley's Ralph Wiggum post
  describes context window management as "the malloc/free problem,"
  layering a systems programming metaphor on top of the cognitive one.
  This double mapping reveals how naturally the working memory frame
  operates: even engineers reaching for a more precise analogy still
  frame it as a memory problem.

## Where It Breaks

- **Working memory is active processing, not passive storage** -- human
  working memory is not a buffer that holds information; it is a system
  that actively manipulates and integrates information. You do not just
  store seven items -- you rehearse them, combine them, relate them to
  long-term memory. A context window is passive input: every token sits
  there with equal ontological status until the attention mechanism
  processes them. The metaphor flattens active cognition into a storage
  problem.
- **Human forgetting is selective; truncation is not** -- when humans
  forget, the process is structured: emotionally significant, frequently
  rehearsed, and deeply encoded information persists while trivia fades.
  When a context window overflows, tokens are dropped from the beginning
  regardless of their importance. The metaphor imports an illusion of
  intelligent forgetting onto what is brute mechanical truncation. A
  system that "forgets" the user's name but remembers a code snippet from
  the same position in the context is not exhibiting memory -- it is
  exhibiting a FIFO buffer.
- **There is no long-term memory to fall back on** -- human working
  memory operates in constant dialogue with long-term memory. When you
  cannot hold everything in working memory, you rely on stored knowledge,
  habits, and schemas. A language model's "long-term memory" (its trained
  weights) is fundamentally different: it encodes statistical patterns
  from training, not episodic memories of previous interactions. The
  metaphor suggests that the model has a richer memory system behind the
  context window, when in most cases it does not.
- **Capacity is not the binding constraint** -- human working memory is
  limited not just by capacity but by interference, decay, and attentional
  control. Expanding context windows (from 4K to 128K to 1M tokens) does
  not produce the equivalent of enhanced human cognition. Models with
  million-token windows still exhibit "lost in the middle" effects where
  they attend poorly to information in the middle of long contexts. The
  metaphor predicts that more capacity equals better memory, but the
  actual failure mode is attentional, not capacitative.
- **The metaphor naturalizes an engineering choice** -- framing the
  context window as working memory makes a design parameter (chosen by
  engineers, constrained by hardware costs) feel like a natural cognitive
  limitation. This discourages questioning why the limit exists. Calling
  it "working memory" makes 128K tokens feel like a biological constraint
  rather than a business decision about inference cost.

## Expressions

- "The model forgot what we discussed earlier" -- memory-failure language
  for context truncation
- "Expanding the context window" -- increasing capacity framed as
  cognitive enhancement
- "Lost in the middle" -- attentional failure described using spatial
  memory vocabulary
- "Stuffing the context" -- overloading working memory with too much
  information
- "The model can only hold so much in memory" -- capacity framing
  borrowed directly from cognitive science
- "RAG as external memory" -- retrieval-augmented generation described
  as a prosthetic memory system

## Origin Story

The working memory metaphor for context windows emerged alongside the
transformer architecture itself. The term "attention" in "attention
mechanism" (Vaswani et al., 2017) already imported cognitive vocabulary,
and once the core mechanism was named after a psychological concept, the
rest of the cognitive framing followed naturally. If the model "attends"
to tokens, then the set of tokens it can attend to is its "working
memory."

The metaphor became practically significant as context windows grew.
When GPT-3 had a 4K token limit, the constraint was small enough to be
experienced as a simple engineering limitation. When Claude and GPT-4
pushed to 100K+ tokens, the working memory frame became the primary way
users understood the capability: "it can hold an entire book in memory."
The cognitive framing made the upgrade feel transformative -- not just
more tokens, but more mind.

Huntley's Ralph Wiggum Loop essay (2025) explicitly engages with the
metaphor, describing context window management in agentic systems as the
central engineering challenge. The fact that agent frameworks spend
enormous effort on "memory management" -- summarizing, compressing,
selectively retaining context -- demonstrates how thoroughly the working
memory frame shapes actual system design.

## References

- Vaswani, A. et al. "Attention Is All You Need" (2017) -- the
  transformer paper that imported cognitive vocabulary into architecture
- Miller, G. "The Magical Number Seven, Plus or Minus Two" (1956) --
  the foundational working memory capacity paper
- Huntley, G. "Ralph Wiggum as a software engineer" (2025) -- describes
  context window management as "the malloc/free problem"
- Liu, N. et al. "Lost in the Middle: How Language Models Use Long
  Contexts" (2023) -- demonstrates that expanded context windows do not
  produce uniform attention