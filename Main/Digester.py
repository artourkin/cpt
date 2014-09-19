from Main.Elements.Property import Property
from Main.XMLParser import XMLParser

__author__ = 'artur'

class Digester:
    def __init__(self, cfgpath):
        self.parser = XMLParser()
        self.xpaths = self.parser.loadCFG(cfgpath)

    def eat(self, filename):
        properties=[]
        for line in self.xpaths:
            result = []
            for xpath in line:
                file_object = open(filename, "r")
                value = self.parser.extractXPath(xpath, file_object)
                result.append(value)

            prop = Property(result[0], result[1], result[2], result[3], result[4])
            properties.append(prop)

        return properties