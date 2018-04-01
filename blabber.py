from snowboy import snowboydecoder
import signal
import subprocess
import io
import time
import os

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def record_callback():
    sally_acknowledge()

def hotword_detector():
    model = "resources/Hi_Sally.pmdl"
    
    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)

    print "Listening..."
    detector.start(detected_callback=record_callback,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)

    detector.terminate()

def sally_acknowledge():
    text_to_speech("'Whats up'")

def main():
    signal.signal(signal.SIGINT, signal_handler)
    hotword_detector()

if __name__ == "__main__":
    main()     
