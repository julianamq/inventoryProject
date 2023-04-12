import xml.etree.ElementTree as ET
from .importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".xml" not in path:  # se houver erro será levantado
            raise ValueError("Arquivo inválido")
        types = []
        with open(path) as file:
            tree = ET.parse(file)
            item = tree.getroot()
            for child in item:
                item = {}
                for items in child:
                    item[items.tag] = items.text
                types.append(item)
        return types
