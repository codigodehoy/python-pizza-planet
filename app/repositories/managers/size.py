from ..models.size import Size
from ...factory.serializers import SizeSerializer
from ..managers.base import BaseManager

class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer
