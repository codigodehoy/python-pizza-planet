from app.common.http_methods import GET, POST, PUT
from flask import Blueprint

from .base import create_entity, get_entity, update_entity, get_entity_by_id
from ..controllers.beverage import BeverageController

beverage = Blueprint('beverage', __name__)


@beverage.route('/create', methods=POST)
def create_beverage():
    return create_entity(BeverageController)


@beverage.route('/update', methods=PUT)
def update_beverage():
    return update_entity(BeverageController)


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return get_entity_by_id(BeverageController, _id)


@beverage.route('/', methods=GET)
def get_beverages():
    return get_entity(BeverageController)
