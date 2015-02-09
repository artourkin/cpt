from Main.Common.Configurator import Configurator
from Main.Utils.MongoUtils import MongoUtils

__author__ = 'artur'


class Aggregator:
    # def __init__(self, dbHost, dbPort, dbName):
    # client = MongoClient(dbHost, dbPort)
    # self.db = client[dbName]

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
        result = MongoUtils.find(query, 100)

        return result

        #def find(self, query, max):
        #    """

    #
    #        :param query: query contains a dictionary of key-value pairs
    #       """
    #      result = MongoUtils.find(query, max)
    #
    #       return result

    def findByFileID(self, fileID):
        result = MongoUtils.findbyFile(fileID)

        return result


    def get_distributions(self, properties):
        frequencies = {}
        for property in properties:
            frequency = self.get_frequency(property)
            frequencies.setdefault(property, frequency)
        return frequencies


    def get_frequency_filtered(self, property):
        filt = Configurator().filter
        filter_frequencies = []
        properties = []
        properties.append(property)
        for filter_key, filter_value in filt.iteritems():
            properties.append(filter_key)
            #filter_frequencies.append(self.get_frequency(filter_key)["result"])
        #sampler = Sampler()
      #  result=sampler.calculate_cartesian_product(properties)
        #property_frequency = self.get_frequency(property)["result"]
        return True

