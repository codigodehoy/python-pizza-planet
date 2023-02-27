from typing import Any, Optional, Tuple
from sqlalchemy.exc import SQLAlchemyError
from ..repositories.managers.base import BaseManager


class BaseController:
    manager: Optional[BaseManager] = None

    @staticmethod
    def handle_exception(query_fn):
        try:
            return query_fn(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)


    @classmethod
    def get_by_id(cls, _id: Any) -> Tuple[Any, Optional[str]]:
        return cls.handle_exception(lambda: cls.manager.get_by_id(_id))


    @classmethod
    def get_all(cls) -> Tuple[Any, Optional[str]]:
        return cls.handle_exception(lambda: cls.manager.get_all())


    @classmethod
    def create(cls, entry: dict) -> Tuple[Any, Optional[str]]:
        return cls.handle_exception(lambda: cls.manager.create(entry))


    @classmethod
    def update(cls, new_values: dict) -> Tuple[Any, Optional[str]]:
        try:
            _id = new_values.pop('_id', None)
            if not _id:
                return None, 'Error: No id was provided for update'
            return cls.manager.update(_id, new_values), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
