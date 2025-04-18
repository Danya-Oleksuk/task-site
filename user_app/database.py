import os

import asyncpg
from dotenv import load_dotenv

load_dotenv()
DB_CONFIG = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "host": os.getenv("DB_HOST"),
}

async def is_user_in_database(telegram_id: int):
    conn = await asyncpg.connect(**DB_CONFIG)
    user_exists = await conn.fetchval('SELECT 1 FROM users WHERE telegram_id = $1', telegram_id)
    return bool(user_exists)

async def get_user_profile(user_id: int):
    conn = await asyncpg.connect(**DB_CONFIG)
    result = await conn.fetchrow('SELECT telegram_id, unique_key FROM users WHERE telegram_id = $1', user_id)
    return result