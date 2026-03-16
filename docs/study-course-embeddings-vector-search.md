# Embeddings & Vector Search: A Study Course

A progressive reading list for a technical leader building per-proposition
embeddings for structural similarity search across a catalog of conceptual
metaphors.

---

## Level 1: Foundations (What ARE Embeddings?)

Start here. No math prerequisites. The goal is to build strong geometric
intuition before touching any code or models.

### 1.1 Vectors, What Even Are They?

- **3Blue1Brown, "Essence of Linear Algebra" -- Chapter 1: Vectors**
- https://www.3blue1brown.com/lessons/vectors
- Watch just the first video (17 min). Builds the visual intuition that a
  vector is simultaneously an arrow in space AND a list of numbers. This
  dual view is the foundation everything else rests on.
- **Time:** 17 minutes (video)
- **Prerequisites:** None

### 1.2 What Is a Vector Embedding, Intuitively

- **Simon Willison, "Embeddings: What They Are and Why They Matter"**
- https://simonwillison.net/2023/Oct/23/embeddings/
- A practitioner's overview of embeddings as a tool: what they do, why
  the fixed-length property matters, and practical applications (related
  content, semantic search, clustering). Written by someone who builds
  things with them, not someone who trains them. The right level of
  abstraction for an architect.
- **Time:** 30 minutes
- **Prerequisites:** None

### 1.3 How Text Gets Turned into Numbers

- **Jay Alammar, "The Illustrated Word2vec"**
- https://jalammar.github.io/illustrated-word2vec/
- The canonical visual explainer. Walks through how a neural network
  learns to place words in vector space by predicting context. The
  key insight: meaning emerges from patterns of co-occurrence, and the
  resulting vectors encode those patterns geometrically. This is the
  "aha" moment for most people.
- **Time:** 45 minutes
- **Prerequisites:** 1.1

### 1.4 What "Similarity" Means in Vector Space

- **Dataquest, "Measuring Similarity and Distance Between Embeddings"**
- https://www.dataquest.io/blog/measuring-similarity-and-distance-between-embeddings/
- Covers cosine similarity, Euclidean (L2) distance, and dot product --
  when each one is appropriate and why cosine similarity dominates in
  text embedding work (because direction matters more than magnitude).
  Practical, code-included, no fluff.
- **Time:** 20 minutes
- **Prerequisites:** 1.1, 1.2

### 1.5 Why Embeddings Capture Meaning

- **Mikolov et al., "Efficient Estimation of Word Representations in Vector Space" (2013)**
- https://arxiv.org/abs/1301.3781
- The original word2vec paper. Short (12 pages) and surprisingly
  readable. Worth skimming after reading Alammar's visual version to
  see how the ideas were originally framed. The king-queen analogy
  result launched an entire field.
- **Time:** 30 minutes (skim)
- **Prerequisites:** 1.3

---

## Level 2: How Embedding Models Work

Now that you have the intuition, understand the machinery. This is
the level where you can evaluate model choices and understand tradeoffs.

### 2.1 The Transformer Architecture

- **Jay Alammar, "The Illustrated Transformer"**
- https://jalammar.github.io/illustrated-transformer/
- The standard reference for understanding attention and transformers
  visually. Every embedding model you will use is built on this
  architecture. Focus on self-attention and how it lets each token
  "look at" every other token -- this is why transformer embeddings
  are context-dependent (unlike word2vec).
- **Time:** 60 minutes
- **Prerequisites:** 1.3

### 2.2 Encoders vs. Decoders: Why Embedding Models Differ from LLMs

- **Sebastian Raschka, "Understanding Encoder and Decoder LLMs"**
- https://magazine.sebastianraschka.com/p/understanding-encoder-and-decoder
- Clarifies the encoder/decoder split. Embedding models are encoders
  (bidirectional, produce a fixed vector). Generative LLMs are decoders
  (autoregressive, produce tokens). Your embedding model is a small,
  fast encoder -- not a billion-parameter generator. This distinction
  matters for cost, latency, and deployment architecture.
- **Time:** 25 minutes
- **Prerequisites:** 2.1

### 2.3 From Word Embeddings to Sentence Embeddings

- **Reimers & Gurevych, "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks" (2019)**
- https://arxiv.org/abs/1908.10084
- The paper that made sentence-level embeddings practical. BERT alone
  can't efficiently compare sentences (you'd need to process every pair).
  SBERT uses a siamese architecture to produce independent sentence
  vectors you can compare with cosine similarity. This is the direct
  ancestor of the embedding models you'll use for per-proposition search.
- **Time:** 40 minutes
- **Prerequisites:** 2.1, 2.2

### 2.4 Contrastive Learning: Why Similar Things End Up Close

- **Lilian Weng, "Contrastive Representation Learning"**
- https://lilianweng.github.io/posts/2021-05-31-contrastive/
- Deep, thorough treatment of how embedding models are trained. The core
  idea: show the model pairs of similar things (positives) and dissimilar
  things (negatives), and train it to push positives together and negatives
  apart in vector space. Understanding this tells you why your embedding
  quality depends heavily on what the model was trained on -- and why
  off-the-shelf models may not capture "structural similarity between
  metaphors" without fine-tuning.
- **Time:** 60 minutes
- **Prerequisites:** 2.1, 2.3

### 2.5 MTEB: How Embedding Quality Is Measured

- **Hugging Face, "MTEB: Massive Text Embedding Benchmark"**
- https://huggingface.co/blog/mteb
- The standard benchmark for evaluating embedding models across 56
  datasets and 8 task types (retrieval, classification, clustering, etc.).
  Key insight: no single model dominates all tasks. When choosing a model
  for metaphor similarity search, you need to evaluate on YOUR data, not
  just trust the leaderboard. But the leaderboard is where you start.
- **Time:** 20 minutes
- **Prerequisites:** 2.3

### 2.6 The Full Picture: From Tokens to Deployment

- **Vicki Boykis, "What Are Embeddings?"**
- https://vickiboykis.com/what_are_embeddings/
- A 70+ page technical book (free) covering the complete pipeline: NLP
  history, tokenization, word2vec, BERT, transformers, and engineering
  considerations for production. Read this as a reference after the
  blog posts above -- it ties everything together in one coherent
  narrative and covers practical concerns (batching, caching, cost)
  that the academic sources skip.
- **Time:** 3-4 hours (reference; read sections as needed)
- **Prerequisites:** 2.1 through 2.4

---

## Level 3: Vector Search Mechanics

The engineering layer. How do you actually store, index, and query
millions of vectors efficiently?

### 3.1 Nearest Neighbor Search: From Brute Force to Indexes

- **Pinecone Learn Series, "Nearest Neighbor Indexes for Similarity Search"**
- https://www.pinecone.io/learn/series/faiss/vector-indexes/
- Starts with flat (brute-force) search and explains why it doesn't scale,
  then introduces IVF (inverted file index) with Voronoi partitioning.
  Clear diagrams, practical code. For your catalog (~500 propositions
  growing to maybe 5,000), brute force will actually work fine --
  but understanding why is valuable.
- **Time:** 30 minutes
- **Prerequisites:** 1.4

### 3.2 HNSW: The Algorithm Behind Most Vector Search

- **Pinecone Learn Series, "Hierarchical Navigable Small Worlds (HNSW)"**
- https://www.pinecone.io/learn/series/faiss/hnsw/
- The dominant ANN algorithm. Uses a multi-layer graph where upper
  layers have long-range connections (for fast coarse navigation) and
  lower layers have short-range connections (for precise local search).
  Think of zooming out on a map to cross a continent, then zooming in
  to find a street. You won't need HNSW at your scale, but it's the
  answer to "how does this work at 10M vectors?"
