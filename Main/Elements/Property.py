from Main.Elements.Source import Source

__author__ = 'artur'


class Property:
    def __init__(self, fileid, name, value, source):
        """
        :param fileid:
        :param name:
        :param value:
        :param source:
        """
        self.fileid = fileid
        self.name = name
        self.value = value
        self.source = []

        if isinstance(source, Source):
            self.source.append(source)
        else:
            for s in source:
                source_name, source_version = s.split(";")
                self.source.append(Source(source_name, source_version))

    def echo(self):
        """
        printing the fields of the Property class
        """
        result = ""
        result += "fileid: " + str(
            self.fileid) + ", name: " + self.name + ", value: " + self.value + " " + self.source.echo()
        print(result)

    def toJSON(self):
        sources = []
        for s in self.source:
            sources.append(s.name + ";" + s.version)
        result = {"fileID": self.fileid,
                  "property_name": self.name,
                  "property_value": self.value,
                  "sources": sources
                  #TODO: refactor the project according to this json mapping. Sources will be put together
        }
        return result

