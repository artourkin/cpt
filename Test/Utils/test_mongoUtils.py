from unittest import TestCase
from Main.Common.Configurator import Configurator
from Main.Utils.MongoUtils import MongoUtils

__author__ = 'artur'


class TestfindbyFile(TestCase):
    Configurator().setup()
    MongoUtils.findbyFile("/home/petrov/taverna/tmp/002/002381.pdf")


class Testaggregate(TestCase):
    Configurator().setup()
    where = {"property_name": "lastmodified"}
    Configurator().addFilterCondition(where)
    groupby = {"_id": "$property_value", "count": {"$sum": 1}}
    result = MongoUtils.aggregate(groupby)
    print result