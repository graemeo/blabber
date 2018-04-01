import signal

from hotword.snowboy_hotword_impl import SnowboyHotwordImpl
from recorder.sox_recorder_impl import SoxRecorderImpl

class SpeechServiceImpl:

    interrupted = False

    def invoke(self):
        signal.signal(signal.SIGINT, self.signal_handler)

        hotword_detector = SnowboyHotwordImpl()
        hotword_detector.detect(self.detect_callback, self.interrupt_callback)

    def signal_handler(self, signal, frame):
        self.interrupted = True

    def detect_callback(self):
        self.record()

    def interrupt_callback(self):
        return self.interrupted

    def record(self):
        recorder = SoxRecorderImpl()
        recorder.record()

    
