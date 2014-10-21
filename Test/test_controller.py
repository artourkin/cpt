from unittest import TestCase
from Main.Common.Configurator import Configurator
from Main.Common.Params import *
from Main.Controller import Controller

__author__ = 'artur'

class TestController(TestCase):
    def test_process(self):
        Configurator().setup()
        cntr = Controller()
        cntr.ingest("Resources/FITS/")
