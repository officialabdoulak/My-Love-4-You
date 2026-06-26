from journey import get_current_day, get_today_nickname


MORNING_COMPLIMENTS = [

f"💛 Good morning, {get_today_nickname()}. Never forget how beautiful your smile is.",

f"🌸 {get_today_nickname()}, I hope today reminds you how amazing you truly are.",

f"☀️ Just thinking about you made my morning brighter, {get_today_nickname()}.",

]


NIGHT_COMPLIMENTS = [

f"🌙 Sleep peacefully, {get_today_nickname()}. You deserve every bit of happiness.",

f"🤍 No matter how today went, I'm still proud of you, {get_today_nickname()}.",

f"✨ End your day with a smile, {get_today_nickname()}. You are deeply appreciated.",

]


def get_today_morning_compliment():
    day = get_current_day()
    index = (day - 1) % len(MORNING_COMPLIMENTS)
    return MORNING_COMPLIMENTS[index]


def get_today_night_compliment():
    day = get_current_day()
    index = (day - 1) % len(NIGHT_COMPLIMENTS)
    return NIGHT_COMPLIMENTS[index]