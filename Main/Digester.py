from Main.Elements.Property import Property
from Main.Elements.Source import Source

__author__ = 'artur'

import os


class Digester:
    def __init__(self):
        pass

    def eat(self, filename):
        file_object = open(filename, "r")
        content = ""
        for line in file_object:
            content += line
        file_object.close()
        extension = os.path.splitext(filename)[1]
        source = Source("Artur", "bare hands")
        extension = Property(1, "extension", extension, source)
        filename = Property(2, "file", filename, source)
        content = Property(3, "content", content, source)
        return extension, filename, content