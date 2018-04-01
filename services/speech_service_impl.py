import signal

from hotword.snowboy_hotword_impl import SnowboyHotwordImpl
from recorder.sox_recorder_impl import SoxRecorderImpl
from transcriber.google_transcriber_impl import GoogleTranscriberImpl
from speaker.espeak_speaker_impl import EspeakSpeakerImpl
from api.external.weather.apixu_weather_impl import ApixuWeatherImpl

class SpeechServiceImpl:

    interrupted = False
    recorder = None
    transcriber = None
    speaker = None
    api_weather = None


    def __init__(self):
        self.recorder = SoxRecorderImpl()
        self.transcriber = GoogleTranscriberImpl()
        self.speaker = EspeakSpeakerImpl()
        self.api_weather = ApixuWeatherImpl()
        
    def invoke(self):
        signal.signal(signal.SIGINT, self.signal_handler)

        hotword_detector = SnowboyHotwordImpl()
        hotword_detector.detect(self.detect_callback, self.interrupt_callback)

    def signal_handler(self, signal, frame):
        self.interrupted = True

    def interrupt_callback(self):
        return self.interrupted

    def detect_callback(self):
        self.speak("'Whats up'")
        self.process()

    def process(self):
        self.record()
        
        #transcript = self.get_transcript()

        #if transcript is None:
            # espeak
        #else:
            # check if matches

    def record(self):
        self.recorder.record()

    def get_transcript(self):
        return self.transcriber.transcribe(None)
   
    def speak(self, message):
        return self.speaker.speak(message) 

    def get_weather(self):
        return self.api_weather.get_weather()
