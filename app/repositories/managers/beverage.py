from typing import Sequence

from ..models.beverage import Beverage
from ..serializers import BeverageSerializer
from ..managers.base import BaseManager

class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []