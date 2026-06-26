from journey import get_current_day, get_today_nickname
from config import OWNER_NAME

MORNING_MESSAGES = [
    f"""
🌅 Good Morning, {get_today_nickname()}

A beautiful new day has begun, and before you get busy with everything around you, I just wanted to remind you that you are deeply loved and always in my prayers.

May Allah fill your heart with peace, brighten your smile, protect you from every difficulty, and make today better than yesterday.

Never forget that someone is always thinking about you and wishing you nothing but happiness.

Have a beautiful day, my love. ❤️

With love,
{OWNER_NAME}
""",

    f"""
🌸 Good Morning, {get_today_nickname()}

Alhamdulillah for another precious morning.

I pray Allah opens doors of happiness for you today, grants you success in everything you do, and keeps your beautiful smile shining.

Take care of yourself, eat well, drink enough water, and do not let anything steal your peace.

I am always wishing you the very best.

With love,
{OWNER_NAME}
""",

    f"""
☀️ Good Morning, {get_today_nickname()}

Every sunrise reminds me that Allah mercy is endless and every new day is another blessing.

I hope today brings you comfort, joy, laughter, and countless little moments that make you smile.

No matter where we are, know that you are always close in my heart.

May Allah protect you throughout today and always.

With love,
{OWNER_NAME}
"""
]


def get_today_morning_message():
    day = get_current_day()
    index = (day - 1) % len(MORNING_MESSAGES)
    return MORNING_MESSAGES[index]