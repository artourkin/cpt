import os
from unittest import TestCase
from Main.Common.Configurator import Configurator
from Main.Logic.Aggregator import Aggregator
from Main.Logic.Digester import Digester
from Main.Logic.Gatherer import Gatherer
from Main.Utils.MongoUtils import MongoUtils

__author__ = 'artur'


class TestAggregator(TestCase):

    properties = []
    gatherer = Gatherer()

    def setUp(self):
        BASE_DIR = os.path.dirname(__file__)
        digester = Digester(BASE_DIR+"/../../../Resources/fits.cfg")
        self.properties = digester.eat(BASE_DIR+"/../../../Resources/FITS/F0.xml")
        Configurator().setup("unittest", "one")
        for property in self.properties:
            self.gatherer.ingest(property)


    def test_get_frequency(self):
        self.aggregator = Aggregator("localhost", 27017, "cpt_core")
        result_frequency = self.aggregator.get_frequency("last_modified")   # TODO: frequency is not calculated properly
        result = self.aggregator.find({ "fileID" : "/home/roda/roda/tomcat/apache-tomcat-6.0.39/temp/METS.xml1510048826782337618.tmp" } )

    def tearDown(self):
        MongoUtils.cleanCollection()