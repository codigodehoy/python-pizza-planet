import pytest


def test_create_order_service(create_order):
    order = create_order.json
    pytest.assume(order['client_name'])
    pytest.assume(order['client_dni'])
    pytest.assume(order['client_address'])
    pytest.assume(order['client_phone'])
    pytest.assume(order['client_phone'])
    pytest.assume(order['size'])
    pytest.assume(order['total_price'])
    pytest.assume(order['detail'])

def test_get_order_by_id_service(client, create_order, order_uri):
    order = create_order.json
    response = client.get(f'{order_uri}id/{order["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_ingredient = response.json
    for param, value in order.items():
        pytest.assume(returned_ingredient[param] == value)

def test_get_orders_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_orders = {order['_id']: order for order in response.json}
    for order in create_orders:
        pytest.assume(order['_id'] in returned_orders)
