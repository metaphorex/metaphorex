#!/usr/bin/env python3
"""
Scrape the Osaka University Conceptual Metaphor Home Page directory index
to extract all metaphor file names as structured candidates.

Archive URL: http://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/metaphors/index.html

This script parses the HTML directory listing to produce a JSON array of
candidate entries. Each entry includes the metaphor name (derived from the
filename), a slug, and source/target frame stubs.

Usage:
    python scrape_osaka_archive.py > osaka_candidates.json

The script fetches the directory listing over HTTP. If the archive is
unreachable, it falls back to a cached copy of the file listing embedded
in the script (captured 2026-03-11).
"""

import json
import re
import sys
import urllib.request
import urllib.error
from html.parser import HTMLParser

ARCHIVE_INDEX_URL = (
    "http://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/metaphors/index.html"
)

# Cached file listing from the Osaka archive, captured 2026-03-11.
# Used as fallback if the live archive is unreachable.
CACHED_FILES = [
    "A_Force_Is_A_Moving_Object.html",
    "A_Problem_Is_A_Body_Of_Water.html",
    "A_Problem_Is_A_Locked_Container_For_Its_Solution.html",
    "A_Problem_Is_A_Region_In_A_Landscape.html",
    "A_Schedule_Is_A_Moving_Object.html",
    "Abilities_Are_Entities_Inside_A_Person.html",
    "Acting_Compulsively_Is_Ingesting_A_Substance_Compulsively.html",
    "Acting_On_Is_Transferring_An_Object.html",
    "Action_Is_Control_Over_Possessions.html",
    "Action_Is_Motion.html",
    "Action_Is_Self-propelled_Motion.html",
    "Active_Is_Alive.html",
    "Affection_Is_Warmth.html",
    "Anger_Is_Heat.html",
    "Aspects_Of_The_Self_Are_Distinct_Individuals.html",
    "Attributes_Are_Entities.html",
    "Beliefs_Are_Beings_With_A_Life_Cycle.html",
    "Beliefs_Are_Fashions.html",
    "Beliefs_Are_Guides.html",
    "Beliefs_Are_Locations.html",
    "Beliefs_Are_Love_Objects.html",
    "Beliefs_Are_Possessions.html",
    "Causal_Precedence_Is_Temporal_Precedence.html",
    "Causation_Is_Commercial_Transaction.html",
    "Causation_Is_Control_Over_An_Entity_Relative_To_A_Location.html",
    "Causation_Is_Control_Over_An_Object_Relative_To_A_Possessor.html",
    "Causation_Is_Control_Over_Relative_Location.html",
    "Causes_And_Effects_Are_Linked_Objects.html",
    "Change_Is_Motion.html",
    "Change_Is_Motion_(location).html",
    "Change_Is_Replacement.html",
    "Change_Of_State_Is_Change_Of_Direction.html",
    "Coherent_Is_Aligned.html",
    "Coherent_Is_Whole.html",
    "Communication_Is_Linguistic_Communication.html",
    "Comparing_And_Seeking_Is_Shopping.html",
    "Comparison_Of_Properties_Is_Comparison_Of_Physical_Properties.html",
    "Comparison_Of_Properties_Is_Comparison_Of_Possessions_(non-evaluative).html",
    "Competition_Is_1_On_1_Physical_Aggression.html",
    "Competition_Is_A_Race.html",
    "Competition_Is_Competition_For_Desired_Objects.html",
    "Competition_Is_War.html",
    "Complience_Is_Adherence.html",
    "Complience_Is_Following.html",
    "Complience_Is_Tightness.html",
    "Conceit_Is_Inflation.html",
    "Conducting_Research_Is_Solving_A_Puzzle.html",
    "Control_Is_Up.html",
    "Creating_Is_Birthing.html",
    "Creating_Is_Giving_An_Object.html",
    "Creating_Is_Making.html",
    "Creating_Is_Making_Visible.html",
    "Creating_Is_Moving_To_A_Location_(here).html",
    "Creation_Is_Cultivation.html",
    "Dangerous_Beliefs_Are_Contagious_Diseases.html",
    "Darkness_Is_A_Cover.html",
    "Darkness_Is_A_Solid.html",
    "Desire_Is_Hunger.html",
    "Desires_Are_Forces_Between_The_Desired_And_The_Desirer.html",
    "Difficult_Subjects_Are_Adversaries.html",
    "Difficulties_Are_Containers.html",
    "Difficulty_Is_Difficulty_Is_Moving.html",
    "Disgust_Is_Nausea.html",
    "Disparity_Is_Change.html",
    "Effect_On_Emotional_Self_Is_Contact_With_Physical_Self.html",
    "Effects_Of_Humor_Are_Injuries.html",
    "Emotion_Is_Motion.html",
    "Emotional_Intimacy_Is_Physical_Closeness.html",
    "Emotional_Self_Is_A_Brittle_Object.html",
    "Emotional_Stability_Is_Balance.html",
    "Emotional_Stability_Is_Contact_With_The_Ground.html",
    "Emotional_Stability_Is_Maintaining_Position.html",
    "Emotions_Are_Entities_Within_A_Person.html",
    "Emotions_Are_Forces.html",
    "Emotions_Are_Locations.html",
    "Euphoric_States_Are_Up.html",
    "Event_Structure_(location_Case).html",
    "Event_Structure_(object_Case).html",
    "Existence_Is_A_Location_(here).html",
    "Existence_Is_An_Object.html",
    "Existence_Is_Having_A_Form.html",
    "Existence_Is_Life.html",
    "Existence_Is_Visibility.html",
    "External_Appearance_Is_A_Cover.html",
    "External_Conditions_Are_Climate.html",
    "External_Events_Affecting_Progress_Are_Forces_Affecting.html",
    "Facts_Are_Points_(set_Up_In_Spatial_Configuration).html",
    "Fear_Is_Cold.html",
    "Force_Is_A_Substance_Contained_In_Affecting_Causes.html",
    "Force_Is_A_Substance_Directed_At_An_Affected_Party.html",
    "Form_Is_Motion.html",
    "Gaining_Physical_Intimacy_(against_Resistance)_Is_A_Competition.html",
    "Getting_Is_Eating.html",
    "Harm_Is_Being_In_A_Harmful_Location.html",
    "Harm_Is_Causing_Functional_Objects_To_Be_Nonfunctional.html",
    "Harm_Is_Having_A_Harmful_Possession.html",
    "Harm_Is_Lacking_A_Needed_Possession.html",
    "Harm_Is_Physical_Injury.html",
    "Harm_Is_Preventing_Forward_Motion_Toward_A_Goal.html",
    "Harming_Is_Lowering.html",
    "Hope_Is_A_Benefical_Possession.html",
    "Hope_Is_A_Child.html",
    "Hope_Is_Light.html",
    "Ideas_Are_Children_(w.r.t_Development).html",
    "Ideas_Are_Fashions.html",
    "Ideas_Are_Food.html",
    "Ideas_Are_Light_Sources.html",
    "Ideas_Are_Locations.html",
    "Ideas_Are_Objects.html",
    "Ideas_Are_Perceptions.html",
    "Ideas_Are_Resources.html",
    "Ideas_Are_Writing.html",
    "Intelligence_Is_A_Light_Source.html",
    "Intense_Emotions_Are_Heat.html",
    "Interaction_Between_Progress_And_External_Events_Affecting.html",
    "Interpersonal_Harmony_Is_Musical_Harmony.html",
    "Intoxication_Is_Becoming_Electrified.html",
    "Intoxication_Is_Getting_A_Burden.html",
    "Intoxication_Is_Getting_Destroyed.html",
    "Investments_Are_Containers_For_Money.html",
    "Knowledge_Of_Past_Events_Is_An_External_Event_Exerting_Force_On.html",
    "Laughter_Is_A_Substance.html",
    "Light_Is_A_Fluid.html",
    "Light_Is_A_Line.html",
    "Linear_Scales_Are_Paths.html",
    "Logic_Is_Gravity.html",
    "Logical_Relations_Are_Causal_Relations.html",
    "Longterm_Purposeful_Activity_Is_A_Journey.html",
    "Longterm_Purposeful_Change_Is_A_Journey.html",
    "Love_Is_A_Journey.html",
    "Love_Is_A_Unity_(of_Two_Complementary_Parts).html",
    "Love_Is_Madness.html",
    "Love_Is_Magic.html",
    "Loved_One_Is_A_Possession.html",
    "Lust_Is_Heat.html",
    "Lustful_Person_Is_An_Activated_Machine.html",
    "Lustful_Person_Is_An_Animal.html",
    "Machines_Are_People.html",
    "Means_Of_Change_Is_Path_Over_Which_Motion_Occurs.html",
    "Mental_Accounting.html",
    "Mind,_Or_Mental_Self_Is_A_Brittle_Object.html",
    "Money_Is_A_Liquid.html",
    "Moral_Accounting.html",
    "Morality_Is_Cleanliness.html",
    "Morality_Is_Purity.html",
    "Morality_Is_Straightness.html",
    "Necessary_Prerequisite_For_Change_Is_Source_Of_Moving_Entity.html",
    "Obligations_Are_Containers.html",
    "Obligations_Are_Forces.html",
    "Obligations_Are_Possessions.html",
    "Opportunities_Are_Objects.html",
    "Opportunities_Are_Open_Paths.html",
    "People_Are_Batteries.html",
    "People_Are_Machines.html",
    "People_Are_Plants.html",
    "Perception_Is_Reception.html",
    "Perception_Is_Shape_Recognition.html",
    "Personality_Is_Material.html",
    "Possessing_Is_Holding.html",
    "Problem_Is_A_Constructed_Object.html",
    "Problem_Is_A_Tangle.html",
    "Problem_Is_A_Target.html",
    "Properties_Are_Contents.html",
    "Properties_Are_Physical_Properties.html",
    "Properties_Are_Possessions.html",
    "Psychological_Forces_Are_Physical_Forces.html",
    "Rational_Is_Up.html",
    "Receiving_Serious_Thought_Is_Being_On_The_Mind.html",
    "Relationship_Is_Kinship.html",
    "Responsibilities_Are_Possessions.html",
    "Seeing_Is_Touching,_Eyes_Are_Limbs.html",
    "Self-initiated_Change_Of_State_Is_Self-propelled_Motion.html",
    "Sexuality_Is_An_Offensive_Weapon.html",
    "Shapes_Are_Containers.html",
    "Social_Accounting.html",
    "Society_Is_A_Body.html",
    "States_Are_Locations.html",
    "States_Are_Shapes.html",
    "Strong_Emotion_Is_Blinding.html",
    "Strong_Emotions_Are_Madness.html",
    "Subjects_Are_Areas.html",
    "The_Body_Is_A_Container_For_The_Self.html",
    "The_Conduit_Metaphor.html",
    "The_Event_Structure_Metaphorical_System.html",
    "The_Mind_Is_A_Body.html",
    "The_Mind_Is_A_Machine.html",
    "The_Progress_Of_External_Events_Is_Forward_Motion.html",
    "The_Visual_Field_Is_A_Bounded_Region.html",
    "The_Visual_Field_Is_A_Container.html",
    "Theoretical_Debate_Is_Competition.html",
    "Theories_Are_Beings_With_Life_Cycles.html",
    "Theories_Are_Cloth.html",
    "Theories_Are_Constructed_Objects.html",
    "Theories_Are_Covers_For_The_Facts.html",
    "Theories_Are_People_(w.r.t._Family_Tree_Structure).html",
    "Theories_Are_People_(w.r.t._Opinions).html",
    "Time_Is_A_Changer.html",
    "Time_Is_A_Container_(bounded).html",
    "Time_Is_A_Landscape_We_Move_Through.html",
    "Time_Is_A_Pursuer.html",
    "Time_Is_A_Resource.html",
    "Time_Is_Money.html",
    "Time_Is_Something_Moving_Toward_You.html",
    "Treating_Illness_Is_Fighting_A_War.html",
    "Well-being_Is_Wealth.html",
    "Words_Are_Weapons.html",
]


