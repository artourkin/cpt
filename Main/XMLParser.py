from lxml import etree
import io

__author__ = 'artur'


class XMLParser:
    def __init__(self):
        self.parser = etree.XMLParser()

    def loadCFG(self, configpath):
        result = []
        file_object = open(configpath, "r")
        for line in file_object:
            line = line.strip("\n")
            result.append(line.split(" "))
        return result

    def extractXPath(self, xpath, xml):

        if not xpath.startswith("/"):
            return xpath

        xml = xml.read().replace('\n', '').replace(' xmlns=', ' xmlnamespace=')
        xml = xml.encode("utf-8")
        tree = etree.XML(xml)
        result = tree.xpath(xpath)
        if len(result) == 1:
            return result[0]

        raise NotImplementedError("not implemented case when there are more results than 1")









