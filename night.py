from journey import get_current_day, get_today_nickname
from config import OWNER_NAME

NIGHT_MESSAGES = [
    f"""
🌙 Good Night, {get_today_nickname()}

Before you close your eyes tonight, I want you to leave every stress of today behind.

You did your best, and that is enough.

May Allah protect you while you sleep, calm your heart, forgive your mistakes, and let you wake up with peace and happiness.

Sleep well, my love. ❤️

With love,
{OWNER_NAME}
""",

    f"""
🌙 Sleep Well, {get_today_nickname()}

The day is over now, and I hope your heart can finally rest.

No matter what happened today, remember that Allah is always near, and tomorrow can still bring something beautiful.

May your dreams be soft, your sleep be peaceful, and your heart feel safe tonight.

Good night, my favorite person. 🤍

With love,
{OWNER_NAME}
""",

    f"""
✨ Good Night, {get_today_nickname()}

One last reminder before you sleep:

You are loved, appreciated, and prayed for.

May Allah remove every worry from your heart, protect you from sadness, and surround your night with mercy.

Rest beautifully, my love. 🌙

With love,
{OWNER_NAME}
"""
]


def get_today_night_message():
    day = get_current_day()
    index = (day - 1) % len(NIGHT_MESSAGES)
    return NIGHT_MESSAGES[index]