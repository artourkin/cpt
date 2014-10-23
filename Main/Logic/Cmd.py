from Main.Common.Command import Command
from Main.Logic.Controller import Controller

__author__ = 'artur'

import cmd


class Cmd(cmd.Cmd):
    controller = Controller()

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.controller.setDaemon(True)
        self.controller.start()

    def do_ingest(self, args):
        ingest = Command("ingest", args)
        self.controller.queue.put(ingest)

    def do_change_collection(self, args):
        change_collection = Command("selectCollection", args)
        self.controller.queue.put(change_collection)
        print "Current collection is: " + args

    def do_delete_collection(self, args):
        clean_collection = Command("cleanCollection", args)
        self.controller.queue.put(clean_collection)
        print "Collection " + args + " cleaned"

    def do_add_filter(self, args):
        add_filter = Command("addFilter", args)
        self.controller.queue.put(add_filter)
        print "Filter: " + args + " added"

    def do_aggregate(self, args):
        aggregate = Command("aggregate", args)
        self.controller.queue.put(aggregate)
        print "Aggregating " + args

    def do_exit(self, args):
        return True

