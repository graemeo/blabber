from services.weather_recogniser import WeatherRecogniser

import unittest

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
