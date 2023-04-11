from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products_list):
        result = super().generate(products_list)
        # Chamando o método estático generate_filter_company da própria classe
        products_by_company = cls.generate_filter_company(products_list)
        # Adicionando a string 'Produtos estocados por empresa:' ao resultado
        result += "\nProdutos estocados por empresa:\n"
        for company, quantity in products_by_company.items():
            result += f"- {company}: {quantity}\n"
            return result
