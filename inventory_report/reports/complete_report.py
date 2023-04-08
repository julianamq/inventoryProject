from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        result = super().generate(list)
        products_stocked_by_company = cls.get_company(list)
        result += "\nProdutos estocados por empresa:\n"
        for c, q in products_stocked_by_company.items():
            result += f"- {c}: {q}\n"
        return result
