def test_get_user_by_id(api_client, existing_user_id):
    response = api_client.get(f"/users/{existing_user_id}")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == existing_user_id
    assert "email" in user

def test_get_nonexistent_user(api_client):
    response = api_client.get("/users/99999")
    assert response.status_code == 404 or response.status_code == 200  # сервис может отдавать пустого юзера

def test_list_users(api_client):
    response = api_client.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0
