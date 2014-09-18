__author__ = 'artur'

from Main.Digester import Digester
from os import walk
from pymongo import MongoClient
import datetime

class Controller:
    db = ''
    digester = ''

    def __init__(self, dbHost, dbPort, dbName):
        client = MongoClient(dbHost, dbPort)
        self.db = client[dbName]
        self.digester = Digester()
        pass

    def process(self, path):
        files = []
        for (dirpath, dirnames, filenames) in walk(path):
            files.extend(filenames)
        i = 0

        post = {"author": "Mike",
                "text": "My first blog post!",
                "tags": ["mongodb", "python", "pymongo"],
                "date": datetime.datetime.utcnow()}
        posts=self.db.posts
        post_id=posts.insert(post)
        print(post_id)

        #for file in files:
        #    metadata = self.digester.eat(path + file)
        #    self.db.insert(metadata)  # TODO: An issue with inserting complex data structures into CodernityDB
        #    i += 1

