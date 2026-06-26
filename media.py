import os
from journey import get_current_day

# ==========================
# ASSETS PATHS
# ==========================

BASE_FOLDER = "assets"

MORNING_FOLDER = os.path.join(BASE_FOLDER, "morning")
NIGHT_FOLDER = os.path.join(BASE_FOLDER, "night")
FRIDAY_FOLDER = os.path.join(BASE_FOLDER, "friday")
LOVE_FOLDER = os.path.join(BASE_FOLDER, "love")


# ==========================
# MORNING IMAGE
# ==========================

def get_morning_image():

    day = get_current_day()

    image_number = ((day - 1) % 14) + 1

    for ext in [".jpg", ".jpeg", ".png", ".webp"]:
        image = os.path.join(MORNING_FOLDER, f"{image_number}{ext}")

        if os.path.exists(image):
            return image

    return None


# ==========================
# NIGHT IMAGE
# ==========================

def get_night_image():

    for ext in [".jpg", ".jpeg", ".png", ".webp"]:
        image = os.path.join(NIGHT_FOLDER, f"gn{ext}")

        if os.path.exists(image):
            return image

    return None


# ==========================
# FRIDAY IMAGES
# ==========================

def get_kahf_image():

    for ext in [".jpg", ".jpeg", ".png", ".webp"]:
        image = os.path.join(FRIDAY_FOLDER, f"kahf{ext}")

        if os.path.exists(image):
            return image

    return None


def get_jumuah_image():

    for ext in [".jpg", ".jpeg", ".png", ".webp"]:
        image = os.path.join(FRIDAY_FOLDER, f"jumuah{ext}")

        if os.path.exists(image):
            return image

    return None


# ==========================
# LOVE IMAGE
# ==========================

def get_love_image():

    images = []

    for file in os.listdir(LOVE_FOLDER):

        if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            images.append(os.path.join(LOVE_FOLDER, file))

    if images:
        return images[0]

    return None