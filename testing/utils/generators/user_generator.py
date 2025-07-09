from faker import Faker

import random
import string
import time

fake = Faker()


def generate_user(password_length: int):
    timestamp = int(time.time() * 1000)
    random_part = random.randint(1000, 9999)
    username = f"{fake.user_name()}_{timestamp}_{random_part}"
    password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))

    result_user = {"username": username, "email": f"{username}@example.com", "password": password}

    return result_user
