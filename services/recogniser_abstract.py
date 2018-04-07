from abc import ABCMeta, abstractmethod

class RecogniserAbstract:
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_recognised(self, text):
        return

    @abstractmethod
    def get(self):
        return
