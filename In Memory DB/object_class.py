from transactions_command import *


class Object:
    def __init__(self, obj_dict=None):
        self.obj_dict = obj_dict

    def put(self, key, value):
        if self.obj_dict is not None and value is not None:
            self.obj_dict[str(key)] = value
        elif value is None:
            raise Exception("Value cannot be null")
        else:
            self.obj_dict = {str(key): value}
        return self.obj_dict

    def get_int(self, key):
        try:
            if type(self.obj_dict[key]) is int:
                return self.obj_dict[key]
            else:
                raise Exception("The item at given key is not of type Int")
        except KeyError:
            print("No value can be found at " + key)

    def get_string(self, key):
        try:
            if type(self.obj_dict[key]) is str:
                return self.obj_dict[key]
            else:
                raise Exception("The item at given key is not of type String")
        except KeyError:
            print("No value can be found at " + key)

    def get_double(self, key):
        try:
            if type(self.obj_dict[key]) is float:
                return self.obj_dict[key]
            else:
                raise Exception("The item at given index is not of type Double")
        except IndexError:
            print("No value can be found at " + key)

    def get_array(self, key):
        try:
            if type(self.obj_dict[key]) is list:
                return self.obj_dict[key]
            elif type(self.obj_dict[key]) is Array:
                return self.obj_dict[key].array
            else:
                raise Exception("The item at given key is not of type Array")
        except KeyError:
            print("No value can be found at " + key)

    def get_object(self, key):
        try:
            if type(self.obj_dict[key]) is dict:
                return self.obj_dict[key]
            elif type(self.obj_dict[key]) is Object:
                return self.obj_dict[key].obj_dict
            else:
                raise Exception("The item at given key is not of type Object")
        except KeyError:
            print("No value can be found at " + key)

    def get(self, key):
        try:
            return self.obj_dict[key]
        except KeyError:
            print("No value can be found at " + key)

    def length(self):
        return len(self.obj_dict)

    def to_string(self):
        return str(self.obj_dict)

    def remove(self, key):
        if key not in self.obj_dict:
            return None
        else:
            deleted_value = self.obj_dict[key]
            del self.obj_dict[key]
            return deleted_value

    @staticmethod
    def from_string(value):
        if '{' in value or ':' in value:
            o = Object()
            for key1, value1 in eval(value).items():
                o.put(key1, value1)
            return o
        else:
            raise Exception("The input string does not represent a valid object")
