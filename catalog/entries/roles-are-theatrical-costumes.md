---
applies_to:
- access-control
author: agent:metaphorex-miner
categories:
- security
- software-engineering
contributors: []
created: '2026-03-21'
harness: Claude Code
kind: metaphor
name: Roles Are Theatrical Costumes
related:
- security-violations-are-trespassing
slug: roles-are-theatrical-costumes
source_frame: performance
updated: '2026-03-21'
embodied_patterns:
  - container
  - superimposition
  - matching
relation_types:
  - enable
  - transform
  - contain
structure: hierarchy
abstraction_level: generic
transfers:
  - '[source] an actor puts on a costume to become a character, then removes it to return to their own identity, mapping role assignment onto the reversible assumption of a temporary external identity'
  - '[source] costumes constrain what the character can plausibly do on stage -- a king''s robes grant authority that a peasant''s rags do not -- importing the structural principle that roles bound capabilities'
  - '[source] a single actor can wear multiple costumes across scenes, framing multi-role assignment as costume changes rather than identity multiplication'
limits:
  - '[source] breaks because theatrical costumes are visible markers of identity, whereas digital roles are invisible metadata -- a user wearing the admin role looks identical to one wearing a viewer role'
  - '[source] misleads by implying that removing a costume fully reverts identity, when a user who has acted under elevated privileges may have already made irreversible changes that persist after role revocation'
---

## Transfers

In role-based access control, a user does not *become* an administrator.
They *put on* the administrator role, like an actor donning a costume
for a scene. When the scene ends, the costume comes off and the person
underneath is unchanged. This theatrical framing structures how
practitioners think about identity, privilege, and the separability of
who you are from what you can do.

Key structural parallels:

- **Role as external garment** -- in theater, the costume is not the
  actor. It sits on top of the person, modifying their appearance and
  their range of plausible actions without altering their underlying
  identity. RBAC systems make exactly this structural distinction:
  the user object (identity) is separate from the role object
  (capability set). A user "assumes" a role the way an actor "assumes"
  a character. The verb choice is not coincidental.
- **Costume changes as role transitions** -- actors change costumes
  between scenes. Users switch roles between tasks. An engineer who
  needs to deploy to production "puts on" the deployer role, performs
  the deployment, and "takes it off." The temporal structure of theater
  -- acts and scenes with costume changes -- maps onto the principle
  of least privilege: wear only the costume you need for the current
  scene.
- **The wardrobe as the role catalog** -- theaters maintain a wardrobe
  of costumes that any actor can wear. RBAC systems maintain a catalog
  of roles that any user can be assigned. The costume pre-exists the
  actor who wears it, just as the role pre-exists the user who assumes
  it. This makes roles feel like organizational infrastructure rather
  than personal attributes.
- **Costume constrains action** -- a character in a doctor's coat can
  plausibly perform surgery on stage; one in a clown suit cannot. The
  costume does not merely signal identity -- it bounds the range of
  credible actions. Roles work identically: the `admin` role enables
  actions that the `viewer` role does not. The metaphor makes
  capability-bounding feel like a natural theatrical convention rather
  than a security mechanism.

## Limits

- **Costumes are visible; roles are not** -- in theater, the audience
  immediately sees what role someone is playing. In digital systems,
  a user's active roles are invisible unless explicitly queried. This
  means the theatrical intuition that role-holders are recognizable
  at a glance does not transfer, creating a false sense of
  auditability.
- **Taking off the costume does not undo the performance** -- when
  an actor removes a king's robes, the audience's memory of the king
  persists. When a user's admin role is revoked, the database changes
  they made while wearing it are not rolled back. The metaphor
  suggests clean reversibility where none exists, which is exactly
  the gap that audit trails must fill.
- **Actors play one role at a time; users often hold many** -- the
  theatrical convention of one character per actor per scene does not
  match reality. Users frequently hold multiple simultaneous roles,
  and the effective permission set is the union of all of them. The
  costume metaphor obscures this combinatorial explosion by suggesting
  a simpler one-at-a-time model.
- **The metaphor hides role inheritance** -- in theater, there is no
  mechanism by which the king's costume confers the general's powers.
  In RBAC systems, role hierarchies mean that assuming a parent role
  implicitly grants all child-role capabilities. This structural
  feature has no theatrical equivalent, and the metaphor provides no
  intuition for reasoning about inherited permissions.

## Expressions

- "Assume a role" -- the standard term, directly from theatrical
  vocabulary ("assume a character")
- "Role assignment" -- casting the user in a part
- "Principle of least privilege" -- wear only the minimal costume for
  the current scene
- "Role switching" -- changing costumes between tasks
- "Role-based access control" -- organizing the entire permission
  system around the theatrical unit of the role rather than the
  individual actor
- "Elevated privileges" -- a grander costume for a more powerful role
