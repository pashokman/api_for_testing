from locust import HttpUser, constant

import os

from testing.locust.user_scenario3 import UserScenario


class MyUser(HttpUser):
    wait_time = constant(1)
    host = os.getenv("API_BASE_URL", "http://127.0.0.1:8000/")
    tasks = [UserScenario]
