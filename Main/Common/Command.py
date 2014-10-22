__author__ = 'artur'


class Command:
    def __init__(self):
        pass

    name = ""
    args = []

    def __init__(self, name, args):
        self.name = name
        if not isinstance(args, list):
            self.args = [args]
        else:
            self.args = args

    def echo(self):
        print(self.name + " " + self.args)
