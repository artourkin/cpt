from unittest import TestCase
import unittest
from Main.Common.Configurator import Configurator
from Main.Logic.Digester import Digester
from Main.Logic.Gatherer import Gatherer
from Main.Utils.MongoUtils import MongoUtils

__author__ = 'artur'


class TestGatherer(TestCase):
    properties = []

    def setUp(self):
        digester = Digester("../../../Resources/fits.cfg")
        self.properties = digester.eat("../../../Resources/FITS/F0.xml")
        Configurator().setup("unittest", "one")

    def test_ingest(self):
        gatherer = Gatherer()
        for property in self.properties:
            gatherer.ingest(property)
        count = MongoUtils.countCollectionSize()
        self.assertEquals(count, 10)


    def tearDown(self):
        MongoUtils.cleanCollection()

if __name__ == '__main__':
    unittest.main()