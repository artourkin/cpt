import os
from unittest import TestCase
from Main.Common.Configurator import Configurator
from Main.Logic.Digester import Digester
from Main.Logic.Gatherer import Gatherer
from Main.Logic.Sampler import Sampler
from Main.Utils.MongoUtils import MongoUtils

__author__ = 'artur'


class TestSampler(TestCase):
    gatherer = Gatherer()
    def setUp(self):
        BASE_DIR = os.path.dirname(__file__)
        digester = Digester(BASE_DIR+"/../../Resources/fits.cfg")
        self.properties = digester.eat(BASE_DIR+"/../../Resources/FITS/F0.xml")
        Configurator().setup("unittest", "one")
        for property in self.properties:
            self.gatherer.ingest(property)

    def test_get_distributions(self):

        sampler = Sampler()

        sampler.get_distributions(["lastmodified", "format"])



    def tearDown(self):
        MongoUtils.cleanCollection()