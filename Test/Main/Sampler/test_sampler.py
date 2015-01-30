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
        digester = Digester(BASE_DIR + "/../../Resources/fits.cfg")
        self.properties = digester.eat(BASE_DIR + "/../../Resources/FITS/F0.xml")
        self.properties += digester.eat(BASE_DIR + "/../../Resources/FITS/F1.xml")
        self.properties += digester.eat(BASE_DIR + "/../../Resources/FITS/F2.xml")
        Configurator().setup("unittest", "one")
        for property in self.properties:
            self.gatherer.ingest(property)


    def test_calculate_cartesian_product(self):
        sampler = Sampler()
        sampler.calculate_cartesian_product(["lastmodified", "format", "mimetype"])

    def test_retrieve_samples(self):
        sampler = Sampler()
        sampler.calculate_cartesian_product(["lastmodified", "format", "mimetype"])
        sampler.retrieve_samples()

    def tearDown(self):
        MongoUtils.cleanCollection()

