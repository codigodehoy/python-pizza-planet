

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
