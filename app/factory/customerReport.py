from .interfaz import AbstractReport

class CustomerReport(AbstractReport):
    
    def __init__(self):
        self.body = "customers"
        
    def get_sales_by_each_product(self, orders):
      sales_by_each_client = dict()
      for order in orders:
        client_dni = order.get('client_dni')
        if client_dni not in sales_by_each_client:
            sales_by_each_client[client_dni] = {'client_name': order.get('client_name'), 'sales': 0}
        current_sale = sales_by_each_client.get(client_dni)
        sales_by_each_client[client_dni] = {'client_name': order.get('client_name'), 'sales': current_sale.get('sales') +1}
      return sales_by_each_client