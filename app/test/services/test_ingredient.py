from app.test.utils.functions import get_random_string, get_random_price


def test_create_ingredient_returns_successful_response_when_reciving_valid_ingredient(create_ingredient):
    created_ingredient = create_ingredient.json

    assert create_ingredient.status_code == 200
    assert '_id' in created_ingredient
    assert 'name' in created_ingredient
    assert 'price' in created_ingredient


def test_update_ingredient_returns_ingredient_with_current_changes_when_reciving_valid_ingredient(client, create_ingredient, ingredient_uri):
    current_ingredient = create_ingredient.json

    update_data = {
        **current_ingredient,
        'name': get_random_string(), 
        'price': get_random_price(1, 5)
    }
    response = client.put(ingredient_uri, json=update_data)

    assert response.status_code == 200
    updated_ingredient = response.json
    for param, value in update_data.items():
        assert updated_ingredient[param] == value


def test_get_ingredient_by_id_returns_correct_ingredient_when_reciving_valid_id(client, create_ingredient, ingredient_uri):
    current_ingredient = create_ingredient.json

    response = client.get(f'{ingredient_uri}id/{current_ingredient["_id"]}')

    assert response.status_code == 200
    returned_ingredient = response.json
    for param, value in current_ingredient.items():
        assert returned_ingredient[param] == value


def test_get_ingredients_returns_all_created_ingredients_when_reciving_valid_ingredients(client, create_ingredients, ingredient_uri):
    response = client.get(ingredient_uri)

    assert response.status_code == 200
    returned_ingredients = {ingredient['_id']: ingredient for ingredient in response.json}
    for ingredient in create_ingredients:
        assert ingredient['_id'] in returned_ingredients
