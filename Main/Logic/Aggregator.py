from Main.Utils.MongoUtils import MongoUtils

__author__ = 'artur'
from pymongo import MongoClient


class Aggregator:
    # def __init__(self, dbHost, dbPort, dbName):
    #    client = MongoClient(dbHost, dbPort)
    #   self.db = client[dbName]

    def get_frequency(self, property):
        match = {"property_name": property}
        group = {"_id": "$property_value", "count": {"$sum": 1}}
        result = MongoUtils.aggregate(match, group)

        # "$group": {
        #     "_id": {"file": "$fileID", "property": "$property_name", "property_value": "$property_value"},
        #     "count": {"$sum": 1}
        # }

        return result

    def find(self, query):
        """

        :param query: query contains a dictionary of key-value pairs
        """
        result = MongoUtils.find(query)

        return result

    def find(self, query, max):
        """

        :param query: query contains a dictionary of key-value pairs
        """
        result = MongoUtils.find(query, max)

        return result

    def findByFileID(self, fileID):
        result = MongoUtils.findbyFile(fileID)

        return result