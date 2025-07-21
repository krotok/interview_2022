import responses

@responses.activate
def test_get_user_by_id_with_decorator(api_client, existing_user_id):
    # Создаём фейковые данные
    fake_user = {
        "id": existing_user_id,
        "name": "Test User",
        "email": "test@example.com"
    }

    # Добавляем мок
    responses.add(
        responses.GET,
        f"https://jsonplaceholder.typicode.com/users/{existing_user_id}",
        json=fake_user,
        status=200
    )

    # Выполняем тест
    response = api_client.get(f"/users/{existing_user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == existing_user_id
    assert data["email"] == "test@example.com"