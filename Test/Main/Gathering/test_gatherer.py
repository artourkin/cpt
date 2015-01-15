import os
from unittest import TestCase
from Main.Common.Configurator import Configurator
from Main.Logic.Digester import Digester
from Main.Logic.Gatherer import Gatherer
from Main.Utils.MongoUtils import MongoUtils

__author__ = 'artur'


class TestGatherer(TestCase):
    properties = []

    def setUp(self):
        BASE_DIR = os.path.dirname(__file__)
        digester = Digester(BASE_DIR+"/../../Resources/fits.cfg")
        self.properties = digester.eat(BASE_DIR+"/../../Resources/FITS/F0.xml")
        Configurator().setup("unittest", "one")

    def test_ingest(self):
        gatherer = Gatherer()
        for property in self.properties:
            gatherer.ingest(property)
        count = MongoUtils.countCollectionSize()
        self.assertEquals(count, 10)


    def tearDown(self):
        MongoUtils.cleanCollection()
