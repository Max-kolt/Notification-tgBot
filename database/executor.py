import sqlite3
from config import database

con = sqlite3.connect(database)

crs = con.cursor()


async def select(fiels: list, table: str, where: str):
    pass


async def delete(table: str, where: str):
    pass


async def update(table: str, what_updates: list, where: str):
    pass


async def add_new_note():
    pass


async def add_new_user():
    pass


def test_db():
    pass


if __name__ == "__main__":
    # Notes table
    crs.execute("CREATE TABLE Notes(" +
                "ID INTEGER PRIMARY KEY AUTOINCREMENT," +
                "Description TEXT NOT NULL," +
                "Creation_date DATE," +
                "Reminder_datetime DATETIME" +
                ");")

    # User table
    crs.execute("CREATE TABLE User (" +
                "ID INTEGER PRIMARY KEY AUTOINCREMENT," +
                "Name TEXT NOT NULL," +
                "Date_of_starting DATE NOT NULL," +
                "City TEXT," +
                "Weather_notify BOOLEAN," +
                "Time_weather_notify VARCHAR(5)," +
                "Analytics BOOLEAN," +
                "Notes INTEGER," +
                "FOREIGN KEY (Notes) REFERENCES Notes(ID) ON DELETE CASCADE ON UPDATE NO ACTION" +
                ");")


