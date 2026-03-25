---
slug: permission-delegation-is-genetic-inheritance
name: Permission Delegation Is Genetic Inheritance
summary: "Child processes inherit parent permissions like offspring inherit genes. But permissions should be revocable; genomes are not."
kind: metaphor
source_frame: reproduction
applies_to:
  - software-engineering
categories:
  - software-engineering
  - security
author: agent:metaphorex-miner
contributors: []
related:
  - system-administration-is-feudal-lordship
  - roles-are-theatrical-costumes
created: '2026-03-21'
updated: '2026-03-21'
grounding: folk
harness: Claude Code
provenance: eval-novel-metaphors-2026-03-16
dead: false
transfers:
  - '[source] offspring inherit traits from parents through a deterministic mechanism -- the genome -- with no negotiation or choice by the child, mapping onto child processes and sub-roles that automatically receive the permission set of their parent context'
  - '[source] some traits are dominant (expressed by default) and others are recessive (carried but not expressed unless both alleles are present), mapping onto permissions that are active by default versus capabilities that exist in the role definition but require explicit activation or a second authorization factor'
  - '[source] mutations introduce variation that natural selection acts upon, mapping onto permission drift where inherited role definitions accumulate ad-hoc modifications over time, some beneficial and some pathological, that diverge from the original design'
limits:
  - '[source] breaks because biological inheritance is irreversible -- an organism cannot shed its genome -- while delegated permissions can be revoked instantly, making the metaphor''s connotation of permanence misleading for security design'
  - '[source] misleads because genetic inheritance produces diversity as a feature (variation drives evolution), but permission inheritance should produce uniformity -- divergent permission sets across child processes are a security smell, not a sign of healthy adaptation'
  - '[source] obscures the fact that biological lineage is strictly vertical (parent to child), while permission delegation in real systems is often lateral (peer-to-peer sharing, temporary escalation, cross-team grants) with no genetic analogue'
embodied_patterns:
  - path
  - part-whole
  - superimposition
relation_types:
  - cause
  - enable
  - accumulate
structure: hierarchy
abstraction_level: generic
---

## Transfers

The genetic-inheritance metaphor maps the mechanism by which biological
organisms pass traits to offspring onto the mechanism by which access-control
systems propagate permissions through hierarchies of processes, roles,
and organizational units.

Key structural parallels:

- **Vertical transmission** -- in biology, traits pass from parent to
  offspring through the genome. The child does not choose its eye color
  or blood type; these are determined by the parent's genetic material.
  In access-control systems, a child process inherits the permissions of
  the process that spawned it (Unix fork semantics), a sub-role inherits
  the permissions of its parent role (RBAC inheritance), and a
  sub-organizational unit inherits the policies of its parent OU
  (Active Directory). The metaphor highlights that inheritance is
  automatic and uninvited -- the child does not request permissions,
  it receives them as a birthright.

- **Dominant and recessive traits** -- some genetic traits are expressed
  immediately (dominant alleles), while others are carried silently and
  only expressed under specific conditions (recessive alleles, or
  epigenetic activation). This maps onto the distinction between
  permissions that are active by default in an inherited role versus
  capabilities that are present in the role definition but require
  explicit activation -- a sudo-like escalation, a just-in-time
  access request, or a second approval step. The permission exists
  in the "genome" of the role but is not "expressed" until triggered.

- **Mutation and drift** -- biological genomes accumulate mutations
  over generations. Most are neutral, some are harmful, a few are
  advantageous. In permission systems, inherited role definitions
  accumulate ad-hoc modifications: an emergency exception that was
  never reverted, a temporary escalation that became permanent, a
  permission added for a one-time project that no one removed. Over
  time, the actual permission set of a role diverges from its intended
  design, just as a species' genome diverges from its ancestral
  sequence. This "permission drift" is one of the most common sources
  of security vulnerabilities in enterprise systems.

- **Lineage and provenance** -- geneticists trace traits back through
  family trees to identify where a mutation originated. Security
  auditors trace permissions back through role hierarchies to identify
  where an excessive privilege was introduced. The metaphor imports the
  concept of provenance -- understanding *where* a permission came from
  is as important as knowing that it exists.

## Limits

- **Inheritance is revocable** -- the deepest structural mismatch. An
  organism cannot un-inherit its genome. It carries its parents' genetic
  material for life. But delegated permissions can be revoked instantly,
  and in well-designed systems, should be revoked aggressively (principle
  of least privilege). The metaphor's biological connotation of
  permanence can lead designers to treat inherited permissions as
  immutable defaults rather than as active grants that require ongoing
  justification.

- **Diversity is a bug, not a feature** -- in biology, genetic variation
  across offspring is the engine of evolution. Diversity is the point.
  In permission inheritance, variation across child roles or processes
  is almost always undesirable. If two instances of the same service
  role have different effective permissions, something has gone wrong.
  The metaphor naturalizes divergence that should trigger an audit.

- **Lateral transfer breaks the model** -- biological inheritance is
  strictly vertical: parent to child, through the genome. But real
  permission systems routinely involve lateral transfers: a colleague
  shares a credential, a cross-functional team gets temporary access
  to another team's resources, an API key is passed between services
  at the same hierarchical level. These have no genetic analogue
  (horizontal gene transfer exists in bacteria, but the metaphor
  users are thinking about multicellular organisms). The vertical-only
  connotation blinds designers to the lateral pathways that often
  constitute the actual attack surface.

- **No sexual recombination** -- biological inheritance in sexually
  reproducing organisms involves combining genetic material from two
  parents, producing offspring that are distinct from both. Permission
  inheritance has no meaningful analogue to this. Roles are not
  "mated" to produce new roles with a random combination of both
  parents' permissions. The metaphor suggests more complexity and
  unpredictability in the inheritance mechanism than actually exists.

## Expressions

- "That role inherited admin from its parent OU" -- describing automatic
  permission propagation through organizational hierarchy
- "Permission drift" -- accumulated mutations in inherited role
  definitions over time
- "We need to check the lineage of that privilege" -- tracing the
  provenance of an unexpected permission back through the role hierarchy
- "Dominant permissions are active by default; recessive ones need
  activation" -- distinguishing always-on inherited rights from
  latent capabilities
- "The child process inherits the parent's credentials" -- Unix fork
  semantics described in genetic terms

## References

- Sandhu, Ravi S., et al. "Role-Based Access Control Models." *IEEE
  Computer* 29.2 (1996) -- foundational RBAC model with role hierarchies
  and inheritance semantics
- Ferraiolo, David F., and D. Richard Kuhn. "Role-Based Access Controls."
  *15th NIST-NCSC National Computer Security Conference* (1992) --
  original formalization of role inheritance
- Thompson, Ken. "Reflections on Trusting Trust." *Communications of the
  ACM* 27.8 (1984) -- the deeper problem of inherited trust in system
  lineages
