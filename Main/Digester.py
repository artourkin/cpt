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
            file_object = open(filename, "r")

            xml = file_object.read().replace('\n', '').replace(' xmlns=', ' xmlnamespace=')
            xml = xml.encode("utf-8")

            value = self.parser.extractXPath(line, xml)
            #result.append(value)


            for val in value:
                prop = Property(val[0], val[1], val[2], val[3], val[4])
                properties.append(prop)

        return properties