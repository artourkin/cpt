__author__ = 'artur'

from Main.Elements.Property import Property

class Utils:
    @staticmethod
    def toJSON(property):
        sources = []
        for s in property.source:
            sources.append(s.name + ";" + s.version)
        result = {"fileID": property.fileid,
                  "property_name": property.name,
                  "property_value": property.value,
                  "sources": sources
                  # TODO: refactor the project according to this json mapping. Sources will be put together
        }
        return result

    @staticmethod
    def toProperty(json):
        fileID=json["fileID"]
        property_name=json["property_name"]
        property_value=json["property_value"]
        sources=json["sources"]
        property = Property(fileID, property_name, property_value,sources)
        return property
