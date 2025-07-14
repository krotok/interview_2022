import requests
import pytest

BASE_URL = 'http://localhost:5000'

def test_get_users():
    response = requests.get(f'{BASE_URL}/users')
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_add_user():
    new_user = {"id": 3, "name": "Charlie", "age": 35}
    response = requests.post(f'{BASE_URL}/users', json=new_user)
    assert response.status_code == 201
    assert response.json()["name"] == "Charlie"

def test_get_user_by_id():
    response = requests.get(f'{BASE_URL}/users/1')
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_user_not_found():
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