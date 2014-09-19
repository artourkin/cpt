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

    def extractXPath(self, xpaths, xml):

        result=[]
        for xpath in xpaths:
            tmp_result=[]
            if not xpath.startswith("/"):
                tmp_result.append(xpath)
            else:
                xml = xml.read().replace('\n', '').replace(' xmlns=', ' xmlnamespace=')
                xml = xml.encode("utf-8")
                tree = etree.XML(xml)
                result = tree.xpath(xpath)
                if len(result) == 1:
                    tmp_result.append(result[0])
                if len(result) > 1:
                    pass
        raise NotImplementedError("not implemented case when there are more results than 1")
        #TODO: we need a recursive function here that will traverse all the results of xpath extraction.
        #if there are more than 1 results of xpath, we should repeat the process for the next xpath, keeping the previous result as a condition
        # e.g.: '//identity/tool/@toolname&//identity/@format=PDF'











