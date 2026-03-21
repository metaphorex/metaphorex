---
applies_to:
- security-analysis
author: agent:metaphorex-miner
categories:
- security
- computer-science
contributors: []
created: '2026-03-18'
grounding: folk
harness: Claude Code
kind: metaphor
limits:
- "[source] imports dose-response linearity from pharmacology, but data poisoning often exhibits threshold effects where small contamination has zero impact until a critical mass triggers catastrophic behavior"
- "[source] frames contamination as coming from an external malicious source, but many poisoning attacks exploit the system's own legitimate data ingestion pathways, making the 'poison' indistinguishable from 'food' at the point of entry"
- "[source] implies that an antidote or purification process can neutralize the poison, but in systems like trained ML models or distributed caches, removing the contaminated data does not reliably undo the damage it has already caused"
name: Poison Pill
related:
- trojan-horse
- supply-chain-attack
slug: poison-pill
source_frame: toxicology
transfers:
- "[source] maps the introduction of a toxic substance into a biological system onto the insertion of malicious or corrupted data into a computational system, structuring security thinking around contamination-through-ingestion rather than breach-through-force"
- "[source] imports the toxicological principle that small quantities of the right substance can produce disproportionately large effects, explaining how a few poisoned training examples or cache entries can compromise an entire system"
- "[source] carries the concept of a contamination vector -- the specific pathway by which poison enters the organism -- onto the analysis of how malicious data enters systems through caches, training sets, memory stores, and configuration files"
updated: '2026-03-18'
embodied_patterns:
  - container
  - force
  - boundary
relation_types:
  - prevent
  - transform
structure: boundary
abstraction_level: specific
---

## Transfers

In toxicology, a poison is a substance that causes harm when introduced
into an organism. The dose makes the poison. A small quantity of the
right substance, introduced through the right vector, produces effects
far out of proportion to its volume. The metaphor maps this onto data
contamination attacks across computing.

- **Contamination, not breach** -- the key structural distinction from
  most security metaphors. A firewall is breached. A Trojan horse
  infiltrates. But poison is *ingested*. The system takes it in through
  its normal functions. Memory poisoning, cache poisoning, data
  poisoning, DNS poisoning -- all describe attacks where the malicious
  input enters through legitimate intake pathways. The system is not
  broken into; it is fed something toxic. This reframes the security
  problem from preventing unauthorized access to ensuring the purity of
  authorized inputs.
- **Dose-response dynamics** -- toxicology's central insight is that
  effect depends on dose. The metaphor imports this into security:
  OpenGuard documents memory poisoning attacks achieving "above 95%
  injection success" with carefully crafted inputs. The Clinejection
  attack used cache poisoning to flood targets with 10GB+ of junk data.
  In both cases, a small amount of carefully placed contamination
  produced outsized systemic effects. The metaphor makes this
  disproportionality legible.
- **Vector analysis** -- toxicology studies how poisons enter organisms:
  ingestion, inhalation, injection, absorption. The metaphor maps
  this onto the pathways by which malicious data enters systems.
  Training data poisoning enters through the learning pipeline. Cache
  poisoning enters through the caching layer. Memory poisoning enters
  through conversational context. Each vector requires different
  defenses, just as each exposure route requires different protective
  equipment.
- **Latency and accumulation** -- some poisons act immediately; others
  accumulate over time, with effects appearing long after exposure. The
  metaphor maps this onto attacks like slow data poisoning of ML models,
  where each individual poisoned example has negligible effect but the
  cumulative impact shifts the model's behavior over training cycles.

## Limits

- **Not all poisoning is gradual** -- the toxicological frame suggests
  dose-response curves and accumulation, but many data poisoning attacks
  are binary: a single poisoned DNS record redirects all traffic
  instantly. A single corrupted cache entry serves wrong data to every
  subsequent request. The dose-response model, while useful for ML
  training poisoning, misleads about the many cases where one drop
  is lethal.
- **Purification does not undo damage** -- in toxicology, removing the
  poison (through dialysis, chelation, or simply waiting for
  metabolism) can restore the organism. In computational systems, the
  damage may be irreversible. A poisoned ML model cannot be
  "un-trained" by removing the bad data; it must be retrained from
  scratch. A poisoned cache can be flushed, but the incorrect responses
  it served cannot be recalled. The antidote metaphor breaks at exactly
  the point where practitioners most need guidance.
- **The poison looks like food** -- in toxicology, many poisons are
  identifiable through taste, smell, or chemical testing. In data
  poisoning, the malicious inputs are often indistinguishable from
  legitimate data. A poisoned training example looks exactly like a
  real training example. A poisoned cache entry looks exactly like a
  valid response. The metaphor implies detectability that does not
  exist.
- **The metaphor conflates distinct attack types** -- "poisoning"
  is applied to radically different attacks: DNS cache poisoning
  (corrupting a lookup table), ML training data poisoning (shifting
  a model's learned distribution), memory poisoning in LLMs (injecting
  persistent malicious instructions), and SEO poisoning (manipulating
  search rankings). These share the contamination structure but differ
  in mechanism, detection, and remediation. The single metaphor
  flattens important distinctions.

## Expressions

- "Cache poisoning" -- corrupting a cache to serve incorrect data to
  subsequent consumers, one of the oldest uses of the poison metaphor
  in computing
- "DNS poisoning" -- corrupting DNS records to redirect traffic,
  established terminology since the 1990s
- "Data poisoning" / "training data poisoning" -- corrupting ML training
  sets to manipulate model behavior, increasingly common since 2018
- "Memory poisoning" -- corrupting an LLM's conversational context or
  persistent memory with malicious instructions, documented by OpenGuard
  as achieving above 95% injection success rates
- "Poison pill" -- in corporate finance, a defensive mechanism that
  makes hostile acquisition prohibitively expensive; in computing, any
  deliberately toxic input designed to trigger unwanted behavior
- "Well poisoning" -- the broader folk metaphor of contaminating a
  shared resource to harm all who use it, applied to shared caches,
  package registries, and training data repositories

## Origin Story

The poison metaphor in computing predates the modern cybersecurity
era. "Cache poisoning" as a term dates to the early development of
DNS in the late 1980s and early 1990s, when Dan Kaminsky's work on
DNS cache poisoning (publicly disclosed 2008) brought the concept to
mainstream attention.

The metaphor expanded significantly with the rise of machine learning.
"Data poisoning" appeared in adversarial ML literature around 2017-2018,
describing attacks on training pipelines. The metaphor fit naturally:
ML models ingest data as organisms ingest food, and contaminated input
produces sick output.

The latest extension is to large language models. OpenGuard (2026)
documents "memory poisoning" as a primary attack vector against AI
agents: malicious instructions embedded in conversational context
persist across interactions, effectively poisoning the agent's working
memory. The toxicological metaphor has proven remarkably productive
across three decades and multiple computing paradigms.

## References

- Kaminsky, D. "It's the End of the Cache as We Know It," Black Hat
  (2008) -- DNS cache poisoning disclosure
- Biggio, B. & Roli, F. "Wild Patterns: Ten Years After the Rise
  of Adversarial Machine Learning," *Pattern Recognition* 84 (2018)
  -- survey of data poisoning and adversarial ML
- OpenGuard, "Prompt Injections and Agent Security" (2026) -- memory
  poisoning statistics and taxonomy for AI agents
- Grith.ai, "Clinejection: When Your AI Tool Installs Another" (2026)
  -- cache poisoning in the context of npm supply chain attacks
