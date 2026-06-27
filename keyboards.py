from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def home_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💌 Love Letter", callback_data="love_letter"),
            InlineKeyboardButton("🤲 Daily Azkar", callback_data="daily_azkar")
        ],
        [
            InlineKeyboardButton("🎁 Open When", callback_data="open_when")
        ]
    ])


def daily_azkar_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🌅 Morning Azkar", callback_data="morning_azkar")],
        [InlineKeyboardButton("🌙 Evening Azkar", callback_data="evening_azkar")],
        [InlineKeyboardButton("😴 Before Sleeping", callback_data="sleep_azkar")],
        [InlineKeyboardButton("🏡 Home", callback_data="home")]
    ])


def love_letter_keyboard(current_day):
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⬅️ Previous", callback_data=f"love_{current_day - 1}"),
            InlineKeyboardButton("🏡 Home", callback_data="home"),
            InlineKeyboardButton("Next ➡️", callback_data=f"love_{current_day + 1}")
        ]
    ])


def dua_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏡 Home", callback_data="home")]
    ])


def jumuah_dua_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🤲 Open Jumu'ah Dua", callback_data="friday_dua")]
    ])


def open_when_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🥺 When You Miss Me", callback_data="open_miss_me")],
        [InlineKeyboardButton("😔 When You Feel Sad", callback_data="open_sad")],
        [InlineKeyboardButton("😴 When You Can't Sleep", callback_data="open_sleep")],
        [InlineKeyboardButton("💪 When You Need Strength", callback_data="open_strength")],
        [InlineKeyboardButton("🏡 Home", callback_data="home")]
    ])