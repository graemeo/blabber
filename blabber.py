from snowboy import snowboydecoder
import signal
import subprocess
import io
import time
import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

from threading import Thread
from apixu.client import ApixuClient, ApixuException

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

    text_to_speech("'The weather now in Sydney, is {} degrees celcius'".format(get_weather()))

def record():
    snowboydecoder.play_audio_file()
    print "Recording..."

    command = "rec -r 16000 -b 16 resources/capture.raw silence 1 0.1 3% 1 3.0 3%"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).wait()

def text_to_speech(message):
    print message
    command = "espeak -s130 -ven-us+f5 " + message
    subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).wait()

def speech_to_text():
    client = speech.SpeechClient()
    file_name = "/Users/graemeong/Documents/projects/blabber/resources/capture.raw"
    
    with io.open(file_name, 'rb') as audio_file:
         content = audio_file.read()
         audio = types.RecognitionAudio(content=content)
    
    config = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16, sample_rate_hertz=16000, language_code='en-US')
    
    response = client.recognize(config, audio)
    
    for result in response.results:
         print('Transcript: {}'.format(result.alternatives[0].transcript))
    

def get_weather():
    client = ApixuClient(os.environ.get("APIXU_API_KEY"))
    current = client.getCurrentWeather(q='Sydney')
    return current.get("current").get("temp_c")

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
