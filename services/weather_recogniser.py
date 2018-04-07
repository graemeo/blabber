from recogniser_abstract import RecogniserAbstract

class WeatherRecogniser(RecogniserAbstract):

    def is_recognised(self, text):
        return "weather" in text.lower()

    def get(self):
        return None
