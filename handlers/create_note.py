from handlers.apsched import note_notification
from loader import dp, scheduler
from filters import IsRegistered
from aiogram import types
from states import add_notes
from aiogram.dispatcher import FSMContext
from keyboards.default import cancel_menu, main_menu
from db_executor import add_new_note, get_last_user_note
from datetime import datetime


@dp.message_handler(IsRegistered(), state=add_notes.states, text="Отмена❌")
async def cancel_note(message: types.Message, state: FSMContext):
    await state.reset_data()
    await state.finish()
    await message.answer('Запись прекращена', reply_markup=main_menu)


@dp.message_handler(IsRegistered(), commands=['create_note'])
@dp.message_handler(IsRegistered(), text='Создать новую\nзапись📝')
async def description_question(message: types.Message):
    await message.answer("Что ты хочешь записать?", reply_markup=cancel_menu)
    await add_notes.description.set()


@dp.message_handler(IsRegistered(), state=add_notes.description)
async def date_notify(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data(description=description)
    await message.answer("В какой день тебя оповестить?\nПиши в формате: dd-mm-yy")
    await add_notes.date_notify.set()


@dp.message_handler(IsRegistered(), state=add_notes.date_notify,
                    regexp=r"(?<!\d)(?:0?[1-9]|[12][0-9]|3[01])-(?:0?[1-9]|1[0-2])-(?:[0-2][0-9])(?!\d)")
async def time_notify(message: types.Message, state: FSMContext):
    date = message.text
    await state.update_data(date=date)
    await message.answer("В какое время тебя оповестить?\nПиши в формате: hh:mm")
    await add_notes.time_notify.set()


@dp.message_handler(IsRegistered(), state=add_notes.time_notify, regexp=r"\d\d[-:]\d\d")
async def last_state(message: types.Message, state: FSMContext):
    time = message.text
    user_id = message.from_user.id
    await state.update_data(time=time)
    data = await state.get_data()
    await state.finish()
    try:
        new_note = add_new_note(user_id=user_id,
                                description=data.get('description'),
                                date_nf=data.get('date'),
                                time_nf=data.get('time'))
    except Exception as error:
        print(error, "\n не удалось создать запись")
        await message.answer("Что-то пошло не так... Попробуйте еще раз")
        return

    note = get_last_user_note(user_id)
    scheduler.add_job(note_notification,
                      trigger='date',
                      run_date=datetime.strptime(f'{note[3]} {note[4]}', "%d-%m-%y %H:%M"),
                      args=(dp, user_id, note),
                      id=str(note[0]))

    await message.answer(f"✅Создана запись:\n\n<b>{data['description']}</b>\n"
                         f"(Оповещение {data['time']} 20{data['date']})")
