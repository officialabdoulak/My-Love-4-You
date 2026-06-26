from datetime import datetime
from config import TOTAL_DAYS, TIMEZONE, LOVER_NICKNAMES

START_DATE = datetime(2026, 6, 26)


def get_current_day():
    today = datetime.now(TIMEZONE).replace(tzinfo=None)
    days_passed = (today.date() - START_DATE.date()).days
    return (days_passed % TOTAL_DAYS) + 1


def get_today_nickname():
    day = get_current_day()
    index = (day - 1) % len(LOVER_NICKNAMES)
    return LOVER_NICKNAMES[index]


def get_progress():
    return f"Day {get_current_day()} of {TOTAL_DAYS}"