from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Давай!")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

yes_no_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Создать новую\nзапись📝"),
            # KeyboardButton(text="Созданные записи📚")
        ],
        [
            KeyboardButton(text="Настройки⚙"),
            KeyboardButton(text="Оставить отзыв✏")
        ]
    ],
    resize_keyboard=True
)

cancel_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отмена❌")]
    ],
    resize_keyboard=True
)
