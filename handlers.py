from aiogram import types, Dispatcher
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import F
import logging

from database import save_quiz_result, get_quiz_stats
from data import quiz_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user_data = {}

def generate_options_keyboard(answer_options, correct_index):
    builder = InlineKeyboardBuilder()
    for i, option in enumerate(answer_options):
        builder.add(types.InlineKeyboardButton(
            text=option,
            callback_data=str(i)
        ))
    builder.adjust(1)
    return builder.as_markup()

async def get_question(message: types.Message, user_id: int, question_index: int, user_answers: list = None):
    if question_index >= len(quiz_data):
        logger.warning(f"Попытка получить вопрос с индексом {question_index}, но всего вопросов {len(quiz_data)}")
        return

    question = quiz_data[question_index]
    correct_index = question['correct_option']
    options = question['options']
    keyboard = generate_options_keyboard(options, correct_index)
    question_text = f"{question['question']}"
    if user_answers:
        question_text += f"\n\nВаши ответы: {', '.join(user_answers)}"
    await message.answer(question_text, reply_markup=keyboard)


async def new_quiz(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {"answers": [], "score": 0, "current_question": 0}
    await get_question(message, user_id, 0)


async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Начать игру"))
    await message.answer("Добро пожаловать в квиз!", reply_markup=builder.as_markup(resize_keyboard=True))


async def cmd_stats(message: types.Message):
    user_id = message.from_user.id
    score, answers = await get_quiz_stats(user_id)

    if score is not None:
        answers_str = [str(answer) for answer in answers]
        await message.answer(f"Ваш последний результат: {score}\nВаши ответы: {', '.join(answers_str)}")
    else:
        await message.answer("Вы еще не проходили квиз.")

def register_handlers(dp: Dispatcher):
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(new_quiz, F.text.lower() == "начать игру")
    dp.message.register(cmd_stats, Command("stats"))
