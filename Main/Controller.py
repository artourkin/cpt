__author__ = 'artur'

from os import walk

from pymongo import MongoClient

from Main.Digester import Digester


class Controller:
    db = ''
    digester = ''

    def __init__(self, dbHost, dbPort, dbName):
        client = MongoClient(dbHost, dbPort)
        self.db = client[dbName]
        self.digester = Digester("Resources/fits.cfg")


    def process(self, path, collectionName):
        collection = self.db[collectionName]
        files = []
        for (dirpath, dirnames, filenames) in walk(path):
            files.extend(filenames)
        for file in files:
            properties = self.digester.eat(path + file)
            for prop in properties:
                json = prop.toJSON()
                collection.insert(json)

