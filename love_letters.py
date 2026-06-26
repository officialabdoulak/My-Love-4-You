from journey import get_current_day, get_today_nickname
from config import OWNER_NAME


LOVE_LETTERS = [

f"""
💌 My Dearest {get_today_nickname()},

Sometimes I wonder if you truly know how much you mean to me.

Life becomes a little brighter whenever I think about you, and even on difficult days, remembering you gives me peace.

I pray Allah continues to protect your heart, increase your happiness, and grant us both goodness in this life and the next.

Never doubt that you are appreciated, respected, and sincerely cared for.

May every step you take bring you closer to success, peace, and Jannah.

With all my love,

{OWNER_NAME} ❤️
""",

f"""
💖 My Beloved {get_today_nickname()},

I may not always find the perfect words, but my du'as for you never stop.

Every day I ask Allah to keep you smiling, protect you from sadness, and bless everything you do.

Thank you for simply being yourself.

You make this journey of life feel more meaningful than you probably realize.

May Allah write nothing but goodness for you.

Forever yours,

{OWNER_NAME} ❤️
""",

f"""
🌹 My Precious {get_today_nickname()},

If today has been difficult, I hope this little letter reminds you that you are never alone.

You are stronger than you think, more beautiful than you know, and more appreciated than words can fully express.

May Allah replace every worry with peace, every sadness with happiness, and every hardship with ease.

Keep believing in yourself because I always will.

With endless love,

{OWNER_NAME} ❤️
"""
]


def get_today_love_letter():
    day = get_current_day()

    index = (day - 1) % len(LOVE_LETTERS)

    return LOVE_LETTERS[index]