from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate_filter_company(cls, file):
        result = [company["nome_da_empresa"] for company in file]
        return Counter(result)

    @staticmethod
    # https://www.programiz.com/python-programming/methods/built-in/staticmethod
    def generate(products):
        min_date = min(product["data_de_fabricacao"] for product in products)
        max_date = min(
            (
                product["data_de_validade"]
                for product in products
                if product["data_de_validade"]
                > datetime.now().strftime("%Y-%m-%d")
            ),
            default=None,
        )
        most_common_company = Counter(
            product["nome_da_empresa"] for product in products
        ).most_common(1)[0][0]
        return (
            f"Data de fabricação mais antiga: {min_date}\n"
            f"Data de validade mais próxima: {max_date}\n"
            f"Empresa com mais produtos: {most_common_company}"
        )
