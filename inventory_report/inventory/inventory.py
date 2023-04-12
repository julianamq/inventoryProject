from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json


class Inventory:
    @classmethod
    def import_data(cls, path: str, relatory: str):
        list_products = []
        if path.endswith("csv"):
            list_products = Inventory.read_archives(path)                           
        elif path.endswith("json"):
            list_products = Inventory.read_json(path)

        if relatory == "simples":
            return SimpleReport.generate(list_products)
        elif relatory == "completo":
            return CompleteReport.generate(list_products)
        raise ValueError("Erro ao ler o arquivo de relatório")

    def read_archives(path):
        with open(path, "r") as file:
            arq_csv = csv.DictReader(file, delimiter=",", quotechar='"')
            read_products = []
            for product in arq_csv:
                read_products.append(product)
            return read_products

    def read_json(path):
        with open(path) as file:
            read = json.load(file)
        return read
