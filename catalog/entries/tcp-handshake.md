---
applies_to:
- computing
author: agent:fshot
categories:
- computer-science
- security
contributors: []
created: '2026-03-17'
dead: true
harness: Claude Code
kind: metaphor
name: TCP Handshake
related:
- network-socket
- network-port
slug: tcp-handshake
source_frame: social-behavior
updated: '2026-03-17'
transfers:
  - '[source] the handshake requires bilateral consent -- communication is not something one party does to another but something two parties agree to do together, with a SYN without SYN-ACK being a hand extended into empty air'
  - '[source] the three-phase ritual (initiate, reciprocate, confirm) is the minimum exchange needed for both sides to verify mutual willingness and ability, mirroring the social greeting sequence'
  - '[source] the handshake precedes the conversation -- no data is exchanged until the greeting completes, enforcing trust establishment before substantive exchange'
limits:
  - '[source] breaks because physical handshakes are hard to fake (you see who extends their hand), while TCP handshakes occur over a network where the source address can be forged -- the SYN flood attack exploits this gap between social trust and protocol vulnerability'
  - '[source] misleads because social handshakes convey identity (face, grip, expression), while TCP handshakes authenticate nothing -- the warmth implied by the social metaphor is absent, which is why TLS had to be layered on top'
embodied_patterns:
  - link
  - iteration
  - matching
relation_types:
  - coordinate
  - enable
structure: cycle
abstraction_level: specific
---

## Transfers

Connection establishment as a social greeting ritual. Two strangers meet; each
must signal willingness to communicate before conversation can begin. The
three-way handshake -- SYN, SYN-ACK, ACK -- maps to the social sequence of
offer, acceptance, and confirmation that structures introductions in nearly
every human culture.

- **Bilateral consent** -- a handshake requires both parties to extend a hand.
  TCP requires both hosts to exchange synchronization messages before data can
  flow. The metaphor encodes the fundamental principle: communication is not
  something one party does *to* another; it is something two parties agree
  *to do together*. A SYN without a SYN-ACK is a hand extended into empty
  air -- an unanswered social overture.
- **The three-phase ritual** -- social handshakes follow a protocol: one party
  initiates (extends hand), the other reciprocates (grasps and extends in
  return), and the initiator confirms (completes the clasp). TCP's SYN /
  SYN-ACK / ACK mirrors this precisely. The three phases are not arbitrary;
  they are the minimum exchanges needed for both sides to confirm that both
  sides are willing and able. Fewer phases leave one party uncertain; more
  would be redundant.
- **Trust establishment before exchange** -- in human interaction, the
  handshake precedes the conversation. You do not begin discussing business
  while walking toward a stranger; you wait for the greeting to complete.
  TCP enforces this sequencing: no data payload is exchanged until the
  three-way handshake completes. The handshake is not communication; it is
  the precondition for communication.

## Limits

- **Handshakes are hard to fake** -- in person, you can see who is extending
  their hand. TCP handshakes occur over a network where the source address
  can be forged. The SYN flood attack exploits this gap: an attacker sends
  thousands of SYN packets with spoofed source addresses, and the server
  dutifully allocates resources for each half-open connection, waiting for
  ACKs that will never arrive. The social metaphor implies that initiating
  a handshake is costless and in good faith; TCP's implementation makes it
  an exploitable commitment.
- **Social handshakes convey identity** -- when you shake someone's hand,
  you see their face, read their expression, assess their grip. A TCP
  handshake conveys only that *someone* at an IP address is willing to talk.
  It authenticates nothing. The warmth and trust implied by the social
  metaphor are entirely absent from the protocol. TLS was layered on top
  precisely because the "handshake" was, in identity terms, a handshake
  between strangers wearing masks.
- **Handshakes are instant** -- a physical handshake takes a second. A TCP
  handshake takes at minimum one round-trip time (RTT), which across
  continents can be hundreds of milliseconds. For short-lived connections
  (a single HTTP request), the handshake can take longer than the actual
  data exchange. The social metaphor of a brief greeting masks a performance
  cost that has driven decades of protocol optimization (TCP Fast Open,
  QUIC's zero-RTT handshake).
- **Ending is nothing like unclasping** -- releasing a handshake is
  instantaneous and symmetric. Closing a TCP connection requires its own
  four-way exchange (FIN, ACK, FIN, ACK), with TIME_WAIT states that can
  linger for minutes. The social metaphor covers the greeting but not the
  farewell, and the farewell is where TCP's complexity actually lives.

## Expressions

- "Three-way handshake" -- the canonical name for TCP connection
  establishment, so standard that "three-way" is often dropped and "TCP
  handshake" suffices
- "SYN flood" -- the attack that exploits the handshake's trust assumption,
  named for the packet type used to initiate it
- "Half-open connection" -- a handshake that was started but not completed,
  the TCP equivalent of a hand left hanging
- "Connection refused" -- the server's explicit rejection, a declined
  handshake
- "TLS handshake" -- the cryptographic negotiation layered on top of TCP,
  extending the greeting metaphor to include identity verification and
  cipher suite agreement

## Origin Story

The three-way handshake was specified by Vint Cerf and Bob Kahn in their
foundational TCP design and formalized in RFC 793 (September 1981), authored
by Jon Postel. The RFC describes the SYN/SYN-ACK/ACK exchange in precise
mechanical terms but consistently uses "handshake" as the framing metaphor.

The social metaphor was not Cerf and Kahn's invention. "Handshaking" had been
used in telecommunications since at least the 1960s to describe modem
negotiation sequences -- the audible tones you heard when a dial-up modem
connected were literally called the "handshake." The term migrated from
hardware signaling to protocol design naturally: if modems shake hands, so
can hosts.

RFC 793 cemented the term for TCP specifically, and the three-way handshake
became one of the most taught concepts in computer networking. Every
networking textbook includes the SYN/SYN-ACK/ACK diagram. The metaphor is
so embedded that networking professionals use "handshake" as a literal
technical term and may not consciously recognize its social origin -- until
they encounter a protocol that does *not* use a handshake (UDP), at which
point the absence feels significant, like a stranger who begins talking
without introducing themselves.

## References

- Postel, J. "Transmission Control Protocol," RFC 793 (1981) -- the
  definitive specification of the three-way handshake
- Cerf, V. & Kahn, R. "A Protocol for Packet Network Intercommunication,"
  *IEEE Transactions on Communications* (1974) -- the original TCP design
- CERT Advisory CA-1996-21 "TCP SYN Flooding" -- documentation of the
  handshake's most famous vulnerability
