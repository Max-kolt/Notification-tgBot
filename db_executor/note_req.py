import time
from loader import sql, connect


# GET __________
def get_last_user_note(user_id: int) -> tuple:
    select = sql.execute(f'''SELECT ID, Description, Creation_date, Reminder_date, Reminder_time FROM Notes
    WHERE User = {user_id}''')
    return select.fetchall()[-1]


def get_all_unperformed_notes() -> list:
    select = sql.execute(f'''SELECT ID, Description, Creation_date, Reminder_date, Reminder_time FROM Notes
    WHERE Performed = 0;''')
    return select.fetchall()


def get_user_by_noteid(note_id: int) -> int:
    select = sql.execute(f'''SELECT User FROM Notes
    WHERE ID = {note_id};''')
    return select.fetchone()[0]


def get_user_notes(user_id: int) -> list:
    select = sql.execute(f'''SELECT ID, Description, Creation_date, Reminder_date, Reminder_time FROM Notes
        WHERE User = {user_id} and Performed = 0;''')
    return select.fetchall()


# VERIFY __________

# DELETE __________
def delete_note(note_id: int) -> bool:
    sql.execute(f'''DELETE FROM Notes
    WHERE ID = {note_id};''')
    connect.commit()
    return True


# UPDATE __________
def update_note_perform(note_id: int):
    try:
        sql.execute(f'''UPDATE Notes
        SET Performed = 1
        WHERE ID = {note_id}''')
        connect.commit()
    except Exception as error:
        print(error, "\nНе удалось изменить perform")
        raise error


# INSERT __________
def add_new_note(user_id: int, description: str, date_nf: str, time_nf: str):
    try:
        sql.execute(f'''INSERT INTO Notes (User, Description, Creation_date, Reminder_date, Reminder_time) 
        VALUES ({user_id}, "{description}", "{time.strftime("%Y-%m-%d")}", "{date_nf}", "{time_nf}");''')
        connect.commit()
    except Exception as error:
        raise error
