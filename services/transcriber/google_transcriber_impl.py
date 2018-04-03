import io

from transcriber_abstract import TranscriberAbstract

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

class GoogleTranscriberImpl(TranscriberAbstract):

    def transcribe(self, source):
        client = speech.SpeechClient()
        file_name = "resources/capture.raw"

        with io.open(file_name, 'rb') as audio_file:
             content = audio_file.read()
             audio = types.RecognitionAudio(content=content)

        config = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16, sample_rate_hertz=16000, language_code='en-US')

        response = client.recognize(config, audio)
        print response

        if response.results:
            return response.results[0].alternatives[0].transcript
        else:
            return None
