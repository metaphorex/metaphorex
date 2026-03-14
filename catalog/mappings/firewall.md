---
author: fshot
categories:
- software-engineering
- security
contributors: []
created: '2026-03-07'
kind: dead-metaphor
name: Firewall
related: []
slug: firewall
source_frame: architecture-and-building
target_frame: network-security
updated: '2026-03-10'
---

## What It Brings

Security as barrier: something placed between danger and what you're
protecting. Physical, spatial, binary: fire side / safe side.

- **Binary separation** — a literal firewall is a fireproof wall between
  buildings, designed to stop fire from spreading. The mapping to network
  security preserves the core structure remarkably well: untrusted
  outside (the internet, the fire), trusted inside (the internal
  network, the building), and a barrier that enforces separation. You
  don't negotiate with a firewall. It simply blocks.
- **Physical-to-digital fidelity** — the structural correspondence is
  unusually tight. Both the source and target have an inside, an
  outside, and a non-negotiable boundary. Few dead metaphors preserve
  their source geometry this faithfully.
- **Instant legibility** — the spatial simplicity makes network security
  *thinkable* for non-specialists. Even a CEO who has never read an RFC
  understands "we're behind the firewall." The metaphor collapses packet
  inspection rules into a single physical image: a wall that fire cannot
  cross.

## Where It Breaks

- **Threats aren't fire** — fire is indiscriminate: it spreads in all
  directions, consuming whatever is combustible, following physics.
  Network threats are targeted, adaptive, and intelligent. An attacker
  probes for specific vulnerabilities, changes tactics when blocked, and
  may already be inside the perimeter. The firewall metaphor assumes the
  threat is *outside*. Modern breaches overwhelmingly start *inside*:
  phishing, compromised credentials, supply chain attacks.
- **Walls are passive** — a physical firewall sits there being
  fireproof. A network firewall must inspect every packet, maintain
  state tables, update rules, and make real-time decisions. Less a wall
  than a fast, paranoid customs officer.
- **The perimeter dissolved** — the barrier metaphor implies a clean
  boundary: inside is safe, outside is dangerous. This held in the 1990s
  when networks had clear edges. It is catastrophically wrong now. Cloud
  services, remote workers, SaaS integrations, and mobile devices have
  dissolved the perimeter. "Zero trust" architecture is an explicit
  rejection of the firewall metaphor: assume nothing is safe, verify
  everything, trust no location.
- **Double death, second life** — the metaphor died once (from literal
  fire barrier to unremarkable technical term), got resurrected in
  networking, and is now dying again as the perimeter model it encodes
  becomes obsolete. Meanwhile it is escaping into casual use ("I need to
  firewall my work from my personal life"), where the binary
  inside/outside framing might actually be *more* appropriate than it is
  in the domain that adopted it.

## Expressions

- "Behind the firewall" — the safe interior, the trusted zone
- "DMZ" — demilitarized zone, another dead military metaphor nested inside
  this one, referring to the network segment between external and internal
  firewalls. The DMZ metaphor imports the idea of a buffer zone between
  hostile territories, which maps well but carries geopolitical baggage
  nobody thinks about anymore.
- "Firewall rules" — the specific allow/deny policies, treated as if they
  were building codes specifying wall materials and thickness
- "Firewalled off from distractions" — the personal-boundary usage, where
  the metaphor has migrated from network security into everyday life
- "Perimeter security" — the broader doctrine that the firewall metaphor
  supports and that zero trust is replacing

## Origin Story

The literal term dates to at least the 17th century: fireproof walls
(brick, stone, later concrete) built between row houses and commercial
buildings to prevent fire from spreading. Building codes still require
them.

The networking usage emerged in the late 1980s. The first commercial
network firewall product (DEC SEAL) appeared in 1992. By the mid-1990s,
"firewall" was standard for any network perimeter security device. The
metaphor was already dead. Nobody setting up a Cisco PIX was thinking
about fire.

The casual personal usage ("I firewall my weekends") appears to have
accelerated in the 2010s, likely via tech culture leaking into general
vocabulary. People who've never configured a network device now use it
without knowing they're extending a metaphor that was itself an extension
of a metaphor.

## References

- Cheswick, W. & Bellovin, S. *Firewalls and Internet Security* (1994) —
  the foundational text, already working with a dead metaphor
- Kindervag, J. "Build Security Into Your Network's DNA: The Zero Trust
  Network Architecture," Forrester Research (2010) — the formal beginning
  of the anti-firewall doctrine