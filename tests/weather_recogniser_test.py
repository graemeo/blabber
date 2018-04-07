import unittest

from mock import patch
from services.weather_recogniser import WeatherRecogniser
from services.api.external.weather.apixu_weather_impl import ApixuWeatherImpl

class WeatherRecogniserTest(unittest.TestCase):

    def setUp(self):
        self.weather = WeatherRecogniser()
       
    def test_should_return_false_when_given_text_is_blank(self):
        # given
        text = ""

        # when
        # then
        self.assertFalse(self.weather.is_recognised(text))

    def test_should_return_false_when_given_text_does_not_match(self):
        # given
        text = "tell me what time it is now"

        # when
        # then 
        self.assertFalse(self.weather.is_recognised(text))

    def test_should_return_true_when_given_text_matches(self):
        # given
        text = "tell me what the weather is today"

        # given
        # then
        self.assertTrue(self.weather.is_recognised(text))

    @patch.object(ApixuWeatherImpl, "get_weather")
    def test_should_invoke_apixu_weather_api_get_weather(self, mock_apixu_get_weather):
        # given
        # when
        self.weather.get()

        # then
        mock_apixu_get_weather.assert_called_once()

    @patch.object(ApixuWeatherImpl, "get_weather")
    def test_should_return_weather_text(self, mock_apixu_get_weather):
        # given
        fake_temperature = 10
        actual = "The weather in Sydney is {} degrees celsius".format(fake_temperature)
        mock_apixu_get_weather.return_value = fake_temperature

        # when
        # them
        self.assertEqual(self.weather.get(), actual)
