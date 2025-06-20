from config import INCORRECT_BEARER_TOKEN

import pytest

pytestmark = pytest.mark.car


def test_create_car_without_authorization_header(setup_not_auth):
    user, house, garage, car = setup_not_auth
    response = car.create_car(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code


def test_create_car_with_incorrect_authorization_header(setup_not_auth):
    user, house, garage, car = setup_not_auth
    user.headers = {"Authorization": f"Bearer {INCORRECT_BEARER_TOKEN}"}
    response = car.create_car(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code
