---
name: studyplan
description: Generate a progressive study course on any technical topic, from entry-level explainers through essential research papers, tailored to the user's role and project context
---

# Study Plan Generator

Build a progressive reading list for a technical leader who learns by doing.
The output is a structured study course saved to `docs/study/`.

## Process

### 1. Understand the scope

Clarify with the user:
- **Topic**: What specific area? (e.g., "embeddings and vector search", "CRDT-based collaboration", "WebAssembly runtimes")
- **Why now**: What project decision or capability does this support?
- **Current level**: What does the user already know? What's the gap?
- **Time budget**: How many hours for the core path?

If the user already provided this context in conversation, skip the questions.

### 2. Research resources

Use WebSearch to find the best current resources for each level. Prioritize:

| Level | Resource type | Examples |
|-------|--------------|---------|
| Foundations | Visual/interactive explainers, practitioner blog posts | 3Blue1Brown, Jay Alammar, Simon Willison |
| Mechanics | Technical blog posts, official docs | Lilian Weng, Sebastian Raschka, Pinecone Learn |
| Applied | Implementation guides, architecture posts | Alex Garcia, Vicki Boykis, HuggingFace blog |
| Advanced | Research papers with practical implications | arXiv papers with clear abstracts |
| Frontier | Recent papers pointing to where the field is going | 2024-2026 papers, workshop proceedings |

**Quality bar**: Every URL must be real and verifiable via web search. Every resource must teach something the user needs for their specific project, not just be "good to know."

### 3. Structure the course

5 levels, each building on the last:

1. **Foundations** — Build intuition. No math prerequisites. Visual where possible.
2. **How it works** — The machinery. Enough to evaluate tradeoffs.
3. **Engineering** — How to build, deploy, operate.
4. **Advanced** — The hard problems specific to the user's use case.
5. **Frontier** — Where the field is going in 12-18 months.

### 4. For each resource, include:

- Title, author/source
- Verified URL
- 1-2 sentence description: what it teaches AND why it matters for the user's project
- Estimated reading time
- Prerequisites (which earlier items to read first)

### 5. Add summary sections

- **Suggested reading order**: A numbered core path (~8-12 hours) for someone with limited time
- **How this maps to your project**: Table connecting readings to specific decisions the user will face

### 6. Save and commit

Save to: `docs/study/YYYY-MM-DD-<topic-slug>.md`

Use today's date. Commit with:
```
docs: study course on <topic>
```

## Anti-patterns

- Don't pad with "nice to have" resources. Every item earns its place.
- Don't include textbooks unless specific chapters are relevant. Blog posts > books for time efficiency.
- Don't guess URLs. Verify every link with WebSearch.
- Don't make the core path longer than 12 hours. Ruthlessly prioritize.
- Don't include resources that require paid access without flagging it.
