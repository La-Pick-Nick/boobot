import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram import types

from handlers import register_handlers
from callbacks import register_callbacks
from database import create_db_connection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_TOKEN = '7849385666:AAH7g5wfj6IzRCfkj7Cjg7V20b9GVpYwA5o' # Замените на ваш токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def main():
    try:
        await create_db_connection()
        register_handlers(dp)
        register_callbacks(dp)
        await dp.start_polling(bot)
    except Exception as e:
        logger.exception("Ошибка при запуске бота!")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        logger.exception("Ошибка при запуске бота!")
