from abc import ABCMeta, abstractmethod

class SpeakerAbstract:

    @abstractmethod
    def speak(self, message):
        """Implementation to convert text to speech for a given message"""
