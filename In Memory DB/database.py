from transactions_command import *
from memento import Memento, MementoCareTaker
from cursor_observable import Cursor
from observer import ObserverA


class Database:
    def __init__(self):
        self.db_dict = None
        self._state = ""
        self.commands_file = r"commands.txt"
        self.db_snap_file = r"db_snapshot.txt"

    def put(self, key, value):
        self.set_state(str({'Put': {key: value}}))
        ct = MementoCareTaker(DB)
        ct.create_and_store_memento(self.commands_file)

        if self.db_dict is not None and value is not None:
            self.db_dict[str(key)] = value
        elif value is None:
            raise Exception("Value cannot be null")
        else:
            self.db_dict = {str(key): value}
        return self.db_dict

    def get_int(self, key):
        try:
            if type(self.db_dict[key]) is int:
                return self.db_dict[key]
            else:
                raise Exception("The item at given key is not of type Int")
        except KeyError:
            return f"Key {key} not in Database"

    def get_string(self, key):
        try:
            if type(self.db_dict[key]) is str:
                return self.db_dict[key]
            else:
                raise Exception("The item at given key is not of type String")
        except KeyError:
            return f"Key {key} not in Database"

    def get_double(self, key):
        try:
            if type(self.db_dict[key]) is float:
                return self.db_dict[key]
            else:
                raise Exception("The item at given index is not of type Double")
        except IndexError:
            return f"Key {key} not in Database"

    def get_array(self, key):
        try:
            if type(self.db_dict[key]) is list:
                return self.db_dict[key]
            elif type(self.db_dict[key]) is Array:
                return self.db_dict[key].array
            else:
                raise Exception("The item at given key is not of type Array")
        except KeyError:
            return f"Key {key} not in Database"

    def get_object(self, key):
        try:
            if type(self.db_dict[key]) is dict:
                return self.db_dict[key]
            elif type(self.db_dict[key]) is Object:
                return self.db_dict[key].obj_dict
            else:
                raise Exception("The item at given key is not of type Object")
        except KeyError:
            raise Exception(f"Key {key} not in Database")

    def get(self, key):
        try:
            return self.db_dict[key]
        except KeyError:
            return f"Key {key} not in Database"

    def remove(self, key):
        self.set_state(str({'Remove': {key: self.db_dict[key]}}))
        ct = MementoCareTaker(DB)
        ct.create_and_store_memento(self.commands_file)
        if key not in self.db_dict:
            return None
        else:
            deleted_value = self.db_dict[key]
            del self.db_dict[key]
            return deleted_value

    @staticmethod
    def transaction():
        return Transactions(DB)

    def set_state(self, state):
        self._state = state

    def save_to_memento(self):
        return Memento(self._state)

    def recover(self, cmds_file=r"commands.txt", db_snap_file=r"db_snapshot.txt"):
        with open(db_snap_file, 'r') as file:
            db_prev_state = file.read()
        self.db_dict = eval(db_prev_state)

        with open(cmds_file, 'r') as file:
            commands = file.readlines()
        for command in commands:
            for key, value in eval(command).items():
                if key.lower() == 'put':
                    k = list(value.keys())[0]
                    v = list(value.values())[0]
                    self.db_dict[str(k)] = v
                elif key.lower() == 'remove':
                    k = list(value.keys())[0]
                    del self.db_dict[str(k)]

    def snapshot(self, cmds_file=r"commands.txt", db_snap_file=r"db_snapshot.txt"):
        self.set_state(str(self.db_dict))
        ct = MementoCareTaker(DB)
        ct.create_and_store_memento(db_snap_file)
        with open(cmds_file, 'w'):
            pass

    def get_cursor(self, key):
        if key not in self.db_dict.keys():
            raise Exception(f"Key {key} not in Database")
        else:
            return Cursor(DB.db_dict, key)









if __name__ == '__main__':
    DB = Database()

    # Creating an array object to be inserted in DB
    arr = Array()
    arr.put(2)
    arr.put({1: 'a'})
    x = arr.from_string('[2, "b"]')
    arr.put(x.array)

    # Creating an Object to be inserted in DB
    obj = Object()
    obj.put('name', 'Roger')
    obj.put('age', '21')

    # Performing insert and remove operations on DB
    DB.put('p', arr.array)
    DB.put('q', 'harika')
    DB.put('r', [7, 4, 9])
    DB.put('s', 4.8)
    DB.put('t', obj.obj_dict)
    DB.put('5', 44)
    DB.remove('s')
    DB.put('s', 6.2)

    print(arr.get_int(0))
    print(arr.remove(1))
    print(DB.get_array('p'))

    # Creating Transactions to perform operations on DB (uses COMMAND PATTERN)
    transaction1 = DB.transaction()
    transaction1.execute(Put(DB, '1', 44))
    transaction1.execute(Put(DB, '2', 3))
    print(transaction1.active)
    transaction1.execute(Put(DB, '3', 55))
    print(DB.db_dict)
    transaction1.commit()
    print(transaction1.active)
    print(DB.db_dict)


    DB.recover()
    print(DB.db_dict)

    # Creating snapshots of DB (uses MEMENTO PATTERN)
    DB.snapshot()

    # Creating Cursor and adding observers (uses OBSERVER PATTERN)
    cursor = DB.get_cursor('5')
    val = cursor.getx(int)
    cursor.add_observer(ObserverA)
    cursor.notify(val)
    DB.put('5', 30)
    val = cursor.getx(int)
    cursor.notify(val)

    print(DB.db_dict)
