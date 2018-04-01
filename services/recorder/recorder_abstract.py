from abc import ABCMeta, abstractmethod

class RecorderAbstract:

    __metaclass__ = ABCMeta

    @abstractmethod
    def record(self):
        """Implementation for recording sound"""
