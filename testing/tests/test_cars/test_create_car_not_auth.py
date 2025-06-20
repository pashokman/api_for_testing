from config import INCORRECT_BEARER_TOKEN
from testing.classes.car import Car
from testing.classes.user import User

import pytest


@pytest.fixture()
def setup_not_auth():
    user = User()
    user.create_user()
    car = Car()
    yield user, car


def test_create_car_without_authorization_header(setup_not_auth):
    user, car = setup_not_auth
    response = car.create_car(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code


def test_create_car_with_incorrect_authorization_header(setup_not_auth):
    user, car = setup_not_auth
    user.headers = {"Authorization": f"Bearer {INCORRECT_BEARER_TOKEN}"}
    response = car.create_car(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code
