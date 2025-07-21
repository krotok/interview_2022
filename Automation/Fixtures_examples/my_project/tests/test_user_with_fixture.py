def test_get_user_by_id_with_fixture(api_client, mock_responses):
    fake_user = {
        "id": 2,
        "name": "Fixture User",
        "email": "fixture@example.com"
    }

    mock_responses.add(
        method=mock_responses.GET,
        url="https://jsonplaceholder.typicode.com/users/2",
        json=fake_user,
        status=200
    )

    response = api_client.get("/users/2")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 2
    assert data["email"] == "fixture@example.com"
