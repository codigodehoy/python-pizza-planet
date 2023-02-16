

def test_create_beverage_returns_successful_response_when_reciving_valid_beverage(create_beverage):
    created_beverage = create_beverage.json

    assert create_beverage.status_code == 200
    assert '_id' in created_beverage
    assert 'name' in created_beverage
    assert 'price' in created_beverage


def test_get_beverages_returns_all_created_sizes_when_reciving_valid_beverages(client, create_beverages, beverage_uri):
    response = client.get(beverage_uri)

    assert response.status_code == 200
    returned_beverages = {beverage['_id']: beverage for beverage in response.json}
    for beverage in create_beverages:
        assert beverage['_id'] in returned_beverages
