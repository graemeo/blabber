from services.speech_service_impl import SpeechServiceImpl

def main():
   speech_service = SpeechServiceImpl()
   speech_service.invoke()

if __name__ == "__main__":
    main()     
