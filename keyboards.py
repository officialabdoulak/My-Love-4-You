from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# ==========================================
# HOME
# ==========================================

def home_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💌 Love Letter", callback_data="love_letter"),
            InlineKeyboardButton("🤲 Daily Azkar", callback_data="daily_azkar")
        ],
        [
            InlineKeyboardButton("🕌 Friday", callback_data="friday")
        ]
    ])


# ==========================================
# DAILY AZKAR MENU
# ==========================================

def daily_azkar_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🌅 Morning Azkar", callback_data="morning_azkar")
        ],
        [
            InlineKeyboardButton("🌙 Evening Azkar", callback_data="evening_azkar")
        ],
        [
            InlineKeyboardButton("😴 Before Sleeping", callback_data="sleep_azkar")
        ],
        [
            InlineKeyboardButton("🏡 Home", callback_data="home")
        ]
    ])


# ==========================================
# FRIDAY MENU
# ==========================================

def friday_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📖 Read Surah Al-Kahf", callback_data="kahf_page_1")
        ],
        [
            InlineKeyboardButton("🤲 Friday Dua", callback_data="friday_dua")
        ],
        [
            InlineKeyboardButton("🏡 Home", callback_data="home")
        ]
    ])


# ==========================================
# LOVE LETTER
# ==========================================

def love_letter_keyboard(current_day, total_days):

    keyboard = []

    navigation = []

    if current_day > 1:
        navigation.append(
            InlineKeyboardButton(
                "⬅ Previous",
                callback_data=f"love_{current_day-1}"
            )
        )

    if current_day < total_days:
        navigation.append(
            InlineKeyboardButton(
                "Next ➡",
                callback_data=f"love_{current_day+1}"
            )
        )

    if navigation:
        keyboard.append(navigation)

    keyboard.append([
        InlineKeyboardButton("🏡 Home", callback_data="home")
    ])

    return InlineKeyboardMarkup(keyboard)


# ==========================================
# DUA SCREEN
# ==========================================

def dua_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🏡 Home", callback_data="home")
        ]
    ])


# ==========================================
# SURAH AL-KAHF PAGES
# ==========================================

def kahf_keyboard(current_page, total_pages):

    keyboard = []

    navigation = []

    if current_page > 1:
        navigation.append(
            InlineKeyboardButton(
                "⬅ Previous",
                callback_data=f"kahf_page_{current_page-1}"
            )
        )

    if current_page < total_pages:
        navigation.append(
            InlineKeyboardButton(
                "Next ➡",
                callback_data=f"kahf_page_{current_page+1}"
            )
        )

    if navigation:
        keyboard.append(navigation)

    if current_page == total_pages:
        keyboard.append([
            InlineKeyboardButton(
                "🤲 Friday Dua",
                callback_data="friday_dua"
            )
        ])

    keyboard.append([
        InlineKeyboardButton(
            "🏡 Home",
            callback_data="home"
        )
    ])

    return InlineKeyboardMarkup(keyboard)