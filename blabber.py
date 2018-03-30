from snowboy import snowboydecoder
import signal
import subprocess

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def record_callback():
    snowboydecoder.play_audio_file()
    print "Recording..."

    command = "rec -r 16000 -b 16 resources/capture.raw silence 1 0.1 3% 1 3.0 3%"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)


def hotword_detector():
    model = "resources/Hi_Sally.pmdl"
    
    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)

    print "Listening..."
    detector.start(detected_callback=record_callback,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)
    
    detector.terminate()

def main():
    signal.signal(signal.SIGINT, signal_handler)
    hotword_detector()

if __name__ == "__main__":
    main()     
