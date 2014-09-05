__author__ = 'artur'

from Main.Digester import Digester
from os import walk
from CodernityDB.database import Database


class Controller:
    db = ''
    digester = ''

    def __init__(self):
        self.db = Database("db/")
        if (self.db.exists("db/")):
            self.db.open("db/")
        else:
            self.db.create()
        self.digester = Digester()
        pass

    def process(self, path):

        files = []
        for (dirpath, dirnames, filenames) in walk(path):
            files.extend(filenames)
        i = 0
        for file in files:
            metadata = self.digester.eat(path + file)
            self.db.insert(dict(i=5))  #TODO: An issue with inserting complex data structures into CodernityDB
            i+=1

