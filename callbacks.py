from aiogram import types, Dispatcher
from aiogram import F
import logging

from database import save_quiz_result
from handlers import get_question, user_data
from data import quiz_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def answer_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    try:
        answer_index = int(callback.data)
        current_question_index = user_data[user_id]["current_question"]
        correct_index = quiz_data[current_question_index]["correct_option"]

        answer = quiz_data[current_question_index]["options"][answer_index]
        correct_answer = quiz_data[current_question_index]["options"][correct_index]

        user_data[user_id]["answers"].append(answer)

        await callback.bot.edit_message_reply_markup(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            reply_markup=None
        )

        if answer_index == correct_index:
            await callback.message.answer("Верно!")
            user_data[user_id]["score"] += 1
        else:
            await callback.message.answer(f"Неправильно. Правильный ответ: {correct_answer}")

        user_data[user_id]["current_question"] += 1
        next_question_index = user_data[user_id]["current_question"]

        if next_question_index < len(quiz_data):
            await get_question(callback.message, user_id, next_question_index, user_data[user_id]["answers"])
        else:
            score = user_data[user_id]["score"]
            answers = user_data[user_id]["answers"]
            await save_quiz_result(user_id, score, answers)
            await callback.message.answer(f"Это был последний вопрос. Квиз завершен!\nВаш результат: {score}")

    except Exception as e:
        logger.exception(f"Ошибка в answer_callback! callback.data = {callback.data}")

def register_callbacks(dp: Dispatcher):
    dp.callback_query.register(answer_callback, F.data.isdigit())
