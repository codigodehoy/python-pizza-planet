import calendar
from .interfaz import AbstractReport

class MonthReport(AbstractReport):
    
    def __init__(self):
        self.body = "month"
        
    def get_sales_by_each_product(self, orders):
      count_month = dict()
      for order in orders:
        orde_date = order.get('date')
        month = calendar.month_name[int(orde_date[5:7])]
        if month not in count_month:
            count_month[month] = 0
        count_month[month] += order.get('total_price')
      return count_month
    