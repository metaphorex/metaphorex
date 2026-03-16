# Suite B Analysis: m4x vs Raw Claude

**Date:** 2026-03-16
**Analyst:** Claude Opus 4.6 + human review
**Raw results:** `2026-03-16-suite-b-report.md`

---

## Headline finding

Raw Claude is surprisingly strong. It consistently identifies 6 well-chosen
metaphors with solid limits analysis. The m4x-augmented version is better, but
the improvement is uneven — transformative in one scenario, marginal in others.

---

## Scenario-by-scenario

### 1. microservices-design — roughly equal

Both find the same core metaphors (services-as-agents, circuit breakers, urban
planning, queues). The m4x version reframes "database as filing cabinet" into
"database as commons" — a better framing because it invokes
tragedy-of-the-commons dynamics. But most m4x metaphors are "not in catalog,"
meaning the search results didn't directly contribute.

### 2. fast-growing-team — m4x clearly wins

This is the showcase scenario. Raw Claude produces solid but generic metaphors.
m4x grounds them in specific, named catalog entries:

| Raw Claude says | m4x says (with catalog entry) | Why m4x is better |
|----------------|-------------------------------|-------------------|
| "knowledge is property" | "knowledge is the senex's treasure hoard" | Archetypal framing adds aged-authority-hoarding-wisdom |
| "technical decisions are territory" | "cathedral building" (software-development-is-cathedral-building) | Captures: one master architect, workers don't question |
| *(nothing)* | "royal decrees" (excalibur) | "legitimacy-by-artifact concentrates power dangerously" — Claude would not spontaneously generate this |

Excalibur is the single strongest catalog contribution across all 5 scenarios.

### 3. permissions-system — roughly equal

Raw Claude's "delegation is feudal hierarchy" is arguably better than m4x's
"delegation is gift-giving." Both are strong. The catalog grounding on
"having-control-is-up" is precise but not revelatory.

### 4. ml-model-opacity — mixed

m4x's "predictions are prophecies" (via ai-is-an-oracle) is substantially
better than raw's "model outputs are predictions." The oracle framing adds:
the process was sacred, hidden, not meant to be understood.

But raw Claude's "confidence is emotional certainty" beats m4x's "confidence
is possession" — anthropomorphization is the sharper lens here. And raw's
"production data is natural habitat" with its "digital inbreeding" observation
is more insightful than m4x's "production data is food."

m4x's best insight — "the team is a cargo cult" — didn't come from the catalog.

### 5. code-review-as-war — raw slightly tighter

Should be the catalog's home turf (argument-is-war is one of our richest
entries). But m4x doesn't exploit this. Raw Claude delivers a cleaner analysis.

m4x does produce "code review is performance/theater" — the idea that reviews
are performed for an audience, not conducted as conversations. Arguably the
single most original insight across all 10 responses. Not from catalog.

---

## Five patterns

### 1. The catalog's value is NAMING, not GENERATING

Raw Claude can identify "founders hoarding knowledge." The catalog names it:
"the senex's treasure hoard." Names make metaphors concrete, shareable, and
actionable. This is the catalog's core value proposition.

### 2. Raw Claude's baseline is high

Consistently 6 well-chosen metaphors with decent limits. The m4x improvement
is measured against a strong baseline, not zero.

### 3. m4x shines when the catalog has deep, non-obvious entries

Excalibur, the-senex, cathedral-building — entries encoding specific
cultural/archetypal knowledge that Claude knows but wouldn't spontaneously
retrieve for a given scenario.

### 4. Search noise dilutes the signal

Irrelevant injected results: anger-is-a-heated-fluid-in-a-container for
microservices, love-is-war for code review. Better precision or aggressive
score thresholds would help.

### 5. The most original m4x insights aren't from the catalog

"Cargo cult," "code review as theater," "database as commons" — all "not in
catalog." The catalog primes Claude into deeper metaphorical analysis. This
priming effect is a second-order benefit that's hard to measure but real.

---

## Implications

1. **Raise search precision** — 0.40 threshold is too low. Many injected
   results are noise. 0.50+ or top-5-only filtering would improve signal.

2. **Invest in non-obvious entries** — Excalibur and the-senex added real
   value. Common metaphors (argument-is-war, technical-debt) don't, because
   Claude already knows them.

3. **Measure the priming effect** — Compare "Claude with catalog results" vs
   "Claude told to think about metaphors carefully" to isolate priming from
   retrieval.