- **Time:** 35 minutes
- **Prerequisites:** 3.1

### 3.3 sqlite-vec: Vector Search That Runs Anywhere

- **Alex Garcia, "I'm Writing a New Vector Search SQLite Extension"**
- https://alexgarcia.xyz/blog/2024/building-new-vector-search-sqlite/index.html
- The design philosophy behind sqlite-vec: pure C, zero dependencies,
  embedded, "fast enough" brute-force search. Directly relevant to your
  architecture (SQLite-based catalog with per-proposition embeddings).
  Read this to understand what sqlite-vec optimizes for and what it
  intentionally doesn't do.
- **Time:** 20 minutes
- **Prerequisites:** 1.4

- **Alex Garcia, "Introducing sqlite-vec v0.1.0"**
- https://alexgarcia.xyz/blog/2024/sqlite-vec-stable-release/index.html
- The stable release announcement with concrete API examples: creating
  vec0 virtual tables, inserting vectors as JSON or BLOBs, running KNN
  queries. This is your implementation reference.
- **Time:** 25 minutes
- **Prerequisites:** 3.3 (first post)

### 3.4 Quantization: Shrinking Vectors Without Losing Quality

- **Pinecone Learn Series, "Product Quantization"**
- https://www.pinecone.io/learn/series/faiss/product-quantization/
- How to compress 768-dimensional float32 vectors by 97% while
  maintaining search quality. Splits vectors into sub-vectors and
  quantizes each independently. Not needed at your current scale,
  but essential knowledge for the "what if we embed the entire catalog
  at multiple granularities" future.
- **Time:** 30 minutes
- **Prerequisites:** 3.1

- **Hugging Face, "Binary and Scalar Embedding Quantization"**
- https://huggingface.co/blog/embedding-quantization
- Practical guide to quantizing embeddings after generation (no
  retraining needed). Binary quantization gives 32x size reduction;
  scalar quantization gives 4x. sqlite-vec supports binary vectors
  natively, making this directly actionable.
- **Time:** 20 minutes
- **Prerequisites:** 3.4 (first post)

---

## Level 4: Structural Similarity and Analogy

This is the hard problem at the center of your project: finding metaphors
that share structure, not just topic. "Argument Is War" and "Negotiation
Is Chess" share structural patterns (strategic moves, opponents,
winning/losing) despite having different source domains.

### 4.1 Why Topic Similarity is Not Structural Similarity

- **Gentner, "Structure-Mapping: A Theoretical Framework for Analogy" (1983)**
- https://groups.psych.northwestern.edu/gentner/papers/Gentner83.2b.pdf
- The foundational cognitive science paper on analogy. Analogy maps
  *relations between objects*, not attributes of objects, from a base
  domain to a target. This is the theoretical grounding for why naive
  embedding similarity (which captures topic/attribute overlap) will
  miss structural parallels. Read for the framework, skim the formalism.
- **Time:** 45 minutes
- **Prerequisites:** None (but benefits from Level 1)

### 4.2 Analogies in Embedding Spaces: What Works and What Doesn't

- **Ethayarajh, "Word Analogies: Understanding King - Man + Woman = Queen"**
- https://kawine.github.io/blog/nlp/2019/06/21/word-analogies.html
- A critical examination of the famous word2vec analogy result. The
  vector arithmetic works less reliably than the popular narrative
  suggests, and the reasons why are instructive. For your project:
  don't expect simple vector subtraction to find structural analogies
  between metaphors. The embedding captures something, but not
  systematic relational structure.
- **Time:** 25 minutes
- **Prerequisites:** 1.3, 1.5

### 4.3 Is Cosine Similarity Even the Right Metric?

