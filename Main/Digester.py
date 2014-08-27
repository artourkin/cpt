__author__ = 'artur'

import os
from Main.Elements.Property import Property


class Digester:
    def __init__(self):
        pass

    def eat(self,filename):
        file = open(filename, "r")
        content= ""
        for line in file:
            content+=line
        file.close()
        extension = os.path.splitext(filename)[1]
        extension = Property(1, "extension", extension)
        filename = Property(2, "file", filename)
        content = Property(3, "content", content)
        return extension, filename, content