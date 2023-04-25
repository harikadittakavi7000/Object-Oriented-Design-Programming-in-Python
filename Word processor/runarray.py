class RunArray(object):
    
    def __init__(self):
        self.run_list = []
        self.index = 0

    def add_run(self, start_index, length, font):
        index_array = [0]*3
        index_array[0] = start_index
        index_array[1] = start_index + length
        index_array[2] = font
        self.run_list.append(index_array)
        self.index += length

    def append_run(self, length, font):
        index_array = [0]*3
        index_array[0] = self.index
        index_array[1] = self.index + length
        index_array[2] = font
        self.run_list.append(index_array)
        self.index += length

    def get_font_at_index(self, index):
        for entry in self.run_list:
            if entry[0] <= index <= entry[1]:
                return entry[2]
        return None
