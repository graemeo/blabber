from snowboy import snowboydecoder
import signal

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def record_callback():
    snowboydecoder.play_audio_file()
    print "hello"

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
