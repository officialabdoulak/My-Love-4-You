from journey import get_current_day, get_today_nickname
from config import OWNER_NAME


LOVE_LETTERS = [
    f"""
💌 Our Journey

Day 1 ❤️

My dear {get_today_nickname()},

Today is the beginning of this little journey, and I want you to know that every word here is written with care.

You are special to me in a way I do not take for granted. I pray Allah protects your heart, keeps your smile safe, and fills your life with peace.

May this journey remind you every day that you are loved, valued, respected, and always remembered in my duas.

With love,
{OWNER_NAME}
""",

    f"""
💌 Our Journey

Day 2 ❤️

My beautiful {get_today_nickname()},

Some people enter life quietly but become a source of peace. You are one of those people to me.

I admire your heart, your patience, and the way you keep going even when life is not easy.

May Allah bless your days, protect your dreams, and keep you close to everything good.

Always,
{OWNER_NAME}
""",

    f"""
💌 Our Journey

Day 3 ❤️

My dear {get_today_nickname()},

I hope this letter finds you smiling.

I want you to remember that your happiness matters to me. Your peace matters. Your heart matters.

May Allah remove sadness from your path and replace it with ease, comfort, and beautiful surprises.

With care,
{OWNER_NAME}
""",

    f"""
💌 Our Journey

Day 4 ❤️

My lovely {get_today_nickname()},

Every day, I find another reason to be grateful for you.

You bring softness into my thoughts and calm into my heart. I pray Allah keeps you safe from anything that could hurt your peace.

Never forget how deeply appreciated you are.

With love,
{OWNER_NAME}
""",

    f"""
💌 Our Journey

Day 5 ❤️

My sweet {get_today_nickname()},

There are moments when I may not say everything perfectly, but my care for you is sincere.

I pray for your happiness, your growth, your safety, and your future.

May Allah make your life beautiful in ways you never expected.

Always thinking of you,
{OWNER_NAME}
""",

    f"""
💌 Our Journey

Day 6 ❤️

My dear {get_today_nickname()},

If today ever feels heavy, I hope this letter reminds you that you are not forgotten.

You are strong, kind, and precious. I pray Allah gives you ease in every matter and places peace inside your heart.

Keep smiling, my love.

With love,
{OWNER_NAME}
""",

    f"""
💌 Our Journey

Day 7 ❤️

My beautiful {get_today_nickname()},

One week of our little journey is here.

I hope these letters have made you smile, even a little. I hope they remind you that someone truly cares about your heart.

May Allah bless our bond with peace, patience, mercy, and goodness.

With all my care,
{OWNER_NAME}
""",

    f"""
💌 Our Journey

Day 8 ❤️

My dear {get_today_nickname()},

I appreciate you more than simple words can explain.

Your presence means something special to me, and I pray Allah continues to guide us toward what is good.

May your heart always find peace, and may your days be filled with blessings.

With love,
{OWNER_NAME}
""",

    f"""
💌 Our Journey

Day 9 ❤️

My lovely {get_today_nickname()},

You deserve kindness, patience, love, and peace.

I pray Allah surrounds you with people who value you properly and protects you from anything that drains your happiness.

You are special, and I hope you never forget that.

Always,
{OWNER_NAME}
""",

    f"""
💌 Our Journey

Day 10 ❤️

My sweet {get_today_nickname()},

Today, I just want to remind you how much I respect the person you are.

Your heart, your effort, your kindness, and your patience all matter.

May Allah reward you for every silent struggle and every good thing you do.

With love,
{OWNER_NAME}
""",

    f"""
💌 Our Journey

Day 11 ❤️

My dear {get_today_nickname()},

Some feelings are hard to explain, but they are easy to feel.

You bring warmth into my life, and I pray Allah keeps our connection full of honesty, care, and barakah.

May your heart stay protected always.

With care,
{OWNER_NAME}
""",

    f"""
💌 Our Journey

Day 12 ❤️

My beautiful {get_today_nickname()},

I hope you know that you are not ordinary to me.

Your smile, your heart, and your presence all mean something deeply special.

May Allah bless you with peace, confidence, happiness, and a future filled with goodness.

With love,
{OWNER_NAME}
""",

    f"""
💌 Our Journey

Day 13 ❤️

My lovely {get_today_nickname()},

As this journey continues, I keep praying that every day brings you closer to peace and happiness.

You are loved in a gentle, sincere, and respectful way.

May Allah protect you today, tomorrow, and always.

Always yours in care,
{OWNER_NAME}
""",

    f"""
💌 Our Journey

Day 14 ❤️

My dear {get_today_nickname()},

We have reached Day 14 of this first journey.

I hope every letter reminded you that you are loved, appreciated, and prayed for.

May Allah continue to bless your heart, protect your smile, and guide us toward what is best.

This is not the end. It is just another beautiful beginning.

With love,
{OWNER_NAME}
"""
]


def get_love_letter_by_day(day):
    index = (day - 1) % len(LOVE_LETTERS)
    return LOVE_LETTERS[index]


def get_today_love_letter():
    day = get_current_day()
    return get_love_letter_by_day(day)