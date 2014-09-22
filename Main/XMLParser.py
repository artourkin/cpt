from lxml import etree
import io
from lxml.etree import _ElementUnicodeResult

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
        result = []
        xpaths_copy = list(xpaths)

        tree = etree.XML(xml)
        tmp_result = []
        for index, xpath in enumerate(xpaths):

            if not xpath.startswith("/"):
                tmp_result.append(xpath)
            else:
                xpath_results = self.applyXPathToElement(xpath, tree)

                if len(xpath_results) == 1:
                    tmp_result.append(xpath_results[0])
                if len(xpath_results) > 1:

                    tmp_xpath = xpaths[index]
                    i = index + 1
                    while i < len(xpaths):
                        tmp_xpath += "|" + xpaths[i]
                        i += 1

                    tmp_xpath_results = self.applyXPathToElement(tmp_xpath, tree)

                    arrayarray = []
                    array=[] #+ tmp_result
                    for i, tmp_xpath_result in enumerate(tmp_xpath_results):
                        if tmp_xpath_result in xpath_results:
                            xpath_result = tmp_xpath_result
                            if len(array) > 0:
                                arrayarray.append(array)
                                array = [] + tmp_result
                                array.append(xpath_result)
                            else:
                                array = [] + tmp_result
                                array.append(tmp_xpath_results[i])
                            k = 0
                        else:
                            k += 1
                            if k % (len(xpaths) - index) != 0:

                                array.append(tmp_xpath_results[i])
                            else:
                                arrayarray.append(array)
                                array = [] + tmp_result
                                array.append(xpath_result)
                                array.append(tmp_xpath_results[i])
                                k += 1
                    arrayarray.append(array)
                    return arrayarray

        return tmp_result




    def applyXPathToElement(self, xpath, element):
        result = element.xpath(xpath)
        return result









