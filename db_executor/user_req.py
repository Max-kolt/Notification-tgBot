import time
from loader import sql, connect


# GET __________
def get_user_info(user_id: int) -> tuple:
    select = sql.execute(f'''SELECT Name, City, 
    Weather_notify, Time_weather_notify, Analytics FROM User
    WHERE ID = {user_id}; ''')
    return select.fetchone()


def get_all_weather_notify_users() -> list:
    select = sql.execute('''SELECT ID FROM User
    WHERE Weather_notify = 1;''')
    return select.fetchall()


# VERIFY __________
def verify_user(user_id: int) -> bool:
    select = sql.execute(f'''SELECT * FROM User
    WHERE ID = {user_id}; ''')
    return select.fetchone() is not None


def verify_time_wn(user_id: int) -> bool:
    select = sql.execute(f'''SELECT Time_weather_notify FROM User
    WHERE ID = {user_id};''')
    return select.fetchone() is not None


def verify_weather_notify(user_id: int) -> bool:
    select = sql.execute(f'''SELECT Weather_notify FROM User
    WHERE ID = {user_id};''')
    return select.fetchone()[0] == 1


def verify_analytics(user_id: int) -> bool:
    select = sql.execute(f'''SELECT Analytics FROM User
    WHERE ID = {user_id};''')
    return select.fetchone()[0] == 1


# DELETE __________
def delete_user(user_id: int) -> bool:
    sql.execute(f'''DELETE FROM User
    WHERE ID = {user_id};''')
    connect.commit()
    return True


# UPDATE __________
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


# INSERT __________
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
