---
name: curate
description: Triage suggestion issues — review, relabel as nugget, close, or skip
---

Triage open `suggestion`-labeled issues in the metaphorex/metaphorex repo.

**Usage:** `/curate`

## Workflow

1. Fetch all open issues with the `suggestion` label:
   ```
   gh issue list --repo metaphorex/metaphorex --label suggestion --json number,title,body,createdAt --limit 50
   ```

2. If none found, tell the user "No suggestions to triage" and stop.

3. For each suggestion, present a summary:
   - Issue number and title
   - Description (from issue body)
   - Source/attribution (if provided)
   - When submitted
   - **Duplicate check**: search `catalog/entries/` for similar slugs or names.
     Use `grep -il` on the catalog to look for key terms from the suggestion name.
     Also check for open `nugget`-labeled issues with similar titles.

4. Ask the user (using AskUserQuestion) what to do with each suggestion:
   - **nugget** — relabel as `nugget`, remove `suggestion` label. This queues it for the Miner.
   - **close** — close the issue with a comment explaining why (ask the user for the reason, or default to "Does not fit the catalog — not a clear metaphor, pattern, or mental model").
   - **merge <#number>** — merge context into an existing issue, then close this one as duplicate.
   - **skip** — leave it for later.

5. For **nugget**: before relabeling, ask if the user wants to enrich the issue body
   (add context, fix the name, note source/target frames). If yes, draft an updated
   body and confirm before applying.

6. After processing all suggestions, print a summary of actions taken.

## Implementation Notes

- Use `gh issue edit` for relabeling and body updates.
- Use `gh issue close --comment` for closures.
- Do NOT auto-mine — just triage. The Miner picks up nuggets on its own schedule.
- Be concise in your summaries. The user wants to make quick decisions.
