class Font:

    def __init__(self, font_name, point_size, style):
        self.font_name = font_name
        self.point_size = point_size
        self.style = style

    def get_name(self):
        return self.font_name

    def get_size(self):
        return self.point_size

    def get_style(self):
        return self.style


class FontFlyweightFactory(object):

    _instance = None

    def __init__(self):
        self.font_array = []

    def __new__(cls):
        """Ensuring single point of access for the factory by using a Singleton"""
        if cls._instance is None:
            cls._instance = super(FontFlyweightFactory, cls).__new__(cls)
        return cls._instance

    def get_font(self, name, style, size):
        """
        :param name: font name
        :param style: font style (NORMAL, ITALIC, BOLD)
        :param size: font size
        :return: font object with above properties
        """
        for font in self.font_array:
            if font.get_name() == name and font.get_size() == size and font.get_style() == style:
                return font
        font = Font(name, size, style)
        self.font_array.append(font)
        return font
