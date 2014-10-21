from Main.Common.Configurator import Configurator
from Main.Utils.MongoUtils import *

__author__ = 'artur'

from os import walk

from pymongo import MongoClient

from Main.Digester import Digester

class Controller:

    def __init__(self):
        self.digester = Digester("Resources/fits.cfg")

    def ingest(self, path):
        collection = Configurator().getCollection()
        files = []
        for (dirpath, dirnames, filenames) in walk(path):
            files.extend(filenames)
        for file in files:
            properties = self.digester.eat(path + file)
            for prop in properties:
                MongoUtils.insert(prop)

