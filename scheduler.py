from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import (
    TIMEZONE,
    MORNING_MESSAGE_TIME,
    MORNING_COMPLIMENT_TIME,
    NIGHT_COMPLIMENT_TIME,
    GOOD_NIGHT_TIME,
    FRIDAY_KAHF_TIME,
    FRIDAY_JUMUAH_TIME,
)

from database import get_all_user_ids

from media import (
    get_morning_image,
    get_night_image,
    get_kahf_image,
    get_jumuah_image,
)

from morning import get_today_morning_message
from night import get_today_night_message
from compliments import get_today_morning_compliment, get_today_night_compliment
from friday import get_kahf_reminder, get_jumuah_reminder
from keyboards import jumuah_dua_keyboard


def split_time(time_text):
    hour, minute = time_text.split(":")
    return int(hour), int(minute)


async def send_photo_or_text(bot, image_path, text, chat_id=None, reply_markup=None):
    if chat_id is None:
        return

    if image_path:
        with open(image_path, "rb") as photo:
            await bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                caption=text,
                reply_markup=reply_markup
            )
    else:
        await bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=reply_markup
        )


async def broadcast_photo_or_text(bot, image_path, text, reply_markup=None):
    user_ids = get_all_user_ids()

    for user_id in user_ids:
        await send_photo_or_text(
            bot,
            image_path,
            text,
            chat_id=user_id,
            reply_markup=reply_markup
        )


async def broadcast_text(bot, text):
    user_ids = get_all_user_ids()

    for user_id in user_ids:
        await bot.send_message(chat_id=user_id, text=text)


async def send_morning_message(bot):
    await broadcast_photo_or_text(
        bot,
        get_morning_image(),
        get_today_morning_message()
    )


async def send_morning_compliment(bot):
    await broadcast_text(bot, get_today_morning_compliment())


async def send_night_compliment(bot):
    await broadcast_text(bot, get_today_night_compliment())


async def send_good_night_message(bot):
    await broadcast_photo_or_text(
        bot,
        get_night_image(),
        get_today_night_message()
    )


async def send_kahf_reminder(bot):
    await broadcast_photo_or_text(
        bot,
        get_kahf_image(),
        get_kahf_reminder(),
        reply_markup=jumuah_dua_keyboard()
    )


async def send_jumuah_reminder(bot):
    await broadcast_photo_or_text(
        bot,
        get_jumuah_image(),
        get_jumuah_reminder(),
        reply_markup=jumuah_dua_keyboard()
    )


def setup_scheduler(bot):
    scheduler = AsyncIOScheduler(timezone=TIMEZONE)

    morning_hour, morning_minute = split_time(MORNING_MESSAGE_TIME)
    morning_comp_hour, morning_comp_minute = split_time(MORNING_COMPLIMENT_TIME)
    night_comp_hour, night_comp_minute = split_time(NIGHT_COMPLIMENT_TIME)
    good_night_hour, good_night_minute = split_time(GOOD_NIGHT_TIME)
    kahf_hour, kahf_minute = split_time(FRIDAY_KAHF_TIME)
    jumuah_hour, jumuah_minute = split_time(FRIDAY_JUMUAH_TIME)

    scheduler.add_job(send_morning_message, "cron", hour=morning_hour, minute=morning_minute, args=[bot])
    scheduler.add_job(send_morning_compliment, "cron", hour=morning_comp_hour, minute=morning_comp_minute, args=[bot])
    scheduler.add_job(send_night_compliment, "cron", hour=night_comp_hour, minute=night_comp_minute, args=[bot])
    scheduler.add_job(send_good_night_message, "cron", hour=good_night_hour, minute=good_night_minute, args=[bot])

    scheduler.add_job(send_kahf_reminder, "cron", day_of_week="fri", hour=kahf_hour, minute=kahf_minute, args=[bot])
    scheduler.add_job(send_jumuah_reminder, "cron", day_of_week="fri", hour=jumuah_hour, minute=jumuah_minute, args=[bot])

    scheduler.start()
    return scheduler