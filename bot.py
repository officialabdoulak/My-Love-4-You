import random

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

from config import BOT_TOKEN, BOT_NAME, get_nickname, get_signature
from scheduler import setup_scheduler, send_photo_or_text
from database import setup_database, register_user, has_seen_welcome, mark_welcomed

from keyboards import (
    home_keyboard,
    daily_azkar_keyboard,
    dua_keyboard,
    love_letter_keyboard,
    open_when_keyboard,
    quran_keyboard,
    quran_page_keyboard,
)

from duas import get_morning_dua, get_evening_dua, get_sleep_dua, get_friday_dua
from quran import get_ayatul_kursi, get_surah_ikhlas, get_surah_falaq, get_surah_nas, get_last_baqarah
from love_letters import get_today_love_letter, get_love_letter_by_day, LOVE_LETTERS
from journey import get_current_day
from morning import get_today_morning_message, MORNING_MESSAGES
from night import get_today_night_message, NIGHT_MESSAGES
from friday import get_kahf_reminder, get_jumuah_reminder
from media import get_morning_image, get_night_image, get_kahf_image, get_jumuah_image


def format_message(message):
    return message.format(
        nickname=get_nickname(),
        signature=get_signature()
    )


def welcome_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("❤️ Begin Our Journey", callback_data="begin_journey")]
    ])


def welcome_message():
    nickname = get_nickname()

    return f"""
🌹 Welcome, {nickname}

Assalamu Alaikum ❤️

If you are reading this, it means you have opened something I made specially for you.

This is not just a Telegram bot.

It is a small place where you will find kind words, heartfelt letters, daily reminders, duas, and little moments of love whenever your heart needs them.

Some days, it will remind you to smile.

Some days, it will remind you that Allah is always with you.

And on difficult days, I hope these messages make your heart feel a little lighter.

Everything here was prepared with sincerity, and I pray it becomes a source of comfort, peace, and happiness for you.

May Allah bless your heart, protect your smile, strengthen your faith, and fill your life with endless barakah.

Welcome to our little journey. ❤️
"""


