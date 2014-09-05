from unittest import TestCase
from Main.Controller import Controller

__author__ = 'artur'


class TestController(TestCase):
    def test_process(self):
        cntr = Controller()
        cntr.process("/home/artur/rnd/git/cpt/Test/")
