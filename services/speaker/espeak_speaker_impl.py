import subprocess

from speaker_abstract import SpeakerAbstract

class EspeakSpeakerImpl(SpeakerAbstract):

    def speak(self, message):
        command = "espeak -s130 -ven-us+f5 " + message
        subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).wait()
