from Main.Common.Configurator import Configurator
from Main.Elements.Property import Property
from Main.Utils.MongoUtils import MongoUtils

__author__ = 'artur'


class Gatherer:

    def __init__(self):
        pass

    def ingest(self, property):
        if isinstance(property, Property):
            MongoUtils.insert(property)
