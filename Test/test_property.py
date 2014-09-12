from unittest import TestCase
from Main.Elements.Property import Property
from Main.Elements.Source import Source

__author__ = 'artur'


class TestProperty(TestCase):
    def test_tostring(self):
        """
        Testing Property class
        """
        source = Source("Artur", "bare hands")
        prop = Property(1, "format", "pdf", source)
        prop.echo()
        prop.uid = prop.uid + 1
        prop.echo()
