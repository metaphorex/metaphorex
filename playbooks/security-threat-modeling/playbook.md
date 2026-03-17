---
project_issue: 1400
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Security Threat Modeling -- Metaphors, Paradigms, and Risk Frameworks

## Source Description

Security practitioner discourse: blog posts, academic papers, conference talks,
RFCs, and established risk frameworks. The project focuses on the metaphorical
structures that shape how people reason about, communicate, and mitigate software
security threats.

This is an **archive** project -- a bounded set of well-known security metaphors
and paradigms. The candidate list is curated from three primary source articles
plus established security literature. 13 candidates total.

### Primary Source Articles

1. **OpenGuard: Prompt Injections & Agent Security** (2026)
   https://openguard.sh/blog/prompt-injections/
   Comprehensive agent security threat taxonomy. Documents attack surface
   expansion, source-and-sink analysis, memory poisoning statistics, and
   defense-in-depth baselines for AI agents.

2. **Grith.ai: Clinejection** (2026)
   https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another
   Supply chain attack case study on AI tooling. Documents confused deputy
   recursion, cache poisoning, credential exfiltration, and blast radius
   assessment in a real-world npm supply chain attack.

3. **Simon Willison: The Lethal Trifecta** (2025)
   https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
   Combinatorial risk framework for AI agents: private data + untrusted
   content + external communication. Named after the fire triangle analogy.

### Secondary References

- Norm Hardy, "The Confused Deputy" (1988) -- capability-system concept
- Sandia National Laboratories, "Metaphors for Cyber Security" (SAND2008-5381)
  https://www.osti.gov/servlets/purl/947345
  Workshop cataloging six families of cybersecurity metaphors: military/conflict,
  biological, healthcare, market-based, spatial, physical asset protection.
- Taddeo & Floridi, "War, Health and Ecosystem: Generative Metaphors in
  Cybersecurity Governance" (2020) -- academic analysis of metaphor families
- Lockheed Martin, Cyber Kill Chain (2011) -- sequential attack modeling
- John Kindervag, "Zero Trust Network Architecture" Forrester (2010)
- NIST Cybersecurity Framework
- Fraud triangle literature (Albrecht/Cressey)

## Access Method

### Archive Sources

The source articles are HTML blog posts, directly fetchable. The Sandia report
is a PDF (SAND2008-5381) available from OSTI.gov. There is no single structured
database of security metaphors -- the domain is documented in scattered blog
posts, academic papers, and framework documentation.

The Sandia CyberFest workshop (2008) is the closest thing to a canonical catalog,
identifying six metaphor families (military, biological, healthcare, market,
spatial, physical asset). This informed the categorization of candidates but the
workshop proceedings do not provide individual metaphor entries at the granularity
Metaphorex requires.

### Scraping Script

`scripts/extract_candidates.py` encodes the candidate list derived from the three
primary source articles and cross-referenced against the Sandia taxonomy. The
script is a static dataset (the source articles are prose, not structured data)
that outputs JSON to stdout. It is idempotent.

The script also validates candidates against existing catalog entries by checking
for slug collisions.

### LLM Gap-Fill

0 of 13 candidates are LLM-sourced. All candidates trace to the three primary
source articles cited in the issue, cross-referenced with established security
literature (Hardy 1988, Kindervag 2010, Sandia 2008). Descriptions synthesize
information from multiple sources but do not introduce candidates lacking
archival attestation.

## Extraction Strategy

### What makes a good candidate for this project

A security metaphor worth documenting must satisfy:

1. **The metaphor shapes reasoning** -- practitioners actually think differently
   because of the framing. "Attack surface" makes risk feel geometric/measurable.
   "Defense in depth" makes security feel like layered fortification. These are
   not decorative language; they are load-bearing mental models.

2. **The source domain import is non-obvious** -- the metaphor smuggles in
   assumptions from its source domain that most practitioners never examine.
   "Blast radius" imports the assumption that damage attenuates with distance;
   in software, it often does not. "Zero trust" imports paranoia as architecture.

3. **The metaphor appears in the source articles** -- all candidates must be
   grounded in the three primary source articles or established security
   literature, not generated from LLM knowledge.

### What to avoid

- **Entries already in catalog** -- firewall, ai-safety-is-containment,
  guardrails, jailbreaking, buffer-overflow, trojan-horse, computer-virus-is-
  biological-infection are all excluded.
- **Pure jargon without metaphorical structure** -- "CVE," "CVSS score," "SOC"
  are security terms but lack source-to-target domain mappings.
