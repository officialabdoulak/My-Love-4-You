from journey import get_current_day
from config import get_nickname, get_signature


NIGHT_MESSAGES = [
    """
🌙 Good Night, {nickname}

Before you close your eyes tonight, leave every worry with Allah.

You did your best today, and that is enough.

May Allah protect you while you sleep, calm your heart, forgive your shortcomings, and let you wake up with peace.

Sleep well, my love. ❤️

{signature}
""",

    """
🌙 Sleep Well, {nickname}

The day has come to an end.

I hope your heart can finally rest after everything you've carried today.

May Allah grant you peaceful sleep, beautiful dreams, and a heart full of tranquility.

{signature}
""",

    """
✨ Good Night, {nickname}

One last reminder before you sleep...

You are loved.
You are appreciated.
You are always remembered in my duas.

May Allah surround your night with mercy and your morning with joy.

{signature}
""",

    """
🤍 Good Night, {nickname}

As you close your eyes tonight, remember that tomorrow is another chance filled with Allah's mercy.

Sleep peacefully knowing that someone sincerely prays for your happiness every day.

{signature}
""",

    """
🌹 Good Night, {nickname}

No matter how today went, I hope you are proud of yourself.

Every small step you take matters.

May Allah reward your patience and grant you a peaceful night.

{signature}
""",

    """
🌌 Good Night, {nickname}

The stars are shining tonight, but none of them shine brighter than your beautiful heart.

May Allah keep you safe until the morning arrives.

{signature}
""",

    """
💛 Good Night, {nickname}

Thank you for simply being you.

I pray Allah fills your dreams with peace and removes every worry from your heart.

Sleep beautifully.

{signature}
""",

    """
🕊️ Good Night, {nickname}

May your soul find complete rest tonight.

Leave every burden with Allah and sleep knowing He is the Best Protector.

{signature}
""",

    """
🌸 Good Night, {nickname}

I hope today gave you at least one reason to smile.

Tomorrow, In Sha Allah, will bring even more reasons.

Rest peacefully.

{signature}
""",

    """
🌙 Sleep Tight, {nickname}

May Allah place barakah in your sleep, strengthen your heart, and make tomorrow easier than today.

You deserve peace.

{signature}
""",

    """
✨ Rest Well, {nickname}

Even when words are few, my duas for you never stop.

May Allah protect your heart, your mind, and your dreams tonight.

{signature}
""",

    """
🤲 Good Night, {nickname}

I pray Allah forgives your sins, accepts your worship, grants you Jannatul Firdaus, and blesses every step of your journey.

Ameen.

{signature}
""",

    """
🌷 Good Night, {nickname}

Your heart deserves kindness.

Your mind deserves peace.

Your soul deserves rest.

Sleep well knowing you are deeply appreciated.

{signature}
""",

    """
❤️ Good Night, {nickname}

Another day has passed.

Alhamdulillah for every blessing, every lesson, and every moment.

May Allah wake you tomorrow with happiness, good health, and endless barakah.

{signature}
"""
]


def get_today_night_message():
    day = get_current_day()
    index = (day - 1) % len(NIGHT_MESSAGES)

    return NIGHT_MESSAGES[index].format(
        nickname=get_nickname(),
        signature=get_signature()
    )