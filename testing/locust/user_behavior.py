import json
import os

from locust import SequentialTaskSet, task
from locust.exception import StopUser

from testing.utils.generators.user_generator import generate_user
from testing.utils.generators.house_generator import generate_house
from testing.utils.logs.locust_main_logger import Logger
from testing.utils.logs.locust_response_err_log import response_err_log

# clear log files
for log_file in ["locust_main.log", "locust_only_error.log"]:
    if os.path.exists(log_file):
        with open(log_file, "w"):
            pass

log = Logger(log_name="UserBehavior")
UserLog = log.get_logger()
UserLog.propagate = False


class UserBehavior(SequentialTaskSet):

    def on_start(self):
        self.user_obj = None
        self.user_id = None
        self.user_token = None
        self.house_ids = []

    def on_stop(self):
        self.user_obj = None
        self.user_id = None
        self.user_token = None
        self.house_ids = []

    def create_user(self):
        self.user_obj = generate_user(password_length=8)
        with self.client.post(
            "/users/register", data=json.dumps(self.user_obj), name="001. Create user", catch_response=True
        ) as response:
            if response.status_code == 200:
                self.user_id = response.json()["id"]
                UserLog.info(f'User created, id - "{self.user_id}"')
            elif response.status_code == 401 and "Username already taken" in response.text:
                UserLog.warning("Username already taken. Stopping this user.")
                raise StopUser()
            else:
                response_err_log(response)
                raise StopUser()

    def auth_user(self):
        json_data = {"username": f"{self.user_obj.get('username')}", "password": f"{self.user_obj.get('password')}"}
        with self.client.post(
            "/auth/login", data=json.dumps(json_data), name="002. Authorize user", catch_response=True
        ) as response:
            if response.status_code == 200:
                self.user_token = response.json()["access_token"]
                self.headers = {"Authorization": f"Bearer {self.user_token}"}
                UserLog.info(f'User authorized, id - "{self.user_id}", token - "{self.user_token}"')
            else:
                response_err_log(response)
                raise StopUser()

    def create_houses(self, house_count: int = 2):
        for i in range(house_count):
            with self.client.post(
                "/houses",
                data=json.dumps(generate_house()),
                name="002. Create house",
                headers=self.headers,
                catch_response=True,
            ) as response:
                if response.status_code == 200:
                    house_id = response.json()["id"]
                    self.house_ids.append(house_id)
                    UserLog.info(f'House created, house_id - "{house_id}", token - "{self.user_token}"')
                else:
                    response_err_log(response)

    @task
    def test_scenario1(self):
        """
        Scenario description:
        001. Create user account
        002. Authorize user account
        003. Create N houses with user account token (N >= 2, default = 2)
        004. Create M garages with user account token
         - K garages belongs to house1 (K >= 1, default = 1)
         - L garages belongs to house2 (L >= 1, default = 1)
         - P garages without house relation (P = M - K - L). If M = 2, K = 1 and L = 1, P = 0. If M = 4, K = 1 and L = 1, P = 2
        005. Create W cars with user account token
         - X cars belongs to garage1 (X >= 1, default = 1)
         - Y cars belongs to garage2 (Y >= 1, default = 1)
         - Z cars without garage relation (Z = W - X - Y). If W = 2, X = 1 and Y = 1, Z = 0. If W = 4, X = 1 and Y = 1, Z = 2
        006. Create driver licence with user account token
        """
        self.create_user()
        self.auth_user()
        self.create_houses()  # add getting variable from console

        self.interrupt()
