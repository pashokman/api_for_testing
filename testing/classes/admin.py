from app.config import ADMIN_PASSWORD
from testing.classes.user import User


class Admin(User):

    def __init__(self, headers=None, request=None):
        super().__init__(headers=headers, request=request)
        self.bearer_token = None
        self.user_id = None
        self.username = "admin"
        self.password = ADMIN_PASSWORD

    def auth(self):
        response = None
        try:
            if self.logger:
                self.logger.info(f"Authenticating admin")
            json = {"username": f"{self.username}", "password": f"{self.password}"}
            response = self.post(endpoint="auth/login", json=json)
            if response.status_code == 200:
                self.bearer_token = response.json()["access_token"]
                self.headers = {"Authorization": f"Bearer {self.bearer_token}"}
                self.logger.info(f"Authenticating admin, response json: {response.json()}")
                self.user_id = self.get_me().json()["id"]
            else:
                self.logger.error(f"Authenticating admin, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in auth: {e}")
        finally:
            return response

    def get_me(self):
        response = None
        try:
            if self.logger:
                self.logger.info(f"Getting admin profile")
            response = self.get(endpoint="users/me", headers=self.headers)
            if response.status_code == 200:
                self.logger.info(f"Getting admin profile, response json: {response.json()}")
            else:
                self.logger.error(f"Getting admin profile, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in get_me: {e}")
        finally:
            return response
