---
slug: permissions-are-keys
name: Permissions Are Keys
kind: metaphor
source_frame: physical-security
applies_to:
  - access-control
categories:
  - security
  - computer-science
author: agent:metaphorex-miner
contributors: []
related:
  - firewall
dead: true
created: '2026-03-18'
updated: '2026-03-18'
grounding: established
harness: Claude Code
transfers:
  - "[source] a physical key has a unique shape that matches exactly one lock mechanism, creating a one-to-one relationship between the credential and the resource it unlocks"
  - "[source] keys can be copied, stolen, or lost, and possession of the key is sufficient for access regardless of who holds it -- the lock authenticates the key, not the person"
  - "[source] a master key opens multiple locks in a hierarchy, enabling centralized authority to override individual access boundaries"
limits:
  - "[source] breaks because physical keys cannot be revoked once copied -- you must change the lock -- while digital permissions can be revoked instantly without altering the protected resource"
  - "[source] misleads because physical keys grant all-or-nothing access (the door opens or it does not), while digital permissions support fine-grained scoping (read but not write, access during business hours, limited to specific records)"
embodied_patterns:
  - matching
  - boundary
  - container
relation_types:
  - enable
  - prevent
structure: boundary
abstraction_level: specific
---

## Transfers

The mapping from physical keys to digital permissions is one of
computing's most deeply embedded metaphors. It is so dead that
practitioners rarely think about metal keys when discussing API keys,
SSH keys, key rotation, or keychains. Yet the physical source domain
continues to structure how access control is designed, discussed, and
misunderstood.

Key structural parallels:

- **Possession equals access** -- a physical key works for anyone who
  holds it. The lock does not check identity; it checks the key's shape.
  This maps directly onto bearer tokens, API keys, and session cookies:
  whoever possesses the credential gains access. The Clinejection supply
  chain attack (2026) demonstrated this when stolen NPM_RELEASE_TOKEN
  and VSCE_PAT credentials gave attackers full publishing access to
  package registries. The tokens worked because possession was
  sufficient -- exactly as a physical key works for a thief.
- **Key hierarchies** -- physical security uses master key systems:
  individual keys open individual doors, sub-master keys open groups,
  and the grand master opens everything. Computing replicates this
  structure in role-based access control (RBAC), where permissions
  cascade through hierarchies. Root access, admin privileges, and
  superuser accounts are all master keys. The metaphor makes these
  hierarchies feel natural and inevitable, even when flat permission
  models might be safer.
- **Key management as infrastructure** -- physical keys require cutting,
  distribution, tracking, and periodic rekeying when employees leave or
  locks are compromised. Digital credentials require generation,
  distribution, storage, rotation, and revocation. The entire practice
  of "key management" in cryptography and access control is organized
  around the physical metaphor, including key ceremony (a formal process
  for creating or distributing high-value keys), key escrow (entrusting
  a copy to a third party), and key rotation (periodically replacing
  credentials to limit exposure).
- **Keychains and key rings** -- a physical keychain bundles multiple
  keys for convenient access. macOS Keychain, GNOME Keyring, and AWS
  KMS all implement this metaphor: a secured container that holds
  multiple credentials, itself protected by a single master credential.
  The physical metaphor makes the concept immediately intelligible:
  one ring to hold many keys, one password to unlock many secrets.

## Limits

- **Keys cannot be revoked; permissions can** -- if someone copies your
  physical house key, your only option is to change the lock. Digital
  permissions can be revoked instantly: deactivate the API key, expire
  the token, remove the role. The physical metaphor creates a mental
  model where revocation feels expensive and disruptive (changing locks),
  when in digital systems it should be cheap and routine. Organizations
  that think in physical-key terms tend to under-rotate credentials
  because the metaphor makes rotation feel like rekeying an entire
  building.
- **Physical keys are all-or-nothing** -- a key either opens a door or
  it does not. There is no "read-only key" for a physical lock. Digital
  permissions support fine-grained scoping: read but not write, access
  during business hours, limited to specific IP ranges, scoped to
  individual resources. The binary nature of the physical metaphor makes
  it harder to think about least-privilege design, where the goal is to
  grant the minimum access necessary. OpenGuard's recommendation of
  "per-session credentials replacing long-lived API tokens" is a move
  away from the master-key mental model toward something the physical
  metaphor cannot easily express.
- **Keys are tangible; permissions are abstract** -- you can see, touch,
  and physically secure a metal key. Digital credentials exist as
  strings of characters that can be invisibly copied, transmitted, and
  stored in unlimited quantities. The physicality of the source domain
  creates a false sense of control. People treat digital keys as if
  they have the same scarcity and trackability as physical keys, when
  in fact a leaked API key can be copied millions of times in seconds.
- **The metaphor hides identity** -- a physical key does not know who
  is using it. Modern access control systems increasingly bind
  credentials to identities (biometrics, multi-factor authentication,
  device attestation), moving beyond what the key metaphor can express.
  The key metaphor encourages designing systems where the credential is
  everything and the holder is nobody -- precisely the vulnerability
  that credential theft exploits.
- **Lock-and-key implies physical proximity** -- you must be at the
  door to use the key. Digital access is location-independent: a stolen
  credential works from anywhere on earth. The spatial constraint of
  the physical metaphor provides a false sense of security that does
  not exist in networked systems.

## Expressions

- "API key" -- a credential string granting access to a web service,
  universally called a "key" though it bears no physical resemblance
  to one
- "Key rotation" -- periodically replacing credentials, borrowing the
  physical practice of rekeying locks
- "SSH keys" / "public key / private key" -- cryptographic key pairs
  where the asymmetric relationship (one locks, the other unlocks) is
  the metaphor's most structurally faithful digital implementation
- "Keychain" / "Key vault" -- credential storage systems named directly
  after physical containers for physical keys
- "Key escrow" -- entrusting a copy of a cryptographic key to a third
  party, borrowing the legal practice of holding assets in escrow
- "Master key" -- an administrative credential granting universal access,
  preserving the physical hierarchy
- "Revoking access" -- the digital capability that the physical metaphor
  struggles to express, since you cannot un-cut a key

## Origin Story

The key metaphor enters computing through cryptography, where "key" has
been used since at least the Caesar cipher to denote the secret that
transforms plaintext into ciphertext. The cryptographic usage predates
digital computing itself -- the Enigma machine's daily key settings were
literal mechanical configurations. When digital access control systems
emerged in the 1960s and 1970s, the key metaphor was already available
and structurally apt.

The physical metaphor deepened as computing infrastructure grew. SSH
(Secure Shell, 1995) introduced "key pairs" for remote authentication.
AWS IAM (2011) organized cloud access around "access keys." OAuth tokens,
JWT tokens, and API keys proliferated through the 2010s, each using the
key vocabulary even as the underlying mechanisms grew increasingly
abstract. The physical metaphor persists because it provides immediate
legibility: everyone understands keys and locks, even if the digital
reality has long outgrown the physical model.

## References

- OpenGuard. "Prompt Injections & Agent Security" (2026) -- discusses
  per-session credentials replacing long-lived API tokens
- Grith.ai. "Clinejection" (2026) -- documents credential theft
  (NPM_RELEASE_TOKEN, VSCE_PAT) in a supply chain attack
- Lampson, B. "Protection," *5th Princeton Symposium on Information
  Sciences and Systems* (1971) -- foundational access control paper
  using capability (key-like) abstractions
- Saltzer, J. & Schroeder, M. "The Protection of Information in
  Computer Systems," *Proceedings of the IEEE* 63(9) (1975) -- defines
  least privilege, a principle the key metaphor struggles to express
