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

API_TOKEN = '' 

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
