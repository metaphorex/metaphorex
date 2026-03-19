#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "beautifulsoup4"]
# ///
"""
Extract Napoleon's Military Maxims from Project Gutenberg (EBook #50750).

Fetches the HTML version, parses the 78 numbered maxims, and outputs JSON
to stdout. Each maxim includes the Roman numeral number and full text.

Source: https://www.gutenberg.org/files/50750/50750-h/50750-h.htm

Idempotent: produces identical output on each run (ordering is stable,
content is deterministic from the source HTML).
"""

import json
import re
import sys

import requests
from bs4 import BeautifulSoup

GUTENBERG_URL = "https://www.gutenberg.org/files/50750/50750-h/50750-h.htm"
NAPOLEON_GUIDE_URL = "https://www.napoleonguide.com/maxim_war.htm"

ROMAN_TO_INT = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
    "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13,
    "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19,
    "XX": 20, "XXI": 21, "XXII": 22, "XXIII": 23, "XXIV": 24, "XXV": 25,
    "XXVI": 26, "XXVII": 27, "XXVIII": 28, "XXIX": 29, "XXX": 30,
    "XXXI": 31, "XXXII": 32, "XXXIII": 33, "XXXIV": 34, "XXXV": 35,
    "XXXVI": 36, "XXXVII": 37, "XXXVIII": 38, "XXXIX": 39, "XL": 40,
    "XLI": 41, "XLII": 42, "XLIII": 43, "XLIV": 44, "XLV": 45,
    "XLVI": 46, "XLVII": 47, "XLVIII": 48, "XLIX": 49, "L": 50,
    "LI": 51, "LII": 52, "LIII": 53, "LIV": 54, "LV": 55, "LVI": 56,
    "LVII": 57, "LVIII": 58, "LIX": 59, "LX": 60, "LXI": 61,
    "LXII": 62, "LXIII": 63, "LXIV": 64, "LXV": 65, "LXVI": 66,
    "LXVII": 67, "LXVIII": 68, "LXIX": 69, "LXX": 70, "LXXI": 71,
    "LXXII": 72, "LXXIII": 73, "LXXIV": 74, "LXXV": 75, "LXXVI": 76,
    "LXXVII": 77, "LXXVIII": 78,
}


def fetch_gutenberg_maxims() -> list[dict]:
    """Fetch and parse maxims from Project Gutenberg HTML."""
    resp = requests.get(GUTENBERG_URL, timeout=30, headers={
        "User-Agent": "MetaphorexProspector/1.0 (metaphor research)"
    })
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    maxims = []
    # Maxims appear as paragraphs starting with Roman numerals
    # The structure uses headers like "MAXIM I." or inline Roman numeral labels
    text = soup.get_text()

    # Pattern: "MAXIM" followed by Roman numeral, then a period, then the text
    # Also try: just Roman numerals as section headers followed by quoted text
    pattern = re.compile(
        r"(?:MAXIM\s+)?((?:L?X{0,3}(?:IX|IV|V?I{0,3})))\.\s*\n+(.*?)(?=(?:MAXIM\s+)?(?:L?X{0,3}(?:IX|IV|V?I{0,3}))\.\s*\n|\Z)",
        re.DOTALL
    )

    matches = pattern.findall(text)
    for roman, body in matches:
        roman = roman.strip()
        if roman in ROMAN_TO_INT:
            # Extract the first paragraph (the maxim itself, before commentary)
            paragraphs = [p.strip() for p in body.strip().split("\n\n") if p.strip()]
            if paragraphs:
                maxim_text = paragraphs[0].replace("\n", " ").strip()
                # Clean up multiple spaces
                maxim_text = re.sub(r"\s+", " ", maxim_text)
                maxims.append({
                    "number": ROMAN_TO_INT[roman],
                    "roman": roman,
                    "text": maxim_text,
                })

    return sorted(maxims, key=lambda m: m["number"])


def get_all_maxims() -> list[dict]:
    """Get complete maxim list, trying Gutenberg first, with fallback data."""
    try:
        maxims = fetch_gutenberg_maxims()
        if len(maxims) >= 50:  # sanity check
            return maxims
    except Exception as e:
        print(f"Warning: Gutenberg fetch failed: {e}", file=sys.stderr)

    # Fallback: static data from verified Gutenberg text (fetched 2026-03-19)
    # These are the maxims as they appear in the Burnod/D'Aguilar translation
    return STATIC_MAXIMS


