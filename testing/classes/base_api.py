from testing.utils.logs.logger_with_context import get_logger_with_context
from typing import Any

import requests


class BaseAPI:
    def __init__(self, headers=None, request=None):
        self.base_url = "http://127.0.0.1:8000/"
        self.headers = headers or {}
        self.logger = get_logger_with_context(request)

    def get(self, endpoint: str, params=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        if self.logger:
            self.logger.info(f"GET {url} params={params}, headers={headers}")
        response = requests.get(url, params=params, headers={**self.headers, **(headers or {})})
        return response

    def post(self, endpoint: str, data=None, json=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        if self.logger:
            self.logger.info(f"POST {url} json={json}, headers={headers}")
        response = requests.post(url, data=data, json=json, headers={**self.headers, **(headers or {})})
        return response

    def put(self, endpoint: str, data=None, json=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        if self.logger:
            self.logger.info(f"POST {url} json={json}, headers={headers}")
        response = requests.put(url, data=data, json=json, headers={**self.headers, **(headers or {})})
        return response

    def patch(self, endpoint: str, data=None, json=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        if self.logger:
            self.logger.info(f"POST {url} json={json}, headers={headers}")
        response = requests.patch(url, data=data, json=json, headers={**self.headers, **(headers or {})})
        return response

    def delete(self, endpoint: str, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        if self.logger:
            self.logger.info(f"POST {url} headers={headers}")
        response = requests.delete(url, headers={**self.headers, **(headers or {})})
        return response
