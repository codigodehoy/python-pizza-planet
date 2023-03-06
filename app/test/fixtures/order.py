import pytest

from ..utils.functions import (shuffle_list, get_random_sequence, get_random_string)


def client_data_mock() -> dict:
    return {
        'client_name': get_random_string(),
        'client_dni': get_random_sequence(),
        'client_address': get_random_string(),
        'client_phone': get_random_sequence()
    }


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def create_order(client, order_uri, create_ingredients, create_size, create_beverages) -> dict:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    size = create_size.json
    size_id = size['_id']
    order = client.post(f'{order_uri}create', json={
        **client_data_mock(),
        'size_id': size_id,
        'ingredients': ingredients,
        "beverages": beverages
    })
    return order


@pytest.fixture
def create_orders(client, order_uri, create_ingredients, create_sizes, create_beverages) -> list:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    sizes = [size.get('_id') for size in create_sizes]
    orders = []
    for _ in range(10):
        new_order = client.post(f'{order_uri}create', json={
            **client_data_mock(),
            'size_id': shuffle_list(sizes)[0],
            'ingredients': shuffle_list(ingredients)[:5],
            'beverages': shuffle_list(beverages)[:5]
        })
        orders.append(new_order.json)
    return orders
