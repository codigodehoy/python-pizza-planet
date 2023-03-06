from app.common.http_methods import GET
from flask import Blueprint

from .base import handle_response
from ..controllers import OrderDetailController

order_detail = Blueprint('order_detail', __name__)


@order_detail.route('/report/ingredient', methods=GET)
def get_report_best_ingredient():
    data, error = OrderDetailController.get_top_ingredient()
    return handle_response(data, error)
