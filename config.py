import os
import random
import pytz

BOT_NAME = "My Love 4 You ❤️"

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TIMEZONE = pytz.timezone("Africa/Lagos")

OWNER_NAME = "I'm Abdoul ❤️"
TOTAL_DAYS = 14

MORNING_MESSAGE_TIME = "07:30"
MORNING_COMPLIMENT_TIME = "09:30"

NIGHT_COMPLIMENT_TIME = "21:30"
GOOD_NIGHT_TIME = "23:00"

FRIDAY_KAHF_TIME = "17:59"
FRIDAY_JUMUAH_TIME = "18:00"

LOVER_NICKNAMES = [
    "ROOHY ❤️",
    "HABIBTY 🤍",
    "JANNAT 🌹",
    "BABE 💖",
    "SHALELE 🥰",
    "KITTY 😘",
    "BEE 🐝",
    "MY PEACE 🕊️",
    "SUNSHINE ☀️",
    "QALBI ❤️",
]

SIGNATURES = [
    "❤️ With all my love,\nAbdoul ❤️",
    "🤍 Always praying for your happiness.\nAbdoul ❤️",
    "🌹 Forever cheering you on.\nAbdoul ❤️",
    "🤲 May Allah protect you always.\nAbdoul ❤️",
    "🌸 Thinking of you always.\nAbdoul ❤️",
    "💖 You are always in my duas.\nAbdoul ❤️",
    "🕊️ May your heart always find peace.\nAbdoul ❤️",
    "✨ Stay safe and keep smiling.\nAbdoul ❤️",
    "🌙 Until tomorrow, take care of yourself.\nAbdoul ❤️",
    "💛 Always grateful that Allah brought you into my life.\nAbdoul ❤️",
]


def get_signature():
    return random.choice(SIGNATURES)


def get_nickname():
    return random.choice(LOVER_NICKNAMES)