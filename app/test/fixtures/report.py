import pytest

from ..utils.functions import (shuffle_list, get_random_sequence, get_random_string)

@pytest.fixture
def report_uri():
    return '/report/'

@pytest.fixture
def report_month_uri():
    return '/report/month'

@pytest.fixture
def report_customers_uri():
    return '/report/customers'

@pytest.fixture
def create_orders_for_report(client, order_uri, create_ingredients, create_sizes) -> list:
    beverages = []
    orders = [] 
    orders.append(client.post(order_uri, json={
        'client_name': 'David', 
        'client_dni': '25465',
        'client_address': get_random_string(),
        'client_phone': get_random_sequence(), 
        'size_id': 3,
        'ingredients': [1 ,2, 3], 
        'beverages': beverages
    }).json)

    orders.append(client.post(order_uri, json={
        'client_name': 'David', 
        'client_dni': '25465',
        'client_address': get_random_string(),
        'client_phone': get_random_sequence(), 
        'size_id': 2,
        'ingredients': [2, 4, 1], 
        'beverages': shuffle_list(beverages)[:5]
    }).json)

    orders.append(client.post(order_uri, json={
        'client_name': 'Pedro', 
        'client_dni': '55556',
        'client_address': get_random_string(),
        'client_phone': get_random_sequence(), 
        'size_id': 1,
        'ingredients': [3 ,1, 5], 
        'beverages': shuffle_list(beverages)[:5]
    }).json)

    return orders
