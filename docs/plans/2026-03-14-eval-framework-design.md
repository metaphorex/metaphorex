# Metaphorex Eval Framework — Design

**Date:** 2026-03-14
**Status:** Draft
**Repo:** `metaphorex/eval` (new, separate repo)

## Problem

We have 408 mappings, 101 frames, and 12 categories in the Metaphorex catalog.
We don't know if this data actually helps anyone do anything better. We need to
measure that.

## Hypotheses

1. LLMs with access to m4x data produce more consistent, structurally faithful
   names for system components than LLMs without it.
2. LLMs with access to "Where It Breaks" sections identify more failure modes
   in metaphor-framed systems than baseline LLMs.
3. LLMs with m4x data detect conceptual metaphors in text with higher
   precision/recall than baseline LLMs.

## Application Tiers

### Tier 1 — High signal, measurable, fast to build

| Application | Measurable how |
|---|---|
| Naming things in a paradigm | Frame consistency, structural fidelity, human preference |
| System weakness identification | Count + quality of failure modes vs baseline |
| Metaphor identification in text | Precision/recall against labeled datasets (VU Amsterdam) |

### Tier 2 — High value, harder to score

| Application | Scoring approach |
|---|---|
| Complex system design | Rubric + LLM-as-judge + human review |
| Audience-adapted explanations | A/B human preference, readability metrics |
| Brainstorming new capabilities | Diversity/coverage metrics, human ranking |
| Threat modeling | Security expert review panel |

### Tier 3 — Interesting but needs careful framing

| Application | Risk |
|---|---|
| Political persuasion/framing | Ethics review needed, sensitive domain |
| Sales & marketing framing | Hard to isolate m4x contribution from general LLM capability |
| Training materials | More of a product than an eval |

## Delivery Formats

| Format | Effort | Best for | Build order |
|---|---|---|---|
| JSON dump (`validate.py extract`) | Done | In-context, fine-tuning prep | 0 |
| Structured pairs (source, target, expressions) | Low | Fine-tuning, embedding | 1st |
| Hugging Face dataset | Medium | Community visibility, reproducibility | 2nd |
| SQLite + embeddings | Medium | RAG experiments | 3rd |
| llms.txt / llms-full.txt | Low | In-context for web-connected models | 2nd (parallel) |
| MCP server | Medium | Tool-use experiments | 3rd (parallel) |
| REST API | High | Production integrations | Later |

## Testing Methodologies

| Method | Cost | Expected signal |
|---|---|---|
| In-context (full dump) | Token cost only | High — tests raw utility |
| Tool use (MCP/function calling) | Low | High — real-world usage pattern |
| RAG (vector search) | Medium (embeddings) | Medium — depends on query quality |
| Fine-tuning small models (Llama 8B, Mistral 7B) | GPU time | High — publishable |
| Fine-tuning large models | $$$ | Lower marginal — large models already know metaphors |

## First Experiment: The Naming Task

**Why first:** Concrete, scorable, compelling. Everyone struggles with naming.

**Setup:**
1. Present a novel system (e.g., "a distributed task queue for ML training jobs")
2. Ask the model to name 10 components using a consistent metaphorical frame
3. Run with 4 conditions:
   - A) Baseline (no m4x data)
   - B) Full corpus in context
   - C) Tool-use (MCP/function call)
   - D) RAG retrieval

**Scoring:**
- **Frame consistency** — do all names come from the same source domain? (automated)
- **Structural fidelity** — do the metaphorical names reflect actual component roles? (LLM-judge)
- **Human preference** — which set of names would you actually use? (survey)

## Second Experiment: "Where It Breaks" Transfer

**Setup:**
1. Give a system description framed with a specific metaphor
2. Ask: "What failure modes does this metaphor smuggle in?"
3. Run with/without m4x "Where It Breaks" sections

**Scoring:**
- Count of distinct failure modes identified
- Novelty (failures NOT in the m4x data)
- Specificity (actionable vs generic)

## Repo Structure

```
metaphorex/eval
├── README.md                    # Mission, hypotheses, how to contribute
├── pyproject.toml               # uv-managed: anthropic, openai, datasets, numpy, rich
├── data/
│   ├── snapshots/               # Pinned CalVer exports from m4x
│   ├── pairs/                   # (source, target, expressions) format
│   ├── baselines/               # Ground truth (VU Amsterdam Metaphor Corpus)
│   └── huggingface/             # Dataset card + push scripts
├── evals/
│   ├── naming/                  # Tier 1: naming task
│   ├── weakness-id/             # Tier 1: failure mode identification
│   └── metaphor-detection/      # Tier 1: metaphor ID in text
├── harnesses/
│   ├── in_context.py            # Full dump into system prompt
│   ├── tool_use.py              # Function-calling interface
│   └── rag.py                   # Vector search retrieval
├── scoring/
│   ├── automated.py             # Metric computation
│   └── llm_judge.py             # LLM-as-judge with configurable rubrics
├── results/                     # Versioned results (committed)
└── .github/workflows/eval.yml   # Manual-dispatch eval runner
```

## Outreach Strategy

**Building in public:** GitHub + HuggingFace + blog + socials

1. Publish repo with hypotheses stated upfront — before results
2. Push dataset to Hugging Face for ML community visibility
3. Blog post: "400+ metaphors. Do they help LLMs reason? We're testing it."
4. Communities to reach:
   - Cognitive linguistics (metaphor detection is active NLP)
   - AI eval community (LMSYS, EleutherAI, HF)
   - Developer tooling (naming, docs, system design)
   - Security (threat modeling angle)

## Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Separate repo | Yes | Different deps, CI, contributors |
| Data coupling | CalVer-pinned snapshots | Eval repo consumes versioned exports, not live files |
| First experiment | Naming task | Concrete, scorable, universally relatable |
| Audience | Practitioners + researchers | Write for devs, rigor for researchers |
