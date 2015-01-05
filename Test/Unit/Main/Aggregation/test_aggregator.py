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
        self.aggregator = Aggregator()
        result_frequency = self.aggregator.get_frequency("lastmodified")
        self.assertEqual(result_frequency, {u'ok': 1.0, u'result': [{u'count': 1, u'_id': u'2014:09:05 17:27:22+01:00'}]})

    def test_find(self):
        self.aggregator = Aggregator()
        result = self.aggregator.find({ "fileID" : "/home/roda/roda/tomcat/apache-tomcat-6.0.39/temp/METS.xml1510048826782337618.tmp" } )
        self.assertIsNotNone(result)
    def tearDown(self):
        MongoUtils.cleanCollection()