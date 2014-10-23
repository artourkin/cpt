from Main.Elements.Property import Property
from Main.Utils.XMLParser import XMLParser

__author__ = 'artur'


class Digester:
    def __init__(self, cfgpath):
        self.parser = XMLParser()
        self.xpaths = self.parser.loadCFG(cfgpath)

    def eat(self, filename):
        properties = []
        result = []
        file_object = open(filename, "r")
        xml = file_object.read().replace('\n', '').replace(' xmlns=', ' xmlnamespace=')
        xml = xml.encode("utf-8")

        result += self.parser.extractFormatInfo(xml)
        result += self.parser.extractMimeType(xml)
        for line in self.xpaths:
            result += self.parser.extractXPath(line, xml)

        for value in result:
            prop = Property(value[0], value[1], value[2], value[3])
            properties.append(prop)

        return properties