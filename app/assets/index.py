from typing import Dict


def get_id_with_sales(data: Dict[str, Dict[str, int]]) -> Dict[str, int]:
    id_with_sales = {}
    for id in data:
        client = data.get(id)
        id_with_sales[id] = client.get('sales')
    return id_with_sales


def get_key_best_products(data: dict):
    products = [key for key, value in data.items() if value ==
                max(data.values())]
    return products
