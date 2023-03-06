from typing import List
import calendar
from sqlalchemy import func

from ..models.order import Order
from ..models.ingredient import Ingredient
from ..models.beverage import Beverage
from ..models.orderDetail import OrderDetail
from ..models.beverageDetail import BeverageDetail
from ...factory.serializers import OrderSerializer
from ..managers.base import BaseManager


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer
 
    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)

        order_details = [OrderDetail(order_id=new_order._id, ingredient_id=ingredient._id, ingredient_price=ingredient.price) for ingredient in ingredients]
        cls.session.add_all(order_details)

        beverage_details = [BeverageDetail(order_id=new_order._id, beverage_id=beverage._id, beverage_price=beverage.price) for beverage in beverages]
        cls.session.add_all(beverage_details)

        cls.session.commit()
        return cls.serializer().dump(new_order)


    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')


    @classmethod
    def get_month(cls):
        months = (
            cls.session.query(func.sum(cls.model.total_price).label('total_sales'), func.strftime('%m', cls.model.date).label("month"))
            .group_by(func.strftime('%m', cls.model.date))
            .order_by((func.sum(cls.model.total_price)).desc())
            .limit(1)
            .all()
        )

        result = [{'month': calendar.month_name[int(row.month)], "total_sales": round(row.total_sales, 2) } for row in months]
        return result
    

    @classmethod
    def get_costumers(cls):
        customers = (
            cls.session.query(func.count(cls.model.client_dni).label('sales'), cls.model.client_name)
            .group_by(cls.model.client_dni)
            .order_by((func.count(cls.model.client_dni)).desc())
            .limit(3)
            .all()
        )

        result = [{'client_name': row.client_name, "sales": row.sales } for row in customers]
        return result
