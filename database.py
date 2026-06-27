import sqlite3
from datetime import datetime

DB_NAME = "bot_users.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            welcomed INTEGER DEFAULT 0,
            joined_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def register_user(user_id, first_name=""):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO users (user_id, first_name, welcomed, joined_at)
        VALUES (?, ?, 0, ?)
    """, (user_id, first_name, datetime.now().isoformat()))

    conn.commit()
    conn.close()


def has_seen_welcome(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT welcomed FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()

    conn.close()

    return result is not None and result[0] == 1


def mark_welcomed(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET welcomed = 1 WHERE user_id = ?", (user_id,))

    conn.commit()
    conn.close()


def get_all_user_ids():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT user_id FROM users")
    users = [row[0] for row in cursor.fetchall()]

    conn.close()

    return users