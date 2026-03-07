---
slug: firewall
name: "Firewall"
kind: dead-metaphor
source_frame: fire-safety
target_frame: network-security
categories:
  - software-engineering
author: metaphorex
contributors: []
related:
  - bottleneck
---

## What It Brings

The intuition that security is a BARRIER — something you place between danger
and what you're protecting. Physical, spatial, binary: fire side / safe side.

A literal firewall is a fireproof wall between buildings, designed to stop fire
from spreading. The mapping to network security preserves the core structure
remarkably well: there is an untrusted outside (the internet, the fire), a
trusted inside (the internal network, the building you're protecting), and a
barrier between them that enforces separation. You don't negotiate with a
firewall. You don't reason with it. It simply blocks.

This spatial simplicity is the metaphor's greatest gift. It makes network
security *thinkable* for non-specialists. Even a CEO who has never read an RFC
understands "we're behind the firewall." The metaphor collapses a complex set
of packet inspection rules into a single physical image: a wall that fire
cannot cross.

## Where It Breaks

Fire is indiscriminate. It spreads in all directions, consuming whatever is
combustible, following physics. Network threats are targeted, adaptive, and
intelligent. An attacker probes for specific vulnerabilities, changes tactics
when blocked, and may already be inside the perimeter. A firewall metaphor
assumes the threat is *outside*. Modern breaches overwhelmingly start *inside*
— phishing, compromised credentials, supply chain attacks.

A physical firewall is passive. Once built, it just sits there being
fireproof. A network firewall must actively inspect every packet, maintain
state tables, update rules, and make real-time decisions. It is less a wall
and more a very fast, very paranoid customs officer.

The barrier metaphor also implies a clean perimeter — inside is safe, outside
is dangerous. This was arguably true in the 1990s when networks had clear
boundaries. It is catastrophically wrong now. Cloud services, remote workers,
SaaS integrations, and mobile devices have dissolved the perimeter entirely.
"Zero trust" architecture is an explicit, named rejection of the firewall
metaphor: assume nothing is safe, verify everything, trust no location.

The metaphor died once (from literal fire barrier to unremarkable technical
term), got resurrected in networking, and is now dying again as the perimeter
model it encodes becomes obsolete. Meanwhile it's escaping into casual use —
"I need to firewall my work from my personal life" — where the binary
inside/outside framing might actually be *more* appropriate than it is in
the domain that adopted it.

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

The literal term dates to at least the 17th century, referring to fireproof
walls (brick, stone, later concrete) built between row houses and in
commercial buildings to prevent fire from spreading between units. Building
codes still require them.

The networking usage emerged in the late 1980s. The first commercial network
firewall product (DEC SEAL) appeared in 1992. By the mid-1990s, "firewall"
was the standard term for any network perimeter security device. The metaphor
was already dead by then — nobody setting up a Cisco PIX was thinking about
fire.

The casual personal usage ("I firewall my weekends") appears to have
accelerated in the 2010s, likely via tech culture leaking into general
vocabulary. It's now common enough that people who've never configured a
network device use it without knowing they're extending a metaphor that was
itself an extension of a metaphor.

## References

- Cheswick, W. & Bellovin, S. *Firewalls and Internet Security* (1994) —
  the foundational text, already working with a dead metaphor
- Kindervag, J. "Build Security Into Your Network's DNA: The Zero Trust
  Network Architecture," Forrester Research (2010) — the formal beginning
  of the anti-firewall doctrine
