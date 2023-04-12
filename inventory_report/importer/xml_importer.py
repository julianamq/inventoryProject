import xml.etree.ElementTree as ET
from .importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_name: str) -> list:
        if not file_name.endswith('.xml'):
            raise ValueError("Arquivo inválido")

        tree = ET.parse(file_name)
        root = tree.getroot()

        data = []
        for item in root.findall('item'):
            product = {}
            for child in item:
                product[child.tag] = child.text
            data.append(product)

        return data