OPEN_WHEN_MESSAGES = {
    "open_miss_me": """
🥺 When You Miss Me

My love, if you are reading this because you miss me, remember that you are always close to my heart.

Distance can never remove you from my prayers.

May Allah keep our hearts connected with love, peace and barakah.
""",

    "open_sad": """
😔 When You Feel Sad

This feeling will pass In Sha Allah.

Allah never abandons the hearts that trust Him.

May He replace your sadness with peace and happiness.
""",

    "open_sleep": """
😴 When You Can't Sleep

Close your eyes.

Leave every worry with Allah.

May He grant you peaceful sleep and beautiful dreams.
""",

    "open_strength": """
💪 When You Need Strength

You are stronger than this moment.

Allah sees every struggle you carry.

Keep going.

I'm always making dua for you.
"""
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    register_user(user.id, user.first_name or "")

    if not has_seen_welcome(user.id):
        await update.message.reply_text(
            welcome_message(),
            reply_markup=welcome_keyboard()
        )
        return

    await update.message.reply_text(
        f"🏡 {BOT_NAME}\n\nWelcome home ❤️\n\nChoose what you want to open.",
        reply_markup=home_keyboard(),
    )


async def test_morning(update: Update, context: ContextTypes.DEFAULT_TYPE):
    register_user(update.effective_user.id, update.effective_user.first_name or "")

    await send_photo_or_text(
        context.bot,
        get_morning_image(),
        get_today_morning_message(),
        chat_id=update.effective_chat.id,
    )


async def test_random_morning(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_photo_or_text(
        context.bot,
        get_morning_image(),
        format_message(random.choice(MORNING_MESSAGES)),
        chat_id=update.effective_chat.id,
    )


async def test_night(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_photo_or_text(
        context.bot,
        get_night_image(),
        get_today_night_message(),
        chat_id=update.effective_chat.id,
    )


async def test_random_night(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_photo_or_text(
        context.bot,
        get_night_image(),
        format_message(random.choice(NIGHT_MESSAGES)),
        chat_id=update.effective_chat.id,
    )


async def test_kahf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_photo_or_text(
        context.bot,
        get_kahf_image(),
        get_kahf_reminder(),
        chat_id=update.effective_chat.id,
    )


async def test_jumuah(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_photo_or_text(
        context.bot,
        get_jumuah_image(),
        get_jumuah_reminder(),
        chat_id=update.effective_chat.id,
    )


async def test_random_love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(format_message(random.choice(LOVE_LETTERS)))


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = update.effective_user
    register_user(user.id, user.first_name or "")

    data = query.data
    today = get_current_day()

    if data == "begin_journey":
        mark_welcomed(user.id)
        await query.edit_message_text(
            f"🏡 {BOT_NAME}\n\nWelcome home ❤️\n\nChoose what you want to open.",
            reply_markup=home_keyboard()
        )

    elif data == "home":
        await query.edit_message_text(
            f"🏡 {BOT_NAME}\n\nChoose what you want to open.",
            reply_markup=home_keyboard(),
        )

    elif data == "daily_azkar":
        await query.edit_message_text(
            "🤲 Daily Azkar\n\nChoose one:",
            reply_markup=daily_azkar_keyboard(),
        )

    elif data == "morning_azkar":
        await query.edit_message_text(get_morning_dua(), reply_markup=dua_keyboard())

    elif data == "evening_azkar":
        await query.edit_message_text(get_evening_dua(), reply_markup=dua_keyboard())

    elif data == "sleep_azkar":
        await query.edit_message_text(get_sleep_dua(), reply_markup=dua_keyboard())

    elif data == "friday_dua":
        await query.edit_message_text(get_friday_dua(), reply_markup=dua_keyboard())

    elif data == "quran":
        await query.edit_message_text(
            "📖 Quran\n\nChoose a Surah or Verse:",
            reply_markup=quran_keyboard()
        )

    elif data == "ayatul_kursi":
        await query.edit_message_text(get_ayatul_kursi(), reply_markup=quran_page_keyboard())

    elif data == "surah_ikhlas":
        await query.edit_message_text(get_surah_ikhlas(), reply_markup=quran_page_keyboard())

    elif data == "surah_falaq":
        await query.edit_message_text(get_surah_falaq(), reply_markup=quran_page_keyboard())

    elif data == "surah_nas":
        await query.edit_message_text(get_surah_nas(), reply_markup=quran_page_keyboard())

    elif data == "last_baqarah":
        await query.edit_message_text(get_last_baqarah(), reply_markup=quran_page_keyboard())

    elif data == "love_letter":
        await query.edit_message_text(
            get_today_love_letter(),
            reply_markup=love_letter_keyboard(today)
        )

    elif data.startswith("love_"):
        requested_day = int(data.replace("love_", ""))

        if requested_day < 1:
            await query.edit_message_text(
                "🤍 This is the beginning of our journey.\n\nThere is no previous letter before Day 1.",
                reply_markup=love_letter_keyboard(today)
            )

        elif requested_day > today:
            await query.edit_message_text(
                "🤍 That chapter has not arrived yet.\n\nCome back tomorrow ❤️",
                reply_markup=love_letter_keyboard(today)
            )

        else:
            await query.edit_message_text(
                get_love_letter_by_day(requested_day),
                reply_markup=love_letter_keyboard(requested_day)
            )

    elif data == "open_when":
        await query.edit_message_text(
            "🎁 Open When...\n\nChoose one:",
            reply_markup=open_when_keyboard()
        )

    elif data in OPEN_WHEN_MESSAGES:
        await query.edit_message_text(
            OPEN_WHEN_MESSAGES[data],
            reply_markup=open_when_keyboard()
        )

    else:
        await query.edit_message_text(
            "Unknown option.",
            reply_markup=home_keyboard()
        )


def main():
    setup_database()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test_morning", test_morning))
    app.add_handler(CommandHandler("test_random_morning", test_random_morning))
    app.add_handler(CommandHandler("test_night", test_night))
    app.add_handler(CommandHandler("test_random_night", test_random_night))
    app.add_handler(CommandHandler("test_kahf", test_kahf))
    app.add_handler(CommandHandler("test_jumuah", test_jumuah))
    app.add_handler(CommandHandler("test_random_love", test_random_love))

    app.add_handler(CallbackQueryHandler(button_handler))

    setup_scheduler(app.bot)

    print(f"✅ {BOT_NAME} is running...")
    app.run_polling()


if __name__ == "__main__":
    main()