class DirectoryIndexParser(HTMLParser):
    """Parse an Apache/Nginx-style directory listing for .html links."""

    def __init__(self):
        super().__init__()
        self.files = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href" and value.endswith(".html"):
                    # Skip parent directory links
                    if (
                        value not in (".", "..", "../", "index.html")
                        and not value.startswith("../")
                        and not value.startswith("/")
                    ):
                        self.files.append(value)


def filename_to_name(filename: str) -> str:
    """Convert an Osaka archive filename to a canonical metaphor name.

    Example: 'Anger_Is_Heat.html' -> 'ANGER IS HEAT'
    """
    name = filename.replace(".html", "")
    # Handle parenthetical qualifiers
    name = re.sub(r"_?\(([^)]+)\)", r" (\1)", name)
    name = name.replace("_", " ")
    # Clean up multiple spaces
    name = re.sub(r"\s+", " ", name).strip()
    return name.upper()


def filename_to_slug(filename: str) -> str:
    """Convert an Osaka archive filename to a URL-friendly slug.

    Example: 'Anger_Is_Heat.html' -> 'anger-is-heat'
    """
    name = filename.replace(".html", "")
    # Remove parenthetical qualifiers for the slug
    name = re.sub(r"_?\([^)]+\)", "", name)
    # Remove trailing dots or underscores
    name = name.rstrip("._")
    slug = name.lower().replace("_", "-").replace(",", "")
    # Clean up multiple hyphens
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


