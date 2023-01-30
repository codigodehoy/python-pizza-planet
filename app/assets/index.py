 
def get_id_ith_sales(dictionaty: dict)-> dict:
  id_with_sales = dict()
  for id in dictionaty:
    client = dictionaty.get(id)
    id_with_sales[id]=client.get('sales')
  return id_with_sales

def get_key_best_products(dictionary: dict ):
  products= [key for key, value in dictionary.items() if value == max(dictionary.values())]
  return products
