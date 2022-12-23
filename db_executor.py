import sqlite3
import time

from config import database
from loader import sql, connect


def select_user(user_id: int) -> bool:
    select = sql.execute(f'''SELECT * FROM User
    WHERE ID = {user_id}; ''')
    return select.fetchone() is not None


def get_user_info(user_id: int) -> tuple:
    select = sql.execute(f'''SELECT Name, City, 
    Weather_notify, Time_weather_notify, Analytics FROM User
    WHERE ID = {user_id}; ''')
    return select.fetchone()


def get_all_weather_notify_users() -> list:
    select = sql.execute('''SELECT ID FROM User
    WHERE Weather_notify = 1;''')
    return select.fetchall()


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


def select_time_wn(user_id: int) -> bool:
    select = sql.execute(f'''SELECT Time_weather_notify FROM User
    WHERE ID = {user_id};''')
    return select.fetchone() is not None


def select_weather_notify(user_id: int) -> bool:
    select = sql.execute(f'''SELECT Weather_notify FROM User
    WHERE ID = {user_id};''')
    return select.fetchone()[0] == 1


def select_analytics(user_id: int) -> bool:
    select = sql.execute(f'''SELECT Analytics FROM User
    WHERE ID = {user_id};''')
    return select.fetchone()[0] == 1


def delete_user(user_id: int) -> bool:
    sql.execute(f'''DELETE FROM User
    WHERE ID = {user_id};''')
    connect.commit()
    return True


def delete_note(note_id: int) -> bool:
    sql.execute(f'''DELETE FROM Notes
    WHERE ID = {note_id};''')
    connect.commit()
    return True


def update_note_perform(note_id: int):
    try:
        sql.execute(f'''UPDATE Notes
        SET Performed = 1
        WHERE ID = {note_id}''')
        connect.commit()
    except Exception as error:
        print(error, "\nНе удалось изменить perform")
        raise error


def update_name(user_id: int, new_name: str):
    try:
        sql.execute(f'''UPDATE User
        SET Name = "{new_name}"
        WHERE ID = {user_id};''')
        connect.commit()
    except Exception as error:
        print(error, "\nНе удалось изменить имя")
        raise error


def update_city(user_id: int, new_city: str):
    try:
        sql.execute(f'''UPDATE User
        SET City = "{new_city}"
        WHERE ID = {user_id};''')
        connect.commit()
    except Exception as error:
        print(error, "\nНе удалось изменить город")
        raise error


def update_weather_notify(user_id: int, notify: bool):
    try:
        sql.execute(f'''UPDATE User
        SET Weather_notify = {notify}
        WHERE ID = {user_id};''')
        connect.commit()
    except Exception as error:
        print(error, "\nНе удалось изменить оповещение погоды")
        raise error


def update_time_weather_notify(user_id: int, new_time: str):
    try:
        sql.execute(f'''UPDATE User
        SET Time_weather_notify = "{new_time}"
        WHERE ID = {user_id};''')
        connect.commit()
    except Exception as error:
        print(error, "\nНе удалось изменить время оповещения")
        raise error


def update_analytics(user_id: int, anality: bool):
    try:
        sql.execute(f'''UPDATE User
        SET Analytics = {anality}
        WHERE ID = {user_id};''')
        connect.commit()
    except Exception as error:
        print(error, "\nНе удалось изменить аналитику")
        raise error


def add_new_note(user_id: int, description: str, date_nf: str, time_nf: str):
    try:
        sql.execute(f'''INSERT INTO Notes (User, Description, Creation_date, Reminder_date, Reminder_time) 
        VALUES ({user_id}, "{description}", "{time.strftime("%Y-%m-%d")}", "{date_nf}", "{time_nf}");''')
        connect.commit()
    except Exception as error:
        raise error


def add_new_user(_id: int, name: str, city: str,
                 weather_notify: bool, time_weather_notify: str,
                 analytics: bool):
    try:
        sql.execute(f'''INSERT INTO User (ID, Name, Date_of_starting, City, 
        Weather_notify, Time_weather_notify, Analytics) VALUES
        ({_id}, "{name}", "{time.strftime("%Y-%m-%d")}", "{city}",
        {weather_notify}, "{time_weather_notify}", {analytics});''')
        connect.commit()
    except Exception as error:
        raise error


if __name__ == "__main__":
    # delete_user(505135286)
    # print(get_user_info(505135286))
    # result = sql.execute('''select * from User;''')
    # print(result.fetchall())
    # print(get_all_weather_notify_users())
    print(get_all_unperformed_notes())
    print(get_user_by_noteid(6))

    '''
    # User table
    sql.execute("CREATE TABLE User (" +
                "ID INTEGER PRIMARY KEY," +
                "Name TEXT NOT NULL," +
                "Date_of_starting DATE NOT NULL," +
                "City TEXT," +
                "Weather_notify BOOLEAN," +
                "Time_weather_notify VARCHAR(5)," +
                "Analytics BOOLEAN" +
                ");")
                
    
    # Notes table
    sql.execute("DROP TABLE Notes;")
    sql.execute("CREATE TABLE Notes(" +
                "ID INTEGER PRIMARY KEY AUTOINCREMENT," +
                "User INTEGER NOT NULL," +
                "Description TEXT NOT NULL," +
                "Creation_date DATE," +
                "Reminder_date DATE," +
                "Reminder_time VARCHAR(5),"+
                "Performed BOOLEAN DEFAULT 0 NOT NULL," +
                "FOREIGN KEY (User) REFERENCES User(ID)" +
                ");")
    print('Таблица Notes создана')
    '''
