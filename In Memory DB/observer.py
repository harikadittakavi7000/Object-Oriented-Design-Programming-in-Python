from abc import ABC, abstractmethod


class IObserver(ABC):

    @abstractmethod
    def notify(self, message):
        pass


class ObserverA(IObserver):

    def __init__(self):
        self.value = None

    def notify(self, value):
        self.value = value
        print("Value is now", value)
        return
