from unittest import TestCase
from Main.Common.Command import Command
from Main.Common.Configurator import Configurator
from Main.Common.Params import *
from Main.Controller import Controller

__author__ = 'artur'


class TestController(TestCase):
    def test_process(self):
        controller = Controller()
        controller.setDaemon(True)
        controller.start()
        cmd = Command("ingest", "Resources/FITS/")
        controller.queue.put(cmd)



        cmd2 = Command("clear", "")
      #  controller.queue.put(cmd2)

        cmd1 = Command("stop", "")
        controller.queue.put(cmd1)

        controller.join()

        # Configurator().setup()
        #cntr = Controller()
        #cntr.ingest("Resources/FITS/")
