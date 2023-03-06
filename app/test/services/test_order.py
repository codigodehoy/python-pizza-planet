

def test_create_order_returns_successful_response_when_reciving_valid_order(create_order):
    created_order = create_order.json

    assert create_order.status_code == 200
    assert 'client_name' in created_order
    assert 'client_dni' in created_order
    assert 'client_address' in created_order
    assert 'client_phone' in created_order
    assert 'size' in created_order
    assert 'total_price' in created_order
    assert 'detail' in created_order


def test_get_order_by_id_returns_correct_order_when_reciving_valid_id(client, create_order, order_uri):
    order = create_order.json

    response = client.get(f'{order_uri}id/{order["_id"]}')
    returned_order = response.json

    assert response.status_code == 200
    for param, value in order.items():
        assert returned_order[param] == value


def test_get_orders_returns_all_created_orders_when_reciving_valid_orders(client, create_orders, order_uri):
    response = client.get(order_uri)

    assert response.status_code == 200
    returned_orders = {order['_id']: order for order in response.json}
    for order in create_orders:
        assert order['_id'] in returned_orders


def test_get_best_month_returns_month_with_highest_total_sales_when_receiving_valid_orders(client, create_orders, order_uri):
    response = client.get(f'{order_uri}report/month')
    returned_report_months = response.json

    assert response.status_code == 200
    for returned_report_month in returned_report_months:
        assert 'month' in returned_report_month
        assert 'total_sales' in returned_report_month


def test_get_best_customers_returns_top_three_customers_by_number_of_orders(client, create_orders, order_uri):
    response = client.get(f'{order_uri}report/customers')

    assert response.status_code == 200
    order_counts = [customer['sales'] for customer in response.json]
    assert order_counts == sorted(order_counts, reverse=True)
