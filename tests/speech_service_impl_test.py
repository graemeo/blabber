import unittest

from mock import patch
from services.speech_service_impl import SpeechServiceImpl
from services.hotword.snowboy_hotword_impl import SnowboyHotwordImpl
from services.recorder.sox_recorder_impl import SoxRecorderImpl

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
