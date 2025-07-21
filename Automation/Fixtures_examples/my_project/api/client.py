import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params)

    def post(self, endpoint, data=None, json=None):
        return requests.post(f"{self.base_url}{endpoint}", data=data, json=json)

    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}{endpoint}")
