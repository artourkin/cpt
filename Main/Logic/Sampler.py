from Main.Common.Configurator import Configurator
from Main.Logic.Aggregator import Aggregator

__author__ = 'artur'



# The idea:
#   We get distributions of the properties X. Then we get cartesian product of the bins of each distrubution, sorted as most popular first.
#   Then for each cartesian product (prop1: val1, prop2: val2,...) we create a query and submit it to mongodb.
#   If there is no result, then we skip this combination. This should mean there is no file available.
#   If there is 1 result and it is not present in the sample collection, we put it in our resulting sample collection.
#   If there are more than 1 results, we pick the first not present in the sample collection and put it in the result.
#
#
#
#
#






class Sampler():

    frequencies={}

    def __init__(self):
        self.aggregator = Aggregator()

    def get_distributions(self, properties):

        for property in properties:
            frequency = self.aggregator.get_frequency(property)
            self.frequencies.setdefault(property, frequency)
        return self.frequencies


    def calculate_cartesian_product(self):

        for property, values in self.frequencies.items():
            assert isinstance(values, dict)
            for value in values.items(): #TODO: finish this method
            pass

