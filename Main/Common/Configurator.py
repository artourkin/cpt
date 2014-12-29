from pymongo import MongoClient
import pymongo
from Main.Common.Params import DB_HOST, DB_PORT, DB_NAME, DB_COLLECTION_NAME

__author__ = 'artur'


class Configurator:
    __shared_state = {}
    filter = {}
    def __init__(self):
        self.__dict__ = self.__shared_state



    def setup(self, db_name=None, db_collection=None, db_host=None, db_port=None):
        if not db_name:
            db_name=DB_NAME
        if not db_collection:
            db_collection=DB_COLLECTION_NAME
        if not db_host:
            db_host=DB_HOST
        if not db_port:
            db_port=DB_PORT
        client = MongoClient(db_host, db_port)
        self.db = client[db_name]
        # self.filter = {}                        #TODO: what will happen to a shared filter in a web app?
        self.selectCollection(db_collection)
        self.collection.ensure_index(
            [("property_name", pymongo.ASCENDING), ("property_value", pymongo.ASCENDING), ("fileID", pymongo.ASCENDING),
             ("sources", pymongo.ASCENDING), ("unique", True)])

    def getCollection(self):
        return self.collection

    def getDB(self):
        return self.db


    def selectCollection(self, collectionName):
        self.collection = self.db[collectionName]

    def addFilterCondition(self, filterCondition):
        self.filter.update(filterCondition)

    def removeFilterCondition(self, filterCondition):
        del self.filter[filterCondition.items()[0][0]]
