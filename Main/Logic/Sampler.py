from Main.Elements.Property import Property
from Main.Logic.Aggregator import Aggregator
import itertools
from Main.Utils.MongoUtils import MongoUtils

__author__ = 'artur'



# The idea:
# We get distributions of the properties X. Then we get cartesian product of the bins of each distrubution, sorted as most popular first.
# Then for each cartesian product (prop1: val1, prop2: val2,...) we create a query and submit it to mongodb.
# If there is no result, then we skip this combination. This should mean there is no file available.
# If there is 1 result and it is not present in the sample collection, we put it in our resulting sample collection.
# If there are more than 1 results, we pick the first not present in the sample collection and put it in the result.
#
#
#
#
#


class Sampler():
    frequencies = {}
    samples_weighted = []

    def __init__(self):
        self.aggregator = Aggregator()


    def prepareDataForCartesian(self, frequencies, limit):
        result = []
        for property, payload in frequencies.items():  # Parsing json
            property_list = []
            assert isinstance(payload, dict)
            distribution = payload.get("result")
            for bin in distribution[:limit]:
                value = bin.get("_id")
                count = bin.get("count")
                property_list.append([property, value, count])
            result.append(property_list)
        return result

    def prepareDataForSorting(self, unsorted):
        result = []
        for tmp_tuple in unsorted:  # Sort samples according to their count in the collection
            assert isinstance(tmp_tuple, tuple)
            tmp_tuple_listed = (list(tmp_tuple))
            weight = 0
            for prop in tmp_tuple_listed:
                assert isinstance(prop, list)
                weight += prop[2]
            tmp_tuple_listed.append(weight)
            result.append(tmp_tuple_listed)
        return result

    def calculate_cartesian_product(self, properties, limit=10):  # TODO: make this limit more visible!

        self.frequencies = self.aggregator.get_distributions(properties)
        tmp_list = self.prepareDataForCartesian(self.frequencies, limit)
        cartesian_product = list(itertools.product(*tmp_list))  # Calculate cartesian product
        unsorted_list = self.prepareDataForSorting(cartesian_product)
        sorted_list = sorted(unsorted_list, key=lambda sample: sample[len(sample) - 1],
                        reverse=True)

        for tmp_list in sorted_list:  # Cleaning up the count variable
            for prop in tmp_list[:-1]:
                assert isinstance(prop, list)
                if len(prop) > 2 and prop[2]:
                    prop.pop(2)
        self.samples_weighted = sorted_list
        return sorted_list


    def retrieve_samples(self):
        aggregator = Aggregator()
        result = []
        i = 0
        for sample in self.samples_weighted:
            query = dict()
            property = sample[0]
            assert isinstance(property, list)
            query.setdefault("property_name", property[0])
            query.setdefault("property_value", property[1])
            documents = aggregator.find(query)

            for document in documents:
                assert isinstance(document, dict)
                found = True
                fileID = document.get("fileID")

                if MongoUtils.FileHasProperties(fileID, sample[:-1]):
                    if not fileID in result:                                #TODO: idea for filtering, if we found a file that satisfies our criteria then put +1 to the bin. Finally, accumulate it for all the bins and vuala.
                        result.append(fileID)
                    break



        return result
        # TODO: test this method carefully! Potentially lots of bugs.


