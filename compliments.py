from journey import get_current_day
from config import get_nickname


MORNING_COMPLIMENTS = [
    "💛 Good morning, {nickname}. Your smile has a way of making everything feel softer.",
    "🌸 Good morning, {nickname}. I hope you remember how precious your heart is today.",
    "☀️ Good morning, {nickname}. Your kindness is one of the most beautiful things about you.",
    "🤍 Good morning, {nickname}. You carry a calm beauty that words can barely explain.",
    "🌹 Good morning, {nickname}. I admire the way you keep going, even on quiet hard days.",
    "🕊️ Good morning, {nickname}. Your presence brings peace in a way I truly appreciate.",
    "✨ Good morning, {nickname}. You are beautiful, not only in face, but in heart too.",
    "🌷 Good morning, {nickname}. I hope today treats your gentle heart with care.",
    "💫 Good morning, {nickname}. Your patience and softness make you special to me.",
    "🌻 Good morning, {nickname}. You deserve a day as lovely as the happiness you bring.",
    "☕ Good morning, {nickname}. I hope you know how deeply appreciated you are.",
    "🌼 Good morning, {nickname}. Your heart is rare, and I pray Allah always protects it.",
    "💐 Good morning, {nickname}. I love the peaceful feeling your name brings to my heart.",
    "❤️ Good morning, {nickname}. You are a beautiful blessing I never want to take for granted.",
]


NIGHT_COMPLIMENTS = [
    "🌙 Sleep peacefully, {nickname}. Your heart deserves rest, comfort, and endless happiness.",
    "🤍 Good night, {nickname}. No matter how today went, I am still proud of you.",
    "✨ Rest well, {nickname}. You are deeply valued more than simple words can explain.",
    "🕊️ Good night, {nickname}. Your softness is beautiful, and I pray life stays gentle with you.",
    "🌹 Sleep well, {nickname}. You have such a lovely soul, and I hope you never forget that.",
    "💛 Good night, {nickname}. Your smile stayed in my thoughts more than once today.",
    "🌸 Rest your heart, {nickname}. You are cared for, prayed for, and truly appreciated.",
    "💫 Good night, {nickname}. Even from far away, your presence still feels close to my heart.",
    "🌷 Sleep calmly, {nickname}. You did enough today, and you deserve peace tonight.",
    "❤️ Good night, {nickname}. You are special to me in a way I always thank Allah for.",
    "🌻 Rest well, {nickname}. Your kindness makes you unforgettable.",
    "☁️ Good night, {nickname}. I hope your dreams feel as peaceful as your heart deserves.",
    "🤲 Sleep peacefully, {nickname}. May Allah protect your heart and reward your patience.",
    "🌙 Good night, {nickname}. You are loved, appreciated, and always remembered in my duas.",
]


def get_today_morning_compliment():
    day = get_current_day()
    index = (day - 1) % len(MORNING_COMPLIMENTS)
    return MORNING_COMPLIMENTS[index].format(nickname=get_nickname())


def get_today_night_compliment():
    day = get_current_day()
    index = (day - 1) % len(NIGHT_COMPLIMENTS)
    return NIGHT_COMPLIMENTS[index].format(nickname=get_nickname())