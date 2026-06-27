from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# ==========================
# HOME
# ==========================

def home_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💌 Love Letter", callback_data="love_letter"),
            InlineKeyboardButton("🤲 Daily Azkar", callback_data="daily_azkar"),
        ],
        [
            InlineKeyboardButton("🎁 Open When", callback_data="open_when")
        ]
    ])


# ==========================
# DAILY AZKAR
# ==========================

def daily_azkar_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🌅 Morning Azkar", callback_data="morning_azkar")],
        [InlineKeyboardButton("🌙 Evening Azkar", callback_data="evening_azkar")],
        [InlineKeyboardButton("😴 Before Sleeping", callback_data="sleep_azkar")],
        [InlineKeyboardButton("📖 Quran", callback_data="quran")],
        [
            InlineKeyboardButton("⬅ Back", callback_data="home"),
            InlineKeyboardButton("🏠 Home", callback_data="home")
        ]
    ])


# ==========================
# QURAN MENU
# ==========================

def quran_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🪑 Ayatul Kursi", callback_data="ayatul_kursi")],
        [InlineKeyboardButton("📖 Surah Al-Ikhlas", callback_data="surah_ikhlas")],
        [InlineKeyboardButton("📖 Surah Al-Falaq", callback_data="surah_falaq")],
        [InlineKeyboardButton("📖 Surah An-Nas", callback_data="surah_nas")],
        [InlineKeyboardButton("📖 Last 2 Verses of Al-Baqarah", callback_data="last_baqarah")],
        [
            InlineKeyboardButton("⬅ Back", callback_data="daily_azkar"),
            InlineKeyboardButton("🏠 Home", callback_data="home")
        ]
    ])


# ==========================
# QURAN PAGE
# ==========================

def quran_page_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⬅ Back", callback_data="quran"),
            InlineKeyboardButton("🏠 Home", callback_data="home")
        ]
    ])


# ==========================
# DUA PAGE
# ==========================

def dua_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⬅ Back", callback_data="daily_azkar"),
            InlineKeyboardButton("🏠 Home", callback_data="home")
        ]
    ])


# ==========================
# JUMU'AH DUA
# ==========================

def jumuah_dua_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🤲 Read Jumu'ah Dua", callback_data="friday_dua")
        ],
        [
            InlineKeyboardButton("🏠 Home", callback_data="home")
        ]
    ])


# ==========================
# LOVE LETTER
# ==========================

def love_letter_keyboard(current_day):
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⬅ Previous", callback_data=f"love_{current_day-1}"),
            InlineKeyboardButton("🏠 Home", callback_data="home"),
            InlineKeyboardButton("Next ➡", callback_data=f"love_{current_day+1}")
        ]
    ])


# ==========================
# OPEN WHEN
# ==========================

def open_when_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🥺 When You Miss Me", callback_data="open_miss_me")],
        [InlineKeyboardButton("😔 When You Feel Sad", callback_data="open_sad")],
        [InlineKeyboardButton("😴 When You Can't Sleep", callback_data="open_sleep")],
        [InlineKeyboardButton("💪 When You Need Strength", callback_data="open_strength")],
        [
            InlineKeyboardButton("⬅ Back", callback_data="home"),
            InlineKeyboardButton("🏠 Home", callback_data="home")
        ]
    ])