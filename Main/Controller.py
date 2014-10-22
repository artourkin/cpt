from Queue import Queue
import threading

from os import walk
from Main.Common.Configurator import Configurator

from Main.Digester import Digester
from Main.Utils.MongoUtils import MongoUtils

__author__ = 'artur'


class Controller(threading.Thread):
    queue = Queue()
    jobs = []
    filter = {}

    def __init__(self):
        super(Controller, self).__init__()
        Configurator().setup()
        self.signal = True

    def run(self):
        while self.signal:
            command = self.queue.get()
            self.execute(command)

    def execute(self, command):
        job = threading.Thread(target=self.commands[command.name], args=(self, command.args,))
        self.jobs.append(job)
        job.start()
        #job.join()  # This affects serial or parallel execution of jobs


    # The next section contains all the possible jobs.
    # The job name should be included in the commands dictionary in the end.

    def ingest(self, args):
        digester = Digester("Resources/fits.cfg")
        files = []
        if isinstance(args, list):
            path = args[0]
        else:
            path = args
        for (dirpath, dirnames, filenames) in walk(path):
            filenames = [dirpath + "/" + x for x in filenames]
            files.extend(filenames)
        for file in files:
            properties = []
            try:
                properties = digester.eat(file)
            except:
                pass
            for prop in properties:
                MongoUtils.insert(prop)
        return "done"

    def cleanCollection(self, args):
        MongoUtils.cleanCollection(args[0])
        return "done"

    def selectCollection(self, args):
        Configurator().selectCollection(
            args[0])  # TODO: be aware, if some operation on the current collection happening,
        # changing a collection name will DEFINITELY affect this operation

    def stopThreads(self, args):
        self.signal = False
        return "done"

    def addFilter(self, args):
        args = "".join(args).split(" ")
        if isinstance(args, list) and args != []:
            self.filter[args[0]] = args[1]
        return "done"

    def aggregate(self, args):
        groupby = {"_id": "$" + args[0], "count": {"$sum": 1}}
        result = MongoUtils.aggregate(self.filter, groupby)
        print result

    commands = {"ingest": ingest,
                "stop": stopThreads,
                "cleanCollection": cleanCollection,
                "selectCollection": selectCollection,
                "addFilter": addFilter,
                "aggregate": aggregate}




