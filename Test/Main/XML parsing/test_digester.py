import os
from unittest import TestCase
from Main.Logic.Digester import Digester

__author__ = 'artur'


class TestDigester(TestCase):
    def test_eat(self):
        BASE_DIR = os.path.dirname(__file__)
        digester = Digester(BASE_DIR+"/../../Resources/fits.cfg")
        result = digester.eat(BASE_DIR+"/../../Resources/FITS/F0.xml")
        self.assertEquals(len(result), 10)
