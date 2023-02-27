from ..common.utils import check_required_keys
from ..repositories.managers.ingredient import IngredientManager
from ..repositories.managers.beverage import BeverageManager
from ..repositories.managers.order import OrderManager
from ..repositories.managers.size import SizeManager
from .base import BaseController


class OrderController(BaseController):
    manager = OrderManager
    __required_info = ('client_name', 'client_dni', 'client_address', 'client_phone', 'size_id')

    @classmethod
    def get_top_month(cls):
        return cls.handle_exception(lambda: cls.manager.get_month())

        
    @classmethod
    def get_top_costumers(cls):
        return cls.handle_exception(lambda: cls.manager.get_costumers())


    @staticmethod
    def  get_prices_from_products(products: list) -> float:
        price = 0
        if products:
            price = sum([product.price for product in products])
        return price


    @staticmethod
    def get_products_by_type(product_type: str, product_ids: list) -> list:
        if product_type == 'ingredients':
            return IngredientManager.get_by_id_list(product_ids)
        if product_type == 'beverages':
            return BeverageManager.get_by_id_list(product_ids)
        raise ValueError(f'Invalid product type: {product_type}')


    @classmethod
    def get_products_for_order(cls, order: dict, product_type: str) -> list:
        product_ids = order.pop(product_type, [])
        products = []
        if product_ids:
            products = cls.get_products_by_type(product_type, product_ids)
        return products
    

    @classmethod
    def calculate_order_price(cls, size_price: float, ingredients: list, beverages: list) -> float:
        ingredients_price = cls.get_prices_from_products(ingredients)
        beverages_price = cls.get_prices_from_products(beverages)
        total_price = size_price + ingredients_price + beverages_price
        return round(total_price, 2)


    @classmethod
    def create(cls, order: dict):
        current_order = order.copy()
        if not check_required_keys(cls.__required_info, current_order):
            return 'Invalid order payload', None

        size_id = current_order.get('size_id')
        size = SizeManager.get_by_id(size_id)

        if not size:
            return 'Invalid size for Order', None

        ingredients = cls.get_products_for_order(current_order, 'ingredients')
        beverages = cls.get_products_for_order(current_order, 'beverages')

        price = cls.calculate_order_price(size.get('price'), ingredients, beverages)
        order_with_price = {**current_order, 'total_price': price}
        
        return cls.handle_exception(lambda: cls.manager.create(order_with_price, ingredients, beverages))
