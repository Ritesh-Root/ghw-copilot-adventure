"""Story data for the Hacktoberfest Forest adventure.

The game engine in adventure.py knows nothing about the story beyond this
scene structure.
"""

SCENES = {
    "start": {
        "text": (
            "You are a lost hiker in a forest during Hacktoberfest week. "
            "Your phone is dead, and the trail has vanished."
        ),
        "choices": {
            "1": ("Follow a compass needle toward a rushing stream.", "stream"),
            "2": ("Look for a light near an old ranger cabin.", "cabin"),
            "3": ("Investigate a patch of suspiciously orange mushrooms.", "mushrooms"),
        },
    },
    "stream": {
        "text": "The stream splits around a fallen tree. A shaky bridge spans one branch.",
        "choices": {
            "1": ("Cross the shaky bridge.", "bridge"),
            "2": ("Follow a trail of glowing fireflies.", "fireflies"),
        },
    },
    "cabin": {
        "text": "The cabin is empty, but a hand-cranked radio sits on a desk beside a dark tunnel.",
        "choices": {
            "1": ("Try the radio.", "radio"),
            "2": ("Crawl into the tunnel.", "tunnel"),
        },
    },
    "mushrooms": {
        "text": "The mushrooms form an arrow, pointing deeper into the forest.",
        "choices": {
            "1": ("Eat one for courage.", "funny_mushrooms"),
            "2": ("Leave them alone and follow the arrow.", "ravine"),
        },
    },
    "bridge": {
        "text": "The bridge creaks over a deep ravine. Halfway across, you spot a sturdy rope.",
        "choices": {
            "1": ("Keep walking carefully.", "good_exit"),
            "2": ("Use the rope to climb down.", "ravine"),
        },
    },
    "fireflies": {
        "text": "The fireflies gather into a glowing arrow, then dart toward a clearing.",
        "choices": {
            "1": ("Trust the fireflies.", "good_exit"),
            "2": ("Ignore them and take a shortcut downhill.", "ravine"),
        },
    },
    "radio": {
        "text": "The radio crackles: 'Hiker, if you can hear us, identify yourself!'",
        "choices": {
            "1": ("Call for the forest rangers.", "good_exit"),
            "2": ("Answer with your best impression of a bear.", "bear"),
        },
    },
    "tunnel": {
        "text": "The tunnel opens into a tiny room with a map and a sign: 'Definitely the exit.'",
        "choices": {
            "1": ("Follow the map.", "good_exit"),
            "2": ("Decide the sign is suspicious and return outside.", "start"),
        },
    },
    "ravine": {
        "text": "At the ravine, a mossy ledge leads down while a vine-covered ladder leads up.",
        "choices": {
            "1": ("Climb the ladder.", "good_exit"),
            "2": ("Slide down the mossy ledge.", "bad_exit"),
        },
    },
    "bear": {
        "text": "A real bear answers your radio impression from behind a tree.",
        "choices": {
            "1": ("Bow politely and dance the Hacktoberfest chicken dance.", "funny_bear"),
            "2": ("Run without looking back.", "bad_exit"),
        },
    },
    "good_exit": {
        "text": (
            "You emerge at the trailhead just as the rangers arrive with hot cocoa. "
            "You are safe—and ready for Hacktoberfest!"
        ),
        "choices": {},
        "ending": "good",
    },
    "bad_exit": {
        "text": (
            "The ledge gives way. You land in a pile of leaves, but your backpack "
            "is stuck in a tree. The rangers find you eventually."
        ),
        "choices": {},
        "ending": "bad",
    },
    "funny_mushrooms": {
        "text": (
            "The mushroom tastes like pumpkin spice. You confidently march in circles "
            "until a park sign introduces you to the same tree for the fourth time."
        ),
        "choices": {},
        "ending": "funny",
    },
    "funny_bear": {
        "text": (
            "The bear joins your dance, then escorts you to the trailhead. "
            "Your new dance partner becomes the week's most popular Hacktoberfest pull request."
        ),
        "choices": {},
        "ending": "funny",
    },
}
