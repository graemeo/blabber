from hotword_abstract import HotwordAbstract

from snowboy import snowboydecoder

class SnowboyHotwordImpl(HotwordAbstract):

    def detect_me(self, detect_callback, interrupt_callback):
        model = "resources/Hi_Sally.pmdl"
    
        detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)

        print "Listening..."
        detector.start(detected_callback=detect_callback,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)

        detector.terminate()

    def detect(self, detect_callback, interrupt_callback):
        return self.detect_me(detect_callback, interrupt_callback)
