from app.common.http_methods import GET, POST
from flask import Blueprint

from .base import create_entity, get_entity, get_entity_by_id, handle_response
from ..controllers import OrderController

order = Blueprint('order', __name__)


@order.route('/create', methods=POST)
def create_order():
    return create_entity(OrderController)


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return get_entity_by_id(OrderController, _id)


@order.route('/', methods=GET)
def get_orders():
    return get_entity(OrderController)


# reports for the order
@order.route('/report/customers', methods=GET)
def get_report_best_costumers():
    data, error = OrderController.get_top_costumers()
    return handle_response(data, error)


@order.route('/report/month', methods=GET)
def get_report_best_month(): 
    data, error = OrderController.get_top_month()
    return handle_response(data, error)
