from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request
from collections import ChainMap
import operator

from ..assets import get_id_ith_sales
from ..assets import get_key_best_products
from ..factory import ReportFactory
from ..controllers import OrderController

report = Blueprint('report', __name__)

@report.route('/customers', methods=GET)
def get_report_customers():
    best_customers = []
    orders, error = OrderController.get_all()
    report = ReportFactory.build_report("customers")
    sales_by_each_client = report.get_sales_by_each_product(orders)
    client_dni_with_sales = get_id_ith_sales(sales_by_each_client)

    clients_sort = sorted(client_dni_with_sales.items(), key=operator.itemgetter(1), reverse=True)

    for client_dni, _ in clients_sort:
        best_customers.append(sales_by_each_client.get(client_dni))
        if len(best_customers) == 3:
            break;

    response = best_customers if not error else {'error': error}
    status_code = 200 if orders else 404 if not error else 400
    return jsonify(response), status_code

@report.route('/month', methods=GET)
def get_report_month(): 
    month_with_most_revenue = []
    orders, error = OrderController.get_all()
    report = ReportFactory.build_report("month")
    count_month = report.get_sales_by_each_product(orders)
    months_revenue= get_key_best_products(count_month)

    for month_revenue in months_revenue:
        month_with_most_revenue.append({'month': month_revenue, 'sales': round(count_month.get(month_revenue), 2)})
    
    response = month_with_most_revenue if not error else {'error': error}
    status_code = 200 if orders else 404 if not error else 400
    return jsonify(response), status_code

@report.route('/', methods=GET)
def get_report_popular_ingredient():
    popular_ingredients = []
    orders, error = OrderController.get_all()
    report = ReportFactory.build_report("ingredient")
    sales_by_each_ingredient = report.get_sales_by_each_product(orders)
    
    ingredient_id_with_sales = get_id_ith_sales(sales_by_each_ingredient)
    ingredients_most_required= get_key_best_products(ingredient_id_with_sales)

    for ingredient_id in ingredients_most_required:
        popular_ingredients.append(sales_by_each_ingredient[ingredient_id])
        
    response = popular_ingredients if not error else {'error': error}
    status_code = 200 if orders else 404 if not error else 400
    return jsonify(response), status_code
