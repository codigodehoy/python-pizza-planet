from sqlalchemy.exc import SQLAlchemyError

from ..common.utils import check_required_keys
from ..repositories.managers.ingredient import IngredientManager
from ..repositories.managers.beverage import BeverageManager
from ..repositories.managers.order import OrderManager
from ..repositories.managers.size import SizeManager
from .base import BaseController


class OrderController(BaseController):
    manager = OrderManager
    __required_info = ('client_name', 'client_dni', 'client_address', 'client_phone', 'size_id')

    @staticmethod
    def  get_price(data_prices: list):
        prices = []
        for data_price in data_prices:
            prices.append(data_price.price)
        return prices

    @classmethod
    def calculate_order_price(cls, size_price: float, ingredients: list, beverages: list):
        if not ingredients and not size_price:
            return ''
        ingredients_price = cls.get_price(ingredients)
        beverages_price = cls.get_price(beverages)

        ingredients_and_size = sum(ingredients_price, size_price)
        total_price = sum(beverages_price, ingredients_and_size)
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

        ingredient_ids = current_order.pop('ingredients', [])
        beverage_ids = current_order.pop('beverages', [])
        try:
            ingredients = IngredientManager.get_by_id_list(ingredient_ids)
            beverages = BeverageManager.get_by_id_list(beverage_ids)
            price = cls.calculate_order_price(size.get('price'), ingredients, beverages)
            order_with_price = {**current_order, 'total_price': price}
            return cls.manager.create(order_with_price, ingredients, beverages), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
