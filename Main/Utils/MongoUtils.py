from bson import SON
from Main.Common.Configurator import Configurator
import logging
from Main.Utils.Utils import *

__author__ = 'artur'

logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG, filename=u'mylog.log')


class MongoUtils:
    @staticmethod
    def insert(property):
        collection = Configurator().getCollection()
        try:
            json = Utils.toJSON(property)
            # count = collection.find(json).limit(1).count()
            # if count < 1:
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
    def find(json, max=None):  # TODO: make this limit more visible!
        collection = Configurator().getCollection()
        if max is not None:
            cursor = collection.find(json).limit(max)
        else:
            cursor = collection.find(json)
        result = []
        for entry in cursor:
            result.append(entry)
        return result

        # @staticmethod
        # def find(json, max):
        #      collection = Configurator().getCollection()
        #      cursor = collection.find(json)
        #      result = []
        #      i=0
        #      for entry in cursor:
        #          result.append(entry)
        #          i+=1
        #          if (i >=max):
        #              break
        #      return result

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
        query = []
        if where:
            query.append({"$match": where})
        if groupby:
            query.append({"$group": groupby})
        # query.append({"$limit": 10})
        query.append({"$sort": SON([("count", -1)])})


        # query = [
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

    @staticmethod
    def applyfilter(filter):
        assert isinstance(filter, dict)
        collection = Configurator().getCollection()
        for prop, prop_value in filter.iteritems():
            query = {prop: prop_value}
            MongoUtils.findbyProperty(query)

    @staticmethod
    def getDistinctValues(field, collectionName=None, query=None):
        command = {}
        command.setdefault("key", field)
        if collectionName is not None:
            command.setdefault("distinct", Configurator().collection.name)
        if query is not None:
            command.setdefault("query", query)
        return MongoUtils.runCommand(command)

    @staticmethod
    def runCommand(command):
        result = Configurator().db.command(command)["values"]
        return result

    @staticmethod
    def FileHasProperty(fileID, property):
        fileDocuments = MongoUtils.findbyFile(fileID)
        for filedoc in fileDocuments:
            if filedoc.name == property[0] and filedoc.value == property[1]:
                return True
        return False

    @staticmethod
    def FileHasProperties(fileID, properties):
        for property in properties:
            if MongoUtils.FileHasProperty(fileID, property) is False:
                return False
        return True


    @staticmethod
    def filter(query):
        collection = Configurator().getCollection()


