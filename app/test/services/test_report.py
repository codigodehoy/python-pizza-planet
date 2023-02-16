import pytest


def test_get_best_ingredient_returns_top_ingredient_when_sales_is_three(client, report_uri, create_orders_for_report):
    best_ingredients = client.get(report_uri)

    assert best_ingredients.status_code == 200
    for best_ingredient in best_ingredients.json:
        assert best_ingredient.get('sales') == 3


def test_get_best_month_returns_month_with_highest_total_sales_when_receiving_valid_orders(client, create_orders, report_month_uri):
    response = client.get(report_month_uri)

    assert response.status_code == 200
    for order in response.json:
        assert order['month']


def test_get_best_customers_returns_top_three_customers_by_number_of_orders(client, create_orders, report_customers_uri):
    response = client.get(report_customers_uri)

    assert response.status_code == 200
    assert len(response.json) == 3
    order_counts = [customer['sales'] for customer in response.json]
    assert order_counts == sorted(order_counts, reverse=True)
