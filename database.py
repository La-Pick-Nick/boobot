import aiosqlite
import json
import logging

DB_NAME = 'quiz_bot.db'
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def create_db_connection():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS quiz_state (
                user_id INTEGER PRIMARY KEY,
                last_score INTEGER DEFAULT 0,
                answers TEXT DEFAULT '[]'
            )
        ''')
        await db.commit()


async def save_quiz_result(user_id, score, answers):
    async with aiosqlite.connect(DB_NAME) as db:
        try:
            await db.execute(
                'INSERT OR REPLACE INTO quiz_state (user_id, last_score, answers) VALUES (?, ?, ?)',
                (user_id, score, json.dumps(answers, ensure_ascii=False))
            )
            await db.commit()
        except Exception as e:
            logger.error(f"Ошибка при сохранении результата: {e}", exc_info=True)


async def get_quiz_stats(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT last_score, answers FROM quiz_state WHERE user_id = (?)', (user_id,)) as cursor:
            result = await cursor.fetchone()
            if result is not None:
                score, answers_json = result
                answers = json.loads(answers_json)
                return score, answers
            else:
                return None, None
