import os
import random

ASSETS_DIR = "assets"


def _get_random_image(folder):
    folder_path = os.path.join(ASSETS_DIR, folder)

    if not os.path.exists(folder_path):
        return None

    images = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
    ]

    if not images:
        return None

    return random.choice(images)


def get_morning_image():
    return _get_random_image("morning")


def get_random_morning_image():
    return _get_random_image("morning")


def get_night_image():
    return _get_random_image("night")


def get_random_night_image():
    return _get_random_image("night")


def get_kahf_image():
    return _get_random_image("kahf")


def get_jumuah_image():
    return _get_random_image("jumuah")