import os


# MEMENTO PATTERN

class Memento(object):
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state


class MementoCareTaker:
    """
    Updates commands.txt file with all operations performed on DB
    and takes snapshots based on predefined condition
    """

    def __init__(self, db_originator):
        self._db_originator = db_originator

    def create_and_store_memento(self, file):
        memento = self._db_originator.save_to_memento()
        # if os.path.getsize(commands_file)/1048576 < 10:
        if file == self._db_originator.commands_file and os.path.getsize(file) < 100:
            with open(file, 'a') as file:
                file.writelines(memento.get_saved_state() + '\n')
        elif file == self._db_originator.db_snap_file:
            with open(file, 'w') as file:
                file.writelines(memento.get_saved_state())
        else:
            with open(self._db_originator.commands_file, 'w') as file:
                file.writelines(memento.get_saved_state() + '\n')
            self._db_originator.snapshot()
