from unittest import TestCase
from Main.Controller import Controller

__author__ = 'artur'

class TestController(TestCase):
    def test_process(self):
        cntr = Controller("localhost", 27017, "cpt")
        cntr.process("Resources/FITS/", "private")
