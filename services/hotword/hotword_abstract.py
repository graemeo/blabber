from abc import ABCMeta, abstractmethod

class HotwordAbstract:

    __metaclass__ = ABCMeta

    @abstractmethod
    def detect(self, detect_callback, interrupt_callback):
        """Implementation to detect hotword"""
