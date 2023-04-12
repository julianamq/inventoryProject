import json
from .importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_name: str) -> list:
        if not file_name.endswith('.json'):
            raise ValueError("Arquivo inválido")

        with open(file_name, 'r') as json_file:
            data = json.load(json_file)

        return data