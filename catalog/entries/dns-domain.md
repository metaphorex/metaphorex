---
applies_to:
- computing
author: agent:metaphorex-miner
categories:
- computer-science
contributors: []
created: '2026-03-17'
dead: true
harness: Claude Code
kind: metaphor
name: DNS Domain
summary: "Internet naming borrows feudal governance: domains, zones, delegation, authority. The hierarchy is real but the territory is abstract."
related: []
slug: dns-domain
source_frame: governance
updated: '2026-03-21'
embodied_patterns:
  - boundary
  - center-periphery
  - part-whole
relation_types:
  - contain
  - decompose
structure: hierarchy
abstraction_level: specific
transfers:
  - '[source] feudal governance delegates authority hierarchically from sovereign to vassal, mapping the DNS tree where root delegates to TLDs, TLDs to registrants, registrants to subdomains'
  - '[source] the authoritative source for land records is the sovereign''s registry, mapping the authoritative name server as the one with the right to define truth about its zone'
  - '[source] territorial sovereignty means the lord controls what happens within borders, mapping a domain registrant''s exclusive control over names in their subtree'
limits:
  - '[source] breaks because DNS domains are abstract namespaces that can point anywhere (GeoDNS, anycast), not fixed mappable territory with physical borders'
  - '[source] misleads because revoking feudal authority triggered wars, but DNS delegation changes are operationally trivial database updates -- the metaphor overstates the weight of authority relationships'
---

## Transfers

Internet naming as territorial governance. A domain is a territory of names
over which an authority exercises control. The entire DNS vocabulary --
domains, zones, delegation, authority, root -- imports the structure of feudal
land administration into the architecture of internet naming.

- **Territorial sovereignty** -- in governance, a domain is a territory under
  a single ruler's authority. In DNS, a domain is a subtree of the namespace
  under a single administrative authority. `example.com` is a territory: the
  registrant controls what names exist within it, who can create subdomains,
  and what those names resolve to. The metaphor encodes the correct principle
  that naming power is jurisdictional -- you control your domain and no one
  else's.
- **Hierarchical delegation** -- feudal governance worked through delegation:
  the king delegated authority over a province to a duke, who delegated
  authority over a county to a count. DNS mirrors this exactly. The root zone
  delegates `.com` to Verisign, which delegates `example.com` to the
  registrant, who may delegate `mail.example.com` to a hosting provider. Each
  level of the hierarchy grants authority over a sub-territory while retaining
  authority over the parent.
- **Authoritative records** -- in governance, the authoritative source for
  land records is the sovereign's registry. In DNS, the authoritative name
  server is the one that holds the primary copy of a zone's records. The word
  "authoritative" is used in its political sense: this server has the right
  to define the truth about this territory. Non-authoritative answers (from
  caches) are hearsay -- useful but not definitive.

## Limits

- **Domains are not physical territory** -- land cannot be in two places at
  once. A DNS domain can resolve to different IP addresses depending on where
  you ask (GeoDNS, anycast). The governance metaphor implies a fixed,
  mappable territory; DNS domains are abstract namespaces that can point
  anywhere. The "territory" of `google.com` has no borders and no geography
  -- it is an administrative fiction maintained by consensus.
- **Authority can be stolen** -- in feudal governance, seizing a domain
  required military force. In DNS, domain hijacking can be accomplished
  through social engineering a registrar, exploiting BGP to reroute queries,
  or compromising a name server. The governance metaphor implies that
  authority is stable and enforced by physical power; DNS authority is
  maintained by cryptographic protocols and administrative procedures that
  can be subverted without anyone moving from their desk.
- **The root is not a sovereign** -- the DNS root zone is managed by ICANN
  and operated by thirteen root server operators. There is no single
  sovereign; the root is a committee. The governance metaphor implies a
  hierarchy with a supreme authority at the top, but the actual DNS root is
  a distributed system governed by multistakeholder processes, memoranda of
  understanding, and occasional political controversy. The feudal model has
  a king; DNS has a nonprofit corporation in Los Angeles.
- **Delegation is revocable and instant** -- in feudal governance, revoking
  a vassal's authority over a territory was a political crisis that could
  trigger war. In DNS, delegation is a database record that can be changed
  in minutes. The governance metaphor implies that authority relationships
  are weighty and consequential; DNS delegation is operationally trivial.
  ICANN's removal of a country-code TLD delegation, however, shows that
  the political weight can sometimes match the metaphor.

## Expressions

- "Domain name" -- the human-readable address (example.com), so commonplace
  that "domain" has lost its territorial connotation entirely
- "Top-level domain" (TLD) -- the highest-level partition (.com, .org, .uk),
  the duchies of the internet
- "Subdomain" -- a name within a domain (mail.example.com), a fief within a
  fief
- "Domain registrar" -- the entity that sells naming rights, functioning as
  the land registry office
- "Authoritative name server" -- the server that holds the definitive records
  for a zone, using "authoritative" in its political sense
- "Domain squatting" -- registering a domain with no intent to use it,
  the digital equivalent of claiming unoccupied territory to extract rent
  from future settlers

## Origin Story

The Domain Name System was designed by Paul Mockapetris and documented in
RFC 1035 (November 1987). Before DNS, internet hosts were mapped in a single
flat file (`HOSTS.TXT`) maintained by the Stanford Research Institute. As the
internet grew, this centralized approach became untenable, and Mockapetris
designed a hierarchical, distributed naming system.

The governance vocabulary was deliberate. RFC 1035 uses "domain," "zone,"
"delegation," and "authority" as its core terminology, mapping the
administrative structure of the internet onto the administrative structure
of territorial governance. The hierarchical namespace -- root at the top,
TLDs below, second-level domains below that -- mirrors the hierarchical
structure of political jurisdiction.

The word "domain" entered English from Latin *dominium* (lordship, ownership),
via Old French *domaine*. Its use for internet naming has become so pervasive
that for many people "domain" now primarily means "website address" rather
than "territory under a lord's control." The governance metaphor is
thoroughly dead in casual usage, but it remains alive in the technical
vocabulary of DNS administration, where "authority," "delegation," and "zone"
retain their political charge.

## References

- Mockapetris, P. "Domain Names -- Implementation and Specification,"
  RFC 1035 (1987) -- the foundational DNS specification
- Mockapetris, P. "Domain Names -- Concepts and Facilities," RFC 1034
  (1987) -- the companion conceptual document
- Postel, J. & Reynolds, J. "Domain Requirements," RFC 920 (1984) -- the
  original TLD structure
