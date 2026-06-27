import random

from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

from config import BOT_TOKEN, BOT_NAME
from scheduler import setup_scheduler, send_photo_or_text

from keyboards import (
    home_keyboard,
    daily_azkar_keyboard,
    dua_keyboard,
    love_letter_keyboard,
    open_when_keyboard,
)

from duas import get_morning_dua, get_evening_dua, get_sleep_dua, get_friday_dua
from love_letters import get_today_love_letter, get_love_letter_by_day, LOVE_LETTERS
from journey import get_current_day

from morning import get_today_morning_message, MORNING_MESSAGES
from night import get_today_night_message, NIGHT_MESSAGES
from friday import get_kahf_reminder, get_jumuah_reminder

from media import get_morning_image, get_night_image, get_kahf_image, get_jumuah_image


OPEN_WHEN_MESSAGES = {
    "open_miss_me": """
🥺 When You Miss Me

My love, if you are reading this because you miss me, I want you to know that you are always close to my heart.

Distance, silence, or a busy day can never remove you from my thoughts.

May Allah keep our hearts connected with peace, patience, and love. ❤️
""",

    "open_sad": """
😔 When You Feel Sad

My love, I wish I could sit beside you and remind you that this feeling will not last forever.

Breathe slowly. Let your heart rest.

May Allah remove your sadness, replace it with peace, and give you a reason to smile again. 🤍
""",

    "open_sleep": """
😴 When You Can't Sleep

My love, close your eyes gently and leave every worry with Allah.

You do not have to solve everything tonight.

May Allah calm your heart, protect your dreams, and let you wake up with peace. 🌙
""",

    "open_strength": """
💪 When You Need Strength

My love, you are stronger than this moment.

Allah sees your effort, your patience, and every silent struggle you carry.

Keep going gently. I believe in you, and I am always praying for you. ❤️
"""
}


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
    await send_photo_or_text(context.bot, get_morning_image(), random.choice(MORNING_MESSAGES))


async def test_night(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_photo_or_text(context.bot, get_night_image(), get_today_night_message())


async def test_random_night(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_photo_or_text(context.bot, get_night_image(), random.choice(NIGHT_MESSAGES))


async def test_kahf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_photo_or_text(context.bot, get_kahf_image(), get_kahf_reminder())


async def test_jumuah(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_photo_or_text(context.bot, get_jumuah_image(), get_jumuah_reminder())


async def test_random_love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(LOVE_LETTERS))


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data
    today = get_current_day()

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

    elif data == "friday_dua":
        await query.edit_message_text(get_friday_dua(), reply_markup=dua_keyboard())

    elif data == "love_letter":
        await query.edit_message_text(
            get_today_love_letter(),
            reply_markup=love_letter_keyboard(today)
        )

    elif data.startswith("love_"):
        requested_day = int(data.replace("love_", ""))

        if requested_day < 1:
            await query.edit_message_text(
                "🤍 This is the first chapter of our journey.\n\nThere is no previous letter before Day 1.",
                reply_markup=love_letter_keyboard(today)
            )

        elif requested_day > today:
            await query.edit_message_text(
                "🤍 That chapter is not ready yet.\n\nCome back tomorrow and let us continue our journey together. ❤️",
                reply_markup=love_letter_keyboard(today)
            )

        else:
            await query.edit_message_text(
                get_love_letter_by_day(requested_day),
                reply_markup=love_letter_keyboard(requested_day)
            )

    elif data == "open_when":
        await query.edit_message_text(
            "🎁 Open When...\n\nChoose the message your heart needs today:",
            reply_markup=open_when_keyboard()
        )

    elif data in OPEN_WHEN_MESSAGES:
        await query.edit_message_text(
            OPEN_WHEN_MESSAGES[data],
            reply_markup=open_when_keyboard()
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