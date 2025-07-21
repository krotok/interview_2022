import pytest
from Automation.Fixtures_examples.my_project.api.client import APIClient
import responses

@pytest.fixture(scope="session")
def base_url():
    """Базовый URL для всех тестов."""
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def api_client(base_url):
    """Клиент для общения с REST API."""
    return APIClient(base_url)

@pytest.fixture
def existing_user_id():
    """Фикстура с существующим ID пользователя."""
    return 1

@pytest.fixture
def mock_responses():
    with responses.RequestsMock() as rsps:
        yield rsps