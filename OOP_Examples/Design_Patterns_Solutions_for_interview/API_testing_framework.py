# Полноценный API тестовый фреймворк с:
# - Strategy, Factory, Singleton, Builder, Decorator
# - Pytest, Allure, логгированием
# - Мок-сервером Flask
# - Jenkins-ready структурой
# - Locust генератором нагрузки по тем же сценариям

## ⚙️ Запуск в Jenkins
# CI-процесс в Jenkins включает:
# 1. Установку зависимостей
# 2. Запуск мок-сервера
# 3. Юнит + API тесты
# 4. Нагрузочное тестирование через JMeter
# 5. Публикацию отчёта Allure
#
# ## 📊 Мониторинг с Grafana
# 1. JMeter пишет метрики в InfluxDB через Backend Listener
# 2. Grafana подключается к InfluxDB и показывает данные
#
# ## 🧱 Паттерны проектирования
# - **Singleton** → `Config`
# - **Strategy** → `AuthStrategy`
# - **Factory Method** → `RequestFactory`
# - **Builder** → `RequestBuilder`
# - **Logger** → `logger_util`
#
# ## 📎 Зависимости
# - Python: `pytest`, `requests`, `allure-pytest`, `flask`
# - Jenkins: `allure`, `jmeter`
# - JMeter: GUI для генерации `.jmx`
# - Grafana + InfluxDB: для визуализации метрик


import requests
import json
import pytest
import logging
import allure
from typing import Dict
from flask import Flask, jsonify, request as flask_request
from threading import Thread
import os
from locust import HttpUser, task, between

# -------------------- ЛОГГЕР --------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("TestFramework")

# -------------------- МОК-СЕРВЕР --------------------
app = Flask(__name__)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify({"id": user_id, "name": f"User{user_id}"}), 200

@app.route("/users", methods=["POST"])
def create_user():
    data = flask_request.json
    return jsonify({"id": 999, **data}), 201

def run_mock_server():
    app.run(port=5001)

if os.getenv("MOCK", "1") == "1":
    Thread(target=run_mock_server, daemon=True).start()

# -------------------- SINGLETON --------------------
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.base_url = os.getenv("API_URL", "http://localhost:5001")
            cls._instance.token = os.getenv("API_TOKEN", "test_token")
        return cls._instance

# -------------------- STRATEGY --------------------
class AuthStrategy:
    def apply(self, headers: Dict[str, str]) -> Dict[str, str]:
        return headers

class TokenAuth(AuthStrategy):
    def apply(self, headers):
        headers["Authorization"] = f"Bearer {Config().token}"
        return headers

class NoAuth(AuthStrategy):
    def apply(self, headers):
        return headers

# -------------------- DECORATOR --------------------
def log_step(func):
    def wrapper(*args, **kwargs):
        logger.info(f"[STEP] {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# -------------------- BUILDER --------------------
class RequestBuilder:
    def __init__(self):
        self._method = "GET"
        self._url = ""
        self._headers = {}
        self._body = None

    def with_method(self, method: str):
        self._method = method
        return self

    def with_url(self, path: str):
        self._url = f"{Config().base_url}{path}"
        return self

    def with_headers(self, headers: Dict[str, str]):
        self._headers.update(headers)
        return self

    def with_body(self, body: Dict):
        self._body = body
        return self

    def build(self):
        return {
            "method": self._method,
            "url": self._url,
            "headers": self._headers,
            "json": self._body
        }

# -------------------- FACTORY --------------------
class RequestFactory:
    def __init__(self, auth_strategy: AuthStrategy):
        self.auth_strategy = auth_strategy

    def create_get_user_request(self, user_id: int):
        headers = self.auth_strategy.apply({"Content-Type": "application/json"})
        return RequestBuilder()\
            .with_method("GET")\
            .with_url(f"/users/{user_id}")\
            .with_headers(headers)\
            .build()

    def create_create_user_request(self, user_data: Dict):
        headers = self.auth_strategy.apply({"Content-Type": "application/json"})
        return RequestBuilder()\
            .with_method("POST")\
            .with_url("/users")\
            .with_headers(headers)\
            .with_body(user_data)\
            .build()

# -------------------- КЛИЕНТ --------------------
class APIClient:
    def send(self, request: Dict):
        response = requests.request(
            method=request["method"],
            url=request["url"],
            headers=request["headers"],
            json=request.get("json")
        )
        logger.info(f"[RESPONSE] {response.status_code} - {response.text}")
        return response

# -------------------- PYTEST --------------------
@pytest.fixture(scope="module")
def client():
    return APIClient()

@pytest.fixture(scope="module")
def factory():
    return RequestFactory(TokenAuth())

@allure.feature("User API")
@allure.story("GET /users/{id}")
@log_step
def test_get_user(factory, client):
    request = factory.create_get_user_request(123)
    response = client.send(request)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 123

@allure.feature("User API")
@allure.story("POST /users")
@log_step
def test_create_user(factory, client):
    user_data = {"name": "Alice", "email": "alice@example.com"}
    request = factory.create_create_user_request(user_data)
    response = client.send(request)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"

# -------------------- LOCUST --------------------
class LoadTestUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.headers.update(TokenAuth().apply({"Content-Type": "application/json"}))

    @task
    def load_get_user(self):
        self.client.get("/users/123")

    @task
    def load_create_user(self):
        payload = {"name": "Locust", "email": "load@test.com"}
        self.client.post("/users", json=payload)
