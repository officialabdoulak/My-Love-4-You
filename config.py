import os
import random
import pytz

BOT_NAME = "My Love 4 You ❤️"

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TIMEZONE = pytz.timezone("Africa/Lagos")

OWNER_NAME = "I'm Abdoul ❤️"
TOTAL_DAYS = 14

MORNING_MESSAGE_TIME = "17:55"
MORNING_COMPLIMENT_TIME = "17:56"
NIGHT_COMPLIMENT_TIME = "17:57"
GOOD_NIGHT_TIME = "17:58"

FRIDAY_KAHF_TIME = "17:59"
FRIDAY_JUMUAH_TIME = "18:00"

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