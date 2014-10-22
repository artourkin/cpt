from pymongo import MongoClient
from Main.Common.Params import DB_HOST, DB_PORT, DB_NAME, DB_COLLECTION_NAME

__author__ = 'artur'


class Configurator:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def setup(self):
        client = MongoClient(DB_HOST, DB_PORT)
        self.db = client[DB_NAME]
      #  self.filter = {}                        #TODO: what will happen to a shared filter in a web app?
        self.selectCollection(DB_COLLECTION_NAME)

    def getCollection(self):
        return self.collection

    def getDB(self):
        return self.db

    def selectCollection(self, collectionName):
        self.collection = self.db[collectionName]

    def addFilterCondition(self, filterCondition):
        self.filter.update(filterCondition)

    def removeFilterCondition(self, filterCondition):
        del filter[filterCondition.items()[0][0]]
