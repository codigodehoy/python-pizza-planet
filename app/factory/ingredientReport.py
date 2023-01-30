from .interfaz import AbstractReport

class IngredientReport(AbstractReport):
    
    def __init__(self):
        self.body = "ingredient"
        
    def get_sales_by_each_product(self, orders):
      sales_by_each_ingredient = dict()
      for order in orders:
        detail_ingredients= order.get('detail')
        for detail in detail_ingredients:
          ingredient = detail.get('ingredient')
          ingredient_id = ingredient.get('_id')
          if ingredient_id not in sales_by_each_ingredient:
            sales_by_each_ingredient[ingredient_id] = {**ingredient, 'sales': 0}
          current_sale = sales_by_each_ingredient.get(ingredient_id)
          sales_by_each_ingredient[ingredient_id] =  {**ingredient, 'sales': current_sale.get('sales') + 1}
      return sales_by_each_ingredient