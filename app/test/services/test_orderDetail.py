

def test_get_best_ingredient_returns_top_ingredient_when_reciving_valid_order(client, order_detail_uri, create_orders):
    response = client.get(f'{order_detail_uri}report/ingredient')
    best_ingredients = response.json

    assert response.status_code == 200
    for best_ingredient in best_ingredients:
        assert 'ingredient_name' in best_ingredient
        assert 'price' in best_ingredient
        assert 'sales' in best_ingredient
