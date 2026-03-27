#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "selectolax"]
# ///
"""
Scrape the complete list of 253 patterns from patternlanguage.cc
and output structured JSON to stdout.

Usage:
    uv run playbooks/alexander-pattern-language/scripts/scrape_patterns.py
"""

import json
import re
import sys

import httpx
from selectolax.parser import HTMLParser


def fetch_patterns() -> list[dict]:
    """Fetch and parse all 253 patterns from patternlanguage.cc."""
    url = "https://patternlanguage.cc/"
    resp = httpx.get(url, timeout=30, follow_redirects=True)
    resp.raise_for_status()

    tree = HTMLParser(resp.text)
    patterns = []

    # The site lists patterns as links with pattern numbers and names
    for node in tree.css("a"):
        text = node.text(strip=True)
        if not text:
            continue
        # Pattern entries look like "1. Independent Regions" or similar
        match = re.match(r"^(\d{1,3})\.\s+(.+)$", text)
        if not match:
            match = re.match(r"^(\d{1,3})\s+(.+)$", text)
        if match:
            num = int(match.group(1))
            name = match.group(2).strip()
            if 1 <= num <= 253:
                href = node.attributes.get("href", "")
                patterns.append({
                    "number": num,
                    "name": name,
                    "url": href if href.startswith("http") else f"https://patternlanguage.cc{href}" if href else None,
                })

    # Deduplicate by number, keep first occurrence
    seen = set()
    unique = []
    for p in patterns:
        if p["number"] not in seen:
            seen.add(p["number"])
            unique.append(p)

    unique.sort(key=lambda p: p["number"])
    return unique


