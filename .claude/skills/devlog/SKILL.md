---
name: devlog
description: This skill should be used when the user asks to "write a devlog", "create a devlog entry", "generate the devlog", invokes the "/devlog" command, or wants to create a weekly development log for metaphorex.org. Orchestrates a three-phase workflow (extract, review, synthesize) to produce a devlog draft from session logs, git history, GitHub activity, and ops reports.
version: 0.1.0
---

# Devlog Writing Skill

Create weekly development log entries for metaphorex.org from project activity data. Three-phase workflow: extract week context, quick review with user, synthesize the devlog.

Output destination: `docs/devlog/`

## Argument Parsing

The user may provide a week identifier: `/devlog 2026-W12` or `/devlog` (defaults to the most recent completed week).

To compute the default week: take today's date, subtract 7 days, and use that week's ISO week number. This ensures you're always writing about a completed week, not the current in-progress one.

## Phase 1: Extract

Dispatch the `week-extractor` agent with the target week. It will mine:
- Claude session logs (conversation arcs, steering decisions)
- Git history (commits, file changes)
- GitHub PRs and issues (merged, closed)
- Ops reports (growth, costs, agent activity)
- Plan documents and agent/skill changes

Present the extracted context to the user as a brief summary:
- "Here's what I found for [week]. N sessions, N PRs merged, N issues closed, N entries added."
- List the 3-5 most notable items.
- Ask: "Anything to add, correct, or emphasize?"

Wait for user response before proceeding. If the user says "looks good" or similar, move to Phase 3.

## Phase 2: Incorporate Feedback

If the user adds context, corrections, or emphasis, fold that into the extracted material before synthesizing.

## Phase 3: Synthesize

Generate the devlog entry. Write the file to:

```
docs/devlog/YYYY-WNN.md
```

### Required Frontmatter

```yaml
---
date: YYYY-MM-DD       # Monday of the week
type: devlog
week: YYYY-WNN
title: "A concise headline for the week"
---
```

### Post Structure

```markdown
# [Title]

[Opening: 2-3 sentences capturing the week's theme. What was the dominant
activity? What shifted? Set the scene.]

## By the Numbers

[Synthesized from ops reports — not a copy-paste of the ops tables.
Highlight trends, comparisons to prior weeks, cost efficiency, notable
milestones. 3-5 bullet points.]

## What Shipped

[Group by type: content, pipeline/kaizen, enrichment, infrastructure.
Name specific PRs/issues with numbers. Focus on what matters, not
exhaustive lists. If 50 entries were added, mention the projects they
came from, not every slug.]

## Pipeline & Kaizen

[Which friction was removed? What agent behavior changed? What kaizen
issues were opened or closed? This is the continuous improvement story.]

## Steering Notes

[Decisions made in conversations or plan docs. Direction changes,
editorial choices, architectural decisions. Extracted from session logs
and plan documents. This is the section that would be lost without
the devlog.]

## What's Next

[Open threads, upcoming work, questions to resolve. 2-4 bullet points.]
```

### Section Guidelines

- **By the Numbers** should interpret, not just report. "Cost per entry dropped to $0.24" is better than repeating the ops table.
- **What Shipped** should group intelligently. If 5 PRs were all from the same import project, say "Completed the security-threat-modeling import (PRs #40-#44, 13 entries)" not list each PR.
- **Steering Notes** is the most valuable section. This is context that exists nowhere else in the repo. Extract it carefully from session logs and plan docs.
- **What's Next** should be concrete, not aspirational. Things that are actually queued, not wishes.

### Voice

- Third person plural or project voice. "The catalog grew to 800 entries" not "I added 800 entries."
- Factual and specific. Name PRs, issues, numbers.
- Brief. Each section should be 3-8 lines. The whole devlog should be readable in 2 minutes.
- No hype. If it was a quiet week, say so.

### Omit sections if empty

If there were no kaizen fixes, no steering decisions, or no enrichment work, omit those sections rather than writing "nothing this week." The devlog should only contain sections with substance.

## After Writing

Present the draft inline. Ask: "Want me to adjust anything before committing?"

Do NOT commit automatically. Wait for user approval.

## Backfill Mode

If the user asks to backfill devlogs for past weeks (e.g., "write devlogs for weeks 10-12"), run the extract-review-synthesize cycle for each week. For backfills, skip the review step and generate all drafts, then present them together for review.
