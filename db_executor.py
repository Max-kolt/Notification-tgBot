import sqlite3
import time

from config import database
from loader import sql, connect


def select_user(user_id: int):
    select = sql.execute(f'''SELECT * FROM User
    WHERE ID = {user_id}; ''')
    return select.fetchone() is not None


def select_user_info(user_id: int):
    select = sql.execute(f'''SELECT Name, City, 
    Weather_notify, Time_weather_notify, Analytics FROM User
    WHERE ID = {user_id}; ''')
    return select.fetchone()


def delete_user(user_id: int):
    sql.execute(f'''DELETE FROM User
    WHERE ID = {user_id};''')
    connect.commit()
    return True


def delete_note(note_id: int):
    sql.execute(f'''DELETE FROM Notes
    WHERE ID = {note_id};''')
    connect.commit()
    return True


def update_name(user_id: int, new_name: str):
    sql.execute(f'''UPDATE User
    SET Name = "{new_name}"
    WHERE ID = {user_id};''')
    connect.commit()


def update_city(user_id: int, new_city: str):
    sql.execute(f'''UPDATE User
    SET City = {new_city}
    WHERE ID = {user_id};''')
    connect.commit()


def update_weather_notify(user_id: int, notify: bool):
    sql.execute(f'''UPDATE User
    SET Weather_notify = {notify}
    WHERE ID = {user_id};''')
    connect.commit()


def update_time_weather_notify(user_id: int, new_time: str):
    sql.execute(f'''UPDATE User
    SET Time_weather_notify = "{new_time}"
    WHERE ID = {user_id};''')
    connect.commit()


def update_analytics(user_id: int, anality: bool):
    sql.execute(f'''UPDATE User
    SET Analytics = {anality}
    WHERE ID = {user_id};''')
    connect.commit()


def add_new_note():
    pass


def add_new_user(_id: int, name: str, city: str,
                 weather_notify: bool, time_weather_notify: str,
                 analytics: bool):
    try:
        sql.execute(f'''INSERT INTO User (ID, Name, Date_of_starting, City, 
        Weather_notify, Time_weather_notify, Analytics) VALUES
        ({_id}, "{name}", "{time.strftime("%Y-%m-%d")}", "{city}",
        {weather_notify}, "{time_weather_notify}", {analytics});''')
        connect.commit()
    except Exception as err:
        print(err)
        print("Не удалось добавить нового юзера")
        return


if __name__ == "__main__":

    # delete_user(505135286)
    result = sql.execute('''select * from User;''')

    print(result.fetchall())

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
    sql.execute("CREATE TABLE Notes(" +
                "ID INTEGER PRIMARY KEY AUTOINCREMENT," +
                "User INTEGER NOT NULL," +
                "Description TEXT NOT NULL," +
                "Creation_date DATE," +
                "Reminder_datetime DATETIME,"
                "Performed BOOLEAN NOT NULL DEFAULT 0 NOT NULL," +
                "FOREIGN KEY (User) REFERENCES User(ID)" +
                ");")
    '''
