from character_class import CharacterFlyweightFactory
from font_class import FontFlyweightFactory
from runarray import RunArray
import tracemalloc
from size_of_object import get_size


class FlyweightWordProcessor:
    tracemalloc.start()
    sample_text = """CS 635 Advanced Object-Oriented Design & Programming Fall Semester, 2018 Doc 17 Mediator, 
    Flyweight, Facade, Demeter, Active Object Nov 19, 2019 Copyright ©, All rights reserved. 2019 SDSU & Roger 
    Whitney, 5500 Campanile Drive, San Diego, CA 92182-7700 USA. OpenContent (http://www.opencontent.org/opl.shtml) 
    license defines the copyright on this document."""
    sample_text_chars = list(sample_text)

    char_flyweight_objects = []
    char_factory = CharacterFlyweightFactory()
    for char in sample_text_chars:
        character = char_factory.get_character(str(char))
        if character not in char_flyweight_objects:
            char_flyweight_objects.append(character)

    font_factory = FontFlyweightFactory()
    fontA = font_factory.get_font("TIMES NEW ROMAN", "BOLD", 12)
    fontB = font_factory.get_font("VERDANA", "italic", 10)

    run_array = RunArray()
    run_array.add_run(0, 144, fontA)
    run_array.add_run(144, 68, fontB)
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    wp_flyweights = get_size(char_flyweight_objects) + get_size(font_factory) + get_size(run_array)
    print(f"Peak memory used - {peak_memory} bytes")
    print(f"Memory used by objects using flyweights - {wp_flyweights} bytes")
    tracemalloc.stop()
