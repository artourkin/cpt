import os
from unittest import TestCase
from Main.Common.Configurator import Configurator
from Main.Elements.Property import Property
from Main.Logic.Digester import Digester
from Main.Utils.MongoUtils import MongoUtils
import copy

__author__ = 'artur'

class TestMongoUtils(TestCase):
    properties = []

    def setUp(self):
        BASE_DIR = os.path.dirname(__file__)
        digester = Digester(BASE_DIR+"/../../Resources/fits.cfg")
        self.properties = digester.eat(BASE_DIR+"/../../Resources/FITS/F0.xml")
        Configurator().setup("unittest", "one")
        for property in self.properties:
            if isinstance(property, Property):
                result = MongoUtils.insert(property)

    def test_insert(self):
       pass
       # TODO: create an incorrect property and try to insert it into db
       # broken_prop = Property(None, 1, "fd", None)
       # result = MongoUtils.insert(broken_prop)
       # self.assertFalse(result)

    def test_countCollectionSize(self):
        collectionSize = MongoUtils.countCollectionSize()
        self.assertEquals(collectionSize, 10)

    def test_findbyProperty(self):
        properties = MongoUtils.findbyProperty(self.properties[0])
        found_property = properties[0]
        found_value = found_property.value
        value = self.properties[0].value
        self.assertAlmostEquals(found_value, value)

    def test_update(self):
        modified_property = copy.copy(self.properties[0])
        assert isinstance(modified_property, Property)
        modified_property.value += "modified"
        MongoUtils.update(self.properties[0], modified_property)
        tmp_property = MongoUtils.findbyProperty(modified_property)
        found_value = tmp_property[0].value
        value = modified_property.value
        self.assertAlmostEquals(found_value, value)

    def test_findbyFile(self):
        fileID = "/home/roda/roda/tomcat/apache-tomcat-6.0.39/temp/METS.xml1510048826782337618.tmp"
        properties = MongoUtils.findbyFile(fileID)
        self.assertEquals(len(properties), 10)

    def test_aggregate(self):
        where = {"property_name": "lastmodified"}
        groupby = {"_id": "$property_value", "count": {"$sum": 1}}
        result = MongoUtils.aggregate( where, groupby)
        self.assertEqual(result, {u'ok': 1.0, u'result': [{u'count': 1, u'_id': u'2014:09:05 17:27:22+01:00'}]})

    def tearDown(self):
        MongoUtils.cleanCollection()
