from unittest import TestCase
from Main.Aggregator import Aggregator

__author__ = 'artur'


class TestAggregator(TestCase):
    def test_get_frequency(self):
        self.aggregator = Aggregator("localhost", 27017, "cpt")
        result= self.aggregator.get_frequency("property_value")
        result = self.aggregator.find({ "fileID" : "/home/roda/roda/tomcat/apache-tomcat-6.0.39/temp/METS.xml1510048826782337618.tmp" } )
        pass