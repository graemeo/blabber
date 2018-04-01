from snowboy import snowboydecoder
import signal
import subprocess
import io
import time
import os

from threading import Thread

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def record_callback():

    sally_acknowledge()
    record_thread = Thread(target=record())
    record_thread.start()
    record_thread.join()

    #stt_thread = Thread(target=speech_to_text())
    #stt_thread.start()
    #stt_thread.join()

def record():
    snowboydecoder.play_audio_file()
    print "Recording..."

    command = "rec -r 16000 -b 16 resources/capture.raw silence 1 0.1 3% 1 3.0 3%"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).wait()

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
