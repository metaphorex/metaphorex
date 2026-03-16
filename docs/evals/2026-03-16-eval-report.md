# Eval Report: Suite A

**Date:** 2026-03-16T19:31:44.303Z
**Results:** 3/10 passed

## Summary

| Test | Result | Found | Missing |
|------|--------|-------|---------|
| blockage-cascade | FAIL | bottleneck, the-pipeline-pattern, data-flow-is-fluid-flow | yak-shaving |
| accumulated-cost | FAIL | technical-debt, compounding, mental-accounting | moral-accounting |
| container-boundary | FAIL | ai-safety-is-containment | relationships-are-enclosures, firewall, activities-are-containers, categories-are-containers |
| threshold-trigger | FAIL | activation-energy, nonlinearity | tipping-point |
| map-territory-reification | PASS | the-map-is-not-the-territory | - |
| transfer-only-debt | PASS | technical-debt, compounding | - |
| limit-only-debt | FAIL | - | technical-debt |
| expression-detection | PASS | technical-debt, the-pipeline-pattern | - |
| cross-domain-structure | FAIL | - | redundancy, jenga |
| adversarial-framing | FAIL | - | argument-is-war, competition-is-competition-for-desired-objects |

## Details

### blockage-cascade FAIL

**Query:** "blockage at one point causes problems everywhere downstream"

**Expected:** bottleneck, the-pipeline-pattern, data-flow-is-fluid-flow, yak-shaving

Top 5 results:

| # | Slug | Section | Score |
|---|------|---------|-------|
| 1 | data-flow-is-fluid-flow | expression | 0.5538 |
| 2 | the-pipeline-pattern | expression | 0.5523 |
| 3 | bottleneck | title | 0.4816 |
| 4 | life-is-a-journey | expression | 0.4778 |
| 5 | difficulties-are-impediments-to-motion | expression | 0.4753 |

### accumulated-cost FAIL

**Query:** "accumulated cost of past shortcuts compounds over time"

**Expected:** technical-debt, compounding, mental-accounting, moral-accounting

Top 5 results:

| # | Slug | Section | Score |
|---|------|---------|-------|
| 1 | technical-debt | transfer | 0.5724 |
| 2 | time-is-money | expression | 0.5468 |
| 3 | compounding | limit | 0.4868 |
| 4 | the-shadow | expression | 0.4741 |
| 5 | mental-accounting | transfer | 0.4681 |

### container-boundary FAIL

**Query:** "boundaries that protect also isolate and trap"

**Expected:** relationships-are-enclosures, firewall, ai-safety-is-containment, activities-are-containers, categories-are-containers

Top 5 results:

| # | Slug | Section | Score |
|---|------|---------|-------|
| 1 | investments-are-containers-for-money | transfer | 0.54 |
| 2 | the-great-mother | transfer | 0.5218 |
| 3 | life-is-a-container | transfer | 0.5081 |
| 4 | shapes-are-containers | limit | 0.4755 |
| 5 | ai-safety-is-containment | transfer | 0.4738 |

### threshold-trigger FAIL

**Query:** "a small input crosses a threshold and triggers a disproportionately large response"

**Expected:** activation-energy, nonlinearity, tipping-point

Top 5 results:

| # | Slug | Section | Score |
|---|------|---------|-------|
| 1 | lollapalooza-effect | transfer | 0.5204 |
| 2 | psychological-forces-are-physical-forces | limit | 0.4682 |
| 3 | nonlinearity | transfer | 0.4664 |
| 4 | neural-network-is-a-brain | transfer | 0.4434 |
| 5 | activation-energy | transfer | 0.436 |

### map-territory-reification PASS

**Query:** "the model becomes confused with the thing it models"

**Expected:** the-map-is-not-the-territory

Top 5 results:

| # | Slug | Section | Score |
|---|------|---------|-------|
| 1 | the-map-is-not-the-territory | expression | 0.5778 |
| 2 | ai-hallucination-is-perception-disorder | expression | 0.5747 |
| 3 | training-is-education | limit | 0.5215 |
| 4 | context-window-is-working-memory | expression | 0.5203 |
| 5 | weights-are-knowledge | expression | 0.5164 |

### transfer-only-debt PASS

**Query:** "interest compounds on deferred work"

**Expected:** technical-debt, compounding

Top 5 results:

| # | Slug | Section | Score |
|---|------|---------|-------|
| 1 | technical-debt | transfer | 0.5053 |
| 2 | compounding | transfer | 0.4062 |
| 3 | faustian-bargain | transfer | 0.3939 |

### limit-only-debt FAIL

**Query:** "the metaphor makes it hard to quantify or prioritize"

**Expected:** technical-debt

Top 5 results:

| # | Slug | Section | Score |
|---|------|---------|-------|
| 1 | morality-is-accounting | limit | 0.6541 |
| 2 | comparison-of-properties-is-comparison-of-physical-properties | limit | 0.61 |
| 3 | importance-is-size | limit | 0.6043 |
| 4 | social-accounting | limit | 0.5891 |
| 5 | comparison-of-properties-is-comparison-of-possessions | limit | 0.5846 |

### expression-detection PASS

**Query:** "we need to pay down our tech debt before the pipeline gets clogged"

**Expected:** technical-debt, the-pipeline-pattern

Top 5 results:

| # | Slug | Section | Score |
|---|------|---------|-------|
| 1 | technical-debt | expression | 0.6532 |
| 2 | the-pipeline-pattern | expression | 0.5479 |
| 3 | software-rot | expression | 0.5135 |
| 4 | the-senex | expression | 0.5055 |
| 5 | the-shadow | expression | 0.4901 |

### cross-domain-structure FAIL

**Query:** "removing one part causes the whole system to collapse"

**Expected:** redundancy, jenga

Top 5 results:

| # | Slug | Section | Score |
|---|------|---------|-------|
| 1 | jenga-code | transfer | 0.549 |
| 2 | coherent-is-whole | expression | 0.5239 |
| 3 | argument-is-a-building | expression | 0.5074 |
| 4 | help-is-support | expression | 0.5048 |
| 5 | organization-is-physical-structure | expression | 0.5003 |

### adversarial-framing FAIL

**Query:** "framing a collaborative activity as a competition with winners and losers"

**Expected:** argument-is-war, competition-is-competition-for-desired-objects

Top 5 results:

| # | Slug | Section | Score |
|---|------|---------|-------|
| 1 | theoretical-debate-is-competition | limit | 0.6055 |
| 2 | competition-is-1-on-1-physical-aggression | limit | 0.5793 |
| 3 | purposes-are-desired-objects | transfer | 0.576 |
| 4 | competition-is-war | transfer | 0.5734 |
| 5 | love-is-war | limit | 0.5692 |

