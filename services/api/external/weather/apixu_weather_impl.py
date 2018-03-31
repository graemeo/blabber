import os

from weather_abstract import WeatherAbstract
from apixu.client import ApixuClient, ApixuException

class ApixuWeatherImpl(WeatherAbstract):

    def get_weather(self):
        client = ApixuClient(os.environ.get("APIXU_API_KEY"))
        current = client.getCurrentWeather(q='Sydney')
        return current.get("current").get("temp_c")
