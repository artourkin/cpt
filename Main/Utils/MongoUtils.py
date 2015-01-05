from bson import SON
from Main.Common.Configurator import Configurator
import logging
from Main.Utils.Utils import *

__author__ = 'artur'


logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'mylog.log')

class MongoUtils:
    @staticmethod
    def insert(property):
        collection = Configurator().getCollection()
        try:
            json = Utils.toJSON(property)
            #count = collection.find(json).limit(1).count()
            #if count < 1:
            collection.insert(json)
            return True
        except ValueError:
            logging.error("Bad Property instance")
            return False


    @staticmethod
    def countCollectionSize():
        collection = Configurator().getCollection()
        result = collection.count()
        return result

    @staticmethod
    def findbyProperty(property):
        collection = Configurator().getCollection()
        assert isinstance(property, Property)
        json = Utils.toJSON(property)
        cursor = collection.find(json)
        result = []
        for entry in cursor:
            result.append(Utils.toProperty(entry))
        return result

    @staticmethod
    def find(json):
        collection = Configurator().getCollection()
        cursor = collection.find(json)
        result = []
        for entry in cursor:
            result.append(entry)
        return result

    @staticmethod
    def delete(property):
        collection = Configurator().getCollection()
        json = Utils.toJSON(property)
        collection.remove(json)

    @staticmethod
    def cleanCollection():
        collection = Configurator().getCollection()
        collection.drop()

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
    def aggregate(where=None, groupby=None):
        collection = Configurator().getCollection()
        # where=Configurator().filter
        query=[]
        if where:
            query.append({"$match": where})
        if groupby:
            query.append({"$group": groupby})
        query.append({"$sort": SON([("count", -1)])})


        #query = [
        #    {"$match": where},
        #    {"$group": groupby},
        #    {"$sort": SON([("count", -1)])}
        #]
        result = collection.aggregate(query)
        return result

        # @staticmethod
        # def aggregate(query):
        #     collection = Configurator().getCollection()
        #     result = collection.aggregate(query)
        #     return result