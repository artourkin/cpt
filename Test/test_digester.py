from unittest import TestCase
from Main.Digester import Digester
__author__ = 'artur'


class TestDigester(TestCase):
    def test_eat(self):
        digester=Digester()
        result=digester.eat("Resources/FITS/F0.xml")
        result[0].echo()
        result[1].echo()
        result[2].echo()