class Character:

    def __init__(self, char):
        self.unicode = ord(char)

    def get_char(self):
        return chr(self.unicode)

    def get_unicode(self):
        return self.unicode


class CharacterFlyweightFactory:

    _instance = None

    def __init__(self):
        self.character_array = []

    def __new__(cls):
        """Ensuring single point of access for the factory by using a Singleton"""
        if cls._instance is None:
            cls._instance = super(CharacterFlyweightFactory, cls).__new__(cls)
        return cls._instance

    def get_character(self, current_char):
        """
        :param current_char: character string
        :return: character object with a unicode value
        """
        for character in self.character_array:
            if character.get_char() == current_char:
                return character
        character = Character(current_char)
        self.character_array.append(character)
        return character
