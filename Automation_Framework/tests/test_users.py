import pytest
import allure
from src.client import APIClient
from src.request_factory import RequestFactory
from src.auth_strategy import TokenAuth
from src.logger_util import logger

@pytest.fixture(scope="module")
def client():
    return APIClient()

@pytest.fixture(scope="module")
def factory():
    return RequestFactory(TokenAuth())

@allure.feature("User API")
@allure.story("GET /users/{id}")
def test_get_user(factory, client):
    logger.info("Testing GET /users/{id}")
    request = factory.create_get_user_request(123)
    response = client.send(request)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 123

@allure.feature("User API")
@allure.story("POST /users")
def test_create_user(factory, client):
    logger.info("Testing POST /users")
    user_data = {"name": "Alice", "email": "alice@example.com"}
    request = factory.create_create_user_request(user_data)
    response = client.send(request)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"