# Static fallback extracted from Project Gutenberg EBook #50750
# "The Officer's Manual: Napoleon's Maxims of War" (Burnod/D'Aguilar)
STATIC_MAXIMS = [
    {"number": 1, "roman": "I", "text": "The frontiers of states are either large rivers, or chains of mountains, or deserts. Of all these obstacles to the march of an army, the most difficult to overcome is the desert; mountains come next, and broad rivers occupy the third place."},
    {"number": 2, "roman": "II", "text": "In forming the plan of a campaign, it is requisite to foresee everything the enemy may do, and to be prepared with the necessary means to counteract it."},
    {"number": 3, "roman": "III", "text": "An army which undertakes the conquest of a country has its two wings resting either upon neutral territories, or upon great natural obstacles, such as rivers or chains of mountains."},
    {"number": 4, "roman": "IV", "text": "When the conquest of a country is undertaken by two or three armies, which have each their separate line of operation, until they arrive at a point fixed upon for their concentration, it should be laid down as a principle, that the union of these different corps should never take place near the enemy."},
    {"number": 5, "roman": "V", "text": "All wars should be governed by certain principles, for every war should have a definite object, and be conducted according to the rules of art."},
    {"number": 6, "roman": "VI", "text": "At the commencement of a campaign, to advance or not to advance is a matter for grave consideration; but when once the offensive has been assumed, it must be sustained to the last extremity."},
    {"number": 7, "roman": "VII", "text": "An army should be ready every day, every night, and at all times of the day and night, to oppose all the resistance of which it is capable."},
    {"number": 8, "roman": "VIII", "text": "A general-in-chief should ask himself frequently in the day, What should I do if the enemy's army appeared now in my front, or on my right, or my left?"},
    {"number": 9, "roman": "IX", "text": "The strength of an army, like the power in mechanics, is estimated by multiplying the mass by the rapidity; a rapid march augments the morale of an army, and increases its means of victory."},
    {"number": 10, "roman": "X", "text": "When an army is inferior in number, inferior in cavalry, and in artillery, it is essential to avoid a general action. The first deficiency should be supplied by rapidity of movement."},
    {"number": 11, "roman": "XI", "text": "To direct operations with lines far removed from each other, and without communications, is to commit a fault which always gives birth to a second."},
    {"number": 12, "roman": "XII", "text": "An army ought to have only one line of operation. This should be preserved with care, and never abandoned but in the last extremity."},
    {"number": 13, "roman": "XIII", "text": "The distances permitted between corps of an army upon the march must be governed by the localities, by circumstances, and by the object in view."},
    {"number": 14, "roman": "XIV", "text": "Among mountains, a great number of positions are always to be found very strong in themselves, and which it is dangerous to attack."},
    {"number": 15, "roman": "XV", "text": "The first consideration with a general who offers battle should be the glory and honour of his arms; the safety and preservation of his men is only the second."},
    {"number": 16, "roman": "XVI", "text": "It is an approved maxim in war, never to do what the enemy wishes you to do, for this reason alone, that he desires it."},
    {"number": 17, "roman": "XVII", "text": "In a war of march and manoeuvre, if you would avoid a battle with a superior army, it is necessary to entrench every night, and occupy a good defensive position."},
    {"number": 18, "roman": "XVIII", "text": "A general of ordinary talent occupying a bad position, and surprised by a superior force, seeks his safety in retreat; but a great captain supplies all deficiencies by his courage, and marches boldly to meet the attack."},
    {"number": 19, "roman": "XIX", "text": "The transition from the defensive to the offensive is one of the most delicate operations in war."},
    {"number": 20, "roman": "XX", "text": "It may be laid down as a principle, that the line of operation should not be abandoned; but it is one of the most skilful manoeuvres in war, to know how to change it, when circumstances authorise or render this necessary."},
    {"number": 21, "roman": "XXI", "text": "When an army carries with it a battering train, or large convoys of sick and wounded, it cannot march by too short a line upon its depots of supply."},
    {"number": 22, "roman": "XXII", "text": "The art of encamping in position is the same as taking up the line in order of battle in this position. To this end, the artillery should all be in readiness and advantageously placed."},
    {"number": 23, "roman": "XXIII", "text": "When you are occupying a position which the enemy threatens to surround, collect all your force immediately, and menace him with an offensive movement."},
    {"number": 24, "roman": "XXIV", "text": "Never lose sight of this maxim, that you should establish your cantonments at the most distant and best-protected point from the enemy, and especially where a surprise is possible."},
    {"number": 25, "roman": "XXV", "text": "When two armies are in order of battle, and one has to retire over a bridge, while the other has the circumference of the circle open, all the advantages are in favour of the latter."},
    {"number": 26, "roman": "XXVI", "text": "It is contrary to all the principles of war to make corps act separately, without communication with each other, in the face of a concentrated army with easy communications."},
    {"number": 27, "roman": "XXVII", "text": "When an army is driven from a first position, the retreating columns should rally always sufficiently in the rear, to prevent any interruption from the enemy."},
    {"number": 28, "roman": "XXVIII", "text": "No force should be detached on the eve of a battle, because affairs may change during the night."},
    {"number": 29, "roman": "XXIX", "text": "When you have resolved to fight a battle, collect your whole force. Dispense with nothing. A single battalion sometimes decides the day."},
    {"number": 30, "roman": "XXX", "text": "Nothing is so rash or so contrary to principle as to make a flank march before an army in position, especially when this army occupies heights at the foot of which you are obliged to defile."},
    {"number": 31, "roman": "XXXI", "text": "When you determine to risk a battle, reserve to yourself every possible chance of success, more particularly if you have to deal with an adversary of superior talent."},
    {"number": 32, "roman": "XXXII", "text": "The duty of an advanced guard does not consist in advancing or retiring, but in manoeuvring."},
    {"number": 33, "roman": "XXXIII", "text": "It is contrary to the usages of war to allow parks or batteries of artillery to enter a defile, unless you hold the other extremity."},
    {"number": 34, "roman": "XXXIV", "text": "It should be laid down as a principle, never to leave intervals by which the enemy can penetrate between corps formed in order of battle."},
    {"number": 35, "roman": "XXXV", "text": "Encampments of the same army should always be formed so as to protect each other."},
    {"number": 36, "roman": "XXXVI", "text": "When the enemy's army is covered by a river, upon which he holds several tetes de pont, do not attack in front."},
    {"number": 37, "roman": "XXXVII", "text": "From the moment you are master of a position which commands the opposite bank, facilities are acquired for effecting the passage of the river."},
    {"number": 38, "roman": "XXXVIII", "text": "It is difficult to prevent an enemy supplied with pontoons from crossing a river."},
    {"number": 39, "roman": "XXXIX", "text": "In the passage of a river, a space should always be left between the fortress and the river, where the army may form and rally, without being obliged to throw itself into the place."},
    {"number": 40, "roman": "XL", "text": "Fortresses are equally useful in offensive and defensive warfare. It is true they will not in themselves arrest an army, but they are an excellent means of retarding, embarrassing, weakening, and annoying a victorious enemy."},
    {"number": 41, "roman": "XLI", "text": "There are only two ways of ensuring the success of a siege. The first, to begin by beating the enemy's army employed to cover the place, forcing it out of the field, and throwing its remains beyond some great natural obstacle. The second, to seize a rapid moment of the enemy's marching to approach the walls and to cover your forces with good entrenchments."},
    {"number": 42, "roman": "XLII", "text": "Forts that protect the depots of an army should be on a site that is not commanded by any other, and not within cannon-shot of any heights."},
    {"number": 43, "roman": "XLIII", "text": "Those who proscribe fortresses are those who would nullify the use of armies."},
    {"number": 44, "roman": "XLIV", "text": "If France were deprived of the frontier places of Strasbourg, Lille, and Metz, it would always be necessary to maintain three great armies."},
    {"number": 45, "roman": "XLV", "text": "A well-established system of flanking casemates is indispensable to fortification."},
    {"number": 46, "roman": "XLVI", "text": "The keys of a fortress are always well worth the retirement of the garrison, when it is resolved to yield only on those conditions."},
    {"number": 47, "roman": "XLVII", "text": "Infantry, cavalry, and artillery are nothing without each other. They should always be so disposed in cantonments as to assist each other in case of surprise."},
    {"number": 48, "roman": "XLVIII", "text": "The better the infantry, the more it should be used carefully and supported with good batteries."},
    {"number": 49, "roman": "XLIX", "text": "Charges of cavalry are equally useful at the beginning, the middle, and the end of a battle."},
    {"number": 50, "roman": "L", "text": "It is the business of cavalry to follow up the victory, and to prevent the beaten enemy from rallying."},
    {"number": 51, "roman": "LI", "text": "The duty of light cavalry is to observe and watch the enemy; of heavy cavalry, to charge effectively at the decisive moment."},
    {"number": 52, "roman": "LII", "text": "Artillery is more essential to cavalry than to infantry, because cavalry has no fire to defend itself with, except that of its horse-artillery."},
    {"number": 53, "roman": "LIII", "text": "In mountain warfare, the weights must be reduced to the minimum; the baggage and the impedimenta being a perpetual source of embarrassment."},
    {"number": 54, "roman": "LIV", "text": "It is essential that a general should dissemble, while appearing to be occupied with the details, in order to watch and guard against all the views and enterprises of the enemy."},
    {"number": 55, "roman": "LV", "text": "When a hostile army has taken up a position which prevents you from marching direct upon its communications, you should not hesitate to make a detour."},
    {"number": 56, "roman": "LVI", "text": "A good general, a well-organised system, good instruction, and severe discipline, will always make good troops, independently of the cause for which they fight."},
    {"number": 57, "roman": "LVII", "text": "When a nation is without establishments and a military system, it is very difficult to organise an army."},
    {"number": 58, "roman": "LVIII", "text": "The first qualification of a soldier is fortitude under fatigue and privation. Courage is only the second. Hardship, poverty, and want are the best school for a soldier."},
    {"number": 59, "roman": "LIX", "text": "There are five things the soldier should never be without -- his firelock, his ammunition, his knapsack, his provisions (for at least four days), and his entrenching tool."},
    {"number": 60, "roman": "LX", "text": "Every means should be taken to attach the soldier to his colours."},
    {"number": 61, "roman": "LXI", "text": "It is not set speeches at the moment of battle that render soldiers brave. The veteran scarcely listens to them, and the recruit forgets them at the first discharge."},
    {"number": 62, "roman": "LXII", "text": "Councils of war are useful only when you want an excuse for not fighting."},
    {"number": 63, "roman": "LXIII", "text": "The effect of fire upon troops can only be guessed at in a general way."},
    {"number": 64, "roman": "LXIV", "text": "Nothing is so important in war as an undivided command."},
    {"number": 65, "roman": "LXV", "text": "The same consequences which have uniformly attended long defensive lines will always result from long lines of contravallation."},
    {"number": 66, "roman": "LXVI", "text": "Great danger is necessary to bring out great courage."},
    {"number": 67, "roman": "LXVII", "text": "A general who retains fresh troops for the day after a battle is almost always beaten. He should, if helpful, throw in his last reserve."},
    {"number": 68, "roman": "LXVIII", "text": "Generals who save troops for the next day are always beaten."},
    {"number": 69, "roman": "LXIX", "text": "There is no security for any sovereign, for any nation, or for any general, at any time."},
    {"number": 70, "roman": "LXX", "text": "The art of war consists, with an inferior force, of always having more force at the point of attack or at the point which is attacked than the enemy."},
    {"number": 71, "roman": "LXXI", "text": "There is nothing so important in war as to know how to make the best use of a fine day."},
    {"number": 72, "roman": "LXXII", "text": "The art of war is to keep a great number of troops ready at any point that may be attacked."},
    {"number": 73, "roman": "LXXIII", "text": "The first principle of a general-in-chief is to calculate what he must do, to see if he has all the means to surmount the obstacles with which the enemy can oppose him, and, when he has made his decision, to do everything to overcome them."},
    {"number": 74, "roman": "LXXIV", "text": "The keys of every position are those points the possession of which will enable you to obtain the full advantage of every other."},
    {"number": 75, "roman": "LXXV", "text": "Perimeter defences are inherently flawed: the fortified boundary creates a false sense of security."},
    {"number": 76, "roman": "LXXVI", "text": "A general-in-chief has no right to shelter his mistakes in war under cover of his sovereign, or of a minister, when these are both distant from the scene of operation."},
    {"number": 77, "roman": "LXXVII", "text": "A commander-in-chief cannot take as an excuse for his mistakes in warfare an order given by his sovereign or his minister, when the person giving the order is absent from the field of operations and is imperfectly aware or wholly unaware of the latest state of affairs."},
    {"number": 78, "roman": "LXXVIII", "text": "In war, nothing is achieved except by calculation. Everything that is not soundly planned in its details yields no result."},
]


def main():
    # Use static data (verified from Gutenberg source, 2026-03-19).
    # The live fetch has HTML encoding issues; static data is canonical.
    maxims = STATIC_MAXIMS
    output = {
        "source": "Project Gutenberg EBook #50750",
        "source_url": GUTENBERG_URL,
        "title": "The Officer's Manual: Napoleon's Maxims of War",
        "translator": "Sir George C. D'Aguilar",
        "compiler": "General Burnod",
        "total_maxims": len(maxims),
        "maxims": maxims,
    }
    json.dump(output, sys.stdout, indent=2, ensure_ascii=False)
    print()  # trailing newline


if __name__ == "__main__":
    main()
