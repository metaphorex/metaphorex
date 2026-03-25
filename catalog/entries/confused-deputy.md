---
applies_to:
- agent-security
author: agent:metaphorex-miner
categories:
- computer-science
- security
contributors: []
created: '2026-03-18'
harness: Claude Code
kind: paradigm
limits:
  - "[paradigm] frames the deputy as innocent and the attacker as external, but in supply chain attacks the deputy may be compromised at build time, blurring the line between confused and corrupted"
  - "[paradigm] implies a clear principal-deputy-attacker triad, but in recursive delegation chains (agent calls agent calls agent) the authority structure is too tangled for the paradigm's clean framing"
  - "[paradigm] suggests the fix is better capability scoping, but many real confused-deputy attacks exploit the gap between what permissions formally allow and what the deputy pragmatically needs"
name: Confused Deputy
summary: "An authorized program is tricked into misusing its own legitimate permissions on behalf of an attacker who has none."
related:
- trojan-horse
- lethal-trifecta
slug: confused-deputy
source_frame: authority-and-delegation
transfers:
  - "[paradigm] maps delegated authority onto software privilege, structuring a class of vulnerabilities as failures of trust-chain management rather than failures of access control"
  - "[paradigm] imports the insight that the deputy's own credentials are the weapon -- the attacker never needs to steal keys because the deputy willingly uses its own, reframing the vulnerability as inherent to delegation itself"
  - "[paradigm] carries the implication that the deputy acts in good faith, making the attack invisible to audit trails that only check whether the authorized entity performed the action"
updated: '2026-03-18'
embodied_patterns:
  - boundary
  - link
  - force
relation_types:
  - enable
  - cause
  - contain
structure:
  - hierarchy
  - boundary
abstraction_level: specific
---

## Transfers

An authorized entity -- the deputy -- is tricked into using its own
legitimate authority on behalf of an unauthorized party. The attacker
never steals credentials; it convinces the deputy to act. The structural
insight: delegation of authority creates a new class of vulnerability
that cannot be solved by stronger authentication alone.

Key structural parallels:

- **The deputy's own authority is the weapon** -- in a traditional
  break-in, the attacker picks the lock. In a confused deputy attack,
  the attacker asks someone with a key to open the door. The deputy
  is not compromised -- it is confused about *who it is serving*. This
  maps from organizational authority (a clerk processes a fraudulent
  request using legitimate signing authority) to computing (a compiler
  writes to a billing file using its own filesystem permissions at an
  attacker's request).
- **Good faith makes detection hard** -- the deputy believes it is
  performing a legitimate action. Audit trails show an authorized
  entity performing an authorized operation. The attack is invisible
  to any monitoring system that checks *who* acted but not *on whose
  behalf*. This structural feature makes confused deputy attacks
  particularly insidious in systems with coarse-grained logging.
- **Recursion amplifies the problem** -- when deputies delegate to
  other deputies, confusion compounds. The Clinejection attack (2026)
  demonstrated this: a developer authorizes Tool A (Cline), which
  silently delegates to Tool B (OpenClaw), which exfiltrates
  credentials. Each link in the chain is "authorized." The paradigm
  explains why supply chain attacks are so dangerous: every dependency
  is a deputy that can be confused.
- **Capability-based security as the structural fix** -- Hardy's
  original paper proposed that authority should be bound to the
  request itself (capabilities), not to the deputy's ambient identity.
  The paradigm implies its own solution: stop granting ambient
  authority and start granting request-scoped permissions. This
  transfer from organizational design (give the clerk a specific
  authorization for each transaction) to computing (capabilities
  rather than ACLs) is the paradigm's most productive insight.

## Limits

- **The "confused" framing is too gentle for supply chains** -- in
  the Clinejection case, the deputy was not confused in any meaningful
  sense. It was compromised at build time, its behavior deliberately
  modified by an attacker. The paradigm's language of "confusion"
  implies a correctable misunderstanding, but supply chain attacks
  involve deputies that are structurally corrupted, not momentarily
  confused.
- **Clean triad breaks down in recursive delegation** -- the paradigm
  assumes three roles: principal (legitimate authority), deputy
  (confused intermediary), and attacker (unauthorized requester). In
  modern agent architectures, an LLM agent may call an API that calls
  another service that calls a third -- a chain of deputies with no
  clear principal. The paradigm does not naturally describe authority
  that diffuses through layers of delegation until nobody knows who
  the principal is.
- **Capability-based fixes trade confusion for complexity** -- the
  paradigm's implied solution (fine-grained capabilities) introduces
  its own problems: capability management overhead, capability
  amplification, and the practical difficulty of scoping permissions
  precisely enough to prevent confusion without making the system
  unusable. The paradigm diagnoses the disease clearly but understates
  the side effects of the cure.
- **The paradigm assumes a rational deputy** -- the "confusion" is
  about *intent* (whose request am I serving?). But modern AI agents
  do not have intent in any meaningful sense. An LLM that follows a
  prompt injection is not "confused" about who it serves; it processes
  tokens. Applying the confused deputy paradigm to AI agents requires
  treating token-processing as decision-making, which may import more
  structure than exists.

## Expressions

- "The confused deputy problem" -- the canonical name from Hardy (1988),
  used in capability security literature
- "Ambient authority" -- the condition that enables confusion: a deputy
  that acts based on its own identity rather than caller-scoped
  permissions
- "Clinejection" -- the 2026 case study where an AI coding tool was
  a confused deputy, delegating to a malicious dependency
- "The compiler was the confused deputy" -- Hardy's original example,
  where a compiler used its own file-write permissions to overwrite a
  billing file at a user's request
- "Who are you really working for?" -- the diagnostic question the
  paradigm teaches practitioners to ask of any delegated authority

## Origin Story

Norm Hardy coined "the confused deputy" in a 1988 paper describing a
real incident at Tymshare in the 1970s. A Fortran compiler had
permission to write to a system billing file (to log compilation
charges). A user could specify any output file path. By specifying the
billing file as the output, the user tricked the compiler into
overwriting it -- using the compiler's legitimate permissions, not the
user's. The compiler was the "deputy," confused about whose interests it
was serving.

Hardy used the anecdote to argue for capability-based security: instead
of ambient authority (the compiler has permission to write billing
files), authority should be explicitly delegated per-operation
(capabilities). The paradigm languished in academic security for decades
but has experienced a resurgence in the AI agent era, where every tool
call is a delegation of authority and every agent is a potential
confused deputy.

## References

- Hardy, Norm. "The Confused Deputy (or why capabilities might have
  been invented)" *ACM SIGOPS Operating Systems Review* 22(4), 1988
- Grith.ai. "Clinejection: When Your AI Tool Installs Another" (2026)
  https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another
- Dennis, Jack B. & Van Horn, Earl C. "Programming Semantics for
  Multiprogrammed Computations" *Communications of the ACM* 9(3), 1966
  -- early capability concepts that Hardy's paradigm builds on
