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
        self.source = source

    def __init__(self, fileid, name, value, source_name, source_version):
        self.fileid = fileid
        self.name = name
        self.value = value
        self.source = Source(source_name, source_version)

    def echo(self):
        """
        printing the fields of the Property class
        """
        result = ""
        result += "fileid: " + str(
            self.fileid) + ", name: " + self.name + ", value: " + self.value + " " + self.source.echo()
        print(result)

    def toJSON(self):
        result = {"fileID": self.fileid,
                  "property_name": self.name,
                  "property_value": self.value,
                  "source_name": self.source.name,
                  "source_version": self.source.version
        }
        return result

