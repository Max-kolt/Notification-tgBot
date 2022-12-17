import sqlite3
import time

from config import database
from loader import sql


def select_user(user_id: int):
    select = sql.execute(f'''SELECT * FROM User
                         WHERE ID = {user_id}; 
                         ''')
    return select.fetchone() is not None


def select_user_info(user_id: int):
    select = sql.execute(f'''SELECT * FROM User
                         WHERE ID = {user_id}; 
                         ''')
    return select.fetchone()


def delete_user(user_id: int):
    sql.execute(f'''DELETE FROM User
                WHERE ID = {user_id};
                ''')
    connect.commit()
    return True


def delete_note(note_id: int):
    sql.execute(f'''DELETE FROM Notes
                    WHERE ID = {note_id};
                    ''')
    connect.commit()
    return True


def update(table: str, what_updates: list, where: str):
    pass


def add_new_note():
    pass


def add_new_user(_id: int, name: str, city: str,
                 weather_notify: bool, time_weather_notify: str,
                 analytics: bool):
    try:
        sql.execute(f'''INSERT INTO User (ID, Name, Date_of_starting, City, 
                    Weather_notify, Time_weather_notify, Analytics) VALUES
                    ({_id}, "{name}", "{time.strftime("%Y-%m-%d")}", "{city}",
                    {weather_notify}, "{time_weather_notify}", {analytics});
                    ''')
        connect.commit()
    except Exception as err:
        print(err)
        print("Не удалось добавить нового юзера")


def test_db():
    sql.execute('''insert into User (ID, Name, Date_of_starting, City, 
                    Weather_notify, Time_weather_notify, Analytics)
                VALUES  (3, "Kot", "1999-12-12", "Питер", True, "08:00", True),
                        (4, "Dog", "2023-12-20", "Москва", True, "12:00", False);
                ''')
    connect.commit()
    select_result = select_user(3)
    print(f"select {select_result}")
    print(sql.execute('select * from User').fetchall())
    delete_user(3)
    delete_user(4)


if __name__ == "__main__":

    try:
        connect = sqlite3.connect(f"../{database}")
        sql = connect.cursor()
    except Exception as ex:
        print(ex)
        print("Не получилось подключиться к базе данных")

    # test_db()
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

