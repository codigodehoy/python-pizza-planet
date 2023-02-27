from sqlalchemy import func

from ..models.orderDetail import OrderDetail
from ..models.ingredient import Ingredient
from ..serializers import OrderDetailSerializer
from .base import BaseManager


class OrderDetailManager(BaseManager):
    model = OrderDetail
    serializer = OrderDetailSerializer

    @classmethod
    def get_ingredient(cls):
        sales = (
            cls.session.query(func.count(cls.model.ingredient_id).label('sales'), Ingredient.price, Ingredient.name)
            .join(Ingredient, Ingredient._id == cls.model.ingredient_id)
            .group_by(cls.model.ingredient_id, Ingredient.name)
            .order_by(func.count(cls.model.ingredient_id).desc())
            .all()
        )
        max_sales = max(row.sales for row in sales)
        result = [{'ingredient_name': row.name, "price": row.price, 'sales': row.sales } for row in sales if row.sales == max_sales]

        return result
