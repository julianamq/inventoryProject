from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json


class Inventory:
    @classmethod
    def import_data(cls, path: str, relatory: str):
        with open(path, encoding="utf-8") as file:
            products = csv.DictReader(file, delimiter=",", quotechar='"')
            list_products = []
            for product in products:
                list_products.append(product)
            list_products = list(list_products)

        if relatory == "simples":
            return SimpleReport.generate(list_products)
        elif relatory == "completo":
            return CompleteReport.generate(list_products)
        raise ValueError("Erro ao ler o arquivo de relatório")

    @classmethod
    def read_archives(path):
        with open(path, "read") as file:
            arq_csv = csv.DictReader(file, delimiter=",", quotechar='"')
            read_products = []
            for product in arq_csv:
                read_products.append(product)
                read_products = list(read_products)
        return read_products

    def read_json(path):
        with open(path) as file:
            read = json.load(file)
        return read
