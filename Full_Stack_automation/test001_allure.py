import requests
import pytest
import allure

BASE_URL = 'http://localhost:5000'

@allure.feature("User Management")
@allure.story("Получение списка пользователей")
def test_get_users():
    with allure.step("GET /users"):
        response = requests.get(f'{BASE_URL}/users')
        assert response.status_code == 200
        assert len(response.json()) > 0

@allure.feature("User Management")
@allure.story("Добавление пользователя")
def test_add_user():
    new_user = {"id": 3, "name": "Charlie", "age": 35}
    with allure.step("POST /users"):
        response = requests.post(f'{BASE_URL}/users', json=new_user)
        assert response.status_code == 201
        assert response.json()["name"] == "Charlie"

@allure.feature("User Management")
@allure.story("Получение пользователя по ID")
def test_get_user_by_id():
    with allure.step("GET /users/1"):
        response = requests.get(f'{BASE_URL}/users/1')
        assert response.status_code == 200
        assert response.json()["id"] == 1

@allure.feature("User Management")
@allure.story("Ошибка при запросе несуществующего пользователя")
def test_user_not_found():
    with allure.step("GET /users/999"):
        response = requests.get(f'{BASE_URL}/users/999')
        assert response.status_code == 404

try:
    test_get_users()
except:
    pass
try:
    test_add_user()
except:
    pass
try:
    test_get_user_by_id()
except:
    pass
try:
    test_user_not_found()
except:
    pass