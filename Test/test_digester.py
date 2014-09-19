from unittest import TestCase
from Main.Digester import Digester
__author__ = 'artur'


class TestDigester(TestCase):
    def test_eat(self):
        digester=Digester("Resources/fits.cfg")
        result=digester.eat("Resources/FITS/F0.xml")
