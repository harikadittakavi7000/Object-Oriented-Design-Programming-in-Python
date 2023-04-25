from array_class import Array
from object_class import Object
from abc import ABC, abstractmethod


# COMMAND PATTERN

class BaseClass(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Put command class
class Put:

    def __init__(self, db_object, key, value):
        self.value = value
        self.db_object = db_object
        self.key = key

    @property
    def transaction_details(self) -> str:
        return f"Insert value {self.value} at key {self.key} from Database"

    def execute(self):
        self.db_object.put(self.key, self.value)

    def undo(self):
        self.db_object.remove(self.key)


# Remove command class
class Remove:

    def __init__(self, db_object, key):
        self.value = None
        self.db_object = db_object
        self.key = key

    @property
    def transaction_details(self) -> str:
        return f"Delete item at key {self.key} from Database"

    def execute(self):
        self.value = self.db_object.remove(self.key)
        return self.value

    def undo(self):
        self.db_object.put(self.key, self.value)


class Transactions:

    def __init__(self, db_object):
        self.db_obj = db_object
        self.undo_stack = []
        self.active = True

    def execute(self, transaction):
        val = transaction.execute()
        self.undo_stack.append(transaction)
        return val

    def getx(self, key, return_type):
        if key in self.db_obj.db_dict.keys():
            try:
                if return_type in [int, str, list, dict]:
                    return return_type(self.db_obj.db_dict[key])
                elif return_type == Array:
                    return self.db_obj.db_dict[key].array
                elif return_type == Object:
                    return return_type(self.db_obj.db_dict[key].obj_dict)
            except (TypeError, AttributeError):
                return f"The item at given key is not of type {return_type}"
        else:
            raise Exception("No value can be found at " + key)

    def get(self, key):
        try:
            return self.db_obj.db_dict[key]
        except KeyError:
            return f"Key {key} not in Database"

    def commit(self):
        self.undo_stack = []
        self.active = False

    # Undo all operations performed in current transaction and remove them from commands.txt
    def abort(self):
        for transaction in self.undo_stack:
            transaction.undo()
            with open(self.db_obj.commands_file, 'a+') as file:
                lines = file.readlines()
                file.writelines(lines[:-1])
        self.active = False

    def is_active(self):
        return self.active
