from Main.Common.Configurator import Configurator
from Main.Elements.Property import Property

from Main.Utils.Utils import *

__author__ = 'artur'


class MongoUtils:
    @staticmethod
    def insert(property):
        collection = Configurator().getCollection()
        json = Utils.toJSON(property)
        count = collection.find(json).limit(1).count()
        if count < 1:
            collection.insert(json)

    @staticmethod
    def find(property):
        collection = Configurator().getCollection()
        json = Utils.toJSON(property)
        cursor = collection.find(json)
        result = []
        for entry in cursor:
            result.append(Utils.toProperty(entry))
        return result

    @staticmethod
    def delete(property):
        collection = Configurator().getCollection()
        json = Utils.toJSON(property)
        collection.remove(json)

    @staticmethod
    def update(old_property, new_property):
        MongoUtils.delete(old_property)
        MongoUtils.insert(new_property)

