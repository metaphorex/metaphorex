import type { APIRoute } from "astro";
import { Octokit } from "@octokit/rest";

export const prerender = false;

const TURNSTILE_SECRET = import.meta.env.TURNSTILE_SECRET;
const GH_TOKEN = import.meta.env.GH_TOKEN;
const REPO_OWNER = "metaphorex";
const REPO_NAME = "metaphorex";

async function verifyTurnstile(token: string, ip: string | null): Promise<boolean> {
  const res = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      secret: TURNSTILE_SECRET,
      response: token,
      ...(ip ? { remoteip: ip } : {}),
    }),
  });
  const data = await res.json();
  return data.success === true;
}

function buildIssueBody(fields: {
  name: string;
  description: string;
  source?: string;
  submitter?: string;
}): string {
  const lines = [
    `## Suggested Metaphor`,
    ``,
    `**Name:** ${fields.name}`,
    `**Description:** ${fields.description}`,
  ];
  if (fields.source) lines.push(`**Source / where encountered:** ${fields.source}`);
  if (fields.submitter) lines.push(`**Submitted by:** ${fields.submitter}`);
  lines.push(``, `---`, `*Submitted via metaphorex.org/suggest*`);
  return lines.join("\n");
}

export const POST: APIRoute = async ({ request }) => {
  // Parse form data
  let body: Record<string, string>;
  try {
    body = await request.json();
  } catch {
    return new Response(JSON.stringify({ error: "Invalid request body" }), {
      status: 400,
      headers: { "Content-Type": "application/json" },
    });
  }

  // Honeypot check — if filled, silently succeed (don't reveal to bots)
  if (body.website) {
    return new Response(JSON.stringify({ ok: true }), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    });
  }

  // Validate required fields
  const name = body.name?.trim();
  const description = body.description?.trim();
  if (!name || !description) {
    return new Response(JSON.stringify({ error: "Name and description are required" }), {
      status: 400,
      headers: { "Content-Type": "application/json" },
    });
  }

  // Verify Turnstile
  const turnstileToken = body["cf-turnstile-response"];
  if (!turnstileToken) {
    return new Response(JSON.stringify({ error: "Turnstile verification required" }), {
      status: 400,
      headers: { "Content-Type": "application/json" },
    });
  }

  const ip = request.headers.get("cf-connecting-ip") || request.headers.get("x-forwarded-for");
  const turnstileOk = await verifyTurnstile(turnstileToken, ip);
  if (!turnstileOk) {
    return new Response(JSON.stringify({ error: "Turnstile verification failed" }), {
      status: 403,
      headers: { "Content-Type": "application/json" },
    });
  }

  // Create GitHub issue
  try {
    const octokit = new Octokit({ auth: GH_TOKEN });
    await octokit.issues.create({
      owner: REPO_OWNER,
      repo: REPO_NAME,
      title: `Suggestion: ${name}`,
      body: buildIssueBody({
        name,
        description,
        source: body.source?.trim() || undefined,
        submitter: body.submitter?.trim() || undefined,
      }),
      labels: ["suggestion"],
    });
  } catch (err) {
    console.error("GitHub issue creation failed:", err);
    return new Response(JSON.stringify({ error: "Failed to submit suggestion" }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }

  return new Response(JSON.stringify({ ok: true }), {
    status: 200,
    headers: { "Content-Type": "application/json" },
  });
};
