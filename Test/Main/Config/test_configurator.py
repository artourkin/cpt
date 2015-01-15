import os
from unittest import TestCase
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
        BASE_DIR = os.path.dirname(__file__)
        digester = Digester(BASE_DIR+"/../../Resources/fits.cfg")
        self.properties = digester.eat(BASE_DIR+"/../../Resources/FITS/F0.xml")
        self.configurator.setup("unittest", "one")
        for property in self.properties:
            self.gatherer.ingest(property)

    def test_setup(self):

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
