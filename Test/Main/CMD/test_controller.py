from unittest import TestCase

from Main.Common.Command import Command
from Main.Logic.Controller import Controller


__author__ = 'artur'


class TestController(TestCase): # TODO: Create tests for Controller
 #   def test_process(self):
 #       controller = Controller()
 #       controller.setDaemon(True)
 #       controller.start()
 #       cmd = Command("ingest", "Resources/FITS/")
 #       controller.queue.put(cmd)

#        cmd2 = Command("clear", "")
        # controller.queue.put(cmd2)

#        cmd1 = Command("stop", "")
#        controller.queue.put(cmd1)

#        controller.join()

        # Configurator().setup()
        #cntr = Controller()
        #cntr.ingest("Resources/FITS/")
    def test_ingest(self):
        controller = Controller()
        pass
        #controller.ingest("/data/FITS/govdocs_subset1")
