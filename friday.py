from datetime import datetime

from config import OWNER_NAME, TIMEZONE


def is_friday():
    """
    Returns True if today is Friday.
    """
    return datetime.now(TIMEZONE).weekday() == 4


def get_kahf_reminder():
    return f"""
🕌 Jumu'ah Mubarak! 🤍

Today is Friday, the best day of the week.

Don't forget to read Surah Al-Kahf today. May Allah place light between this Friday and the next.

Take a few moments to increase your salawat upon our beloved Prophet Muhammad ﷺ and make sincere du'a.

May Allah accept your worship, forgive your sins, and fill your heart with peace.

With love,
{OWNER_NAME}
"""


def get_jumuah_reminder():
    return f"""
🤲 Jumu'ah Mubarak ❤️

As you prepare for Jumu'ah prayer today, I pray Allah accepts all your du'as, grants you endless barakah, and keeps you under His protection.

May your heart always remain attached to Him, and may every Friday bring you closer to Jannah.

Ameen.

With love,
{OWNER_NAME}
"""