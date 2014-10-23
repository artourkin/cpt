from bson import SON
from Main.Common.Configurator import Configurator

from Main.Utils.Utils import *

__author__ = 'artur'


class MongoUtils:
    @staticmethod
    def insert(property):
        collection = Configurator().getCollection()
        json = Utils.toJSON(property)
        #count = collection.find(json).limit(1).count()
        #if count < 1:
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
    def cleanCollection(collectionName):
        db = Configurator().getDB()
        db[collectionName].drop()

    @staticmethod
    def update(old_property, new_property):
        MongoUtils.delete(old_property)
        MongoUtils.insert(new_property)

    @staticmethod
    def findbyFile(fileID):
        collection = Configurator().getCollection()
        cursor = collection.find({"fileID": fileID})
        result = []
        for entry in cursor:
            result.append(Utils.toProperty(entry))
        return result

    @staticmethod
    def aggregate(where, groupby):
        collection = Configurator().getCollection()
        # where=Configurator().filter
        query = [
            {"$match": where},
            {"$group": groupby},
            {"$sort": SON([("count", -1)])}
        ]
        result = collection.aggregate(query)
        return result

        # @staticmethod
        # def aggregate(query):
        #     collection = Configurator().getCollection()
        #     result = collection.aggregate(query)
        #     return result