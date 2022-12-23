from db_executor import get_all_weather_notify_users, get_user_info
from handlers.apsched import weather_notification
from loader import scheduler


async def set_users_schedulers(dp):
    users = get_all_weather_notify_users()
    for _id in users:
        user = get_user_info(_id[0])
        scheduler.add_job(weather_notification,
                          trigger='cron',
                          hour=int(user[3][:2]),
                          minute=int(user[3][3:]),
                          args=(dp, _id[0]),
                          id=str(_id[0]))


