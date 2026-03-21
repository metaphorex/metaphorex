---
slug: heard
name: Heard
kind: pattern
source_frame: food-and-cooking
applies_to:
  - communication
categories:
  - systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
  - andon
created: '2026-03-19'
updated: '2026-03-19'
grounding: established
embodied_patterns:
  - link
  - iteration
  - matching
relation_types:
  - coordinate
  - enable
structure:
  - cycle
abstraction_level: specific
harness: Claude Code
transfers:
  - '[source] a verbal command issued into a noisy, high-tempo environment requires an explicit acknowledgment before the sender can trust it was received, making silence structurally equivalent to failure'
  - '[source] the acknowledgment must echo the content of the command, not merely signal receipt, so that misheard instructions surface immediately rather than propagating as silent errors'
  - '[source] the protocol is symmetric across rank -- a head chef calling "two lobster, one lamb" and a line cook responding "heard, two lobster one lamb" creates a closed loop regardless of hierarchy, making the information flow the authority rather than the person'
limits:
  - '[source] breaks in asynchronous environments where the sender and receiver are not co-present in time, because the closed-loop protocol assumes immediate verbal exchange and has no mechanism for delayed acknowledgment'
  - '[source] assumes commands are unambiguous and short enough to echo verbatim, which fails for complex instructions that require interpretation or judgment before meaningful acknowledgment is possible'
---

## Transfers

In a professional kitchen during service, communication follows a strict
protocol: the expeditor or chef calls an order, and every cook who needs
to act on it responds "heard" (or echoes the order back). This is not
politeness. It is a reliability protocol for an environment where a
dropped instruction means a wrong dish, a late plate, or a cascade of
timing failures across the entire service.

Key structural parallels:

- **Closed-loop communication** -- the fundamental pattern. An open-loop
  command ("fire table seven") provides no feedback about whether it was
  received. A closed-loop command requires acknowledgment before the sender
  can proceed. The kitchen solved this problem independently of aviation
  (readback/hearback protocol) and military radio (roger/wilco), arriving
  at the same structural solution: silence is not consent, silence is
  failure. In software, this maps to TCP vs. UDP -- the "heard" protocol
  is TCP's ACK applied to human communication. Message queues with
  acknowledgment (RabbitMQ's basic.ack, SQS's delete-after-process) encode
  the same principle: a message is not considered delivered until the
  consumer confirms it.

- **Content echo, not just receipt** -- a kitchen "heard" that echoes back
  the order ("heard, two salmon mid-rare") is structurally different from
  a bare acknowledgment ("got it"). The echo forces the receiver to parse
  the instruction and repeat it, surfacing mishearing at the point of
  receipt rather than at the point of delivery. Aviation readback protocol
  uses the same principle: a pilot reads back the altitude assignment, not
  just "roger." The structural insight is that acknowledgment of receipt
  and acknowledgment of understanding are different things, and only the
  latter catches errors.

- **Hierarchy-flattening** -- in a kitchen brigade, the head chef
  outranks the line cooks, but the "heard" protocol treats information
  flow as more important than status. A chef who calls an order and gets
  silence will call it again, louder. The information must close the loop
  regardless of rank. This transfers to incident response: during an
  outage, the incident commander's instructions require verbal
  acknowledgment from the engineer taking the action, regardless of
  seniority.

## Limits

- **Asynchronous communication breaks the loop.** The "heard" protocol
  depends on temporal co-presence -- sender and receiver are in the same
  moment. Slack messages, email, and pull request comments exist in
  asynchronous time where the "I sent it, did they get it?" problem is
  solved differently (read receipts, @-mentions, assignment). Transplanting
  the "heard" expectation into async contexts creates false urgency and
  interrupt-driven culture.

- **Complex instructions resist echoing.** A kitchen order is short and
  formulaic: "two covers, one duck, one bass, fire now." A design review
  comment or architectural decision cannot be meaningfully echoed back in
  the same way. The pattern works for commands, not for discussions. Forcing
  echo-acknowledgment on nuanced communication produces performative
  compliance rather than genuine understanding.

- **Cultural mismatch.** The pattern assumes a shared understanding that
  silence means failure. In many workplace cultures, silence means
  agreement or deference. Importing the kitchen protocol without importing
  the cultural expectation produces confusion: the sender expects an echo,
  the receiver thinks silence is acknowledgment.

## Expressions

- "Heard!" -- the single-word acknowledgment in professional kitchens,
  now spreading to restaurant-adjacent culture and startup teams.
- "Readback/hearback" -- aviation's formalized version of the same
  protocol, mandated by ICAO.
- "Roger" / "Wilco" -- military radio acknowledgment (received /
  will comply), distinguishing receipt from commitment to act.
- "ACK" -- the TCP packet that closes the loop, and occasionally used
  as slang in engineering teams to mean "I received and understood."
- "Say again" -- the explicit request when the loop fails to close,
  used in kitchens ("say again, chef?"), aviation, and military contexts.
