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
        self.collection=self.db[DB_COLLECTION_NAME]
    def getCollection(self):
        return self.collection