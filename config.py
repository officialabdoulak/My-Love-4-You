import os
import random
import pytz

BOT_NAME = "My Love 4 You ❤️"

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TIMEZONE = pytz.timezone("Africa/Lagos")

OWNER_NAME = "Abdoul ❤️"
TOTAL_DAYS = 14

MORNING_MESSAGE_TIME = "07:00"
MORNING_COMPLIMENT_TIME = "07:30"
NIGHT_COMPLIMENT_TIME = "22:30"
GOOD_NIGHT_TIME = "23:00"

FRIDAY_KAHF_TIME = "09:00"
FRIDAY_JUMUAH_TIME = "11:30"

LOVER_NICKNAMES = [
    "ROOHY ❤️",
    "HABIBTY 🤍",
    "JANNAT 🌹",
    "BABE 💕",
    "SHALELE 🥰",
    "Kitty 😘",
    "BEE 🐝",
]

SIGNATURES = [
    "❤️ With all my love,\nAbdoul ❤️",
    "🤍 Always praying for your happiness.\nAbdoul ❤️",
    "🌹 Forever cheering you on.\nAbdoul ❤️",
    "🤲 May Allah protect you always.\nAbdoul ❤️",
    "🌸 Thinking of you always.\nAbdoul ❤️",
    "❤️ You are always in my duas.\nAbdoul ❤️",
]


def get_signature():
    return random.choice(SIGNATURES)