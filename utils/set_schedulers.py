from db_executor import get_all_weather_notify_users, get_user_info, get_all_unperformed_notes, get_user_by_noteid
from handlers.apsched import weather_notification, note_notification
from loader import scheduler
from datetime import datetime


async def set_weather_schedulers(dp):
    users = get_all_weather_notify_users()
    for _id in users:
        user = get_user_info(_id[0])
        scheduler.add_job(weather_notification,
                          trigger='cron',
                          hour=int(user[3][:2]),
                          minute=int(user[3][3:]),
                          args=(dp, _id[0]),
                          id=str(_id[0]))


async def set_note_schedulers(dp):
    notes = get_all_unperformed_notes()
    for note in notes:
        scheduler.add_job(note_notification,
                          trigger='date',
                          run_date=datetime.strptime(f'{note[3]} {note[4]}', "%d-%m-%y %H:%M"),
                          args=(dp, get_user_by_noteid(note[0]), note),
                          id=str(note[0]))
