from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from .base import create_entity, get_entity, update_entity, get_entity_by_id
from ..controllers import OrderController

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    return create_entity(OrderController)


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return get_entity_by_id(OrderController, _id)


@order.route('/', methods=GET)
def get_orders():
    return get_entity(OrderController)
