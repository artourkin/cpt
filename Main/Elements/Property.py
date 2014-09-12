__author__ = 'artur'


class Property:
    def __init__(self, uid, name, value, source):
        """
        :param uid:
        :param name:
        :param value:
        :param source:
        """
        self.uid = uid
        self.name = name
        self.value = value
        self.source = source

    def echo(self):
        """
        printing the fields of the Property class
        """
        result = ""
        result += "uid: " + str(self.uid) + ", name: " + self.name + ", value: " + self.value + " " + self.source.echo()
        print(result)