def parse_source_target(name: str):
    """Extract source and target frame stubs from a metaphor name.

    Most entries follow the pattern 'TARGET IS/ARE SOURCE'.
    Returns (source_frame_stub, target_frame_stub).
    """
    # Try splitting on ' IS ' or ' ARE '
    for splitter in [" IS ", " ARE "]:
        if splitter in name:
            parts = name.split(splitter, 1)
            target_stub = parts[0].strip()
            source_stub = parts[1].strip()
            return source_stub.lower(), target_stub.lower()
    # Fallback for 'THE X' style entries
    return name.lower(), name.lower()


def fetch_file_list() -> list[str]:
    """Fetch the directory listing from the Osaka archive.

    Falls back to cached list if the archive is unreachable.
    """
    try:
        req = urllib.request.Request(
            ARCHIVE_INDEX_URL,
            headers={"User-Agent": "metaphorex-prospector/1.0"},
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")
        parser = DirectoryIndexParser()
        parser.feed(html)
        if parser.files:
            print(f"Fetched {len(parser.files)} files from live archive", file=sys.stderr)
            return parser.files
    except (urllib.error.URLError, OSError, TimeoutError) as e:
        print(f"Archive unreachable ({e}), using cached listing", file=sys.stderr)

    print(f"Using cached listing ({len(CACHED_FILES)} files)", file=sys.stderr)
    return CACHED_FILES


def main():
    files = fetch_file_list()

    candidates = []
    seen_slugs = set()

    for filename in sorted(files):
        slug = filename_to_slug(filename)

        # Deduplicate (some files differ only by trailing dots)
        if slug in seen_slugs:
            continue
        seen_slugs.add(slug)

        name = filename_to_name(filename)
        source_stub, target_stub = parse_source_target(name)

        archive_url = (
            "http://www.lang.osaka-u.ac.jp/~sugimoto/MasterMetaphorList/metaphors/"
            + filename
        )

        candidates.append({
            "filename": filename,
            "slug": slug,
            "name": name,
            "source_stub": source_stub,
            "target_stub": target_stub,
            "archive_url": archive_url,
        })

    json.dump(candidates, sys.stdout, indent=2)
    print(file=sys.stdout)  # trailing newline
    print(f"Total: {len(candidates)} unique candidates", file=sys.stderr)


if __name__ == "__main__":
    main()