- **Steck, Ekanadham & Kallus, "Is Cosine-Similarity of Embeddings Really About Similarity?" (2024)**
- https://arxiv.org/abs/2403.05440
- Shows that cosine similarity of embeddings can produce arbitrary
  results depending on regularization choices and embedding properties.
  The practical takeaway: cosine similarity is a useful starting point,
  not ground truth. For structural similarity search, you may need
  learned metrics or re-ranking on top.
- **Time:** 30 minutes
- **Prerequisites:** 1.4, 2.4

### 4.4 Cross-Encoder Reranking: Precision When You Need It

- **Omar Sanseviero, "Sentence Embeddings: Cross-Encoders and Re-ranking"**
- https://osanseviero.github.io/hackerllama/blog/posts/sentence_embeddings2/
- The retrieve-then-rerank pattern: use fast bi-encoder embeddings for
  recall (find 100 candidates), then use a slow cross-encoder for
  precision (rank the top 10). The cross-encoder sees both texts
  simultaneously, so it captures relationships that independent
  embeddings miss. This is your best near-term path to improving
  structural similarity results without training a custom model.
- **Time:** 30 minutes
- **Prerequisites:** 2.3, 2.4

### 4.5 Matryoshka Embeddings: Flexible Precision

- **Hugging Face, "Introduction to Matryoshka Embedding Models"**
- https://huggingface.co/blog/matryoshka
- Matryoshka models front-load the most important information into the
  first N dimensions, so you can truncate embeddings for fast coarse
  search, then use full-length embeddings for precise reranking. A
  single model gives you both speed and quality. Directly relevant to
  a two-pass search strategy.
- **Time:** 25 minutes
- **Prerequisites:** 2.4, 3.4

- **Kusupati et al., "Matryoshka Representation Learning" (2022)**
- https://arxiv.org/abs/2205.13147
- The original paper. The training trick is elegant: compute loss at
  multiple dimensionalities simultaneously, forcing the model to encode
  the most important information first. Read the intro and method
  sections; skip the exhaustive experiments unless you want the details.
- **Time:** 30 minutes (skim)
- **Prerequisites:** 4.5 (HF blog post)

### 4.6 Reasoning in Continuous Space

- **Hao et al., "Training Large Language Models to Reason in a Continuous Latent Space" (Coconut, 2024)**
- https://arxiv.org/abs/2412.06769
- Replaces chain-of-thought tokens with continuous "thought" vectors,
  enabling breadth-first search over reasoning paths in latent space.
  Speculative but important: if reasoning can happen in embedding space,
  then structural comparison of metaphors might too. This points toward
  a future where analogy detection operates on latent representations
  rather than surface text.
- **Time:** 45 minutes
- **Prerequisites:** 2.1, 2.2, 2.4

---

## Level 5: Frontier -- Where This Is Going

Emerging research that shapes where your project could go in 12-18 months.
Read for strategic awareness, not implementation.

### 5.1 Multimodal Embeddings

- **Pinecone, "Multi-modal ML with OpenAI's CLIP"**
- https://www.pinecone.io/learn/series/image-search/clip/
- CLIP aligns images and text in a shared embedding space using
  contrastive training. The relevance for your project: if a metaphor's
  "source frame" could be represented visually (war, journey, container),
  multimodal embeddings could enable cross-modal search. Find metaphors
  by sketching a diagram.
- **Time:** 30 minutes
- **Prerequisites:** 2.4

### 5.2 Embedding Alignment Across Models

- **Jha & Zhang, "Harnessing the Universal Geometry of Embeddings" (2025)**
- https://arxiv.org/abs/2505.12540
- Demonstrates unsupervised translation between different embedding
  spaces without paired data. Practical implication: if you embed your
  catalog with model A today and model B comes out tomorrow, you may not
  need to re-embed everything. Also enables combining embeddings from
  different models for ensemble search.
- **Time:** 35 minutes
- **Prerequisites:** 2.4, 4.3

### 5.3 The Platonic Representation Hypothesis

