#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

Writes one monologue to /output/entry.txt. The text is fixed and
deterministic: the same bytes on every run. The speaker is Karghul,
Lord of the Ashen Spire, forty-three years into an empire built on
grain levies and tolls, addressing the hero who climbed his nine
hundred steps. His tiredness lives in the pauses, the trailing
thoughts and the small deflections, never in a plain statement.
"""

import os

MONOLOGUE = (
    "You climbed nine hundred steps for this. Past the gargoyles \u2014 "
    "the ones with chipped noses. I meant to fix those... "
    "forty-three years ago. Sit. No, stand. Heroes always stand. "
    "My knees filed a formal complaint years ago.\n\n"
    "I built this empire on ledgers, boy. Grain levies. Tolls on the "
    "Dunhollow road. Every soul in the valley owes me three copper "
    "and a signature, and not one of them \u2014 not one \u2014 has paid "
    "on time.\n\n"
    "So here is my grand design. My final curse. My... where was I? "
    "Ah. Strike, then. Take the crown.\n\n"
    "It comes with the paperwork."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(MONOLOGUE + "\n")


if __name__ == "__main__":
    main()
