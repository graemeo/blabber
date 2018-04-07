from recogniser_abstract import RecogniserAbstract
from api.external.weather.apixu_weather_impl import ApixuWeatherImpl

class WeatherRecogniser(RecogniserAbstract):

    def is_recognised(self, text):
        if text:
            return "weather" in text.lower()
        else:
            return False

    def get(self):
        weather_api = ApixuWeatherImpl()
        temperature = weather_api.get_weather()

        return "The weather in Sydney is {} degrees celsius".format(temperature)