- **Huh et al., "The Platonic Representation Hypothesis" (2024)**
- https://arxiv.org/abs/2405.07987
- Argues that neural network representations are converging across
  architectures, training methods, and even modalities toward a shared
  geometric structure. If true, this means your embeddings are tapping
  into something real about the structure of concepts -- not just
  artifacts of a particular model. Philosophically grounding for the
  entire project.
- **Time:** 45 minutes
- **Prerequisites:** 2.4, 5.2

### 5.4 Reasoning-Enhanced Embeddings

- **ReasonEmbed: "Enhanced Text Embeddings for Reasoning-Intensive Document Retrieval" (2025)**
- https://arxiv.org/abs/2510.08252
- Trains embedding models specifically for queries that require reasoning
  (not just keyword matching). Uses synthesized training data with varying
  "reasoning intensity." Directly relevant: finding structurally similar
  metaphors is a reasoning-intensive retrieval task. This is the closest
  current research to what your project needs.
- **Time:** 40 minutes
- **Prerequisites:** 2.4, 4.4

- **Large Reasoning Embedding Models (LREM): "Towards Next-Generation Dense Retrieval" (2025)**
- https://arxiv.org/abs/2510.14321
- Takes it further: generates chain-of-thought reasoning before embedding,
  using the reasoning as a "semantic bridge" between query and target.
  Deployed at scale on Alibaba. The reasoning-then-embedding paradigm
  could transform how you search for structural analogies.
- **Time:** 40 minutes
- **Prerequisites:** 2.4, 4.6, 5.4 (first paper)

---

## Suggested Reading Order

For someone with limited time, read these in order. Each builds on the last.

| # | Item | Time | Running total |
|---|------|------|---------------|
| 1 | 3Blue1Brown: Vectors (1.1) | 17 min | 17 min |
| 2 | Willison: Embeddings (1.2) | 30 min | 47 min |
| 3 | Alammar: Illustrated Word2vec (1.3) | 45 min | 1h 32m |
| 4 | Dataquest: Similarity metrics (1.4) | 20 min | 1h 52m |
| 5 | Alammar: Illustrated Transformer (2.1) | 60 min | 2h 52m |
| 6 | Raschka: Encoder vs Decoder (2.2) | 25 min | 3h 17m |
| 7 | Weng: Contrastive Learning (2.4) | 60 min | 4h 17m |
| 8 | HF: MTEB benchmark (2.5) | 20 min | 4h 37m |
| 9 | Garcia: sqlite-vec design (3.3) | 20 min | 4h 57m |
| 10 | Pinecone: HNSW (3.2) | 35 min | 5h 32m |
| 11 | Gentner: Structure-Mapping (4.1) | 45 min | 6h 17m |
| 12 | Sanseviero: Cross-encoder reranking (4.4) | 30 min | 6h 47m |
| 13 | HF: Matryoshka embeddings (4.5) | 25 min | 7h 12m |
| 14 | Platonic Representation Hypothesis (5.3) | 45 min | 7h 57m |

**Total core path: ~8 hours of reading.**

The remaining items are valuable but can be read on-demand as specific
questions arise during implementation.

---

## How This Maps to Your Project

| Project decision | Key readings |
|-----------------|-------------|
| Which embedding model to use | 2.5 (MTEB), 2.6 (Boykis book) |
| Whether sqlite-vec is sufficient | 3.1, 3.2, 3.3 |
| Why "similar metaphors" search returns topically similar but structurally different results | 4.1 (Gentner), 4.2 (analogy limits), 4.3 (cosine pitfalls) |
| How to improve search quality without training a custom model | 4.4 (cross-encoder reranking), 4.5 (Matryoshka two-pass) |
| Whether to invest in fine-tuning | 2.4 (contrastive learning), 5.4 (reasoning embeddings) |
| Long-term architecture bets | 5.2 (model alignment), 5.3 (Platonic hypothesis), 4.6 (Coconut) |
