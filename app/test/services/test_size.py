from app.test.utils.functions import get_random_string, get_random_price


def test_create_size_returns_successful_response_when_reciving_valid_size(create_size):
    created_size = create_size.json

    assert create_size.status_code == 200
    assert '_id' in created_size
    assert 'name' in created_size
    assert 'price' in created_size


def test_update_ingredient_returns_ingredient_with_current_changes_when_reciving_valid_ingredient(client, create_size, size_uri):
    current_size = create_size.json

    update_data = {
        **current_size,
        'name': get_random_string(), 
        'price': get_random_price(1, 5)
    }
    response = client.put(f'{size_uri}update', json=update_data)

    assert response.status_code == 200
    updated_size = response.json
    for param, value in update_data.items():
        assert updated_size[param] == value


def test_get_size_by_id_returns_correct_size_when_reciving_valid_id(client, create_size, size_uri):
    size = create_size.json

    response = client.get(f'{size_uri}id/{size["_id"]}')
    returned_size = response.json

    assert response.status_code == 200
    for param, value in size.items():
        assert returned_size[param] == value


def test_get_sizes_returns_all_created_sizes_when_reciving_valid_sizes(client, create_sizes, size_uri):
    response = client.get(size_uri)

    assert response.status_code == 200
    returned_sizes = {size['_id']: size for size in response.json}
    for size in create_sizes:
        assert size['_id'] in returned_sizes
