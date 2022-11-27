from typing import Dict, Union

from python_weather.enums import WeatherType
from python_weather.forecast import Weather
from translate import Translator
import python_weather
import asyncio
import os


async def get_weather(country: str = "St Petersburg") -> Weather:
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:  # fetch a weather forecast from a city
        weather = await client.get("SPb")
        return weather


async def get_current_forecast(country: str = "St Petersburg") -> Dict[str, Union[str, float, WeatherType]]:
    weather = await get_weather(country)
    current_forecast = {
        "date": weather.current.local_time.strftime("%Y-%m-%d"),
        "temperature_celsius": (weather.current.temperature - 32) * 5 / 9,
        "description": weather.current.description +
                       f" ({Translator(to_lang='Russian').translate(weather.current.description)})",
        "icon": weather.current.type
    }
    return current_forecast


async def get_hourly_forecast(country: str = "St Petersburg") -> Dict[str, Union[str, list]]:
    weather = await get_weather(country)
    forecast_today = next(weather.forecasts)
    hourly_forecast = {
        "date": forecast_today.date.strftime("%Y-%m-%d"),
        "hourly_fc": []
    }

    for hourly_fc in forecast_today.hourly:
        hourly_forecast["hourly_fc"].append([f"{hourly_fc.time.hour} hours",
                                             hourly_fc.temperature,
                                             hourly_fc.type])
    return hourly_forecast


if __name__ == "__main__":
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(get_hourly_forecast())
