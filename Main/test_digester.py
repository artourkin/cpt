from unittest import TestCase
from Main.Digester import Digester
__author__ = 'artur'


class TestDigester(TestCase):
    def test_eat(self):
        digester=Digester()
        result=digester.eat("/home/artur/Downloads/manifest.txt")
        result[0].tostring()
        result[1].tostring()
        result[2].tostring()