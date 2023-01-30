import pytest


def test_get_best_ingredient_service(client, report_uri, create_orders_for_report):
    best_ingredients = client.get(report_uri)
    pytest.assume(best_ingredients.status.startswith('200'))
    for best_ingredient in best_ingredients.json:
        pytest.assume(best_ingredient.get('sales') == 3)

def test_get_best_month_service(client, create_orders, report_month_uri):
    response = client.get(report_month_uri)
    pytest.assume(response.status.startswith('200'))
    for order in response.json:
        pytest.assume(order['month'])

def test_get_best_customers_service(client, create_orders, report_customers_uri):
    response = client.get(report_customers_uri)
    pytest.assume(response.status.startswith('200'))
    lenght = len(response.json)
    pytest.assume(lenght == 3)
