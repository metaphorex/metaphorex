---
project_issue: 1355
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Playbook: Firefighting Decision Maxims

## Source Description

Wildland and structural firefighting decision maxims -- principally the
**10 Standard Fire Orders** (NWCG PMS 110), the **18 Watch Out Situations**
(NWCG PMS 118), Chief Alan Brunacini's risk management doctrine (codified
in NFPA 1500), and the **NIOSH 5** causal factors from the Fire Fighter
Fatality Investigation and Prevention Program.

These are not metaphors in the Lakoff sense -- they are operational
decision frameworks forged from fatality investigations. Their value to
the catalog is as **mental models and paradigms** that have migrated far
beyond firefighting into incident response, crisis management, software
operations, medicine, and organizational behavior. The fire service
developed these frameworks under the most unforgiving feedback loop
available (people die when the framework fails), which gives them a
rigor and compactness that softer domains borrow.

### Historical Context

The 10 Standard Fire Orders were developed in 1957 by a USDA Forest
Service task force that reviewed 16 tragedy fires between 1937 and 1956.
They were modeled on the US military's General Orders and arranged by
priority: fire behavior awareness first, personal safety second,
organizational control third. The 18 Watch Out Situations were added
later as a companion catalog of specific dangerous conditions, each
derived from fatality investigations.

The Incident Command System (ICS) was developed in the 1970s after
Southern California wildfires exposed coordination failures between
agencies. It was adopted by FEMA as the national standard for all-hazards
response and has migrated into software incident management, hospital
mass-casualty response, and corporate crisis management.

Chief Alan Brunacini (Phoenix Fire Department) drove the creation of
NFPA 1500, the fire service occupational safety standard, and codified
the three-tier risk doctrine: risk a lot to save a lot, risk a little
to save a little, risk nothing to save nothing.

## Access Method

### Primary Archives

**NWCG 10 Standard Firefighting Orders (PMS 110)**
- URL: https://www.nwcg.gov/6mfs/operational-engagement/10-standard-firefighting-orders
- Format: HTML with structured text
- Coverage: All 10 orders with grouping by function (fire behavior,
  fireline safety, organizational control)

**NWCG 18 Watch Out Situations (PMS 118)**
- URL: https://www.nwcg.gov/publications/18-watch-out-situations-pms-118
- Format: HTML with individual situation pages and downloadable poster
- Coverage: All 18 situations with explanatory text

**NPS Combined Reference**
- URL: https://www.nps.gov/articles/firefighting-orders-watchout-situations.htm
- Format: HTML article listing both orders and watch outs
- Coverage: Combined reference page

**Fire Engineering -- NIOSH 5**
- URL: https://www.fireengineering.com/firefighting/the-niosh-5-beyond-firefighter-line-of-duty-deaths/
- Format: Article with case studies illustrating each factor
- Coverage: All 5 factors with incident examples

**FireRescue1 -- Brunacini Impact**
- URL: https://www.firerescue1.com/leadership/articles/the-impact-of-alan-brunacini-MSfWicvv5wuyjKPZ/
- Format: Article
- Coverage: Brunacini's risk doctrine and NFPA 1500 history

**National Fallen Firefighters Foundation -- Everyone Goes Home**
- URL: https://www.firehero.org/fire-service-resources/until-everyone-goes-home/
- Format: Program website
- Coverage: 16 Life Safety Initiatives and cultural change program

### Secondary Sources (not scraped, used for cross-reference)

- NWCG Incident Response Pocket Guide (IRPG), PMS 461
- USFA/FEMA Risk Management Practices in the Fire Service (PDF):
  https://www.usfa.fema.gov/downloads/pdf/publications/risk_management_practices.pdf
- USDA Forest Service Research Paper: "A Genealogy of Wildland Firefighters'
  10 Standard Fire Orders":
  https://research.fs.usda.gov/sites/default/files/2023-03/rmrs-a_geneiology_of_wildland_firefighters_10_standard_fire_orders_508.pdf
- Wikipedia: "Incident Command System"
- FEMA ICS-100 training materials

### Extraction Script

