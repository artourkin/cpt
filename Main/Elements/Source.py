__author__ = 'artur'


class Source:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def echo(self):
        result = ""
        result += "source: " + self.name + ", source_version: " + self.version
        return result
