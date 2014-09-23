__author__ = 'artur'
from pymongo import MongoClient


class Aggregator:
    def __init__(self, dbHost, dbPort, dbName):
        client = MongoClient(dbHost, dbPort)
        self.db = client[dbName]

    def get_frequency(self, property):
        result = self.db.private.aggregate([
            #{"$match": {"property_name": "format"}},
            {
                "$group": {
                            "_id": { "file": "$fileID",  "property" : "$property_name",  "property_value" : "$property_value"  } ,
                            "count": {"$sum": 1}
                           }
            }

        ])
        pass

    def find(self, query):
        """

        :param query: query contains a dictionary of key-value pairs
        """
        result = self.db.private.find(query).count()

        return result
