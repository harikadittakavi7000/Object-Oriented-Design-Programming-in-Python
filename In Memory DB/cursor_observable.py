from transactions_command import *


# OBSERVER PATTERN

class IObservable(ABC):

    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify(self, message):
        pass


class Cursor(IObservable):
    """
    Holds a value in DB.
    Adds and removes observers to observe that value
    """

    def __init__(self, db_object, key):
        self.value = None
        self.db_object = db_object
        self.key = key
        self._observers = set()

    def getx(self, return_type):
        try:
            self.value = self.db_object[self.key]
            if return_type in [int, str, list, dict]:
                return return_type(self.value)
            elif return_type == Array:
                return self.value.array
            elif return_type == Object:
                return return_type(self.value.obj_dict)
        except (TypeError, AttributeError):
            return f"The item at given key is not of type {return_type}"

    def get(self):
        self.value = self.db_object[self.key]
        return self.value

    def add_observer(self, observer):
        self._observers.add(observer)
        return

    def remove_observer(self, observer):
        self._observers.remove(observer)
        return

    def notify(self, value):
        for observer in self._observers:
            observer.notify(self, value)
