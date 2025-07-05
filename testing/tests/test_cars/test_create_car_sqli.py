from app.config import SQLI_DATA
from testing.utils.generators.car_generator import generate_car

import pytest

pytestmark = [pytest.mark.car, pytest.mark.xfail, pytest.mark.sqli]


def test_create_car_successful_without_garage_relation_model_sqli(setup):
    user, house, garage, car = setup
    car.car_obj = generate_car()
    car.car_obj["model"] = SQLI_DATA

    response = car.create_car(user)
    expected_status_code = 401

    assert expected_status_code == response.status_code


def test_create_car_successful_with_garage_relation_garage_id_sqli(setup):
    user, house, garage, car = setup
    car.car_obj = generate_car()
    car.car_obj["garage_id"] = SQLI_DATA

    response = car.create_car(user)
    expected_status_code = 401

    assert expected_status_code == response.status_code
