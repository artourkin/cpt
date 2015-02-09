import os
from unittest import TestCase
from Main.Common.Configurator import Configurator
from Main.Logic.Aggregator import Aggregator
from Main.Logic.Digester import Digester
from Main.Logic.Gatherer import Gatherer
from Main.Logic.Sampler import Sampler
from Main.Utils.MongoUtils import MongoUtils

__author__ = 'artur'


class TestAggregator(TestCase):
    properties = []
    gatherer = Gatherer()

    def setUp(self):
        BASE_DIR = os.path.dirname(__file__)
        digester = Digester(BASE_DIR + "/../../Resources/fits.cfg")
        self.properties = digester.eat(BASE_DIR + "/../../Resources/FITS/F0.xml")
        self.properties += digester.eat(BASE_DIR + "/../../Resources/FITS/F1.xml")
        Configurator().setup("unittest", "one")
        for property in self.properties:
            self.gatherer.ingest(property)


    def test_get_frequency(self):
        self.aggregator = Aggregator()
        result_frequency = self.aggregator.get_frequency("lastmodified")
        self.assertEqual(result_frequency,
                         {u'ok': 1.0, u'result': [{u'count': 1, u'_id': u'2014:09:05 17:27:22+01:00'}]})

    def test_find(self):
        self.aggregator = Aggregator()
        result = self.aggregator.find(
            {"fileID": "/home/roda/roda/tomcat/apache-tomcat-6.0.39/temp/METS.xml1510048826782337618.tmp"})
        self.assertIsNotNone(result)


    def test_get_frequency_filtered(self):
        self.aggregator = Aggregator()
        Configurator().addFilterCondition({"mimetype": "text/xml"})
        result_frequency = self.get_frequency_filtered("lastmodified")

    def get_frequency_filtered(self, property):
        self.aggregator = Aggregator()
        filt = Configurator().filter

        properties = []
        properties.append(property)
        for filter_key, filter_value in filt.iteritems():
            properties.append(filter_key)
        sampler = Sampler()
        products = sampler.calculate_cartesian_product(properties)
        # property_frequency = self.get_frequency(property)["result"]
        result = []
        for product in products:
            nofit = False
            product_dict = {}
            for product_property in product[:-1]:
                product_dict.setdefault(product_property[0], product_property[1])
            # if filt in product_dict:
            # result.append(product)
            for filter_key, filter_value in filt.iteritems():
                if (product_dict[filter_key] != filter_value):
                    nofit = True
                    break
            if nofit == False:
                result.append(product)
        del filt, filter_value,filter_key, nofit, product_dict, product, product_property, products
        frequencies = dict()
        result_ = []
        for sample in result:
            query = dict()
            property_ = sample[0]
            freq_dict = dict()

            assert isinstance(property_, list)
            query.setdefault("property_name", property_[0])
            query.setdefault("property_value", property_[1])
            documents = self.aggregator.find(query)
            for props in sample[:-1]:
                if props[0] == property:
                    freq_dict.setdefault(property, props[1])
            for document in documents:
                assert isinstance(document, dict)
                found = True
                fileID = document.get("fileID")

                if MongoUtils.FileHasProperties(fileID, sample[:-1]):
                    if not fileID in result_:  # TODO: idea for filtering, if we found a file that satisfies our criteria then put +1 to the bin. Finally, accumulate it for all the bins and vuala.
                        result_.append(fileID)
                        val = freq_dict.get(property)
                        frequencies[val] = frequencies.get(val, 0) + 1
                        # if freq_dict[property] in frequencies:
                        # frequencies[freq_dict[property]] = +1
                        #  else:
                        #      frequencies[freq_dict[property]] = 1
                    break

        return True


    def tearDown(self):
        MongoUtils.cleanCollection()