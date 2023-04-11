import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path: str, relatory: str):
        with open(path, encoding="utf-8") as file:
            products = csv.DictReader(file, delimiter=",", quotechar='"')
            read_products = []
            for product in products:
                read_products.append(product)
                read_products = list(read_products)
                if relatory == "simples":
                    return SimpleReport.generate(read_products)
                elif relatory == "completo":
                    return CompleteReport.generate(read_products)
                raise ValueError("Erro ao ler o arquivo de relatório")

    @classmethod
    def read_archives(cls, path: str):
        if path.endswith("csv"):
            with open(path, encoding="utf-8") as file:
                aquivo_csv = csv.DictReader(file, delimiter=",", quotechar='"')
                read_products = []
                for product in aquivo_csv:
                    read_products.append(product)
                    read_products = list(read_products)
                    return read_products
        elif path.endswith("json"):
            with open(path) as file:
                content = file.read()
                read = json.loads(content)
                return read
