import unittest

from mock import patch
from services.speech_service_impl import SpeechServiceImpl
from services.hotword.snowboy_hotword_impl import SnowboyHotwordImpl

class SpeechServiceImplTest(unittest.TestCase):

    @patch.object(SnowboyHotwordImpl, "detect")
    def test_should_invoke_hotword_detector(self, mock_snowboy_hotword_impl):
        # given
        speech = SpeechServiceImpl()

        # when
        speech.invoke()

        # then
        mock_snowboy_hotword_impl.assert_called_once()
