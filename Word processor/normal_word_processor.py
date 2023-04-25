import tracemalloc
from font_class import Font
from size_of_object import get_size


class CharWithFont:

    def __init__(self, char, font):
        self.unicode = ord(char)
        self.font = font

    def get_char(self):
        return self.unicode

    def get_font(self):
        return self.font


class NormalWordProcessor:
    tracemalloc.start()
    sample_text = """CS 635 Advanced Object-Oriented Design & Programming Fall Semester, 2018 Doc 17 Mediator, 
    Flyweight, Facade, Demeter, Active Object Nov 19, 2019 Copyright ©, All rights reserved. 2019 SDSU & Roger 
    Whitney, 5500 Campanile Drive, San Diego, CA 92182-7700 USA. OpenContent (http://www.opencontent.org/opl.shtml) 
    license defines the copyright on this document."""
    chars = list(sample_text)

    char_objects_without_flyweight = []
    for char in chars:
        fontC = Font("Arial", "BOLD", 14)
        char_with_font = CharWithFont(char, fontC)
        char_objects_without_flyweight.append(char_with_font)

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    wp_without_flyweights = get_size(char_objects_without_flyweight)
    print(f"Peak memory used - {peak_memory} bytes")
    print(f"Memory used by objects without flyweights - {wp_without_flyweights} bytes")
    tracemalloc.stop()
