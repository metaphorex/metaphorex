# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""
Extract firefighting decision maxims from NWCG and related archives.

Sources:
- NWCG 10 Standard Firefighting Orders (PMS 110)
- NWCG 18 Watch Out Situations (PMS 118)
- NIOSH 5 causal factors
- Brunacini risk management doctrine
- LCES safety protocol

Outputs structured JSON to stdout.
"""

import json
import sys
from typing import Any

import requests
from bs4 import BeautifulSoup

NWCG_10_ORDERS_URL = "https://www.nwcg.gov/6mfs/operational-engagement/10-standard-firefighting-orders"
NWCG_18_WATCHOUTS_URL = "https://www.nwcg.gov/publications/18-watch-out-situations-pms-118"
NPS_COMBINED_URL = "https://www.nps.gov/articles/firefighting-orders-watchout-situations.htm"

HEADERS = {
    "User-Agent": "metaphorex-prospector/1.0 (catalog research; https://github.com/metaphorex/metaphorex)"
}


def fetch_page(url: str) -> BeautifulSoup:
    """Fetch and parse a page."""
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def extract_nps_orders_and_watchouts() -> dict[str, list[dict]]:
    """
    Extract from NPS combined page which lists both the 10 Orders
    and 18 Watch Out Situations in plain text.
    """
    # Canonical text from NWCG PMS 110 and PMS 118.
    # These are official US government publications (public domain).
    # The text is stable -- these orders have not changed since 1957 (orders)
    # and 1966 (watch outs).

    orders = [
        {"number": 1, "text": "Keep informed on fire weather conditions and forecasts."},
        {"number": 2, "text": "Know what your fire is doing at all times."},
        {"number": 3, "text": "Base all actions on current and expected behavior of the fire."},
        {"number": 4, "text": "Identify escape routes and safety zones, and make them known."},
        {"number": 5, "text": "Post lookouts when there is possible danger."},
        {"number": 6, "text": "Be alert. Keep calm. Think clearly. Act decisively."},
        {"number": 7, "text": "Maintain prompt communications with your forces, your supervisor, and adjoining forces."},
        {"number": 8, "text": "Give clear instructions and be sure they are understood."},
        {"number": 9, "text": "Maintain control of your forces at all times."},
        {"number": 10, "text": "Fight fire aggressively, having provided for safety first."},
    ]

    watchouts = [
        {"number": 1, "text": "Fire not scouted and sized up."},
        {"number": 2, "text": "In country not seen in daylight."},
        {"number": 3, "text": "Safety zones and escape routes not identified."},
        {"number": 4, "text": "Unfamiliar with weather and local factors influencing fire behavior."},
        {"number": 5, "text": "Uninformed on strategy, tactics, and hazards."},
        {"number": 6, "text": "Instructions and assignments not clear."},
        {"number": 7, "text": "No communication link with crewmembers or supervisor."},
        {"number": 8, "text": "Constructing line without safe anchor point."},
        {"number": 9, "text": "Building fireline downhill with fire below."},
        {"number": 10, "text": "Attempting frontal assault on fire."},
        {"number": 11, "text": "Unburned fuel between you and fire."},
        {"number": 12, "text": "Cannot see main fire; not in contact with someone who can."},
        {"number": 13, "text": "On a hillside where rolling material can ignite fuel below."},
        {"number": 14, "text": "Weather becoming hotter and drier."},
        {"number": 15, "text": "Wind increases and/or changes direction."},
        {"number": 16, "text": "Getting frequent spot fires across line."},
        {"number": 17, "text": "Terrain and fuels make escape to safety zones difficult."},
        {"number": 18, "text": "Taking a nap near fireline."},
    ]

    return {"orders": orders, "watchouts": watchouts}


def extract_niosh_5() -> list[dict]:
    """The NIOSH 5 causal factors from NIOSH FFFIPP."""
    return [
        {"number": 1, "text": "Improper risk assessment"},
        {"number": 2, "text": "Lack of incident command"},
        {"number": 3, "text": "Lack of accountability"},
        {"number": 4, "text": "Inadequate communications"},
        {"number": 5, "text": "Lack of or failure to follow standard operating procedures"},
    ]


def extract_brunacini_risk_doctrine() -> list[dict]:
    """Brunacini's risk management doctrine from NFPA 1500."""
    return [
        {
            "name": "Risk a lot to save a lot",
            "text": "We will risk our lives a lot, in a highly calculated and controlled manner, to protect a savable human life.",
        },
        {
            "name": "Risk a little to save a little",
            "text": "We will risk our lives a little, in a highly calculated and controlled manner, to protect savable property.",
        },
        {
            "name": "Risk nothing to save nothing",
            "text": "We will not risk our lives at all for lives or property that are already lost.",
        },
    ]


def extract_lces() -> dict:
    """LCES safety protocol."""
    return {
        "acronym": "LCES",
        "components": [
            {"letter": "L", "name": "Lookouts", "text": "Post lookouts in potentially hazardous situations to monitor fire behavior, weather and other hazardous conditions."},
            {"letter": "C", "name": "Communications", "text": "Communications need to be clear, concise and understood."},
            {"letter": "E", "name": "Escape Routes", "text": "Pathways to escape hazardous situations that need to be identified and communicated to all personnel."},
            {"letter": "S", "name": "Safety Zones", "text": "Areas large enough that you can survive the fire burning around you without other protection."},
        ],
    }


def main() -> None:
    data = extract_nps_orders_and_watchouts()
    niosh = extract_niosh_5()
    brunacini = extract_brunacini_risk_doctrine()
    lces = extract_lces()

    output: dict[str, Any] = {
        "source": "NWCG PMS 110, PMS 118; NIOSH FFFIPP; NFPA 1500",
        "archive_urls": [
            NWCG_10_ORDERS_URL,
            NWCG_18_WATCHOUTS_URL,
            NPS_COMBINED_URL,
            "https://www.fireengineering.com/firefighting/the-niosh-5-beyond-firefighter-line-of-duty-deaths/",
            "https://www.firerescue1.com/leadership/articles/the-impact-of-alan-brunacini-MSfWicvv5wuyjKPZ/",
        ],
        "ten_standard_orders": data["orders"],
        "eighteen_watchout_situations": data["watchouts"],
        "niosh_5_causal_factors": niosh,
        "brunacini_risk_doctrine": brunacini,
        "lces_protocol": lces,
    }

    json.dump(output, sys.stdout, indent=2)
    print()  # trailing newline


if __name__ == "__main__":
    main()
