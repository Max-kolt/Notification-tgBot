from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsNotRegistered
from loader import dp
from keyboards.default import start_menu, main_menu

from random import randint as rd


@dp.message_handler(IsNotRegistered(), commands=["start", "help"], state="*")
async def command_start(message: types.Message, state: FSMContext):
    if state is not None:
        await state.finish()
    await message.answer(f'Привет, {message.from_user.full_name}!👋\n'
                         f'Ты здесь впервые?🧐 Тогда давай познакомимся,\n'
                         f'чтобы мне было легче тебя оповещать информацией!',
                         reply_markup=start_menu)


@dp.message_handler(commands=["start", "help"], state="*")
async def command_help(message: types.Message, state: FSMContext):
    if state is not None:
        await state.finish()
    answer_for_user = f'''Привет! Я Умный Бот! 🤓🤖
По крайней мере так считает мой создатель...😄\n
Изначально я создавался как бот для заметок и оповещения.
В мой функционал входит: ⛅оповещать о прогнозе погоды, ✏запоминать твои записи и 🕓напоминать о них в заданное тобой время. 
Но никто знает, что нового придумает мой создатель. 🥰 '''

    if rd(0, 10) == 5:
        answer_for_user += """\n\n<span class="tg-spoiler">😎Сообщение от создателя: оставляйте отзывы, также 
буду крайне признателен если вы напишете свои предложения
на счет расширении возможностей этого Умного Бота</span>"""

    await message.answer(answer_for_user, reply_markup=main_menu)
