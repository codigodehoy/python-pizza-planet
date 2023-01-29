from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request
from collections import ChainMap
import calendar
import operator

from ..controllers import OrderController

report = Blueprint('report', __name__)

@report.route('/customers', methods=GET)
def get_report_customers():
    sales_by_each_client = dict()
    client_dni_with_sales = dict()
    best_customers = []
    orders, error = OrderController.get_all()
    for order in orders:
        client_dni = order.get('client_dni')
        if client_dni not in sales_by_each_client:
            sales_by_each_client[client_dni] = {'client_name': order.get('client_name'), 'sales': 0}
        current_sale = sales_by_each_client.get(client_dni)
        sales_by_each_client[client_dni] = {'client_name': order.get('client_name'), 'sales': current_sale.get('sales') +1}

    for client_dni in sales_by_each_client:
        client = sales_by_each_client.get(client_dni)
        client_dni_with_sales[client_dni]=client.get('sales')

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
    count_month = dict()
    month_with_most_revenue = []
    orders, error = OrderController.get_all()
    for order in orders:
        orde_date = order.get('date')
        month = calendar.month_name[int(orde_date[5:7])]
        if month not in count_month:
            count_month[month] = 0
        count_month[month] += order.get('total_price')

    months_revenue= [key for key, value in count_month.items() if value == max(count_month.values())]
    for month_revenue in months_revenue:
        month_with_most_revenue.append({'month': month_revenue, 'sales': round(count_month.get(month_revenue), 2)})
    
    response = month_with_most_revenue if not error else {'error': error}
    status_code = 200 if orders else 404 if not error else 400
    return jsonify(response), status_code

@report.route('/', methods=GET)
def get_report_popular_ingredient():
    sales_by_each_ingredient = dict()
    ingredient_id_with_sales = dict()
    popular_ingredients = []
    orders, error = OrderController.get_all()
    for order in orders:
        detail_ingredients= order.get('detail')
        for detail in detail_ingredients:
            ingredient = detail.get('ingredient')
            ingredient_id = ingredient.get('_id')
            if ingredient_id not in sales_by_each_ingredient:
                sales_by_each_ingredient[ingredient_id] = {**ingredient, 'sales': 0}
            current_sale = sales_by_each_ingredient.get(ingredient_id)
            sales_by_each_ingredient[ingredient_id] =  {**ingredient, 'sales': current_sale.get('sales') + 1}
    
    for ingredient_id in sales_by_each_ingredient:
        ingredient = sales_by_each_ingredient.get(ingredient_id)
        ingredient_id_with_sales[ingredient_id]=ingredient.get('sales')

    ingredients_most_required= [key for key, value in ingredient_id_with_sales.items() if value == max(ingredient_id_with_sales.values())]

    for ingredient_id in ingredients_most_required:
        popular_ingredients.append(sales_by_each_ingredient[ingredient_id])
        
    response = popular_ingredients if not error else {'error': error}
    status_code = 200 if orders else 404 if not error else 400
    return jsonify(response), status_code
