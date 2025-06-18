from testing.classes.base_api import BaseAPI
from testing.utils.generators.user_generator import generate_user


class User(BaseAPI):

    def __init__(self):
        super().__init__()
        self.user_obj = generate_user(password_length=8)
        self.bearer_token = None
        self.user_id = None

    def create_user(self):
        response = self.post(endpoint="users/register", json=self.user_obj)
        if response.status_code == 200:
            self.user_id = response.json()["id"]
        return response

    def auth(self):
        json = {"username": f"{self.user_obj.get('username')}", "password": f"{self.user_obj.get('password')}"}
        response = self.post(endpoint="auth/login", json=json)
        self.bearer_token = response.json()["access_token"]
        self.headers = {"Authorization": f"Bearer {self.bearer_token}"}
        return response

    def get_me(self):
        response = self.get(endpoint="users/me", headers=self.headers)
        return response
