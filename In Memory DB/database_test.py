from database import *
import unittest
import os


# UNIT TESTS

class TestDBFunctions(unittest.TestCase):
    def test_db_put(self):
        answer = DB.put('key1', 'value1')
        self.assertEqual(answer, {'p': [2, {1: 'a'}, ['2', ' "b"']],
                                  'q': 'harika', 'r': [7, 4, 9], 's': 6.2,
                                  't': {'name': 'Roger', 'age': '21'},
                                  '5': 30, '1': 44, '2': 3, '3': 55, 'key1': 'value1'})

    def test_db_remove(self):
        answer = DB.remove('2')
        self.assertEqual(answer, 3)

    def test_db_get_int(self):
        answer = DB.get_int('5')
        self.assertEqual(answer, 30)


class TestFunctionArrayGetInt(unittest.TestCase):
    def test_get_int_arr(self):
        answer = arr.get_int(0)
        self.assertEqual(answer, 2)


class TestFunctionTransactionGet(unittest.TestCase):
    def test_transaction_get(self):
        answer = transaction1.getx('3', int)
        self.assertEqual(answer, 55)


class TestCursorFunctions(unittest.TestCase):
    def test_cursor_add_observer(self):
        cursor.add_observer(ObserverA)
        answer = cursor._observers
        self.assertEqual(answer, {ObserverA})

    def test_cursor_get(self):
        answer = cursor.getx(int)
        self.assertEqual(answer, 30)


class TestSnapshotFunction(unittest.TestCase):
    def test_snapshot_created(self):
        DB.snapshot()
        answer = os.path.exists(DB.db_snap_file)
        self.assertEqual(answer, True)
