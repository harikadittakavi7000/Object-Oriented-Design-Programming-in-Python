import unittest
from flyweight_word_processor import FlyweightWordProcessor


# UNIT TESTS

class TestCharacterFlyweight(unittest.TestCase):
    def test_get_char_unicode(self):
        char_fact = FlyweightWordProcessor.char_factory
        unicode = char_fact.get_character('A').unicode
        answer = 65
        self.assertEqual(answer, unicode)


class TestFontFlyweight(unittest.TestCase):
    def test_get_font_name(self):
        font_fact = FlyweightWordProcessor.font_factory
        font_name = font_fact.get_font("TIMES NEW ROMAN", "BOLD", 12).font_name
        answer = 'TIMES NEW ROMAN'
        self.assertEqual(answer, font_name)


class TestRunArray(unittest.TestCase):
    def test_run_array_get_font(self):
        answer = 'TIMES NEW ROMAN'
        font = FlyweightWordProcessor.run_array.get_font_at_index(3)
        self.assertEqual(answer, font.get_name())