`scripts/extract_firefighting_maxims.py` consolidates the canonical text
of the 10 Orders, 18 Watch Outs, NIOSH 5 factors, Brunacini risk doctrine,
and LCES protocol into structured JSON. The source texts are US government
publications (public domain) and have been stable for decades.

```bash
uv run playbooks/firefighting-maxims/scripts/extract_firefighting_maxims.py
```

## Extraction Strategy

### Selectivity Criteria

The raw source material includes 10 orders, 18 watch out situations,
5 NIOSH factors, 3 Brunacini risk tiers, 4 LCES components, 16 Life
Safety Initiatives, and ICS organizational structure. The manifest
selects 19 candidates that encode transferable reasoning patterns:

1. **Framework-level entries** -- the 10 Orders and 18 Watch Outs as
   complete decision frameworks, not individual items. Individual orders
   are selected only when they encode a standalone transferable insight.

2. **Standalone maxims** -- orders or heuristics that have independent
   metaphorical life outside firefighting (e.g., "fight fire aggressively,
   having provided for safety first" encodes a universal tension between
   aggression and preparation).

3. **Concepts that have migrated** -- ICS, LCES, size-up, mayday,
   freelancing, rehab -- these have been adopted by other domains with
   structural parallels intact.

4. **Meta-insights about safety culture** -- "good luck reinforces bad
   habits," "200 years of tradition unimpeded by progress," "everyone goes
   home" -- these encode insights about institutional behavior that
   transcend firefighting.

### What is NOT included

- Individual Watch Out Situations as separate entries (they are part of
  the 18-WOS framework entry)
- Individual NIOSH 5 factors as separate entries (they are part of the
  NIOSH-5 framework entry)
- The 16 Life Safety Initiatives individually (they are organizational
  policy recommendations, not transferable reasoning patterns; the
  cultural change message is captured in "everyone-goes-home")
- ICS organizational roles (Operations Chief, Planning Chief, etc.) --
  these are job titles, not reasoning patterns
- Fire behavior science (fire triangle, fire weather) -- these are
  physics, not decision heuristics

### For Miners

Each candidate in the manifest has:
- `slug`: filename for `catalog/entries/{slug}.md`
- `name`: the concept as commonly expressed
- `kind`: `mental-model`, `paradigm`, or `metaphor`
- `source_frame` and `target_frame`: existing frames
- `source`: `archive` (from NWCG/NIOSH/NFPA sources) or `llm` (gap-fill)
- `description`: what makes this entry worth writing

**Miner workflow:**

1. For archive-sourced entries, the primary source text is in the
   extraction script output and the NWCG URLs above. Cross-reference
   with the USDA Forest Service genealogy paper for historical context.
2. For each candidate, research its migration path: where has this
   concept been adopted outside firefighting? Software incident response,
   medicine, aviation, military, corporate crisis management?
3. Write Transfers section emphasizing the structural insight that
   transfers, not just the firefighting practice. Many of these
   concepts have been adopted so widely that the firefighting origin
   is forgotten -- the entry should recover it.
4. Write Limits section: where does the firefighting origin mislead
   when applied to other domains? Key tension: firefighting is physical,
   immediate, and life-threatening; most target domains are not.
5. Set `related:` to link within this project (LCES references safety-zone
   and escape-route; NIOSH-5 references incident-command-system;
   fight-fire-aggressively references risk-a-lot-to-save-a-lot) and to
   existing catalog entries (blast-radius, firewall, checklist-approach,
   scenario-analysis, defense-in-depth).
6. Set `provenance: firefighting-maxims` on all entries.

### Batching Recommendation

Process in thematic clusters:

- **Batch 1 -- Core Frameworks (3):** ten-standard-fire-orders,
  eighteen-watch-out-situations, niosh-5. These are the canonical
  source documents and should be mined first for calibration.
- **Batch 2 -- Standalone Orders (3):** fight-fire-aggressively-having-
  provided-for-safety-first, know-what-your-fire-is-doing, base-actions-
  on-current-and-expected-fire-behavior. Individual orders with
  standalone metaphorical life.
