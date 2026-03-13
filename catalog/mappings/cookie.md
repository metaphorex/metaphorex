---
slug: cookie
name: "Cookie"
kind: dead-metaphor
source_frame: food-and-cooking
target_frame: computing
categories:
  - software-engineering
  - linguistics
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related: []
---

## What It Brings

A web cookie is a small piece of data stored on a user's browser by a
website. The name traces through two layers: Unix "magic cookies" (opaque
tokens passed between programs) borrowed from fortune cookies (baked
treats containing hidden messages). The metaphor maps the physical
properties of a cookie -- small, given to you by someone else, containing
something you did not put there -- onto a data token with the same
structural properties.

- **Small and numerous** -- cookies are individually insignificant but
  collectively substantial. A single cookie is a few kilobytes; a
  browser accumulates hundreds. The food metaphor captures the scale
  relationship: one cookie is a snack, a jar full is a supply. Nobody
  worries about one cookie. The privacy problem is the jar.
- **Given, not requested** -- in the food domain, someone offers you a
  cookie. You receive it; you did not ask for it or choose its contents.
  Web cookies work identically: the server sets the cookie on your
  browser without your active participation. The hospitality frame (here,
  have a cookie) masks the asymmetry of the exchange. The server chose
  what to put inside. You just accepted what was offered.
- **Hidden contents** -- fortune cookies contain messages invisible from
  the outside. Web cookies contain tracking data, session identifiers,
  and preference flags that users cannot see without developer tools.
  The metaphor's structural correspondence is precise: the container is
  opaque, the contents are meaningful to the giver, and the receiver
  carries the message without reading it.

## Where It Breaks

- **Cookies are not gifts** -- the food metaphor frames cookies as
  something pleasant that someone gives you. This framing is exactly
  wrong for third-party tracking cookies, which serve the interests of
  the giver, not the receiver. A more honest metaphor would be "tag" or
  "tracer" -- something placed on you for someone else's benefit. The
  warm, domestic connotation of "cookie" has actively impeded public
  understanding of web tracking. Cookie consent banners are fighting
  against the metaphor's built-in friendliness.
- **You cannot refuse a real cookie and keep visiting** -- in the food
  domain, declining a cookie is socially simple. On the web, refusing
  cookies often means degraded functionality, broken sessions, or
  outright denial of access. The metaphor implies optionality that does
  not exist in practice. "Accept cookies to continue" has no food-domain
  equivalent.
- **Cookies do not follow you home** -- a physical cookie stays where
  you eat it. Third-party cookies follow you across the entire web,
  building a profile of your browsing behavior across unrelated sites.
  The metaphor's spatial containment (a cookie is a thing in one place)
  hides the surveillance architecture that cookies enable. The metaphor
  makes cross-site tracking conceptually invisible because cookies do
  not move in the source domain.
- **The domesticity masks the infrastructure** -- "cookie" evokes
  kitchens, children, comfort. The actual infrastructure is a
  surveillance and advertising ecosystem worth hundreds of billions of
  dollars. The gap between the metaphor's affect (warm, small, harmless)
  and the reality (pervasive tracking, behavioral profiling, data
  brokerage) is one of the largest in computing terminology. No other
  dead metaphor in tech has such a stark mismatch between its
  connotations and its function.

## Expressions

- "Accept cookies" -- the consent prompt that every web user has
  encountered, where the food metaphor makes surveillance sound like
  hospitality
- "Third-party cookie" -- a cookie set by a domain other than the one
  you are visiting, where the "third party" is the uninvited guest at
  the table
- "Cookie jar" -- browser storage for cookies, extending the kitchen
  metaphor with a container image
- "Clear your cookies" -- delete stored tracking data, where "clear"
  maps to emptying the jar
- "Session cookie" -- a cookie that expires when you close the browser,
  as perishable as the food version
- "Cookie-less tracking" -- methods that accomplish the same surveillance
  without the named mechanism, revealing that the problem was never the
  cookie itself

## Origin Story

The lineage runs through three generations. First, Unix systems in the
1970s and 1980s used "magic cookie" for an opaque data token passed
between programs -- a reference to fortune cookies, where you receive a
small object containing a message you did not write. The "magic" prefix
distinguished these from other program data; the "cookie" metaphor
captured their small size and hidden contents.

Lou Montulli, a Netscape engineer, coined the web usage in 1994 when he
needed a mechanism for websites to remember returning visitors. He
borrowed "cookie" from the Unix magic cookie concept. The original
implementation was a simple state-management tool: the server could hand
the browser a small token and ask for it back on the next visit, solving
the statelessness of HTTP.

The metaphor died almost immediately. Within a year, advertisers
discovered that cookies could track users across sites. By the late
1990s, "cookie" meant "web tracking mechanism" to privacy advocates and
"essential web infrastructure" to developers. Neither group was thinking
about baked goods. The EU's 2011 Cookie Directive and GDPR's consent
requirements brought the word to public attention, but by then the
metaphor was so dead that "cookie consent" sounded like a technical
phrase rather than an absurd juxtaposition.

## References

- Montulli, L. "The Irregular Musings of Lou Montulli" (blog) --
  the inventor's account of naming cookies
- Schwartz, J. "Giving Web a Memory Cost Its Users Privacy," *New York
  Times* (2001) -- early reporting on the privacy implications
- RFC 6265, "HTTP State Management Mechanism" (2011) -- the formal
  standard, which uses "cookie" throughout without acknowledging the
  metaphor
- Etymonline, "cookie (n.)" -- traces the food word to Dutch *koekje*,
  diminutive of *koek* (cake)
