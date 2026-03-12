---
name: assay
description: Review a Miner's mapping PR for quality and correctness
---

Launch the Assayer agent to review a mapping PR.

**Usage:** `/assay <pr-url>`

The Assayer will:

1. Review structural correctness (schema, cross-refs, validation)
2. Evaluate content quality (depth, rigor, grounded expressions)
3. Push fixup commits for mechanical issues
4. Post a GitHub review (approve or request changes)

Invoke the Assayer agent with the PR URL as context.
