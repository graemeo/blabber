from abc import ABCMeta, abstractmethod

class TranscriberAbstract:
    __metaclass__ = ABCMeta

    @abstractmethod
    def transcribe(self, source):
        """ Implementation to convert speech to text"""
        return
