# data.py (Файл для хранения данных викторины)
import json

# Указываем путь к файлу с данными викторины
DICT_DATA = 'data/quiz_data.json'

quiz_data = [
    {
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
    {
        'question': 'Какой оператор используется для проверки равенства двух значений в Python?',
        'options': ['=', '==', 'is', 'equals'],
        'correct_option': 1
    },
    {
        'question': 'Какая функция используется для получения ввода от пользователя?',
        'options': ['print', 'input', 'get', 'read'],
        'correct_option': 1
    },
    {
        'question': 'Как создать список в Python?',
        'options': ['()', '{}', '<>', '[]'],
        'correct_option': 3
    },
    {
        'question': 'Какой метод используется для добавления элемента в конец списка?',
        'options': ['insert', 'add', 'append', 'extend'],
        'correct_option': 2
    },
    {
        'question': ' Что такое "list comprehension" в Python?',
        'options': ['Функция для создания списка на основе другого списка или итерируемого объекта.', 'Способ импорта модулей в Python.', 'Оператор для работы со строками.', 'Метод создания класса в Python.'],
        'correct_option': 0
    },
    {
        'question': 'Что означает аббревиатура PEP в контексте Python?',
        'options': ['Python Execution Process', 'Python Enhancement Proposal', 'Python Error Prevention', 'Python Extension Package'],
        'correct_option': 1
    },
    {
        'question': ' Какая структура данных в Python является неизменяемой (immutable)?',
        'options': ['list', 'dict', 'tuple', 'set'],
        'correct_option': 2
    },
    {
        'question': 'Какой способ является лучшим для обработки исключений в Python?',
        'options': [' Игнорировать ошибки', 'Использовать оператор if для проверки на возможные ошибки', 'Использовать конструкцию try...except', 'Завершать программу при возникновении исключения'],
        'correct_option': 2
    },
]

# Записываем данные quiz_data в JSON-файл
with open(DICT_DATA, 'w') as file:
    json.dump(quiz_data, file, indent=4, ensure_ascii=False)
