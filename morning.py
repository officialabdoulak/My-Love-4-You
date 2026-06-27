from journey import get_current_day, get_today_nickname
from config import OWNER_NAME


MORNING_MESSAGES = [
    f"""
🌅 Good Morning, {get_today_nickname()}

A beautiful new day has started, and I just want you to begin it with peace in your heart.

May Allah protect you, guide your steps, open doors of ease for you, and keep your smile safe today.

Remember that you are loved, valued, and always in my duas.

With love,
{OWNER_NAME}
""",

    f"""
🌸 Good Morning, {get_today_nickname()}

Alhamdulillah for another precious morning.

I pray today brings you happiness, soft moments, good news, and the kind of peace your heart truly deserves.

Take care of yourself today. Eat well, smile often, and do not let anything steal your peace.

With love,
{OWNER_NAME}
""",

    f"""
☀️ Good Morning, {get_today_nickname()}

Before the world gets busy, I want you to remember how special you are to me.

May Allah bless your day, remove every worry from your heart, and replace it with comfort, confidence, and joy.

Go gently today, my love.

With love,
{OWNER_NAME}
""",

    f"""
🤍 Good Morning, {get_today_nickname()}

I hope your heart feels light today.

May Allah make your path easy, protect you from harm, and surround you with people and moments that bring you happiness.

You deserve a peaceful day and a beautiful smile.

With love,
{OWNER_NAME}
""",

    f"""
🌹 Good Morning, {get_today_nickname()}

Another morning, another reason to thank Allah.

I pray your day is filled with barakah, calm thoughts, kind words, and reasons to smile.

No matter how the day goes, remember that someone is quietly praying for you.

With love,
{OWNER_NAME}
""",

    f"""
🌤️ Good Morning, {get_today_nickname()}

May today be gentle with you.

May Allah give you strength where you feel weak, patience where things feel heavy, and happiness in places you did not expect.

You are deeply appreciated, more than words can explain.

With love,
{OWNER_NAME}
""",

    f"""
💛 Good Morning, {get_today_nickname()}

I hope this message finds you smiling.

May Allah bless your morning, protect your heart, and make everything you touch today filled with ease and goodness.

Please take care of yourself for me.

With love,
{OWNER_NAME}
""",

    f"""
🌷 Good Morning, {get_today_nickname()}

A new day means a fresh chance to breathe, grow, and trust Allah again.

May your heart stay soft, your mind stay calm, and your smile stay bright today.

You are always close to my thoughts.

With love,
{OWNER_NAME}
""",

    f"""
✨ Good Morning, {get_today_nickname()}

I pray today gives you more peace than stress, more smiles than worries, and more blessings than you expected.

You have such a beautiful heart, and I hope life treats it gently today.

With love,
{OWNER_NAME}
""",

    f"""
🌻 Good Morning, {get_today_nickname()}

May Allah fill your morning with light and your day with ease.

Whatever you are hoping for, I pray it comes to you in the best way and at the best time.

Keep smiling, my love.

With love,
{OWNER_NAME}
""",

    f"""
☕ Good Morning, {get_today_nickname()}

I hope today starts softly for you.

May Allah protect you from sadness, bless your efforts, and give you calmness in every situation you face.

You are loved more than you know.

With love,
{OWNER_NAME}
""",

    f"""
🕊️ Good Morning, {get_today_nickname()}

May your heart wake up with peace and your soul feel safe today.

I pray Allah gives you beautiful reasons to smile and keeps every difficulty far from you.

Have a calm and blessed day.

With love,
{OWNER_NAME}
""",

    f"""
🌼 Good Morning, {get_today_nickname()}

Today, I just want you to remember one thing.

You matter. Your happiness matters. Your peace matters.

May Allah protect all three for you today and always.

With love,
{OWNER_NAME}
""",

    f"""
🌅 Good Morning, {get_today_nickname()}

Day by day, I keep praying that Allah writes ease, happiness, and protection for you.

May today be one of those days that feels light, blessed, and full of quiet joy.

Start your day with a smile, my love.

With love,
{OWNER_NAME}
"""
]


def get_today_morning_message():
    day = get_current_day()
    index = (day - 1) % len(MORNING_MESSAGES)
    return MORNING_MESSAGES[index]