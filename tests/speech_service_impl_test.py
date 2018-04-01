import unittest

from mock import patch
from services.speech_service_impl import SpeechServiceImpl
from services.hotword.snowboy_hotword_impl import SnowboyHotwordImpl
from services.recorder.sox_recorder_impl import SoxRecorderImpl
from services.transcriber.google_transcriber_impl import GoogleTranscriberImpl
from services.speaker.espeak_speaker_impl import EspeakSpeakerImpl
from services.api.external.weather.apixu_weather_impl import ApixuWeatherImpl

class SpeechServiceImplTest(unittest.TestCase):

    def setUp(self):
        self.speech_service = SpeechServiceImpl()

    @patch.object(SnowboyHotwordImpl, "detect")
    def test_should_invoke_snowboy_hotword_detector_detect_function(self, mock_snowboy_detect):
        # given
        # when
        self.speech_service.invoke()

        # then
        mock_snowboy_detect.assert_called_once()

    @patch.object(SoxRecorderImpl, "record")
    def test_should_invoke_sox_recorder_record_function(self, mock_sox_record):
        # given
        # when
        self.speech_service.record()

        # then
        mock_sox_record.assert_called_once()

    @patch.object(GoogleTranscriberImpl, "transcribe")
    def test_should_invoke_google_transcriber_transcribe_function(self, mock_google_transcribe):
        # given
        # when
        self.speech_service.get_transcript()

        # then
        mock_google_transcribe.assert_called_once()

    @patch.object(EspeakSpeakerImpl, "speak")
    def test_should_invoke_espeak_speaker_speak_function(self, mock_espeak_speak):
        # given
        # when
        self.speech_service.speak("hello")

        # then
        mock_espeak_speak.assert_called_once()

    @patch.object(ApixuWeatherImpl, "get_weather")
    def test_should_invoke_apixu_weather_get_weather_function(self, mock_apixu_get_weather):
        # given
        # when
        self.speech_service.get_weather()

        # then
        mock_apixu_get_weather.assert_called_once()
