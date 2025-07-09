from locust import HttpUser, constant

import os

from testing.locust.user_behavior import UserBehavior


class MyUser(HttpUser):
    wait_time = constant(1)
    host = os.getenv("API_BASE_URL", "http://127.0.0.1:8000/")
    tasks = [UserBehavior]
