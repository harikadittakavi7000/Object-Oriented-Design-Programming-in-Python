from transactions_command import *


class Array:
    def __init__(self, array=None):
        self.array = array

    def put(self, value):
        if self.array is not None and value is not None:
            self.array.append(value)
        elif value is None:
            raise Exception("Value cannot be null")
        else:
            self.array = [value]
        return self.array

    def get_int(self, index):
        try:
            if type(self.array[index]) is int:
                return self.array[index]
            else:
                raise Exception("The item at given index is not of type Int")
        except IndexError:
            print("No value can be found at " + index)

    def get_string(self, index):
        try:
            if type(self.array[index]) is str:
                return self.array[index]
            else:
                raise Exception("The item at given index is not of type String")
        except IndexError:
            print("No value can be found at " + index)

    def get_double(self, index):
        try:
            if type(self.array[index]) is float:
                return self.array[index]
            else:
                raise Exception("The item at given index is not of type Double")
        except IndexError:
            print("No value can be found at " + index)

    def get_array(self, index):
        try:
            if type(self.array[index]) is list:
                return self.array[index]
            elif type(self.array[index]) is Array:
                return self.array[index].array
            else:
                raise Exception("The item at given index is not of type Array")
        except IndexError:
            print("No value can be found at " + index)

    def get_object(self, index):
        try:
            if type(self.array[index]) is dict:
                return self.array[index]
            elif type(self.array[index]) is Object:
                return self.array[index].obj_dict
            else:
                raise Exception("The item at given index is not of type Object")
        except IndexError:
            print("No value can be found at " + index)

    def get(self, index):
        try:
            return self.array[index]
        except KeyError:
            print("No value can be found at " + index)

    def length(self):
        return len(self.array)

    def to_string(self):
        return str(self.array)

    def remove(self, index):
        try:
            deleted_value = self.array[index]
            del self.array[index]
            return deleted_value
        except IndexError:
            raise Exception(f"Index {index} not in array")

    @staticmethod
    def from_string(value):
        if '[' in value or ',' in value:
            a = Array()
            vals = value.strip('[,]').split(',')
            for elem in vals:
                a.put(elem)
            return a
        else:
            raise Exception("The input string does not represent a valid array object")
