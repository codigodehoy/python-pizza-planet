from app.test.utils.functions import get_random_string, get_random_price

def test_create_beverage_returns_successful_response_when_reciving_valid_beverage(create_beverage):
    created_beverage = create_beverage.json

    assert create_beverage.status_code == 200
    assert '_id' in created_beverage
    assert 'name' in created_beverage
    assert 'price' in created_beverage


def test_update_beverage_returns_beverage_with_current_changes_when_reciving_beverage(client, create_beverage, beverage_uri):
    current_beverage = create_beverage.json

    update_data = {
        **current_beverage,
        'name': get_random_string(), 
        'price': get_random_price(1, 5)
    }
    response = client.put(f'{beverage_uri}update', json=update_data)

    assert response.status_code == 200
    updated_beverage = response.json
    for param, value in update_data.items():
        assert updated_beverage[param] == value


def test_get_beverage_by_id_returns_correct_beverage_when_reciving_valid_id(client, create_beverage, beverage_uri):
    beverage = create_beverage.json

    response = client.get(f'{beverage_uri}id/{beverage["_id"]}')
    returned_beverage = response.json

    assert response.status_code == 200
    for param, value in beverage.items():
        assert returned_beverage[param] == value


def test_get_beverages_returns_all_created_beverages_when_reciving_valid_beverages(client, create_beverages, beverage_uri):
    response = client.get(beverage_uri)

    assert response.status_code == 200
    returned_beverages = {beverage['_id']: beverage for beverage in response.json}
    for beverage in create_beverages:
        assert beverage['_id'] in returned_beverages
