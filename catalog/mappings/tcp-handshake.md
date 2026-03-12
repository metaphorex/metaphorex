---
slug: tcp-handshake
name: "TCP Handshake"
kind: dead-metaphor
source_frame: social-behavior
target_frame: network-communication
categories:
  - computer-science
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - network-socket
  - network-port
---

## What It Brings

A handshake is the oldest formalized social greeting -- two parties
physically clasp hands to signal mutual recognition, trust, and the
beginning of an interaction. TCP's three-way handshake (SYN, SYN-ACK, ACK)
borrows this social ritual to describe the process by which two hosts
establish a reliable connection. The metaphor was present from TCP's design:
RFC 793 (1981) uses "handshake" explicitly to describe the connection
establishment sequence. The social frame imports several critical features.

Key structural parallels:

- **Bilateral consent** -- a handshake requires both parties to
  participate. One person extending a hand is not a handshake; it is an
  invitation that can be refused. TCP's three-way handshake encodes the
  same requirement: the client sends SYN ("I want to talk"), the server
  responds SYN-ACK ("I acknowledge and I want to talk too"), the client
  completes with ACK ("agreed"). Neither party can unilaterally establish
  a connection. The metaphor makes this mutual-consent requirement
  intuitive.
- **Sequential exchange** -- a physical handshake follows a sequence:
  extend, grasp, release. TCP's handshake follows a sequence: SYN,
  SYN-ACK, ACK. Each step depends on the previous one. You cannot
  skip to the grasp without the extension. The metaphor imports the
  idea that connection establishment is a protocol -- a fixed sequence
  of social gestures, not a single event.
- **Synchronization of state** -- when two people shake hands, they
  synchronize their social state: both know they have been acknowledged,
  both know the interaction has begun. TCP's handshake synchronizes
  sequence numbers: after the three messages, both hosts know the
  other's starting sequence number. The metaphor maps "mutual social
  recognition" onto "mutual state synchronization."
- **Refusal is meaningful** -- declining a handshake is a social signal
  of rejection. A TCP RST (reset) in response to a SYN is a connection
  refusal. The metaphor makes the refusal legible: the other party does
  not want to talk to you.

## Where It Breaks

- **Handshakes are fast; TCP handshakes cost a round trip** -- a physical
  handshake takes a fraction of a second. A TCP handshake requires a
  full network round trip (SYN to server, SYN-ACK back, ACK to server),
  which can take hundreds of milliseconds across continents. The social
  metaphor creates an expectation of instantaneity that the protocol
  cannot deliver. This mismatch is why TLS 1.3 and QUIC worked so hard
  to reduce "handshake" overhead -- the metaphor makes the latency feel
  like a defect rather than a physical constraint.
- **Handshakes can be faked** -- in social contexts, a handshake implies
  good faith. In TCP, the SYN flood attack exploits the handshake
  metaphor's trust assumption: an attacker sends thousands of SYN packets
  with spoofed source addresses, forcing the server to hold half-open
  connections waiting for ACKs that will never arrive. The social
  metaphor provides no frame for this kind of bad-faith mass deception.
  SYN cookies were invented specifically to counter this attack -- a
  technical fix for a problem the metaphor could not anticipate.
- **No identity verification** -- a physical handshake involves seeing the
  other person. You know whom you are shaking hands with. TCP's handshake
  verifies that a host exists at an IP address, but it says nothing about
  identity. The metaphor implies a level of mutual recognition that TCP
  does not provide, which is why TLS was needed on top of TCP to add
  actual authentication. The handshake metaphor was recycled for TLS
  ("TLS handshake"), doubling down on the social frame while addressing
  what the original TCP handshake left out.
- **The three-way structure is arbitrary to the metaphor** -- physical
  handshakes do not have a fixed number of steps. TCP's three-way
  structure is an engineering decision to minimize round trips while
  ensuring bilateral synchronization. The metaphor suggests that three
  steps are natural, but QUIC's zero-RTT handshake and TLS 1.3's
  single-round-trip handshake show that the "three" was a design choice,
  not a structural necessity.

## Expressions

- "Three-way handshake" -- the canonical description of TCP connection
  establishment, so standard that it appears in every networking textbook
- "Handshake failed" -- connection could not be established, treated as
  a social rebuff
- "TLS handshake" -- the extension of the metaphor to encrypted
  connection negotiation, a handshake on top of a handshake
- "Handshake timeout" -- the social greeting taking too long, implying
  rudeness or absence on the other end
- "SYN flood" -- the attack that exploits the trust implicit in the
  handshake metaphor, overwhelming a host with insincere greetings
- "Half-open connection" -- a handshake left incomplete, like an
  extended hand left hanging

## Origin Story

RFC 793 (September 1981), authored by Jon Postel, formally specified TCP
and its connection establishment procedure. The document uses "handshake"
to describe the three-way exchange, drawing on an analogy already
circulating in networking research. The metaphor was natural for a
protocol designed to establish reliable, ordered, connection-oriented
communication between hosts -- exactly the kind of interaction that
begins with a social greeting.

The three-way handshake solved a specific technical problem: how can two
hosts agree on initial sequence numbers without a pre-existing connection?
The answer was a miniature negotiation protocol, and "handshake" gave it
a human face. The term proved so apt that it was reused for every
subsequent connection-establishment protocol: TLS, SSH, WebSocket, and
QUIC all have "handshakes," each borrowing the social metaphor to
describe their own bilateral negotiation sequences.

## References

- Postel, J. RFC 793, "Transmission Control Protocol," 1981
- Bernstein, D.J. "SYN cookies," 1996 -- the defense against handshake
  abuse
- Rescorla, E. RFC 8446, "The Transport Layer Security (TLS) Protocol
  Version 1.3," 2018
- Stevens, W.R. *TCP/IP Illustrated, Volume 1*, Addison-Wesley, 1994
