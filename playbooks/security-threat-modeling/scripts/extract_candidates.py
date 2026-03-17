# /// script
# requires-python = ">=3.11"
# ///
"""
Extract security threat modeling candidates from curated source articles.

Sources:
  - OpenGuard: Prompt Injections & Agent Security (2026)
    https://openguard.sh/blog/prompt-injections/
  - Grith.ai: Clinejection (2026)
    https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another
  - Simon Willison: The Lethal Trifecta (2025)
    https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
  - Sandia National Laboratories, Metaphors for Cyber Security (2008)
    https://www.osti.gov/servlets/purl/947345

Outputs JSON to stdout. Idempotent.
"""

import json
import sys
from pathlib import Path


# Static dataset derived from the source articles.
# The source articles are prose (HTML blog posts), not structured data,
# so this script encodes the extracted candidates directly.

CANDIDATES = [
    {
        "slug": "risk-is-a-triangle",
        "name": "Risk Is A Triangle",
        "kind": "cross-field-mapping",
        "source_frame": "fire-safety",
        "target_frame": "combinatorial-risk",
        "categories": ["systems-thinking", "security"],
        "source": "archive",
        "source_articles": [
            "https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/"
        ],
        "description": (
            "The 'necessary conditions' pattern: N independent conditions, "
            "individually manageable, dangerous only in combination. Fire "
            "triangle (heat+fuel+oxygen), fraud triangle, epidemiological "
            "triad, lethal trifecta. Mitigation is subtraction."
        ),
    },
    {
        "slug": "lethal-trifecta",
        "name": "Lethal Trifecta",
        "kind": "paradigm",
        "source_frame": "fire-safety",
        "target_frame": "agent-security",
        "categories": ["ai-discourse", "security"],
        "source": "archive",
        "source_articles": [
            "https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/"
        ],
        "description": (
            "Willison (2025): private data + untrusted content + external "
            "communication. Structurally isomorphic to fire triangle."
        ),
    },
    {
        "slug": "confused-deputy",
        "name": "Confused Deputy",
        "kind": "paradigm",
        "source_frame": "authority-and-delegation",
        "target_frame": "agent-security",
        "categories": ["computer-science", "security"],
        "source": "archive",
        "source_articles": [
            "https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another"
        ],
        "description": (
            "Norm Hardy (1988). An authorized entity is tricked into misusing "
            "its authority on behalf of an attacker."
        ),
    },
    {
        "slug": "source-and-sink-analysis",
        "name": "Source And Sink Analysis",
        "kind": "paradigm",
        "source_frame": "fluid-dynamics",
        "target_frame": "security-analysis",
        "categories": ["computer-science", "security"],
        "source": "archive",
        "source_articles": [
            "https://openguard.sh/blog/prompt-injections/"
        ],
        "description": (
            "Map untrusted inputs (sources) to dangerous outputs (sinks). "
            "Borrowed from taint analysis in compilers."
        ),
    },
    {
        "slug": "attack-surface",
        "name": "Attack Surface",
        "kind": "metaphor",
        "source_frame": "war",
        "target_frame": "security-analysis",
        "categories": ["security", "software-engineering"],
        "source": "archive",
        "source_articles": [
            "https://openguard.sh/blog/prompt-injections/"
        ],
        "description": (
            "Spatial/geometric: every exposed interface is terrain the "
            "adversary can probe. Makes risk feel measurable (area)."
        ),
    },
    {
        "slug": "supply-chain-attack",
        "name": "Supply Chain Attack",
        "kind": "metaphor",
        "source_frame": "logistics",
        "target_frame": "security-analysis",
        "categories": ["security", "software-engineering"],
        "source": "archive",
        "source_articles": [
            "https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another"
        ],
        "description": (
            "Transitive trust structured as a chain. A single compromised "
            "link poisons everything downstream."
        ),
    },
    {
        "slug": "defense-in-depth",
        "name": "Defense In Depth",
        "kind": "metaphor",
        "source_frame": "war",
        "target_frame": "security-analysis",
        "categories": ["security", "systems-thinking"],
        "source": "archive",
        "source_articles": [
            "https://openguard.sh/blog/prompt-injections/"
        ],
        "description": (
            "Military doctrine (Clausewitz, WWI trench systems) applied to "
            "layered security controls. No single layer is sufficient."
        ),
    },
    {
        "slug": "zero-trust",
        "name": "Zero Trust",
        "kind": "metaphor",
        "source_frame": "social-dynamics",
        "target_frame": "network-security",
        "categories": ["security", "organizational-behavior"],
        "source": "archive",
        "source_articles": [
            "https://openguard.sh/blog/prompt-injections/"
        ],
        "description": (
            "Explicit rejection of the firewall/perimeter metaphor. "
            "'Never trust, always verify.' Kindervag (2010)."
        ),
    },
    {
        "slug": "blast-radius",
        "name": "Blast Radius",
        "kind": "metaphor",
        "source_frame": "war",
        "target_frame": "security-analysis",
        "categories": ["security", "systems-thinking"],
        "source": "archive",
        "source_articles": [
            "https://openguard.sh/blog/prompt-injections/",
            "https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another",
        ],
        "description": (
            "Scope of damage from a single compromise. Spatial metaphor "
            "for impact assessment. Assumes damage attenuates with distance."
        ),
    },
    {
        "slug": "poison-pill",
        "name": "Poison Pill",
        "kind": "metaphor",
        "source_frame": "toxicology",
        "target_frame": "security-analysis",
        "categories": ["security", "computer-science"],
        "source": "archive",
        "source_articles": [
            "https://openguard.sh/blog/prompt-injections/",
            "https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another",
        ],
        "description": (
            "Memory poisoning, cache poisoning, data poisoning -- all use "
            "the toxicology frame. Small contamination, large effect."
        ),
    },
    {
        "slug": "prompt-injection",
        "name": "Prompt Injection",
        "kind": "metaphor",
        "source_frame": "medicine",
        "target_frame": "agent-security",
        "categories": ["security", "ai-discourse"],
        "source": "archive",
        "source_articles": [
            "https://openguard.sh/blog/prompt-injections/",
            "https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/",
        ],
        "description": (
            "Named after SQL injection, which borrows the medical/syringe "
            "metaphor: foreign material injected into a trusted stream."
        ),
    },
    {
        "slug": "security-is-an-immune-system",
        "name": "Security Is An Immune System",
        "kind": "metaphor",
        "source_frame": "biology",
        "target_frame": "security-analysis",
        "categories": ["security", "systems-thinking"],
        "source": "archive",
        "source_articles": [
            "https://openguard.sh/blog/prompt-injections/",
            "https://www.osti.gov/servlets/purl/947345",
        ],
        "description": (
            "Adaptive defense, not static walls. Detect-and-respond vs. "
            "prevent-and-block. The alternative to the perimeter model."
        ),
    },
    {
        "slug": "permissions-are-keys",
        "name": "Permissions Are Keys",
        "kind": "metaphor",
        "source_frame": "physical-security",
        "target_frame": "access-control",
        "categories": ["security", "computer-science"],
        "source": "archive",
        "source_articles": [
            "https://openguard.sh/blog/prompt-injections/",
            "https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another",
        ],
        "description": (
            "Keys, keychains, key rotation, master keys. So dead that "
            "'key' in computing rarely triggers the physical source domain."
        ),
    },
]

# Entries already in the catalog -- excluded from output.
EXISTING_SLUGS = {
    "firewall",
    "ai-safety-is-containment",
    "guardrails",
    "jailbreaking",
    "buffer-overflow",
    "trojan-horse",
    "computer-virus-is-biological-infection",
}


def check_catalog_collisions(catalog_dir: Path) -> list[str]:
    """Check if any candidate slugs collide with existing catalog entries."""
    warnings = []
    if not catalog_dir.exists():
        return warnings
    existing = {p.stem for p in catalog_dir.glob("*.md")}
    for c in CANDIDATES:
        if c["slug"] in existing:
            warnings.append(
                f"WARNING: {c['slug']} already exists in catalog"
            )
    return warnings


def main() -> None:
    # Optional: check for catalog collisions if catalog path provided
    if len(sys.argv) > 1:
        catalog_dir = Path(sys.argv[1])
        warnings = check_catalog_collisions(catalog_dir)
        for w in warnings:
            print(w, file=sys.stderr)

    # Filter out candidates that match existing entries
    output = [c for c in CANDIDATES if c["slug"] not in EXISTING_SLUGS]

    # Strip source_articles (internal metadata, not part of manifest schema)
    for c in output:
        c.pop("source_articles", None)

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
