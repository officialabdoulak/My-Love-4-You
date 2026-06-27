import random

from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

from config import BOT_TOKEN, BOT_NAME, TOTAL_DAYS
from scheduler import setup_scheduler, send_photo_or_text

from keyboards import (
    home_keyboard,
    daily_azkar_keyboard,
    friday_keyboard,
    dua_keyboard,
    love_letter_keyboard,
)

from duas import get_morning_dua, get_evening_dua, get_sleep_dua, get_friday_dua
from love_letters import get_today_love_letter, LOVE_LETTERS
from journey import get_current_day

from morning import get_today_morning_message, MORNING_MESSAGES
from night import get_today_night_message, NIGHT_MESSAGES
from friday import get_kahf_reminder, get_jumuah_reminder

from media import (
    get_morning_image,
    get_night_image,
    get_kahf_image,
    get_jumuah_image,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = f"""
🏡 {BOT_NAME}

Welcome home ❤️

Choose what you want to open.
"""
    await update.message.reply_text(text, reply_markup=home_keyboard())


async def test_morning(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_photo_or_text(context.bot, get_morning_image(), get_today_morning_message())


async def test_random_morning(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = random.choice(MORNING_MESSAGES)
    await send_photo_or_text(context.bot, get_morning_image(), message)


async def test_night(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_photo_or_text(context.bot, get_night_image(), get_today_night_message())


async def test_random_night(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = random.choice(NIGHT_MESSAGES)
    await send_photo_or_text(context.bot, get_night_image(), message)


async def test_kahf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_photo_or_text(context.bot, get_kahf_image(), get_kahf_reminder())


async def test_jumuah(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_photo_or_text(context.bot, get_jumuah_image(), get_jumuah_reminder())


async def test_random_love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = random.choice(LOVE_LETTERS)
    await update.message.reply_text(message)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "home":
        await query.edit_message_text(
            f"🏡 {BOT_NAME}\n\nChoose what you want to open.",
            reply_markup=home_keyboard()
        )

    elif data == "daily_azkar":
        await query.edit_message_text(
            "🤲 Daily Azkar\n\nChoose one:",
            reply_markup=daily_azkar_keyboard()
        )

    elif data == "morning_azkar":
        await query.edit_message_text(get_morning_dua(), reply_markup=dua_keyboard())

    elif data == "evening_azkar":
        await query.edit_message_text(get_evening_dua(), reply_markup=dua_keyboard())

    elif data == "sleep_azkar":
        await query.edit_message_text(get_sleep_dua(), reply_markup=dua_keyboard())

    elif data == "friday":
        await query.edit_message_text(
            "🕌 Friday\n\nChoose one:",
            reply_markup=friday_keyboard()
        )

    elif data == "kahf_page_1":
        await query.edit_message_text(get_kahf_reminder(), reply_markup=dua_keyboard())

    elif data == "friday_dua":
        await query.edit_message_text(get_friday_dua(), reply_markup=dua_keyboard())

    elif data == "love_letter":
        day = get_current_day()
        await query.edit_message_text(
            get_today_love_letter(),
            reply_markup=love_letter_keyboard(day, TOTAL_DAYS)
        )

    elif data.startswith("love_"):
        day = get_current_day()
        await query.edit_message_text(
            get_today_love_letter(),
            reply_markup=love_letter_keyboard(day, TOTAL_DAYS)
        )

    else:
        await query.edit_message_text(
            "I don't understand this button yet.",
            reply_markup=home_keyboard()
        )


def main():
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

    print(f"{BOT_NAME} is running...")
    app.run_polling()


if __name__ == "__main__":
    main()