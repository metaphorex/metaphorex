---
slug: ai-is-an-agent
name: "AI Is an Agent"
kind: conceptual-metaphor
source_frame: governance
target_frame: artificial-intelligence
categories:
  - ai-discourse
  - philosophy
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - ai-is-a-tool
  - ai-is-a-copilot
  - ai-is-an-intern
  - ai-is-an-oracle
---

## What It Brings

An agent acts on behalf of a principal with delegated authority. The
legal concept is precise: an agent has fiduciary duty, operates within
defined scope, and can bind the principal to commitments. The AI
industry adopted "agent" in 2024-2025 to describe systems that take
autonomous multi-step actions -- browsing the web, writing and executing
code, calling APIs, managing workflows -- moving beyond the
request-response pattern of chatbots.

Key structural parallels:

- **Delegated authority** -- an agent acts within scope granted by the
  principal. You tell your real estate agent "find me a house under
  $500K" and they operate within that mandate. The AI agent frame maps
  this onto task delegation: you give the AI a goal ("refactor this
  module," "research this topic," "book a flight") and it takes
  multiple autonomous steps to accomplish it. The frame implies that
  the human defines the objective while the agent chooses the method.
- **The principal-agent relationship** -- in law and economics, the
  principal delegates to the agent because the agent has capabilities
  the principal lacks or cannot efficiently deploy. The frame imports
  this asymmetry: you use an AI agent because it can process
  information faster, access more data, or operate continuously in ways
  you cannot. The delegation is rational, not arbitrary.
- **Scope and constraints** -- agents operate within boundaries. A
  talent agent cannot commit their client to a contract without
  approval. A financial agent cannot invest in prohibited instruments.
  The frame maps onto AI guardrails, permission systems, and
  approval workflows: the agent can act autonomously within defined
  limits but must escalate decisions outside its scope.
- **Accountability flows to the principal** -- when an agent acts within
  scope, the principal bears responsibility for the outcome. When an
  agent exceeds scope, the agent (and potentially the principal) are
  liable. This maps onto the emerging question of AI accountability:
  if an AI agent books the wrong flight or deploys broken code, who is
  responsible? The governance frame provides a vocabulary for answering
  this, even if the answers are not yet settled.
- **The autonomy spectrum** -- the agent frame positions AI at the high
  end of the tool-copilot-agent autonomy progression. A tool waits to
  be used. A copilot assists while the human drives. An agent acts
  independently toward a goal. This progression maps onto the actual
  trajectory of AI product development: from autocomplete to
  assistants to autonomous systems.

## Where It Breaks

- **Legal agents have fiduciary duty; AI agents have no obligations** --
  the core structural import of "agent" is that agents owe duties to
  their principals: loyalty, care, disclosure, obedience. An AI system
  has no legal personhood and owes no duties to anyone. The agent frame
  imports a trust framework that has no enforcement mechanism. When your
  lawyer acts against your interests, you can sue. When your AI agent
  acts against your interests, you have a customer support ticket.
- **Agents can be held accountable; AI cannot** -- a real agent who
  exceeds scope faces consequences: termination, lawsuits, loss of
  license. An AI agent that exceeds scope faces, at most, a bug report.
  The governance frame imports accountability structures that do not
  exist for AI. This is not merely a gap in current law -- it is a
  fundamental category error. Accountability requires moral agency, and
  AI systems are not moral agents regardless of what we call them.
- **The frame normalizes autonomy before trust is earned** -- calling
  something an "agent" implies it has earned the right to autonomous
  action. In human contexts, agency is granted after demonstrated
  competence and is revocable. The AI industry adopted "agent" as a
  marketing term for systems that have not demonstrated the reliability
  that would justify autonomous operation. The frame imports trust that
  has not been established.
- **Agents communicate; AI systems generate** -- a human agent reports
  back to their principal, explains their reasoning, discloses risks,
  and seeks approval for major decisions. AI agents produce outputs that
  look like communication but are statistically generated text. The
  frame imports a communicative relationship that does not exist: when
  an AI agent "explains" its reasoning, it is generating plausible-
  sounding text, not engaging in genuine disclosure.
- **Multi-agent systems strain the metaphor to breaking** -- the current
  trend toward "agent swarms," "agent orchestration," and "multi-agent
  systems" pushes beyond what the governance source domain can support.
  Legal agency is a bilateral relationship between principal and agent.
  A "swarm of agents" has no clear legal analog -- it maps better onto
  organizational theory or ecology than onto governance.

## Expressions

- "AI agents" -- the industry-standard term for autonomous AI systems,
  now the dominant framing in product launches and technical
  documentation
- "Agentic AI" -- adjective form, used to distinguish autonomous systems
  from passive chatbots
- "Give the agent a task" -- framing the interaction as delegation
  rather than query
- "The agent decided to..." -- attributing decision-making to the AI,
  implying intentionality
- "Agent loop" -- the technical pattern of plan-act-observe-repeat,
  named by analogy to an agent working through a task
- "Tool use" -- within the agent frame, the paradoxical sub-metaphor
  where the agent (itself a metaphor) uses tools (also a metaphor)
- "Delegate to the agent" -- management language applied to AI task
  assignment

## Origin Story

"Agent" in AI has a long history, predating LLMs by decades. In
classical AI, an "intelligent agent" was any system that perceives its
environment and takes actions to maximize some objective -- a definition
broad enough to include thermostats. The term was formalized in Russell
and Norvig's *Artificial Intelligence: A Modern Approach* (1995), which
organized the entire field around the agent concept.

The current usage is narrower and more loaded. When the AI industry
began shipping autonomous LLM-based systems in 2024 (AutoGPT, Claude
with tool use, OpenAI's agent APIs), "agent" shifted from a theoretical
abstraction to a product category. The governance connotations --
delegated authority, principal-agent relationships, fiduciary duty --
came along for the ride, whether intended or not.

Maas (2023) categorizes agent-like metaphors under "Operation," noting
that they frame AI as having capacity for independent action. The
progression from tool to copilot to agent tracks the industry's
increasing comfort with AI autonomy, and each step up the ladder
imports more assumptions about reliability and trustworthiness than
the technology currently supports.

## References

- Maas, M. "AI is Like... A Literature Review of AI Metaphors and Why
  They Matter for Policy" (2023) -- catalogs agency metaphors in the
  "Operation" category
- Russell, S. & Norvig, P. *Artificial Intelligence: A Modern Approach*
  (1995) -- formalized the "intelligent agent" framework
- Wooldridge, M. & Jennings, N. "Intelligent Agents: Theory and
  Practice" (1995) -- foundational survey of agent-based AI