- **Batch 3 -- Safety Infrastructure (4):** lces, safety-zone,
  escape-route, anchor-point. The pre-engagement safety protocol and
  its components.
- **Batch 4 -- Risk Philosophy (3):** risk-a-lot-to-save-a-lot,
  good-luck-reinforces-bad-habits, everyone-goes-home. Meta-level
  insights about risk culture.
- **Batch 5 -- Institutional Concepts (4):** incident-command-system,
  two-in-two-out, freelancing, mayday. Organizational structures and
  communication patterns.
- **Batch 6 -- Operations and Culture (3):** size-up, rehab,
  tradition-unimpeded-by-progress. Operational practices and cultural
  self-awareness.

## Schema Mapping

### Kind Assignment

| Category | Kind | Count | Criteria |
|----------|------|-------|----------|
| Decision frameworks | `mental-model` | 14 | Reasoning pattern or diagnostic |
| Organizational paradigms | `paradigm` | 1 | Complete operational system (ICS) |
| Structural metaphors | `metaphor` | 3 | Explicit source-target mapping (anchor-point, safety-zone, escape-route) |
| Aphorisms | `mental-model` | 1 | Compressed insight (tradition-unimpeded-by-progress) |

Most firefighting decision maxims are `mental-model` because they encode
specific reasoning patterns ("if X, then do Y" or "before X, ensure Y").
ICS is a `paradigm` because it is a complete organizational system. The
spatial concepts (anchor point, safety zone, escape route) are `metaphor`
because they map physical firefighting concepts onto abstract domains.

### Frame Inventory

**Existing reusable frames:**
- `fire-safety` -- source frame for all entries
- `decision-making` -- target frame for most entries
- `organizational-behavior` -- target frame for ICS, NIOSH-5, culture entries
- `communication` -- target frame for mayday

**New frames potentially needed:**
- None. Existing frames cover all candidates.

### Categories

Primary categories by cluster:
- All entries: `systems-thinking` (primary)
- Risk/culture entries: `organizational-behavior` (primary or secondary)
- Risk-a-lot, everyone-goes-home: `ethics-and-morality` (secondary)
- Good-luck-reinforces-bad-habits: `psychology` (secondary)

## Gotchas

1. **Overlap with existing entries.** `blast-radius` and `firewall` already
   exist in the catalog with `war` as source frame. These firefighting
   entries are distinct: they come from the fire service's decision-making
   tradition, not from the military explosive/fortification tradition. The
   Miner should use `related:` links to connect but not duplicate.

2. **The 10 Orders are a SYSTEM, not 10 separate entries.** The manifest
   includes the 10 Orders as one framework entry plus 3 individual orders
   that have standalone metaphorical life. The Miner should not create
   10 separate entries. The framework entry should discuss the ordering
   principle (observe-orient-communicate-act) and the structural insight
   that awareness precedes action.

3. **Similarly, the 18 Watch Outs are one entry.** The interesting
   transferable concept is the PRACTICE of maintaining a catalog of
   known-dangerous conditions derived from fatality investigations, not
   any individual watch out situation.

4. **LLM-sourced entries (5 of 19).** Two-in-two-out, size-up, mayday,
   freelancing, and rehab are sourced from LLM knowledge rather than
   directly scraped archives. They are well-established firefighting
   concepts widely documented in fire service literature but were not
   found in the specific NWCG archives scraped. The Surveyor should
   verify they meet the metaphorical depth threshold.

5. **"Fireground" qualifier.** Several terms (freelancing, rehab, size-up)
   have meanings outside firefighting. The entries should use the
   firefighting-specific meaning as the source and discuss how the concept
   transfers. The slug should not include "fireground-" prefix to keep
   slugs clean, but the entry body should clarify the firefighting origin.

6. **19 candidates is well under the 100 sub-issue cap.** No overflow
   handling needed.

7. **US-centric source material.** The 10 Orders, 18 Watch Outs, ICS,
   and NFPA standards are US fire service documents. Other countries have
   their own fire service traditions. The entries should acknowledge the
   US origin without claiming universality.
