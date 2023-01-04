import time
from loader import sql, connect
from aiogram.dispatcher import FSMContext


async def new_feedback(state: FSMContext):
    data = await state.get_data()
    try:
        if verify_user_feedback(data['user_id']):
            await update_feedback(state)
        else:
            await add_feedback(state)
    except Exception as error:
        raise error


# GET __________


# VERIFY __________
def verify_user_feedback(user_id: int) -> bool:
    select = sql.execute(f'''SELECT * FROM Reviews
    WHERE User = {user_id};
    ''')
    return select.fetchone() is not None

# DELETE __________


# UPDATE __________
async def update_feedback(state: FSMContext):
    data = await state.get_data()
    try:
        sql.execute(f'''UPDATE Reviews
        SET Letter = '{data['letter']}', Grade = {data['grade']}, Creation_date = "{time.strftime("%Y-%m-%d")}"
        WHERE User = {data['user_id']};
        ''')
        connect.commit()
    except Exception as error:
        print('Не удалось изменить отзыв\n', error)
        raise error


# INSERT __________
async def add_feedback(state: FSMContext):
    data = await state.get_data()
    try:
        sql.execute(f'''INSERT INTO Reviews VALUES
        ({data['user_id']}, '{data['letter']}', {data['grade']}, "{time.strftime("%Y-%m-%d")}");
        ''')
        connect.commit()
    except Exception as error:
        print('не удалось создать запись об отзыве\n', error)
        raise error