- **Idioms without structural depth** -- security has colorful language ("script
  kiddie," "black hat") but not all of it carries structural mappings worth
  analyzing.

### Kind assignments

- `cross-field-mapping` -- risk-is-a-triangle (cross-domain structural pattern)
- `paradigm` -- lethal-trifecta, confused-deputy, source-and-sink-analysis
  (named frameworks with specific inventors/origins)
- `metaphor` -- all Layer 2 and Layer 3 candidates (active or dead conceptual
  metaphors with source-to-target mappings)

The issue notes several candidates as "dead-metaphor" but per the schema, `kind`
should be `metaphor` with `dead: true` in frontmatter. The Miner should assess
deadness for each entry.

### Distinguishing from existing entries

Several existing entries are in the same conceptual neighborhood:

| Existing entry | Relationship to new candidate |
|---|---|
| `firewall` | Zero-trust is its explicit rejection |
| `trojan-horse` | Poison-pill is adjacent (toxicology vs warfare) |
| `buffer-overflow` | Source-and-sink-analysis is the broader analytical frame |
| `ai-safety-is-containment` | Prompt-injection is a specific attack vector |
| `computer-virus-is-biological-infection` | Security-is-an-immune-system is the defensive counterpart |

The Miner should cross-reference with `related:` links.

## Schema Mapping

### New frames needed (9)

| Frame | Roles | Notes |
|---|---|---|
| `fire-safety` | heat, fuel, oxygen, suppression, prevention, ignition | Source for risk-is-a-triangle and lethal-trifecta |
| `combinatorial-risk` | necessary-conditions, combination, emergence, threshold, mitigation-by-subtraction | Target for the triangle pattern |
| `agent-security` | prompt-injection, tool-poisoning, memory-poisoning, exfiltration, trust-boundary, sandbox | Target for lethal-trifecta, confused-deputy, prompt-injection |
| `security-analysis` | attack-surface, threat-model, blast-radius, defense-layer, trust-zone, vulnerability, exploit | Target for most Layer 2 entries |
| `authority-and-delegation` | principal, agent, deputy, delegation, revocation, scope, proxy | Source for confused-deputy |
| `logistics` | supply-chain, upstream, downstream, provenance, chain-of-custody, manifest | Source for supply-chain-attack |
| `toxicology` | dose, poison, contamination, vector, antidote, threshold, lethal-dose | Source for poison-pill |
| `access-control` | key, permission, credential, scope, rotation, revocation, token | Target for permissions-are-keys |
| `physical-security` | lock, key, barrier, perimeter, zone, vault, badge | Source for permissions-are-keys |

### Existing frames that will be reused

- `war` -- attack-surface, defense-in-depth, blast-radius
- `fluid-dynamics` -- source-and-sink-analysis
- `biology` -- security-is-an-immune-system
- `medicine` -- prompt-injection
- `social-behavior` -- zero-trust (check if roles cover trust/paranoia concepts;
  if not, a `social-dynamics` frame may be needed)
- `network-security` -- zero-trust target (frame exists)

### Categories that will be reused

- `security` -- all entries
- `computer-science` -- confused-deputy, source-and-sink-analysis, poison-pill, permissions-are-keys
- `software-engineering` -- attack-surface, supply-chain-attack
- `ai-discourse` -- lethal-trifecta, prompt-injection
- `systems-thinking` -- risk-is-a-triangle, defense-in-depth, blast-radius, security-is-an-immune-system
- `organizational-behavior` -- zero-trust

### New categories needed

None.

## Gotchas

1. **Overlap with AI discourse project (issue #601).** The entries `ai-safety-is-
   containment`, `guardrails`, and `jailbreaking` already exist. `prompt-injection`
   is new here because the AI project framed it as an AI metaphor; this project
   frames it as a security metaphor with the injection/medical source domain.
   The Miner should cross-reference with `related:` links.

2. **trojan-horse already exists.** The issue listed it as a Layer 2 candidate
   but an entry was created on 2026-03-16. Excluded from the manifest.

3. **computer-virus-is-biological-infection already exists.** Created 2026-03-17.
   The biological infection angle is covered. The `security-is-an-immune-system`
   candidate is the defensive counterpart and is NOT a duplicate.

4. **Dead metaphor judgment calls.** Several candidates (attack-surface,
   blast-radius, defense-in-depth, permissions-are-keys) are deeply dead --
   practitioners do not think about warfare or physical locks when using them.
   The Miner should set `dead: true` in frontmatter and address deadness
   explicitly in the entry, following the `firewall` entry as a template.

5. **The fire triangle has no single inventor.** Unlike the fraud triangle
   (Albrecht) or lethal trifecta (Willison), the fire triangle emerged from
   fire safety pedagogy without a clear origin. The Miner should note this
   in risk-is-a-triangle's Origin Story.

6. **social-behavior vs social-dynamics frame.** The catalog has a
   `social-behavior` frame. Check whether it covers the trust/paranoia
   concepts needed for zero-trust, or whether a distinct frame is needed.
   The Miner should use the existing frame if its roles fit.

7. **13 candidates -- well under the 100 sub-issue cap.** No overflow handling
   needed.

8. **Reference quality.** The three primary source articles are blog posts, not
   peer-reviewed papers. They are well-researched practitioner writing, but the
   Miner should supplement with academic references where available (Hardy 1988,
   Kindervag 2010, Sandia 2008, Lockheed Martin 2011).

9. **prompt-injection vs injection metaphor.** The entry should cover the broader
   injection pattern (SQL injection, code injection, XSS) not just prompt
   injection. The medical/syringe source domain applies to all injection attacks.
   Prompt injection is the most current and most documented instance.
