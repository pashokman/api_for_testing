from faker import Faker

import random
import string

fake = Faker()


def generate_user(password_length: int):
    username = fake.user_name()
    password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))

    result_user = {"username": f"{username}", "email": f"{username}@example.com", "password": f"{password}"}

    return result_user