# Fallback: canonical list from the book, verified against
# patternlanguage.cc and claytondorge.com/patterns-list
CANONICAL_PATTERNS = [
    (1, "Independent Regions"),
    (2, "The Distribution of Towns"),
    (3, "City Country Fingers"),
    (4, "Agricultural Valleys"),
    (5, "Lace of Country Streets"),
    (6, "Country Towns"),
    (7, "The Countryside"),
    (8, "Mosaic of Subcultures"),
    (9, "Scattered Work"),
    (10, "Magic of the City"),
    (11, "Local Transport Areas"),
    (12, "Community of 7000"),
    (13, "Subculture Boundary"),
    (14, "Identifiable Neighborhood"),
    (15, "Neighborhood Boundary"),
    (16, "Web of Public Transport"),
    (17, "Ring Roads"),
    (18, "Network of Learning"),
    (19, "Web of Shopping"),
    (20, "Mini-Buses"),
    (21, "Four-Story Limit"),
    (22, "Nine Per Cent Parking"),
    (23, "Parallel Roads"),
    (24, "Sacred Sites"),
    (25, "Access to Water"),
    (26, "Life Cycle"),
    (27, "Men and Women"),
    (28, "Eccentric Nucleus"),
    (29, "Density Rings"),
    (30, "Activity Nodes"),
    (31, "Promenade"),
    (32, "Shopping Street"),
    (33, "Night Life"),
    (34, "Interchange"),
    (35, "Household Mix"),
    (36, "Degrees of Publicness"),
    (37, "House Cluster"),
    (38, "Row Houses"),
    (39, "Housing Hill"),
    (40, "Old People Everywhere"),
    (41, "Work Community"),
    (42, "Industrial Ribbon"),
    (43, "University as a Marketplace"),
    (44, "Local Town Hall"),
    (45, "Necklace of Community Projects"),
    (46, "Market of Many Shops"),
    (47, "Health Center"),
    (48, "Housing In Between"),
    (49, "Looped Local Roads"),
    (50, "T Junctions"),
    (51, "Green Streets"),
    (52, "Network of Paths and Cars"),
    (53, "Main Gateways"),
    (54, "Road Crossing"),
    (55, "Raised Walk"),
    (56, "Bike Paths and Racks"),
    (57, "Children in the City"),
    (58, "Carnival"),
    (59, "Quiet Backs"),
    (60, "Accessible Green"),
    (61, "Small Public Squares"),
    (62, "High Places"),
    (63, "Dancing in the Street"),
    (64, "Pools and Streams"),
    (65, "Birth Places"),
    (66, "Holy Ground"),
    (67, "Common Land"),
    (68, "Connected Play"),
    (69, "Public Outdoor Room"),
    (70, "Grave Sites"),
    (71, "Still Water"),
    (72, "Local Sports"),
    (73, "Adventure Playground"),
    (74, "Animals"),
    (75, "The Family"),
    (76, "House for a Small Family"),
    (77, "House for a Couple"),
    (78, "House for One Person"),
    (79, "Your Own Home"),
    (80, "Self-Governing Workshops and Offices"),
    (81, "Small Services Without Red Tape"),
    (82, "Office Connections"),
    (83, "Master and Apprentices"),
    (84, "Teenage Society"),
    (85, "Shopfront Schools"),
    (86, "Children's Home"),
    (87, "Individually Owned Shops"),
    (88, "Street Cafe"),
    (89, "Corner Grocery"),
    (90, "Beer Hall"),
    (91, "Traveler's Inn"),
    (92, "Bus Stop"),
    (93, "Food Stands"),
    (94, "Sleeping in Public"),
    (95, "Building Complex"),
    (96, "Number of Stories"),
    (97, "Shielded Parking"),
    (98, "Circulation Realms"),
    (99, "Main Building"),
    (100, "Pedestrian Street"),
    (101, "Building Thoroughfare"),
    (102, "Family of Entrances"),
    (103, "Small Parking Lots"),
    (104, "Site Repair"),
    (105, "South Facing Outdoors"),
    (106, "Positive Outdoor Space"),
    (107, "Wings of Light"),
    (108, "Connected Buildings"),
    (109, "Long Thin House"),
    (110, "Main Entrance"),
    (111, "Half-Hidden Garden"),
    (112, "Entrance Transition"),
    (113, "Car Connection"),
    (114, "Hierarchy of Open Space"),
    (115, "Courtyards Which Live"),
    (116, "Cascade of Roofs"),
    (117, "Sheltering Roof"),
    (118, "Roof Garden"),
    (119, "Arcades"),
    (120, "Paths and Goals"),
    (121, "Path Shape"),
    (122, "Building Fronts"),
    (123, "Pedestrian Density"),
    (124, "Activity Pockets"),
    (125, "Stair Seats"),
    (126, "Something Roughly in the Middle"),
    (127, "Intimacy Gradient"),
    (128, "Indoor Sunlight"),
    (129, "Common Areas at the Heart"),
    (130, "Entrance Room"),
    (131, "The Flow Through Rooms"),
    (132, "Short Passages"),
    (133, "Staircase as a Stage"),
    (134, "Zen View"),
    (135, "Tapestry of Light and Dark"),
    (136, "Couple's Realm"),
    (137, "Children's Realm"),
    (138, "Sleeping to the East"),
    (139, "Farmhouse Kitchen"),
    (140, "Private Terrace on the Street"),
    (141, "A Room of One's Own"),
    (142, "Sequence of Sitting Spaces"),
    (143, "Bed Cluster"),
    (144, "Bathing Room"),
    (145, "Bulk Storage"),
    (146, "Flexible Office Space"),
    (147, "Communal Eating"),
    (148, "Small Work Groups"),
    (149, "Reception Welcomes You"),
    (150, "A Place to Wait"),
    (151, "Small Meeting Rooms"),
    (152, "Half-Private Office"),
    (153, "Rooms to Rent"),
    (154, "Teenager's Cottage"),
    (155, "Old Age Cottage"),
    (156, "Settled Work"),
    (157, "Home Workshop"),
    (158, "Open Stairs"),
    (159, "Light on Two Sides of Every Room"),
    (160, "Building Edge"),
    (161, "Sunny Place"),
    (162, "North Face"),
    (163, "Outdoor Room"),
    (164, "Street Windows"),
    (165, "Opening to the Street"),
    (166, "Gallery Surround"),
    (167, "Six-Foot Balcony"),
    (168, "Connection to the Earth"),
    (169, "Terraced Slope"),
    (170, "Fruit Trees"),
    (171, "Tree Places"),
    (172, "Garden Growing Wild"),
    (173, "Garden Wall"),
    (174, "Trellised Walk"),
    (175, "Greenhouse"),
    (176, "Garden Seat"),
    (177, "Vegetable Garden"),
    (178, "Compost"),
    (179, "Alcoves"),
    (180, "Window Place"),
    (181, "The Fire"),
    (182, "Eating Atmosphere"),
    (183, "Workspace Enclosure"),
    (184, "Cooking Layout"),
    (185, "Sitting Circle"),
    (186, "Communal Sleeping"),
    (187, "Marriage Bed"),
    (188, "Bed Alcove"),
    (189, "Dressing Rooms"),
    (190, "Ceiling Height Variety"),
    (191, "The Shape of Indoor Space"),
    (192, "Windows Overlooking Life"),
    (193, "Half-Open Wall"),
    (194, "Interior Windows"),
    (195, "Staircase Volume"),
    (196, "Corner Doors"),
    (197, "Thick Walls"),
    (198, "Closets Between Rooms"),
    (199, "Sunny Counter"),
    (200, "Open Shelves"),
    (201, "Waist-High Shelf"),
    (202, "Built-in Seats"),
    (203, "Child Caves"),
    (204, "Secret Place"),
    (205, "Structure Follows Social Spaces"),
    (206, "Efficient Structure"),
    (207, "Good Materials"),
    (208, "Gradual Stiffening"),
    (209, "Roof Layout"),
    (210, "Floor and Ceiling Layout"),
    (211, "Thickening the Outer Walls"),
    (212, "Columns at the Corners"),
    (213, "Final Column Distribution"),
    (214, "Root Foundations"),
    (215, "Ground Floor Slab"),
    (216, "Box Columns"),
    (217, "Perimeter Beams"),
    (218, "Wall Membranes"),
    (219, "Floor-Ceiling Vaults"),
    (220, "Roof Vaults"),
    (221, "Natural Doors and Windows"),
    (222, "Low Sill"),
    (223, "Deep Reveals"),
    (224, "Low Doorway"),
    (225, "Frames as Thickened Edges"),
    (226, "Column Place"),
    (227, "Column Connections"),
    (228, "Stair Vault"),
    (229, "Duct Space"),
    (230, "Radiant Heat"),
    (231, "Dormer Windows"),
    (232, "Roof Caps"),
    (233, "Floor Surface"),
    (234, "Lapped Outside Walls"),
    (235, "Soft Inside Walls"),
    (236, "Windows Which Open Wide"),
    (237, "Solid Doors with Glass"),
    (238, "Filtered Light"),
    (239, "Small Panes"),
    (240, "Half-Inch Trim"),
    (241, "Seat Spots"),
    (242, "Front Door Bench"),
    (243, "Sitting Wall"),
    (244, "Canvas Roofs"),
    (245, "Raised Flowers"),
    (246, "Climbing Plants"),
    (247, "Paving With Cracks Between the Stones"),
    (248, "Soft Tile and Brick"),
    (249, "Ornament"),
    (250, "Warm Colors"),
    (251, "Different Chairs"),
    (252, "Pools of Light"),
    (253, "Things From Your Life"),
]


def main():
    try:
        patterns = fetch_patterns()
        if len(patterns) < 200:
            print(
                f"Warning: only scraped {len(patterns)} patterns, "
                "falling back to canonical list",
                file=sys.stderr,
            )
            patterns = [
                {"number": n, "name": name, "url": None}
                for n, name in CANONICAL_PATTERNS
            ]
    except Exception as e:
        print(f"Scraping failed ({e}), using canonical list", file=sys.stderr)
        patterns = [
            {"number": n, "name": name, "url": None}
            for n, name in CANONICAL_PATTERNS
        ]

    output = {
        "source": "A Pattern Language (Alexander et al., 1977)",
        "archive_url": "https://patternlanguage.cc/",
        "total_patterns": len(patterns),
        "patterns": patterns,
    }
    json.dump(output, sys.stdout, indent=2)
    print(file=sys.stdout)


if __name__ == "__main__":
    main()
