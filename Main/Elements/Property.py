__author__ = 'artur'


class Property:
    def __init__(self, uid, name, value):
        """

        :param uid:
        :param name:
        :param value:
        """
        self.uid = uid
        self.name = name
        self.value = value

    def tostring(self):
        """
        printing the fields of the Property class
        """
        result = ''.join(['uid: ', str(self.uid), ', name: ', self.name, ', value: ', self.value])
        print result
