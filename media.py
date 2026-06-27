import os
import random

MEDIA_DIR = "media"

MORNING_IMAGES = [
    os.path.join(MEDIA_DIR, "morning", f)
    for f in os.listdir(os.path.join(MEDIA_DIR, "morning"))
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

NIGHT_IMAGES = [
    os.path.join(MEDIA_DIR, "night", f)
    for f in os.listdir(os.path.join(MEDIA_DIR, "night"))
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

KAHF_IMAGES = [
    os.path.join(MEDIA_DIR, "kahf", f)
    for f in os.listdir(os.path.join(MEDIA_DIR, "kahf"))
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

JUMUAH_IMAGES = [
    os.path.join(MEDIA_DIR, "jumuah", f)
    for f in os.listdir(os.path.join(MEDIA_DIR, "jumuah"))
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]


def get_morning_image():
    return random.choice(MORNING_IMAGES)


def get_random_morning_image():
    return random.choice(MORNING_IMAGES)


def get_night_image():
    return random.choice(NIGHT_IMAGES)


def get_random_night_image():
    return random.choice(NIGHT_IMAGES)


def get_kahf_image():
    return random.choice(KAHF_IMAGES)


def get_jumuah_image():
    return random.choice(JUMUAH_IMAGES)