from unittest import TestCase
from Main.Elements.Property import Property

__author__ = 'artur'


class TestProperty(TestCase):
    def test_tostring(self):
        """
        Testing Property class
        """
        prop = Property(1, "format", "pdf")
        prop.tostring()