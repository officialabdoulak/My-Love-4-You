import os
import random

ASSETS_DIR = "assets"


def _random_from_folder(folder):
    folder_path = os.path.join(ASSETS_DIR, folder)

    if not os.path.exists(folder_path):
        return None

    images = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
    ]

    if not images:
        return None

    return random.choice(images)


def _find_file(folder, names):
    folder_path = os.path.join(ASSETS_DIR, folder)

    if not os.path.exists(folder_path):
        return None

    for name in names:
        for ext in [".jpg", ".jpeg", ".png", ".webp"]:
            path = os.path.join(folder_path, f"{name}{ext}")
            if os.path.exists(path):
                return path

    return None


def get_morning_image():
    return _random_from_folder("morning")


def get_random_morning_image():
    return _random_from_folder("morning")


def get_night_image():
    return _random_from_folder("night")


def get_random_night_image():
    return _random_from_folder("night")


def get_kahf_image():
    return _find_file("friday", ["kahf", "al_kahf"])


def get_jumuah_image():
    return _find_file("friday", ["jumuah", "jummah", "jumaah"])