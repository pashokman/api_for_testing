from testing.classes.base_api import BaseAPI
from testing.utils.generators.user_generator import generate_user


class User(BaseAPI):

    def __init__(self, headers=None, request=None):
        super().__init__(headers=headers, request=request)
        self.user_obj = None
        self.bearer_token = None
        self.user_id = None

    def create_user(self):
        response = None
        try:
            if self.user_obj is None:
                self.user_obj = generate_user(password_length=8)
            username = self.user_obj.get("username")
            if self.logger:
                if username is not None:
                    self.logger.info(f"Registering user: {username}")
                else:
                    self.logger.info("Registering user without username field")
            response = self.post(endpoint="users/register", json=self.user_obj)
            if response.status_code == 200:
                self.user_id = response.json()["id"]
                self.logger.info(f"Registering user: {username}, response json: {response.json()}")
            else:
                self.logger.error(f"Registering user: {username}, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in create_user: {e}")
        finally:
            return response

    def auth(self):
        response = None
        try:
            username = self.user_obj["username"]
            if self.logger:
                self.logger.info(f"Authenticating user: {username}")
            json = {"username": f"{self.user_obj.get('username')}", "password": f"{self.user_obj.get('password')}"}
            response = self.post(endpoint="auth/login", json=json)
            if response.status_code == 200:
                self.bearer_token = response.json()["access_token"]
                self.headers = {"Authorization": f"Bearer {self.bearer_token}"}
                self.logger.info(f"Authenticating user: {username}, response json: {response.json()}")
            else:
                self.logger.error(f"Authenticating user: {username}, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in auth: {e}")
        finally:
            return response

    def get_me(self):
        response = None
        try:
            username = self.user_obj["username"]
            if self.logger:
                self.logger.info(f"Getting user: {username} profile")
            response = self.get(endpoint="users/me", headers=self.headers)
            if response.status_code == 200:
                self.logger.info(f"Getting user: {username} profile, response json: {response.json()}")
            else:
                self.logger.error(f"Getting user: {username} profile, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in get_me: {e}")
        finally:
            return response
