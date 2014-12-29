from Main.Utils.MongoUtils import MongoUtils

__author__ = 'artur'
from pymongo import MongoClient


class Aggregator:
    def __init__(self, dbHost, dbPort, dbName):
        client = MongoClient(dbHost, dbPort)
        self.db = client[dbName]

    def get_frequency(self, property):
        where = {"property_name": property}
        groupby_text = {"_id": "$property_value", "count": {"$sum": 1}}
        result = MongoUtils.aggregate( groupby=groupby_text )

               # "$group": {
               #     "_id": {"file": "$fileID", "property": "$property_name", "property_value": "$property_value"},
               #     "count": {"$sum": 1}
               # }

        return result

    def find(self, query):
        """

        :param query: query contains a dictionary of key-value pairs
        """
        result = self.db.private.find(query).count()

        return result
