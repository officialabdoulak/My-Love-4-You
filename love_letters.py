from journey import get_current_day
from config import get_nickname, get_signature


LOVE_LETTERS = [
    """
💌 Our Journey

Day 1 ❤️

My dear {nickname},

Today is the beginning of this little journey, and I want this first letter to remind you of something simple but important.

You are valued. You are appreciated. You are remembered in my duas.

Life can get busy, people can get tired, and some days may feel heavier than others, but I hope this message gives your heart a soft place to rest.

May Allah protect your smile, guide your steps, and place peace in every corner of your heart.

May He keep you away from sadness, bless your efforts, and open doors of goodness for you in ways you never expected.

This journey is only beginning, and I pray every day brings you comfort, happiness, and barakah.

{signature}
""",

    """
💌 Our Journey

Day 2 ❤️

My dear {nickname},

Today I just want to appreciate you.

Not for anything big or loud, but for the quiet beauty in the way you keep going, the kindness you carry, and the peace your presence brings.

Some people make life feel softer just by being themselves, and you are one of those people.

I pray Allah rewards your patience, protects your heart, and gives you happiness that does not fade quickly.

May your day be filled with good news, calm thoughts, and reasons to smile.

May Allah bless you with ease in every matter and keep you surrounded by mercy.

You deserve kindness, peace, and every good thing Allah has written for you.

{signature}
""",

    """
💌 Our Journey

Day 3 ❤️

My dear {nickname},

Some days may feel quiet, but I hope you never feel forgotten.

You are remembered in my duas, and I pray Allah keeps you safe wherever you are.

I pray He removes every worry from your heart and replaces it with calmness, strength, and beautiful patience.

You have a gentle heart, and I hope life treats it with care.

May Allah guide you toward what is best, protect you from what may hurt you, and bless you with happiness that feels peaceful.

No matter how the day goes, I hope this letter reminds you that your peace matters.

Your smile matters.

Your heart matters.

{signature}
""",

    """
💌 Our Journey

Day 4 ❤️

My dear {nickname},

Today, I want to remind you that your smile is a blessing.

There is something beautiful about seeing someone carry light even when life is not perfect.

I pray Allah gives you more reasons to smile and fewer reasons to worry.

May He bless your morning, protect your evening, and place comfort in your heart throughout the day.

Sometimes the smallest moments bring the biggest peace, and I pray today gives you one of those moments.

May Allah keep your heart soft, your mind calm, and your soul close to Him.

You are appreciated more than simple words can fully explain.

{signature}
""",

    """
💌 Our Journey

Day 5 ❤️

My dear {nickname},

Trust and patience are not always easy, but they are beautiful when they are protected with honesty and care.

I pray Allah fills your heart with patience that does not break you, but strengthens you.

May He guide your choices, protect your emotions, and make every difficult thing easier for you.

You do not have to carry everything alone.

Allah sees what is hidden, understands what is unspoken, and rewards every sincere heart.

I pray your life becomes lighter, your worries become smaller, and your happiness becomes stronger.

May Allah bless you with peace that stays.

{signature}
""",

    """
💌 Our Journey

Day 6 ❤️

My dear {nickname},

I admire your strength.

Not the loud kind of strength, but the quiet one.

The kind that keeps going even when things are not easy.

The kind that smiles, tries, and still hopes for better days.

I pray Allah rewards every silent struggle you have faced and every effort people did not notice.

May He give you strength when you feel tired, patience when things feel heavy, and happiness when your heart needs comfort.

You are stronger than many moments that tried to make you feel weak.

May Allah always protect you and raise you in goodness.

{signature}
""",

    """
💌 Our Journey

Day 7 ❤️

My dear {nickname},

Today marks one week of this little journey.

Seven days of reminders, prayers, care, and soft words.

I hope each letter has made your heart smile, even if only a little.

I pray Allah keeps filling your days with mercy, your nights with peace, and your life with blessings.

May He protect what is good for you and remove what is harmful without making your heart heavy.

You deserve to feel safe, respected, valued, and appreciated.

May this week be only the beginning of many beautiful reminders.

{signature}
""",

    """
💌 Our Journey

Day 8 ❤️

My dear {nickname},

Today is about appreciation.

I appreciate your heart, your patience, your kindness, and the peaceful way you exist.

Sometimes people do not realize how much their presence means, but I hope you know yours is special.

I pray Allah blesses you with happiness that reaches deep into your heart.

May He grant you good health, strong faith, calm thoughts, and beautiful moments.

May your path be protected from harm and filled with light.

You are not ordinary, and I hope this letter reminds you of that.

{signature}
""",

    """
💌 Our Journey

Day 9 ❤️

My dear {nickname},

Today I make dua for you.

May Allah forgive your sins, accept your prayers, increase your rizq, protect your heart, and bless your future.

May He guide you when you feel confused, comfort you when you feel tired, and strengthen you when life feels heavy.

May He place barakah in your time, your health, your dreams, and your relationships.

I pray your heart never loses hope in Allah's mercy.

I pray your smile returns quickly after every difficult moment.

May Allah write goodness for you in this life and the next.

Ameen.

{signature}
""",

    """
💌 Our Journey

Day 10 ❤️

My dear {nickname},

Some memories do not need to be loud to be special.

Sometimes it is the simple talks, the little smiles, the calm moments, and the quiet care that stay in the heart.

I pray Allah blesses every good memory and replaces every painful one with healing.

May He keep your heart free from bitterness and full of peace.

May your future hold moments that make you grateful you kept going.

You deserve memories that feel safe, warm, and beautiful.

I pray Allah keeps guiding your story toward what is best for you.

{signature}
""",

    """
💌 Our Journey

Day 11 ❤️

My dear {nickname},

Your heart is one of the most beautiful things about you.

A good heart is not something small.

It is a blessing from Allah, and I pray He protects yours from people, places, and moments that may drain it.

May your kindness never be used against you.

May your softness never make you feel weak.

May Allah surround you with people who value you properly and treat your heart with care.

You deserve respect, honesty, peace, and gentle words.

May Allah always keep your heart close to Him.

{signature}
""",

    """
💌 Our Journey

Day 12 ❤️

My dear {nickname},

When I think about the future, I always pray that Allah writes what is best.

Not what is rushed, not what is forced, but what is peaceful, halal, and full of barakah.

May Allah guide every step ahead of you.

May He protect you from wrong paths and open doors that bring you closer to happiness, faith, and success.

I pray your future is brighter than your fears and calmer than your worries.

May Allah bless you with a life that makes your heart grateful.

You deserve a future filled with goodness.

{signature}
""",

    """
💌 Our Journey

Day 13 ❤️

My dear {nickname},

Today, I just want to thank Allah for every beautiful thing He places in life.

For peace after stress.

For smiles after sadness.

For hope after worry.

And for kind hearts that make life feel softer.

I pray Allah continues to bless you, protect you, and guide you.

May He make your heart firm in faith, your days full of ease, and your nights full of peace.

You are a blessing in your own way, and I hope you never forget that.

May Allah always keep you safe.

{signature}
""",

    """
💌 Our Journey

Day 14 ❤️

My dear {nickname},

We have reached Day 14 of this journey.

But this does not feel like an ending.

It feels like a beautiful reminder that care can be shown in small, consistent ways.

I hope every letter made you smile, gave your heart comfort, or reminded you that you are valued.

May Allah bless your life with peace, protect your heart from sadness, and guide you toward everything good.

May He make your days easier, your duas accepted, and your happiness lasting.

This is only another beginning.

May Allah write more beautiful days ahead.

{signature}
"""
]


def get_love_letter_by_day(day):
    index = (day - 1) % len(LOVE_LETTERS)

    return LOVE_LETTERS[index].format(
        nickname=get_nickname(),
        signature=get_signature()
    )


def get_today_love_letter():
    day = get_current_day()
    return get_love_letter_by_day(day)