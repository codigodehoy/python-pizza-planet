from .customerReport import CustomerReport
from .monthReport import MonthReport
from .ingredientReport import IngredientReport

class ReportFactory:
    
    @staticmethod
    def build_report(plan):
        try:
            if plan == "customers":
                return CustomerReport()
            elif plan == "month":
                return MonthReport()
            elif plan == "ingredient":
                return IngredientReport()
            raise AssertionError("Report type is not valid.")
        except AssertionError as e:
            print(e)