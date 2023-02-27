from typing import Any, Optional, Tuple

from ..repositories.managers.orderDetail import OrderDetailManager
from .base import BaseController


class OrderDetailController(BaseController):
    manager = OrderDetailManager

    @classmethod
    def get_top_ingredient(cls) -> Tuple[Any, Optional[str]]:
        return cls.handle_exception(lambda: cls.manager.get_ingredient())
