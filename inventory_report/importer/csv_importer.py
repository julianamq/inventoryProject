import csv
from .importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_name: str) -> list:
        if not file_name.endswith('.csv'):
            raise ValueError("Arquivo inválido")

        with open(file_name, newline='') as csvfile:
            data = list(csv.DictReader(csvfile))

        return data
