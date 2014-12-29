from unittest import TestCase
import unittest
from Main.Common.Configurator import Configurator
from Main.Logic.Digester import Digester
from Main.Logic.Gatherer import Gatherer
from Main.Utils.MongoUtils import MongoUtils

__author__ = 'artur'


class TestConfigurator(TestCase):
    configurator = Configurator()
    properties = []
    gatherer = Gatherer()

    def setUp(self):
        digester = Digester("../../../Resources/fits.cfg")
        self.properties = digester.eat("../../../Resources/FITS/F0.xml")
        self.configurator.setup("unittest", "one")

    def test_setup(self):
        for property in self.properties:
            self.gatherer.ingest(property)
        count = MongoUtils.countCollectionSize()
        self.assertEquals(count, 10)


    def test_getCollection(self):
        collectionName=self.configurator.getCollection().name
        self.assertEquals(collectionName, "one")


    def test_getDB(self):
        dbName=self.configurator.getDB().name
        self.assertEquals(dbName, "unittest")

    def test_addFilterCondition(self):
        where = {"property_name": "lastmodified"}
        self.configurator.addFilterCondition(where)


    def test_removeFilterCondition(self):
        where = {"property_name": "lastmodified"}
        self.configurator.removeFilterCondition(where)

    def tearDown(self):
        MongoUtils.cleanCollection()


if __name__ == '__main__':
    unittest.main()