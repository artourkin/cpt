from Main.Common.Configurator import Configurator
from Main.Elements.Property import Property
from Main.Logic.Aggregator import Aggregator
import itertools

__author__ = 'artur'



# The idea:
# We get distributions of the properties X. Then we get cartesian product of the bins of each distrubution, sorted as most popular first.
# Then for each cartesian product (prop1: val1, prop2: val2,...) we create a query and submit it to mongodb.
# If there is no result, then we skip this combination. This should mean there is no file available.
# If there is 1 result and it is not present in the sample collection, we put it in our resulting sample collection.
#   If there are more than 1 results, we pick the first not present in the sample collection and put it in the result.
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

    def get_distributions(self, properties):

        for property in properties:
            frequency = self.aggregator.get_frequency(property)
            self.frequencies.setdefault(property, frequency)
        return self.frequencies


    def calculate_cartesian_product(self):
        tmp_list = []
        result = []
        for property, payload in self.frequencies.items():  #Parsing json
            property_list = []
            assert isinstance(payload, dict)
            distribution = payload.get("result")
            for bin in distribution:
                value = bin.get("_id")
                count = bin.get("count")
                property_list.append([property, value, count])
            tmp_list.append(property_list)

        tmp_result = list(itertools.product(*tmp_list))  #Calculate cartesian product

        for tmp_tuple in tmp_result:  #Sort samples according to their count in the collection
            assert isinstance(tmp_tuple, tuple)
            tmp_tuple_listed = (list(tmp_tuple))
            weight = 0
            for prop in tmp_tuple_listed:
                assert isinstance(prop, list)
                weight += prop[2]
            tmp_tuple_listed.append(weight)
            result.append(tmp_tuple_listed)

        result = sorted(result, key=lambda sample: sample[len(sample) - 1],
                        reverse=True)

        for tmp_list in result:  #Cleaning up the count variable
            for prop in tmp_list[:-1]:
                assert isinstance(prop, list)
                if len(prop) > 2 and prop[2]:
                    prop.pop(2)
        self.samples_weighted = result
        return result

    def retrieve_samples(self, max):
        aggregator = Aggregator()
        result = []
        i = 0
        for sample in self.samples_weighted:
            query = dict()
            property = sample[0]
            assert isinstance(property, list)
            query.setdefault("property_name", property[0])
            query.setdefault("property_value", property[1])
            documents = aggregator.find(query, 100)

            for document in documents:
                assert isinstance(document, dict)
                found = True
                fileID = document.get("fileID")
                tmp_documents = aggregator.findByFileID(fileID)
                for sample_property in sample[:-1]:

                    for property in tmp_documents:
                        assert isinstance(property, Property)
                        if (property.name == sample_property[0] and
                                    property.value == sample_property[1]):
                            found = True
                            break
                        found = False

                if (found == True):
                    if i <= max and not fileID in result:
                        result.append(fileID)
                        i += 1
        return result


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
                tmp_documents = aggregator.findByFileID(fileID)
                for sample_property in sample[:-1]:

                    for property in tmp_documents:
                        assert isinstance(property, Property)
                        if (property.name == sample_property[0] and
                                    property.value == sample_property[1]):
                            found = True
                            break
                        found = False

                if (found == True):
                    if not fileID in result:
                        result.append(fileID)

        return result
        #TODO: test this method carefully! Potentially lots of bugs.