from typing import Sequence

from ..models.ingredient import Ingredient
from ...factory.serializers import IngredientSerializer
from ..managers.base import BaseManager

class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []