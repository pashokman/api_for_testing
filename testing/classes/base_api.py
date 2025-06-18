import requests


class BaseAPI:
    def __init__(self, headers=None):
        self.base_url = "http://127.0.0.1:8000/"
        self.headers = headers or {}

    def get(self, endpoint: str, params=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.get(url, params=params, headers={**self.headers, **(headers or {})})
        return response

    def post(self, endpoint: str, data=None, json=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.post(url, data=data, json=json, headers={**self.headers, **(headers or {})})
        return response

    def put(self, endpoint: str, data=None, json=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.put(url, data=data, json=json, headers={**self.headers, **(headers or {})})
        return response

    def patch(self, endpoint: str, data=None, json=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.patch(url, data=data, json=json, headers={**self.headers, **(headers or {})})
        return response

    def delete(self, endpoint: str, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.delete(url, headers={**self.headers, **(headers or {})})
        return response
